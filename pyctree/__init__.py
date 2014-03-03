import analysis
import parse

"""
compile_to_ctree :: String -> [configuration object] -> Ctree object
Takes a string containing Python source code and compiles it into a
ctree object.
"""
def compile_to_ctree(pysource):
    sys.setrecursionlimit(100000)
    print 'Generating ctree...'
    raw_ast = parse(pysource)
    annotated_ast = analyze(raw_ast)
    c_ast = transform_to_ctree(annotated_ast)
    print 'Finished generating ctree'
    print '[elapsed time: %.2f seconds]' % (time.time() - t0)
    return c_ast