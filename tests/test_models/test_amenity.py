#!/usr/bin/python3
"""TestCases for the Amenity Class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test case Class for Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initializes test_Amenity"""
        super(test_Amenity, self).__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test the name attribute in Amenity class"""
        new = self.value()
        self.assertEqual(type(new.name), str)
