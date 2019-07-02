#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from collections import Counter

import PythonCoursework

path = "sample_600k_lines.json"
sortKey = len

#Button click functions
def task2a(docID = ""):
    """Read files are received which contain the document ID docID, each reader's country is gathered in a list and then a histogram is created with this data"""
    if CheckVar.get():
        messagebox.showinfo(title="Help-task2a", message="Task2a (requires documentID) - Read files are received which contain the document ID docID, each reader's country is gathered in a list and then a histogram is created with this data")
    else:
        docID = docIDentry.get()
        files = PythonCoursework.loadFromFileDocID(path, docID)
        countries = PythonCoursework.getCountriesList(files)
        PythonCoursework.createHistogramOfCount(countries, "Histogram showing viewers of document with ID = {}\nper country".format(docID), "Countries", False)

def task2b():
    """Read files are received which contain the document ID docID, each reader's country is gathered in a list and then these countries are converted to their
    corresponding continets. A histogram of these continents is then produced"""
    if CheckVar.get():
        messagebox.showinfo(title="Help-task2b", message="Task2b (requires documentID) - Read files are received which contain the document ID docID, each reader's country is gathered in a list and then these countries are converted to their corresponding continets. A histogram of these continents is then produced")
    else:
        docID = docIDentry.get()
        files = PythonCoursework.loadFromFileDocID(path, docID)
        countries = PythonCoursework.getCountriesList(files)
        continents = PythonCoursework.getContinentList(countries)
        #PythonCoursework.createHistogramOfCount(continents, "Histogram showing viewerrs of document with ID = {}\nper continent".format(docID), "Continents", False)
        fullContinentNames = PythonCoursework.getFullContinentName(continents)
        PythonCoursework.createHistogramOfCount(fullContinentNames, "Histogram showing viewers of document with ID = {}\nper continent".format(docID), "Continents", True)

def task3a():
    """All read lines are returned from loadFromFileReadEvent and then the agents are extracted from these lines. A histogram is produced with this agent data."""
    if CheckVar.get():
        messagebox.showinfo(title="Help-task3a", message="Task3a - All read lines are returned from loadFromFileReadEvent and then the agents are extracted from these lines. A histogram is produced with this agent data.")
    else:
        readFiles = PythonCoursework.loadFromFileReadEvent(path)
        agents = PythonCoursework.getBrowserAgents(readFiles)
        PythonCoursework.createHistogramOfCount(agents, "Histogram showing which browsers have been used to 'read' files", "Browser", True)

def task3b():
    """All read lines are returned from loadFromFileReadEvent and then the agents identifying name only (i.e. Mozilla, Opera) is extracted. A histogram of these
    agents is then produced"""
    if CheckVar.get():
        messagebox.showinfo(title="Help-task3b", message="Task3b - All read lines are returned from loadFromFileReadEvent and then the agents identifying name only (i.e. Mozilla, Opera) is extracted. A histogram of these agents is then produced")
    else:
        readFiles = PythonCoursework.loadFromFileReadEvent(path)
        agentsNameOnly = PythonCoursework.getBrowserAgentsNameOnly(readFiles)
        PythonCoursework.createHistogramOfCount(agentsNameOnly, "Histogram showing which browsers have been used to 'read' files", "Browser", True)

def task4a():
    """All readers of a specified documentID are gathered and then a list of these readers is produced"""
    if CheckVar.get():
        messagebox.showinfo(title="Help-task4a", message="Task4a (requires documentID) - All readers of a specified documentID are gathered and then a list of these readers is produced")
    else:
        docID = docIDentry.get()
        readers = PythonCoursework.getAllReaders(docID, path)
        outputs = []
        for x in range(len(readers)):
            currOutput = "{}\n".format(readers[x])
            outputs.append(currOutput)
        messagebox.showinfo(title="List of all readers UUID that have read document with ID = {}".format(docID), message="".join(outputs))

def task4b():
    """All documents read by a specified user are gathered and then a list of these readers is produced"""
    if CheckVar.get():
        messagebox.showinfo(title="Help-task4b", message="Task4b (requires visitorID) - All documents read by a specified user are gathered and then a list of these readers is produced")
    else:
        visitorID = visitorIDentry.get()
        documents = PythonCoursework.getVisitorsReads(visitorID, path)
        outputs = []
        for x in range(len(documents)):
            currOutput = "{}\n".format(documents[x])
            outputs.append(currOutput)
        messagebox.showinfo(title="List of all documents read by user with ID = {}".format(visitorID), message="".join(outputs))

def task4c():
    """The also likes documents (those read by the same users that read the specified docID) are received from the getAlsoLikes function and a list of all these
    documents is produced. If a visitorID is provided, only the documents that user has also read will be returned."""
    if CheckVar.get():
        messagebox.showinfo(title="Help-task4c", message="Task4c (requires documentID, optional visitorID) - The also likes documents (those read by the same users that read the specified docID) are received from the getAlsoLikes function and a list of all these documents is produced. If a visitorID is provided, only the documents that user has also read will be returned.")
    else:
        docID = docIDentry.get()
        visitorID = visitorIDentry.get()
        if visitorID is "":
            alsoLikes = PythonCoursework.getAlsoLikes(docID, path, sortFunction=sortKey)
        else:
            alsoLikes = PythonCoursework.getAlsoLikes(docID, path, visitorUUID=visitorID, sortFunction=sortKey)
        outputs = []
        for x in range(len(alsoLikes)):
            currOutput = "{}\n".format(alsoLikes[x])
            outputs.append(currOutput)
        messagebox.showinfo(title="Readers of document with ID={} also like the following documents".format(docID), message="".join(outputs))


