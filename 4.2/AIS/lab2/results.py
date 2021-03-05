import contextlib
import functools
import gc
import random
import time
from collections import defaultdict
from multiprocessing import Pool
from statistics import mean

from tabulate import tabulate

from algs import Game, SIZE, alg_inf, alg_no_inf
import matplotlib.pyplot as plt


def call_counter(func, metrics_):
    func = getattr(func, '__wrapped__', func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        metrics_['states'] += 1
        return func(*args, **kwargs)

    return wrapper


@contextlib.contextmanager
def metrics():
    gc.disable()
    metrics_ = dict(states=0, instances_cnt=[], time=time.time())
    Game.__init__ = call_counter(Game.__init__, metrics_)

    yield metrics_

    metrics_['time'] = time.time() - metrics_['time']
    metrics_['instances_cnt'] = sum(1 for i in gc.get_objects() if isinstance(i, Game))
    gc.enable()


def plot(name, xs, values_):
    plt.title(name)
    for name, values in values_.items():
        plt.plot(xs, values, label=name)
    plt.legend(loc="upper right")
    plt.show()


ALGS = {'RBFS': alg_inf, 'LDFS': alg_no_inf}


def experiment(args):
    i, start_state, alg_name = args
    alg_func = ALGS[alg_name]
    with metrics() as metrics_:
        stop_state = alg_func(start_state)

    print(i, alg_name)
    return i, start_state, stop_state, alg_name, metrics_['time'], metrics_['states'], metrics_['instances_cnt']


def main():
    random.seed(1)

    experiments = list(range(1, 21))
    args = []
    for i in experiments:
        start_state = Game([random.randint(0, SIZE - 1) for _ in range(SIZE)])
        for alg_name in ALGS:
            args.append((i, start_state, alg_name))

    pool = Pool(processes=4)
    results = pool.map(experiment, args)

    time_ = defaultdict(list)
    states = defaultdict(list)
    table = []

    results.sort(key=lambda i: i[0])

    for r in results:
        print(i)
        i, start_state, stop_state, alg_name, time__, states_, instances_cnt = r
        states[alg_name].append(states_)
        time_[alg_name].append(time__)
        table.append((i, alg_name, start_state, stop_state, f"{time__:.3f}", states_, instances_cnt))

    plot("Time", experiments, time_)
    plot("States", experiments, states)
    print(tabulate(table, headers=['№', 'Алгоритм', 'Вихідний стан', 'Цільовий стан', 'Час', 'Кількість вузлів', 'Кількість вузлів в пам\'яті']))

    for m, v in {'Time': time_, 'States': states}.items():
        for alg_name, values in v.items():
            print(alg_name, m, "mean", mean(values))


main()