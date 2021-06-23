if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    
    first = max(arr)
    
    second = min(arr)
    
    for i in range(0,len(arr)):
        if arr[i] > second and arr[i] < first:
            second = arr[i]
            
    print(second)