#!/bin/env python3

import deepctx.scripting as dcs

import _common

def main(context: dcs.Context):
    config = context.config

    assert config.input_path.is_dir()
    config.output_path.mkdir(exist_ok=True)

    fastq_files = list(_common.find_fastqs(config.input_path / "fastq"))
    fastq_files = [f for f in fastq_files if not f.name.startswith("Blank")]
    fastq_files = [f for f in fastq_files if "_R2_001" not in f.name]
    _common.build_multiplexed_fasta_db(fastq_files, config.name, config.output_path)

if __name__ == "__main__":
    context = dcs.Context(main)
    _common.define_io_arguments(context.argument_parser)
    _common.define_dataset_arguments(context.argument_parser, "Hopland")
    context.execute()
