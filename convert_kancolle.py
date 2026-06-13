import json

def load_svdata(path):
    text = open(path, "r", encoding="utf-8").read().strip()

    if text.startswith("svdata="):
        text = text[len("svdata="):]

    start = text.find('"api_result"')
    if start >= 0:
        text = text[start:]

    if not text.startswith("{"):
        text = "{" + text

    if not text.endswith("}"):
        text = text + "}"

    return json.loads(text)

port = load_svdata("port.txt")
start2 = load_svdata("start2.txt")
slotitem = load_svdata("slotitem.txt")
require_info = load_svdata("require_info.txt")
payitem = load_svdata("payitem.txt")

owned_ships = port["api_data"]["api_ship"]
master_ships = start2["api_data"]["api_mst_ship"]

ship_master_by_id = {
    ship["api_id"]: ship
    for ship in master_ships
}

stype_names = {
    stype["api_id"]: stype["api_name"]
    for stype in start2["api_data"]["api_mst_stype"]
}

result = []

for ship in owned_ships:
    ship_id = ship["api_ship_id"]
    master = ship_master_by_id.get(ship_id)

    if master is None:
        name = f"unknown_{ship_id}"
        ship_type = "不明"
    else:
        name = master.get("api_name", f"unknown_{ship_id}")

        stype_id = master.get("api_stype")
        ship_type = stype_names.get(
            stype_id,
            f"艦種{stype_id}"
        )

    result.append({
        "name": name,
        "level": ship["api_lv"],
        "shipType": ship_type,
        "sortNumber": master.get("api_sortno", 9999) if master else 9999
    })

result.sort(key=lambda x: x["level"], reverse=True)

with open("ships.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"ships.json を作成しました: {len(result)}隻")

material_names = {
    1: "燃料",
    2: "弾薬",
    3: "鋼材",
    4: "ボーキサイト",
    5: "高速建造材",
    6: "高速修復材",
    7: "開発資材",
    8: "改修資材"
}

materials = []

for mat in port["api_data"]["api_material"]:
    mat_id = mat["api_id"]

    materials.append({
        "name": material_names.get(mat_id, f"資材{mat_id}"),
        "amount": mat["api_value"]
    })

basic = port["api_data"]["api_basic"]

materials.append({
    "name": "勲章",
    "amount": basic.get("api_medals", 0)
})

materials.append({
    "name": "家具コイン",
    "amount": basic.get("api_fcoin", 0)
})

with open("materials.json", "w", encoding="utf-8") as f:
    json.dump(materials, f, ensure_ascii=False, indent=2)

print("materials.json を作成しました")

equip_types = start2["api_data"]["api_mst_slotitem_equiptype"]

item_type_names = {
    t["api_id"]: t["api_name"]
    for t in equip_types
}

slotitem = load_svdata("slotitem.txt")
owned_items = slotitem["api_data"]["api_slot_item"]
master_items = start2["api_data"]["api_mst_slotitem"]

item_master_by_id = {
    item["api_id"]: item
    for item in master_items
}

items_result = []

for item in owned_items:
    item_id = item["api_slotitem_id"]
    master = item_master_by_id.get(item_id)

    if master is None:
        name = f"unknown_item_{item_id}"
        category = "不明"
    else:
        name = master.get("api_name", f"unknown_item_{item_id}")
        type_id = master.get("api_type", [0,0,0])[2]

    category = item_type_names.get(
        type_id,
        f"種別{type_id}"
    )

    items_result.append({
        "name": name,
        "category": category,
        "improvement": item.get("api_level", 0),
        "typeOrder": type_id
    })

with open("items.json", "w", encoding="utf-8") as f:
    json.dump(items_result, f, ensure_ascii=False, indent=2)

master_useitems = start2["api_data"]["api_mst_useitem"]

useitem_master_by_id = {
    item["api_id"]: item
    for item in master_useitems
}

useitems_result = []

for item in require_info["api_data"]["api_useitem"]:
    item_id = item["api_id"]
    master = useitem_master_by_id.get(item_id)

    if master is None:
        name = f"useitem_{item_id}"
    else:
        name = master.get("api_name", f"useitem_{item_id}")

    useitems_result.append({
        "name": name,
        "amount": item["api_count"]
    })

with open("useitems.json", "w", encoding="utf-8") as f:
    json.dump(useitems_result, f, ensure_ascii=False, indent=2)

print(f"useitems.json を作成しました: {len(useitems_result)}個")

master_payitems = start2["api_data"]["api_mst_payitem"]

payitem_master_by_id = {
    int(item["api_id"]): item
    for item in master_payitems
}

payitems_result = []

for item in payitem["api_data"]:
    item_id = int(item["api_payitem_id"])

    master = payitem_master_by_id.get(item_id)

    if master is None:
        name = item.get("api_name", f"payitem_{item_id}")
    else:
        name = master.get("api_name", item.get("api_name", f"payitem_{item_id}"))

    payitems_result.append({
        "name": name,
        "amount": item["api_count"]
    })

with open("payitems.json", "w", encoding="utf-8") as f:
    json.dump(payitems_result, f, ensure_ascii=False, indent=2)

print(f"payitems.json を作成しました: {len(payitems_result)}個")

print(f"items.json を作成しました: {len(items_result)}個")