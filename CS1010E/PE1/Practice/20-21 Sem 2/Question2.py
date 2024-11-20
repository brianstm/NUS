# PE 01

"""
Question 2: RNA Translation
"""

"""
2.1 RNA Segment
  Write the function to find
  the translated region
"""


def rna_segment(rna):
    new_rna = ''
    for i in range(len(rna)):
        base = rna[i:i+2]
        if base == 'UU' or base == 'UG':
            new_rna = rna[i:]
            break
    for i in range(0, len(new_rna), 2):
        base = new_rna[i:i+2]
        if base == 'AC' or base == 'AA':
            new_rna = new_rna[:i+2]
            break
    return new_rna


# Test cases (comment out or remove before copying to Coursemology)
print(rna_segment('AUGUUAUAAACUU'))
print(rna_segment('GUUGAAGUACAAAG'))


"""
2.2 Polypeptide Property
  Write the function to find
  the property of a polypeptide
"""


def poly_property(poly):
    poly_property_dict = {'F': 'acidic', 'L': 'non-polar', 'M': 'basic', 'S': 'polar', 'P': 'acidic',
                          'T': 'polar', 'Y': 'polar', 'O': 'non-polar', 'A': 'basic', 'Q': 'acidic', 'C': 'basic', 'R': 'basic'}
    result = {'acidic': 0, 'basic': 0, 'polar': 0, 'non-polar': 0}
    for i in range(len(poly)):
        if poly[i] in poly_property_dict:
            result[poly_property_dict[poly[i]]] = result.get(
                poly_property_dict[poly[i]], 0) + 1
    if result['acidic'] > result['basic']:
        return 'Acidic'
    elif result['acidic'] < result['basic']:
        return 'Basic'
    elif result['polar'] > result['non-polar']:
        return 'Polar'
    else:
        return 'Neutral'


# Test cases (comment out or remove before copying to Coursemology)
print(poly_property('FM'))
print(poly_property('YSF'))
print(poly_property('FXM'))
