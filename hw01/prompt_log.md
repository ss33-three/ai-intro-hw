# AI交互日志
## 一、需求描述阶段
我给Cursor发的指令：
请用Python实现八皇后问题求解器，用回溯法，函数名solve_n_queens(n=8)，返回92个合法解，代码放src/queen.py；再写pytest测试放tests/test_queen.py，测试解数量、合法性、边界情况。

## 二、AI初次响应
Cursor返回了queen.py（八皇后求解器）和test_queen.py（单元测试）的完整代码，代码能算出8皇后的92个解，测试用例也覆盖了解数量、合法性、边界情况。

## 三、Bug引入
我故意改了queen.py里的代码：删掉斜线判断条件，只保留列判断；运行pytest tests/test_queen.py -v后，测试失败，解数量不是92。

## 四、Bug修复提问
我给Cursor发的指令：
这段八皇后代码解数量不是92，帮我找Bug、说原因、给修复代码。

## 五、AI修复结果
Cursor告诉我：Bug是少了斜线判断，恢复斜线判断后测试就过了；我把修复后的代码替换回去，重新运行pytest，所有测试都显示PASSED。