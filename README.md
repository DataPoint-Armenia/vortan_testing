# vortan_testing

## About

A program for testing the precision, accuracy and speed of Armenian spellcheckers.
Provides a suit of tests that measure performance in different scenarios.

## Documentation

-   **Technical Spec**: [link](https://docs.google.com/document/d/174XceYg-MSX32kfEz-C4bQx8zk43uHebvGSBaEduQWM/edit)
-   **Google Drive Folder**: [link](https://drive.google.com/drive/folders/1f1feyB_po6hS7TFvdvPWZ3Q6dSEDjklQ)
-   **Slack Channel**: [#vortan](https://datapointarmenia.slack.com/archives/C01LE2ADLFJ)

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

# for example
python3 ./src/test.py run ./tests/ reformed_orth/rubina.wrong reformed_orth/rubina.sug "node spellcheck.js suggest"
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

-   [@sourenp](https://github.com/sourenp)

## Acknowledgements
