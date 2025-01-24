import aiohttp
import pytest


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


@pytest.mark.asyncio
async def test_fetch_data():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    result = await fetch_data(url)
    assert 'userId' in result
    assert 'id' in result
    assert 'title' in result
    assert 'body' in result
    print(result)
