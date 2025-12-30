def log(num, log_list):
    def decorator(func):
        async def wrapper(i: int):
            log_list.append(num)
            return await func(i)
        return wrapper
    return decorator


async def task_1(i: int):
    if i == 0:
        return

    if i > 5:
        await task_2(i // 2)
    else:
        await task_2(i - 1)


async def task_2(i: int):
    if i == 0:
        return

    if i % 2 == 0:
        await task_1(i // 2)
    else:
        await task_2(i - 1)


async def coroutines_execution_order(i: int = 42) -> int:
    # Отследите порядок исполнения корутин при i = 42 и верните число, соответствующее ему.
    #
    # Когда поток управления входит в task_1 добавьте к результату цифру 1, а когда он входит в task_2,
    # добавьте цифру 2.
    #
    # Пример:
    # i = 7
    # return 12212
    global task_1, task_2
    result = []
    task_1 = log('1', result)(task_1)
    task_2 = log('2', result)(task_2)
    await task_1(i)
    return int(''.join(result))
