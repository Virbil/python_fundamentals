class Underscore:
    def map(self, iterable, callback):
        new_arr = []
        for i in iterable:
            new_arr.append(callback(i))
        return new_arr
    def find(self, iterable, callback):
        new_arr = []
        for i in iterable:
            if callback(i) == True:
                new_arr.append(i)
                break
        return new_arr
    def filter(self, iterable, callback):
        new_arr = []
        for i in iterable:
            if callback(i) == True:
                new_arr.append(i)
        return new_arr
    def reject(self, iterable, callback):
        new_arr = []
        for i in iterable:
            if callback(i) == True:
                new_arr.append(i)
        return new_arr


_ = Underscore()
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0) # should return [2, 4, 6] after you finish implementing the code above
print(f"Map method: {_.map([1,2,3], lambda x: x*2)}") # should return [2,4,6]
print(f"Find method: {_.find([1,2,3,4,5,6], lambda x: x>4)}") # should return the first value that is greater than 4
print(f"Filter method: {_.filter([1,2,3,4,5,6], lambda x: x%2==0)}") # should return [2,4,6]
print(f"Reject method: {_.reject([1,2,3,4,5,6], lambda x: x%2!=0)}") # should return [1,3,5]
