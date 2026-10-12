from xmlrpc.server import SimpleXMLRPCServer


def rpc_prima(n):
    """Mengembalikan list bilangan prima <= n (Sieve of Eratosthenes)."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, p in enumerate(sieve) if p]


if __name__ == "__main__":
    server = SimpleXMLRPCServer(("0.0.0.0", 8000), allow_none=True)
    server.register_function(rpc_prima, "rpc_prima")
    print("RPC server berjalan di port 8000 ...", flush=True)
    server.serve_forever()
