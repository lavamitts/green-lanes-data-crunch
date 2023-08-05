# Green lane data crunch

## Implementation steps

- Create and activate a virtual environment, e.g.

  `python -m venv venv/`

  `source venv/bin/activate`

- Install necessary Python modules via `pip install -r requirements.txt`

## Usage

### To create a new file in CSV format
`python create.py uk`

`python create.py uk 4 5` where argument 1 is the scope [uk|xi], argument 2 is the start index (1st digit of comm code) and argument 3 is the end index  (1st digit of comm code); arguments 2 and 3 are optional.

`python create.py uk 0 10 2022-10-01` where argument 1 is the scope [uk|xi], argument 2 is the start index (1st digit of comm code) and argument 3 is the end index  (1st digit of comm code); arguments 2 and 3 are optional.

