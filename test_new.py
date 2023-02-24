import pytest

class TestDemo:
    def test_001(self):

        assert 1+2 == 3

    def test_002(self):

        assert 2 == 3


if __name__ == '__main__':

    # -s参数表示在控制台输出信息
    # 当指定了模块名后，运行文件，只收集当前文件的两条用例。

    pytest.main(['-s', 'test_new.py'])
