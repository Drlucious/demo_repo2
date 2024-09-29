import csv
import xml.sax
import requests

import schedule
import tornado.gen

r = requests.get('https://commons.wikimedia.org/wiki/File:Shark_scare_(535163908).jpg')

print(r.headers)

# projects = [{"student": "99 bottles"},{"student": "timetable"},
#             {"student": "Magic ball 8"}, {"student": "Pythagorean Triple checker"},
#             {"student": "Rock Paper Scissors"}, {"student": "Coin Estimator"},
#             {"student": "Mad libs Story Maker"}, {"student": "Change Calculator"},
#             {"student": "Mean,Median,Mode"}, {"student": "Guessing Game"},
#             {"student": "Multiplication table"}, {"student": "fibonacci sequence"},
#             {"student": "Base jumper"}, {"student": "Hangman Jumper"},
#             {"student": "Menu Calculator"}, {"student": "BMI index calculator"},
#             {"student": "Dice rolling simulator"}, {"student": "Factors of a number"},
#             {"student": "Countdown Clock"}, {"student": "Random Wikipedia Article"},
#             {"student": "Weather"}, {"student": "Blackjack"},
#             {"student": "Sierpinski triangle"}, {"student": "Amazon Price tracker"},
#             {"student": "Music Player"}, {"student": "Reddit Bot"}]
#
# with open("ProjectSpace.csv", mode='w') as csvfile:
#     classnames = projects[0].keys()
#     writer = csv.DictWriter(csvfile, fieldnames=classnames)
#     for row in projects:
#         writer.writerow(row)
#

class PeopleHandler(xml.sax.ContentHandler):

     def startElement(self, name, attrs):
         self.current = name
         if name == "person":
             print(f"--Person{attrs['id']} --")
     def characters(self, content):
         if self.current == "name":
            self.name = content
         elif self.current == "age":
            self.age = content
         elif self.current == "weight":
            self.weight = content
         elif self.current == "height":
            self.height = content

     def endElement(self,name):
         if self.current == "name":
            print(f"Name:{self.name}")
         elif self.current == "age":
             print(f"Age:{self.age}")
         elif self.current == "weight":
             print(f"Weight:{self.weight}")
         elif self.current == "height":
             print(f"Height:{self.height}")
         self.current = ""
