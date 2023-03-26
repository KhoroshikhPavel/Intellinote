from timezonefinder import TimezoneFinder

tf = TimezoneFinder()  # reuse

query_points = [(37.319671, 55.63865)]
for lng, lat in query_points:
    tz = tf.timezone_at(lng=lng, lat=lat)