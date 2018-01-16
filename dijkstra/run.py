#!/usr/bin/env python2
from graph import Graph
from dijkstra import dijkstra, shortest
import re, os, sys

def path_test(afile):
    if not os.path.exists(afile): 
        raise OSError, 'there was a problem opening/reading your file' 
    return afile

def process_file(afile):
    """turns file into a list of lists for build graph function"""
    try:
        with open(afile, 'rb') as ct:
            c = ct.read()
            return [[int(i) for i in re.split('\s', line)] for line in re.split('\n', c)]
    except IOError as e:
        print e, 'there was a problem opening/reading your file'

if __name__=='__main__':

    g = Graph()
    g.build_graph(process_file(path_test(sys.argv[1])))
    a1 = int(sys.argv[2])
    a2 = int(sys.argv[3])
    if g.vert_check(a1) != True or g.vert_check(a2) != True:
        print 'both nodes must be in graph'
    else:
        dijkstra(g, g.v1(a1), g.v1(a2)) 






