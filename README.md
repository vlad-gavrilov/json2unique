# JSON To Unique

Parses the [JSON](https://www.json.org/json-en.html) document into a list of unique elements

## Instructions

```bash
json2unique --help
```

```text
usage: json2unique [-h] [-d DEPTH] [infile] [outfile]

JSON parser

positional arguments:
  infile                the path to the JSON file to be parsed
  outfile               the path to the output file

optional arguments:
  -h, --help            show this help message and exit
  -d DEPTH, --depth DEPTH
                        set maximum recursion depth
```

If the optional ```infile``` or ```outfile``` arguments are not passed to utility, ```STDIN``` and ```STDOUT``` will be considered as default values.

For large JSON files with many nested objects, you can manually increase the recursion depth using ```-d``` flag. The default value is ```10_000```.

## Usage

### Command Line Interface

You can use this package both as a CLI utility and as a library. Here is an example of how to use it in the terminal:

```bash
json2unique array.json
```

```text
[1, 2, 42]
```

You can use Unix pipes to read STDIN and write to STDOUT streams:

```bash
echo '{"a": 1}' | json2unique > result.txt
cat result.txt 
```

```text
[1, 'a']
```

Manually type the desired JSON in the terminal (press ```Ctrl+D``` when finish typing):
```bash
json2unique                    
{"a": [34, "hello", -343.56]}
```

```text
['a', -343.56, 34, 'hello']
```

Use standard CLI Unix utilities to process the program's output:

```bash
json2unique array.json | grep 42
```

```text
[1, 2, 42]
```

If there is a non-valid JSON, ```json2unique``` will throw an appropriate exception and terminate with a non-zero code:
```bash
echo '{"a": 1""}' | json2unique
```

```text
Expecting ',' delimiter: line 1 column 8 (char 7)
```

Last exit code is:

```bash
echo $?
```

```text
1
```

### Python Library

To use this module as a library, enter the following line:

```python
import json2unique

json2unique.parse_json_to_list_of_unique({"a": 1})  # [1, 'a']
```
