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

### Environment Variables

Create a `.env` file in the root directory:

```env
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=True

# Model Configuration
DEFAULT_MODEL=multilingual_predictor
MODEL_CACHE_DIR=./models
ENABLE_GPU=True

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
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

## 🚀 Production Deployment

### Docker (Recommended)

```bash
# Build image
docker build -t se334-sentiment-api .

# Run container
docker run -p 8000:8000 se334-sentiment-api
```

### Docker Compose

```yaml
version: '3.8'
services:
  sentiment-api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - API_HOST=0.0.0.0
      - API_PORT=8000
    volumes:
      - ./models:/app/models
```

### systemd Service

```bash
# Copy service file
sudo cp deployment/sentiment-api.service /etc/systemd/system/

# Enable and start
sudo systemctl enable sentiment-api
sudo systemctl start sentiment-api
```

### Nginx Reverse Proxy

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 🎯 Performance Optimization

### GPU Acceleration

```python
# Enable GPU in config
ENABLE_GPU=True
CUDA_VISIBLE_DEVICES=0
```

### Model Caching

```python
# Models are automatically cached after first load
MODEL_CACHE_DIR=./models
CACHE_MODELS=True
```

### Batch Processing

For better performance with multiple texts, use the batch endpoint:

```python
# Instead of multiple single requests
texts = ["text1", "text2", "text3"]
response = requests.post(f"{base_url}/api/v1/predict/batch", json={"texts": texts})
```

## 🔍 Troubleshooting

### Common Issues

1. **Out of Memory Error**
   ```bash
   # Reduce batch size or use CPU
   export CUDA_VISIBLE_DEVICES=""
   ```

2. **Model Download Issues**
   ```bash
   # Manual model download
   python -c "from transformers import AutoTokenizer, AutoModel; AutoTokenizer.from_pretrained('model_name'); AutoModel.from_pretrained('model_name')"
   ```

3. **Port Already in Use**
   ```bash
   # Use different port
   uvicorn api.main:app --port 8001
   ```

## 📈 Monitoring

### Health Checks

```bash
# API health
curl http://localhost:8000/api/v1/health

# Detailed status
curl http://localhost:8000/api/v1/status
```

### Logging

Logs are available in:
- Console output (development)
- `logs/app.log` (production)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run pre-commit hooks
pre-commit install

# Run tests before committing
pytest
black .
flake8
```

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙏 Acknowledgments

- **Author**: Nguyễn Duy Tâm Anh
- **Email**: anhndt.work@gmail.com
- **GitHub**: https://github.com/anhndt/se334-ai

## 📚 References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Transformers Documentation](https://huggingface.co/docs/transformers/)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [spaCy Documentation](https://spacy.io/)

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/anhndt/se334-ai/issues) page
2. Create a new issue with detailed information
3. Contact the author via email

---

⭐ **If you find this project helpful, please give it a star!** ⭐
