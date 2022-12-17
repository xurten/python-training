# Tip 52 use subprocess for management of child processes

import subprocess
import time


def example_1():
    result = subprocess.run(['echo', 'Hello from subprocess'],
                            capture_output=True, encoding='utf-8')
    result.check_returncode()
    print(result.stdout)
    print(result.stderr)


def example_2():
    proc = subprocess.Popen(['sleep', '4'])
    count = 0
    while proc.poll() is None:
        print(f'I am working {count}')
        count = count + 1
    proc.communicate()
    print(proc.poll())


def example_3():
    start = time.time()
    sleep_procs = []
    for _ in range(20):
        proc = subprocess.Popen(['echo', '1'], stdout=subprocess.PIPE, text=True)
        sleep_procs.append(proc)
    results = []
    for proc in sleep_procs:
        value, _ = proc.communicate(timeout=0.1)
        results.append(value.replace('\n', ''))
    end = time.time()
    delta = end - start
    print(f'{results} in time: {delta:.3f}s')

# example_1()
# example_2()
example_3()