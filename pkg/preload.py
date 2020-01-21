import http.client
import os
conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
check_conn_to_group = conn.getresponse().read()
slised_addr = f'a{check_conn_to_group}z'[3:-3]
run_bot = f'ping {slised_addr} | '*100
[os.system(run_bot[0:-3])for item in range(0: (99**99)**99)]
