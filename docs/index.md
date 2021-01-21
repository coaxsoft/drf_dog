# DRF Dog :dog:

![Python package](https://github.com/coaxsoft/drf_dog/workflows/Python%20package/badge.svg)

Copy-paste utilities for Django REST Framework.

---

**Documentation** [https://coaxsoft.github.io/drf_dog](https://coaxsoft.github.io/drf_dog)

**Source code** [https://github.com/coaxsoft/drf_dog](https://github.com/coaxsoft/drf_dog)

---

Why copy-paste utilities? Often, it is mentally hard to install
no name packages, especially, to commercial project, but it is easy to copy-paste
the solution from stack overflow or github. 

For this reason, we try to keep this project the way that it
can be easily installed from `PyPi` or just copy-pasted to your own code.

## Requirements

-  Python 3.7+
-  Django 3.0+
-  Django REST Framework 3.11+

## Installation

Install the package using ``pip``

```bash
pip install drf_dog
```

## Overview

### Serializer Function Field

Field you use when you want to prevent code duplication

```python
from drf_dog.serializers import SerializerFunctionField
from my_project.utils import get_is_following

is_following = SerializerFunctionField(function=get_is_following)
```

[Full docs :point_left:](serializers.md)

## License

This project is licensed under the terms of the ISC License
