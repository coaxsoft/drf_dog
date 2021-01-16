import pytest
from rest_framework import serializers

from drf_dog.serializers import SerializerFunctionField


class TestSerializerFunctionField:

    def test_field(self):
        return_value = 0

        def _func(*args, **kwargs):
            return return_value

        class _Serializer(serializers.Serializer):
            f = SerializerFunctionField(function=_func)

        s = _Serializer(instance={})
        assert s.data['f'] == return_value

    def test_field_with_instance(self):
        return_value = {'instance': True}

        def _func(value, *args, **kwargs):
            return value

        class _Serializer(serializers.Serializer):
            f = SerializerFunctionField(function=_func)

        s = _Serializer(instance=return_value)
        assert s.data['f'] == return_value

    def test_field_with_context(self):
        context_value = {'instance': True}

        def _func(_, context):
            return context

        class _Serializer(serializers.Serializer):
            f = SerializerFunctionField(function=_func)

        s = _Serializer(instance={}, context=context_value)
        assert s.data['f'] == context_value

    def test_field_without_function(self):

        class _Serializer(serializers.Serializer):
            f = SerializerFunctionField(function=None)

        s = _Serializer(instance={})
        with pytest.raises(AttributeError):
            assert s.data['f']
