"""
当前分析这个代码主要的逻辑是实现模幂运算和素性检测

注意在手敲实现代码后了解相应的代码库

"""

def QuickMod(a, n, p):
    """
    快速模幂运算：计算 (a^n) % p 的结果
    a：底数，n：指数，p：模数
    """
    result = 1  # 初始结果设为1
    a = a % p   # 先对底数取模，简化后续计算
    
    while n > 0:
        if n % 2 == 1:  # 当指数为奇数时，将当前a乘到结果中
            result = (result * a) % p
        a = (a * a) % p  # 底数平方（无论指数奇偶都需要）
        n = n // 2       # 指数整除2（向下取整）
    
    return result

def MilerRabin(p):
    """"
    进行素性测试,判断p是否为素数
    如果是素数,返回true ,如果不是,返回false
    """
    for i in range(10):#重复进行10次检测提高准确率
        

