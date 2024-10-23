# Given a sorted list print the elements of the list that add up to the target in O(n)
def pairsum(N: list[int], target: int) -> list[int]:
    start, end = 0, len(N) - 1
    
    while start < end:
        val = N[start] + N[end]
        
        if val == target:
            return [N[start], N[end]]
        elif val < target:
            start += 1
        else:
            end -= 1
    
    return []
    

N = [1,4,3,5,2]
N.sort()
print(pairsum(N, 9))
