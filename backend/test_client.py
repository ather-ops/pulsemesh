from api_client import fetch_url
import asyncio
async def main():

    url1 = "https://httpbin.org/json"
    result1 = await fetch_url(url1)
    print(result1)
if __name__ == "__main__":
    asyncio.run(main())
