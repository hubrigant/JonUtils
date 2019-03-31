import pytest
from JonUtils import Spatial


# @pytest.fixture
# def origin():
#     import pandas as pd
#     import geopandas as gpd
#     import shapely
#
#     point_dict = {'geometry': [shapely.geometry.Point('435543,4644361')]}
#     df = pd.DataFrame(data=point_dict)
#     gdf = gpd.GeoDataFrame(df)
#     return gdf
#
# @pytest.fixture
# def destination():
#     import pandas as pd
#     import geopandas as gpd
#     import shapely
#
#     point_dict = {'geometry': [shapely.geometry.Point('436025,4644953'),
#                                shapely.geometry.Point('435859,4644584'),
#                                shapely.geometry.Point('435339,4645082')
#                                ],
#                   'name': ['pointA','pointB','pointC']}
#     df = pd.DataFrame(data=point_dict)
#     gdf = gpd.GeoDataFrame(df)
#     return gdf


# def test_find_nearest():
#     with pytest.raises(TypeError):
#         Spatial.find_nearest()
#     with pytest.raises(ValueError):
#         Spatial.find_nearest(True)
#     origin_df = origin()
#     dest_df = destination()
#     assert Spatial.find_nearest(origin_df.iloc[0], dest_df=dest_df)
