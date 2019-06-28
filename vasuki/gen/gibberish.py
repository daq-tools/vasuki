# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# Apache License, Version 2
from gibberish import Gibberish


len_options = {'small': 1, 'medium': 2, 'large': 3}


def get_wordlength(selector):
    selector = selector or 'small'
    return len_options[selector]


def generate_gibberish(wordlength=None):
    vowel_consonant_repeats = get_wordlength(wordlength)
    return Gibberish().generate_word(vowel_consonant_repeats=vowel_consonant_repeats)