def task4d():
    """The also likes documents (those read by the same users that read the specified docID) are received from the getAlsoLikes function and then a list of the top 10
    matched documents is provided. The top 10 documents are the ones that are also read by multiple users that read the specified docID.
    A counter calculates how many users have also read another document and then this dictionary is used to calculate which documents are in the top 10."""
    if CheckVar.get():
        messagebox.showinfo(title="Help-task4d", message="Task4d (requires documentID, optional visitorID) - The also likes documents (those read by the same users that read the specified docID) are received from the getAlsoLikes function and then a list of the top 10 matched documents is provided. The top 10 documents are the ones that are also read by multiple users that read the specified docID. A counter calculates how many users have also read another document and then this dictionary is used to calculate which documents are in the top 10.")
    else:
        docID = docIDentry.get()
        visitorID = visitorIDentry.get()
        if visitorID is "":
            alsoLikes = PythonCoursework.getAlsoLikes(docID, path, sortFunction=sortKey)
        else:
            alsoLikes = PythonCoursework.getAlsoLikes(docID, path, visitorUUID=visitorID, sortFunction=sortKey)
        alsoLikesCount = Counter(alsoLikes)

        topAlsoLikes = []
        for x in alsoLikesCount:
            key = x
            value = alsoLikesCount[key]
            topAlsoLikes.append((key, value))

        if len(topAlsoLikes) < 10:
            limit = len(alsoLikesCount)
        else:
            limit = 10

        outputs = []
        for x in range(limit):
            currOutput = "{} other(s) also like - {}\n\n".format(topAlsoLikes[x][1], topAlsoLikes[x][0])
            outputs.append(currOutput)

        outputs.sort(reverse=True)
        messagebox.showinfo(title="Readers of document with ID={} also like the following documents".format(docID), message="".join(outputs))

def setPath400():
    """The file path in used is changed to sample_400k_lines.json"""
    if CheckVar.get():
        messagebox.showinfo(title="Help-400k", message="This would set the input file path to sample_400k_lines.json")
    else:
        path = "sample_400k_lines.json"
        messagebox.showinfo(title="File change", message="File path has been changed to sample_400k_lines.json")

def setPath600():
    """The file path in used is changed to sample_600k_lines.json"""
    if CheckVar.get():
        messagebox.showinfo(title="Help-600k", message="This would set the input file path to sample_600k_lines.json")
    else:
        path = "sample_600k_lines.json"
        messagebox.showinfo(title="File change", message="File path has been changed to sample_600k_lines.json")

def setPath3m():
    """The file path in used is changed to sample_3m_lines.json"""
    if CheckVar.get():
        messagebox.showinfo(title="Help-3m", message="This would set the input file path to sample_3m_lines.json")
    else:
        path = "sample_3m_lines.json"
        messagebox.showinfo(title="File change", message="File path has been changed to sample_3m_lines.json")

def sortlen():
    """The sort key to be used in getAlsoLikes is set to len"""
    if CheckVar.get():
        messagebox.showinfo(title="Help-sortLen", message="This would set the sort key used in getAlsoLikes to len")
    else:
        sortKey = len
        messagebox.showinfo(title="Sort change", message="Sorting key is now len")

def sortstrlower():
    """The sort key to be used in getAlsoLikes is set to str.lower"""
    if CheckVar.get():
        messagebox.showinfo(title="Help-sortstrlower", message="This would set the sort key used in getAlsoLikes to str.lower")
    else:
        sortKey = str.lower
        messagebox.showinfo(title="Sort change", message="Sorting key is now str.lower")


"""Below this line is the code required to create the GUI for the program. It is generated through the implementation of
simple labels, buttons and text entry boxes"""
#Create the window
window = Tk()
window.title("F20SC - Python Coursework")
window.configure(background = "black", width=750, height=450)

#Create labels
Label (window, text="F20SC - Python Coursework", bg="black", fg="white", font="none 18 bold").place(x=100, y=10, height=50, width=500)
Label (window, text="Document ID", bg="black", fg="white", font="none 12 bold").place(x=50, y=80)
Label (window, text="User ID", bg="black", fg="white", font="none 12 bold").place(x=50, y=120)

#Create text input boxes
docIDentry = Entry(window, width=50, bg="white")
docIDentry.place(x=200, y=80)

visitorIDentry = Entry(window, width=50, bg="white")
visitorIDentry.place(x=200, y=120)

#Create buttons
Button(window, text="Task2a", width=8, command=task2a).place(x=150, y=170)
Button(window, text="Task2b", width=8, command=task2b).place(x=150, y=210)
Button(window, text="Task3a", width=8, command=task3a).place(x=300, y=170)
Button(window, text="Task3b", width=8, command=task3b).place(x=300, y=210)
Button(window, text="Task4a", width=8, command=task4a).place(x=450, y=170)
Button(window, text="Task4b", width=8, command=task4b).place(x=450, y=210)
Button(window, text="Task4c", width=8, command=task4c).place(x=450, y=250)
Button(window, text="Task4d", width=8, command=task4d).place(x=450, y=290)
Button(window, text="400k lines", width=8, command=setPath400).place(x=150, y=350)
Button(window, text="600k lines", width=8, command=setPath600).place(x=300, y=350)
Button(window, text="3m lines", width=8, command=setPath3m).place(x=450, y=350)
Button(window, text="Sort key = len", width=10, command=sortlen).place(x=200, y=400)
Button(window, text="Sort key = str.lower", width=15, command=sortstrlower).place(x=375, y=400)

CheckVar = IntVar()
Check = Checkbutton(window, text = "Help", variable = CheckVar, onvalue = 1, offvalue = 0).place(x=5, y=5)

#Run the main loop
window.mainloop()
