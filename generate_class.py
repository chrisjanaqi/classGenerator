#!/usr/bin/env python3
"""
Simple adaptative script to generate c++ classes with header
"""
import argparse


ATTRIBS = "\t\t{type} {attribname};\n"

IOP_DEF = "\t\t{classname}& operator{op}=({classname}& other);\n"

ARITH_DEF = "{classname}& operator{op}({classname}& first, {classname}& second);\n"

COMP_DEF = "bool operator{op}({classname}& first, {classname}& second);\n"

IOP_IMPL = """
{classname}& {classname}::operator{op}=({classname}& other){
\t// TODO: fill this
}
"""

OPERATORS = ['+', '-', '*', '/', '%',               # Arithmetic operators
             '==', '!=', '>', '<', '>=', '<=']      # Comparison operators


def generate_class(classname: str, attributes: list, operators: list):
    raise NotImplementedError()


def build_parser():
    """
    Create the parser for command line arguments
    """
    parser = argparse.ArgumentParser(description='Generate c++ class')
    parser.add_argument('classname',
                        metavar='ClassName',
                        help='Name of the class to generate')
    parser.add_argument('-a', '--attribs',
                        nargs='+',
                        help='List of attributes of the class in the form :\
                        `type attributeName`, the list has to have an even \
                        number of arguments')
    parser.add_argument('-o', '--operators',
                        choices=OPERATORS,
                        metavar='OPERATORS',
                        nargs='+',
                        help='List of operator to write for the class, \
                        generates automatically the in place operators \
                        associated. Only handles intern operations.')
    parser.add_argument('-i', '--interactive',
                        action='store_true',
                        help='Build the class using an interactive CLI')
    return parser


def main():
    """
    main function
    """
    parser = build_parser()
    args = parser.parse_args()
    print(args)
    if !args.interactive:
        args.attribs = [] if args.attribs is None else args.attribs
        args.operators = [] if args.operators is None else args.operators
        generate_class(args.classname, args.attribs, args.operators)
        assert(len(args.attribs) % 2 == 0)



if __name__ == "__main__":
    main()
