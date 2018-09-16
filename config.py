from collections import OrderedDict

status_code_weight = OrderedDict([(200, 0.80),
                      (404, 0.10),
                      (400, 0.05),
                      (500, 0.05),
                      ])
lognormal_mu = 6
lognormal_sigma = 0.75