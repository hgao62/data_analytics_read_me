# TASKS.md

This file outlines the tasks for your finance ETL and analysis project. Each task includes relevant functions (based on your existing code) and instructions on their usage. Follow them in order to implement a typical data workflow: get data → clean data → enrich data → visualization → create charts → report generation.

---

### Lesson 1 录屏:[Google drive 链接](https://drive.google.com/drive/folders/1iU_gEgyRuALyBOeynR6HDsr5lbL9nP69?usp=sharing)

## Task 1: Get Data

### Functions

1. **`get_stock_data(stock_name: str, start_date: str, end_date: str) -> pd.DataFrame`**

   - Located in: `read_data.py`
   - Loads CSV data from the `stock_data.csv` file.
   - Filters rows matching the given `stock_name` (case-insensitive) and the date range between `start_date` and `end_date`.
   - Returns a Pandas DataFrame with the filtered results.

2. **`get_sector_data() -> pd.DataFrame`**
   - Located in: `read_data.py`
   - Loads sector and industry information from `sector_info.csv`.
   - Returns a DataFrame with columns such as `Ticker`, `Sector`, and `Industry`.

### Instructions

- Implement or review the logic in `get_stock_data` to verify it correctly filters the CSV by `stock_name` and date range.
- Verify that `get_sector_data` properly reads from your sector CSV file (e.g., `sector_info.csv`).

### Expected Output

- A DataFrame with valid stock data (filtered by date range and stock name).
- A DataFrame containing sector/industry mappings.

---

## Task 2: Clean Data

_(If you have a dedicated function for cleaning data or handling missing values, include it here. Otherwise, place your cleaning logic directly in your main pipeline.)_

### Possible Steps

- Convert date columns to a proper datetime type (already done in `get_stock_data`).
- Handle missing values (e.g., drop or fill with averages).
- Drop or rename unnecessary columns.

### Expected Output

- A DataFrame with consistent and valid data for further processing.  
  _(Note: No specific function exists in your current codebase for cleaning, so you can implement these steps wherever needed.)_

---

## Task 3: Enrich Data

### Relevant Functions

_(Potentially from `transform_data.py`)_

1. `add_stock_returns(df: pd.DataFrame) -> pd.DataFrame`
2. `calculate_moving_average(df: pd.DataFrame, window: int) -> pd.DataFrame`
3. `add_stock_volatility(df: pd.DataFrame, window: int) -> pd.DataFrame`
4. `enrich_with_sector_industry(df: pd.DataFrame) -> pd.DataFrame`

### Instructions

- **`add_stock_returns`**: Calculate daily returns → `(Close_today - Close_yesterday) / Close_yesterday`.
- **`calculate_moving_average`**: Add a specified moving-average column (e.g., 30-day MA).
- **`add_stock_volatility`**: Compute rolling standard deviation based on daily returns over a chosen window (e.g., 30 days).
- **`enrich_with_sector_industry`**: Merge data from `get_sector_data()` into your DataFrame to add sector and industry columns.

### Expected Output

- A DataFrame enriched with new columns (e.g., daily returns, moving average, volatility, sector, industry).

---

## Task 4: Compute Monthly Stats

### Relevant Functions

_(Potentially from `transform_data.py`)_

1. `calculate_monthly_returns(df: pd.DataFrame) -> pd.DataFrame`
2. `calculate_stats(df: pd.DataFrame) -> pd.DataFrame`

### Instructions

- **`calculate_monthly_returns`**: Group data by month (using the Date column) and compute monthly returns using month-end prices or aggregated returns.
- **`calculate_stats`**: Produce summary statistics such as mean returns, max returns, min returns, or overall volatility.

### Expected Output

- A monthly returns DataFrame with columns like `Month`, `Monthly Return`.
- A stats DataFrame (or dictionary) with key indicators for the stock.

---

## Task 5: Visualization (Create Charts)

_(No specific standalone function for chart creation is currently visible in your codebase—likely these steps occur inside `generate_stock_analysis_html`.)_

- You may create separate functions for plotting, or embed them directly in the HTML generation step.
- Typical charts include:
  1. Stock price trend
  2. Daily/monthly returns
  3. Volatility
  4. (Optional) Heatmap of daily returns

### Expected Output

- Plotly figures or other visual outputs representing the stock's performance.

---

## Task 6: Generate HTML Report

### Function

1. **`generate_stock_analysis_html(stock_history: pd.DataFrame, monthly_returns: pd.DataFrame, stats: dict, output_file: str) -> None`**
   - Located in: `visualization.py`
   - Combines charts (price, returns, volatility) and tables (monthly returns, statistics) into an HTML file.

### Instructions

- Pass in your full DataFrame (`stock_history`), the monthly returns DataFrame, and the stats dictionary.
- Embed your charts (e.g., from Plotly) in a user-friendly HTML report.

### Expected Output

- An HTML file (e.g., `AAPL_stock_analysis.html`) containing:
  1. Graphs of stock prices, volatility, etc.
  2. A table of monthly returns.
  3. Summary statistics.

---

## Putting It All Together

After completing the above tasks, you will have:

1. A pipeline that reads raw CSV data (Tasks 1 & 2).
2. Enriched & transformed data sets with additional insights (Tasks 3 & 4).
3. Visual charts and an automated HTML report (Tasks 5 & 6).

Use your `main.py` script to stitch everything together in a logical sequence:

1. **Retrieve data** (Task 1).
2. **Clean data** if needed (Task 2).
3. **Enrich data** with returns, volatility, and sector info (Task 3).
4. **Compute monthly returns** and overall stats (Task 4).
5. **Create charts** and **generate** an HTML report (Tasks 5 & 6).

---

**Final Notes**

- Explore each function’s docstrings and confirm that inputs and outputs meet expectations.
- Add or refine data cleaning steps (Task 2) if necessary.
- Experiment with additional data visualization techniques (bar charts, scatter plots, heatmaps), especially if you want more variety in your HTML report.
