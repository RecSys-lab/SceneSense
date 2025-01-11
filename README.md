# MoVieFex: A Multi-Faceted Movie Recommendation Framework

This repository provides a multi-modal movie recommendation framework titled `MoVieFex` that integrates **Computer Vision**, **Generative AI**, and **Recommender Systems** to provide enhanced suggestions.

## 🛠️ Getting Started

After cloning the repository, you need to install the required dependencies. The Python version used while developing the framework is `3.10.4`. It is highly recommended to create a Python virtual environment using `python -m venv .venv`, activate it using `source .venv/bin/activate` (Linux) or `.\.venv\Scripts\activate` (Windows). The next step is running the `setup.py` inside the root directory using the command below:

```
pip install -e .
```

You can also install the required dependencies in the `requirements.txt` using the below command:

```
pip install -r requirements.txt
```

## 📊 Data

As the framework supports multi-modal processing and covers **text**, **visual**, and **fused data**, varios datasets can be fed for reproducibility, evaluation, and experiments purposes:

- **Text Feed:** `MovieLenz-25M` ([link](https://grouplens.org/datasets/movielens/25m/)) is recommended to provide data about movies, user interactions, _etc._
- **Visual Feed:** `MoVieFex Dataset` ([link](https://huggingface.co/datasets/alitourani/MoViFex_Dataset)) is collected by the team and provides frame-level features for each movie using different Convolutional Neural Networks (CNNs).

In order to use the datasets, some **helper functions** and **example colabs** are provided in the [`examples` path](/examples/).

## 🚀 Launching the Framework

To launch the framework, you need to take the below steps:

### I. Set Configurations

The first step is to modify the configurations, adapting the framework towards what you target. Accordingly, you need to modify the [config.yml](/config/config.yml) file based on the [documentations provided for it](/config/README.md).

### II. Run the Code

After activating the `.venv` (if set), run the [`main.py`](/main.py) file and enjoy working with the framework!

## 🗄️ Code Structure

You can find below where to search for the codes in the framework:

```bash
> [config]                  ## framework configs & docs
    - config.yml
    - README.md
> [src]                     ## framework codes
    > [datasets]            ## dataset functions
        > [movielens]
        > [scenesense]
        - runDataset.py
    > [pipelines]           ## core functionalities and pipelines
        > [downloaders]     ## YouTube downloader for trailers
        > [frames]          ## frame extraction functions
        > [shots]           ## shot detection functions
        > [visual_feats]    ## visual feature extraction functions
    > [multimodal]          ## processing modules
        > [textual]
        > [visual]
        > [fused]
    - utils.py              ## general utilities
    - runCore.py            ## core runner
- main.py                   ## main file
```

## 👨🏻‍💻 Contribution

In case you are willing to contribute to the project, please consider the following notes before opening your [pull requests](https://github.com/RecSys-lab/SceneSense/pulls):

- Please keep the structure of the project and add new codes in proper locations in the `src` folder. The **Code Structure** section provides general information accordingly.
- In case you add new dependencies, do not forget to add them to `requirements.txt` using `pip freeze > requirements.txt` (you may need to remove the current file to have an updated version!).

## 📝 Citation

If you find **SceneSense** useful for your research or development, please cite the following [paper](#):

```
@article{tbd,
  title={TBD}
}
```
