"""
============================
Author:柠檬班-木森
Time:2020/4/21   20:03
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
深浅复制：在列表中有嵌套列表的情况下才会去讨论深浅复制



"""

# li = [1, 2, 3]
#
# li_cp = li.copy()
# print(li, id(li))
# print(li_cp, id(li_cp))
#
# # 修改li
# li.append(999)
# print(li, id(li))
# print(li_cp, id(li_cp))


# 浅复制：
# a = [11, 22, 33]
# li = [1, 2, 3, a]
# li_cp = li.copy()

# print(li, id(li))
# print(li_cp, id(li_cp))

# li.append(999)
# a.append(789)
# print(li, id(li))
# print(li_cp, id(li_cp))

# 深复制
from copy import deepcopy


a = [11, 22, 33]
li = [1, 2, 3, a]
# 浅copy
li_cp = li.copy()
# 深copy
li_dpcp =deepcopy(li)

print(id(li[3]))
print(id(li_cp[3]))
print(id(li_dpcp[3]))


# print("li",li)
# print("浅复制",li_cp)
# print("深复制",li_dpcp)
# print('------------------------')
# a.append(789)
# print("li",li)
# print("浅复制",li_cp)
# print("深复制",li_dpcp)




