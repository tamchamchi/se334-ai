# SE334 Multilingual Sentiment Analysis API

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0+-00a393.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An advanced multilingual sentiment analysis API built with FastAPI and Transformers, supporting both Vietnamese and English languages.

## 🚀 Key Features

- **Multilingual Sentiment Analysis**: Support for Vietnamese and English
- **RESTful API**: Built with FastAPI, fast and modern
- **Advanced AI Models**: Using Transformers and PyTorch
- **Automatic Language Detection**: No need to specify language beforehand
- **Auto-generated API Documentation**: Swagger UI and ReDoc
- **Easy to Extend**: Modular architecture and clean code

## 📋 System Requirements

- Python 3.11 or higher
- RAM: Minimum 4GB (recommended 8GB+)
- Storage: 2GB free space for models
- GPU (optional): CUDA-compatible for optimal performance

## 🛠️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/anhndt/se334-ai.git
cd se334-ai
```

### 2. Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Or using conda
conda create -n se334-ai python=3.11
conda activate se334-ai
```

### 3. Install Dependencies

```bash
# Basic installation
pip install -e .

# Or install with development tools
pip install -e ".[dev]"

# Or install with jupyter support
pip install -e ".[jupyter]"

# Install everything
pip install -e ".[dev,docs,jupyter]"
```

### 4. Install spaCy Models (if needed)

```bash
python -m spacy download en_core_web_sm
python -m spacy download vi_core_news_lg
```

## 🚀 Running the API

### Start Development Server

```bash
# Method 1: Using uvicorn directly
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

# Method 2: Using console script
sentiment-api

# Method 3: Running from Python
python -m api.main
```

The API will be available at: http://localhost:8000

### API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## 📖 Usage

#### Analyze Single Text

```http
POST /api/v1/predict
Content-Type: application/json

{
  "texts": [
    "I absolutely love the new design of this app!",
    "The customer service was disappointing.",
    "The weather is fine, nothing special.",
    "cho mình xin bài nhạc tên là gì với ạ",
    "uớc gì sau này về già vẫn có thể như cụ này :))",
    "Mày nhìn cái chó gì :)))"
  ]
}

```

**Response:**
```json
{
  "results": [
    {
      "text": "I absolutely love the new design of this app!",
      "label": "Positive"
    },
    {
      "text": "The customer service was disappointing.",
      "label": "Negative"
    },
    {
      "text": "The weather is fine, nothing special.",
      "label": "Neutral"
    },
    {
      "text": "cho mình xin bài nhạc tên là gì với ạ",
      "label": "Neutral"
    },
    {
      "text": "uớc gì sau này về già vẫn có thể như cụ này :))",
      "label": "Neutral"
    },
    {
      "text": "Mày nhìn cái chó gì :)))",
      "label": "Negative"
    }
  ]
}
```

## 🔧 Configuration

### Config Files

- `config/config.yaml`: General application configuration
- `config/model_config.yaml`: Machine learning model configuration

### Model Configuration Example

The `model_config.yaml` file contains detailed configurations for different sentiment analysis models:

```yaml
# Default settings
default:
  model_name: "multilingual_predictor"
  device: "auto"
  batch_size: 32
  max_length: 512

# Model configurations
predictor:
  multilingual:
    model_name: "tabularisai/multilingual-sentiment-analysis"
    device: "cuda"
    seed: 42
```
## 📁 Project Structure

```
se334-ai/
├── api/                    # FastAPI application
│   ├── main.py            # API entry point
│   └── schema/            # Pydantic schemas
├── src/                   # Core source code
│   ├── predictor/         # Sentiment prediction models
│   ├── preprocessor/      # Text preprocessing
│   └── utils/             # Utilities
├── config/                # Configuration files
├── data/                  # Training data
├── models/                # Trained models
├── notebooks/             # Jupyter notebooks
├── tests/                 # Unit tests
├── requirements.txt       # Dependencies
├── setup.py              # Package setup
└── README.md             # This file
```

## 🚀 Deployment Options

### 🔥 Kaggle Deployment (Recommended for Testing)


#### 📓 Quickstart Notebook (RECOMMENDED)

📎 **Notebook**: [`./notebooks/se334_ai_kaggle_api.ipynb`](./notebooks/se334_ai_kaggle_api.ipynb)

> A complete step-by-step Kaggle notebook to clone, install, deploy, and test the API within 3 minutes.

---

Deploy and test your API quickly on Kaggle with ngrok tunneling:

#### Step 1: Create Kaggle Notebook

1. Go to [Kaggle Notebooks](https://www.kaggle.com/code)
2. Create a new notebook
3. Enable Internet access in notebook settings

#### Step 2: Setup Code

```python
# Clone the repository
!git clone https://github.com/anhndt/se334-ai.git
%cd /kaggle/working/se334-ai

# Install the package
!pip install -e .

# Install ngrok for public URL
!pip install pyngrok

# Add your ngrok authtoken (get from https://ngrok.com/)
!ngrok config add-authtoken "YOUR_NGROK_TOKEN_HERE"
```

#### Step 3: Deploy API

```python
from pyngrok import ngrok
import uvicorn
import threading

# Create public tunnel
public_url = ngrok.connect(8000)
print("🔥 Public URL:", public_url)

# Run FastAPI in background
def run_api():
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000)

threading.Thread(target=run_api).start()
```

#### Step 4: Test the API

Access your API via:
- **Swagger UI**: `https://<your-ngrok-url>.ngrok-free.app/docs`
- **API Endpoint**: `https://<your-ngrok-url>.ngrok-free.app/predict`

**Test with curl:**
```bash
curl -X POST "https://<your-ngrok-url>.ngrok-free.app/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "texts": [
         "I love this product!",
         "Dịch vụ rất tốt!",
         "The service was terrible."
       ]
     }'
```

**Test with Python:**
```python
import requests

# Use your ngrok URL
base_url = "https://your-ngrok-url.ngrok-free.app"

response = requests.post(
    f"{base_url}/predict",
    json={
        "texts": [
            "This is amazing!",
            "Sản phẩm tuyệt vời!",
            "Could be better..."
        ]
    }
)

print("✅ API Response:")
print(response.json())
```
