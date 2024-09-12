# main.py

import subprocess
import concurrent.futures

def execute_script(script):
    subprocess.run(['python', script])

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    future1 = executor.submit(execute_script, 'TP1\Tp1.py')
    future2 = executor.submit(execute_script, 'TP1\p_sum.py')

    # Attendez que les deux processus se terminent
    future1.result()
    future2.result()