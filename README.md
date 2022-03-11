# kindle_to_csv_anki
This Python script automatically exports vocab builder lookups from Kindle (Paperwhite and Oasis) into a CSV file that you can easily import into Anki. It's perfect if you would like to do sentence mining with your kindle. It uses the DeepL API and the Python DeepTranslator library to automatically fetch translations of both the word in question and the entire sentence. It also automatically bolds the word in the context sentence to make it more readable.

You need to sign up for a free API Key from DeepL to use the script. You can also change the source/target languages if you want. The default is Spanish > English.

Steps to use:

1. Download the repo and install python.
2. Install the deep-translator libary: 'pip install -U deep-translator'.
3. Sign up for a free API Key at the DeepL website.
4. Paste your API key on line 5 of the 'export_csv_kindle.py' script, where it says 'paste_api_key_here'.
5. Change the source and target languages if you want. You have to use the 2-digit international language code - e.g. 'en' for English. You can change the source and target langues on lines 6-7 of the 'export_csv_kindle.py' script.
6. Save the script.
7. Plug your Kindle into your computer and search for the 'vocab.db' file. Drag it into the project directory.
8. Execute the script by typing 'python export_csv_kindle.py'.
9. After it runs, you will see a new CSV file in the same directory as the script. You can open this to prune it if needed, but it should be ready for immediate import into Anki. **The fields are as follows:**

Field 1: Word
Field 2: Context sentence with the word in bold.
Field 3: Translation of word in isolation.
Field 4: Translation of entire sentence. DeepL is really good at this. Now you have a more nuanced translation to use if you want to update the individual translation as well.

Be sure to allow HTML in fields when you're importing.
