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

# Treatment

```python
import pandas
from waste_flow.zip_files import waste_trt
with pandas.option_context('display.min_rows', 10, 'display.max_rows', 10):
    display(waste_trt.df)
```

# Check waste categories avail

```python
from waste_flow.common  import wastes_selected
from waste_flow.zip_files import waste_trt

wastes_avail = waste_trt.df.waste.unique()
print(set(wastes_avail)    - set(wastes_selected))
print(set(wastes_selected) - set(wastes_avail))
```

# Unique values in columns

```python
from waste_flow.zip_files import waste_trt
print(waste_trt.df.wst_oper.unique())
print(waste_trt.df.waste.unique())
print(waste_trt.df.country.unique())
```

# Filtered

```python
import pandas
from waste_flow.treatment import waste_trt
print(waste_trt.filtered.waste.unique())
with pandas.option_context('display.min_rows', 10, 'display.max_rows', 10):
    display(waste_trt.filtered)
```

# Preview of long format

```python
import pandas
from waste_flow.treatment import waste_trt

with pandas.option_context('display.min_rows', 20, 'display.max_rows', 20):
    display(waste_trt.long_format)
```

# Preview of wide format

```python
import pandas
from waste_flow.treatment import waste_trt

with pandas.option_context('display.min_rows', 20, 'display.max_rows', 20):
    display(waste_trt.wide_format)
```

# Years available 

```python
# Import #
from waste_flow.treatment import waste_trt

# Process #
df = waste_trt.long_format

# Display #
print(df.year.unique())
```

# Check that TRT is a total

```python
# Import #
import pandas, numpy
from waste_flow.treatment import waste_trt as trt_processed
all_close = numpy.testing.assert_allclose
from waste_flow.zip_files import waste_trt

# Load #
df = waste_trt.df.copy()

# Include all #
from waste_flow.common import wastes_selected
df = df.query("waste in @wastes_selected")
df = df.melt(id_vars    = ['wst_oper', 'waste', 'country'],
             value_name = 'tonnes',
             var_name   = 'year')

# Process #
groups = df.groupby(['country', 'year', 'waste'])

# Function #
def check_tot(subdf):
    # Select total #
    selector = subdf['wst_oper'] == 'TRT' 
    tot  = subdf[selector].copy()
    rest = subdf[~selector].copy()
    # Assert #
    if len(tot) != 1:
        print(tot)
        print(rest)
        print('-------')
        assert False
    # Sum #
    sum_tot  = tot['tonnes'].iloc[0]
    sum_rest = rest['tonnes'].sum()
    # Case no total #
    if sum_tot != sum_tot: 
        if sum_rest == 0: return 'nan_ok'
        else:
            #print(tot)
            #print(rest)
            #print('-------')
            return 'nan_bad'
    # Assert #
    try:
        all_close(sum_tot, sum_rest, rtol=1e-2)
    except AssertionError:
        #print(tot)
        #print(rest)
        #print("%s AGAINST %s" % (sum_tot, sum_rest))
        #print('-------')
        return 'bad'
    # Return #
    return 'ok'
    
# Apply #
result = groups.apply(check_tot)

# Display #
print(result.value_counts())
#with pandas.option_context('display.min_rows', 20, 'display.max_rows', 20):
#    print(type(result))
#    display(result)
```

# Normalize

```python
# Import #
import pandas
from waste_flow.treatment import waste_trt

# Process #
df         = waste_trt.long_format.copy()
groups     = df.groupby(['country', 'year', 'waste'])
df['frac'] = groups.transform(lambda x: (x / x.sum()))
df         = df.drop(columns=['tonnes'])

# Filter #
result = df.query('country == "EU28"')
result = result.query('year    == "2010"')

# Filter #
result = df.query('country == "AT"')
result = result.query('year    == "2004"')

# Display #
with pandas.option_context('display.min_rows', 100, 'display.max_rows', 100):
    display(result)
```

# Check sums to one 

```python
# Import #
import pandas, numpy
from waste_flow.treatment import waste_trt
all_close = numpy.testing.assert_allclose

# Load #
df = waste_trt.normalized.copy()

# Process #
groups = df.groupby(['country', 'year', 'waste'])

# Function #
def check_sum_one(subdf):
    result = subdf['frac'].sum()
    return result
    
# Apply #
df = groups.apply(check_sum_one)

# Display #
print(df.value_counts())

# Display #
with pandas.option_context('display.min_rows', 100, 'display.max_rows', 100):
    display(df)
```
