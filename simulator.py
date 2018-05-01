import time
import random
from nameko.standalone.rpc import ClusterRpcProxy

temperature = 20
config = {'AMQP_URI':'amqp://guest:guest@ec2-18-231-106-14.sa-east-1.compute.amazonaws.com:80"}

with ClusterRpcProxy(config) as cluster_rpc:


    while True:
        
        cluster_rpc.temperature_server.receive_temperature(temperature)
        time.sleep(2)
        temperature = random.randint(20, 30) + random.random()
