from collections import deque

class SmartPrinterQueue:
    def __init__(self):
        self.urgent = deque()
        self.normal = deque()

    
    def addJob(self, jobName, priority):
        if priority.upper() == "URGENT":
            self.urgent.append(jobName)
            print(f"Added URGENT Job: {jobName}")
        else:
            self.normal.append(jobName)
            print(f"Added Normal Job: {jobName}")

    
    def printJob(self):
        if self.urgent:
            job = self.urgent.popleft()
            print(f"Printing URGENT Job: {job}")

        elif self.normal:
            job = self.normal.popleft()
            print(f"Printing Normal Job: {job}")

        else:
            print("No jobs in queue.")

    
    def displayQueue(self):
        print("\nUrgent Queue :", list(self.urgent))
        print("Normal Queue :", list(self.normal))



printer = SmartPrinterQueue()

printer.addJob("Resume.pdf", "Normal")
printer.addJob("Project_Report.pdf", "URGENT")
printer.addJob("Assignment.docx", "Normal")
printer.addJob("Exam_Paper.pdf", "URGENT")

printer.displayQueue()

print("\nPrinting Jobs...\n")

printer.printJob()
printer.printJob()
printer.printJob()
printer.printJob()
printer.printJob()