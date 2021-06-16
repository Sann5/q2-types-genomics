# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from q2_types.sample_data import SampleData
from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.per_sample_data import (
    MAGs, MultiMAGSequencesDirFmt,
    Contigs, ContigSequencesDirFmt,
    MultiBowtie2Index, MultiBowtie2IndexDirFmt
)


class TestTypes(TestPluginBase):
    package = "q2_types_genomics.per_sample_data.tests"

    def test_mags_semantic_type_registration(self):
        self.assertRegisteredSemanticType(MAGs)

    def test_mags_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            SampleData[MAGs],
            MultiMAGSequencesDirFmt
        )

    def test_contigs_semantic_type_registration(self):
        self.assertRegisteredSemanticType(Contigs)

    def test_contigs_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            SampleData[Contigs],
            ContigSequencesDirFmt
        )

    def test_multibowtie_semantic_type_registration(self):
        self.assertRegisteredSemanticType(MultiBowtie2Index)

    def test_multibowtie_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            SampleData[MultiBowtie2Index],
            MultiBowtie2IndexDirFmt
        )


if __name__ == '__main__':
    unittest.main()
