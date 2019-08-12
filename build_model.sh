#! /bin/sh

# TODO(drocco): add check on conda environment
unzip -f "data/peerLoanData.zip" -d data/
python predict-late-payers-basic-model.py