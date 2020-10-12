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
from .needleman_wunch import *
from .tanimoto_coefficient import *
from .gram import *
from .euclidean_distance import *
from .exact import *

_method = Levenshtein()
_level = 'char'
_verbose = False

def get_method(name=None):
    if not name:
        name = 'LE'
    if name == 'LE':
        return Levenshtein()
    if name == 'ED':
        return EuclideanDistance()
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
    elif name == 'TC':
        return TanimotoCoefficient()
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
    elif name == 'NW':
        return NeedlemanWunch()
    elif name == 'SW':
        return SmithWaterman()
    elif name == 'SWG':
        return SmithWatermanGotoh()
    elif name == 'EX':
        return Exact()
    elif name == 'ME':
        return MongeElkan()
    else:
        raise NotImplementedError

def set_params(level=None, verbose=False, *args, **kwargs):
    if level:
        global _level
        _level = level
    global _verbose
    _verbose = verbose 
    if args or kwargs:
        global _method
        _method.set_params(*args, **kwargs)

def use(name=None, level='char'):
    global _method
    _method = get_method(name)
    set_params(level)
    global _verbose
    if _verbose:
        print(f'mode change to {_method}[level={_level}]')
        
def tokenize(s, t):
    global _level
    if _level == 'char':
        return s, t
    elif _level == 'setterm':
        return list(s), list(t)
    elif _level == 'term':
        return s.split(), t.split()
    elif isinstance(_level, int):
        gram = Gram(q=_level)
        return gram.grams(s), gram.grams(t)
    else:
        return NotImplementedError

def similarity(s, t):
    global _method
    s, t = tokenize(s, t)
    return _method.similarity(s, t)

def dissimilarity(s, t):
    global _method
    s, t = tokenize(s, t)
    return _method.dissimilarity(s, t)

def distance(s, t):
    global _method
    s, t = tokenize(s, t)
    return _method.distance(s, t)

def score(s, t):
    global _method
    s, t = tokenize(s, t)
    return _method.score(s, t)
