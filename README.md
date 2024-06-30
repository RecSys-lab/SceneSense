# SceneSense

This repository provides a multi-modal movie recommendation framework titled `SceneSense` that benefits from **Generative AI** for providing enhanced suggestions.

## 🛠️ Getting Started

After cloning the repository, you need to install the required dependencies. The Python version used while developing the framework is `3.12.3`. It is highly recommended to create a Python virtual environment using `python -m venv [myenv]` and then, install the required dependencies in the `requirements.txt` using the below command:

```
pip install -r requirements.txt
```

## 📊 Data

As the framework supports multi-modal processing and covers **text**, **visual**, and **fused data**, varios datasets can be fed for reproducibility, evaluation, and experiments purposes:

- **Text Feed:** `MovieLenz-25M` ([link](https://grouplens.org/datasets/movielens/25m/)) is recommended to provide data about movies, user interactions, _etc._
- **Visual Feed:** `SceneSense Dataset` ([link](https://huggingface.co/datasets/alitourani/moviefeats_visual)) is collected by the team and provides frame-level features for each movie using different Convolutional Neural Networks (CNNs).

In order to use the datasets, some **helper functions** and **example codes** are provided in the `src/core/datasets` [path](https://github.com/RecSys-lab/SceneSense/tree/main/src/core/datasets).

## 🚀 Launching the Framework

To launch the framework, you need to take the below steps:

### I. Set Configurations

The first step is to modify the configurations, adapting the framework towards what you target. Accordingly, you need to modify the [config.yml](/config/config.yml) file based on the [documentations provided for it](/config/README.md).

## 🗄️ Code Structure

You can find below where to search for the codes in the framework:

```
> [config]              ## framework configs & docs
    - config.yml
> [src]                 ## framework codes
    > [core]            ## core functionalities
        > [datasets]    ## dataset connection & helpers
    > [multimodal]      ## processing modules
        > [textual]
        > [visual]
        > [fused]
    - utils.py          ## general utilities
    - main.py           ## main runner file
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
