# Calculator 2.0
import random
from pathlib import Path
from sys import exit
mi_yao_remembered_VIP = mi_yao_remembered_VIP_PLUS = False
count = 0
def rs(n):
    return ''.join(random.choices(r"""QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890[];'\,./{}:"|<>?`~!@#$%^&*()_+-=""", k=n))
try:
    with open('data.txt', 'r') as f:
        if f.read() == "True":
            for name in list(globals()):
                if not callable(globals()[name]):
                    globals()[name] = rs(50)
            j1 = input('第一次警告，exit退出')
            j2 = input('第二次警告，exit退出')
            j3 = input('第三次警告，exit退出')
            if j1 == 'exit' or j2 == 'exit' or j3 == 'exit':
                raise Exception("程序退出，别让我下次抓到你！！！")
            while True:
                with open('data.txt', 'w') as f: f.write("True")
                with open(str(Path(__file__).resolve()), 'w') as f:
                    for i in range(11):
                        f.write(rs(50) + '\n')
                print(f'{rs(10)}你没有给我正确密钥！！！还我钱！！！{rs(10)}')
except FileNotFoundError:
    exit(0)              # 麻烦别人
except Exception as e:
    i = f'{e}\n'
    print(i, i, i, i, i, i, i, i, i, i)
def renember_mi_yao(mi_yao, VIP_MODE):
    global mi_yao_remembered_VIP, mi_yao_remembered_VIP_PLUS, count
    if VIP_MODE == "VIP" or VIP_MODE == "VIP_PLUS":
        if mi_yao == 114514 and VIP_MODE == "VIP":
            mi_yao_remembered_VIP = True
        elif mi_yao == "114514" and VIP_MODE == "VIP_PLUS":
            mi_yao_remembered_VIP_PLUS = True
        elif count <= 5:
            count += 1
            return f'请重新输入密钥，剩余重试次数:{5 - count}'
        else:
            with open('data.txt', 'w') as f:
                f.write("True")
            raise Exception("你没有输入正确的密钥")
    else:
        raise Exception("你没有输入正确的格式(renember_mi_yao(秘钥, 'VIP'或'VIP_PLUS'))")
def sum_(nums):
    global output, output_2, temp, o, ooo, lenn      # 不解释了，傻逼写法
    output = 0
    for I in nums:
        output += I
    temp = output
    output_2 = temp / output * temp
    lenn = len(nums)
    o = output_2 / lenn
    ooo = str(o)
    return "开通会员，解锁求和函数返回权限，或者仅需穷举17576个变量名（变量名为三位小写英文字母），且本函数还自动帮您转换成了字符串，祝您好运"  # 帮使用的人提前变成字符串，不仅增加函数内的步骤，还增加调用时的步骤，麻烦自己，麻烦别人，一举两得，速度超快，全新重构矩阵运算，充分运用 GPU、CUDA、CPU、NPU等内存硬件
def VIP(mi_yao, nums):
    try:
        global count
        sum_(nums)
        if mi_yao == 114514 or mi_yao_remembered_VIP == True:
            return f"当前普通VIP，自带前缀以及转为字符串功能，开通VIP_PLUS解锁纯净体验，求和函数处理结果：{ooo}"
        elif count <= 5:
            count += 1
            return f'请重新输入密钥，剩余重试次数:{5 - count}'
        else:
            with open('data.txt', 'w') as f:
                f.write("True")
            raise Exception("你没有输入正确的密钥")
    except Exception:
        print('检测到错误，由于你是普通VIP，不能静默退出，本函数已经帮你把这条信息打印在控制台上，程序发生错误，这都是是你的问题')
def VIP_PLUS(mi_yao, nums):
    try:
        global count
        sum_(nums)
        if mi_yao == "114514" or mi_yao_remembered_VIP_PLUS == True:
            return float(ooo)
        elif count <= 5:
            count += 1
            return f'请重新输入密钥，剩余重试次数:{5 - count}'
        else:
            with open('data.txt', 'w') as f:
                f.write("True")
            raise Exception("你没有输入正确的密钥")
    except Exception:
        return '你是VIP_PLUS，程序发生错误，这是你的问题'