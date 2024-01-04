#!/bin/bash -l
#SBATCH --gres=gpu:4
#SBATCH --partition=gpu
#SBATCH --mail-type=BEGIN,END,FAIL


module load cuda/10.1

conda activate DLC_20220714

cd /lmb/home/dmalmazet/Desktop

python DLCroutine.py
