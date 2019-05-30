#!/usr/bin/env python3
"""
Simple adaptative script to generate c++ classes with header
"""
import argparse


ATTRIBS = "\t\t{type} {name};\n"

OPERATORS = ['+', '-', '*', '/', '%',               # Arithmetic operators
             '==', '!=', '>', '<', '>=', '<=']      # Comparison operators

OUTPUT_DIR = "output/"

def chunks(iterable: list, chunksize: int):
    for i in range(0, len(iterable), chunksize):
        yield iterable[i:i+chunksize]


def generate_class(classname: str, attributes: list, operators: list):
    output_cpp = "".join([output, classname, '.cpp'])
    output_h = "".join([output, classname, '.h'])
    # Reading template files
    with open('template.cpp', 'r') as file:
        template_cpp: str = file.read()
    with open('template.h', 'r') as file:
        template_h: str = file.read()
    with open('ioperator.def', 'r') as file:
        template_iop_def: str = file.read()
    with open('ioperator.impl', 'r') as file:
        template_iop_impl: str = file.read()
    with open('operator.def', 'r') as file:
        template_op_def: str = file.read()
    with open('operator.impl', 'r') as file:
        template_op_impl: str = file.read()

    attribs = "".join([ATTRIBS.format(type=a_type, name=a_name) for a_type, a_name in chunks(attributes, 2)])
    iop_impl = "".join([template_iop_impl.format(classname=classname, op=op) for op in operators])
    iop_def = "".join([template_iop_def.format(classname=classname, op=op) for op in operators])
    op_impl = "".join([template_op_impl.format(classname=classname, op=op) for op in operators])
    op_def = "".join([template_iop_def.format(classname=classname, op=op) for op in operators])

    class_cpp = template_cpp.format(
            classname=classname,
            ioperators_impl=iop_impl,
            operators_impl=op_impl
    )
    class_h = template_h.format(
            up_classname=classname.upper(),
            classname=classname,
            attributes=attribs,
            ioperators_def=iop_def,
            operators_def=op_def
    )
    with open(output_cpp, 'w') as output:
        output.write(class_cpp)
    with open(output_h, 'w') as output:
        output.write(class_h)


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
    if not args.interactive:
        args.attribs = [] if args.attribs is None else args.attribs
        args.operators = [] if args.operators is None else args.operators
        generate_class(args.classname, args.attribs, args.operators)
        assert(len(args.attribs) % 2 == 0)
        generate_class(args.classname, args.attribs, args.operators)


if __name__ == "__main__":
    main()

