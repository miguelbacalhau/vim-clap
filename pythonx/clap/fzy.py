#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vim

from .fzy_impl import fzy_scorer
from .myrustlib import fuzzy_match


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


def clap_fzy():
    #  query = vim.eval("a:query")
    #  candidates = vim.eval("a:candidates")
    #  print(query)
    #  return fuzzy_match(query, candidates)
    #  return fuzzy_match(vim.eval("a:query"), vim.eval("a:candidates"))
    return fuzzy_match_py(vim.eval("a:query"), vim.eval("a:candidates"))
