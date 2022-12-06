
marker_len = 14
with open('input6.txt', 'r') as f:
    for line in f.readlines():
        for i in range(0, len(line)-marker_len):
            marker = set(line[i:i+marker_len])
            if len(marker) == marker_len:
                print(i+marker_len)
                break
