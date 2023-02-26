# from pyecharts.charts import Line
# line = Line()
# line.add_xaxis(["中国","美国"])
# line.add_yaxis("gdp",[30,20,10])
# line.render()
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts
import json
import requests

map1 = Map()
data = [
    ("北京市", 200),
    ("上海", 2007),
    ("广东", 200)
]

map1.add("地图1", data, "china")
# map.set_global_opts(
#     title_opts=TitleOpts(title="地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min": 1, "max": 1000, "label": "1-1000人", "color": "#CCFFFF"},
#             {"min": 1001, "max": 9999, "label": "1001-9999人", "color": "#CC6666"},
#             {"min": 10000, "max": 199999, "label": "10000-199999人", "color": "#CC3333"}
#         ]
#     )
# )

map1.render()
