#!/bin/bash
# cURL a JSON file
curl -sL "$1" -H "Content-Type: application/json" -d @"$2" -X POST