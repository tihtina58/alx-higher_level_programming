#!/bin/bash
# displays the size of the body of some HTTP response.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
