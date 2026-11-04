# Python Dictionaries

## What is a Dictionary?

A dictionary is a collection that stores data in **key-value pairs**.

Each item in a dictionary has a key and a value.

```python
server = {
    "name": "web-server1",
    "status": "running",
    "port": 8080
}
```

In this example:

- `"name"` is a key and `"web-server1"` is its value.
- `"status"` is a key and `"running"` is its value.
- `"port"` is a key and `8080` is its value.

Dictionaries are useful when I want to store related information together and access that information using a name/key instead of an index.

Dictionaries are:

- Mutable
- Dynamic
- Ordered
- Able to store different types of values
- Based on key-value pairs

Dictionary keys must be unique.

---

## Creating a Dictionary

A dictionary can be created using curly brackets `{}`.

```python
server = {
    "name": "web-server1",
    "status": "running"
}
```

Each key and value is separated using a colon `:`.

Multiple key-value pairs are separated using commas.

```python
server = {
    "name": "web-server1",
    "status": "running",
    "port": 8080
}
```

An empty dictionary can be created using:

```python
server = {}
```

I can also use the `dict()` constructor:

```python
server = dict()
```

Both create an empty dictionary.

---

## Dictionary Keys

Dictionary keys are used to identify the values stored in the dictionary.

```python
server = {
    "name": "web-server1",
    "status": "running"
}
```

Here, `"name"` and `"status"` are the keys.

Keys must be **hashable**, which means they can be used by Python to locate the value efficiently.

Common types that can be used as dictionary keys include:

```python
"name"
10
3.14
True
```

Tuples can also be used as keys as long as all of the values inside the tuple are hashable.

```python
locations = {
    (10, 20): "server-room"
}
```

Lists cannot be used as dictionary keys because lists are mutable.

```python
# This will not work
data = {
    [1, 2]: "value"
}
```

Sets and dictionaries also cannot be used as dictionary keys.

---

## Dictionary Values

Dictionary values do not have the same restrictions as keys.

Values can be strings, integers, floats, Booleans, lists, tuples, sets, dictionaries, or other Python objects.

```python
server = {
    "name": "web-server1",
    "port": 8080,
    "active": True,
    "tags": ["web", "production"]
}
```

Different keys can also have the same value.

```python
servers = {
    "server1": "running",
    "server2": "running",
    "server3": "running"
}
```

There is no problem with this because the keys are different.

---

## Duplicate Dictionary Keys

Dictionary keys must be unique.

If the same key is used more than once, the later value replaces the previous value.

```python
server = {
    "status": "running",
    "status": "stopped"
}
```

The final value of `"status"` will be:

```python
"stopped"
```

Python does not keep both values under the same key.

---

# Accessing Dictionary Values

Dictionary content can be accessed by keys.

To retrieve a value from a dictionary, I can specify its corresponding key in square brackets `[]` after the dictionary name.

```python
MLB_teams = {
    "Minnesota": "Twins",
    "Boston": "Red Sox"
}

print(MLB_teams["Minnesota"])
```

Output:

```text
Twins
```

The key is used to retrieve the value associated with it.

For example:

```python
server["status"]
```

means I am retrieving the value associated with the `"status"` key.

---

## KeyError

When I refer to a key that isn't in the dictionary, Python raises a `KeyError`.

```python
server = {
    "name": "web-server1",
    "status": "running"
}

print(server["port"])
```

Since `"port"` does not exist, Python raises:

```text
KeyError
```

This is important when accessing dictionary values directly because the key needs to exist.

---

# Populating Dictionaries Incrementally

A dictionary can be populated one item at a time.

```python
server = {}

server["name"] = "web-server1"
server["status"] = "running"
server["port"] = 8080
```

The dictionary now contains:

```python
{
    "name": "web-server1",
    "status": "running",
    "port": 8080
}
```

This is useful when I don't have all the information when I first create the dictionary.

I can start with an empty dictionary and add the values as I get them.

---

## Adding a New Key

If the key does not already exist, assigning a value to it adds the key to the dictionary.

```python
server = {
    "name": "web-server1"
}

server["status"] = "running"
```

Now the dictionary contains:

```python
{
    "name": "web-server1",
    "status": "running"
}
```

---

## Updating an Existing Key

If the key already exists, assigning a new value updates the existing value.

```python
server = {
    "name": "web-server1",
    "status": "running"
}

server["status"] = "stopped"
```

The value of `"status"` is now `"stopped"`.

The key is not duplicated.

