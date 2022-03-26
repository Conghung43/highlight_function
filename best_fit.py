from skspatial.objects import Line
from skspatial.objects import Points
from skspatial.plotting import plot_3d
from skspatial.objects import Plane
import geometry_calculation as cal
import math

def line_best_fit(points):

    points = Points(points)

    line_fit = Line.best_fit(points)

    return line_fit

def plane_best_fit(points):

    points = Points(points)

    plane_fit = Plane.best_fit(points)

    return plane_fit
