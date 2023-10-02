import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        test_obj = category_factory(name="test_cat")
        assert test_obj.__str__() == "test_cat"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        test_obj = brand_factory(name="test_brand")
        assert test_obj.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        test_obj = product_factory(name="test_product")
        assert test_obj.__str__() == "test_product"
