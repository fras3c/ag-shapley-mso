# ag-shapley-mso
This is an implementation of our algorithms for computing the Shapley value and the Banzhaf value in polynomial time for the resource allocation games over bounded treewidth graphs described in:

Greco, Lupia, Scarcello: Coalitional games induced by matching problems: Complexity and islands of tractability for the Shapley value. Artif. Intell. 278 (2020)

This code is for research only purposes. If you decide to use it, please cite our work:
```
@article{DBLP:journals/ai/GrecoLS20,
  author    = {Gianluigi Greco and
               Francesco Lupia and
               Francesco Scarcello},
  title     = {Coalitional games induced by matching problems: Complexity and islands
               of tractability for the Shapley value},
  journal   = {Artif. Intell.},
  volume    = {278},
  year      = {2020},
  url       = {https://doi.org/10.1016/j.artint.2019.103180},
  doi       = {10.1016/j.artint.2019.103180},
  timestamp = {Thu, 19 Dec 2019 09:27:15 +0100},
  biburl    = {https://dblp.org/rec/journals/ai/GrecoLS20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
##INSTALLATION

git clone https://github.com/fras3c/ag-shapley-mso.git
docker build -t ag-shapley-mso .

EXECUTION
```
docker run -i -t ag-shapley-mso:latest /bin/bash
chmod +x ag-sv-mso.py
```
USAGE

```./ag-sv-mso.py -b outdir agents goods expected_goods``` # builds an allocation game [INPUT] outdir and CSV files; [OUTPUT] an allocation game (LEDA format)
```./ag-sv-mso.py -s instance_name``` # builds and solves a MSO counting problem by taking in INPUT the resource allocation graph built in the previous step (to do that we use Sequoia MSO Solver)
```./ag-sv-mso.py -c outdir instance_name``` # computes the Shapley Value of the Resource allocation game by exploiting the solutions (histograms) computed in previous step.

All of those steps can be performed together using the switch "-a" as follows:

```./ag-sv-mso.py -a outdir agents goods expected_goods instance_name
./ag-sv-mso.py -a "/home/sequoia/out" "examples/roma30res.csv" "examples/roma30val.csv" "examples/roma30expectedpub.csv" 30
```
You will find more instances in the "example" folder.
