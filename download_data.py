import parse

loaded = 0

with open("urls.txt", "r") as f:
    urls = f.read().split("\n")

total = len(urls)

from joblib import Parallel, delayed


def download_url(i):
    message = parse.process_page(urls[i], "data")
    loaded += 1
    print(f"({loaded} / {total}) {message}")

if __name__ == "__main__":
    # Run the loop in parallel.
    results = Parallel(n_jobs=4)(delayed(download_url)(i) for i in range(0, len(urls)))