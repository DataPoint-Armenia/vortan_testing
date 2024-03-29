import click
import argparse
import os
import codecs
import unicodedata
from codecs import StreamReaderWriter
from typing import TextIO
from typing import Tuple
from typing import Dict
import subprocess
import time
import json


@click.group()
def cli() -> None:
    pass


# run: todo docs
@click.command()
@click.argument('test_dir', type=str)
@click.argument('wrong_file', type=str)
@click.argument('sug_file', type=str)
@click.argument('cmd', type=str)
def run(test_dir, wrong_file, sug_file, cmd) -> None:
    # setup
    wrg_file, sug_file = _get_test_file_pair(test_dir, wrong_file, sug_file)

    # test
    test_results = test(wrg_file, sug_file, cmd)

    # show results
    print(test_results)


# test: todo docs
def test(wrg_file, sug_file, spellcheck_cmd) -> Dict:
    n, bad = 0, 0
    time_start = time.time()

    for sug_word, wrg_word in zip(sug_file, wrg_file):
        # words
        sug_word = sug_word.strip()
        wrg_word = wrg_word.strip()

        # spellcheck
        success = _spellcheck(spellcheck_cmd, sug_word, wrg_word)

        # stats
        n += 1
        bad += not success

    time_end = time.time()

    return dict(bad=bad, n=n, perc=float(100. - 100.*bad/n), elapsed=time_end-time_start)


# Returns true if spellcheck was correct
def _spellcheck(spellcheck_cmd, sug_word, wrg_word) -> bool:
    proc = subprocess.Popen(
        spellcheck_cmd.split() + [wrg_word],
        stdout=subprocess.PIPE,
    )
    communicate = proc.communicate()
    raw_result = communicate[0]

    suggestions = json.loads(raw_result.decode('utf8'))['suggestions']

    success = sug_word in suggestions

    # TODO(sourencho): print this in a nice format in verbose mode
    print(f"in: '{wrg_word}', exp: '{sug_word}', out: '{suggestions}', match: {success}")

    return success


# Opens both files and returns their streams
def _get_test_file_pair(tests_dir: str,  in_filename: str, exp_filename: str) -> Tuple[StreamReaderWriter, StreamReaderWriter]:
    return (
        codecs.open(os.path.join(tests_dir, in_filename), encoding='utf-8'),
        codecs.open(os.path.join(tests_dir, exp_filename), encoding='utf-8')
    )


cli.add_command(run)

if __name__ == '__main__':
    cli()
