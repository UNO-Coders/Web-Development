# Class: `ThreadRipperAsync`

This class provides a simple way to run multiple async functions in parallel.

## Initialization

The `ThreadRipperAsync` class is initialized with an integer parameter `n_workers` indicating the number of workers to use.

```python
_tr = ThreadRipperAsync(20)
```

## Usage

To run multiple async functions in parallel, create a list of async functions as arguments and pass them to the run function as follows:

```python
result = await _tr.run(
    *[async_function(i) for i in range(10)]
)
```

The run function uses a Semaphore to limit the number of concurrent tasks to the specified number of workers, and returns a list of results when all tasks have completed.

Alternatively, you can use the run_next function to run multiple async functions in sequence.

```python
result = await _tr.run_next(
    async_function1(),
    async_function2(),
    async_function3()
)
```

The run_next function is useful when you need to run async functions in a particular order.

Example

```python
import asyncio

async def async_function(i):
    await asyncio.sleep(1)
    return i

async def main():
    _tr = ThreadRipperAsync(20)
    result = await _tr.run(
        *[async_function(i) for i in range(10)]
    )
    print(result)

asyncio.run(main())
```

```bash
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

# Class: `ThreadRipper`

This class provides a simple way to run multiple functions in parallel using multithreading.

## Initialization

The `ThreadRipper` class is initialized with two optional parameters: `n_threads` sets the number of threads to use (default is 4), and `thread_name_prefix` sets the prefix for the thread names (default is "TRip").

```python
_tr = ThreadRipper(n_threads=60)
```

# Usage

To execute a series of functions in parallel, create a list of partial functions using the add_executables function, passing the function and its arguments as arguments to the partial function.

```python
for i in range(500):
    _tr.add_executables(callable_function, d=i, i=1)
```

Then call the start function to execute all partial functions in multithreaded mode.

```python
_tr.start()
```

The start function uses the ThreadPoolExecutor class to execute all partial functions concurrently, and waits for them to complete.

To get the collated result, access the result property after calling the start function.

```python
print(_tr.result)
```
