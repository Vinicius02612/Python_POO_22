class A():

    def __init__(self) -> None:
        pass


    def m1(self):
        print('Classe A')


class B(A):

    def __init__(self) -> None:
        pass

    def m1(self):
        super().m1
        
    def m2(self):
        print('Class B')


class C():
    def __init__(self) -> None:
        pass
    
    def m3(self):
        print('Class C')


class D(B, C):
    pass



if __name__ == '__main__':
    d = D()


    d.m3()
    d.m2()

    print(D.__mro__)
