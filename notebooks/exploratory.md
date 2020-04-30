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

# Pickle

```python
del waste_gen.processed_csv
del waste_trt.processed_csv
print(waste_gen.processed_csv.shape)
print(waste_trt.processed_csv.shape)
```

# Columns 

```python
print(waste_gen.df.columns)
print(waste_trt.df.columns)
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

# Check values

```python
print(waste_gen.df.nace_r2.unique())
```

```python
print(waste_trt.df.wst_oper.unique())
```

```python
print(waste_gen.df.waste.unique())
```

```python
print(waste_gen.df.waste.unique())
```

```python
gen = set(waste_gen.df.waste.unique())
trt = set(waste_trt.df.waste.unique())
print(gen ^ trt)
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

# Filter

```python
with pandas.option_context('display.min_rows', 50, 'display.max_rows', 50):
    display(waste_gen.df)
```

```python
with pandas.option_context('display.min_rows', 50, 'display.max_rows', 50):
    display(waste_gen.df)
```
