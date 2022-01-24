#!/bin/bash
curl -sL -d @"$2" -H "Content-Type: application/json" "$1"