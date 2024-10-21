def maxp3(lst):
    if len(lst) < 3:
        raise ValueError("The list must contain at least three numbers.")
    
    # 获取排序后的列表的前三个最大值和前两个最小值
    lst.sort()
    max1, max2, max3 = lst[-1], lst[-2], lst[-3]  # 三个最大值
    min1, min2 = lst[0], lst[1]  # 两个最小值
    
    # 计算两种可能的最高乘积
    hi3 = max1 * max2 * max3  # 三个最大元素的乘积
    low2hi1 = min1 * min2 * max1  # 两个最小元素与一个最大元素的乘积
    
    # 返回更大的那个乘积
    return max(hi3, low2hi1)

# 示例测试
result = maxp3(lst=[-5, -2, -1, 0, 0, 3, 4, 5])
print(result)

result = maxp3(lst=[-5, -2, -1, 0, 0, 1, 1, 5])
print(result)


