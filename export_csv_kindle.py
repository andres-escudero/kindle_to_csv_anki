import csv
from deep_translator import DeeplTranslator
import sqlite3
# get a free API key from DeepL and paste it here.
your_api_key = "paste_api_key_here"
source_lang = 'es'
target_lang = 'en'
# Create a SQL connection to our SQLite database
con = sqlite3.connect("vocab.db")
cur = con.cursor()
# open the file in the write mode
f = open('anki_csv_output.csv', 'w')
# create the csv writer
writer = csv.writer(f, delimiter='\t')
# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute("SELECT * FROM LOOKUPS;"):
    # You can change the source/target languages if desired.
    term = row[1]
    term = term.replace(source_lang+':', '')
    translated = DeeplTranslator(api_key=your_api_key, source=source_lang, target=target_lang, use_free_api=True).translate(term)
    translatedSentence = DeeplTranslator(api_key=your_api_key, source=source_lang, target=target_lang, use_free_api=True).translate(row[5])
    # Make phrase/word bold in full sentence, if it exists.
    sentence = row[5]
    sentence = sentence.replace(term, "<b>"+term+"</b>")
    # Create new row with translation of term.
    newRow = [term, sentence, translated, translatedSentence]
    print (newRow)
    # write a row to the csv file
    writer.writerow(newRow)
f.close()
# Be sure to close the connection
con.close()