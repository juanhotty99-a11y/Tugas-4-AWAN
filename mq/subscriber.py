import json
import os

import zmq

host = os.environ.get("PUB_HOST", "localhost")
ctx = zmq.Context()
sock = ctx.socket(zmq.SUB)
sock.connect(f"tcp://{host}:5556")
sock.setsockopt_string(zmq.SUBSCRIBE, "sensor")
print("Subscriber menunggu data ...", flush=True)
while True:
    topic, _, payload = sock.recv_string().partition(" ")
    d = json.loads(payload)
    print(f"Terima: {d['waktu']} | suhu={d['suhu']} C | kelembaban={d['kelembaban']} %", flush=True)
