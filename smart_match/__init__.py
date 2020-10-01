from .damerau_levenshtein import *
from .levenshtein import *
from .overlapcoefficient import *
from .generalizedoverlapcoefficient import *
from .block_distance import *
from .cosine_similarity import *
from .dice_similarity import *
from .monge_elkan import *
from .jaccard import *
from .hamming_distance import *
from .generalized_jaccard import *
from .jaro import *
from .jaro_winkler import *
from .smith_waterman_gotoh import *
from .simon_white import *

_method = Levenshtein()

def get_method(name=None, verbose=False):
    if not name:
        name = 'ED'
    if name == 'ED':
        if verbose:
            print('mode change to Levenshtein')
        return Levenshtein()
    elif name == 'DL':
        if verbose:
            print('mode change to DamerauLevenshtein')
        _method = DamerauLevenshtein()    
    elif mode == "OC":
        _method = OverlapCoefficient()
    elif mode == "GOC":
        _method = GeOverlapCoefficient()
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
    elif name == 'HD':
        if verbose:
            print('mode change to HammingDistance')
        return HammingDistance()
    elif name == 'jaro':
        if verbose:
            print('mode change to Jaro')
        return Jaro()
    elif name == 'JW':
        if verbose:
            print('mode change to JaroWinkler')
        return JaroWinkler()
    elif name == 'simon':
        if verbose:
            print('mode change to SimonWhite')
        return SimonWhite()
    elif name == 'SWG':
        if verbose:
            print('mode change to SmithWatermanGotoh')
        return SmithWatermanGotoh()
    elif name == 'ME':
        if verbose:
            print('mode change to MongeElkan')
        return MongeElkan()
    else:
        raise NotImplementedError

def set_params(*args, **kwargs):
    _method.set_params(*args, **kwargs )

def use(name=None, verbose=False):
    global _method
    _method = get_method(name, verbose)

def similarity(s, t):
    global _method
    return _method.similarity(s, t)

def dissimilarity(s, t):
    global _method
    return _method.dissimilarity(s, t)

def distance(s, t):
    global _method
    return _method.distance(s, t)
