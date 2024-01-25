#!/bin/bash
# cURL only methods
curl -sI "$1" | grep -i Allow | cut -d " " -f 2-