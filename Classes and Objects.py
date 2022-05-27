class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name="Bob", age=26, tracks=["FE","BE"],score=20.90):
        self.name = name
        self.age  = age
        self.tracks = tracks
        self.score = score
    def changeNam(self, new_name):
        self.name = new_name
    
    def cahngeAge(self, new_age):
        self.age = new_age
    
    def addTrack(self,new_track):
        self.tracks = new_track
    
    def get_score(self):
        if isinstance(self.age, int):
            print(self.name, self.age, self.tracks, self.score)
        else:
            print('The age is not integer, Try Integer numbers as age')
            

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.changeNam("Peter")
Bob.cahngeAge(34)
Bob.addTrack("UI/UX")
Bob.get_score()
