#!/usr/bin/env python
# encoding: utf-8
#@author: Julianna
#@software: pycharm
#@file: zst.py
#@time: 2019-08-23 11:29

'''小于n的所有质数'''
# def Num(num):
#     value = []
#     # 2为最小的质数，从2开始做穷举，直到这个数本身
#     for i in range(2, num + 1):
#     # 从2到获取到的数求余，余数为0则不是质数，跳出循环
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             # 求余不为0则为质数
#             value.append(i)
#     return value



'''排列组合'''
# def perm(a,b):
#     # 这里是递归函数的出口，为什么呢，因为这里表示：一个长度为1的字符串，它的排列组合就是它自己。
#     if len(s) <= 1:
#         return [s]
#     sl = []  # 保存字符串的所有可能排列组合
#     for i in range(len(s)):  # 这个循环，对应 解题思路1）确定字符串的第一个字母是谁，有n种可能（n为字符串s的长度
#         for j in perm(s[0:i] + s[i + 1:]):  # 这个循环，对应 解题思路2）进入递归，s[0:i]+s[i+1:]的意思就是把s中的s[i]给去掉
#             sl.append(s[i] + j)  # 对应 解题思路2）问题就从“返回字符串中的字母排列组合” **变成了** “返回 第一个字母+除去第一个字母外的字符串的排列组合”
#     return sl
#
#
#
# def perm(s1,s2):
#     result = []
#     for i in range(len(s1)):
#         for j in range(s2):
#             result.append(s1[i]+j)
#     return result
#
#
# def main():
#     perm_nums = perm('abc')  # 有可能存在字母相同的情况
#     no_repeat_nums = list(set(perm_nums))  # 去重，挺牛的，这个代码
#     print('perm_nums', len(perm_nums), perm_nums)
#     print('no_repeat_nums', len(no_repeat_nums), no_repeat_nums)
#     pass
#
#
# if __name__ == '__main__':
#     main()


# def perm(a, b):
#     result = ''
#     for i in a:
#         for j in b:
#             result += i+j+' '
#     return result
#
#
# if __name__ == '__main__':
#     dic = {1: 'abc', 2: 'def', 3: 'ghi', 4: 'jkl', 5: 'mno', 6: 'pqr', 7: 'stu', 8: 'vwx', 9: 'yz'}
#     s = input()
#
#     a = dic[int(s[0])]
#     b = dic[int(s[1])]
#     print(perm(a, b))




# def perm(a, b):
#     result = []
#     for i in a:
#         for j in b:
#             result.append(i+j)
#     return result
#
#
# def perm2(res):
#     if len(res)==1:
#         return res
#     if len(res)==2:
#         return perm(res[0],res[1])
#     result = perm(res[0],res[1])
#     for i in range(2,len(res)):
#         result = perm(result, res[i])
#     return result



# if __name__ == '__main__':
#     dic = {1: 'abc', 2: 'def', 3: 'ghi', 4: 'jkl', 5: 'mno', 6: 'pqr', 7: 'stu', 8: 'vwx', 9: 'yz'}
#     s = input()
#     res = []
#     for i in s:
#         res.append(dic[int(i)])
#     res = perm2(res)
#     print(' '.join(res))
#


# def calculate(self, s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     res, num, sign = 0, 0, 1
#     stack = []
#     for c in s:
#         if c.isdigit():
#             num = 10 * num + int(c)
#         elif c == "+" or c == "-":
#             res += sign * num
#             num = 0
#             sign = 1 if c == "+" else -1
#         elif c == "(":
#             stack.append(res)
#             stack.append(sign)
#             res = 0
#             sign = 1
#         elif c == ")":
#             res += sign * num
#             num = 0
#             res *= stack.pop()
#             res += stack.pop()
#         elif c =='*':
#
#
#
#
#
#     res = res + sign * num
#     return res
#
# def calculate(self, s):
#
#     stack = []
#     pre_op = '+'
#     num = 0
#     for i, each in enumerate(s):
#         if each.isdigit():
#             num = 10 * num + int(each)
#         if i == len(s) - 1 or each in '+-*/':
#             if pre_op == '+':
#                 stack.append(num)
#             elif pre_op == '-':
#                 stack.append(-num)
#             elif pre_op == '*':
#                 stack.append(stack.pop() * num)
#             elif pre_op == '/':
#                 top = stack.pop()
#                 if top < 0:
#                     stack.append(int(top / num))
#                 else:
#                     stack.append(top // num)
#
#             pre_op = each
#             num = 0
#         if each
#     return sum(stack)
#


# from itertools import accumulate
#
# def all_sub_string(a_string):
#     if len(a_string) == 1:
#         return [a_string]
#     else:
#         return list(accumulate(a_string)) + all_sub_string(a_string[1:])
#
# if __name__ == '__main__':
#     s = input().strip()
#     res = all_sub_string(s)
#     print(len(res))



'''和为S的所有子集'''

def PowerSetsRecursive2(items):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in items:
        result.extend([subset + [x] for subset in result])
    return result



result = PowerSetsRecursive2([1,2,2,3,5])
res = []
for i in range(len(result)):
    if sum(result[i])== 5 and result[i] not in res:
        res.append(result[i])
print(res)