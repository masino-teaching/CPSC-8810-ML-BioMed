# Palmetto PyTorch Configuration
The following commands can be used to create a Python environment that supports PyTorch and PyTorch lighting with GPU support. This environment has been tested on Palmetto nodes that have P100, A100, V100 GPUs.

````
conda create --name 8810-pytorch python=3.10
source activate 8810-pytorch
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip3 install lightning
pip3 install torchmetrics
pip3 install ipython
pip3 install ipykernel
pip3 install matplotlib
pip3 install seaborn
pip3 install -U scikit-learn
pip3 install torchtext
pip3 install torchdata
pip3 install 'portalocker>=2.0.0' # the single quotes are necessary
python -m ipykernel install --user --name 8810-pytorch --display-name “8810-pytorch”
````

To use PyTorch Geometric in practicum-08, additionally execute the following commands.
````
source activate 8810-pytorch
pip3 install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.2.0+cu118.html
pip3 install torch_geometric
````