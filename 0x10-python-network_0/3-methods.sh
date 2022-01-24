#!/bin/bash
curl -sIL "$1" -X OPTIONS | grep Allow | cut -d " " -f2-