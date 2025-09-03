# Robust CSV Test Assertions for Unordered Data

## Problem

CI tests for CSV export failed due to assumptions about row and column order, which are not guaranteed in the output. Local builds passed, but CI failed due to data order differences.

## Solution

Modified the test to use the `pandas` library to read the CSV into a DataFrame. Assertions were then performed on the DataFrame, allowing for order-independent checks of data presence and values across rows and columns.

## Impact

Prevents flaky CI failures caused by non-deterministic data ordering, leading to more reliable and stable test suites.

## Takeaways

* Always assume data order (rows and columns) in file exports (CSV, JSON, etc.) is non-deterministic unless explicitly guaranteed by the export mechanism.
* Use robust data parsing libraries (for example, `pandas` for CSV/Excel, `json` for JSON) to load exported data into structured formats (DataFrames, dictionaries) for testing.
* Perform assertions on the structured data using key-based lookups or filtering, rather than relying on line numbers or fixed column indices.