The existing value is simply replaced.

---

# Using `dict()`

`dict()` can be used to create a dictionary.

```python
server = dict()
```

This creates an empty dictionary.

I can also pass data to `dict()`.

```python
server = dict(
    name="web-server1",
    status="running"
)
```

This creates:

```python
{
    "name": "web-server1",
    "status": "running"
}
```

The `dict()` constructor can also accept an iterable containing key-value pairs.

---

# Using `zip()` to Create a Dictionary

`zip()` can be used to combine two sequences.

One sequence can contain the keys and the other can contain the values.

```python
keys = ["name", "status", "port"]
values = ["web-server1", "running", 8080]

server = dict(zip(keys, values))
```

The result is:

```python
{
    "name": "web-server1",
    "status": "running",
    "port": 8080
}
```

The first item from `keys` is paired with the first item from `values`, and so on.

---

# `dict.fromkeys()`

`dict.fromkeys()` creates a dictionary using a sequence of keys.

```python
servers = ["web1", "web2", "web3"]

data = dict.fromkeys(servers)
```

The result is:

```python
{
    "web1": None,
    "web2": None,
    "web3": None
}
```

I can also provide a default value.

```python
data = dict.fromkeys(servers, "running")
```

The result is:

```python
{
    "web1": "running",
    "web2": "running",
    "web3": "running"
}
```

---

# Using `.get()`

The `.get()` method can be used to retrieve a value from a dictionary.

```python
server = {
    "name": "web-server1",
    "status": "running"
}

print(server.get("status"))
```

Output:

```text
running
```

The main difference between `.get()` and using square brackets is what happens when the key does not exist.

```python
server["port"]
```

raises a `KeyError` if `"port"` does not exist.

But:

```python
server.get("port")
```

returns:

```text
None
```

I can also provide a default value to `.get()`.

```python
server.get("port", 80)
```

If `"port"` does not exist, `80` will be returned.

---

# `.keys()`

The `.keys()` method returns the keys in a dictionary.

```python
server = {
    "name": "web-server1",
    "status": "running",
    "port": 8080
}

print(server.keys())
```

I can also loop through the keys.

```python
for key in server.keys():
    print(key)
```

Output:

```text
name
status
port
```

---

# `.values()`

The `.values()` method returns the values in a dictionary.

```python
for value in server.values():
    print(value)
```

Output:

```text
web-server1
running
8080
```

This is useful when I only need the values and don't need the keys.

For example, if I have:

```python
servers = {
    "web-server1": "running",
    "web-server2": "stopped",
    "database-server": "running"
}
```

I can check the values:

```python
for value in servers.values():
    if value == "running":
        print("Server is running")
```

---

# `.items()`

The `.items()` method returns the key-value pairs.

```python
for key, value in server.items():
    print(key, value)
```

Output:

```text
name web-server1
status running
port 8080
```

`.items()` is useful when I need both the key and its value while looping through a dictionary.

---

# `.setdefault()`

The `.setdefault()` method returns the value of a key if it exists.

If the key does not exist, it creates the key with a default value.

```python
server = {
    "name": "web-server1"
}

server.setdefault("status", "unknown")
```

The dictionary becomes:

```python
{
    "name": "web-server1",
    "status": "unknown"
}
```

If `"status"` already existed, `.setdefault()` would keep the existing value instead of replacing it.

---

# `.update()`

The `.update()` method can be used to add or update multiple dictionary items.

```python
server = {
    "name": "web-server1"
}

server.update({
    "status": "running",
    "port": 8080
})
```

The result is:

```python
{
    "name": "web-server1",
    "status": "running",
    "port": 8080
}
```

If a key already exists, `.update()` changes its value.

```python
server.update({
    "status": "stopped"
})
```

Now:

```python
"status": "stopped"
```

---

# Removing Dictionary Items

## `.pop()`

The `.pop()` method removes a specified key and returns its value.

```python
server = {
    "name": "web-server1",
    "status": "running",
    "port": 8080
}

port = server.pop("port")
```

The value removed is stored in `port`.

```python
print(port)
```

Output:

```text
8080
```

The `"port"` key is also removed from the dictionary.

---

## `del`

The `del` statement can be used to remove a key-value pair.

```python
del server["port"]
```

Unlike `.pop()`, `del` does not return the removed value.

---

## `.popitem()`

The `.popitem()` method removes and returns the last key-value pair in the dictionary.

```python
server.popitem()
```

The removed key-value pair is returned.

