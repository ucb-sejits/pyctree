import sys
import time

import analysis
import parse
import ctree

"""
compile_to_ctree :: String -> [configuration object] -> Ctree object
Takes a string containing Python source code and compiles it into a
ctree object.
"""
def compile_to_ctree(pysource):
    sys.setrecursionlimit(100000)
    t0 = time.time()

    print 'Generating ctree...'
    raw_ast = parse(pysource)
    annotated_ast = analysis.analyze(raw_ast)
    c_ast = ctree.transform_to_ctree(annotated_ast)
    
    print 'Finished generating ctree'
    print '[elapsed time: %.2f seconds]' % (time.time() - t0)
    return c_ast