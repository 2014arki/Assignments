#! /usr/bin/env python

"""

"""
from __future__ import division, print_function

def fasta_reader(fp):
    """
    :param fp:
    :return:
    """
    pass

def hamming(seq1, seq2):
    """
    :type seq1: str
    :param seq1:
    :type seq2: str
    :param seq2:
    :return:
    """
    if len(seq1) != len(seq2):
        raise ValueError("")
    return sum(a != b for a, b in zip(seq1, seq2))

def matrix_mul(matr1, matr2):
    nrow_matr1, ncol_matr1 = len(matr1), len(matr1[0])
    nrow_matr2, ncol_matr2 = len(matr2), len(matr2[0])
    if ncol_matr1 != nrow_matr2:
        raise ValueError("")
    matrix_mult_res = [[None] for i in xrange(ncol_matr2)   #генер-р списков, влож-й в генер-р списков
                              for i in xrange(nrow_matr1)]
    def get_col(matr, j):
        return [row[j] for row in matr]
         



