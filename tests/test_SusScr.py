import pytest

import stdpopsim
from tests import test_species


class TestSpeciesData(test_species.SpeciesTestBase):

    species = stdpopsim.get_species("SusScr")

    def test_ensembl_id(self):
        assert self.species.ensembl_id == "sus_scrofa"

    def test_name(self):
        assert self.species.name == "Sus scrofa"

    def test_common_name(self):
        assert self.species.common_name == "Pig"

    def test_assembly_source(self):
        assert self.species.genome.assembly_source == "ensembl"

    def test_assembly_build_version(self):
        assert self.species.genome.assembly_build_version == "113"

    # QC Tests. These tests are performed by another contributor
    # independently referring to the citations provided in the
    # species definition, filling in the appropriate values
    # and deleting the pytest "skip" annotations.
    @pytest.mark.skip("Population size QC not done yet")
    def test_qc_population_size(self):
        assert self.species.population_size == -1

    @pytest.mark.skip("Generation time QC not done yet")
    def test_qc_generation_time(self):
        assert self.species.generation_time == -1


class TestGenomeData(test_species.GenomeTestBase):

    genome = stdpopsim.get_species("SusScr").genome

    @pytest.mark.skip("Recombination rate QC not done yet")
    @pytest.mark.parametrize(
        ["name", "rate"],
        {
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
            "11": -1,
            "12": -1,
            "13": -1,
            "14": -1,
            "15": -1,
            "16": -1,
            "17": -1,
            "18": -1,
            "X": -1,
            "Y": -1,
            "MT": -1,
        }.items(),
    )
    def test_recombination_rate(self, name, rate):
        assert rate == pytest.approx(
            self.genome.get_chromosome(name).recombination_rate
        )

    @pytest.mark.skip("Mutation rate QC not done yet")
    @pytest.mark.parametrize(
        ["name", "rate"],
        {
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
            "11": -1,
            "12": -1,
            "13": -1,
            "14": -1,
            "15": -1,
            "16": -1,
            "17": -1,
            "18": -1,
            "X": -1,
            "Y": -1,
            "MT": -1,
        }.items(),
    )
    def test_mutation_rate(self, name, rate):
        assert rate == pytest.approx(self.genome.get_chromosome(name).mutation_rate)

    @pytest.mark.skip("Ploidy QC not done yet")
    @pytest.mark.parametrize(
        ["name", "ploidy"],
        {
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
            "11": -1,
            "12": -1,
            "13": -1,
            "14": -1,
            "15": -1,
            "16": -1,
            "17": -1,
            "18": -1,
            "X": -1,
            "Y": -1,
            "MT": -1,
        }.items(),
    )
    def test_chromosome_ploidy(self, name, ploidy):
        assert ploidy == self.genome.get_chromosome(name).ploidy
