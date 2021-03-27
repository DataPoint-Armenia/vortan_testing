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

# TODO(sourencho): Convert these into commad line arguments
IN_FILE = "reformed_orth/rubina.wrong"
EXPECTED_FILE = "reformed_orth/rubina.sug"
SPELLCHECK_CMD = r"C:/Users/souren/AppData/Local/Microsoft/WindowsApps/python3.exe C:/Users/souren/Documents/code/vortan_testing/src/dummy_spellcheck.py"
TESTS_DIR = "./tests/"


@click.group()
def cli() -> None:
    pass


# run: todo docs
@click.command()
def run() -> None:
    # setup
    wrg_file, sug_file = _get_test_file_pair(TESTS_DIR, IN_FILE, EXPECTED_FILE)
    spellcheck_cmd = SPELLCHECK_CMD

    # test
    test_results = test(wrg_file, sug_file, spellcheck_cmd)

    # show results
    print(test_results)


# test: todo docs
def test(wrg_file, sug_file, spellcheck_cmd) -> Dict:
    n, bad, start_time = 0, 0, time.process_time()

    for sug_word, wrg_word in zip(sug_file, wrg_file):
        # words
        sug_word = sug_word.strip()
        wrg_word = wrg_word.strip()

        # spellcheck
        success = _spellcheck(spellcheck_cmd, sug_word, wrg_word)

        # stats
        n += 1
        bad += not success

    return dict(bad=bad, n=n, perc=float(100. - 100.*bad/n), elapsed=time.process_time()-start_time)


# Returns true if spellcheck was correct
def _spellcheck(spellcheck_cmd, sug_word, wrg_word) -> bool:
    proc = subprocess.Popen(
        spellcheck_cmd.split() + [wrg_word],
        stdout=subprocess.PIPE,
        shell=True)
    raw_result = proc.communicate()[0]

    result = raw_result.decode().strip()

    success = result == sug_word

    # TODO(sourencho): print this in a nice format in verbose mode
    print(
        f"in: '{wrg_word}', exp: '{sug_word}, out: '{result}', match: {success}")

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