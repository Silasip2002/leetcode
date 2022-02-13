# Dynamic programming notes

## When to use DP ?
1. related recursive problems
2. the execution time is too long i.e O(2^n)

## How to use it ? 
1. save the subproblem in the memory. (Array,hash table or map)
2. check if the subproblem is existing in the memory
3. if existing in the subproblem, then just get the value from the memory which is O(1)

## How to solve the DP question? 
1. how many possible ways to get the ans 
2. **f(passible methods)** = **f(method 1)** + **(method 2)**
3. also need to seed the bounder condition i.e **if n = 0 then return 1**


## Templates 
two types of dynamic programming
### Dynamic programming (Button to top)
```
dp = ... // create db array;
        // add padding if needed

dp[0][0] = ... // init dp array
               // base case

for i ...
    for ...
    ...
    dp[i][i] = ... // transition

return dp[n][m]
```

### Recursion with memorization (Top to button)
```
mem = ... # create mem dictionary 

def dp(i,j....):
    if base_case(i,j): return ... #base cases
    if (i,j) not in mem : 
        mem[(i,j)] = ...         # transition
    return mem[(i,j)]

return dp(n,m)
```

## Common patterns
