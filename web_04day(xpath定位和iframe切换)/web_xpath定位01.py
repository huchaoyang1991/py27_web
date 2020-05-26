"""
============================
Author:柠檬班-木森
Time:2020/4/28   20:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

#  逻辑运算  and
# //a[@class='nav-block' and @title='京东' and @target='_blank']


# 逻辑运算  or

# //span[text()='推荐' or text()='导航']



# xpath的函数

# text()：获取节点的文本内容

# contains(参数1，参数2):判断参数1是否包含参数2中的内容

# 匹配value属性包含 一下的input标签
# // input[contains(@value,'一下')]

# 匹配文本内容包含 抗击的 a标签
# //a[contains(text(),'抗击')]

# 匹配title属性包含 易购的 a标签
# //a[contains(@title,易购')]


# starts-with(参数1，参数2):判断参数1是否以参数2开头

# 匹配文本内容是 五一假期开头的a标签
# //a[starts-with(text(),'五一假期')]



# 轴定位

# 定位的某个节点/轴名称::节点

# 定位id=form的form节点中 子元素中name=issp的input标签
# //form[@id='form']/child::input[@name='issp']


# 定位id=form的form节点中 祖先元素中id='wrapper的div标签
# //form[@id='form']/ancestor::div[@id='wrapper']

