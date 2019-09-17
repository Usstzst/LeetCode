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

# def PowerSetsRecursive2(items):
#     # the power set of the empty set has one element, the empty set
#     result = [[]]
#     for x in items:
#         result.extend([subset + [x] for subset in result])
#     return result
#
#
#
# result = PowerSetsRecursive2([1,2,2,3,5])
# res = []
# for i in range(len(result)):
#     if sum(result[i])== 5 and result[i] not in res:
#         res.append(result[i])
# print(res)
#




'''美团笔试一：找最长公共前缀'''
# def find_lcsubstr(s1, s2):
#     m = min(len(s1), len(s2))
#     cnt = 0
#     for i in range(m):
#         if s1[i]==s2[i]:
#             cnt += 1
#         else:
#             break
#     return cnt
#
#
# if __name__ == '__main__':
#     n = int(input())
#     listA = list(input().split(','))
#     print(listA)
#     while True:
#         a, b = [i for i in list(map(int,input().split()))]
#         if a<0 or b<0 or a>n or b>n:
#             continue
#         print(find_lcsubstr(listA[a-1], listA[b-1]))
#

'''美团笔试二：逆序排列字符串'''
# def compare(s1, s2):
#     if not s1:
#         return True
#     if not s2:
#         return False
#     for i in range(min(len(s1), len(s2))):
#         if ord(s1[i])>ord(s2[i]):
#             return True
#         elif ord(s1[i])<ord(s2[i]):
#             return False
#     return True if len(s1) < len(s2) else False
#
#
#
# def quick(nums):
#     if not nums:
#         return []
#     curr = nums[0]
#     left = quick([i for i in nums[1:] if not compare(i, curr)])
#     right = quick([i for i in nums[1:] if compare(i, curr)])
#     return left + [curr] + right
#
#
# if __name__ == '__main__':
#     listA = input().split(',')
#     res = quick(listA)
#     print(','.join(res[::-1]))

# import copy
# def solve(array):
#     if len(set(array))==len(array):
#         return 'YES'
#     if len(array)%2!=0:
#         return 'NO'
#
#     for i in range(1, len(array)):
#         if array[0]!= array[j]:
#             array.pop(0)
#             array.pop(i)
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     T = int(input())
#     for i in range(T):
#         n = int(input())
#         array = [int(i) for i in input().split()]
#
#


# def count1(num):
#     cnt = 0
#     while num > 0:
#         if num & 1 == 1:
#             cnt += 1
#         num >>= 1
#     return cnt
#
#
# if __name__ == '__main__':
#     #num = int(input())
#     # binary = bin(num).replace('0b', '')
#     #print(count1(num))
#     a = 2/2.00
#     print(a)


# import decimal
# def solve(xs, k):
#     res = ''
#     n = len(xs)
#     for i in range(n-k+1):
#         s = sum(xs[i:i + k])
#         b = str(decimal.Decimal('%.2f'%float(s/k)))
#         res+=b+' '
#     return res
#
#
# if __name__ == '__main__':
#     xs = list(map(int, input().split()))
#     k = int(input())
#     print(solve(xs, k))


# def KS(res, N, cnt0_all, cnt1_all):
#     dp0 = [0] * (N + 1)
#     dp1 = [0] * (N + 1)
#     result = []
#     cnt0, cnt1 = 0, 0
#     for i in range(N):
#         if res[i][1] == 0:
#             cnt0 += 1
#             dp0[i + 1] = cnt0 / cnt0_all
#             dp1[i + 1] = dp1[i]
#         else:
#             cnt1 += 1
#             dp1[i + 1] = cnt1 / cnt1_all
#             dp0[i + 1] = dp0[i]
#     for i in range(len(dp0)):
#         result.append(abs(dp0[i]-dp1[i]))
#     return max(result)
#
#
# if __name__ == '__main__':
#     N = int(input())
#     res = [[0] * 2 for _ in range(N)]
#     cnt1_all, cnt0_all = 0, 0
#     for i in range(N):
#         res[i][0], res[i][1] = [float(x) for x in input().split()]
#         if res[i][1] == 1:
#             cnt1_all += 1
#         else:
#             cnt0_all += 1
#     res.sort()
#     print(KS(res, N, cnt0_all, cnt1_all))
#
#


# def bag(n, c, w, v):
#     value = [[0 for j in range(c+1)] for i in range(n + 1)]
#     for i in range(1, n + 1):
#         for j in range(1, c + 1):
#             value[i][j] = value[i - 1][j]
#             if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i]] + v[i-1]:
#                 value[i][j] = value[i - 1][j - w[i]] + v[i-1]
#     return value[-1][-1]
#
#
# if __name__ == '__main__':
#     n, c = [int(i) for i in input().split()]
#     w, v = [], []
#     for i in range(n):
#         a, b = [int(j) for j in input().split()]
#         w.append(a)
#         v.append(b)
#     print(bag(n, c, w, v))


# def maxProfit(prices):
#     n = len(prices)
#     if n < 2:
#         return 0
#     pre_max_profit = [0 for i in range(n)]
#     pro_max_profit = [0 for i in range(n)]
#     max_profit = 0
#     pre_min_buy = prices[0]
#
#     for i in range(1, n):
#         pre_min_buy = min(pre_min_buy, prices[i])
#         pre_max_profit[i] = max(pre_max_profit[i - 1], prices[i] - pre_min_buy)
#     print(pre_max_profit)
#
#     pro_max_sell = prices[n - 1]
#     for k in range(n - 2, -1, -1):
#         pro_max_sell = max(prices[k], pro_max_sell)
#         pro_max_profit[k] = max(pro_max_profit[k + 1], pro_max_sell - prices[k])
#
#     print(pro_max_profit)
#
#     for j in range(0, n):
#         max_profit = max(max_profit, pre_max_profit[j] + pro_max_profit[j])
#     return max_profit
#
#
# if __name__ == '__main__':
#     prices = list(map(int, input().split()))
#     print(maxProfit(prices))


# def candy(ratings):
#
#     if ratings == None:
#         return 0
#     lenth = len(ratings)
#     dp = [1 for i in range(lenth)]
#     sum = 0
#     for i in range(1, len(ratings)):
#         if ratings[i] > ratings[i - 1]:
#             dp[i] = dp[i - 1] + 1
#     for i in range(len(ratings) - 2, -1, -1):
#         if ratings[i] > ratings[i + 1] and dp[i] <= dp[i + 1]:
#             dp[i] = dp[i + 1] + 1
#     for i in range(lenth):
#         sum += dp[i]
#     return sum
#
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = []
#     for i in range(n):
#         a = int(input())
#         arr.append(a)
#     print(candy(arr))


