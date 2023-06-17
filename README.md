# transportation-census-3jiod-tripend-map
## デモサイト
- https://shi-works.github.io/transportation-census-3jiod-tripend-map/
- サンプル画像
![image](https://user-images.githubusercontent.com/71203808/232194673-9ef94086-dfed-4ac5-9bdc-f42a288f3954.png)

# データ加工
## tripend_syuk.py
- [3次OD集計データ](https://github.com/shi-works/transportation-census-3jiod-pmtiles)をもとに、駅別の発生集中量（トリップエンド）を集計するプログラムです。
### 使用データ
- 3次OD集計データ
- 2021年12月某日1日目  
`https://xs489works.xsrv.jp/pmtiles-data/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_1_3jiod_od_pattern_count_add_coordinate.csv`,134.0MB
- 2021年12月某日2日目  
`https://xs489works.xsrv.jp/pmtiles-data/transportation-census/3jiod/02_3jiod_od_pattern_count_add_coordinate/out/202112_2_3jiod_od_pattern_count_add_coordinate.csv`,136.7MB

### 出力結果
- 2021年12月某日1日目  
`https://github.com/shi-works/transportation-census-3jiod-tripend-map/blob/main/202112_1_3jiod_tripend.csv`  
`https://github.com/shi-works/transportation-census-3jiod-tripend-map/blob/main/202112_1_3jiod_tripend.geojson`
- 2021年12月某日2日目  
`https://github.com/shi-works/transportation-census-3jiod-tripend-map/blob/main/202112_2_3jiod_tripend.csv`  
`https://github.com/shi-works/transportation-census-3jiod-tripend-map/blob/main/202112_2_3jiod_tripend.geojson`

# ライセンス
本データセット（使用データ及び出力結果）は[CC-BY-4.0](https://github.com/shi-works/traffic-accident-pmtiles/blob/main/LICENSE)で提供されます。使用の際には本レポジトリへのリンクを提示してください。

また、本データセットは、第13回大都市交通センサスの3次ODデータを加工して作成したものです。本データセットの使用・加工にあたっては、[国土交通省のリンク・著作権・免責事項](https://www.mlit.go.jp/link.html)を必ずご確認ください。

# 免責事項
利用者が当該データを用いて行う一切の行為について何ら責任を負うものではありません。
