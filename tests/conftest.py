import pytest
import pandas as pd
import geopandas as gpd
import shapely


@pytest.fixture
def origin():
    point_dict = {'geometry': [shapely.geometry.Point(435543,4644361)]}
    df = pd.DataFrame(data=point_dict)
    gdf = gpd.GeoDataFrame(df)
    return gdf


@pytest.fixture
def destination():
    dest_point_dict = {'geometry': [shapely.geometry.Point(436025,4644953),
                                    shapely.geometry.Point(435859,4644584),
                                    shapely.geometry.Point(435339,4645082)
                                    ],
                       'name': ['pointA', 'pointB', 'pointC']}
    df = pd.DataFrame(data=dest_point_dict)
    gdf = gpd.GeoDataFrame(df)
    return gdf
