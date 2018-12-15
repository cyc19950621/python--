#输入数据
n = int(input('输入大于1的整数:'))
#if判定是否为大于一的整数
if type(n) == int and n > 1:
#判定质数
    for i in range(2,n):
        if (n % i)==0:
            print(n,"不是质数")
            break
        else:
            print(n,"是质数")
else:
        print("请输入大于1的整数")
#当输入2 时无对应值,且输入带小数点的整数无法正确识别
