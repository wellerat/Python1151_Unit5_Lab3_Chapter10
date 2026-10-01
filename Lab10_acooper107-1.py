"""
Program Name:  Word Count

Purpose of program:

Author:
    Ann Cooper

Starter Code:
    No Started code, but the lab has 4 text files to query

Date:
    Oct. 1, 2026
"""

from pathlib import Path
import string

class WordAnalyzer():
    def __init__(self, filepath):
        self.__path = Path(filepath)
        self.__word_freq = {}

    def process_file(self):
        if not self.__path.exists():
            print("Error: File not found.")
            return
        
        try:
            extra_punctuation = "—–“”‘’…"
            delete_punctuation = str.maketrans("","",string.punctuation +extra_punctuation)

            with self.__path.open(encoding="utf-8") as file:
                for line in file:
                    clean_line = line.lower().translate(delete_punctuation)
                    words = clean_line.split()

                    for w in words:
                        if not w:
                            continue
                        self.__word_freq[w] = self.__word_freq.get(w, 0) +1

            return True
                
        except FileNotFoundError:
            print("\nError: File not found.")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False


    def print_report(self):
        
        if not self.__word_freq:
            print("No words were processed.")
            return

        print("\n------Word Frequency Report-----")

        for word in sorted(self.__word_freq.keys()):
            count = self.__word_freq[word]
            print(f"{word}:{count}")


def main():

    file_paths = {
        "1": Path("princess_mars.txt"),
        "2": Path("Tarzan.txt"),
        "3": Path("treasure_island.txt"),
        "4": Path("monte_cristo.txt")
    }

    program_end = False

    while not program_end:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        print("1. A Princess of Mars")
        print("2. Tarzan of the Apes")
        print("3. Treasure Island")
        print("4. The Count of Monte Cristo")
        print("5. Exit")

        option = input("Enter your choice (1-5):  ")

        if option =="5":
            print("\n\nGoodbye!")
            program_end = True
            continue
        
        if option not in file_paths:
            print("Invalid choice. Try again")
            continue

        filepath = file_paths[option]

        analyzer = WordAnalyzer(filepath)

        if analyzer.process_file():
            analyzer.print_report()
    
main()    