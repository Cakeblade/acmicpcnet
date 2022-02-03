import itertools
import sys

def get_index(_data, _list):
    index = []
    output = []
    for i in range(0, len(_list)):
        for j in range(0, len(_list[i])):
            for data in _data:
                if _list[i][j] == data[0]:
                    index.append(data[1])
        
        output.append(sum(index))
        index = []
        
    return output

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    data = []
    data1 = []
    source = []
    comb = []
    
    for i in range(0, n):
        w, v = map(int, sys.stdin.readline().split())
        data.append([w, v])
        data1.append(w)
        
    for i in range(1, len(data[0]) + 1):
        source.append(list(itertools.combinations(data1, i)))
    
    for i in range(0, len(source)):
        for j in range(0, len(source[i])):
            if sum(source[i][j]) <= k:
                comb.append(source[i][j])
    
    index = get_index(data, comb)
    
    _max = -1
    for _index in index:
        if _max < _index:
            _max = _index
              
    print(_max)