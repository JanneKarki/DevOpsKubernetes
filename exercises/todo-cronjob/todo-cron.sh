#!/bin/sh
set -e

URL=$(curl -s -I https://en.wikipedia.org/wiki/Special:Random | grep -i location | awk '{print $2}' | tr -d '\r')

echo "Read $URL"
