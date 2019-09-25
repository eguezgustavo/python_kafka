import asyncio


async def wait_for_five_seconds():
    while True:
        print('5 seconds')
        await asyncio.sleep(5)


async def wait_for_three_seconds():
    while True:
        print('3 seconds')
        await asyncio.sleep(3)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()

    five_secs = loop.create_task(wait_for_five_seconds())
    three_secs = loop.create_task(wait_for_three_seconds())

    loop.run_until_complete(asyncio.wait([five_secs, three_secs]))
    loop.close()
