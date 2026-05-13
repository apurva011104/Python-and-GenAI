import asyncio

async def download(dataset):
    print(f"Downloading {dataset}...")
    await asyncio.sleep(2)

async def main():
    datasets = ["dataset1", "dataset2", "dataset3"]

    tasks = [download(d) for d in datasets]

    await asyncio.gather(*tasks)

    print("All downloads complete.")

asyncio.run(main())