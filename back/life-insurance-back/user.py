class User:
    
    def __init__(self, name = None, age = None, dob = None, conditions = None, smoker = None, height = None, weight = None, occupation = None):
        self.name = name
        self.age = age
        self.dob = dob
        self.conditions = conditions
        self.smoker = smoker
        self.height = height
        self.weight = weight
        self.occupation = occupation
        
    # getter method 
    def get_name(self): 
        return self.name 
    
    def get_age(self): 
        return self.age 
    
    def get_dob(self): 
        return self.dob 
    
    def get_conditions(self): 
        return self.conditions
    
    def get_smoker(self): 
        return self.smoker 
    
    def get_height(self): 
        return self.height 
    
    def get_weight(self): 
        return self.weight
    
    def get_occupation(self): 
        return self.occupation
      
    # setter method 
    def set_name(self, x): 
        self.name = x
        
    def set_age(self, x): 
        self.age = x 
        
    def set_dob(self, x): 
        self.dob = x
        
    def set_conditions(self, x): 
        self.conditions = x
        
    def set_smoker(self, x): 
        self.smoker = x
        
    def set_height(self, x): 
        self.height = x
        
    def set_weight(self, x): 
        self.weight = x
        
    def set_occupation(self, x): 
        self.occupation = x
        
Essien = User()
Essien.set_age(20)
print(Essien)