import fakeData
import montiorForAlert


fireList = []
for i in range(40,50):
    fireList.append("arduino"+str(i))

montiorForAlert.checkForCritialLevel()
fakeData.generateFakeData(50, fireList)

