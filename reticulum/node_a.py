"""Node A: membuat identity + destination lalu melakukan announce secara periodik."""
import sys
import time

import RNS

cfg = sys.argv[1] if len(sys.argv) > 1 else "cfgA"
RNS.Reticulum(cfg)
identity = RNS.Identity()
dest = RNS.Destination(identity, RNS.Destination.IN, RNS.Destination.SINGLE, "tugas4", "announce")
print("Node A aktif. Alamat destination:", RNS.prettyhexrep(dest.hash), flush=True)
for i in range(1, 6):
    dest.announce(app_data=f"Halo dari Node A (announce ke-{i})".encode())
    print(f"Node A: announce ke-{i} dikirim", flush=True)
    time.sleep(3)
