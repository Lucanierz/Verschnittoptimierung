#!/usr/bin/python
# -*- coding:utf-8 -*-

import filehandler
import algorithmus
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true" )
parser.add_argument('-l', '--lengths', help='Input lengths in format \"-l 1,2,3\"', type=str)
parser.add_argument("-m", "--material", help="specify material", type=str)
parser.add_argument("-d", "--dimensions", help="specify dimensions", type=str)
parser.add_argument("-a", "--add", help="Account for width of saw blade", type=int)
parser.add_argument("-s", "--storage", help="Use custom storage, specify in format \"-s 1,2,3\"", type=str)
parser.add_argument("-Is", "--import_storage", help="Specify Path to storage file", type=str)
parser.add_argument("-Il", "--import_lengths", help="specify path to lengths file", type=str)
parser.add_argument("-e", "--export", help="specify filepath you want the output to be saved to", type=str)
parser.add_argument("-Rs", "--read_storage", help="read the storage file, you can specify material and dimensions to narrow output", action="store_true")
parser.add_argument("-Cs", "--check_storage", help="Check if certain dimensions, lengths or materials are available", action="store_true")

args = parser.parse_args()

if args.lengths != None:
    eingabe = [int(item) for item in args.lengths.split(',')]

if args.import_lengths != None:
    eingabe = list(map(int, filehandler.importfile(args.import_lengths).split(",")))
    print(eingabe)

if args.import_storage == None:
    filename = "default.json"

else:
    filename = args.import_storage

if not args.read_storage and not args.check_storage:

    if all(i <= 13000 for i in eingabe):

        if args.material == None or args.dimensions == None:

            if args.storage==None:
                print("specify material and dimensions or use custom storage")
                exit()

        if args.storage != None:
            lager = [int(item) for item in args.storage.split(',')]

        else:
            lager = filehandler.readinterm(args.material, args.dimensions, filename)

        if not args.add:
            args.add = 0

        data = algorithmus.kombinierterverschnitt(lager, eingabe, args.verbose, args.add)

        if args.verbose:
            print(data)
            print(data[1])
            print(lager)

        for i in range(len(data[0])):
            print("subset: " + str(data[0][i]) + " minverschnitt: " + str(min(data[1][i])) + " ausgelagert: " + str(lager[data[1][i].index(min(data[1][i]))]))

        if args.add != 0:
            for i in range(len(data[0])):
                print("subset: " + str(data[0][i]) + " minverschnitt: " + str(min(data[2][i])) + " ausgelagert: " + str(lager[data[2][i].index(min(data[2][i]))]) + " mit " + str(args.add) + "mm Saegeblatt")

        if args.export != None and args.export[-4:] == ".txt":
            filehandler.exportdata(data, args.export)

        if args.export != None and args.export[-4:] != ".txt":
            print("Could not export, hast to be .txt")

    else:
        print("Any length can't be over 13000")
        exit()

elif args.read_storage:

    lager = json.loads(filehandler.importfile(filename))
    key = list(lager.keys())
    lauf = -1

    if args.material == None and args.dimensions == None:
        print(json.dumps(lager, indent=4, sort_keys=True))

    if args.material != None and args.dimensions == None:
        print(json.dumps(lager[args.material], indent=4, sort_keys=True))

    if args.material != None and args.dimensions != None:
        print(json.dumps(lager[args.material][args.dimensions], indent=4, sort_keys=True))

    if args.material == None and args.dimensions != None:
        for obj in lager:
            lauf += 1
            print(key[lauf])
            print(json.dumps(lager[obj][args.dimensions], indent=4, sort_keys=True))

elif args.check_storage:

    lager = json.loads(filehandler.importfile(filename))
    key = list(lager.keys())

    for i in range (len(key)):
        dims = list(lager[key[i]].keys())
        print("Available dimensions for Material " + key[i] + ": " + ", ".join(dims))