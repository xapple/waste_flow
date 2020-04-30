---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
import pandas
from waste_flow.zip_files import waste_gen, waste_trt
```

# Raw

```python
with pandas.option_context('display.min_rows', 3000, 'display.max_rows', 3000):
    display(waste_gen.raw_csv)
```

```python
with pandas.option_context('display.min_rows', 3000, 'display.max_rows', 3000):
    display(waste_trt.raw_csv)
```

# Columns 

```python
print(waste_gen.processed_csv.columns)
print(waste_trt.processed_csv.columns)
```

# Profiling

```python
from pandas_profiling import ProfileReport
waste_gen_profile = ProfileReport(waste_gen.df, html={'style': {'full_width': True}})
waste_trt_profile = ProfileReport(waste_trt.df, html={'style': {'full_width': True}})
```

```python
waste_gen_profile.to_widgets()
```

```python
waste_trt_profile.to_widgets()
```

# Check filtered dataframe

```python
import pandas
from waste_flow.zip_files import waste_gen, waste_trt
with pandas.option_context('display.min_rows', 100, 'display.max_rows', 100):
    display(waste_gen.df)
```

```python
import pandas
from waste_flow.zip_files import waste_gen, waste_trt
with pandas.option_context('display.min_rows', 100, 'display.max_rows', 100):
    display(waste_trt.df)
```

# Filter

```python
with pandas.option_context('display.min_rows', 50, 'display.max_rows', 50):
    display(waste_gen.df)
```

```python
with pandas.option_context('display.min_rows', 50, 'display.max_rows', 50):
    display(waste_gen.df)
```