Dictionaries maintain insertion order, so `.popitem()` removes the last inserted item.

---

## `.clear()`

The `.clear()` method removes all items from a dictionary.

```python
server.clear()
```

The dictionary becomes:

```python
{}
```

The dictionary still exists, but it is now empty.

---

# Copying Dictionaries

The `.copy()` method creates a copy of a dictionary.

```python
server_copy = server.copy()
```

The new dictionary contains the same key-value pairs as the original.

```python
server = {
    "name": "web-server1",
    "status": "running"
}

server_copy = server.copy()
```

Now both dictionaries contain the same information.

`.copy()` creates a shallow copy.

This means that nested mutable objects inside the dictionary can still be shared between the original and the copy.

---

# Checking if a Key Exists

The `in` operator can be used to check whether a key exists in a dictionary.

```python
server = {
    "name": "web-server1",
    "status": "running"
}

print("status" in server)
```

Output:

```text
True
```

I can also use `not in`.

```python
print("port" not in server)
```

Output:

```text
True
```

When using `in` with a dictionary, Python checks the keys.

---

# Dictionary Equality

Two dictionaries can be compared using `==`.

```python
server1 = {
    "name": "web-server1",
    "status": "running"
}

server2 = {
    "name": "web-server1",
    "status": "running"
}

print(server1 == server2)
```

Output:

```text
True
```

The dictionaries are equal because they contain the same key-value pairs.

The order of the key-value pairs does not affect dictionary equality.

---

# Dictionary Union

The `|` operator can be used to combine dictionaries.

```python
server_info = {
    "name": "web-server1",
    "status": "running"
}

network_info = {
    "ip": "10.0.1.10",
    "port": 8080
}

server = server_info | network_info
```

The result contains the items from both dictionaries.

```python
{
    "name": "web-server1",
    "status": "running",
    "ip": "10.0.1.10",
    "port": 8080
}
```

If both dictionaries contain the same key, the value from the dictionary on the right is used.

---

# Dictionary Iteration

A dictionary can be looped through directly.

```python
for key in server:
    print(key)
```

When looping directly through a dictionary, the keys are returned.

To get the values:

```python
for value in server.values():
    print(value)
```

To get both keys and values:

```python
for key, value in server.items():
    print(key, value)
```

---

# Dictionary Comprehensions

A dictionary comprehension is a way of creating a dictionary using a compact syntax.

For example:

```python
numbers = {
    number: number * 2
    for number in range(1, 6)
}
```

This creates:

```python
{
    1: 2,
    2: 4,
    3: 6,
    4: 8,
    5: 10
}
```

The basic structure is:

```python
{
    key: value
    for item in iterable
}
```

A condition can also be included.

```python
numbers = {
    number: number * 2
    for number in range(1, 6)
    if number % 2 == 0
}
```

This only includes the even numbers.

---

# Nested Dictionaries

A dictionary can contain another dictionary as a value.

```python
servers = {
    "web-server": {
        "status": "running",
        "port": 80
    },
    "database-server": {
        "status": "running",
        "port": 5432
    }
}
```

To access the web server's status:

```python
print(servers["web-server"]["status"])
```

Output:

```text
running
```

The first key accesses the inner dictionary and the second key accesses the value inside it.

---

# Dictionaries with Lists

A dictionary value can also be a list.

```python
server = {
    "name": "web-server1",
    "tags": ["web", "production", "nginx"]
}
```

I can access the list using the dictionary key:

```python
print(server["tags"])
```

I can also access an individual item from the list:

```python
print(server["tags"][0])
```

Output:

```text
web
```

This is useful when one key needs to store multiple related values.

---

# `len()` with Dictionaries

`len()` returns the number of key-value pairs in a dictionary.

```python
server = {
    "name": "web-server1",
    "status": "running",
    "port": 8080
}

print(len(server))
```

Output:

```text
3
```

There are three key-value pairs in the dictionary.

---

# `all()` and `any()`

`all()` can be used to check whether all items in an iterable are true.

`any()` checks whether at least one item is true.

These can also be used with dictionaries.

When used directly on a dictionary, the keys are what are evaluated.

---

# `sorted()`

`sorted()` can be used to sort dictionary keys.

```python
servers = {
    "server3": "running",
    "server1": "stopped",
    "server2": "running"
}

print(sorted(servers))
```

This returns the keys in sorted order.

I can also sort dictionary items based on their values.

```python
sorted(servers.items(), key=lambda item: item[1])
```

Here:

```python
item[0]
```

