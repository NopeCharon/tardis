"""
Basic TARDIS Benchmark.
"""

from benchmarks.benchmark_base import BenchmarkBase
from tardis import run_tardis
from tardis.io.atom_data.util import download_atom_data
from tardis.io.configuration.config_reader import Configuration


class BenchmarkRunTardis(BenchmarkBase):
    """
    Class to benchmark the `run tardis` function.
    """

    def __init__(self):
        super().__init__()
        filename = "data/tardis_configv1_benchmark.yml"
        self.path = self.get_relative_path(filename)
        download_atom_data('kurucz_cd23_chianti_H_He')

    def time_run_tardis(self):
        run_tardis(self.path, log_level="ERROR", show_progress_bars=False)


