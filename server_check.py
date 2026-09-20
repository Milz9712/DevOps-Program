servers = [
    {"name": "web-01", "status": "running"},
    {"name": "web-02", "status": "stopped"},
    {"name": "database-01", "status": "running"},
]

def check_server(server):
    if server["status"] == "running":
        return f"{server['name']} is healthy"
    else:
        return f"{server['name']} needs attention"


for server in servers:
    print(check_server(server))