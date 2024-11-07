#!/bin/bash

curl https://api.x.ai/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer PUT_API_KEY_HERE" -d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "Testing. Just say hi and hello world and who you are and nothing else."
    }
  ],
  "model": "grok-beta",
  "stream": false,
  "temperature": 0
}'
