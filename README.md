# ewbf-statsd
Statsd aggregator for the EWBF miner

![](images/dashboard-example.png)

# Run:
```
docker run -d \
--restart always \
-e API_KEY=${DATADOG_API_KEY} \
-e APP_KEY=${DATADOG_APP_KEY} \
-e HOST=127.0.0.1 \
-e PORT=5000 \
-e POLLSEC=15 \
--name statsd \
--net host \
djenriquez/ewbf-statsd:latest
```
## Donations
- BTC - 33DyXVuy3R5jfLZRRpEQcXXAJ1Xz5rkGxE
- LTC - MUaov1JidbnpfeuQiSR3mtJhN3CN8Wj5g9
- ETH - 0xCBBC579Ac1Bc4868823fbBb2D8dDaFF93D619ceD
- DASH - Xy4cgJVAiHsrbeBB53NeQWk2iXKoWjBvJp
- ZEC - t1gYs8Zn2ZCFZWKZsTmZWd5bgXa9eD8M87K
- ZCL - t1JthRczZHUrYW4ayU8PjWA3RcRhZs1SnDv
- BCH - LOL