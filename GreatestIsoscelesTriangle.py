file = open(r"C:\File\test.txt")
listTriangles = []

for line in file:
	line = line.rstrip()
	lenLine = len(line)

	if lenLine > 10:
		i = 0
		key = 0
		coordinate = {}

		while key < 6:
			if line[i] == '-':
				i = i + 1
				minus = -1
			else:
				minus = 1

			y = i
			number = ""

			while y < lenLine:
				if line[y].isnumeric():
					number = number + line[y]
				else:
					break
				y = y + 1
				i = i + 1

			if number != "":
				coordinate[key] = int(number) * minus
			else:
				break
			i = i + 1
			key = key + 1

		if key == 6 and i >= lenLine:
			if (i - 1) == lenLine or ord(line[i - 1]) == 10:
				i = 0
				length1 = (((coordinate[i] - coordinate[i+2]) ** 2) + ((coordinate[i+1] - coordinate[i+3]) ** 2 )) ** 0.5
				length2 = (((coordinate[i+2] - coordinate[i+4]) ** 2) + ((coordinate[i+3] - coordinate[i+5]) ** 2 )) ** 0.5
				length3 = (((coordinate[i+4] - coordinate[i]) ** 2) + ((coordinate[i+5] - coordinate[i+1]) ** 2 )) ** 0.5

				if (length1 + length2 > length3) and (length1 + length3 > length2) and (length2 + length3 > length1):
					if (length1 == length2) or (length2 == length3) or (length1 == length3):
						halfPerim = (length1 + length2 + length3) / 2
						coordinate['area'] = (halfPerim * (halfPerim - length1) * (halfPerim - length2) * (halfPerim - length3)) ** 0.5
						listTriangles.append(coordinate)

file.close()
selectedCoordinate = ""
lenList = len(listTriangles)

if lenList > 0:
	coordinate = listTriangles[0].copy()

	if lenList > 1:
		i = 0

		while i < lenList - 1:
			if listTriangles[i + 1]['area'] > coordinate['area']:
				coordinate = listTriangles[i + 1].copy()
			i = i + 1

		i = 0
		while i < 6:
			selectedCoordinate = selectedCoordinate + str(coordinate[i]) + " "
			i = i + 1

selectedCoordinate = selectedCoordinate.rstrip()

fileResult = open(r"C:\File\result.txt", "w")
fileResult.write(selectedCoordinate)
fileResult.close()