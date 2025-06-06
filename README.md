# DataQuality-With-GreatExpectations

# How to start

1. If `pip`
    + make a python venv
        ```sh
        python3 -m venv venv_name
        ```

    + activate the env
        + linux/mac
            ```sh
            source venv_name/bin/activate
            ```
    + install libraries
        ```sh
        pip3 install -r requirements.txt
        ```

    + clone the repo

2. If `uv`
    - clone the repo
    - navigate to dir and run: 
        ```sh 
        uv init
        ```
    - remove `main.py`
    - run 
        ```sh 
        uv sync
        ```
    - run
        ```sh
        uv add -r requirements.txt
        ``` 

+ run ```csv_data_validate.py```

# Fresh start
+ [quickStart](https://docs.greatexpectations.io/docs/oss/tutorials/quickstart)
+ [All validations API](https://greatexpectations.io/expectations/?banner=false)

# Postgres Connection
+ rename the ```.env_sample``` to ```.env```
+ run the ```*.py``` file
