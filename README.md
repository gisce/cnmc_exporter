# CNMC Prometheus exporter

- It needs a [Prometheus Pushgateway](https://github.com/prometheus/pushgateway)
- Install requirements via `pip install -r requirements.txt`
- Export the following environment variables: CNMC_CONSUMER_KEY CNMC_CONSUMER_SECRET and CNMC_CUPS_TEST

## How to use

```shell
CNMC_CONSUMER_KEY=XXXX CNMC_CONSUMER_SECRET=XXXX CNMC_CUPS_TEST=ESXXXXX python cnmc_exporter.py
```
