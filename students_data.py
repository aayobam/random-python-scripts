class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, tracks: list, score: float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def get_student_details(self):
        print(f"INITIAL DATA = {self.name} {self.age} {self.tracks} {self.score}")

    def change_name(self, name):
        self.name = name
        print(f"NEW NAME = {self.name}")

    def change_age(self, age):
        self.age = age
        print(f"NEW AGE = {self.age}")

    def add_track(self, track):
        self.tracks.append(track)
        print(f"NEW TRACK LIST = {self.tracks}")
    
    def get_score(self):
        print(f"SCORE = {self.score}")

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.get_student_details()
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()