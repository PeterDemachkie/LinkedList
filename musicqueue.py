"""
Peter Demachkie
pdemachk@uscs.edu
https://github.com/PeterDemachkie/LinkedList.py
musicqueue.py
"""

from LinkedList import *
import random

def mainOptions():
    print("Options:")
    print("Options - Show options list")
    print("Print - Print the queue")
    print("Add - Add more songs to the queue")
    print("Remove - Remove a song from the queue")
    print("Delete - Delete the queue and start over")
    print("Shuffle - Shuffle the queue into random order")
    print("Play - Play the queue")
    print("Quit - Quit program")

def playOptions():
    print("Options - Print options list")
    print("Next - Skip forwards")
    print("Prev - Skip backwards")
    print("Exit - Exit the queue and return to main menu")

def addSongs(Queue):
    print("To add songs to the queue, simply enter the name of the song.")
    print("If you have no more songs to add, just hit enter.")
    addmusic = input("Song Name: ")

    while addmusic != "":
        Queue.append(addmusic)
        addmusic = input("Song Name: ")

def playQueue(Queue):
    Queue.moveFront()
    playOptions()
    print("Current Song: ", Queue.getFront())
    while True:
        answer = input("What would you like to do now? ")
        if answer == "Options":
            playOptions()

        if answer == "Next":
            if not Queue.getNext():
                print("Already at end of queue!")

            else:
                Queue.moveNext()
                print("Current Song: ", Queue.getCursor())

        if answer == "Prev":
            if not Queue.getPrev():
                print("Already at front of queue!")

            else:
                Queue.movePrev()
                print("Current Song: ", Queue.getCursor())

        if answer == "Exit":
            return

def main():
    Q = List() 
    addSongs(Q)
    mainOptions()
    answer = input("What would you like to do now? ")

    while answer != "":
        if answer == "Options":
            mainOptions()

        elif answer == "Print":
            print(Q)

        elif answer == "Add":
            addSongs(Q)

        elif answer == "Remove":
            # seek for song and delete it if it exists
            if Q.Length == 0:
                print("There are no songs in the queue!")

            else:
                song = input("What song would you like to remove: ")
                Q.moveFront()
                found = False
                while Q.getCursor() and not found:
                    if song == Q.getCursor():
                        print("Song successfully removed from queue")
                        Q.delete()
                        found = True
                        break
                    else:
                        Q.moveNext()
                if not found:
                    print("Song not in queue")

        elif answer == "Delete":
            Q.clear()
            addSongs(Q)

        elif answer == "Shuffle":
            shuffled = []
            Q.moveFront()

            while Q.getCursor():
                shuffled.append(Q.getCursor())
                Q.moveNext()

            random.shuffle(shuffled)
            Q.clear()

            for item in shuffled:
                Q.append(item)

        elif answer == "Play":
            if Q.Length() == 0:
                print("No songs in queue to play!")
            else:
                playQueue(Q)

        elif answer == "Quit":
            print("Thank you for listening")
            quit()

        else:
            print("Unrecognized answer, try again")

        answer = input("What would you like to do now? ")


if __name__ == "__main__":
    main()