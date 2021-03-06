# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:06:20 2017

@author: Nick
"""

def defineTrainingDataset (gamma):
    
# Note: Nine possible output classes: 0 .. 8 trainingDataListXX [4]
    trainingDataDict = {}
    # BEGIN ORIGINAL LETTERS
    trainingDataDict[0]  =  (1,[0,0,0,0,1,0,0,0,0, 0,0,0,1,0,1,0,0,0, 0,0,1,0,0,0,1,0,0, 0,1,0,0,0,0,0,1,0, 1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1], 0,'A',0,'A') # training data list 1 selected for the letter 'A'
    trainingDataDict[1]  =  (2,[1,1,1,1,1,1,1,1,0, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,1,0, 1,1,1,1,1,1,1,0,0, 1,0,0,0,0,0,0,1,0, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1,0], 1,'B',1,'B') # training data list 2, letter 'E', courtesy AJM
    trainingDataDict[2]  =  (3,[1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1], 2,'C',2,'C') # training data list 3, letter 'C', courtesy PKVR
    trainingDataDict[3]  =  (4,[1,1,1,1,1,1,1,1,0, 1,0,0,0,0,0,0,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,1,1, 1,1,1,1,1,1,1,1,0], 3,'D',3,'O') # training data list 4, letter 'D', courtesy TD
    trainingDataDict[4]  =  (5,[1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1], 4,'E',4,'E') # training data list 5, letter 'E', courtesy BMcD 
    trainingDataDict[5]  =  (6,[1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0], 5,'F',4,'E') # training data list 6, letter 'F', courtesy SK
    trainingDataDict[6]  =  (7,[1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,1,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1,1], 6,'G',2,'C')
    trainingDataDict[7]  =  (8,[1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1], 7,'H',0,'A') # training data list 8, letter 'H', courtesy JC
    trainingDataDict[8]  =  (9,[0,0,1,1,1,1,1,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,1,1,1,1,1,0,0], 8,'I',5,'I') # training data list 9, letter 'I', courtesy GR
    trainingDataDict[9]  = (10,[0,0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1,0, 0,1,0,0,0,0,0,1,0, 0,1,0,0,0,0,0,1,0, 0,0,1,0,0,0,1,0,0, 0,0,0,1,1,1,0,0,0], 9,'J',6,'U') # training data list 10 selected for the letter 'L', courtesy JT
    trainingDataDict[10] = (11,[1,0,0,0,0,0,1,0,0, 1,0,0,0,0,1,0,0,0, 1,0,0,0,1,0,0,0,0, 1,0,0,1,0,0,0,0,0, 1,1,1,0,0,0,0,0,0, 1,0,0,1,0,0,0,0,0, 1,0,0,0,1,0,0,0,0, 1,0,0,0,0,1,0,0,0, 1,0,0,0,0,0,1,0,0],10,'K',4,'E') # training data list 11 selected for the letter 'K', courtesy EO      
    trainingDataDict[11] = (12,[1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1],11,'L',4,'E') # training data list 12 selected for the letter 'L', courtesy PV
    trainingDataDict[12] = (13,[1,0,0,0,0,0,0,0,1, 1,1,0,0,0,0,0,1,1, 1,1,0,0,0,0,0,1,1, 1,0,1,0,0,0,1,0,1, 1,0,1,0,0,0,1,0,1, 1,0,0,1,0,1,0,0,1, 1,0,0,1,0,1,0,0,1, 1,0,0,0,1,0,0,0,1, 1,0,0,0,1,0,0,0,1],12,'M',7,'M') # training data list 13 selected for the letter 'M', courtesy GR            
    trainingDataDict[13] = (14,[1,0,0,0,0,0,0,0,1, 1,1,0,0,0,0,0,0,1, 1,0,1,0,0,0,0,0,1, 1,0,0,1,0,0,0,0,1, 1,0,0,0,1,0,0,0,1, 1,0,0,0,0,1,0,0,1, 1,0,0,0,0,0,1,0,1, 1,0,0,0,0,0,0,1,1, 1,0,0,0,0,0,0,0,1],13,'N',7,'M') # training data list 14 selected for the letter 'N'
    trainingDataDict[14] = (15,[0,1,1,1,1,1,1,1,0, 1,1,0,0,0,0,0,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 0,1,1,1,1,1,1,1,0],14,'O',3,'O') # training data list 15, letter 'O', courtesy TD
    trainingDataDict[15] = (16,[1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0],15,'P',1,'B') # training data list 16, letter 'P', courtesy MT 
    trainingDataDict[16] = (17,[1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,1,0,0,1, 1,0,0,0,0,0,1,0,1, 1,0,0,0,0,0,0,1,1, 1,1,1,1,1,1,1,1,1],16,'Q',3,'O') # training data list 17, letter 'Q', courtesy AJM (square corners)
    trainingDataDict[17] = (18,[1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1,1, 1,0,0,0,0,1,0,0,0, 1,0,0,0,0,0,1,0,0, 1,0,0,0,0,0,0,1,0, 1,0,0,0,0,0,0,0,1],17,'R',1,'B') # training data list 18, letter 'R', courtesy AJM (variant on 'P') 
    trainingDataDict[18] = (19,[1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0,1, 0,0,0,0,0,0,0,0,1, 0,0,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1,1],18,'S',0,'A') # training data list 19, letter 'S', courtesy RG (square corners)
    trainingDataDict[19] = (20,[0,1,1,1,1,1,1,1,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0],19,'T',5,'I') # training data list 20, letter 'T', courtesy JR
    trainingDataDict[20] = (21,[1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 0,1,0,0,0,0,0,1,0, 0,0,1,1,1,1,1,0,0],20,'U',6,'U') # training data list 21, letter 'U', courtesy AJM 
    trainingDataDict[21] = (22,[1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 0,1,0,0,0,0,0,1,0, 0,1,0,0,0,0,0,1,0, 0,0,1,0,0,0,1,0,0, 0,0,1,0,0,0,1,0,0, 0,0,0,1,0,1,0,0,0, 0,0,0,1,0,1,0,0,0, 0,0,0,0,1,0,0,0,0],21,'V',6,'U') # training data list 22, letter 'V', courtesy AJM 
    trainingDataDict[22] = (23,[1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,1,0,0,0,1, 1,0,0,1,0,1,0,0,1, 1,0,1,0,0,0,1,0,1, 0,1,0,0,0,0,0,1,0],22,'W',8,'X') # training data list 23, letter 'W', courtesy KW
    trainingDataDict[23] = (24,[1,0,0,0,0,0,0,0,1, 0,1,0,0,0,0,0,1,0, 0,0,1,0,0,0,1,0,0, 0,0,0,1,0,1,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,1,0,1,0,0,0, 0,0,1,0,0,0,1,0,0, 0,1,0,0,0,0,0,1,0, 1,0,0,0,0,0,0,0,1],23,'X',8,'X') # training data list 24, letter 'X', courtesy JD
    trainingDataDict[24] = (25,[1,0,0,0,0,0,0,0,1, 0,1,0,0,0,0,0,1,0, 0,0,1,0,0,0,1,0,0, 0,0,0,1,0,1,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0],24,'Y',8,'X') # training data list 25, letter 'Y', courtesy ZC
    trainingDataDict[25] = (26,[1,1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,1,0, 0,0,0,0,0,0,1,0,0, 0,0,0,0,0,1,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,1,0,0,0,0,0, 0,0,1,0,0,0,0,0,0, 0,1,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1],25,'Z',8,'X') # training data list 26, letter 'Z', courtesy ZW
    # BEGIN VARIANTS
    trainingDataDict[26] = (27,[1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1], 0,'A',0,'A') # training data list 27, letter 'A', BLOCK version
    trainingDataDict[27] = (28,[0,1,1,1,1,1,1,1,0, 0,1,0,0,0,0,0,0,1, 0,1,0,0,0,0,0,0,1, 0,1,0,0,0,0,0,1,0, 0,1,1,1,1,1,1,0,0, 0,1,0,0,0,0,0,1,0, 0,1,0,0,0,0,0,0,1, 0,1,0,0,0,0,0,0,1, 0,1,1,1,1,1,1,1,0], 1,'B',1,'B') # training data list 28, letter 'B', Left vertical bar shifted 1 column RIGHT
    trainingDataDict[28] = (29,[0,0,1,1,1,1,1,0,0, 0,1,0,0,0,0,0,1,0, 1,0,0,0,0,0,0,1,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,1,1, 0,1,0,0,0,0,0,1,0, 0,0,1,1,1,1,1,0,0], 2,'C',2,'C') # training data list 29, letter 'C', BEARSish C
    trainingDataDict[29] = (30,[1,1,1,1,1,1,1,0,0, 1,0,0,0,0,0,0,1,0, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,1,0, 1,1,1,1,1,1,1,0,0], 3,'D',3,'O') # training data list 30, letter 'D', More rounded D
    trainingDataDict[30] = (31,[0,1,1,1,1,1,1,1,0, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 0,1,1,1,1,1,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,1, 0,1,1,1,1,1,1,1,0], 4,'E',4,'E') # training data list 31, letter 'E', Rounded E
    trainingDataDict[31] = (32,[1,1,1,1,1,1,1,1,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,1,1,1,1,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0], 5,'F',4,'E') # training data list 32, letter 'F', F w/ shortened horizontals
    trainingDataDict[32] = (33,[0,1,1,1,1,1,1,1,0, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,1,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 0,1,1,1,1,1,1,1,0], 6,'G',2,'C') # training data list 33, letter 'G', rounded G
    trainingDataDict[33] = (34,[1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1], 7,'H',0,'A') # training data list 34, letter 'H', lowercase h    
    trainingDataDict[34] = (35,[0,0,0,1,1,1,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,1,1,1,0,0,0], 8,'I',5,'I') # training data list 35, letter 'I', shortened horizontal bars
    trainingDataDict[35] = (36,[0,0,0,0,1,1,1,1,1, 0,0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1,0, 0,0,0,0,0,0,0,1,0, 0,1,0,0,0,0,0,1,0, 0,1,0,0,0,0,0,1,0, 0,1,0,0,0,0,0,1,0, 0,1,0,0,0,0,0,1,0, 0,1,1,1,1,1,1,1,0], 9,'J',6,'U') # training data list 36, letter 'J', block J with top horizontal bar
    trainingDataDict[36] = (37,[1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,1,1,0, 1,0,0,0,1,1,0,0,0, 1,0,1,1,0,0,0,0,0, 1,1,1,0,0,0,0,0,0, 1,0,1,1,0,0,0,0,0, 1,0,0,0,1,1,0,0,0, 1,0,0,0,0,0,1,1,0, 1,0,0,0,0,0,0,0,1],10,'K',4,'E') # training data list 37, letter 'K', elongated diagonals
    trainingDataDict[37] = (38,[1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,1,1,1,1,0,0,0,0],11,'L',4,'E') # training data list 38, letter 'L', shortened bottom horizontal
    trainingDataDict[38] = (39,[1,0,0,0,0,0,0,0,1, 1,1,0,0,0,0,0,1,1, 1,0,1,0,0,0,1,0,1, 1,0,0,1,0,1,0,0,1, 1,0,0,0,1,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1],12,'M',7,'M') # training data list 39, letter 'M', BLOCK version
    trainingDataDict[39] = (40,[1,0,0,0,0,0,0,0,1, 1,1,0,0,0,0,0,0,1, 1,1,1,0,0,0,0,0,1, 1,0,1,1,0,0,0,0,1, 1,0,0,1,1,1,0,0,1, 1,0,0,0,0,1,1,0,1, 1,0,0,0,0,0,1,1,1, 1,0,0,0,0,0,0,1,1, 1,0,0,0,0,0,0,0,1],13,'N',7,'M') # training data list 40, letter 'N', Thicker diagonal
    trainingDataDict[40] = (41,[1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1,1],14,'O',3,'O') # training data list 41, letter 'O', BLOCK version
    trainingDataDict[41] = (42,[1,1,1,1,1,0,0,0,0, 1,0,0,0,0,1,0,0,0, 1,0,0,0,0,1,0,0,0, 1,0,0,0,0,1,0,0,0, 1,1,1,1,1,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0],15,'P',1,'B') # training data list 42, letter 'P', Rounded with shortened horizontals
    trainingDataDict[42] = (43,[0,0,1,1,1,1,1,0,0, 0,1,0,0,0,0,0,1,0, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,1,0,1, 1,0,0,0,0,0,0,1,0, 0,0,1,1,1,1,1,0,1],16,'Q',3,'O') # training data list 43, letter 'Q', Rounded Q
    trainingDataDict[43] = (44,[1,1,1,1,1,0,0,0,0, 1,0,0,0,0,1,0,0,0, 1,0,0,0,0,1,0,0,0, 1,0,0,0,0,1,0,0,0, 1,1,1,1,1,0,0,0,0, 1,0,0,0,0,1,0,0,0, 1,0,0,0,0,0,1,0,0, 1,0,0,0,0,0,0,1,0, 1,0,0,0,0,0,0,0,1],17,'R',1,'B') # training data list 44, letter 'R', Shortened horizontals
    trainingDataDict[44] = (45,[0,1,1,1,1,1,1,1,0, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0, 0,1,1,1,1,1,1,1,0, 0,0,0,0,0,0,0,0,1, 0,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 0,1,1,1,1,1,1,1,0],18,'S',0,'A') # training data list 45, letter 'S', rounded
    trainingDataDict[45] = (46,[0,0,1,1,1,1,1,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0],19,'T',5,'I') # training data list 46, letter 'T', shortened horizontal
    trainingDataDict[46] = (47,[1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1,1],20,'U',6,'U') # training data list 47, letter 'U', BLOCK version
    trainingDataDict[47] = (48,[1,0,0,0,0,0,0,0,1, 0,1,0,0,0,0,0,1,0, 0,1,0,0,0,0,0,1,0, 0,0,1,0,0,0,1,0,0, 0,0,1,0,0,0,1,0,0, 0,0,0,1,0,1,0,0,0, 0,0,0,1,0,1,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0],21,'V',6,'U') # training data list 48, letter 'V', Modified diagonals
    trainingDataDict[48] = (49,[1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0,1, 1,0,0,0,1,0,0,0,1, 1,0,0,1,0,1,0,0,1, 1,0,1,0,0,0,1,0,1, 1,1,0,0,0,0,0,1,1, 1,0,0,0,0,0,0,0,1],22,'W',8,'X') # training data list 49, letter 'W', BLOCK version
    trainingDataDict[49] = (50,[1,1,0,0,0,0,0,1,1, 0,1,0,0,0,0,0,1,0, 0,0,1,0,0,0,1,0,0, 0,0,0,1,0,1,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,1,0,1,0,0,0, 0,0,1,0,0,0,1,0,0, 0,1,0,0,0,0,0,1,0, 1,1,0,0,0,0,0,1,1],23,'X',8,'X') # training data list 50, letter 'X', Embellished corners
    trainingDataDict[50] = (51,[1,1,0,0,0,0,0,1,1, 0,1,1,0,0,0,1,1,0, 0,0,0,1,0,1,0,0,0, 0,0,0,1,1,1,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,0,1,0,0,0,0],24,'Y',8,'X') # training data list 51, letter 'Y', Broader diagonals
    trainingDataDict[51] = (52,[1,1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,1,0, 0,0,0,0,0,0,1,0,0, 0,0,0,0,0,1,0,0,0, 0,0,0,0,1,0,0,0,0, 0,0,0,1,0,0,0,0,0, 0,0,1,0,0,0,0,0,0, 0,1,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1,1],25,'Z',8,'X') # training data list 26, letter 'Z', Embellished corners

    # Now compute one random variant for each initial training set
    # Determine length of trainingDataDict before updating
    lenTrainingDataDict = len(trainingDataDict)
    # Add random noise to the training record to test the model
    for letter in range(len(trainingDataDict)):
        
        tempList = []
        for i in range(len(trainingDataDict[letter][1])):
            randNum = random.random()       # Generate a random number between 0 and 1
            if randNum <= gamma:        # If the random number is <= gamma, flip the value of the pixel to create noise
                if trainingDataDict[letter][1][i] == 1:
                    tempList.append(0)
                else:
                    tempList.append(1)
            else:
                tempList.append(trainingDataDict[letter][1][i])   # Otherwise append the original value from the reference letter list
        
        # Tuples are immutable, so all values must be determined before assignment
        trainingDataDict[lenTrainingDataDict + letter] = (lenTrainingDataDict + letter + 1,     # Increment tuple counter
                                                          tempList,                             # Insert random noise pixel list
                                                          trainingDataDict[letter][2],          # Retain starting letter output index
                                                          trainingDataDict[letter][3],          # Retain starting letter assignment
                                                          trainingDataDict[letter][4],          # Retain starting big shape output index
                                                          trainingDataDict[letter][5])          # Retain starting big shape label
      
    return (trainingDataDict)      