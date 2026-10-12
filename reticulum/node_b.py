"""Node B: mendengarkan announce dan menampilkannya."""
import sys
import time

import RNS


class Handler:
    aspect_filter = "tugas4.announce"

    def received_announce(self, destination_hash, announced_identity, app_data):
        print("Node B: ANNOUNCE DITERIMA")
        print("   dari destination :", RNS.prettyhexrep(destination_hash))
        print("   app_data         :", app_data.decode() if app_data else "-", flush=True)


cfg = sys.argv[1] if len(sys.argv) > 1 else "cfgB"
RNS.Reticulum(cfg)
RNS.Transport.register_announce_handler(Handler())
print("Node B aktif, menunggu announce ...", flush=True)
while True:
    time.sleep(1)
