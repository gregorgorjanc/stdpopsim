import stdpopsim

from . import genome_data

# TODO
_ToDOEtAl = stdpopsim.Citation(
    author="TODO",
    year=-1,
    doi="TODO",
    reasons={},
)

# stdpopsim.CiteReason.ASSEMBLY
# stdpopsim.CiteReason.GEN_TIME
# stdpopsim.CiteReason.POP_SIZE
# stdpopsim.CiteReason.REC_RATE
# stdpopsim.CiteReason.MUT_RATE

# TODO
# [The following are notes for implementers and should be deleted
#  once the recombination rates have been inserted]
# This is the per-chromosome recombination rate, typically the mean
# rate along the chromosome.
# Values in this dictionary are set to -1 by default, so you have
# to update each one. These should be derived from the most reliable
# data and how they were obtained should be documented here.
# The appropriate citation must be added to the list of
# recombination_rate_citations in the Genome object.

_recombination_rate = {
    "1": -1,
    "2": -1,
    "3": -1,
    "4": -1,
    "5": -1,
    "6": -1,
    "7": -1,
    "8": -1,
    "9": -1,
    "10": -1,
    "Pt": 0,
    "Mt": 0,
}

# TODO
# [The following are notes for implementers and should be deleted
#  once the mutation rates have been inserted]
# This is the per-chromosome mutation rate, typically the mean
# rate along the chromosome. If per chromosome rates are not available,
# the same value should be used for each chromosome. In this case,
# please use a variable to store this value, rather than repeating
# the same numerical constant, e.g.
# _mutation_rate = {
#    1: _overall_rate,
#    2: _overall_rate,
#    ...
# Values in this dictionary are set to -1 by default, so you have
# to update each one. These should be derived from the most reliable
# data and how they were obtained should be documented here.
# The appropriate citation must be added to the list of
# mutation_rate_citations in the Genome object.

_mutation_rate = {
    "1": -1,
    "2": -1,
    "3": -1,
    "4": -1,
    "5": -1,
    "6": -1,
    "7": -1,
    "8": -1,
    "9": -1,
    "10": -1,
    "Pt": -1,
    "Mt": -1,
}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    # TODO citations
    citations=[],
)

_species = stdpopsim.Species(
    id="ZeaMay",
    ensembl_id="zea_mays",
    name="Zea mays",
    common_name="Zea mays",
    genome=_genome,
    # TODO citation
    generation_time=1,
    # TODO and citation
    population_size=0,
    citations=[],
)

stdpopsim.register_species(_species)
