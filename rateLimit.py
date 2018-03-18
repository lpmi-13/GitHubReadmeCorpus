def return_rate_limit(github):
    rate_limit = github.get_rate_limit()
    rate = rate_limit.rate
    return rate.remaining
