from libc.math cimport sin, cos, acos
import math


def haversine(tuple coord1, tuple coord2):
    """Given two (lat, lng) tuples, returns the distance between them in
    meters."""
    cdef float lat1
    cdef float lng1
    cdef float lat2
    cdef float lng2
    lat1, lng1 = coord1
    lat2, lng2 = coord2

    cdef float ph1
    cdef float ph2
    cdef float theta1
    cdef float theta2
    cdef float c
    cdef float arc

    phi1 = (90.0 - lat1) * 0.0174532925
    phi2 = (90.0 - lat2) * 0.0174532925
    theta1 = lng1 * 0.0174532925
    theta2 = lng2 * 0.0174532925

    c = (sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2))
    arc = acos(c)
    return arc * 6367444.7
