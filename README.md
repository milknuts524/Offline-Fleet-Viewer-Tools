# Offline-Fleet-Viewer-Tools
Tools for Offline Fleet Viewer

艦これの艦隊データを、Offline Fleet Viewer（提督手帳）で利用できる JSON ファイルへ変換するためのツールです。

This tool converts Kancolle game data into JSON files that can be imported into Offline Fleet Viewer.

---

## Disclaimer / 免責事項

This project is an unofficial fan-made tool.

"Kantai Collection -KanColle-" and all related copyrights, trademarks, and intellectual property belong to their respective owners.

This project is not affiliated with DMM GAMES, C2機関, KADOKAWA, or any related organizations.

This tool is provided free of charge and is not intended for commercial use.

---

本ツールは個人が趣味として開発した非公式ツールです。

「艦隊これくしょん -艦これ-」に関する著作権、商標権その他の権利は各権利者に帰属します。

本ツールは DMM GAMES 様、C2機関様、KADOKAWA 様および関係各社とは一切関係ありません。

また、本ツールは無料で公開されており、営利目的ではありません。

---

## Requirements / 必要なもの

- Python 3
- port.txt
- start2.txt
- slotitem.txt
- require_info.txt
- payitem.txt

---

## Usage / 使用方法

Place the following files in the same folder:

以下のファイルを同じフォルダに配置してください。

port.txt
start2.txt
slotitem.txt
require_info.txt
payitem.txt
convert_kancolle.py


Run the script.

スクリプトを実行します。

python3 convert_kancolle.py


Output Files / 出力ファイル

The script generates the following files.

以下のファイルが作成されます。

ships.json
items.json
materials.json
useitems.json
payitems.json

These JSON files can be imported into Offline Fleet Viewer.

これらのJSONファイルを、Offline Fleet Viewer（提督手帳）で読み込めます。

Converted Data / 変換される内容
ships.json
Ship name / 艦名
Ship type / 艦種
Level / レベル
Sort number / 図鑑順
items.json
Equipment name / 装備名
Equipment category / 装備カテゴリ
Improvement level / 改修値
Type order / 装備種別順
materials.json
Fuel / 燃料
Ammo / 弾薬
Steel / 鋼材
Bauxite / ボーキサイト
Instant construction materials / 高速建造材
Instant repair materials / 高速修復材
Development materials / 開発資材
Improvement materials / 改修資材
Medals / 勲章
Furniture coins / 家具コイン
useitems.json
Special items / 特殊アイテム
Blueprint-related items / 設計図関連
Catapults and other owned items / カタパルト等の保有アイテム
payitems.json
Paid items / 課金アイテム
Notes / 注意事項

This tool is intended only for personal use with data obtained by the user.

本ツールは、利用者自身が取得したデータを個人利用の範囲で変換することを目的としています。

This tool does not connect to Kancolle game servers.

本ツールには艦これサーバーへ通信する機能はありません。

This tool does not automate gameplay.

本ツールはゲーム操作の自動化を行いません。

Generated JSON files are intended for local use only.

生成されたJSONファイルは、ローカル環境での利用を想定しています。

The developer is not responsible for any damage or trouble caused by using this tool.

本ツールの利用により生じたいかなる損害やトラブルについても、開発者は責任を負いません。
