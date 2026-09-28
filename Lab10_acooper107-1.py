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

class WordAnalyzer():
    def __init__(self, filepath):
        self.__path = Path(filepath)

        self.__word_freq = {}

    def process_file(self):
        if not self.__path.exists():
            print("Error: File not found.")
            return
        
        try:
            text = self.__path.read_text(encoding="utf-8")
        except FileNotFoundError:
            print("Error: File not found.")
            return
        except Exception as e:
            print(f"Unexpected error: {e}")
            return


    def print_report(self):
        pass




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
            program_end = True
            continue
        
        if option not in file_paths:
            print("Invalid choice. Try again")
            continue

        filepath = file_paths[option]

        analyzer = WordAnalyzer(filepath)
main()    