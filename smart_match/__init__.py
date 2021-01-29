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
        name = 'Levenshtein'
    if name == 'Levenshtein':
        return Levenshtein()
    if name == 'Euclidean':
        return EuclideanDistance()
    elif name == 'Damerau Levenshtein':
        return DamerauLevenshtein()
    elif name == "Overlap Coefficient":
        return OverlapCoefficient()
    elif name == "Generalized Overlap Coefficient":
        return GeneralizedOverlapCoefficient()
    elif name == "Longest Common Substring":
        return LongestCommonSubstring()
    elif name == "Longest Common SubSequence":
        return LongestCommonSubsequence()
    elif name == 'Block Distance':
        return BlockDistance()
    elif name == 'Cosine':
        return CosineSimilarity()
    elif name == 'Tanimoto Coefficient':
        return TanimotoCoefficient()
    elif name == 'Dice':
        return DiceSimilarity()
    elif name == 'Jaccard':
        return Jaccard()
    elif name == 'Generalized Jaccard':
        return GeneralizedJaccard()
    elif name == 'Hamming':
        return HammingDistance()
    elif name == 'Jaro':
        return Jaro()
    elif name == 'Jaro Winkler':
        return JaroWinkler()
    elif name == 'Simon White':
        return SimonWhite()
    elif name == 'Needleman Wunch':
        return NeedlemanWunch()
    elif name == 'Smith Waterman':
        return SmithWaterman()
    elif name == 'Smith Waterman Gotoh':
        return SmithWatermanGotoh()
    elif name == 'Exact':
        return Exact()
    elif name == 'Monge Elkan':
        return MongeElkan()
    else:
        raise NotImplementedError
        
def methods():
  return [
    'Levenshtein',
    'Euclidean',
    'Damerau Levenshtein',
    'Block Distance',
    'Cosine',
    'Tanimoto Coefficient',
    'Dice',
    'Simon White',
    'Longest Common Substring',
    'Longest Common SubSequence',
    'Overlap Coefficient',
    'Generalized Overlap Coefficient',
    'Jaccard',
    'Generalized Jaccard',
    'Hamming',
    'Jaro',
    'Jaro Winkler',
    'Needleman Wunch',
    'Smith Waterman',
    'Smith Waterman Gotoh',
    'Monge Elkan'
  ]
  

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
