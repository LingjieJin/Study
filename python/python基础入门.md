# Python 知识点快速回顾

如果需要仔细学习Python，建议到[官方文档](https://docs.python.org/zh-cn/3/tutorial/index.html)查看

## Python简介

python是一门解释型，面向对象的高级程序设计语言。

由于历史原因，python目前存在python（python2版本）和python3两个主要的大版本，其中有部分的功能是互相不兼容的。现在基本都使用Python3，Python2在2020年就已经不更新了。所以最好是使用最新的版本。

查看python版本：

```python

➜  ~ python --version
Python 2.7.10
➜  ~ python3 --version
Python 3.7.3
```

### 第一个 Hello world

新建一个hello_world.py，内容如下:

```python

#!/usr/bin/env python3
 
print("Hello, World!")
```

执行这个脚本,查看输出：

```shell

➜  ~ python3 hello-world.py

Hello, World!
```

在这里，由于第一行的语法`#!`是告诉系统用python3解释器来执行这个脚本，这样就可以直接执行：

```shell

➜  ~ ./hello-world.py

Hello, World!
```

## Python基础语法

### 注释

以#开头的为注释，多行注释可以是`"""`或者`'''`

```python

#注释1

"""
多行注释1
多行注释2
"""
```

### 缩进

和其他语言用大括号来区分代码块不同，python用缩进来表示代码块，空格和Tab均可，如果是空格要保证同一代码块的空格数量相同。

```python

if s > 0:
 print("1")
else:
 print("2")
```

### 查看函数定义

可以通过help查看函数定义，比如查看**print()函数**：

```python

➜  python3
>>> help(print)

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

```

### print()函数

print()函数是我们平时使用的频率最高的函数之一。可以通过了解print()函数了解python的设计理念。

```python

#默认以空格分割
>>> print("a","b","c")
a b c

#修改分隔符
>>> print("a","b","c",sep=",")
a,b,c

#结尾不换行
>>> print("a","b","c",sep=",",end=".") 
a,b,c.
```

格式化打印会在之后的字符串部分详细介绍。

### 变量和类型

- 变量以数字字母和下划线命名，不能以数字开头
- 命名中多个单词以下划线分开，大小写敏感，不需要提前声明。
- protected实例变量以下划线开头(具体见类一小节)
- private实例变量以双下划线开头(具体见类一小节)

```python

file_name = "temp.txt" #变量赋值
a,b = 1,2  #多个变量可以同时赋值，以逗号分开
```

#### 常见基本类型

- 整型，支持任意大小的整型，只有int没有long
- 浮点数，支持科学计数法，比如111e-2表示1.11
- 布尔，True和False（注意大写），可以通过比较获得 temp = a > b
- 复数，虚部用j来表示，比如64.23+3j
- 字符串，单引号或者双引号包裹的文本，python中没有char的概念，char就是长度为1的字符串

```python
数字
2
2 * 3
2 ** 7
(2 + 3) * 4

浮点
2.7
0.1 + 0.2 # 0.3
2 * 0.1 # 0.2

布尔值
True # First letter is caps
False
bool("some value") # Returns True
bool("") # Returns False
bool(1) # Returns True

字符串
msg_from_computer = "Hello" 
another_msg ='Hello in single quote'

```

类型之间可以进行转换：

```python

>>> s="12"
>>> int(s) #字符串转int
12

>>> s="12.3"
>>> float(s) #字符串转float
12.3

>>> num=16
>>> hex(num) #整数转16进制字符串
'0x10'
```

### 运算符

#### 下标:[]

下标支持从左到右：以0开始；从右到左：以-1开始

```python

>>> s="123"
>>> s[0]
'1'

>>> s[-1]
'3'
```

关于下标可以参考这一张图：

```python

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

#### 切片:[left:right]

切片支持按照索引来返回子序列，**包含left，不包含right**

```python

>>> s="123456789"
>>> s[0:2]
'12'

>>> s[4:]
'56789'

>>> s[:-3]
'123456'
```

#### 成员运算符: in/not in

```python

>>> "123" in "12345"
True

>>> "123" not in "12345"
False
```

#### 逻辑运算符: and or not

```python

>>> s = 'Python'
>>> s.startswith("P") and s.endswith("n")
True

>>> s.startswith("P") or s.endswith("K")
True

>>> not s.startswith("P")
False
```

## 字符串

用三引号(`"""`或者`'''`)表示一个多行字符串，换行符会自动包含在里面：

```python

>>> print('''First line 
... second line
... third line''')

First line
second line
third line
```

用加号可以连接字符串：

```python

>>> "Hello" + " " + "Leo"

'Hello Leo'
```

### 格式化字符字面值

- 在字符串开始加上f/F，然后就可以在字符串内部用{}引用表达式的值，这点和shell很像：

    ```python

    >>> year=2019
    >>> month=6
    >>> day=18
    >>> f"Today is {year} {month} {day}"

    'Today is 2019 6 18'
    ```

- 格式化的时候可以指定字符串的最小宽度，这样能够打印出对齐的列：

    ```python

    >>> info={'year':2019,'day':18,'month':6}
    >>> for key,value in info.items():
    ...     print(f'{key:10} : {value:10}')
    ... 

    year       :       2019
    day        :         18
    month      :          6
    ```

- str.format同样可以格式化字符串

    ```python

    >>> "a{}{}".format("b","c")

    'abc'
    ```

- 可以指定引用顺序：

    ```python

    >>> "a{0}{1}".format("b","c")

    'abc'

    >>> "a{1}{0}".format("b","c")

    'acb'
    ```

- 也可以用关键字参数引用：

    ```python

    >>> "Today is {year} {month} {day}".format(year=2019,month=6,day=18)

    'Today is 2019 6 18'
    ```

- 可以用**符号，将map作为关键字传递：

    ```python

    >>> info={'year':2019,'day':18,'month':6}
    >>> "Today is {year} {month} {day}".format(**info)

    'Today is 2019 6 18'
    ```

- 内置函数vars()会把局部变量以字典返回，可以配合**来做格式化：

    ```python

    >>> "Today is {year} {month} {day}".format(**vars())

    'Today is 2019 6 18'
    ```

上文提到过，字符串支持切片，但不能用索引修改字符串的值，因为字符串是[不可变的](https://docs.python.org/zh-cn/3/glossary.html#term-immutable)：

```python

>>> s="Python"
>>> s[2:]
'thon'

>>> s[0]="T" #字符串是不可变的s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

## 流程控制

### 分支控制

#### if else

```python

>>> s="Python"
>>> if len(s) < 3:
...     print("length less than 3")
... elif len(s) < 5:
...     print("length less than 5")
... else:
...     print("length greater than 5")
... 

length greater than 5
```

### 循环控制

#### for x in xxx

python的for语句是用来**遍历**序列：

```python

>>> words = ['Hello','Leo']
>>> for word in words:
...     print(word)
... 

Hello
Leo
```

用**range函数**，可以创建以一个数字序列

```python

>>> for i in range(3):
...     print(i)
...

0
1
2
```

字典可以同时遍历key，value：

```python

>>> info={'year':2019,'day':18,'month':6}
>>> for key,value in info.items():
...     print(f'{key:10} : {value:10}')
```

序列可以用enumerate函数同时遍历index，value：

```python

>>> for index,word in enumerate(words):
...     print(index,word)
... 

0 Hello
1 Leo
```

break/continue可以跳出和继续循环，这点和C语言一样：

```python

>>> for i in range(5):
...     if i > 3:
...         break
...     print(i)
... 

0
1
2
3
```

#### while

while的语法和C语言也类似

```python

>>> i = 0
>>> while i < 5:
...     print(i)
...     i = i + 1
```

#### else

while和for都支持else语句，当循环条件不满足的时候执行，但是**注意break语句不会触发else语句**：

```python

>>> i = 0
>>> while i < 5:
...     print(i)
...     i = i + 1
... else:
...     print("Not less than 5")
... 

0
1
2
3
4
Not less than 5
```

### pass

当你在语法上需要一个**占位符**的时候，可以用pass语句，这个分支结构啥也不做：

```python

#定义一个空函数，如果没有pass语句，python会报错
>>> def initlog(*args):
...     pass   
...
```

## Python自带数据结构

### 列表

列表和其他语言的数组一样，用来存储一组值，列表支持索引和切片，是可变类型：

```python

#创建列表
>>> l=[1,2,3]

#列表最后添加一个元素
>>> l.append(4)

#修改列表的第一个元素
>>> l[0]=5

#对列表切片，返回一个新的列表
>>> l1=l[0:1]

#删除列表的最后一个元素，并返回
>>> l.pop()

#删除指定位置元素
>>> del l[0]

#删除全部元素
>>> del l[:]
```

### 元组

元组是用逗号分隔的一组值，通常由括号包裹，和列表的区别是**元组是不可变**的：

```python

>>> t=(1,2,'3')
#索引访问值

>>> t[0]
1

#序列解包，同时解开多个值
>>> a,b,c=t
>>> print(a,b,c)
1 2 3
```

### 集合

集合用来表示**不重复元素的无序**的集，可以用`{}`或者set创建，空集合只能用set()创建，集合是可变的。

```python

>>> a={1,2,3}
>>> b=set([2,3,4])

#遍历
>>> for element in a:
...     print(element)
... 
1
2
3

#添加元素
>>> a.add(5)

#删除元素
>>> a.remove(5)

#元素是否存在
>>> 1 in a

#集合运算
>>> print(a-b)
{1}
>>> print(a|b)
{1, 2, 3, 4}
>>> print(a&b)
{2, 3}
```

### 字典

字典是一种key-value的数据结构，任何不可变的类型都可以作为key。

```python

#初始化值
>>> temp={'a':1,'b':2}

#修改值
>>> temp['a']=3

#访问值
>>> temp['a']
3

#遍历
>>> for key,value in temp.items():
...     print(key,value)
... 
a 3
b 2

#删除
>>> del temp['a']

#按插入顺序返回key
>>> list(temp)
['b', 'c']

#字典的构造函数可以从键值对里创建
>>> temp=dict([('a',1),('b',2),('c',3)])

# Example of nested dict.
user = {
  'id': 1,
  'name': 'John wick',
  'cars': ['audi', 'bmw', 'tesla'],
  'projects': [
    {
      'id': 10,
      'name': 'Project 1'
    },
    {
      'id': 11,
      'name': 'Project 2'
    }
  ]
}
```

## 函数

函数可以让你灵活的组织和复用代码，**定义一个函数，以def表示函数定义，括号来表示参数，return来返回值，函数体以缩进表示**：

```python

>>> def add(a,b):
...     sum=a+b
...     return sum
... 
>>> add(1,2)
3
```

函数内部的变量存储在**局部符号表**里，在进行符号访问的时候，依次查找局部符号表，然后是外层函数的布局符号表，最后是内置符号表。

所以：

- 函数内可以访问全局变量
- 局部变量和全局变量重名，会访问到全局变量

```python

>>> def add(a,b):
...     print(temp)
...     return a+b
... 
>>> temp=1
>>> temp = "Hi"
>>> add(1,2)
Hi
3
```

函数内部**不能直接修改变全局变量**，但是可以通过global关键字重定义后可修改：

```python

>>> def add(a,b):
...     global c
...     c = 11
...     return a + b + c
... 

>>> c = 1
>>> add(1,2)
14
```

函数参数可以有默认值，这样在调用的时候可以提供更少的参数：

```python

def ask_ok(promot,retries=4,reminder="Please try again~"):
    while True:
        ok = input(promot)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("Invalid input")
        print(reminder)
```

调用的时候，有默认值的参数可以不提供：

```python

ask_ok("Developer ?")
ask_ok("Developer ?",2)
ask_ok("Developer ?",reminder="Oh no")
```

注意，默认值**只会执行一次**，所以当你要修改默认值的时候要慎重，比如：

```python

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

[1]
[1, 2]
[1, 2, 3]
```

这种情况，可以用**None**来代替：

```python

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

### 参数解包

- `*`解包元组或者列表
- `**`解包字典

```python

>>> def add(a,b):
...     return a+b
... 

>>> l = [2,3]
>>> add(*l)
5

>>> dic={'a':3,'b':4}
>>> add(**dic)
7
```

### lambda表达式

lambda表达式可以用来表示一类无序定义标识符的函数或者子程序：冒号前作为参数，冒号后为表达式：

```python

>>> a = lambda x,y:x*y
>>> a(3,4)
12
```

## 模块

代码多了之后，就产生了两个核心问题

1. 如何组织代码：很明显所有代码写到一个文件里是不合理的
2. 如何复用代码：通用的代码没必要每次都写一遍

在python中，解决这两个问题的方式就是模块。模块是一个包含Python定义和语句的文件，模块名就是文件名去掉.py后缀。

模块还能解决函数重名的问题。同一个文件里，如果定义了两个一样的函数，那么第二个会把第一个覆盖掉，但是在两个模块里，允许出现同名函数。

新建两个文件，logger1和logger2

```python

logger1.py
#!/usr/bin/env python3
 
def log():
  print('hello leo')
  

logger2.py
#!/usr/bin/env python3
 
def log():
  print('hello lina')
```

然后，创建demo.py，引用这两个文件，并调用里面的log函数

```python

import logger1,logger2

logger1.log()
logger2.log()
```

输出

```shell

➜ python3 demo.py
hello leo
hello lina
```

引用的时候，可以用别名

```python

import logger1 as l1
import logger2 as l2

l1.log()
l2.log()
```

模块在import的时候，python脚本会从上之下执行，可以通过判断`__name__=='__main__'`来判断是被import，还是直接执行的：

```python

#!/usr/bin/env python3

def log():
    print('hello leo')

#import的时候，不要执行这个方法
if __name__ == '__main__':
   log()

```

### 模块中的一些使用方法

打印模块中的所有变量和方法

```python

import math
print(dir(math))
```

返回全局和局部命名空间的变量

```python

print(locals())
print(globals())
```

## 类

用`class`关键字来定义类，`__init__`来定义构造哈数，属性直接通过在构造函数中赋值即可

```python

class Logger:
    def __init__(self,prefix):
        self.prefix = prefix
    
    def log_message(self,content):
        print(self.prefix + ":" + content)
```

创建对象和调用方法：

```python

l = Logger("Leo")
l.log_message("hi~")
```

属性分为公开和私有的，双下划线开头的表示私有：

```python

class Logger:
    def __init__(self,prefix):
        self.__prefix = prefix

    def log_message(self,content):
        print(self.__prefix + ":" + content)

l = Logger("Leo")
l.log_message("hi~")
print(l.__prefix)

执行，会发现使用函数能够正常输出，直接输出会报错该属性找不到。

➜  python python demo.py  
Leo:hi~
Traceback (most recent call last):
  File "demo.py", line 9, in <module>
    print(l.__prefix)
AttributeError: Logger instance has no attribute '__prefix'
```

### Sample

```python

class Athlete:
    # 构造函数
    def __init__(self, a_name, a_age = None, a_grade = dict()):
        self.name = a_name
        self.age = a_age
        self.grades = a_grade

    # 析构函数
    def __del__(self):
        self.name = ''
        self.age = 0
        self.grades = {}

    # 比较
    def __cmp__(self, other):
        if self.age > other.age:
            print('你有点年轻')
        elif self.age < other.age:
            print('你有点成熟')
        else:
            print('刚刚好')

    # 下面两个方法作用相同，都是打印类信息
    def __repr__(self):
        # 在命令端口输入对象名，也可以输出
        return ('Athlete Class：name、age、grades')

    def __str__(self):
        # 只能使用print(对象)
        grade = ''
        for key, value in self.grades.items():
            grade += str(key) + ':' + str(value)
        return (self.name + ' ' + str(self.age) + ' ' + grade)

    # 对字典进行操作
    def  __getitem__(self, key): # 返回字典值
        if key == '田径': return self.grades['田径']
        elif key == '游泳': return self.grades['游泳']
        elif key == '健身': return self.grades['健身']
        else: return 'unknown'

    # 当期望定义的类具备按照键存储值时，即类能够执行data['key']=value
    def __setitem__(self, key, value): # 设置字典值
        self.grades[key] = value

    def __delitem__(self, key): # 删除字典值
        del self.grades[key]
    
a = Athlete('jiangxuehan', 42, {'田径':98, '游泳':82, '健身':90})
b = Athlete('james', 36, {'田径':90, '游泳':96, '健身':98})
a['田径'] = 92
del a['游泳']
print(a)
a.__cmp__(b)
a.__del__()
print(a)
```

### 属性

可以通过双下划线来隐藏属性的，但仍然能通过一些trick的方式拿到属性的实现。所以**一般都用单下换线表示私有属性，外部不应该访问**。

然后，通过`@property`关键字来getter和setter，对应属性的获取和设置函数。

```python

class Logger(object):
    def __init__(self,prefix):
        self._prefix = prefix
    
    # 设置某个值为属性
    @property
    def prefix(self):
        return self._prefix

    # 与property是成对出现
    # 设置属性
    @prefix.setter
    def prefix(self,prefix):
        self._prefix = prefix

    # 返回属性值
    @prefix.getter 
    def prefix(self):
        print('@prefix.getter')
        return self.prefix

    # 删除属性值
    @prefix.deleter 
    def prefix(self): # 删除后就找不到对象属性
        del self.prefix
    
    def log(self,content):
        print(self._prefix + ":" + content)

l = Logger("Leo")
l.log("hello world")

l.prefix = "Lina"
l.log("hello world")
```

### 静态方法

直接通过类名来调用的方法叫做类方法，不需要先创建实例，通过关键字`@staticmethod`来标记：

```python

class Logger(object):
    def __init__(self,prefix):
        self._prefix = prefix
    
    def log(self,content):
        print(self._prefix + ":" + content)
    
    @staticmethod
    def version():
        return "1.0"
    
print(Logger.version())
```

### 类方法

类方法是只能访问类变量和类方法的方法。

类方法和静态方法一样，都是通过类名直接调用。类方法的关键字`@classmethod`，并且第一个参数是类本身，注意类本身也是个对象

```python

class Logger(object):
    def __init__(self,prefix):
        self._prefix = prefix
    
    def log(self,content):
        print(self._prefix + ":" + content)
    
    @classmethod
    def logger(cls,prefix):
        return cls(prefix)
    
l = Logger.logger("leo")
l.log("hello world")
```

#### 静态方法和类方法区别

主要区别：

- 类方法必须有一个参数，通常被命名为"cls"，指代类本身；而静态方法没有默认的参数，就像一个普通函数。
- 类方法可以访问类变量，而静态方法不可以访问类变量。
- 类方法可以通过类名或类的实例来调用，静态方法也可以通过类名或类的实例来调用。

使用环境区别：

- 使用类方法主要是在需要在方法中进行操作时需要调用类变量的情况下。
- 使用静态方法主要是在方法与类的属性和方法都没有直接关系，只是一个函数功能时使用。

总的来说，如果需要使用类变量或者需要与类有关系的操作，应该使用类方法。如果方法与类无关，可以使用静态方法。

### 继承

和其他语言一样，Python中也可以通过继承来扩展类的能力，在类定义的时候括号内标注基类即可，比如Event继承object，LoginEvent又继承Event。

```python

class Event(object):
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    def fire(self):
        print("Event fired")

class LoginEvent(Event):
    def fire(self):
        print("User Login")

if __name__ == "__main__":
    e = Event("event")
    e.fire()
    l = LoginEvent("login")
    l.fire()
```

多态是面向对象编程的一个核心概念，所以子类可以重写父类的方法，比如demo里LoginEvent override了父类的fire方法。

### 抽象类

没有办法实例化的类称作抽象类，比如猫和老鼠都是动物，但动物不能被实例化。Python的abc模块定义了抽象类，通过设置`metaclass=abc.ABCMeta`，然后用关键字`@abc.abstractmethod`来标注抽象方法：

```python

import abc

class Animal(object,metaclass=abc.ABCMeta):
    def __init__(self,kind):
        self._kind = kind

    @abc.abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪~")

class Cat(Animal):
    def speak(self):
        print("喵~")

if __name__ == "__main__":
    dog = Dog("狗")
    dog.speak()
    cat = Cat("猫")
    cat.speak()
```

## 文件

通过open可以打开文件，然后进行读写。

- '`r`' 读(默认)
- `'w'` 写(截断之前的内容)
- `'x'` 写，如果之前存在内容会触发异常
- `'a'` 追加内容到文件结尾
- `'b'` 二进制模式
- `'t'` 文本模式(默认)
- `'t'` 读写模式

比如，一个文本文件content.txt：

```txt
Environment in Bristol
Economic history of the Russian Federation
Energy in Chile
Employee monitoring
E-Government in South Korea
```

然后，通过read函数读取文件内容，注意打开文件后要关闭

```python

def read_file(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    print(f.read())
    f.close()

if __name__ == '__main__':
    read_file('content.txt')
```

也可以通过with语句，来指定文件对象的上下文，然后离开上下文的时候自动释放；可以通过for in逐行读取，或者通过readlines()把内容读取到一个容器里：

```python

def read_file(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        for line in f:
            print(line.rstrip())

    with open(file_name,'r',encoding='utf-8') as f:
        print(f.readlines())

if __name__ == '__main__':
    read_file('content.txt')
```

### 使用pickle进行数据的存储和读取

pickle模块是Python中提供的一个序列化模块，用于将Python对象序列化为字节流，并将其保存到文件中或者在网络上传输。它也可以将字节流反序列化为原始的Python对象。

pickle模块可以序列化几乎所有的Python数据对象，包括基本数据类型、自定义类的实例、函数等。通过pickle模块，可以轻松地将Python对象存储在文件中，以便稍后检索和重新使用。

需要注意的是，pickle序列化的数据是二进制格式的，因此不适合用作长期保存数据或跨平台数据传输。当数据需要长期存储或跨平台传输时，建议使用JSON、XML等格式

```python

import pickle
try:
    # 写文件
    with open('/Users/mac/PycharmProjects/hello/test.pickle', 'wb') as data:
        pickle.dump([1, 2, 'a'], data)
    # 读文件
    with open('/Users/mac/PycharmProjects/hello/test.pickle', 'rb') as data:
        a_list = pickle.load(data)
    print(a_list)
except IOError as err:
     print('File Error: '+ str(err))
```

## 异常

python中的异常可以用try-expect-finally来处理

- try 执行可能会抛出异常的代码块
- expect 捕获异常
- finally 一定会执行的代码，一般用来释放资源等等

```python

def read_file(file_name):
    try:
        with open(file_name,'r',encoding='utf-8') as f:
            for line in f:
                print(line.rstrip())
    except FileNotFoundError as ex:
        print(ex)
        print("File not found")
    finally:
        print("Code always run")

if __name__ == '__main__':
    read_file('abcd.txt')

```

程序里也可以手动抛出异常

```python

raise NameError("test error")
```

python3中，可以通过以下方式查找内置的error

```python

>>> import builtins
>>> dir(builtins)
```

## 数据库

使用mysql数据库

```python

import pymysql

try:
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='db_testAnalyzeData', port=9996, charset='utf8') # 连接数据库
    cur = conn.cursor() # 使用游标 
    try: # 执行sql语句
      cur.execute('SELECT  * FROM Customers')
      db.commit() # 提交修改
    except: # 出现错误，则回滚
        db.rollback()
    data = cur.fetchall() #返回多个元祖（多条记录）
    for d in data:
        print("cust_id: " + str(d[0]) + ' cust_name：' + d[2])
    cur.close() # 关闭游标
    conn.close() # 关闭数据库连接
except Exception:
    print('查询失败')
```

使用sqlite数据库

```python

import  sqlite3

connection = sqlite3.connect('data.sqlite')
cursor = connection.cursor()
# 使用通配符
cursor.execute("INSERT INTO school(name, dob) VALUES (?,?)", (name, dob))
cursor.close()
connection.close()
```
