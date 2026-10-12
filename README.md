# Tugas 4 – Komputasi Awan

Tiga contoh komunikasi antar-proses dengan Python:

| Folder        | Topik                          | Library        |
|---------------|--------------------------------|----------------|
| `rpc/`        | RPC – fungsi `rpc_prima(n)`    | `xmlrpc` (bawaan Python) |
| `mq/`         | Message Queue Pub/Sub (sensor) | `pyzmq`        |
| `reticulum/`  | Announce antar node Reticulum  | `rns`          |

## Persiapan di VS Code

1. Install **Python 3.10+** dan ekstensi **Python** di VS Code.
2. Clone repo: `git clone https://github.com/juanhotty99-a11y/Tugas-4-AWAN.git`, lalu **File → Open Folder** ke folder tersebut.
3. Buka terminal (**Terminal → New Terminal** atau `` Ctrl+` ``), lalu buat virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate

   pip install -r requirements.txt
   ```

4. Tekan `Ctrl+Shift+P` → **Python: Select Interpreter** → pilih `.venv`.

Setiap program butuh **2 terminal** (klik ikon `+` atau *Split Terminal* di panel terminal). Hentikan program dengan `Ctrl+C`.

## 1. RPC (`rpc/`)

Terminal 1:
```bash
cd rpc
python server.py
```
Terminal 2:
```bash
cd rpc
python client.py 11
```
Output: `rpc_prima(11) = 2, 3, 5, 7, 11`

## 2. Message Queue (`mq/`)

Terminal 1:
```bash
cd mq
python subscriber.py
```
Terminal 2:
```bash
cd mq
python publisher.py
```
Publisher mengirim data sensor tiap 60 detik. Supaya cepat terlihat, atur interval jadi 2 detik:
- Windows (PowerShell): `$env:INTERVAL=2; python publisher.py`
- macOS/Linux: `INTERVAL=2 python publisher.py`

## 3. Reticulum (`reticulum/`)

Terminal 1 (Node A – TCP server, kirim 5 announce tiap 3 detik):
```bash
cd reticulum
python node_a.py cfgA
```
Terminal 2 (segera jalankan setelah Node A aktif):
```bash
cd reticulum
python node_b.py cfgB
```
Node B menampilkan `ANNOUNCE DITERIMA` beserta pesan dari Node A.
Di macOS/Linux bisa juga pakai `bash reticulum/run.sh` (log ada di `/tmp/a.log` dan `/tmp/b.log`).

## Alternatif: Docker

Jika Docker Desktop terpasang:
```bash
cd rpc && docker compose up --build
cd mq  && docker compose up --build
```