represents the key.

```python
item[1]
```

represents the value.

So if I want to sort by values, I use `item[1]`.

---

# Sorting in Reverse

I can use `reverse=True` to sort in descending order.

```python
sorted(
    servers.items(),
    key=lambda item: item[1],
    reverse=True
)
```

This reverses the sorting order.

---

# `sum()` with Dictionary Values

`sum()` can be used with dictionary values when the values are numbers.

```python
servers = {
    "server1": 20,
    "server2": 30,
    "server3": 50
}

total = sum(servers.values())

print(total)
```

Output:

```text
100
```

The `.values()` method gets the numbers and `sum()` adds them together.

---

# `min()` and `max()`

`min()` and `max()` can be used to find the smallest or largest values.

```python
cpu_usage = {
    "server1": 20,
    "server2": 70,
    "server3": 45
}

print(min(cpu_usage.values()))
print(max(cpu_usage.values()))
```

Output:

```text
20
70
```

This can be useful when working with things such as CPU usage, memory usage, or other numerical monitoring data.

---

# `Counter`

`Counter` is available from the `collections` module.

It is used for counting how many times values occur.

```python
from collections import Counter
```

For example:

```python
letters = Counter("mississippi")
```

The `Counter` keeps track of how many times each character appears.

I can use `.most_common()` to see the most common values.

```python
letters.most_common()
```

This returns the values and their counts.

---

# `defaultdict`

`defaultdict` is also available from the `collections` module.

It provides a default value when a key does not exist.

For example:

```python
from collections import defaultdict
```

I can create a `defaultdict` containing lists:

```python
employees = defaultdict(list)
```

If I access a key that does not exist, a new empty list is created automatically.

This can be useful for grouping data.

For example, employees can be grouped by department.

---

# `OrderedDict`

`OrderedDict` is another dictionary-like class available from `collections`.

```python
from collections import OrderedDict
```

It was commonly used when explicit ordering behavior was needed.

Normal Python dictionaries preserve insertion order in modern versions of Python, so `OrderedDict` is less necessary for basic ordering than it used to be.

---

# Dictionary-Like Classes

Python also allows me to create my own dictionary-like classes.

I can inherit from `dict` and add additional methods.

For example:

```python
class SortableDict(dict):

    def sort_by_keys(self):
        return sorted(self.items())

    def sort_by_values(self):
        return sorted(
            self.items(),
            key=lambda item: item[1]
        )
```

This creates a dictionary-like class with additional sorting methods.

I can also use `UserDict` from the `collections` module when creating custom dictionary-like classes.

---

# Dictionary Methods to Remember

| Method | What it does |
|---|---|
| `get()` | Gets a value without raising `KeyError` |
| `keys()` | Gets the dictionary keys |
| `values()` | Gets the dictionary values |
| `items()` | Gets key-value pairs |
| `setdefault()` | Gets a value or creates a default |
| `update()` | Adds or updates items |
| `pop()` | Removes a specified key |
| `popitem()` | Removes the last key-value pair |
| `clear()` | Removes everything |
| `copy()` | Creates a shallow copy |

---

# Important Things to Remember

- Dictionaries store data as **key-value pairs**.
- Keys must be **unique**.
- Keys must be **hashable**.
- Values can be different data types.
- Dictionaries are mutable, so I can add, update and remove items.
- I use square brackets `[]` to access a value using its key.
- Accessing a key that does not exist using `[]` causes a `KeyError`.
- `.get()` can be used when I want to avoid a `KeyError`.
- `.keys()` returns the keys.
- `.values()` returns the values.
- `.items()` returns both keys and values.
- `in` and `not in` can be used to check for keys.
- Dictionaries can contain lists and other dictionaries as values.
- Dictionaries can be looped through.
- Dictionary comprehensions provide a shorter way to create dictionaries.
- `Counter`, `defaultdict`, and `OrderedDict` are dictionary-related classes from `collections`.

## Basic Dictionary Pattern

```python
server = {
    "name": "web-server1",
    "status": "running",
    "port": 8080
}
```

Access a value:

```python
print(server["status"])
```

Add or update:

```python
server["status"] = "stopped"
```

Get a value safely:

```python
server.get("status")
```

Loop through keys:

```python
for key in server:
    print(key)
```

Loop through values:

```python
for value in server.values():
    print(value)
```

Loop through both:

```python
for key, value in server.items():
    print(key, value)
```

This is the main structure I need to understand before moving on to more advanced dictionary operations.