from deepface import DeepFace
import time
import random
from enum import Enum 

class Action(Enum): 
    CLOSE_EYES = 0 
    SMILE = 1  
    NEUTRAL = 2 

    def __str__(self):
        return self.name
    





def generateRandomSequence(actions_count:int)->list[Action]:       
    result = []
    for i in range(actions_count):    
        ran = 1 
        result.append(Action(ran))  

    return result 



def main():      
    isVerified = False
    actions = generateRandomSequence(5)  
    currActIdx = 0
    act:Action = actions[currActIdx]

    def getAction() -> Action: 
        nonlocal act 
        return act

    def resetActions():    
        nonlocal currActIdx 
        nonlocal act 

        currActIdx = 0 
        actions = generateRandomSequence(5)
        act = actions[0]

    def handleAction(act: Action, happyProba:float , facialFeatures: dict ):     
        nonlocal actions 
        nonlocal isVerified
        nonlocal currActIdx

        isHappy = happyProba > 0.5 
        left_eye = facialFeatures["left_eye"] 
        right_eye = facialFeatures["right_eye"] 
        eyesClosed = left_eye == None and right_eye == None

        # determmine fail/pass
        if currActIdx >= len(actions):  
            # passed 
            return True 

        passed = False
        if act == Action.SMILE:  
            passed = isHappy 

        if act == Action.CLOSE_EYES: 
            passed = eyesClosed


        # failed
        return passed 

    


    # streaming video   
    DeepFace.stream(db_path="./output",handleAction=handleAction, getAction = getAction,resetActions=resetActions)

    if isVerified: 
        print("Verification success")
    else: 
        print("Not verified, but application stopped")

 
main() 
# actions = generateRandomSequence(5) 
# print(actions[0])



