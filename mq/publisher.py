import json
import os
import random
import time
from datetime import datetime

import zmq

INTERVAL = int(os.environ.get("INTERVAL", "60"))  # detik (1 menit)
ctx = zmq.Context()
sock = ctx.socket(zmq.PUB)
sock.bind("tcp://*:5556")
time.sleep(1)  # beri waktu subscriber terhubung
print(f"Publisher berjalan, kirim data tiap {INTERVAL} detik", flush=True)
while True:
    data = {
        "sensor_id": "sensor-01",
        "waktu": datetime.now().isoformat(timespec="seconds"),
        "suhu": round(random.uniform(24, 34), 2),
        "kelembaban": round(random.uniform(40, 80), 2),
    }
    sock.send_string("sensor " + json.dumps(data))
    print("Kirim :", data, flush=True)
    time.sleep(INTERVAL)
