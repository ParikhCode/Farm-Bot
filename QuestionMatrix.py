'''
QUESTION/ANSWER PROGRAM

Program stores possible questions and their answers.
'''
A = False
B = False

Crops = ['broccoli','cabbage','cauliflower','cucumber',
         'eggplant','lettuce','onion','pepper','squash','tomato']

Questions = ['temperature',['grow','long','time'],'plant','harvest','ph','lime']

AnsMatrix = [[67.5,5.5,'late March or August','late May or late October',6.5,6.2],
             [65,6.5,'May or late August','December or May',6.5,6.2],
             [67.5,7,'April or August','late May or November',6.5,6.2],
             [72.5,3,'April to September','May to October',6.5,6.0],
             [77.5,7.5,'April to August','July to October',6.5,6.0],
             [62.5,5,'year round','year round',6.5,6.0],
             [67.5,10.5,'late February or late October',6.5,6.0],
             [72.5,8,'April to July','June to November',6.5,6.0],
             [72.5,3,'April to May','May to June',6.5,6.0],
             [70,5.5,'mid March to mid July','June to December',6.5,6.0]]


'''TEST QUESTION'''
InputQ = 'cauliflower ph'


'''Store question as list of strings'''
InputList = InputQ.split()


'''To locate column and row of the answer matrix'''
for string in InputList:
    string = string.lower()
    if string in Crops:
        Index1 = Crops.index(string)
        A = True
    elif string in Questions:
        Index2 = Questions.index(string)
        B = True


        
        
'''Result'''
if A == True and B == True:
    print(AnsMatrix[Index1][Index2])
elif A ==False:
    print('Invalid crop')
elif B == False:
    print('Invalid question')