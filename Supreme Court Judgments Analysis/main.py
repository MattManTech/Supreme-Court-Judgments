import asyncio
from config import config
from init import init


async def main():
    await asyncio.gather(init(config), return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
