from .damerau_levenshtein import *
from .levenshtein import *
from .overlap_coefficient import *
from .generalized_overlap_coefficient import *
from .block_distance import *
from .cosine_similarity import *
from .dice_similarity import *
from .monge_elkan import *
from .jaccard import *
from .hamming_distance import *
from .generalized_jaccard import *
from .jaro import *
from .jaro_winkler import *
from .smith_waterman import *
from .smith_waterman_gotoh import *
from .simon_white import *
from .longest_common_substring import *
from .longest_common_subsequence import *

_method = Levenshtein()

def get_method(name=None):
    if not name:
        name = 'ED'
    if name == 'ED':
        return Levenshtein()
    elif name == 'DL':
        return DamerauLevenshtein()
    elif name == "OC":
        return OverlapCoefficient()
    elif name == "GOC":
        return GeneralizedOverlapCoefficient()
    elif name == "LCST":
        return LongestCommonSubstring()
    elif name == "LCSQ":
        return LongestCommonSubsequence()
    elif name == 'BD':
        return BlockDistance()
    elif name == 'cos':
        return CosineSimilarity()
    elif name == 'dice':
        return DiceSimilarity()
    elif name == 'jac':
        return Jaccard()
    elif name == 'gjac':
        return GeneralizedJaccard()
    elif name == 'HD':
        return HammingDistance()
    elif name == 'jaro':
        return Jaro()
    elif name == 'JW':
        return JaroWinkler()
    elif name == 'simon':
        return SimonWhite()
    elif name == 'SW':
        return SmithWaterman()
    elif name == 'SWG':
        return SmithWatermanGotoh()
    elif name == 'ME':
        return MongeElkan()
    else:
        raise NotImplementedError

def set_params(*args, **kwargs):
    global _method
    _method.set_params(*args, **kwargs )

def use(name=None, verbose=False):
    global _method
    _method = get_method(name)
    if verbose:
        print('mode change to', _method)

def similarity(s, t):
    global _method
    return _method.similarity(s, t)

def dissimilarity(s, t):
    global _method
    return _method.dissimilarity(s, t)

def distance(s, t):
    global _method
    return _method.distance(s, t)

def score(s, t):
    global _method
    return _method.score(s, t)
