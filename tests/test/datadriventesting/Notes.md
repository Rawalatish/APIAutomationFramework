

# Data driven testing in API automation

1. Excel File  (download csv file as .xlsx format). We cam also create via Google Drive(Excel)
2. pip install openpyxl
2. Create your script
# Data Driven testing we can do by below two ways
3. for loop to read the file every  data and run it 
or
4. Data Driven Testing  feature of pytest

**************************
# Data Driven Testing (DDT) in API Automation

Data Driven Testing allows us to execute the same test logic multiple times with different sets of data (Positive, Negative, Edge cases) from an external source.

## 1. Prerequisites
* **Data Source:** Use an **Excel sheet** (convert/download CSV files to `.xlsx` format for better compatibility with modern libraries).
* **Environment:** Ensure libraries like `pandas` or `openpyxl` are installed to read Excel files.

## 2. Implementation Strategies

You can implement DDT in your script using two primary methods:

### Method A: Using a `for` loop (Manual Iteration)
* **How it works:** You write a utility function to read all rows from the Excel file and use a standard Python `for` loop to iterate through each row inside your test function.
* **Pros:** Simple to implement.
* **Cons:** If one data set fails, the loop might break. Pytest treats the entire loop as **one single test case** in the final report.

### Method B: Pytest `@pytest.mark.parametrize` (Professional Way)
* **How it works:** Use the built-in [Pytest Parameterization](https://docs.pytest.org) decorator. You pass the data list to the decorator, and it injects the data into the test function.
* **Pros:** 
  - Each row of data is treated as a **separate test case**.
  - If one row fails, Pytest continues to run the others.
  - Detailed reporting: You can see exactly which data set caused a failure.
  - Very clean and scalable for large Frameworks.

## 3. Workflow Summary
1. Prepare the **Excel/CSV** data file.
2. Create a **Utility/Helper** method to read the file and return a list of tuples/dictionaries.
3. Decorate the test method using `@pytest.mark.parametrize`.
4. Run the script and analyze the per-data-set results in the report.
