# HTTP stub server
Server that can be used for testing HTTP calls.

Implements this endpoints:
* */mirror/headers*: Respond with the request headers as a message. It also print them on logs.
* */response/<int>*: Response with the status code indicated in path (i.e. /response/419 will return a 418 "I'm a teapot")
* */wait/lognormal*: The response will wait some random time to simulate network delay. It is statistically model to return a status code according to the weight configured in the *config.py* file. The response time is a random value modelled using a [Log-normal probability distribution](https://en.wikipedia.org/wiki/Log-normal_distribution) which values can be configured using *lognormal_mu* and *lognormal_sigma* variables in the *config.py* file.

## Run
It can be run using docker:
```bash
docker build -t stub_server .
docker run -p 5000:5000 stub_server
```
