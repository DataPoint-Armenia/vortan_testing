import random
import codecs
import click

IN_FILE = "reformed_orth/insert.sug"
OUT_FILE = "reformed_orth/insert.sug"
TESTS_DIR = "./tests/"

# Armenian unicode alphabet
ALPHABET = [u'\u0561', u'\u0562', u'\u0563', u'\u0564',
            u'\u0565', u'\u0566', u'\u0567', u'\u0568',
            u'\u0569', u'\u056A', u'\u056B', u'\u056C',
            u'\u056D', u'\u056E', u'\u056F', u'\u0570',
            u'\u0571', u'\u0572', u'\u0573', u'\u0574',
            u'\u0575', u'\u0576', u'\u0577', u'\u0578',
            u'\u0579', u'\u057A', u'\u057B', u'\u057C',
            u'\u057D', u'\u057E', u'\u057F', u'\u0580',
            u'\u0581', u'\u0582', u'\u0583', u'\u0584',
            u'\u0585', u'\u0586', u'\u0587']


class synthesizer:
    def __init__(self, mode):
        if mode == "delete":
            self.func = self.delete
        elif mode == "transpose":
            self.func = self.transpose
        elif mode == "replace":
            self.func = self.replace
        elif mode == "insert":
            self.func = self.insert
        else:
            raise ValueError('Unknown mode.')
        pass

    def split(self, word):
        return [(word[:i], word[i:]) for i in range(len(word) + 1)]

    def delete(self, word):
        splits = self.split(word)
        return [a + b[1:] for a, b in splits if b]

    def transpose(self, word):
        splits = self.split(word)
        return [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]

    def replace(self, word):
        splits = self.split(word)
        return [a + c + b[1:] for a, b in splits for c in ALPHABET if b]

    def insert(self, word):
        splits = self.split(word)
        return [a + c + b for a, b in splits for c in ALPHABET]

    def make_edit(self, word):
        return random.choice(self.func(word))

    def generate(self, filename):
        for word in codecs.open(filename, encoding='utf-8'):
            edit = self.make_edit(word.strip())
            if len(edit) != 0:
                print(edit)


@click.group()
def cli() -> None:
    pass


@click.command()
@click.argument('filename', type=str)
@click.argument('mode', type=str)
def generate(filename, mode) -> None:
    synth = synthesizer(mode)
    synth.generate(filename)


cli.add_command(generate)

if __name__ == '__main__':
    cli()
