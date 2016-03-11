#! /usr/bin/env python

from __future__ import division, print_function
from itertools import izip


CODONS = {
        "TTT": "F",
        "TTC": "F",
        "TTA": "L",
        "TTG": "L",
        "CTT": "L",
        "CTC": "L",
        "CTA": "L",
        "CTG": "L",
        "ATT": "I",
        "ATC": "I",
        "ATA": "I",
        "ATG": "M",
        "GTT": "V",
        "GTC": "V",
        "GTA": "V",
        "GTG": "V",
        "TCT": "S",
        "TCC": "S",
        "TCA": "S",
        "TCG": "S",
        "CCT": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "ACT": "U",
        "ACC": "U",
        "ACA": "U",
        "ACG": "U",
        "GCT": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "TAT": "Y",
        "TAC": "Y",
        "CAT": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "AAT": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "GAT": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "TGT": "C",
        "TGC": "C",
        "TGG": "W",
        "CGT": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AGT": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GGT": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G",
        "TAA": ".",
        "TAG": ".",
        "TGA": "."

}


def reconstruct_protein_aligment(*args):
    """
    :type args: str
    :param args:
    :return:
    """


def transcript_amino_acid(*nucleotide_seq):
    """
    :type nucleotide_seq: str
    :param nucleotide_seq:
    :return:
    """
    current_triplet = []
    for char in nucleotide_seq:
        if nucleotide_seq.isalpha():
            current_triplet.append(char)
                if len(current_triplet) == 3 and current_triplet in dictionary_of_codes:
                        CODONS.get(value)
# Заступорилась на этом моменте. Не понимаю как воспользоваться методом get,
# а именно - как сделать, чтобы, найдя ключь в словаре, функция доставала
# его значение (понимаю, что писать (value) не прокатит, а как иначе - понять не могу)





