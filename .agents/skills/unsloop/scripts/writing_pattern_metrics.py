#!/usr/bin/env python3
"""Calculate transparent writing-pattern measurements without inferring AI authorship."""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Sequence


WORD_RE = re.compile(r"[^\W_]+(?:['’][^\W_]+)*", re.UNICODE)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
PARAGRAPH_SPLIT_RE = re.compile(r"(?:\r?\n)\s*(?:\r?\n)+")


def words(text: str) -> list[str]:
    return [match.group(0).casefold() for match in WORD_RE.finditer(text)]


def sentences(text: str) -> list[str]:
    return [part.strip() for part in SENTENCE_SPLIT_RE.split(text.strip()) if words(part)]


def paragraphs(text: str) -> list[str]:
    return [part.strip() for part in PARAGRAPH_SPLIT_RE.split(text.strip()) if words(part)]


def distribution(values: Sequence[int]) -> dict[str, float | int | None]:
    if not values:
        return {"minimum": None, "maximum": None, "mean": None, "median": None, "population_standard_deviation": None}
    return {
        "minimum": min(values),
        "maximum": max(values),
        "mean": round(statistics.fmean(values), 3),
        "median": round(float(statistics.median(values)), 3),
        "population_standard_deviation": round(statistics.pstdev(values), 3),
    }


def repeated_sequences(tokens: Sequence[str], size: int, minimum: int, limit: int) -> list[dict[str, int | str]]:
    counts = Counter(tuple(tokens[index:index + size]) for index in range(max(0, len(tokens) - size + 1)))
    ordered = sorted(
        ((phrase, count) for phrase, count in counts.items() if count >= minimum),
        key=lambda item: (-item[1], item[0]),
    )
    return [{"phrase": " ".join(phrase), "count": count} for phrase, count in ordered[:limit]]


def count_token_sequence(tokens: Sequence[str], target: Sequence[str]) -> int:
    if not target or len(target) > len(tokens):
        return 0
    width = len(target)
    return sum(1 for index in range(len(tokens) - width + 1) if list(tokens[index:index + width]) == list(target))


def analyze(
    text: str,
    *,
    identifier: str,
    phrase_size: int = 3,
    minimum_repeat: int = 2,
    top: int = 20,
    opening_words: int = 3,
    transitions: Sequence[str] = (),
) -> dict[str, object]:
    token_list = words(text)
    sentence_list = sentences(text)
    paragraph_list = paragraphs(text)
    sentence_lengths = [len(words(sentence)) for sentence in sentence_list]
    paragraph_sentence_counts = [len(sentences(paragraph)) for paragraph in paragraph_list]

    opening_counts = Counter(tuple(words(sentence)[:opening_words]) for sentence in sentence_list if words(sentence))
    repeated_openings = sorted(
        ((opening, count) for opening, count in opening_counts.items() if count >= minimum_repeat),
        key=lambda item: (-item[1], item[0]),
    )

    transition_counts = []
    for transition in transitions:
        target = words(transition)
        transition_counts.append(
            {
                "transition": transition,
                "normalized": " ".join(target),
                "count": count_token_sequence(token_list, target),
            }
        )

    return {
        "schema_version": "1.0",
        "assessment": "Writing-pattern measurements",
        "input_identifier": identifier,
        "authorship_boundary": "Not assessable from prose alone",
        "measurements": {
            "word_count": len(token_list),
            "sentence_count": len(sentence_list),
            "paragraph_count": len(paragraph_list),
            "sentence_length_words": distribution(sentence_lengths),
            "paragraph_length_sentences": distribution(paragraph_sentence_counts),
            "repeated_phrases": repeated_sequences(token_list, phrase_size, minimum_repeat, top),
            "repeated_sentence_openings": [
                {"opening": " ".join(opening), "count": count}
                for opening, count in repeated_openings[:top]
            ],
            "requested_transition_counts": transition_counts,
        },
        "method": {
            "word_rule": "Unicode letter/number sequences with internal apostrophes, case-folded",
            "sentence_rule": "Split on whitespace following period, exclamation mark, or question mark",
            "paragraph_rule": "Split on one or more blank lines",
            "repeated_phrase_rule": f"Sliding {phrase_size}-word sequences across the normalized token stream; minimum count {minimum_repeat}",
            "sentence_opening_rule": f"First {opening_words} normalized words; minimum count {minimum_repeat}",
            "transition_rule": "Exact normalized token-sequence match for each user-supplied transition",
        },
        "limitations": [
            "Sentence splitting is heuristic and may split abbreviations or miss unconventional punctuation.",
            "Repeated phrases may cross sentence or paragraph boundaries.",
            "Counts depend on the supplied text, parameters, language, genre, formatting, and extraction quality.",
            "These measurements describe textual regularity and do not determine human or AI authorship.",
        ],
    }


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("value must be at least 1")
    return parsed


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="UTF-8 text file, or - for standard input")
    parser.add_argument("--phrase-size", type=positive_int, default=3, help="words per repeated phrase (default: 3)")
    parser.add_argument("--min-repeat", type=positive_int, default=2, help="minimum repeated count (default: 2)")
    parser.add_argument("--top", type=positive_int, default=20, help="maximum repeated items per list (default: 20)")
    parser.add_argument("--opening-words", type=positive_int, default=3, help="words in a sentence opening (default: 3)")
    parser.add_argument("--transition", action="append", default=[], help="literal transition phrase to count; repeat as needed")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.input == "-":
        content = sys.stdin.read()
        identifier = "<stdin>"
    else:
        path = Path(args.input)
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            print(f"ERROR unable to read UTF-8 input: {exc}", file=sys.stderr)
            return 2
        identifier = path.name

    result = analyze(
        content,
        identifier=identifier,
        phrase_size=args.phrase_size,
        minimum_repeat=args.min_repeat,
        top=args.top,
        opening_words=args.opening_words,
        transitions=args.transition,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
