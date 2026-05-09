if __name__ == '__main__':
    N = int(input())
    records = []
    for _ in range(N):
        name = input()
        score = float(input())
        records.append([name, score])
        # 2 2 3 4 5 5
        #        0     -1
        # x = [name, score]
    records.sort(key=lambda x: (x[-1], x[0]))
    lowest = records[0][-1]

    second_lowest = None
    for _, score in records:
        if score != lowest:
            second_lowest = score
            break
    for name, score in records:
        if score == second_lowest:
            print(name)
    
    