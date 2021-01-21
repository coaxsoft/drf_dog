# DRF Dog

![Python package](https://github.com/coaxsoft/drf_dog/workflows/Python%20package/badge.svg)

Copy-paste utilities for Django REST Framework.

---

**Documentation** [https://coaxsoft.github.io/drf_dog](https://coaxsoft.github.io/drf_dog)

**Source code** [https://github.com/coaxsoft/drf_dog](https://github.com/coaxsoft/drf_dog)

---

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
