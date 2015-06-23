from math import cos, sin, pi, radians, degrees

from shapely.geometry import Polygon
from shapely.ops import cascaded_union


def merkator():
    """ Return coordinates of world merkator projection """
    return [
        (85, 180), (85, 90), (85, 0), (85, -90), (85, -180), (0, -180), (-85, -180),
        (-85, -90), (-85, 0), (-85, 90), (-85, 180), (0, 180), (85, 180)]


def geo_circle(latitude, longitude, radius):
    """ Create circle for planet parameters """
    earthsradius = 6371.0   # earths radius in km
    resolution = 77         # number of points in polygon
    
    # find the raidus in lat/lon 
    radius_lat = degrees(radius / earthsradius)
    radius_lng = radius_lat / cos(radians(latitude)) 

    master, slave = [], []

    for index in range(resolution + 1):
        # circle angle
        theta =  2. * pi / resolution * index
        # current point
        ey = longitude + radius_lng * cos(theta)  # center a + radius x * cos(theta) 
        ex = latitude + radius_lat * sin(theta)   # center b + radius y * sin(theta) 
        # insert point into polygon
        if -180 <= ey <= 180:
            master.append((ex, ey))
        else:
            # when world is over - need to divide point into both world
            slave.append((ex, ey + 2 * 180 * (-1) ** int(ey > 180)))
            master.append((ex, 180 * (-1) ** int(ey < -180)))

    return master, slave


def polygon_union(points):
    """ Create polygon union for points """
    polygons = []
    for point in points:
        a, b = geo_circle(*point)
        polygons.append(Polygon(a))
        if b:
            polygons.append(Polygon(b))
    # merge polygons into union
    union = cascaded_union(polygons)
    coords = []
    if union.geom_type != 'MultiPolygon':
        # if only one polygon result - return they coords
        coords.append(list(reversed(list(union.exterior.coords))))
    else:
        # otherwise return multi coords for each polygon
        for polygon in union:
            coords.append(list(reversed(list(polygon.exterior.coords))))
    return coords


def wrap_google(polygons):
    """ Return google points for polygons """
    point_str = 'new google.maps.LatLng(%s, %s),'
    result = ''
    for polygon in polygons:
        result += '['
        for point in polygon:
            result += point_str % point
        result += '],'
    return result


def get_map_js(points):
    """ Create maps coords Js code """
    # get all of holes
    polygons = polygon_union(points)
    # get merkator and insert it into polygons
    polygons.insert(0, merkator())
    # wrap all into js
    js_string = wrap_google(polygons)
    return js_string.rstrip(',')
