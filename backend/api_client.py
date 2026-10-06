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
                        "error": "Not Found",
                        "status": response_status
                         }
                    return await response.json()
        except asyncio.TimeoutError:
           print(f"Attempt {attempt+1} failed :Timeout")
    return {"error":"Request timeout after 3 attempts"}

# fetch multiple url
async def fetch_multiple(urls):
    response = await asyncio.gather(
        *(fetch_url(url) for url in urls)
    )
    return response
