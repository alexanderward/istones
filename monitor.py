import argparse
import subprocess
import time
from threading import Thread
import os


def track_pids(proc_name, sleep):
    monitor_pid = os.getpid()
    existing_procs = set()
    proc_map = {}
    while True:
        proc_list = set()
        for line in os.popen(f'ps ax | grep "{proc_name}" | grep -v grep'):
            fields = line.split()
            pid = int(fields[0])
            if pid != monitor_pid:
                fields_str = " ".join(fields[4:])
                proc_list.add(fields_str)
                if fields_str not in existing_procs:
                    existing_procs.add(fields_str)
                    proc_map[fields_str] = fields[4:]

        restart = existing_procs.difference(proc_list)
        for item in restart:
            print("restarting", item)
            subprocess.Popen(proc_map[item])
        time.sleep(sleep)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Monitor")
    parser.add_argument("-n", dest="name", required=True, help="name")
    parser.add_argument("-t", dest="timer", required=True, help="timer", type=int)
    args = parser.parse_args()
    t = Thread(target=track_pids, args=(args.name, args.timer))
    t.daemon = True
    t.start()
    t.join()
