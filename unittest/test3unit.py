# https://docs.python.org/es/3.9/library/unittest.html
import unittest


class Widget:
    def __init__(self, valor):
        self.myvalor = valor
    def size(self):
        return 10,10


class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (10, 10))


class WidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (101, 10))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DefaultWidgetSizeTestCase('test_default_widget_size'))
    suite.addTest(WidgetSizeTestCase('test_widget_resize'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


'''def size(a):
    """>>> size("hola")
16"""
    return (10)
if __name__ == "__main__":
    import doctest
    doctest.testmod()'''