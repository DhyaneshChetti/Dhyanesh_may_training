import pandas as pd
from pathlib import Path

def reduce_dataset():
    input_path = Path('data/interim/jobs_clean.csv')
    if not input_path.exists():
        print(f"File not found at {input_path}")
        return
    print("Loading 1L+ dataset...")
    df = pd.read_csv(input_path)
    df_reduced = df.sample(n=10000, random_state=42)
    output_path = Path('data/interim/jobs_reduced.csv')
    df_reduced.to_csv(output_path, index=False)
    print(f"Dataset successfully reduced to {len(df_reduced)} rows.")

if __name__ == "__main__":
    reduce_dataset()
