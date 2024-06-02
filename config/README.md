# SceneSense - Configurations

You can find below various configurations of the framework, which can be modified in [`config.yml`](/config/config.yml):

| Main Category | Sub-Category     | Options           | Description                                                                       |
| ------------- | ---------------- | ----------------- | --------------------------------------------------------------------------------- |
| `datasets`    | `text_dataset`   | `name`            | the name of the text dataset (e.g., `movielens-25m`)                              |
| `datasets`    | `text_dataset`   | `url`             | the url of the text dataset                                                       |
| `datasets`    | `visual_dataset` | `name`            | the name of the visual dataset (e.g., `SceneSense`)                               |
| `datasets`    | `visual_dataset` | `url`             | the url of the visual dataset                                                     |
| `datasets`    | `visual_dataset` | `feature_sources` | features extracted from which **sources** should be used? (e.g., [`full_movies`]) |
| `datasets`    | `visual_dataset` | `feature_models`  | features extracted from which **models** should be used? (e.g., [`vgg19`])        |
