# python3


def build_heap(data):
    swaps = []
    
    for i in range(len(data)//2-1,-1,-1):
        while True:
            min_n = i
            left_n = 2*i+1
            right_n = 2*i+2

            if left_n<len(data) and right_n<len(data):
                if data[left_n] < data[min_n]:
                    min_n = left_n
                if data[right_n] < data[min_n]:
                    min_n = right_n
            
            if i != min_n:
                data[i], data[min_n] = data[min_n], data[i]
                swaps.append((i, min_n))
                i = min_n
            else:
                break


    return swaps


def main():
    input_type = input()

    if "I" in input_type:
        n = int(input())
        data = list(map(int, input().split()))

    elif "F" in input_type:
        file_name = input()

        if "tests/" not in file_name:
            file_name = "tests/" + file_name

        with open(file_name, 'r') as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    
    
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()