def chase(*data, speed=2):
    if data == []:
        print('NoPositionalArgsError: Too few arguments')
        return None
    try:
        ans = []
        for i in data:
            if len(i) % speed == 0:
                ans.append(i)
    except ZeroDivisionError:
        print('ZeroDivisionError: Zero speed')
    if ans == []:
        print("UnsuccessfulChaseError: We didn't catch up with anyone")
        return None
    ans.sort(key=len, reverse=True)
    return ans
