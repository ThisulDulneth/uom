from dataclasses import dataclass
from pathlib import Path

# Define base paths relative to the project root
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"

@dataclass(frozen=True) # frozen=True makes the instance immutable
class LabConfig:
    """
    Configuration settings for the Signal Log Analyzer lab.
    """
    # File Paths (using pathlib.Path for robustness)
    signal_path: Path = DATA_DIR / "signal.csv"
    features_path: Path = OUTPUT_DIR / "features.csv"
    
    # Processing Parameters
    CHUNK_SIZE: int = 500
    WINDOW_SIZE: int = 10
    
    # Decorator/Context Manager Parameters
    SLOW_THRESHOLD_MS: float = 20.0 # Time in milliseconds for slow call warning

# Global instance of the configuration
CONFIG = LabConfig()