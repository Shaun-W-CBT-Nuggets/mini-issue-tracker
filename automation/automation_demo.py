import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()


async def main():
    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(timeout=timeout) as session:

        # GET request
        data = await fetch(
            session,
            "https://jsonplaceholder.typicode.com/posts/1"
        )
        print("GET response:", data)

        # POST request
        payload = {
            "title": "Hello World",
            "body": "Testing aiohttp",
            "userId": 1
        }

        async with session.post(
            "https://jsonplaceholder.typicode.com/posts",
            json=payload
        ) as response:
            response.raise_for_status()
            result = await response.json()
            print("POST response:", result)


if __name__ == "__main__":
    asyncio.run(main())