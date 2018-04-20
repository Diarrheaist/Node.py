class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Wed')
e3 = daynames('Tue')
e4 = daynames('Thu')
e5 = daynames('Sat')
e6 = daynames('sun')
e7 = daynames('fri')

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4
e4.nextval = e7
e7.nextval = e5
e5.nextval = e6

thisvalue = e1

while thisvalue:
        print(thisvalue.dataval)
        thisvalue = thisvalue.nextval
