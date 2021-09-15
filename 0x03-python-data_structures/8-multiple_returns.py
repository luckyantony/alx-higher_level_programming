#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence:
        len_5 = len(sentence)
        char = sentence[:1]
        return(len_5, char)
    else:
        sentence = None
        return(0, sentence)
