import numpy as np
import csv
from pathlib import Path
from typing import List, Dict, Any

def load_signal_csv(path: Path) -> np.ndarray:
    """
    Loads signal data from a CSV file into a NumPy array using pathlib.
    """
    if not path.exists():
        raise FileNotFoundError(f"Signal file not found at: {path}")

    # Use numpy's loadtxt for efficient CSV reading into an array
    # delimiter="," is assumed for standard CSV
    # unpack=True loads data into separate arrays if multiple columns, 
    # but we assume 1D signal here, so we keep the standard behavior.
    return np.loadtxt(path, delimiter=",")

def save_features_csv(path: Path, rows: List[Dict[str, Any]]):
    """
    Saves a list of feature dictionaries to a CSV file using pathlib.
    """
    if not rows:
        return

    # Ensure the output directory exists
    path.parent.mkdir(parents=True, exist_ok=True)

    # Use keys from the first dictionary as the header
    fieldnames = list(rows[0].keys())

    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(rows)