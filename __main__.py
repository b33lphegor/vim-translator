#!/usr/bin/env python3
import sys
from googletrans import Translator
from termcolor import colored


if __name__ == '__main__':
    try:
        if len(sys.argv) == 5:
            command_lines = ['-f', '-d']
            for command_arg in sys.argv:
                if command_arg in sys.argv:
                    dictionary_file = (sys.argv[2], 'r')
                    for dict_file in dictionary_file:
                        dict_file = dict_file.strip('\n')
                        # Create Translator object
                        translator = Translator()
                        # Translate lines
                        dict_file = translator.translate(dict_file,dest=str(sys.argv[4]))
                        print(colored(f'{dict_file.origin} => {dict_file.text}', 'blue'))
    except:
        sys.stderr.write(f'Usage {sys.argv[0]} : <example> -f file.txt -d eng \n')
    
    # chmod +x __main__.py
    # if sys.argv is greater than 2:
    #   create Translator object
    #   if -f isempty:
    #       output sorry file empty
    #   else:
    #       create Translator object
    #       open -f in read-mode and -f.strip(\n):
    #           create origin set translate(-f, dest=-d)
    #           output origin.text with colored blue|green
    # else:
    #   output usage <useage> script_name file.txt with colored redr