#!/bin/bash
# displays body size of HTTP response in bytes
content_length=$(curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}')
echo "Body size of HTTP response: $content_length bytes"
