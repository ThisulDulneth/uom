import typer
import numpy as np
import logging
import csv
from typing import List, Dict, Any
from pathlib import Path

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger("ipylab")

# --- Import all core components ---
# Assuming the user has moved the ipylab folder to the root and the imports work
from ipylab.config import CONFIG, LabConfig
from ipylab.io import load_signal_csv, save_features_csv
from ipylab.generators import chunks, moving_average, moving_median
from ipylab.features import feature_vector
from ipylab.context import timer, suppress_and_log
from ipylab.decorators import timed
from ipylab.vectorize import python_rms, numpy_rms

# --- Typer App Setup ---
app = typer.Typer(help="Signal Log Analyzer Toolkit.")
signal_app = typer.Typer(help="Commands for signal processing.")
app.add_typer(signal_app, name="signal")

# --- Helper Function for Pipeline Logic ---

@timed(threshold_ms=CONFIG.SLOW_THRESHOLD_MS)
def process_chunk(chunk_array: np.ndarray, avg_gen, med_gen) -> Dict[str, Any]:
    """
    Applies statistical analysis and feature extraction to a single chunk.
    This function is decorated to log its execution time.
    """
    
    # 1. Extract Vectorized Features
    rms, zc, ptp, mad = feature_vector(chunk_array)
    
    # 2. Apply Stateful Moving Statistics
    last_avg = None
    last_med = None
    for sample in chunk_array:
        # Send data to coroutine generators
        last_avg = avg_gen.send(float(sample))
        last_med = med_gen.send(float(sample))
    
    return {
        "chunk_size": chunk_array.size,
        "rms": rms,
        "zero_crossings": zc,
        "peak_to_peak": ptp,
        "mad": mad,
        "moving_avg_last": last_avg,
        "moving_med_last": last_med,
    }


# --- Typer Commands ---

@signal_app.command("run-pipeline")
def run_pipeline(
    input_path: Path = typer.Option(
        CONFIG.signal_path, 
        "--input", 
        "-i", 
        help="Path to the input signal CSV file."
    ),
    output_path: Path = typer.Option(
        CONFIG.features_path, 
        "--output", 
        "-o", 
        help="Path to save the output features CSV."
    ),
):
    """
    Loads data, streams in chunks, extracts features, and saves the result.
    Uses context managers for timing and error suppression.
    """
    
    logger.info(f"--- Starting Signal Analysis Pipeline ---")
    logger.info(f"Input: {input_path}, Output: {output_path}")
    logger.info(f"Chunk Size: {CONFIG.CHUNK_SIZE}, Window Size: {CONFIG.WINDOW_SIZE}")

    with timer("Full Pipeline Execution"):
        
        # 1. Load Data
        signal_array = None
        # Use suppress_and_log for robust file loading
        with suppress_and_log(FileNotFoundError):
            signal_array = load_signal_csv(input_path)
            
        if signal_array is None:
            logger.error("Data loading failed or file was empty. Exiting.")
            return

        logger.info(f"Total signal points loaded: {signal_array.size}")
        
        feature_rows = []
        
        # Initialize stateful generators (coroutines)
        avg_gen = moving_average(CONFIG.WINDOW_SIZE)
        med_gen = moving_median(CONFIG.WINDOW_SIZE)
        # Prime the generators
        next(avg_gen)
        next(med_gen)

        # 2. Process in Chunks
        for i, chunk in enumerate(chunks(signal_array, CONFIG.CHUNK_SIZE)):
            chunk_array = np.array(chunk)
            
            # Apply processing 
            try:
                row = process_chunk(chunk_array, avg_gen, med_gen)
                row["chunk_index"] = i
                feature_rows.append(row)
            except Exception as e:
                logger.error(f"Processing failed for chunk {i}: {e}. Skipping chunk.")
        
        # 3. Save Results
        save_features_csv(output_path, feature_rows)
        logger.info(f"Pipeline completed successfully. Features saved to {output_path}")


@app.command("profile")
def profile_commands():
    """
    Runs RMS calculation using both Python and NumPy for performance comparison.
    """
    logger.info("--- Starting RMS Profiling ---")
    
    # Create a large test array
    N = 1000000
    test_array = np.random.randn(N)
    test_list = test_array.tolist()
    
    print(f"\nComparing RMS calculation speed on {N:,} data points...")
    
    @timed()
    def profile_python_rms(data):
        return python_rms(data)

    @timed()
    def profile_numpy_rms(data):
        return numpy_rms(data)

    profile_python_rms(test_list)
    profile_numpy_rms(test_array)
    
    print("-" * 30)
    print("Profiling finished. Check logs for timing comparison.")


@app.command("generate-data")
def generate_data_cli(
    path: Path = typer.Option(
        CONFIG.signal_path, 
        "--output", 
        "-o", 
        help="Path to save the generated signal CSV file."
    )
):
    """
    Generates the synthetic signal dataset and saves it to a CSV file.
    """
    logger.info("--- Generating Synthetic Signal Data ---")
    
    # Configuration for data generation
    np.random.seed(42)
    N = 200000
    time_steps = np.arange(N)
    
    # Signal: sine wave + random noise
    signal = 5 * np.sin(0.01 * time_steps) + 1 * np.random.randn(N)
    
    # Ensure parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)

    try:
        # --- This is the complete and correct I/O logic ---
        np.savetxt(path, signal, delimiter=",", header="", comments="")
        logger.info(f"Successfully generated and saved {N:,} data points to: {path}")
    except Exception as e:
        logger.error(f"Failed to save data: {e}")


# --- Entry Point ---
if __name__ == "__main__":
    app()