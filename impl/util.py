import os
import subprocess

def ping (host):
    """
    ping a deivce on a network

    Args:
        host(str) : hostname or IP address
    
    Returns:
        bool: True==ok
    """
    if (host):
        devnull = open(os.devnull, 'w')
        return subprocess.call(["ping", "-n", "1", host], stdout=devnull, stderr=devnull) == 0
    return False 
    
