import logging 

logger = logging.getLogger(__name__)

class Error(Exception):
    pass

#make dictionary? for nucleotides to codon

codon_table = {
    # Phenylalanine (F), Leucine (L)
    "uuu": "F", "uuc": "F", "uua": "L", "uug": "L",
    "cuu": "L", "cuc": "L", "cua": "L", "cug": "L",

    # Isoleucine (I), Methionine (M) - start codon
    "auu": "I", "auc": "I", "aua": "I", "aug": "M",

    # Valine (V)
    "guu": "V", "guc": "V", "gua": "V", "gug": "V",

    # Serine (S)
    "ucu": "S", "ucc": "S", "uca": "S", "ucg": "S",
    "agu": "S", "agc": "S",

    # Proline (P)
    "ccu": "P", "ccc": "P", "cca": "P", "ccg": "P",

    # Threonine (T)
    "acu": "T", "acc": "T", "aca": "T", "acg": "T",

    # Alanine (A)
    "gcu": "A", "gcc": "A", "gca": "A", "gcg": "A",

    # Tyrosine (Y), Stop
    "uau": "Y", "uac": "Y", "uaa": "Stop", "uag": "Stop",

    # Histidine (H), Glutamine (Q)
    "cau": "H", "cac": "H", "caa": "Q", "cag": "Q",

    # Asparagine (N), Lysine (K)
    "aau": "N", "aac": "N", "aaa": "K", "aag": "K",

    # Aspartic acid (D), Glutamic acid (E)
    "gau": "D", "gac": "D", "gaa": "E", "gag": "E",

    # Cysteine (C), Stop, Tryptophan (W)
    "ugu": "C", "ugc": "C", "uga": "Stop", "ugg": "W",

    # Arginine (R)
    "cgu": "R", "cgc": "R", "cga": "R", "cgg": "R",
    "aga": "R", "agg": "R",

    # Glycine (G)
    "ggu": "G", "ggc": "G", "gga": "G", "ggg": "G",
}
       
#chunk them by three

def codons(sequence):
    codon_list = []
    while sequence:
        codon_list.append(sequence[:3])
        sequence = sequence[3:]
    return codon_list

def translate(sequence):
    codon_list = codons(sequence)
    translated_sequence = []
    for codon in codon_list:
        amino_acid = codon_table[codon]
        if amino_acid == "Stop":
            break
        translated_sequence.append(amino_acid)
    return "".join(translated_sequence)