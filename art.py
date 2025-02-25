class art:
    
    def multipleFrames(previousEmoji, currentEmoji, nextEmoji):
        return (f"""
                             ↓↓
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   |                            |   |          
           |   |                            |   |          
 {previousEmoji}        |   |             {currentEmoji}             |   |        {nextEmoji} 
           |   |                            |   |          
 __________|   |                            |   |__________
               |____________________________|

""")

    def singleFrame(currentEmoji):
        return (f"""
                             ↓↓
               |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    
               |                            |          
               |                            |        
               |             {currentEmoji}             |       
               |                            |         
               |                            |  
               |____________________________|                           

               
               """)
    
    def addingFrame():
        return ("""
                            |‾‾|
               |‾‾‾‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾‾‾‾|   
               |            |  |            |                   
               |            |  |            |                    
               |           _|  |_           |   
               |          \      /          |                
               |           \    /           |   
               |____________\  /____________|
                             \/
                            
""")
    
    def addSingleLeft():
        return  ("""
                 /|                      
                / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   
               /  |                         |          
              /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|      
             |           Adding Left          |       
              \    ___________________________|             
               \  |                         |   
                \ |_________________________|
                 \|                      
                             
""")
    
    def addSingleRight():
        return ("""
                                         |\ 
               |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \  
               |                         |  \          
             |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \          
             |        Adding Right            |    
             |___________________________    /    
               |                         |  /  
               |_________________________| /
                                         |/
                             
""")
    
    def addMultipleRight(previousEmoji, nextEmoji):
        return(f"""
                                         |\ 
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
           |   |                         |  \   |                   
           | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
 {previousEmoji}        | |        Adding Right            | |        {nextEmoji}        
           | |___________________________    /  |                  
 __________|   |                         |  /   |__________
               |_________________________| /
                                         |/
                             
""")
    
    def addMultipleLeft(previousEmoji, nextEmoji):
        return (f"""
                 /|                      
 __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   /  |                         |   |                   
           |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
 {previousEmoji}        | |           Adding Left          | |        {nextEmoji}        
           |  \    ___________________________| |                  
 __________|   \  |                         |   |__________
                \ |_________________________|
                 \|                      
                             
""")
    
    def movingLeft(previousEmoji, nextEmoji):
        return (f"""
                 /|                      
 __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   /  |                         |   |                   
           |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
 {previousEmoji}        | |              Left              | |        {nextEmoji}        
           |  \    ___________________________| |                  
 __________|   \  |                         |   |__________
                \ |_________________________|
                 \|                      
""" )


    def movingRight(previousEmoji, nextEmoji):
        return (f"""
                                         |\ 
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
           |   |                         |  \   |                   
           | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
 {previousEmoji}        | |            Right               | |        {nextEmoji}        
           | |___________________________    /  |                  
 __________|   |                         |  /   |__________
               |_________________________| /
                                         |/
""")

    def singleDeletion():
        return ("""
                             /\ 
               |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|   
               |           /    \           |                    
               |          /_    _\          |           
               |            |  |            |       
               |            |  |            |                  
               |            |  |            |   
               |____________|  |____________|
                            |__|
                             
""")
    def multipleDeletion(previousEmoji, nextEmoji):
        return (f"""
                             /\ 
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   |           /    \           |   |                   
           |   |          /_    _\          |   |                   
 {previousEmoji}        |   |            |  |            |   |        {nextEmoji}        
           |   |            |  |            |   |                  
 __________|   |            |  |            |   |__________
               |____________|  |____________|
                            |__|
""")















