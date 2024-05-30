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

## 🚀 Launching the Framework

TBD

## 👨🏻‍💻 Contribution

- In case you add new dependencies, do not forget to add them to `requirements.txt` using `pip freeze > requirements.txt` (you may need to remove the current file to have an updated version!).
