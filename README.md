# 🌍 GeoVision Retrieval Agent

![GeoVision Retriaval Agent](GeoVision_banner.jpg)

An AI-powered multi-agent application for semantic retrieval of Earth observation imagery.

## Overview

GeoVision Retrieval Agent retrieves visually similar satellite scenes instead of performing traditional image classification.

Users upload an RGB satellite image, and the system searches a reference database built from the **EuroSAT RGB dataset (Kaggle)** using deep visual embeddings. The application then retrieves the five most similar scenes and provides an AI-generated interpretation with a confidence estimate.

This project was developed for the **Kaggle AI Agents: Intensive Vibe Coding Capstone Project**.

## Features

- Semantic image retrieval
- Multi-agent architecture
- AI-generated scene interpretation
- Confidence estimation
- Interactive Streamlit interface
- Fast cosine similarity search

## Multi-Agent Architecture

### Retrieval Agent

- Image preprocessing
- Embedding generation (ResNet18)
- Cosine similarity search
- Top-5 retrieval

### Analyst Agent

- Confidence estimation
- Scene interpretation
- Retrieval consistency analysis
- Natural-language summary generation

## Supported Input

- RGB satellite images
- JPG
- JPEG
- PNG

The current version is optimized for images with visual characteristics similar to the EuroSAT RGB dataset.

## Output

For each uploaded image, the application returns:

- Top-5 visually similar satellite scenes
- Similarity scores
- Predicted land-cover category
- Confidence level
- AI-generated interpretation

## Dataset

Reference database: **EuroSAT RGB Dataset (Kaggle)**

Land-cover classes:
- AnnualCrop
- Forest
- HerbaceousVegetation
- Highway
- Industrial
- Pasture
- PermanentCrop
- Residential
- River
- SeaLake

## AI Concepts Demonstrated

- **Agent / Multi-agent system (ADK)**
- **Deployability**
- **Agent skills**

## Technologies

- Python
- Streamlit
- PyTorch
- torchvision
- NumPy
- scikit-learn
- Pillow

## Project Structure

```text
GeoVision-Retrieval-Agent/
├── app.py
├── agent.py
├── build_embeddings.py
├── data/
├── banner/
├── weights/
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

```bash
pip install -r requirements.txt
```

Download the pretrained ResNet18 weights and place `resnet18-f37072fd.pth` inside the `weights/` directory.

## Run

```bash
streamlit run app.py
```

## Current Limitations

The current version is optimized for the EuroSAT RGB dataset.

Some visually similar classes (for example River and Highway) may occasionally produce ambiguous retrieval results.

## Future Work

- Larger reference databases
- Additional Earth observation datasets
- Aerial imagery support
- Expert AI agents
- Improved semantic interpretation
- Cloud deployment
