# Troubleshooting Guide

## Common Issues

### "Connection refused" (Ollama)
```bash
# Start Ollama server
ollama serve
```

### "Model not found"
```bash
# Pull model
ollama pull qwen2.5-coder:7b
```

### "API key not found"
```bash
# Check .env file
cat .env

# Reload
source .env
```

### Empty responses
- Check model is running
- Increase max_tokens
- Try different temperature

### Slow responses
- Use smaller model
- Check system resources
- Try local Ollama instead of cloud

## Debug Mode
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```
