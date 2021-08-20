import logging
import sys


def getLogger(module_name):
    log = logging.getLogger(module_name)
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s'))
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    return log
