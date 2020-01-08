# coding: utf-8

import os
import re

from optparse import OptionParser

from pangu import spacing_file

def process(opt):
    path, file = opt.path, opt.file

    if path:
        file_with_paths = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(f)]
        for old_file_path in file_with_paths:
            call_pangu(old_file_path)
    elif file:
        call_pangu(file)
    else:
        print('I need a parameter!')
        print(parser.print_help())


def call_pangu(name):
    new_file_content = spacing_file(name)
    # Fix Markdown delete symbol
    new_file_content = re.sub(r'\~\~(\s)?(.*?)(\s)?\~\~',r'~~\2~~',new_file_content)
    # Fix Markdown bold(em) symbol
    new_file_content = re.sub(r'\*\*(\s)?(.*?)(\s)?\*\*',r'**\2**',new_file_content)
    # Fix Markdown italic symbol
    new_file_content = re.sub(r'\*(\s)?(.*?)(\s)?\*',r'*\2*',new_file_content)
    # OverWrite the original files
    with open(name, 'w', encoding='utf-8') as f:
        f.write(new_file_content)


def exe_main():
    parser = OptionParser(version="%prog 0.0.2")
    parser.add_option("-p", "--path", dest="path",
                      help="parse a directory", metavar="DIR")
    parser.add_option("-f", "--file", dest="file",
                      help="parse a file", metavar="FILE")
    options, args = parser.parse_args()

    process(options)
