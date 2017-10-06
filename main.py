#!/usr/bin/env python

__author__ = "Jeanna Clark"
__version__ = "1.0"


def main():
    describe_morse_code()
    convert_string()


def describe_morse_code():
    print("According to Wikipedia's Morse Code web page (https://en.wikipedia.org/wiki/Morse_code), International "
          "Morse Code is comprised of letters and numerals")
    print("\n\t'International Morse Code:'")
    print("\n\t\t'1. The length of a dot is one unit.'")
    print("\n\t\t'2. A dash is three units.'")
    print("\n\t\t'3. The space between parts of the same letter is one unit.")
    print("\n\t\t'4. The base between letters is three units.'")
    print("\n\t\t'5. The space between words is seven units.'")
    print("\nNOTE: each morse code unit of 'space' is represented as a caret symbol '^' for readability purposes")
    print("NOTE: each morse code unit of 'dash' will be represented by consecutive dash symbols '-' for "
          "readability purposes")
    print("NOTE: each morse code unit of 'dot' is represented as a asterick symbol '*' for readability purposes")
    print("NOTE: there are three different morse code dictionaries for America, Continential & International; this "
          "translator implements International Morse Code")
    print("NOTE: punctuation appears to be stripped from the International Morse Code according to Wikipedia "
          "translation chart, so punctionation latin characters are not translated")


def convert_string():
    input_string = input("\nPlease enter a latin alphabet string you would like converted to morse code: ")
    morse_string = ''
    for i in range(0, len(input_string)-2):
        morse_string += convert_latin_letter_to_morse_symbol(input_string[i])
        if (not input_string[i] == ' ') and (not input_string[i + 1] == ' '):
            morse_string += '^^^'
    morse_string += convert_latin_letter_to_morse_symbol(input_string[len(input_string)-1])
    print("\nOriginal Latin Alphabet String: " + input_string)
    print("Translated Morse Code: " + morse_string)


def convert_latin_letter_to_morse_symbol(latin_letter):
    # International Morse Code Symbol translation sourced from https://en.wikipedia.org/wiki/Morse_code
    morse_code_dictionary = {
                                'a': '*^---',
                                'b': '---^*^*^*',
                                'c': '---^*^---^*',
                                'd': '---^*^*',
                                'e': '*',
                                'f': '*^*^---^*',
                                'g': '---^---^*',
                                'h': '*^*^*^*',
                                'i': '*^*',
                                'j': '*^---^---^---',
                                'k': '---^*^---',
                                'l': '*^---^*^*',
                                'm': '---^---',
                                'n': '---^*',
                                'o': '---^---^---',
                                'p': '*^---^---^*',
                                'q': '---^---^*^---',
                                'r': '*^---^*',
                                's': '*^*^*',
                                't': '---',
                                'u': '*^*^---',
                                'v': '*^*^*^---',
                                'w': '*^---^---',
                                'x': '---^*^*^---',
                                'y': '---^*^---^---',
                                'z': '---^---^*^*',
                                'A': '*^---',
                                'B': '---^*^*^*',
                                'C': '---^*^---^*',
                                'D': '---^*^*',
                                'E': '*',
                                'F': '*^*^---^*',
                                'G': '---^---^*',
                                'H': '*^*^*^*',
                                'I': '*^*',
                                'J': '*^---^---^---',
                                'K': '---^*^---',
                                'L': '*^---^*^*',
                                'M': '---^---',
                                'N': '---^*',
                                'O': '---^---^---',
                                'P': '*^---^---^*',
                                'Q': '---^---^*^---',
                                'R': '*^---^*',
                                'S': '*^*^*',
                                'T': '---',
                                'U': '*^*^---',
                                'V': '*^*^*^---',
                                'W': '*^---^---',
                                'X': '---^*^*^---',
                                'Y': '---^*^---^---',
                                'Z': '---^---^*^*',
                                '0': '---^---^---^---^---',
                                '1': '*^---^---^---^---',
                                '2': '*^*^---^---^---',
                                '3': '*^*^*^---^---',
                                '4': '*^*^*^*^---',
                                '5': '*^*^*^*^---',
                                '6': '---^*^*^*^*',
                                '7': '---^---^*^*^*',
                                '8': '---^---^---^*^*',
                                '9': '---^---^---^---^*',
                                ' ': '^^^^^^^',
                                '!': '',
                                '@': '',
                                '#': '',
                                '$': '',
                                '%': '',
                                '^': '',
                                '&': '',
                                '*': '',
                                '(': '',
                                ')': '',
                                '-': '',
                                '+': '',
                                '=': '',
                                '|': '',
                                '\\': '',
                                '~': '',
                                '`': '',
                                '[': '',
                                ']': '',
                                ':': '',
                                ';': '',
                                '>': '',
                                '<': '',
                                ',': '',
                                '.': '',
                                '?': '',
                                '/': '',
                                '_': '',
                                '"': '',
                                '': '',
                                '{': '',
                                '}': ''
                            }
    return morse_code_dictionary[latin_letter]


if __name__ == '__main__':
    main()
