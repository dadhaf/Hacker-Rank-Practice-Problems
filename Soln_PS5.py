if __name__ == '__main__':
    N = int(raw_input())
    list = []
    for i in range(N):
        a = raw_input().split()
        if a[0] == 'insert':
            list.insert(int(a[1]), int(a[2]))
        elif a[0] == 'remove':
            list.remove(int(a[1]))
        elif a[0] == 'append':
            list.append(int(a[1]))
        elif a[0] == 'pop':
            list.pop()
        elif a[0] == 'sort':
            list.sort()
        elif a[0] == 'reverse':
            list.reverse()
        else:
            print list
            
    
