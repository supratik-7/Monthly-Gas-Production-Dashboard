
# Monthly Gas Production Dashboard

A comprehensive gas production analysis dashboard built with Python's Tkinter for the GUI and Matplotlib for data visualization. This project allows users to filter and visualize gas production data by field, sand, year, and month.

## Features

* **Field-Wise and Sand-Wise Filtering:** Choose between analyzing data based on fields or sand layers.
* **Date-Based Filtering:** Narrow down data by year and month for more precise analysis.
* **Interactive Graphs:** Generate bar charts and line plots with navigation tools.
* **Clear Button:** Quickly reset the dashboard to the default state.

## Prerequisites

Ensure you have the following libraries installed:

```bash
pip install pandas matplotlib pillow
```

## Project Structure

```
Project-1/
├── Monthly_Production_Volume_Students.csv
├── main.py
└── README.md
```

## How to Run the Project

1. Clone the repository:

```bash
git clone <repo_url>
cd Project-1
```

2. Run the main script:

```bash
python main.py
```

3. Make sure the `Monthly_Production_Volume_Students.csv` file is in the same directory as `main.py`.

## File Descriptions

* **main.py:** The primary script that runs the Tkinter-based gas production dashboard.
* **Monthly\_Production\_Volume\_Students.csv:** The production volume data used for visualization.

## Usage

* **Field/Sand Selection:** Use the radio buttons to choose between field-wise or sand-wise data visualization.
* **Date Filters:** Select the desired year and month to refine your data view.
* **Submit:** Click the "SUBMIT" button to generate the chart.
* **Clear:** Use the "CLEAR" button to reset all selections.

## Screenshots

Include screenshots here (if needed) for a better understanding of the UI.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Feel free to open issues or submit pull requests if you have ideas for improvement.

