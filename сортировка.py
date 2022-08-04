import asyncio

import aiohttp

name_f = input('Введите имя файла: ')
url = 'https://raw.githubusercontent.com/Arthurs21/N_Normal1/main/samples/' + name_f


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text(encoding='utf-8')
    print(data)
    d1 = data.split('\n')
    N = len(d1)
    a = [int(x) for x in d1]

    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print(*a)


asyncio.run(main())
print()
f = input()
