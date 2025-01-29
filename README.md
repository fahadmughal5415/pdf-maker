# PDF Maker

This project generates a PDF file with headers, footers, and lines on each page based on the data from a CSV file.

## Requirements

- Python 3.x
- fpdf
- pandas

## Installation

1. Install the required Python packages:
    ```sh
    pip install fpdf pandas
    ```

2. Ensure you have a CSV file named `topics.csv` in the same directory as the script. The CSV file should have the following columns:
    - `Topic`: The topic name to be used in the header and footer.
    - `Pages`: The number of pages to generate for each topic.

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. The script will generate a PDF file named `outline.pdf` in the same directory.

## Example

An example `topics.csv` file:
```csv
Topic,Pages
Topic 1,2
Topic 2,3
```

This will generate a PDF with the following structure:
- Page 1: Header "Topic 1", 20 lines, Footer "Topic 1"
- Page 2: Header "Topic 1", 20 lines, Footer "Topic 1"
- Page 3: Header "Topic 2", 20 lines, Footer "Topic 2"
- Page 4: Header "Topic 2", 20 lines, Footer "Topic 2"
- Page 5: Header "Topic 2", 20 lines, Footer "Topic 2"

