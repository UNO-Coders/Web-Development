import functools
import itertools


class PIPE:
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __ror__(self, other):
        return self.function(other)

    def __call__(self, *args, **kwargs):
        return PIPE(lambda x: self.function(x, *args, **kwargs))


chain = PIPE(itertools.chain.from_iterable)
chain_with = PIPE(itertools.chain)
