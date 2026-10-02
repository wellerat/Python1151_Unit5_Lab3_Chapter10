"""
Program Name:  Word Count

Purpose of program:
        This program displays the word count of all the words in a given
        text file called by the user.  The text file has to be a predefined 
        in the program. The terminal output lists the words in alphabetical
        order.

Author:
    Ann Cooper

Starter Code:
    No Starter code, but the lab has 4 text files to query

Date:
    Oct. 1, 2026
"""

from pathlib import Path
import string

class WordAnalyzer():
    """ A class that analyzes a text file and counts the frequency of each word"""
    
    def __init__(self, filepath: str | Path ) -> None:
        """ Initialization of the WordAnalyzer"""

        self.__path: Path = Path(filepath)
        self.__word_freq: dict[str, int] = {}

    def process_file(self) -> bool:
        """Method to process the file by taking out all of the punctuation,convert
           to lower case, splitting lines into words, counting the frequency of each word
           """
        
        if not self.__path.exists():
            print("Error: File not found.")
            return False
        
        try:
            extra_punctuation = "—–“”‘’…"
            delete_punctuation = str.maketrans("","",string.punctuation +extra_punctuation)

            with self.__path.open(encoding="utf-8") as file:
                for line in file:
                    clean_line = line.lower().translate(delete_punctuation)
                    words = clean_line.split()

                    for w in words:
                        self.__word_freq[w] = self.__word_freq.get(w, 0) +1

            return True
                
        except FileNotFoundError:
            print("\nError: File not found.")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False


    def print_report(self) -> None:
        """ Prints the report of all words and frequency of each word alphabetically"""

        if not self.__word_freq:
            print("No words were processed.")
            return

        print("\n------Word Frequency Report-----")

        for word in sorted(self.__word_freq.keys()):
            count = self.__word_freq[word]
            print(f"{word}:{count}")


def main() -> None:
    """ The main function which displays the menu, allows the user to respond,
        and coordinates the file processing and reporting."""
    
    file_paths: dict[str, Path] = {
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