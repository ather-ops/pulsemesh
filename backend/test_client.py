from api_client import fetch_url, fetch_multiple,aggregate_results
import asyncio
import time
async def main():

    urls=[
        "https://jsonplaceholder.typicode.com/todos/1",
         "https://httpbin.org/delay/5",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/does-not-exist"
    ]

    start = time.perf_counter()
    """
    result1 = await asyncio.gather(fetch_url(urls[0]))
    result2 = await asyncio.gather(fetch_url(urls[1]))
    end = time.perf_counter()

    result = await asyncio.gather(
        *(fetch_url(url) for url in urls)
    )

    end = time.perf_counter()
    print(result)
    print(f"Total time :{(end - start):.2f}") """

    result = await fetch_multiple(urls)
    summary = aggregate_results(result)
    end = time.perf_counter()
    print(result)
    print(f"Total Time :{(end - start):.2f}")
    print("Summary :",summary)
asyncio.run(main())
