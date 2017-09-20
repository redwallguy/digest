#!/bin/bash
kill $(ps aux | grep '[H]ighnoon.py' | awk '{print $2}')