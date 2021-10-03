from functools import wraps
import tracemalloc
import time


def profile(f):
    """
    ## Decorator to profile memory usage by a function
    """

    def memory_humanize(num, suffix="B"):
        """
        ## Convert bytes to human readable format
        """
        for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
            if abs(num) < 1024.0:
                return f"{num:3.1f}{unit}{suffix}"
            num /= 1024.0
        return f"{num:.1f}Yi{suffix}"

    def time_humanize(seconds):
        """
        ## Convert seconds to human readable format
        """
        h = int(seconds / 3600)
        m = int((seconds % 3600) / 60)
        s = int(seconds % 60)
        return f"{h}h {m}m {s}s"

    @wraps(f)
    def decorator(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        res = f(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        print(f"profiler.mem.current: {memory_humanize(current) }")
        print(f"profiler.mem.peak: {memory_humanize(peak) }")
        tracemalloc.stop()
        end_time = time.time()
        print(f"profiler.duration: {time_humanize(end_time-start_time)}")
        return res

    return decorator
