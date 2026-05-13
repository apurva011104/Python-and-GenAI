import asyncio

async def task_a():
    await asyncio.sleep(2)
    print("Task A completed.")

async def task_b():
    print("Task B started.")
    await asyncio.sleep(2)
    print("Task B completed.")

async def main():
    await task_a()
    await task_b()

asyncio.run(main())