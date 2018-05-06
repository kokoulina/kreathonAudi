import random
import time
from google import google
import inspect

class Student():
    def __init__(self):
        self.name = "Ekaterina Kokoulina"
        self.origin = "Tyumen, Russland"
        self.age = 25
        self.skills = ["kreativ", "analytisch", "eigeninitiativ", "ehrlich", "motiviert", "neugierig", "objektiv und offen für andere kreative Loesungen"]
        self.problemsToSolve = []
        self.solvedProblems = []
        self.education = "Automatisierungstechnik im Master"

    def addProblem(self, problem):
        self.problemsToSolve.append(problem)

    def solveProblem(self, problem):
        try:
            self.problemsToSolve.remove(problem)
        except:
            self.beCreative(problem)
            self.problemsToSolve.remove(problem)
            self.solvedProblems.append(problem)

    def askColleague(self, problem):
        print("Hallo zusammen! Ich habe das Problem " + problem + "! Könnte jemand mir damit helfen?")
        if random.uniform(0, 1.0) < 0.1:
            return False
        return True

    def takeAPause(self):
        time.sleep(100)
        return True

    def makeResearch(self, problem):
        num_page = 3
        search_results = google.search(problem, num_page)
        print(search_results)
        for result in search_results:
            print(result.description)
        return True

    def beCreativ(self, problem):
        creativ = False
        while creativ == False:
            creativ = self.askColleague(problem) or self.takeAPause() or self.makeResearch(problem)

if __name__ == "__main__":
    student = Student()
    print("Sehr geehrte Damen und Herren")
    print("Mein Name ist ", student.name, ", Ich bin ", str(student.age), " Jahre alt und studiere ", student.education)
    print("Ich habe folgende Fähigkeiten: ")
    for skill in student.skills:
        print(skill)
    print("Ich kann noch folgendes machen: ")
    print(inspect.getmembers(Student))
    student.makeResearch("how to impress Audi Kreathon-Team?")
    print("Ich freue mich über eine Eiladung zum Kreathon.")
    print("Vielen Dank für Ihre Zeit und Aufmerksamkeit!")
    print("Mit freundlichen Grüßen, " + student.name)
