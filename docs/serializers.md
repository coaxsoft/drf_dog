# Serializers

## Serializer Function Field

`SerializerFunctionField` is very similar to `SerializerMethodField`. except
you pass a function instead of a method to the field.

You should use `SerializerFunctionField` when you have to include the same 
functionality in several serializers.

### Example

Let's take a look to example when you need to return whether
authenticated user follows the other user.

With `SerializerMethodField` it will look like

```python
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    is_following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'is_following')

    def get_is_following(self, obj):
        return obj.followers.filter(
            pk=self.context['request'].user.pk
        ).exists()
```

Using `SerializerFunctionField` it will look like

```python
from rest_framework import serializers
from drf_dog.serializers import SerializerFunctionField


def get_is_following(obj, context):
    return obj.followers.filter(pk=context['request'].user.pk).exists()

class UserSerializer(serializers.ModelSerializer):
    is_following = SerializerFunctionField(function=get_is_following)

    class Meta:
        model = User
        fields = ('id', 'username', 'is_following')
```

This is very useful when you have several serializers relying on `get_is_following`.

For example,

```python
from rest_framework import serializers
from drf_dog.serializers import SerializerFunctionField

from my_project.utils import get_is_following


class AutocompleteUserSerializer(serializers.ModelSerializer):
    is_following = SerializerFunctionField(function=get_is_following)

    class Meta:
        model = User
        fields = ('id', 'username', 'is_following')


class RetrieveUserSerializer(serializers.ModelSerializer):
    is_following = SerializerFunctionField(function=get_is_following)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'avatar', 
                  'is_following')
```

So, above is some sort of solution to code duplication :tada:.
