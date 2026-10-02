import asyncio, aiohttp, time
# fetch url
async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
             return await response.json()
# fetch multiple url
async def fetch_multiple(urls):
    response = await asyncio.gather(
        *(fetch_url(url) for url in urls)
    )
    return response
