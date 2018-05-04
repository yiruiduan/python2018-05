#Author:yiruidaun
from rediscluster import StrictRedisCluster
import sys
def redis_cluster():
    redis_nodes=[
        {"host":"192.168.1.141","port":7000},
        {"host": "192.168.1.141", "port": 7001},
        {"host": "192.168.1.141", "port": 7002},
        {"host": "192.168.1.159", "port": 7000},
        {"host": "192.168.1.159", "port": 7001},
        {"host": "192.168.1.159", "port": 7002},

    ]
    try:
        redis_conn=StrictRedisCluster(startup_nodes=redis_nodes)
        return redis_conn
    except Exception:
        print("connect error")
        sys.exit(0)

print(redis_cluster().get("xiao"))
print("hello")