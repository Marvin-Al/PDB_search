from Bio import pairwise2
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from tqdm import tqdm

def hobohm1(sequences, threshold=0.8):
    """
    Remove redundant sequences from a list using the Hobohm 1 algorithm.

    Args:
    - sequences: List of Bio.SeqRecord objects
    - threshold: Fraction of identical amino acids for a sequence to be considered redundant

    Returns:
    - List of non-redundant sequences
    """



    non_redundant_sequences = []
    with tqdm(total=len(sequences), desc="Processing Sequences") as pbar:
        for seq in sequences:
            seq = SeqRecord(Seq(seq))
            add_seq = True
            for nr_seq in non_redundant_sequences:
                alignment = pairwise2.align.globalxx(seq.seq, nr_seq.seq, one_alignment_only=True)[0]
                score = alignment[2]
                length = max(len(seq), len(nr_seq))
                if score / length > threshold:
                    add_seq = False
                    break
            if add_seq:
                non_redundant_sequences.append(seq)
                pbar.update(1)
    return non_redundant_sequences

# Example usage with shorter sequences

"""
sequences = [
            "MFSVLLQLP",
            "MFSVLTRLT",
            "GFNVTQFNG",
            "MFSVLTRLT",
            "MYTMLQQLK",
            "MFSVLLQLP"
        ]

non_redundant = hobohm1(sequences)
for seq in non_redundant:
    print(seq.seq)
"""