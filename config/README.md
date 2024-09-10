# SceneSense - Configurations

The first recommended step to use the framework is setting the configuration parameters. You can find below the configurations modifiable in [`config.yml`](/config/config.yml):

## I. General

It covers the general configurations of the system, including the followings:

- **mode**: what is the expected functionality of the framework? It can be `ds` to run dataset-related modules, `pipeline` to run an available pipeline, or `recsys` to run the recommender system.
- **sub_mode_ds**: if `ds` is selected as the `mode`, which dataset-related functionality is expected? Choose from `scenesense_meta` to process based on **SceneSense**'s metadata, or `scenesense_visual` to process its visual features.
- **sub_mode_pipeline**: if `pipeline` is selected as the `mode`, which pipeline functionality is desired? Choose from `dl_trailers` to download trailers for a list of given movies from YouTube, `frame_extractor` to extract frames of a video, `feat_extractor` to extract features of a frame, `shot_from_frame` to extract shots from a set of frames, or `shot_from_feat` to extract shots from features.
- **sub_mode_recsys**: if `recsys` is selected as the `mode`, which recommender system is expected? [TODO]

<!--
# Datasets

datasets: # Text dataset (MovieLenz 25M)
text_dataset: # Dataset name
name: movielens-25m # Path to the dataset
url: https://files.grouplens.org/datasets/movielens/ml-25m.zip # Visual dataset (SceneSense)
visual_dataset: # Dataset name
name: SceneSense-visual # Path to the dataset
path_metadata: https://huggingface.co/datasets/alitourani/moviefeats_visual/resolve/main/stats.json # Path to the features
path_raw: https://huggingface.co/datasets/alitourani/moviefeats_visual/blob/main/ # Feature sources to be used (in an array) # Possible values: ["full_movies", "movie_shots", "movie_trailers"]
feature_sources: ["full_movies", "movie_shots", "movie_trailers"] # Feature extraction models to be used (in an array) # Possible values: ["incp3", "vgg19"]
feature_models: ["incp3", "vgg19"]
pipelines: # Movie trailers finder and downloader pipeline
movie_trailers: # Pipeline name
name: Trailer-fetcher # Path to the pipeline
download_path: "~/Downloads" # Movie frames extractor pipeline
movie_frames: # Pipeline name
name: Frame-extractor # Movies path
movies_path: "E:/Datasets/Movies/Videos" # Frames path
frames_path: "E:/Datasets/Movies/MovieFrames" # Supported video formats
video_formats: ["mp4", "avi", "mkv"] # Frequency of frames extraction (picking 'n' frames every second)
frequency: 1 # Output file format
output_format: "jpg" # Feature extraction model input size (width)
model_input_size: 420 # Movie frames visual feature extractor pipeline
movie_frames_visual_features: # Pipeline name
name: Visual-feature-extractor # Path the root directory containing the frames in folders # [Note] it is equal to the frames_path in the movie_frames pipeline
frames_path: "E:/Datasets/Movies/MovieFrames" # Features path
features_path: "E:/Datasets/Movies/MovieFeatures" # Supported image (saved frames) formats
image_formats: ["png", "jpg", "jpeg"] # Feature extraction models to be used (in an array) # Possible values: ["incp3", "vgg19"]
feature_extractor_model: "incp3" # Packets size (number of frames in each packet)
packet_size: 25 # Movie frames and extracted features shot detection pipeline
movie_shots: # Pipeline name
name: Shot-detector # Variants of shot detection
variants: # Shot detection from frames
from_frames: # Input frames path
frames_path: "E:/Datasets/Movies/MovieFrames" # Output shot frames path
shot_frames_path: "E:/Datasets/Movies/MovieShotsFrames" # Supported input image (saved frames) formats
image_formats: ["png", "jpg", "jpeg"] # Output file format
output_format: "jpg" # Shot boundaries detection threshold
threshold: 0.65 # Shot detection from features
from_features: # Input features path
features_path: "E:/Datasets/Movies/MovieFeatures" # Output shot features path
shot_features_path: "E:/Datasets/Movies/MovieShotsFeatures" # Shot boundaries detection threshold
threshold: 0.7 # Packets size (number of frames in each packet) # [Note] it is recommended to set it equal to the packet_size in the movie_frames_visual_features pipeline
packet_size: 25 -->

| Main Category | Sub-Category     | Options           | Description                                                                       |
| ------------- | ---------------- | ----------------- | --------------------------------------------------------------------------------- |
| `datasets`    | `text_dataset`   | `name`            | the name of the text dataset (e.g., `movielens-25m`)                              |
| `datasets`    | `text_dataset`   | `url`             | the url of the text dataset                                                       |
| `datasets`    | `visual_dataset` | `name`            | the name of the visual dataset (e.g., `SceneSense`)                               |
| `datasets`    | `visual_dataset` | `url`             | the url of the visual dataset                                                     |
| `datasets`    | `visual_dataset` | `feature_sources` | features extracted from which **sources** should be used? (e.g., [`full_movies`]) |
| `datasets`    | `visual_dataset` | `feature_models`  | features extracted from which **models** should be used? (e.g., [`vgg19`])        |
