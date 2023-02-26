# from pyecharts.charts import Line
# line = Line()
# line.add_xaxis(["中国","美国"])
# line.add_yaxis("gdp",[30,20,10])
# line.render()
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts
import json
import requests

url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'
headers = {
    "authority": "c.m.163.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "_ntes_nnid=9d08d30e2a7a27dab20a6cc8c7b83524,1596769155485; _ntes_nuid=9d08d30e2a7a27dab20a6cc8c7b83524",
    # "sec-ch-ua": ""Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24""
    # "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
resp = requests.get(url=url, headers=headers)
pro_date = resp.json()["data"]["areaTree"][2]["children"]
date_list = []
for pro_data in pro_date:
    if pro_data["name"] in ('北京', '上海', '重庆', '天津'):
        pro_name = pro_data["name"] + '市'
    else:
        pro_name = pro_data["name"] + '省'
    pro_confirm = pro_data["total"]["confirm"]
    date_list.append((pro_name, pro_confirm))
print(date_list)
map = Map()
map.add("地图", date_list, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 1000, "label": "1-1000人", "color": "#CCFFFF"},
            {"min": 1001, "max": 9999, "label": "1001-9999人", "color": "#CC6666"},
            {"min": 10000, "max": 199999, "label": "10000-199999人", "color": "#CC3333"}
        ]
    )
)

map.render("地图.html")
