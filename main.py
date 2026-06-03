import os

print("Starting Multi-City Weather Data Pipeline...\n")

os.system("python scripts/extract.py")
os.system("python scripts/transform.py")
os.system("python scripts/load.py")
os.system("python scripts/analysis.py")

print("\nPipeline Completed Successfully!")