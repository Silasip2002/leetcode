# Python useful Tips 

## Sort
### Sort()
The the key is a value which is base on the sort
```
sorted(intervals, key=lambda interval: interval[0])

# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))
print(sorted_list)
```

### cmp_to_key
- use a custom compare function to compare with two value with specific condition
- if return 1 then need to sort the value 
- 
```
def cmp_func(x:[String], y:[String]):
            if x + y > y + x:
                return 1  //return 1 need to be sorted  
            elif x == y:
                return 0
            else:
                return -1

        nums = [str(num) for num in nums] # convet all the value into String

        # sorted the string base on the custom compare function
        res = sorted(nums, key = cmp_to_key(cmp_func),reverse=True) 
```