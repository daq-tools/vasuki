# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# License: GNU Affero General Public License, Version 3
from gibberish import Gibberish


size_map = {'small': 1, 'medium': 2, 'large': 3}
generator = Gibberish()


def generate_gibberish(size=None):
    vowel_consonant_repeats = get_wordlength(size)
    return generator.generate_word(vowel_consonant_repeats=vowel_consonant_repeats)


def get_wordlength(selector):
    selector = selector or 'small'
    return size_map[selector]
