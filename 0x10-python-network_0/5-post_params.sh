#!/bin/bash
# sends a POST request with two variables.
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I+will+always+be+here+for+PLD"
