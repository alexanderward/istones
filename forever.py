import argparse
import multiprocessing
import time
# from threading import Thread

# import setproctitle


def run():
    while 1:
        # print('asfd')
        time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Forever")
    parser.add_argument("-name", dest="name", required=True, help="name")
    # parser.add_argument("-num", dest="num", required=True, type=int, help="name")
    args = parser.parse_args()
    proc = multiprocessing.Process(name=f'{args.name}', target=run)
    proc.daemon = True
    proc.start()
    proc.join()
