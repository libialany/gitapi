##retrieves  any environment variables
import os
def run(**args):
    print "[*] In environment module."
    return str(os.environ)
