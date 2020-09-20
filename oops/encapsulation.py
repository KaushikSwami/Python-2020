class TestLeaf:
    num=[1,2,3,4,5]
    acc_num=123456
    __pin=1234

    def get_data(self):
        return TestLeaf.__pin

    def set_data(self,val):
        TestLeaf.__pin=val

t=TestLeaf()
print(t.get_data())
t.set_data('4455')
print(t.get_data())




