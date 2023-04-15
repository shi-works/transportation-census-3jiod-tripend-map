import csv
from collections import defaultdict

# 3次OD集計データを辞書に読み込み
unique_stations = defaultdict(lambda: {'count': 0, 'lat': 0, 'lon': 0})

# ファイルを開く
with open("./out/202112_2_3jiod_od_pattern_count_add_coordinate.csv", mode="r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        in_station = (row['入場事業者名'], row['入場路線名'], row['入場駅名'])
        out_station = (row['出場事業者名'], row['出場路線名'], row['出場駅名'])

        unique_stations[in_station]['count'] += int(row['件数'])
        unique_stations[out_station]['count'] += int(row['件数'])

        unique_stations[in_station]['lat'] = row['入場駅_緯度']
        unique_stations[in_station]['lon'] = row['入場駅_経度']
        unique_stations[out_station]['lat'] = row['出場駅_緯度']
        unique_stations[out_station]['lon'] = row['出場駅_経度']

# 結果をファイルに書き出す
with open("./out/202112_2_3jiod_tripend.csv", mode="w", encoding="utf-8", newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['緯度', '経度', '事業者名', '路線名', '駅名', '件数'])

    for station, info in unique_stations.items():
        writer.writerow([info['lat'], info['lon']] +
                        list(station) + [info['count']])

print(u'処理終了')
