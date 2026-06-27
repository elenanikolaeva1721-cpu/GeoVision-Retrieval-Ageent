# 🌍 GeoVision Retrieval Agent

## Download the Dataset

This project uses the EuroSAT RGB dataset available on Kaggle: https://www.kaggle.com/datasets/waseemalastal/eurosat-rgb-dataset

    Download the EuroSAT RGB dataset from Kaggle.
    Extract the archive.
    Create a folder named data in the project root.
    Copy the dataset into the data/ folder.

The project directory should look like:

GeoVision-Retrieval-Agent/
```text
├── data/EuroSAT/
│        ├── AnnualCrop/
│        ├── Forest/
│        ├── HerbaceousVegetation/
│        ├── Highway/
│        ├── Industrial/
│        ├── Pasture/
│        ├── PermanentCrop/
│        ├── Residential/
│        ├── River/
│        └── SeaLake/
```
The script build_embeddings.py uses the images stored in the data/ directory to generate the embedding database (embeddings.npy, labels.npy, and paths.npy).
- Cloud deployment
