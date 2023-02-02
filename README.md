# postcode-parser

## Getting started

If your local machine is operating on Windows, first install Windows Subsystem for Linux (WSL).  
Please follow [Windows Subsystem for Linux Installation (WSL)](https://docs.docker.com/docker-for-windows/wsl/) and [Using Docker in WSL 2](https://code.visualstudio.com/blogs/2020/03/02/docker-in-wsl2), to get started.

## Option 1: Using Docker

### Prerequisites

- **macOS**: [Install Docker Desktop](https://docs.docker.com/desktop/).
- **Linux/Ubuntu**: [Install Docker Compose](https://docs.docker.com/compose/install/) and [Install Docker Engine](https://docs.docker.com/engine/install/).
- **Windows**: Windows Subsystem for Linux (WSL). Please follow [Windows Subsystem for Linux Installation (WSL)](https://docs.docker.com/docker-for-windows/wsl/) and [Using Docker in WSL 2](https://code.visualstudio.com/blogs/2020/03/02/docker-in-wsl2), to get started.

```bash
git clone https://github.com/bgrinsted/postcode-parser && \
cd postcode-parser && \
docker build -t postcode-parser . && \
docker run -v $(pwd)/data/input:/app/data/input -v $(pwd)/app/data/output -it --name postcode-parser-container postcode-parser	
```

## Option 2: macOS, Linux or WSL (for Windows):
1. Install Python 3.9
2. Open a terminal on local machine
3. Clone this repository: `git clone git@github.com:bgrinsted/postcode-parser.git`
4. Create virtual environment: `python -m venv venv`
5. Activate virtual env: `source venv/bin/activate`
6. Install requirements: `pip install -r requirements`
7. Run app: `python main.py`

# The Brief 

### Source data:
Presented with two CSV files containing a collection of strings representing UK postcodes.
1. InputFile.csv: unvalidated postcode data.
2. LondonPostcodes.csv: clean and validated postcodes for London districts.

### Task:
Categorise the values in InputFile.csv as:
1. Invalid postcodes.
2. Valid postcodes:
    - London (exists in LondonPostcodes.csv)
    - not-London

### Approach:
1. Read data from `data/input` directory
2. Standardise whitespace:
    - replace all whitespace with a single space.
    - remove all leading and trailing whitespace.
3. Using regex, invalidate strings not compliant with UK-postcode formatting standards.
4. Divide remaining valid strings into two groups:
   - London
   - not-London:
5. write original values to separate CSV files in `data/output`.

### Assumptions:
1. This script is only concerned with validating the structure of the string.
2. A string can be in a valid UK-postcode format, though may not exist according to postal services.
3. A postcode containing no whitespace is considered invalid.
4. Standardisation of whitespace is acceptable and preferable.
5. Duplicate string in InputFile.csv should be ignored.