# Array

## Useful Skills
- Create an empty martrix :
```
//first assign 0 into the col then assign each column into row.
mat = [[0 for i in range(0,sizeOfCol)] for j in range(0,sizeOfRow)]
```

- Simple loop all value index in martrix with different shape
 -  loop a martrix size
 -  using index devicy
``` 
for i in range(0, sizeOfRow * sizeOfCol) :  
    org_y = int(i / sizeOfCol)
    org_x = int(i % sizeOfCol)
    new_y = int(i / c)
    new_x = int(i % c)
    ans[new_y][new_x] = mat[org_y][org_x] 
```