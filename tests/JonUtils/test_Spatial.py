import pytest
from JonUtils import Spatial


class TestSpatial():
    def test__init__(self, origin):
        assert True

    def test_find_nearest(self, origin, destination):
        with pytest.raises(TypeError):
            Spatial.find_nearest()
        with pytest.raises(ValueError):
            Spatial.find_nearest(True)
        origin_df = origin
        dest_df = destination
        with pytest.raises(ValueError):
            Spatial.find_nearest(origin_df.iloc[0])
        with pytest.raises(TypeError):
            Spatial.find_nearest(origin_df.iloc[0], dest_df=dest_df, blarf=True)
        assert Spatial.find_nearest(origin_df.iloc[0], dest_df=dest_df)
        nearest_index, distance = Spatial.find_nearest(origin_df.iloc[0], dest_df=dest_df)
        assert nearest_index == 1
        assert distance == 386.76220084180926