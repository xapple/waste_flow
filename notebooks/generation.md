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
import waste_flow
```

# Countries

```python
from waste_flow.mappings   import wastes_selected
from waste_flow.mappings   import nace_selected

print(len(wastes_selected) * len(nace_selected) * len((2016, 2014, 2012, 2010, 2008, 2006, 2004)))

from waste_flow.generation import waste_gen
    
display(waste_gen.long_format
        .groupby(['country'])
        .size())

print(waste_gen.long_format.country.unique())
```

# Preview of filtered

```python
import pandas
from waste_flow.generation import waste_gen
with pandas.option_context('display.min_rows', 10, 'display.max_rows', 10):
    display(waste_gen.filtered)
```

# Filtered dtypes

```python
import numpy
from waste_flow.generation import waste_gen

df = waste_gen.filtered
print(df.dtypes)
[name for name, kind in df.dtypes.items() if kind == object]
```

# Preview of long format

```python
import pandas
from waste_flow.generation import waste_gen
with pandas.option_context('display.min_rows', 10, 'display.max_rows', 10):
    display(waste_gen.long_format)
```

# Preview of wide format

```python
import pandas
from waste_flow.generation import waste_gen
with pandas.option_context('display.min_rows', 10, 'display.max_rows', 10):
    display(waste_gen.wide_format)
```

# Check waste categories avail

```python
from waste_flow.mappings   import wastes_selected
from waste_flow.zip_files  import waste_gen

wastes_avail = waste_gen.df.waste.unique()
print(len(wastes_avail))
print(len(wastes_selected))
print(set(wastes_selected) - set(wastes_avail))
```

# Check nace categories

```python
from waste_flow.mappings   import nace_selected
from waste_flow.zip_files  import waste_gen

nace_avail = waste_gen.df.nace_r2.unique()
print(len(nace_avail))
print(len(nace_selected))
print(set(nace_selected) - set(nace_avail))
```

# Remove municipal

```python
import pandas
from waste_flow.generation import waste_gen
with pandas.option_context('display.min_rows', 20, 'display.max_rows', 20):
    display(waste_gen.spread_muni)
```

# Convert to dry weight

```python
import pandas
from waste_flow.generation import waste_gen
from waste_flow import module_dir

df = waste_gen.spread_muni

dry_coef = module_dir + 'extra_data/dry_weight_coef.csv'
dry_coef = pandas.read_csv(str(dry_coef), index_col=0)
dry_coef = dry_coef.fraction

with pandas.option_context('display.min_rows', 20, 'display.max_rows', 20):
    display(dry_coef)
    display(df)
    
result = df * dry_coef * 1000

with pandas.option_context('display.min_rows', 20, 'display.max_rows', 20):
    display(result)
```

```python

```

```python

```
