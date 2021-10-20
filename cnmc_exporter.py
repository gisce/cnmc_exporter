from cnmc_client import Client
import time, json,requests

cnmc = Client(
    environment='prod', key=$KEY,
    secret=$SECRET
)
while True:
    start_time = time.time()
    cnmc_status = cnmc.fetch(cups=[$CUPS], file_type='SIPS2_PS_ELECTRICIDAD')
    response_time = time.time() - start_time

    if cnmc_status["code"] == 200:
        status = 1
    else:
        status = 0

    headers = {'content-type': 'text/plain'}

    payload = 'status %s\n' % status
    payload2 = 'response_time %s\n' % response_time

    r = requests.post("http://localhost:9091/metrics/job/status", data=payload, headers=headers)
    r = requests.post("http://localhost:9091/metrics/job/response_time", data=payload2, headers=headers)

    time.sleep(60)
