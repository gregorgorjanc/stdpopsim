import stdpopsim

_species = stdpopsim.get_species("BosTau")

_gm = stdpopsim.GeneticMap(
    species=_species,
    id="Brekke2023_NRF_ARS-UCD1.2",
    url="TODO",
    sha256="TODO",
    file_pattern="chr_{id}_ratemap.txt",
    description="Sex-averaged genetic map for the Norwegian Red (NRF) cattle breed",
    long_description="""
        Sex-averaged genetic map for the Norwegian Red cattle (NRF) breed
        from Brekke et al. (2023). Sex-specific genetic map was estimated
        with Lepmap3 after identifying individual crossovers in
        a multi-generational pedigree with 110,555 individuals,
        which had genotypes at 35,880 autosomal SNPs (after filtering).
        19,603 full-sib families were used to identify individual crossovers
        for 603 unique bulls with 19,861 associated offspring and
        for 14,815 unique cows with 19,824 associated offspring.
        Haldane mapping function was used in Lepmap3. SNP positions across
        autosomal chromosomes 1-29 are based on the ARS-UCD1.2 genome assembly.
        Note that all cattle chromosomes are acrocentric with
        centromere occurring at the beginning of each chromosome.
        The total length was estimated to be 2,493 cM for males,
        2,309 cM for females, and 2,401 cM averaged across sexes.
    """,
    citations=stdpopsim.Citation(
        doi="https://doi.org/10.3168/jds.2022-22368",
        author="Brekke et al.",
        year="2023",
        reasons={stdpopsim.CiteReason.GEN_MAP},
    ),
)

_species.add_genetic_map(_gm)
