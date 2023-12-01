import concurrent.futures
import time
import random
import swarms.utils.futures


def f(x):
    time.sleep(random.random())
    return x


with concurrent.futures.ThreadPoolExecutor() as executor:
    fs_dict = {str(i): executor.submit(f, i) for i in range(10)}
    print(swarms.utils.futures.execute_futures_dict(fs_dict))