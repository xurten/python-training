import threading
import urllib.request


def download_file(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded {url} to {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def main():
    urls = [
        ('http://speedtest.ftp.otenet.gr/files/test1Mb.db', 'file1.txt'),
        ('http://speedtest.ftp.otenet.gr/files/test1Mb.db', 'file2.txt'),
        ('http://speedtest.ftp.otenet.gr/files/test1Mb.db', 'file3.txt')
    ]

    threads = []

    for url, filename in urls:
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()