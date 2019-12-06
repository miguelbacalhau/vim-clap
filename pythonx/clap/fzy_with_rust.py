#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import random
import re
import string

import myrustlib
from fzy_impl import fzy_scorer


def fuzzy_match_py(query, candidates):
    scored = []

    for c in candidates:
        score, indices = fzy_scorer(query, c)
        if score != float("-inf"):
            scored.append({'score': score, 'indices': indices, 'text': c})

    ranked = sorted(scored, key=lambda x: x['score'], reverse=True)

    indices = []
    filtered = []
    for r in ranked:
        filtered.append(r['text'])
        indices.append(r['indices'])

    return (indices, filtered)


query = 'sr'
candidates = open('/home/xlc/files.txt', 'r').read().split('\n')[:100]

print(fuzzy_match_py(query, candidates))
print(myrustlib.fuzzy_match(query, candidates))


def test_pure_python(benchmark):
    print(benchmark(fuzzy_match_py, query, candidates))


def test_rust(benchmark):
    print(benchmark(myrustlib.fuzzy_match, query, candidates))
