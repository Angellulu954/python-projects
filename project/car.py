class Car:
    def __init__(self,model,year,colour,forsale):
        self.model=model
        self.year=year
        self.colour=colour
        self.forsale=forsale
    def drive(self):
        print(f"You drive the {self.colour} {self.model}")
    def stop(self):
        print(f"You stop the {self.colour} {self.model}")    
    def describe(self):
        print(f"{self.year} {self.colour} {self.model}")    