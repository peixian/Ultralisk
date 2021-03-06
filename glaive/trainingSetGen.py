import numpy as np

def distance(x, y, maxX, maxY):
    """get the euclidian distance"""
    xDis = (x-maxX/2)**2
    yDis = (y-maxY/2)**2
    distance = np.sqrt(xDis + yDis)
    return distance
    
class TrainingSetGen:
    def __init__(self):        
        #[Unit name(s), player number, unitMultiplyer]
        self.ally = ["Zerg_Zergling", 0, 1]
        self.enemy = ["Terran_Marine", 1, 1]
        self.unitCount = 3
        self.maxX = 1280
        self.maxY = 690
    
    def writeOut(self):
        """Writes out random ally and enemy positions, returns them"""
        #Map Limitations are 0-1280 for x, and 0-720 for y
        with open("unitPos.txt", "w+") as expFile:
            outFormat = "{} {} {} {}\n"
            #player 0 positions are between (0-640, 0-720)
            allyPositions = []
            for i in range(self.ally[2]*self.unitCount):
                x = np.random.randint(0, self.maxX/2)
                y = np.random.randint(0, self.maxY)
                allyPositions.append((x, y))
                expFile.write(outFormat.format(self.ally[0], self.ally[1], x, y))
            
            enemyPositions = []
            for i in range(self.enemy[2]*self.unitCount):
                x = np.random.randint(self.maxX/4, 3*self.maxX/4)
                y = np.random.randint(self.maxY/4, 3*self.maxY/4)
                enemyPositions.append((x, y))
                expFile.write(outFormat.format(self.enemy[0], self.enemy[1], x, y))
        return allyPositions, enemyPositions
    
    def writeEnemyPositions(self):
        """Writes out random enemy positions and returns them"""
        with open("unitPos.txt", "w+") as expFile:
            outFormat = "{} {} {} {}\n"
            enemyPositions = []
            for i in range(self.enemy[2]*self.unitCount):
                x = np.random.randint(self.maxX/4, 3*self.maxX/4)
                y = np.random.randint(self.maxY/4, 3*self.maxY/4)
                enemyPositions.append((x, y))
                expFile.write(outFormat.format(self.enemy[0], self.enemy[1], x, y))
        return enemyPositions

    def writeAllyPositions(self, allyPositions):
        with open("unitPos.txt", "a") as expFile:
            outFormat = "{} {} {} {}\n"
            for allyPos in allyPositions:
                expFile.write(outFormat.format(self.ally[0], self.ally[1], allyPos[0], allyPos[1]))
        return allyPositions

    

    
    