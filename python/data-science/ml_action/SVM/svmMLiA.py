

def loadDataSet(fileName):
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat
def main():
    trainMat , labelMat =  loadDataSet('testSet.txt')

    print trainMat[1]
    print labelMat[1]
if __name__ == '__main__':
    main()