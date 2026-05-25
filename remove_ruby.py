import os
from pathlib import Path
import re

# 読み込み対象のディレクトリパス
r_directory_path = 'src/'

# 書き込み対象のディレクトリパス
w_directory_path ='book/no_ruby'

# 書き込み対象のディレクトリ作成
if not os.path.exists(w_directory_path):
    os.makedirs(w_directory_path)
    print(f"{w_directory_path} を作成しました。")

# ディレクトリ内のファイルとサブディレクトリの一覧を取得
file_list = os.listdir(r_directory_path)

# ファイルを読み込む
for item in file_list:
    if item == "SUMMARY.md":
        continue
    if item.endswith(".md"):
        r_file_path = os.path.join(r_directory_path, item)
# ファイルを読み込む
for item in file_list:
    if item.endswith(".md"):
        r_file_path = os.path.join(r_directory_path, item)
        try:
            with open(r_file_path, "r", encoding="utf-8") as rf:
                tmp_text = rf.read()
                # 1. <rt>...</rt> (読み仮名) と <rp>...</rp> (括弧など) を中身ごと消す
                clean_text = re.sub(r'<(rt|rp)>.*?</(rt|rp)>', '', tmp_text)
                # 2. 残った <ruby> と </ruby> タグ自体を消す
                clean_text = re.sub(r'</?ruby>', '', clean_text)

                # resultを書き込みディレクトリに書き込む
                w_file_path = os.path.join(w_directory_path, item)
                with open(w_file_path , "w", encoding="utf-8") as wf:
                    wf.write(clean_text)

                # print(clean_text)
                # 出力: これは漢字のテストです。
        except IOError as e:
            print(f"ファイル書き込みエラー: {e}")        
