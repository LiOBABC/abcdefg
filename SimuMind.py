"""
 SimuMind Version 1.0
"""
import random
import time
RANDOM_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789，。！？；：、（）【】《》“”‘’—…·,.!?;:()[]{}<>"\'`~@#$%^&*+-=/_\\|' + ''.join(map(chr, range(0x4E00, 0x9FA6)))
ai = "<AI> "
def sikao(a,b):
    sikaoo = 0
    ts = random.randint(a,b)
    for _ in range(ts):
        time.sleep(1)
        sikaoo = sikaoo + 1
        print(f"\r     正在思考...（{sikaoo}秒）", end="", flush=True)
    print(f"\r     思考完成（用时{ts}秒）    ")
while True:
    user_input = input("> ")
    s = random.randint(1,8)
    if s == 1:
        sikao(2,6)
        print(f"{ai}这个问题我还不会呢，换个话题吧。")
    elif s == 2:
        sikao(2,6)
        print(f"{ai}我不太明白你在说什么。")
    elif s == 3:
        sikao(2,6)
        print(f"{ai}你能换个方式问我吗？")
    elif s == 4:
        sikao(2,6)
        print(f"{ai}抱歉，我不太理解你的意思。")
    elif s == 5:
        sikao(2,6)
        print(f"{ai}这个问题有点难，我需要更多的信息。")
    elif s == 6:
        sikao(2,6)
        print(f"{ai}我不确定该如何回答这个问题。")
    elif s == 7:
        sikao(2,6)
        print(f"{ai}服务器繁忙，请稍后再试。")
    elif s == 8:
        sikao(3, 8)
        print(ai + ''.join(random.choices(RANDOM_CHARS, k=random.randint(6, 12))))