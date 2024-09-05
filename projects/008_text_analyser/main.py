from collections import Counter 

# 1. Create a function that handles opening files
def open_file(path: str) -> str:
    with open(path, 'r') as file:
        text: str = file.read()
        return text


# 2. Create a function that analyses any string
def analyse(text: str) -> dict[str, int | list[tuple[str,int]]]:
    result: dict[str, int | list[tuple[str,int]]] = {
        'total_chars_incl_spaces': len(text),
        'total_chars_excl_spaces': len(text.replace(' ', '')),
        'total_spaces': text.count(' '),
        'total_words': len(text.split()),
        'top_5_most_occured_words' : Counter(text.split()).most_common(5)
    }

    return result


# 3. Create a main entry point 
def main() -> None:
    text: str = open_file(path='projects/008_text_analyser/note.txt')
    analysis: dict[str, int | list[tuple[str,int]]] = analyse(text)

    # 4. Display the information
    # for key, value in analysis.items():
    #     print(f'{key}: {value}')

    print(f'Provided text totally contains {analysis.get('total_chars_incl_spaces')} characters out of which {analysis.get('total_spaces')} are whitespaces')
    print(f'Provided text contains {analysis.get('total_chars_excl_spaces')} characters excluding whitespaces')
    # print(f'Provided text contains {analysis.get('total_spaces')} whitespaces')
    print(f'Provided text contains {analysis.get('total_words')} words')
    print('The top 5 most occured words are')
    for word,count in analysis.get('top_5_most_occured_words'):
        print(f'{word} : {count}')

# 5. Run the script
if __name__ == '__main__':
    main()


"""
Homework:
1. Create a much more user friendly message regarding the analysis (eg. "This text file contains...").
2. Add the top 5 most common words to the analysis message.

"""