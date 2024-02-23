import overpass
import geojson
from shapely.geometry import Polygon
import geopandas


# DEFINE THE COORDINATES OF THE AIRPORT AND THE SEARCH RADIUS
lat = float('52.30804523811394')
lon = float('4.759058118356535')

search_radius = '6000'
# radius (metres) around the coordinates where it will search for any terminal infra


# CALL API AND OBTAIN GEOJSON FORMATTED DATA OF THE SHAPE
api = overpass.API()
data_query = f'way["aeroway"="terminal"](around:{search_radius}, {lat}, {lon});out geom;'
api_geo_return = api.get(data_query, responseformat = 'geojson')
# this returns the raw geo data for the geojson file, which can then be saved as a file in the next step
print(api_geo_return)


# SAVE AS GEOJSON LINESTRING SHAPE:
with open(f'terminal_linestring_{round(lat, 2)}_{round(lon, 2)}.geojson', 'w') as output:
    output.write(geojson.dumps(api_geo_return))


# SAVE AS GEOJSON POLYGON:
features = []
for feature in api_geo_return['features']:
    if feature['geometry']['type'] == 'LineString':
        coords = feature['geometry']['coordinates']
        if not coords:
            print('Empty coordinate list:', feature)
            continue
        poly_coords = coords + [coords[0]]
        # append the first coordinate to close the area/shape
        poly = Polygon(poly_coords)
        new_feature = geojson.Feature(geometry = poly.__geo_interface__)
        features.append(new_feature)
    else:
        features.append(feature)

feature_collection = geojson.FeatureCollection(features)
print(feature_collection)
gdf = geopandas.GeoDataFrame.from_features(feature_collection)
# convert into a geodataframe to allow for setting the coordinate ref system (crs) and save the file geolocated
gdf.crs = 'EPSG:4326'
# WGS84 (EPSG: 4326)

gdf.to_file(f'terminal_polygon{round(lat, 2)}_{round(lon, 2)}.geojson', driver = 'GeoJSON')
# export to file for import into qgis, etc


# MERGE THE VARIOUS PARTS OF THE TML SHAPE INTO ONE SINGLE
sub_polygon_geometries = []
for index, row in gdf.iterrows():
    sub_polygon_geometries.append(row['geometry'])

sub_polygon_series = geopandas.GeoSeries(sub_polygon_geometries)
# for the merging (unary_union), the object needs to be a geoseries instead of list, hence conversion here
merged_polygon = sub_polygon_series.unary_union
# this merges all TML parts into one polygon

merged_gdf = geopandas.GeoDataFrame(geometry = [merged_polygon])
# convert to gdf to set crs in next step and save file as geojson
merged_gdf.crs = 'EPSG:4326'
merged_gdf.to_file(f'terminal_merged_polygon{round(lat, 2)}_{round(lon, 2)}.geojson', driver='GeoJSON')
