import asyncio
"""
Asynchronous programming in Python has several advantages and disadvantages:

Advantages:

Efficiency: Asynchronous programming can significantly improve the efficiency of your application, especially when dealing with I/O operations. Instead of waiting for one operation to complete before starting another, asynchronous code allows multiple operations to be executed concurrently.

Scalability: Asynchronous code is more scalable. It can handle more requests on a single server, which is particularly important for web applications and API services.

Better User Experience: Asynchronous programming can enhance user experiences by allowing an application to continue working even when some parts are busy. For example, a user interface can remain responsive even while the application is fetching data from the internet.

Resource Management: Asynchronous code can better manage system resources as it does not block resources while waiting for I/O operations to complete.

Disadvantages:

Complexity: Asynchronous programming can be more complex to understand and debug due to its nature. It requires a good understanding of concepts like event loops, tasks, and futures.

Error Handling: Error handling in asynchronous programming can be tricky. Exceptions might not always be raised where they occur but instead where they are awaited.

Not Always Faster: Asynchronous programming is not always faster. For CPU-bound tasks that don’t involve I/O, using a simple synchronous approach might be faster and simpler.

Library Support: Not all libraries support asynchronous programming. Some libraries might block the event loop and make your asynchronous code run as if it were synchronous.
"""


async def fetch_data(url):
    print(f"Fetching data from: {url}")
    await asyncio.sleep(2)  # Simulating an I/O-bound task
    print(f"Data fetched from: {url}")


async def main():
    tasks = [
        asyncio.ensure_future(fetch_data("http://example.com")),
        asyncio.ensure_future(fetch_data("http://google.com")),
        asyncio.ensure_future(fetch_data("http://github.com"))
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
