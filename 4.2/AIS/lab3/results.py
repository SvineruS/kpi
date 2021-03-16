import multiprocessing
import subprocess

from pathlib import Path
from time import time

from tabulate import tabulate

PACMAN_DIR = Path(__file__).parent / 'pacman'
MAPS = [f.stem for f in (PACMAN_DIR / 'layouts').iterdir()]


def main():
    results = multiprocessing.Pool().map(run_game, MAPS)
    print(tabulate(results, headers=['Map', 'WinRate', 'Avg Score', 'Time']))


def run_game(map_):
    time_start = time()
    output = subprocess.run(
        f'python pacman.py -p ExpectimaxAgent -l {map_} -a depth=3 -n 20 -q --timeout 5 -c',
        cwd=PACMAN_DIR, stdout=subprocess.PIPE, shell=True, text=True
    ).stdout.rsplit('\n', 5)
    time_delta = time() - time_start
    avg_score = output[-5].split(', ')[-1].split(')')[0]
    win_rate = output[-3].split('(')[-1].split(')')[0]
    return map_, win_rate, avg_score, time_delta


main()
