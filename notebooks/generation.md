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
with pandas.option_context('display.min_rows', 20, 'display.max_rows', 20):
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

# Test swapping levels

```python
# Import #
import pandas
from waste_flow.generation import waste_gen

# Load #
df = waste_gen.dry_mass

# Select rows for country #
df = df.loc[['AT']]

# Remove #
df = df.droplevel(0)

# Swap #
#df = df.swaplevel(0, 1)

# Swap #
#df = df.reorder_levels([1, 0])

# Swap #
df = df.reset_index()
df = df.sort_values(['nace_r2', 'year'])
df = df.set_index(['nace_r2', 'year'])

# Get all sectors #
sectors = df.index.levels[0]
print(sectors)

# One graph per sector #
result = [df.loc[[sec]] for sec in sectors]

# Show #
with pandas.option_context('display.min_rows', 20, 'display.max_rows', 20):
    display(result[0])
    display(result[1])
    display(result[2])
```
