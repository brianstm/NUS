# PE 01

"""
Question 1: DNA Transcription
"""

"""
1.1 Iterative Transcription
  Write the function to transcribe
  DNA to RNA iteratively
"""


def dna_transcription_I(dna):
    dna_to_rna = {'A': 'U', 'G': 'C', 'T': 'A', 'C': 'G'}
    rna = ''
    for dna_base in dna:
        rna += dna_to_rna[dna_base]
    return rna


# Test cases (comment out or remove before copying to Coursemology)
print(dna_transcription_I('AGCTGACGTA'))
print(dna_transcription_I('AGCAGGACT'))
print(dna_transcription_I('AAGGCCTT'))


"""
1.2 Recursive Transcription
  Write the function to transcribe
  DNA to RNA recursively
"""


def dna_transcription_R(dna):
    if dna == '':
        return ''
    dna_to_rna = {'A': 'U', 'G': 'C', 'T': 'A', 'C': 'G'}
    rna = ''
    dna_base = dna[0]
    rna += dna_to_rna[dna_base]

    return rna + dna_transcription_R(dna[1:])


# Test cases (comment out or remove before copying to Coursemology)
print(dna_transcription_R('AGCTGACGTA'))
print(dna_transcription_R('AGCAGGACT'))
print(dna_transcription_R('AAGGCCTT'))
