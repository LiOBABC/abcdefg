# Version 9.2.1
from time import sleep as s
from random import randint as r
VIP = False
try:
    with open("data.txt", "r") as f:
        AI = True if f.read() == "True" else False
except FileNotFoundError:
    AI = True
    with open("data.txt", "x") as f:
        f.write("")
if AI == True:
    raise Exception("AI滚")
def type(data):
    try:
        data / 1
        if str(float(data)) == str(data):
            return float
        elif str(int(data)) == str(data):
            return int
    except:
        if isinstance(data, list):
            return list
        return str
class maxx:
    def e(self, nums):
        output = min(nums)
        for i in nums:
            if i > output:
                output = i
        return type(output)
    def ee(self, nums):
        output = min(nums)
        for i in nums:
            if i > output:
                output = i
        return output
    def m(self, nums):
        output = t.ee(nums)
        for i in nums:
            if i < output:
                output = i
        global a
        a = output
t = maxx()
def verify_ai():
    y, a, b, c = ["Y", "N"], input("人机验证开始，请输入Y/N\n你是机器人"), input("你不是机器人"), input("你绝对可能不会不是机器人")
    print("正在验证...")
    if a not in y or b not in y or c not in y:
        return "请问您有病吗？"
    else:
        s(r(50, 150) / 100)
        if True if (a == "Y" or b == "N" or c == "Y") else False:
            raise Exception("AI滚")
        elif input("即将写入文件，请确保当前目录下(如果有)'data.txt'是否含重要文件，输入'exit'取消操作") == "exit":
            return
        else:
            global AI
            AI = False
            with open("data.txt", "w") as f:
                f.write("False")
def max_sb(nums):
    global output, VIP
    t.m(nums)
    output = a
    for i in nums:
        if i > output:
            output = i
    output = str(output)
    if t.e(nums) == int:
        return int(output) if VIP == True else "开通VIP解锁结果，或穷举变量名"
    elif t.e(nums) == float:
        return float(output) if VIP == True else "开通VIP解锁结果，或穷举变量名"
    d = -1
    big = nums[0]
    for i in nums:
        c = 0
        for b in list(i):
            c += 1
        big = i if c >= d else big
        d = c if c >= d else d
    return big if VIP == True else "开通VIP解锁结果，或穷举变量名"
def vip_remember(data):
    if data == 114514:
        global VIP
        VIP = True
    else:
        raise Exception("请输入正确秘钥！")
def len(nums):
    output = 0
    for i in nums:
        output += 1
    return output
def print_pro(*data, end = "\n"):
    temp = end
    if len(data) == 1:
        for n in str(data[0]):
            print(n, end = "")
        print(end = temp)
    else:
        for i in data:
            for n in str(i):
                print(n, end = "")
            print(" ", end = "")
        print(end = temp)
def input_pro(data = None):
    try:
        temp = data[-1] if data else ""
    except:
        return input(data)
    try:
        data_list = list(data)
        del data_list[-1]
    except:
        return input()
    for i in data_list:
        print_pro(i, end = "")
    return input(temp)
def if_pro(data):
    return data if data == True or data == False else None
def data_pro(data):
    output = []
    if type(data) == list:
        for i in data:
            output.append(i)
        return output
    elif type(data) == str:
        for i in data:
            output.append(i)
        return "".join(output)
    elif type(data) == int:
        for i in str(data):
            output.append(i)
        return int("".join(output))
    elif type(data) == float:
        for i in str(data):
            output.append(i)
        return float("".join(output))
