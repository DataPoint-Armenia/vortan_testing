# vortan_testing

## About

Testing framework for precision, accuracy and speed of Armenian spellcheckers.

Provides a suit of tests that measure performance in different scenarios.

## Documentation

- [vortan_docs](https://github.com/DataPoint-Armenia/vortan_docs)

## Getting Started

This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

### Prereqs

-   [python3](https://www.python.org/downloads/)
-   [pip](https://pypi.org/project/pip/)

### Installation

1. Clone the repo

```
git clone git@github.com:DataPoint-Armenia/vortan_testing.git
```

2. Install requirements

```
pip install -r requirements.txt
```

## Usage

### Run test

```
# format
test.py run TEST_DIR WRONG_FILE SUG_FILE CMD

# Example that tests a spellchecker running on localhost
python3 ./src/test.py run ./tests/ reformed_orth/rubina.wrong reformed_orth/rubina.sug "bash util/get_sug_json.sh"

# Example that tests vortan_hyspell
python3 ./src/test.py run ./tests/ reformed_orth/rubina.wrong reformed_orth/rubina.sug "node path/vortan_hyspell/index.js correct"
```

### Syntesize test

```
# format
synthesize_test.py generate FILENAME MODE

# example
python3 src/synthesize_test.py generate tests/reformed_orth/transpose.sug transpose > tests/reformed_orth/transpose.wrong
```

Supported modes:

-   delete
-   transpose
-   replace
-   insert

## Contributors

-   [@sourencho](https://github.com/sourencho)

## Acknowledgements
