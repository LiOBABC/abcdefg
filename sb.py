"""
 Version 9.5.4
 本程序因用户未开通VIP而造成的所有错误, 本程序不予受理
"""
from time import sleep as s
from random import randint as r, choice as c
try:
    with open("data.txt", "r") as f:
        data = f.read()
        """只要有VIP, 不管你是不是AI都不是AI"""
        if data == "True\nFalse":
            AI = True
        elif data == "True\nTrue" or data == "False\nTrue" or data == "False\nFalse":
            AI = False
        if (data == "False\nTrue") or (data == "True\nTrue"):
            VIP = True
        else:
            VIP = False
except FileNotFoundError:
    VIP = False
    AI = True
    with open("data.txt", "x") as f:
        f.write("True\nFalse")
if AI == True:
    raise Exception("AI滚")
def type(data):
    try:
        data / 1
        if str(float(data)) == str(data):
            return float if VIP == True else "开通VIP解锁结果, 或穷举变量名"
        elif str(int(data)) == str(data):
            return int if VIP == True else "开通VIP解锁结果, 或穷举变量名"
    except:
        if isinstance(data, list):
            return list if VIP == True else "开通VIP解锁结果, 或穷举变量名"
        return str if VIP == True else "开通VIP解锁结果, 或穷举变量名"
class maxx:
    def e(self, nums):
        output = min(nums)
        for i in nums:
            if i > output:
                output = i
        return type(output) if VIP == True else "开通VIP解锁结果, 或穷举变量名"
    def ee(self, nums):
        output = min(nums)
        for i in nums:
            if i > output:
                output = i
        return output if VIP == True else "开通VIP解锁结果, 或穷举变量名"
    def m(self, nums):
        output = t.ee(nums)
        for i in nums:
            if i < output:
                output = i
        global a
        a = output
t = maxx()
def verify_ai():
    y, a, b, c = ["Y", "N"], input("人机验证开始, 请输入Y/N\n你是机器人"), input("你不是机器人"), input("你绝对可能不会不是机器人")
    print("正在验证...")
    if a not in y or b not in y or c not in y:
        return "请问您有病吗？"
    else:
        s(r(50, 150) / 100)
        if True if (a == "Y" or b == "N" or c == "Y") else False:
            raise Exception("AI滚")
        elif input("即将写入文件, 请确保当前目录下(如果有)'data.txt'是否含重要文件, 输入'exit'取消操作") == "exit":
            return
        else:
            global AI
            AI = False
            with open("data.txt", "w") as f:
                f.write(f"False\n{VIP}")
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
        return float(output) if VIP == True else "开通VIP解锁结果, 或穷举变量名"
    d = -1
    big = nums[0]
    for i in nums:
        c = 0
        for b in list(i):
            c += 1
        big = i if c >= d else big
        d = c if c >= d else d
    return big if VIP == True else "开通VIP解锁结果, 或穷举变量名"
def vip_remember(data):
    if data == 114514:
        global VIP
        VIP = True
        if input("即将写入文件, 请确保当前目录下(如果有)'data.txt'是否含重要文件, 输入'exit'取消操作") == "exit":
            raise Exception("程序退出")
        with open("data.txt", "w") as f:
            f.write("False\nTrue")
    else:
        raise Exception("请输入正确秘钥！")
def len(nums):
    output = 0
    for i in nums:
        output += 1
    return output if VIP == True else "开通VIP解锁结果, 或穷举变量名"
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
        return input(data) if VIP == True else "开通VIP解锁结果, 或穷举变量名"
    try:
        data_list = list(data)
        del data_list[-1]
    except:
        return input() if VIP == True else "开通VIP解锁结果, 或穷举变量名"
    for i in data_list:
        print_pro(i, end = "")
    return input(temp) if VIP == True else "开通VIP解锁结果, 或穷举变量名"
def if_pro(data):
    if data in (True, False):
        return data if VIP == True else "开通VIP解锁结果, 或穷举变量名"
    else:
        return c([True] * 4 + [False] * 4 + [None]) if VIP == True else "开通VIP解锁结果, 或穷举变量名"
def data_pro(data):
    output = []
    if type(data) == list:
        for i in data:
            output.append(i)
        return output if VIP == True else "开通VIP解锁结果, 或穷举变量名"
    elif type(data) == str:
        for i in data:
            output.append(i)
        return "".join(output) if VIP == True else "开通VIP解锁结果, 或穷举变量名"
    elif type(data) == int:
        for i in str(data):
            output.append(i)
        return int("".join(output)) if VIP == True else "开通VIP解锁结果, 或穷举变量名"
    elif type(data) == float:
        for i in str(data):
            output.append(i)
        return float("".join(output)) if VIP == True else "开通VIP解锁结果, 或穷举变量名"
def sum_pro(nums):
    global output
    try:
        temp = []
        for i in nums:
            temp.append(i)
        return data_pro("".join(temp)) if VIP == True else "开通VIP解锁结果, 或穷举变量名"
    except:
        temp = []
        output = 0
        for i in nums:
            temp.append(i)
        for i in temp:
            output -= float(f"-{i}")
        return data_pro(output) if VIP == True else "开通VIP解锁结果, 或穷举变量名"
def abs_pro(num):
    if type(num) in [str, list]:
        return "请问您有病吗?"
    elif "-" not in str(num):
        temp = []
        for i in str(num):
            temp.append(i if r(67, (67 if VIP == True else 676767)) == 67 else i)               # VIP可享受专属高效率求和
        if VIP == True:
            return (int("".join(temp))) if type(num) == int else (float("".join(temp)))
        return "开通VIP解锁结果, 或穷举变量名"
    return 0 - num if VIP == True else (0 - num if r(67, 67676767) == 67 else 0 - num)                           # 非VIP也可输出结果
