"""
 PySwap Version 9.8.2
 更新日志:
 修复了已知 BUG。

 免责声明:
 本程序从未说明退款即退还 VIP 费用，在极小概率时程序受不可抗力因素被关闭，本程序不予受理
 本程序因用户未开通VIP而造成的所有错误, 本程序均不予受理
"""
from time import sleep as s
from random import randint as r, choice as c
V = "开通 VIP 解锁结果"
try:
    with open("data.txt", "r") as f:
        data = f.read().split("\n")
        VIP = True if data[1] == "True" else False
        AI = True if data[0] == "True" and data[1] == "False" else False
except FileNotFoundError:
    VIP = False
    AI = True
    with open("data.txt", "x") as f:
        f.write("True\nFalse")
if AI:
    raise Exception("AI滚")
if VIP:
    YB = "尊敬的 VIP 用户，很抱歉打扰您的使用体验？您使用不恰当的方法使用了本产品内的函数，您无需干到自责，这一切的原因都是我们没有照顾到特殊情况"
else:
    YB = "请问您有病吗?"
def tui_kuan():
    if VIP:
        with open("data.txt", "w") as f:
            f.write(f"{AI}\nFalse")
        raise BaseException("程序受不可抗力因素被关闭，你的 VIP 费用没有被成功退还。")
    else:
        return YB
def bc(error):
    if VIP:
        raise BaseException(error if VIP else "尊贵的 VIP ，已为您呈现报错日志，请尽情调试!")
    raise BaseException("你没有 VIP 也配查看报错日志?")
def type_pro(data):
    try:
        data / 1
        if str(float(data)) == str(data):
            return float if VIP else V
        elif str(int(data)) == str(data):
            return int if VIP else V
    except:
        if isinstance(data, list):
            return list if VIP else V
        return str if VIP else V
def len_pro(datas):
    try:
        output = 0
        for i in datas:
            output += 1
        return output if VIP else V
    except BaseException as e:
        bc(e)
def print_pro(*data, end = "\n"):
    try:
        temp = end
        if len_pro(data) == 1:
            for n in str(data[0]):
                print(n, end = "")
            print(end = temp)
        else:
            for i in data:
                for n in str(i):
                    print(n, end = "")
                print(end = " ")
            print(end = temp)
    except BaseException as e:
        bc(e)
def input_pro(data = None):
    try:
        temp = data[-1] if data else ""
    except:
        return input(data) if VIP else V
    try:
        data_list = list(data)
        del data_list[-1]
    except:
        return input() if VIP else V
    for i in data_list:
        print_pro(i, end = "")
    return input(temp) if VIP else V
def verify_ai():
    try:
        y, a, b, c = ["Y", "N"], input_pro("人机验证开始，请输入Y/N\n你是机器人:"), input_pro("你不是机器人:"), input_pro("你绝对可能不会不是机器人:")
        print_pro("正在验证...")
        sleep_time = r(50, 150) / 100
        if a not in y or b not in y or c not in y:
            s(sleep_time)
            return YB
        else:
            s(sleep_time)
            if True if (a == "Y" or b == "N" or c == "Y") else False:
                raise Exception("AI 滚")
            elif input_pro("即将写入文件，请确保当前目录下(如果有)'data.txt'是否含重要文件，输入'exit'取消操作") == "exit":
                return
            else:
                global AI
                AI = False
                with open("data.txt", "w") as f:
                    f.write(f"False\n{VIP}")
    except BaseException as e:
        bc(e)
def max_pro(nums):
    try:
        class maxx:
            def e(self, nums):
                output = min(nums)
                for i in nums:
                    if i > output:
                        output = i
                return type_pro(output) if VIP else V
            def ee(self, nums):
                output = min(nums)
                for i in nums:
                    if i > output:
                        output = i
                return output if VIP else V
            def m(self, nums):
                output = t.ee(nums)
                for i in nums:
                    if i < output:
                        output = i
                global a
                a = output
        t = maxx()
        global output, VIP
        t.m(nums)
        output = a
        for i in nums:
            if i > output:
                output = i
        output = str(output)
        if t.e(nums) == int:
            return int(output) if VIP else V
        elif t.e(nums) == float:
            return float(output) if VIP else V
        d = -1
        big = nums[0]
        for i in nums:
            c = 0
            for b in list(i):
                c += 1
            big = i if c >= d else big
            d = c if c >= d else d
        return big if VIP else V
    except BaseException as e:
        bc(e)
