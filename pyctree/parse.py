'''
parse.py

Parser to transform a python string into a raw python AST
'''

"""
parse :: String -> AST object
parses a string containing Python source and returns a raw Python AST
"""
def parse(pysource):
   return compile(pysource, "input to pyctree", "exec") 