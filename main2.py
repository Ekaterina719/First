def chase(*data, speed=2):
    try:
        ans = []
        for i in data:
            try:
                if len(i) % speed == 0:
                    ans.append(i)
            except:
                print('ZeroDivisionError: Zero speed')
                break
        try:
            ans.sort(key=len, reverse=True)
            return ans
        except:
            print("UnsuccessfulChaseError: We didn't catch up with anyone")
    except:
        print('NoPositionalArgsError: Too few arguments')



data = ('Kitay Gorod', 'Chistye Prudy', 'Vasilievsky Fall')
print(chase(*data, speed=3))