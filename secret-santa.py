# Secret Santa Generator

import sys, getopt
import random

def read_file( input_file_path ):
    contents = []
    input_file = open( input_file_path, 'r' )
    temp = input_file.read().splitlines()
    for line in temp:
        if line != '':
            contents.append( line )
    input_file.close()
    return contents


def pick( name, picked ):
    n = random.randint( 0, len( picked ) -1 )
    picked_person = picked[ n ]
    if picked_person == name:
        return pick( name, picked )
    else:
        return picked_person

def write_out_result( name, picked_person ):
    output_file = open( name + '.txt', 'w' )
    output_file.write( picked_person )
    output_file.close()


def picker( input_file_path ):
    names = read_file( input_file_path )
    picked = read_file( input_file_path )
    for name in names:
        picked_person = pick( name, picked )
        picked.remove( picked_person )
        write_out_result( name, picked_person )


def main( argv ):
    input_file_path = None
    try:
        opts, args = getopt.getopt( argv, "hi:", [ "ifile=" ] )
    except getopt.GetoptError:
        print( 'Run like: secret-santa.py -i <inputfilepath>' )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print( 'Run like: secret-santa.py -i <inputfilepath>' )
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file_path = arg
    if not input_file_path:
        print( 'Run like: secret-santa.py -i <inputfilepath>' )
        sys.exit(2)
    picker( input_file_path )


if __name__ == '__main__':
    main( sys.argv[ 1: ] )