class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

a1 = A()
a1.feature1()

class B(A):
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")


b1 = B()
b1.feature2()
        
