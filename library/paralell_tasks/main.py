import asyncio
import aiohttp


async def download_file(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            with open(filename, 'wb') as file:
                file.write(content)
            print(f"Downloaded {url} to {filename}")


async def main():
    tasks = [
        download_file('https://example.com/file1.txt', 'file1.txt'),
        download_file('https://example.com/file2.txt', 'file2.txt'),
        download_file('https://example.com/file3.txt', 'file3.txt')
    ]

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())