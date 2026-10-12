#!/usr/bin/env bash
cd "$(dirname "$0")"
python3 node_a.py cfgA > /tmp/a.log 2>&1 &
A=$!
sleep 4
timeout 22 python3 node_b.py cfgB > /tmp/b.log 2>&1
kill $A
