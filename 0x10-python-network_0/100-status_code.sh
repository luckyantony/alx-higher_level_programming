#!/bin/bash
curl -so /dev/null -w '%{response_code}' "$1"