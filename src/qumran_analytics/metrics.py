"""Simple, transparent sequence-error metrics for research text recognition.

References and predictions are Unicode-normalized identically. Neither string is
reversed: Hebrew is represented in its logical Unicode order.
"""
from __future__ import annotations
import unicodedata


def edit_distance(a, b) -> int:
    """Levenshtein distance for sequences (characters or tokens)."""
    previous = list(range(len(b) + 1))
    for i, x in enumerate(a, start=1):
        current = [i]
        for j, y in enumerate(b, start=1):
            current.append(min(current[-1] + 1, previous[j] + 1,
                               previous[j - 1] + (x != y)))
        previous = current
    return previous[-1]


def normalize(text: str, form: str = 'NFD', strip_combining: bool = False) -> str:
    """Normalize to NFC/NFD/NFKC/NFKD or leave untouched (NONE).

    Note: stripping combining marks is an *editorial policy choice* and must
    be preregistered for fair comparisons. Do not remove diacritics silently.
    """
    if form.upper() not in {'NFC', 'NFD', 'NFKC', 'NFKD', 'NONE'}:
        raise ValueError('Unknown Unicode normalization')
    value = text if form.upper() == 'NONE' else unicodedata.normalize(form.upper(), text)
    if strip_combining:
        value = ''.join(ch for ch in unicodedata.normalize('NFD', value)
                        if unicodedata.category(ch) != 'Mn')
    return value


def error_counts(reference: str, prediction: str, *, form: str = 'NFD',
                 strip_combining: bool = False) -> dict[str, int | float | None]:
    """Return edit counts and CER/WER for one aligned line.

    WER uses whitespace tokenization, which should be documented for Hebrew.
    Undefined denominators return None instead of silently returning zero.
    """
    ref = normalize(reference, form, strip_combining)
    pred = normalize(prediction, form, strip_combining)
    char_edits = edit_distance(ref, pred)
    word_ref, word_pred = ref.split(), pred.split()
    word_edits = edit_distance(word_ref, word_pred)
    return {'ref_chars': len(ref), 'char_edits': char_edits,
            'cer': char_edits / len(ref) if ref else None,
            'ref_words': len(word_ref), 'word_edits': word_edits,
            'wer': word_edits / len(word_ref) if word_ref else None}


def aggregate(lines: list[dict]) -> dict:
    """Return micro-averaged CER/WER across line dicts from error_counts."""
    rc = sum(int(line['ref_chars']) for line in lines)
    ce = sum(int(line['char_edits']) for line in lines)
    rw = sum(int(line['ref_words']) for line in lines)
    we = sum(int(line['word_edits']) for line in lines)
    return {'lines': len(lines), 'ref_chars': rc, 'char_edits': ce,
            'CER': ce / rc if rc else None,
            'ref_words': rw, 'word_edits': we,
            'WER': we / rw if rw else None}
