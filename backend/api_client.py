import asyncio, aiohttp
import random
# fetch url
async def fetch_url(url):
    delay = random.randint(1,3)
    timeout = aiohttp.ClientTimeout(delay)
    for attempt in range(3):
        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(url) as response:
                    response_status = response.status
                    if response_status != 200:
                        return {
                        "success":False,
                        "status": response_status,
                        "data":None,
                        "error":"HTTP request failed"
                         }
                    data = await response.json()
                    return {
                        "success":True,
                         "status":response_status,
                         "data":data,
                         "error":None
                    }

        except asyncio.TimeoutError:
           print(f"Attempt {attempt+1} failed :Timeout")
    return {
        "success":False,
        "status":None,
        "data":None,
        "error":"Request timeout after 3 attempts"}

# fetch multiple url
async def fetch_multiple(urls):
    response = await asyncio.gather(
        *(fetch_url(url) for url in urls)
    )
    return response
# Aggreagte function
def aggregate_results(response):
    total = len(response)
    successful = 0
    failed = 0
    for result in response:
        if result["success"]:
            successful += 1
        else:
            failed += 1

    return {
        "total": total,
        "successful": successful,
        "failed": failed,
        "results": response
    }
