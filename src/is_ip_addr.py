# 用于判断输入的字符串是否为ip地址
# 1. 获取输入的ip地址
# 2. 实现对字符串的处理方式判断是否为ip地址
# 3. 使用正则表达式的方式判断是否为ip地址
import re


def is_ip_addr_regex(ip):
    if re.match(
            '^([1-9]|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])(\\.(\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])){2}(\\.([1-9]|['
            '1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5]))$', ip) is None:
        return False
    else:
        return True


def is_ip_addr(ip):
    if ip is None:
        print("Error: 1")
        return False
    if 7 > len(ip) or len(ip) > 15:
        print("Error: 2")
        return False
    if ip_str[0] == '0' or ip_str[-1] == '0':
        print("Error: 3")
        return False
    child = str.split(ip_str, ".")
    if len(child) != 4:
        print("Error: 4")
        return False
    for c in child:
        if len(c) > 2 and c[0] == '0':
            print("Error: 5")
            return False
        for a in c:
            if a < '0' or a > '9':
                print("Error: 6")
                return False
        if int(c) > 255 or int(c) < 0:
            print("Error: 7")
            return False
    if int(child[0]) == 0:
        print("Error: 8")
        return False
    return True


if __name__ == "__main__":
    ip_str: str = input("请输入ip地址：")
    way = input("1. 字符串比较\n2. 正则表达式匹配\n请输入测试方式: ")
    if int(way) == 1:
        if is_ip_addr(ip_str):
            print("这是一个IP地址。")
        else:
            print("这不是一个IP地址。")
    elif int(way) == 2:
        if is_ip_addr_regex(ip_str):
            print("这是一个IP地址。")
        else:
            print("这不是一个IP地址。")
    else:
        print("输入错误")
