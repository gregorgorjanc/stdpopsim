import stdpopsim

from . import genome_data

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

_ClarkEtAl = stdpopsim.Citation(
    author="Clark et al.",
    year=2005,
    doi="https://doi.org/10.1093/molbev/msi228",
    reasons={stdpopsim.CiteReason.MUT_RATE},
)

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

_overall_rate = 3.3e-8
_mutation_rate = {
    "1": _overall_rate,
    "2": _overall_rate,
    "3": _overall_rate,
    "4": _overall_rate,
    "5": _overall_rate,
    "6": _overall_rate,
    "7": _overall_rate,
    "8": _overall_rate,
    "9": _overall_rate,
    "10": _overall_rate,
    "Pt": _overall_rate,
    "Mt": _overall_rate,
}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    # TODO citations
    citations=[_ClarkEtAl],
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
