# 🌯 BURRito (BUrp Request Replayer)
🚧 This tool is still under development, stay tuned!

## Description
🐍 This tool was written in Python 3.

## 🌟 Current Features
- 🍪 Supports cookies
- 🔧 Supports HTTP/2
- 🔍 Supports filtering based on URL, HTTP methods, status code and response length
- 🌐 Supports proxies

## 🔥 Comming Soon
- 🗒️ Saving output to file
- ⚡ Concurrency

## ❓ Help
```
usage: burrito [-h] [-c COOKIES [COOKIES ...]] -f FILENAME [-hv {1.1,2}] [-p PROXIES [PROXIES ...]] -m METHODS
               [METHODS ...] [-mu MATCH_URL] [-mc MATCH_CODE] [-ml MATCH_LENGTH] [-fu FILTER_URL] [-fc FILTER_CODE]
               [-fl FILTER_LENGTH]

BURRito - BUrp Request Replayer v0.1

options:
  -h, --help            show this help message and exit
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
  -mu MATCH_URL, --match-url MATCH_URL
                        The target URL to match (filters all others)
  -mc MATCH_CODE, --match-code MATCH_CODE
                        The status code to match (filters all others)
  -ml MATCH_LENGTH, --match-length MATCH_LENGTH
                        The length to match (filters all others)
  -fu FILTER_URL, --filter-url FILTER_URL
                        The target URL to filter (matches all others)
  -fc FILTER_CODE, --filter-code FILTER_CODE
                        The status code to filter (matches all others)
  -fl FILTER_LENGTH, --filter-length FILTER_LENGTH
                        The length to filter (match all others)
```
