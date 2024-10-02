import os
import requests
from datetime import datetime, timedelta

# ダウンロード先のディレクトリ
download_dir = "downloaded_files"
os.makedirs(download_dir, exist_ok=True)

# 日付の範囲を設定
start_date = datetime(2021, 4, 14)
end_date = datetime.today()

# 日付を一日ずつ増やしながらループ
current_date = start_date
while current_date <= end_date:
    # 日付をYYYY-MM-DD形式にフォーマット
    date_str = current_date.strftime("%Y-%m-%d")

    # URLを作成
    url = f"https://epss.cyentia.com/epss_scores-{date_str}.csv.gz"

    # ファイル名を決定
    file_name = f"epss_scores-{date_str}.csv.gz"
    file_path = os.path.join(download_dir, file_name)

    # ファイルをダウンロード
    try:
        # SSL証明書の検証を無効にするために verify=False を追加
        response = requests.get(url, verify=False)
        response.raise_for_status()  # エラーチェック

        # ファイルを保存
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {file_name}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {url}")
    except Exception as err:
        print(f"Other error occurred: {err} - {url}")

    # 次の日付に進む
    current_date += timedelta(days=1)
