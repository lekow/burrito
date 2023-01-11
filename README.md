# 🌯 BURRito (BUrp Request Replayer)
🚧 This tool is still under development, stay tuned!

## Description
🐍 This tool was written in Python 3.

## 🌟 Current Features
- 🍪 Supports cookies
- 🔧 Supports HTTP/2
- 🔍 Supports filtering based on HTTP methods (more comming soon)
- 🌐 Supports proxies

## 🔥 Comming Soon
- 🔍 More filters, such as filtering based on status code, length, etc.
- 🗒️ Saving output to file
- ⚡ Concurrency

## ❓ Help
```
usage: burrito [-h] [-u URL] [-c COOKIES [COOKIES ...]] -f FILENAME [-hv {1.1,2}] [-p PROXIES [PROXIES ...]] -m METHODS [METHODS ...]

BURRito - BUrp Request Replayer v0.1

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     The target URL to use (skips all others)
  -c COOKIES [COOKIES ...], --cookies COOKIES [COOKIES ...]
                        The cookies to use
  -f FILENAME, --filename FILENAME
                        The file to use
  -hv {1.1,2}, --http-version {1.1,2}
                        The HTTP version to use (default: 1.1)
  -p PROXIES [PROXIES ...], --proxies PROXIES [PROXIES ...]
                        The proxy to use
  -m METHODS [METHODS ...], --methods METHODS [METHODS ...]
                        The HTTP methods to use
```
