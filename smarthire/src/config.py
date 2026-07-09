from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_RAW = BASE_DIR / "data/raw"
DATA_INT = BASE_DIR / "data/interim"
DATA_PRO = BASE_DIR / "data/processed"
MODELS_DIR = BASE_DIR / "models"

for d in [DATA_PRO, MODELS_DIR]: d.mkdir(parents=True, exist_ok=True)