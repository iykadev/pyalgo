

aunsorted = [6, 2, 7, 8, 3, 1, 10, 5, 4, 9]
asorted = []

amin = aunsorted[0]
aminindex = 0

while True:
    for i in range(len(aunsorted)):
        if aunsorted[i] < amin:
            amin = aunsorted[i]
            aminindex = i

    del aunsorted[aminindex]
    asorted = asorted + [amin]

    if len(aunsorted) == 0: break

    amin = aunsorted[0]
    aminindex = 0


print asorted
