bind = "0.0.0.0:3000"
workers = 4
timeout = 3000
loglevel = "info"


def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")