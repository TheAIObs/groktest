# Grok API Testing Scripts

>  For a detailed walkthrough and explanation, check out my blog post: [Getting Started with xAI's Grok API](https://www.theaiobserver.com/how-to-claim-your-free-25-monthly-xai-api-credits-for-grok2-a-complete-guide/)

This repository contains various scripts to interact with the xAI Grok-beta API. These scripts demonstrate different approaches to using the API, from basic testing to more advanced interactive usage.

## Prerequisites

- xAI API Key (Get it from [console.x.ai](https://console.x.ai))
- Python 3.7+ (for Python scripts)
- curl (for shell script)
- OpenAI Python package (`pip install openai`)

## Available Scripts

### 1. testgrok.sh
A basic shell script to test the Grok API using curl.

```bash
# Make executable
chmod +x testgrok.sh

# Edit script to add your API key
nano testgrok.sh

# Run
./testgrok.sh
```

### 2. testgrok_direct.py
A simple Python script with the API key directly in the code (for quick testing only).

```python
# Edit script to add your API key
nano testgrok_direct.py

# Run
python testgrok_direct.py
```

:warning: **Note:** This method is not recommended for production use. Only use for quick local testing.

### 3. testgrok_env.py
A Python script that uses environment variables for the API key (recommended approach).

```bash
# Set API key in environment
export XAI_API_KEY=your_api_key_here

# Run script
python testgrok_env.py
```

### 4. chatgrok.py
An Python script with command-line arguments support.

```bash
# Set API key in environment
export XAI_API_KEY=your_api_key_here

# Basic usage (with default system prompt)
python chatgrok.py "What is the meaning of life?"

# Advanced usage (with custom system prompt)
python chatgrok.py -s "You are a helpful math tutor" "Explain calculus"
```

## Script Comparison

| Script | Language | API Key Method | Features |
|--------|----------|----------------|----------|
| testgrok.sh | Shell | Direct in script | Basic API test |
| testgrok_direct.py | Python | Direct in code | Basic API test |
| testgrok_env.py | Python | Environment variable | Basic API test |
| chatgrok.py | Python | Environment variable | Custom prompts |

## Security Best Practices

1. Always use environment variables for API keys in production
2. Never commit API keys to version control
3. Keep backup copies of your key in a secure location
4. Regularly monitor your API usage through the console

## Environment Setup

### Setting Environment Variables

**Linux/macOS:**
```bash
export XAI_API_KEY=your_api_key_here
```

**Windows Command Prompt:**
```cmd
set XAI_API_KEY=your_api_key_here
```

**Windows PowerShell:**
```powershell
$env:XAI_API_KEY = "your_api_key_here"
```
*Remember to replace 'your_api_key_here' with your actual xAI API key when using these scripts.*

### Python Dependencies

Install required packages:
```bash
pip install openai
```

## Troubleshooting

### Common Issues

1. **API Key Not Found**
   - Check if environment variable is set correctly
   - Verify API key format

2. **Script Permissions (Shell Script)**
   - Ensure script is executable (`chmod +x testgrok.sh`)

3. **Python Import Errors**
   - Verify OpenAI package is installed
   - Check Python version (3.7+ required)

### Getting Help

- Check the [xAI Documentation](https://console.x.ai/docs)
- Review API usage in the [xAI Console](https://console.x.ai)
- Join the xAI developer community

## Additional Resources

- [Detailed Blog Tutorial: Getting Started with xAI's Grok API](https://www.theaiobserver.com/how-to-claim-your-free-25-monthly-xai-api-credits-for-grok2-a-complete-guide/)
- [Official xAI Documentation](https://console.x.ai/docs)
- [xAI Console](https://console.x.ai)

## Contributing

Feel free to submit issues and enhancement requests!

## License

These scripts are released under the MIT License. See [LICENSE](LICENSE) file for details.

## Acknowledgments

- xAI Team for providing the Grok API
- OpenAI for the Python client library

---
