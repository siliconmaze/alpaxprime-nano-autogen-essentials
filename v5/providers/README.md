# Provider Guides

## Priority: Ollama First

This course is designed to work **without any API keys** using Ollama.

---

## Ollama (Recommended)

### Installation
```bash
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai/download
```

### Pull Models
```bash
ollama pull qwen2.5-coder:7b
ollama pull llama3
ollama pull mistral
```

### Start Server
```bash
ollama serve
```

### Test
```bash
curl http://localhost:11434/api/tags
```

---

## DeepSeek (Optional)

### Get API Key
1. Go to https://platform.deepseek.com
2. Sign up for free account
3. Create API key
4. Add to .env: `DEEPSEEK_API_KEY=your-key`

### Model: deepseek-chat

---

## MiniMax (Optional)

### Get API Key
1. Go to https://platform.minimax.io
2. Sign up
3. Get API key
4. Add to .env: `MINIMAX_API_KEY=your-key`

### Model: MiniMax-Text-01

---

## Comparison

| Provider | Cost | Setup | Best For |
|----------|------|-------|----------|
| Ollama | Free | Medium | Learning, Development |
| DeepSeek | Cheap | Easy | Production |
| MiniMax | Cheap | Easy | Long Context |
