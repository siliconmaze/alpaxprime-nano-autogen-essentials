# Ollama Walkthrough - AutoGen Labs

## Provider Overview
- **Model Used**: qwen2.5-coder:7b
- **Type**: Local / Self-hosted
- **API Endpoint**: http://localhost:11434/v1
- **API Key**: Not required (local)

## Lab Results

### Lab 1: Hello AutoGen ✅
**Status**: Verified Working
**Configuration**:
```python
config_list = [{
    "model": "qwen2.5-coder:7b",
    "base_url": "http://localhost:11434/v1",
    "api_key": "ollama",
    "api_type": "openai"
}]
```
**Key Learnings**:
- Ollama requires OpenAI-compatible API wrapper
- Model must be explicitly pulled before use
- Response times vary based on hardware

### Lab 2: Agent Conversations ✅
**Status**: Verified Working
**Pattern**: Two-agent conversation with assistant and user proxy
**Configuration**: Same as Lab 1
**Key Learnings**:
- Conversations require UserProxyAgent paired with AssistantAgent
- Context maintained across turns
- Streaming supported for real-time output

### Lab 3: Tools & Functions ✅
**Status**: Verified Working  
**Pattern**: Register custom Python functions
**Key Learnings**:
- Use `register_for_execution()` and `register_for_llm()`
- Tool calls return structured JSON
- Can chain multiple tools

### Lab 4: GroupChat ✅
**Status**: Verified Working
**Pattern**: Multiple agents in group conversation
**Key Learnings**:
- GroupChatManager orchestrates
- Speaker selection strategies available
- Max rounds prevent infinite loops

### Lab 5: Human-in-the-Loop ✅
**Status**: Verified Working
**Pattern**: Interactive human approval
**Key Learnings**:
- `human_input_mode` controls interaction
- "ALWAYS" = always ask humans
- "TERMINATE" = ask at termination

### Lab 6: Real-World Apps ✅
**Status**: Verified Working
**Pattern**: Multi-step workflows
**Key Learnings**:
- Sequential chats pass context
- Nested chats for delegation
- Error handling critical

### Lab 7: Production Patterns ✅
**Status**: Verified Working
**Pattern**: Scaling & monitoring
**Key Learnings**:
- Logging essential for debugging
- Retry logic for API failures
- Session management important

## Pros & Cons

### Pros
- ✅ Zero API costs after initial setup
- ✅ Complete privacy (data never leaves machine)
- ✅ No rate limits
- ✅ Offline capability

### Cons
- ❌ Requires powerful hardware (8GB+ RAM recommended)
- ❌ Limited model selection compared to cloud
- ❌ Slower inference on consumer hardware
- ❌ No built-in embeddings without additional setup

## Recommendations

1. **Best for**: Development, testing, privacy-sensitive work
2. **Hardware**: M1/M2/M3 Mac or Linux with 16GB RAM
3. **Model choice**: qwen2.5-coder excellent for code tasks
4. **Production**: Use cloud providers for scale
