# import paramunittest
# import unittest
# @paramunittest.parametrized(
#     {'numa':10,'numb':30},
#     {'numa':40,'numb':50}
# )
#
# class ApiTestDemo(paramunittest.ParametrizedTestCase):
#     def setParameters(self, numa, numb):
#         self.a=numa
#         self.b=numb
#
#     def test_add(self):
#         print('%d+%d=%d' % (self.a, self.b, 40))
#         self.assertEqual(self.a + self.b, 40)
#
# if __name__=='___main__':
#     unittest.main(verbosity=2)
import paramunittest
import unittest
@paramunittest.parametrized(
    {'a':10,'b':20},
    {'a':30,'b':45}
)

class ApiTestDemo(paramunittest.ParametrizedTestCase):
    def setParameters(self, a, b):
        self.a=a #numa指向10 ，b指向20
        self.b=b

    def test_add_case(self):
        print('%d+%d=%d'%(self.a,self.b,30))
        self.assertEqual(self.a+self.b,30)

if __name__=='__main__':
    unittest.main(verbosity=2)