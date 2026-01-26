TARGET0 = 2**240
N = 2016
BLOCK_TIME = 600

def retarget(prev_target, actual_time):
    expected = N * BLOCK_TIME
    adj = max(0.25, min(4.0, actual_time/expected))
    return int(prev_target * adj)
