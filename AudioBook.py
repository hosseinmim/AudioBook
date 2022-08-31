import pyttsx3
import PyPDF2


# read PDF file as a binary book
book = open('6min.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
# to know how many pages book have
pages = pdfReader.numPages
# print(pages)

speaker = pyttsx3.init()
engine = pyttsx3.init()

# set speed
rate = engine.getProperty('rate')
# print('rate')
engine.setProperty('rate', 120)

# set volume
volume = engine.getProperty('volume')
#print (volume)
engine.setProperty('volume', 1.0)

# change voice, 0 for male and 1 for female
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', voices[1].id)

# set start and finish page
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

# save audio as a .mp3 file
# engine.save_to_file('audiobook', 'test.mp3')
# engine.runAndWait()
