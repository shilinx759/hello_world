import unittest  # 导入unittest模块
from hello_world import get_info


# 创建一个继承unittest.TestCase的类
class Tests(unittest.TestCase):
    def test_get_info(self):
        self.assertEqual(
            get_info(),
            'hello project!')


if __name__ == '__main__':
    unittest.main()