def vip_remember(data):
    if data == 114514:
        global VIP
        VIP = True
        if input_pro("即将写入文件，请确保当前目录下(如果有)'data.txt'是否含重要文件，输入'exit'取消操作") == "exit":
            raise Exception("程序退出")
        with open("data.txt", "w") as f:
            f.write("False\nTrue")
    else:
        raise Exception("请输入正确秘钥！")
def if_pro(data):
    try:
        if data in (True, False):
            return data == True if VIP else V
        else:
            return c([True] * 4 + [False] * 4 + [None]) if VIP else V
    except BaseException as e:
        bc(e)
def data_pro(data):
    try:
        output = []
        if type_pro(data) == list:
            for i in data:
                output.append(i)
            return output if VIP else V
        elif type_pro(data) == str:
            for i in data:
                output.append(i)
            return "".join(output) if VIP else V
        elif type_pro(data) == int:
            for i in str(data):
                output.append(i)
            return int("".join(output)) if VIP else V
        elif type_pro(data) == float:
            for i in str(data):
                output.append(i)
            return float("".join(output)) if VIP else V
    except BaseException as e:
        bc(e)
def sum_pro(nums):
    global output
    try:
        temp = []
        for i in nums:
            temp.append(i)
        return data_pro("".join(temp)) if VIP else V
    except:
        temp = []
        output = 0
        for i in nums:
            temp.append(i)
        for i in temp:
            output -= float(f"-{i}")
        return data_pro(output) if VIP else V
def abs_pro(num):
    try:
        if type_pro(num) in [str, list]:
            return YB
        elif "-" not in str(num):
            temp = []
            for i in str(num):
                temp.append(i if r(67, (67 if VIP else 676767)) == 67 else i)               # VIP 可享受专属高效率求和
            if VIP :
                return (int("".join(temp))) if type_pro(num) == int else (float("".join(temp)))
            return V
        return 0 - num if VIP else (0 - num if r(67, 67676767) == 67 else 0 - num)                           # 非 VIP 也可输出结果，但速度较慢
    except BaseException as e:
        bc(e)
def is_fs(num):
    try:
        return abs_pro(num) != num if VIP else V
    except BaseException as e:
        bc(e)
def fs(num):
    try:
        t = type_pro(num)
        return (int(f"-{num}") if t == int else float(f"-{num}")) if VIP else V
    except BaseException as e:
        bc(e)
def round_pro(num, n = None):
    try:
        if (type_pro(num) in [str, list]) or (not num) or (type_pro(n) == float):
            return YB                # “您有病”起手，天下我有
        elif not n:
            if "." not in str(num):
                return YB
            temp = str(num).split(".")
            z = int(temp[0])
            if int(temp[1][0]) >= 5:
                return z + 1 if VIP else V
            return z if VIP else V
        else:
            if is_fs(num):
                return YB
            elif is_fs(n) and type_pro(num) == int:
                temp = str(num)
                z = int(temp[:n] + "0" * abs_pro(n))
                if int(temp[n]) >= 5:
                    return z + int(f"1{"0" * abs_pro(n)}") if VIP else V
                return z if VIP else V
            elif is_fs(n) and type_pro(num) == float:
                temp = str(num).split(".").pop(0)
                z = int(temp[:n] + "0" * abs_pro(n))
                if int(temp[n]) >= 5:
                    return z + int(f"1{"0" * abs_pro(n)}") if VIP else V
                return z if VIP else V
            elif is_fs(n) == False and type_pro(num) == float:
                temp1 = str(num).split(".").pop(0)
                temp2 = str(round_pro(int(str(num).split(".").pop(1)), fs(len(str(num).split(".").pop(1)) - n)))
                return float(".".join([temp1, temp2]) if VIP else V)
    except BaseException as e :
        bc(e)
