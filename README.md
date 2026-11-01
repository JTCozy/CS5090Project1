# CS5090Project1
CS5090 Project 1 using karpathy's nanogpt as a base

Environment used was Google Collab with Google Drive
No Dependencies if used in Google Collab, if not: tiktoken, os, kagglehub, datasets, numpy, pytorch
note: if not run in google collab gc and google collab references must be removed in data processing

Steps to replicate
1. create folder in google drive to house files from github
2. log into google collab
3. run DataProccessing.ipynb(cpu) with changes to filepaths where needed
4. make sure train and val.bin files are in CodeSnippets folder
5. run Training.ipynb(gpu) to train the corresponding models
6. run sampling.ipynb(cpu or gput) to sample from the model
