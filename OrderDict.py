#! /bin/env python
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity = capacity
    def __setitem__(self,key,value):
        containsKey = 1 if key in self else 0
        if len(self)-containsKey >= self._capacity:
            first = self.popitem(last=False)
            print('remove:',first)
        
        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)
if __name__ == "__main__":
    
    d = LastUpdatedOrderedDict(3)

    d['c']= 2772
    d['a']= 33333
    d['b']= 325235
    print(d)

    d['d'] = 324
    print(d)

    d['a'] = 999
    print(d)
    

