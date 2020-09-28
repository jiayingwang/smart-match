from .damerau_levenshtein import *
from .levenshtein import *
from .block_distance import *
from .cosine_similarity import *
from .dice_similarity import *
from .monge_elkan import *
from .jaccard import *
from .hamming_distance import *
from .generalized_jaccard import *
from .jaro import *
from .jarowinkler import *

_method = Levenshtein()

def get_method(name=None, inner_method=None, verbose=False):
    if not name:
        name = 'ED'
    if name == 'ED':
        if verbose:
            print('mode change to Levenshtein')
        return Levenshtein()
    elif name == 'DL':
        if verbose:
            print('mode change to DamerauLevenshtein')
        return DamerauLevenshtein()
    elif name == 'BD':
        if verbose:
            print('mode change to BlockDistance')
        return BlockDistance()
    elif name == 'cos':
        if verbose:
            print('mode change to CosineSimilarity')
        return CosineSimilarity()
    elif name == 'dice':
        if verbose:
            print('mode change to DiceSimilarity')
        return DiceSimilarity()
    elif name == 'jac':
        if verbose:
            print('mode change to Jaccard')
        return Jaccard()
    elif name == 'gjac':
        if verbose:
            print('mode change to GeneralizedJaccard')
        return GeneralizedJaccard()
    elif name=='HD':
        if verbose:
            print('mode change to HammingDistance')
        return HammingDistance()
    elif name=='jaro':
        if verbose:
            print('mode change to Jaro')
        return Jaro()
    elif name=='JW':
        if verbose:
            print('mode change to JaroWinkler')
        return JaroWinkler()
    elif name == 'ME':
        if verbose:
            print('mode change to MongeElkan')
        return MongeElkan(inner_method)
    else:
        raise NotImplementedError
    

def use(name=None, inner_method=None, verbose=False):
    global _method
    _method = get_method(name, inner_method, verbose)

def similarity(s, t):
    global _method
    return _method.similarity(s, t)

def dissimilarity(s, t):
    global _method
    return _method.dissimilarity(s, t)

def distance(s, t):
    global _method
    return _method.distance(s, t)
