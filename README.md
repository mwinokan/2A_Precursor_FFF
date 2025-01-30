# FFF_Template

To use this repository:

1. Use this template to create a new repository
1. Clone the newly repository on IRIS
1. Follow the steps indicated below

## 1. Dependencies

Skip this section if you have run a FFF campaign with this template before

### Pre-requisites

- [x] SSH access to STFC/IRIS
- [x] Working directory in `cepheus-slurm:/opt/xchem-fragalysis-2/``
- [x] Set up [xchem/slurm](https://github.com/xchem/slurm)
- [x] Conda setup w/ `python >= 3.10`
- [x] Custom bashrc
- [x] Start a Jupyter notebook server
- [x] [BulkDock](https://github.com/mwinokan/BulkDock)
- [x] [HIPPO](https://github.com/mwinokan/HIPPO)
- [x] [Fragmenstein](https://github.com/matteoferla/Fragmenstein)
- [x] [FragmentKnitwork](https://github.com/xchem/FragmentKnitwork)
- [x] [syndirella](https://github.com/kate-fie/syndirella)
- [x] [EnamineCatalogs](https://github.com/mwinokan/EnamineCatalogs)

### Checklist

- [x] you can ssh to IRIS (cepheus-slurm.diamond.ac.uk)
- [x] you can source a file to set up conda
- [x] you can connect to a Jupyter notebook on IRIS
- [x] you can run `python -m bulkdock status` from the BulkDock directory
- [x] you can `import hippo` from a notebook
- [x] you can run `fragmenstein --help`
- [x] you can ssh to the sw-graph VM (optional, only for Knitwork)
- [x] you can run `syndirella --help`
- [x] you have set up EnamineCatalogs

## 2. Setup

- [x] Define merging opportunities by creating tags of LHS hits in Fragalysis
- [x] Download target from Fragalysis and place the .zip archive in the repo
- [x] Setup target in BulkDock 

```
python -m bulkdock extract TARGET_NAME
python -m bulkdock setup TARGET_NAME
```

## 3. Compound Design

- [x] run the notebook `hippo/1_merge_prep.ipynb`

### Fragmenstein

For each merging hypothesis

- [x] go to the fragmenstein subdirectory `cd fragmenstein`
- [x] queue fragmenstein job 

```sb.sh --job-name "fragmenstein" $HOME2/slurm/run_bash_with_conda.sh run_fragmenstein.sh HYPOTHESIS_NICKNAME```

This will create outputs in the chosen HYPOTHESIS_NICKNAME subdirectory:

- **`HYPOTHESIS_NICKNAME_fstein_bulkdock_input.csv`: use this for BulkDock placement**
- `output`: fragmenstein merge poses in subdirectories
- `output.sdf`: fragmenstein merge ligand conformers
- `output.csv`: fragmenstein merge metadata

- [ ] placement with bulkdock

```
cp -v HYPOTHESIS_NICKNAME/HYPOTHESIS_NICKNAME_fstein_bulkdock_input.csv $BULK/INPUTS/TARGET_HYPOTHESIS_NICKNAME_fstein.csv
cd $BULK
python -m bulkdock place TARGET_NAME INPUTS/TARGET_HYPOTHESIS_NICKNAME_fstein.csv

```

- [ ] monitor placements (until complete)

```
python -m bulkdock status
```

- [ ] export Fragalysis SDF

```
sb.sh --job-name "bulkdock_out" $HOME2/slurm/run_python.sh -m bulkdock to-fragalysis TARGET OUTPUTS/SDF_FILE METHOD_NAME
```

### Fragment Knitwork

Running Fragment Knitting currently requires access to a specific VM known as `graph-sw2`. If you don't have access, skip this section

- [x] `git add`, `commit` and `push` the contents of `aligned_files` and `knitwork` to the repository
- [x] `git clone` the repository on `graph-sw2`
- [x] navigate to the `knitwork` subdirectory

Then, for each merging hypothesis:

- [x] Run the "fragment" step of FragmentKnitwork: `./run_fragment.sh HYPOTHESIS_NICKNAME`
- [x] Run the pure "knitting" step of FragmentKnitwork: `./run_knitwork_pure.sh HYPOTHESIS_NICKNAME`
- [ ] Run the impure "knitting" step of FragmentKnitwork: `./run_knitwork_impure.sh HYPOTHESIS_NICKNAME`
- [ ] Create the BulkDock inputs: `python to_bulkdock.py HYPOTHESIS_NICKNAME`
- [ ] `git add`, `commit` and `push` the CSVs created by the previous step
- [ ] back on `cepheus-slurm` pull the latest changes
- [ ] Run BulkDock placement as for Fragmenstein above

```
cp -v HYPOTHESIS_NICKNAME/HYPOTHESIS_NICKNAME_knitwork_pure.csv $BULK/INPUTS/TARGET_HYPOTHESIS_NICKNAME_knitwork_pure.csv
cp -v HYPOTHESIS_NICKNAME/HYPOTHESIS_NICKNAME_knitwork_impure.csv $BULK/INPUTS/TARGET_HYPOTHESIS_NICKNAME_knitwork_impure.csv
cd $BULK
python -m bulkdock place TARGET_NAME INPUTS/TARGET_HYPOTHESIS_NICKNAME_knitwork_pure.csv
python -m bulkdock place TARGET_NAME INPUTS/TARGET_HYPOTHESIS_NICKNAME_knitwork_impure.csv
```

- [ ] Export Fragalysis SDF as for Fragmenstein

## 4. Scaffold selection

### Syndirella retrosynthesis
### Review chemistry
### HIPPO filtering
### Fragalysis curation

## 5. Syndirella elaboration

## 6. HIPPO

### Load elaborations
### Quote reactants
### Solve routes
### Calculate interactions
### Generate random recipes
### Score random recipes
### Optimise best recipes
### Create proposal web page

## 7. Review & order

### Review chemistry
### Order reactants
