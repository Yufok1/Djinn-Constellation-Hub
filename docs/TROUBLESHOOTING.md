# Troubleshooting Guide

## Common Issues

### Ollama not found
- Ensure Ollama is installed and in your PATH
- Run `ollama --version` to test

### Model build fails
- Check RAM and disk space
- Ensure all model files are present

### Agents not responding
- Check logs in `memory_bank/`
- Restart the hub

### Menu or analytics not updating
- Delete corrupted `user_preferences.json` or conversation history
