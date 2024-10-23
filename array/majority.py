# find the number that comes max times in the array on O(n)
# uses extra memory 

def majority(N:list[int]) -> int:
    a = {}
    for i in N:
        a[i] = a.get(i,0)+1

    for i in a:
        if a[i]>len(N)/2:
            return i
    return -1

N = [1,2,1,3,3]
print(majority(N))
