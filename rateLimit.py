def return_rate_limit(github):
    rate_limit = github.get_rate_limit()
    return rate_limit.core.remaining
