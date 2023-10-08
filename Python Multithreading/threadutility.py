from typing import Callable, Any
from functools import partial
import concurrent.futures
from loguru import logger
import asyncio


class ThreadRipper(object):
    def __init__(self, n_threads: int = 4, thread_name_prefix: str = "TRip") -> None:
        """Executes a series of partial functions in multithreading.

        Args:
            n_threads (int): number of threads
            thread_name_prefix (str, optional): thread prefix name. Defaults to "TRip".
        Usage:
            _tr = ThreadRipper(60)
            for i in range(500):
                _tr.add_executables(callable_function, d=i, i=1)
            _tr.start()
            print(_tr.result) # to get the collated result

        """

        self.__thread_name_prefix = thread_name_prefix
        self.__partials = []
        self.__thread_count = n_threads
        self.__futures = []

    def add_executables(self, func: Callable, *fargs: Any, **fkwargs: Any):
        self.__partials.append(partial(func, *fargs, **fkwargs))

    def start(self):
        logger.info(
            f"Dispatching ThreadPoolExecutor with {self.__thread_count} threads(s)"
        )
        with concurrent.futures.ThreadPoolExecutor(
            self.__thread_count, thread_name_prefix=self.__thread_name_prefix
        ) as executor:
            _res = []
            for executable in self.__partials:
                _res.append(executor.submit(executable))
            executor.shutdown(wait=False)
            self.__futures = [i.result() for i in _res]

    @property
    def result(self):
        try:
            return self.__futures
        finally:
            self.__partials = []
            self.__futures = []


class ThreadRipperAsync:
    def __init__(self, n_workers: int) -> None:
        """
        Args:
            n_workers (int): number of workers to use
        Usage:
            _tr = ThreadRipperAsync(20)
            result = await _tr.run(
                *[async_function(i) for i in range(10)])],
            )
        """
        self.__worker_count = n_workers

    async def run(self, *tasks):
        semaphore = asyncio.Semaphore(self.__worker_count)

        async def fn(aw):
            async with semaphore:
                await asyncio.sleep(delay=1)
                return await aw

        return await asyncio.gather(*(fn(aw) for aw in tasks))

    async def run_next(self, *tasks):
        f = [*tasks]
        return await asyncio.wait(f)