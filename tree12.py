import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque


# =========================================================
# CLASS ต้นแบบข้อมูลต้นไม้
# =========================================================
class Tree:
    def __init__(
        self,
        treeId,
        commonName,
        scientificName,
        family,
        species,
        age,
        height,
        trunkDiameter,
        location,
        latitude,
        longitude,
        plantingDate,
        healthStatus,
        owner,
        note
    ):
        self.treeId = treeId
        self.commonName = commonName
        self.scientificName = scientificName
        self.family = family
        self.species = species
        self.age = age
        self.height = height
        self.trunkDiameter = trunkDiameter
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.plantingDate = plantingDate
        self.healthStatus = healthStatus
        self.owner = owner
        self.note = note

    def display_details(self):
        return (
            f"รหัส: {self.treeId}\n"
            f"ชื่อ: {self.commonName}\n"
            f"ชื่อวิทยาศาสตร์: {self.scientificName}\n"
            f"วงศ์: {self.family}\n"
            f"ชนิด: {self.species}\n"
            f"อายุ: {self.age} ปี\n"
            f"ความสูง: {self.height} เมตร\n"
            f"เส้นผ่านศูนย์กลางลำต้น: {self.trunkDiameter} ซม.\n"
            f"สถานที่: {self.location}\n"
            f"พิกัด: {self.latitude}, {self.longitude}\n"
            f"วันที่ปลูก: {self.plantingDate}\n"
            f"สุขภาพ: {self.healthStatus}\n"
            f"ผู้ดูแล: {self.owner}\n"
            f"หมายเหตุ: {self.note}"
        )


# =========================================================
# สร้างข้อมูลต้นไม้ 20 OBJECTS
# =========================================================
trees = [

    Tree("T001", "มะขาม", "Tamarindus indica",
         "Fabaceae", "ไม้ผล", 15, 8.5, 35,
         "สวนบ้าน", 12.61, 102.10, "2011-05-10",
         "แข็งแรง", "นายสมชาย", "ให้ผลผลิตดี"),

    Tree("T002", "ยางนา", "Dipterocarpus alatus",
         "Dipterocarpaceae", "ไม้ยืนต้น", 25, 15.0, 60,
         "ป่าชุมชน", 12.62, 102.11, "2001-06-15",
         "แข็งแรง", "ชุมชน", "ต้นใหญ่"),

    Tree("T003", "จามจุรี", "Samanea saman",
         "Fabaceae", "ไม้ให้ร่มเงา", 20, 12.0, 50,
         "โรงเรียน", 12.63, 102.12, "2006-04-20",
         "ต้องดูแล", "โรงเรียน", "ควรตัดแต่งกิ่ง"),

    Tree("T004", "มะม่วง", "Mangifera indica",
         "Anacardiaceae", "ไม้ผล", 5, 4.5, 20,
         "สวนหลังบ้าน", 12.64, 102.13, "2021-03-10",
         "แข็งแรง", "นายสมศักดิ์", "ออกผลทุกปี"),

    Tree("T005", "ขนุน", "Artocarpus heterophyllus",
         "Moraceae", "ไม้ผล", 8, 6.0, 28,
         "สวนบ้าน", 12.65, 102.14, "2018-05-01",
         "แข็งแรง", "นางสมพร", "ให้ผลผลิตดี"),

    Tree("T006", "ตะเคียน", "Hopea odorata",
         "Dipterocarpaceae", "ไม้ยืนต้น", 30, 18.0, 70,
         "ป่าชุมชน", 12.66, 102.15, "1996-07-12",
         "แข็งแรง", "ชุมชน", "ต้นสูงมาก"),

    Tree("T007", "ประดู่", "Pterocarpus macrocarpus",
         "Fabaceae", "ไม้ยืนต้น", 18, 10.0, 40,
         "สวนสาธารณะ", 12.67, 102.16, "2008-08-20",
         "แข็งแรง", "เทศบาล", "ให้ร่มเงา"),

    Tree("T008", "อินทนิล", "Lagerstroemia speciosa",
         "Lythraceae", "ไม้ดอก", 10, 7.0, 30,
         "โรงเรียน", 12.68, 102.17, "2016-01-15",
         "แข็งแรง", "โรงเรียน", "ดอกสวย"),

    Tree("T009", "หูกวาง", "Terminalia catappa",
         "Combretaceae", "ไม้ให้ร่มเงา", 12, 9.0, 32,
         "ริมถนน", 12.69, 102.18, "2014-02-10",
         "ต้องดูแล", "เทศบาล", "ควรตัดแต่งกิ่ง"),

    Tree("T010", "พะยูง", "Dalbergia cochinchinensis",
         "Fabaceae", "ไม้ยืนต้น", 35, 16.0, 65,
         "ป่าชุมชน", 12.70, 102.19, "1991-09-10",
         "แข็งแรง", "ชุมชน", "อนุรักษ์"),

    Tree("T011", "มะพร้าว", "Cocos nucifera",
         "Arecaceae", "ไม้ผล", 7, 8.0, 25,
         "สวน", 12.71, 102.20, "2019-05-12",
         "แข็งแรง", "นายประสิทธิ์", "มีผลผลิต"),

    Tree("T012", "กล้วย", "Musa acuminata",
         "Musaceae", "ไม้ผล", 2, 3.5, 10,
         "สวนหลังบ้าน", 12.72, 102.21, "2024-02-01",
         "แข็งแรง", "นางสาวมาลี", "โตเร็ว"),

    Tree("T013", "ไผ่", "Bambusa vulgaris",
         "Poaceae", "ไม้ไผ่", 4, 6.5, 15,
         "สวน", 12.73, 102.22, "2022-06-10",
         "แข็งแรง", "นายสมชาย", "ใช้ทำเครื่องจักสาน"),

    Tree("T014", "ลำไย", "Dimocarpus longan",
         "Sapindaceae", "ไม้ผล", 9, 7.5, 27,
         "สวนผลไม้", 12.74, 102.23, "2017-04-05",
         "แข็งแรง", "นายวิชัย", "ให้ผลผลิต"),

    Tree("T015", "ทุเรียน", "Durio zibethinus",
         "Malvaceae", "ไม้ผล", 12, 10.5, 38,
         "สวนผลไม้", 12.75, 102.24, "2014-05-15",
         "ต้องดูแล", "นายวิชัย", "ต้องให้น้ำสม่ำเสมอ"),

    Tree("T016", "เงาะ", "Nephelium lappaceum",
         "Sapindaceae", "ไม้ผล", 11, 8.0, 30,
         "สวนผลไม้", 12.76, 102.25, "2015-06-01",
         "แข็งแรง", "นายวิชัย", "ผลผลิตดี"),

    Tree("T017", "มังคุด", "Garcinia mangostana",
         "Clusiaceae", "ไม้ผล", 14, 9.0, 33,
         "สวนผลไม้", 12.77, 102.26, "2012-05-20",
         "แข็งแรง", "นายวิชัย", "ผลผลิตดี"),

    Tree("T018", "สน", "Pinus merkusii",
         "Pinaceae", "ไม้ยืนต้น", 22, 14.0, 45,
         "สวนสาธารณะ", 12.78, 102.27, "2004-01-10",
         "แข็งแรง", "เทศบาล", "ต้นสูง"),

    Tree("T019", "กฤษณา", "Aquilaria crassna",
         "Thymelaeaceae", "ไม้ยืนต้น", 16, 11.0, 40,
         "ป่าชุมชน", 12.79, 102.28, "2010-07-01",
         "ต้องดูแล", "ชุมชน", "ต้องดูแลเป็นพิเศษ"),

    Tree("T020", "ราชพฤกษ์", "Cassia fistula",
         "Fabaceae", "ไม้ดอก", 13, 9.5, 34,
         "สวนสาธารณะ", 12.80, 102.29, "2013-03-15",
         "แข็งแรง", "เทศบาล", "ดอกสีเหลือง")
]


# =========================================================
# QUEUE
# FIFO - เก็บคำขอเพิ่มข้อมูล
# =========================================================
tree_queue = deque()


# =========================================================
# STACK
# LIFO - เก็บประวัติการแก้ไขสำหรับ Undo
# =========================================================
undo_stack = []


# =========================================================
# GUI
# =========================================================
root = tk.Tk()
root.title("ระบบจัดการข้อมูลต้นไม้")
root.geometry("1250x700")


# =========================================================
# TITLE
# =========================================================
title = tk.Label(
    root,
    text="ระบบจัดการข้อมูลต้นไม้",
    font=("Tahoma", 24, "bold")
)
title.pack(pady=10)


subtitle = tk.Label(
    root,
    text="Tree Information Management System",
    font=("Tahoma", 12)
)
subtitle.pack()


# =========================================================
# SEARCH
# =========================================================
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(
    search_frame,
    text="ค้นหา:",
    font=("Tahoma", 12)
).pack(side=tk.LEFT)

search_entry = tk.Entry(
    search_frame,
    width=40,
    font=("Tahoma", 12)
)
search_entry.pack(side=tk.LEFT, padx=5)


# =========================================================
# TABLE
# =========================================================
columns = (
    "id",
    "name",
    "species",
    "age",
    "height",
    "location",
    "health"
)

tree_table = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=15
)

tree_table.heading("id", text="รหัส")
tree_table.heading("name", text="ชื่อต้นไม้")
tree_table.heading("species", text="ชนิด")
tree_table.heading("age", text="อายุ")
tree_table.heading("height", text="ความสูง")
tree_table.heading("location", text="สถานที่")
tree_table.heading("health", text="สุขภาพ")

tree_table.column("id", width=70)
tree_table.column("name", width=120)
tree_table.column("species", width=120)
tree_table.column("age", width=70)
tree_table.column("height", width=90)
tree_table.column("location", width=150)
tree_table.column("health", width=100)

tree_table.pack(pady=10)


# =========================================================
# แสดงข้อมูลในตาราง
# =========================================================
def display_trees(data=None):

    if data is None:
        data = trees

    # ล้างข้อมูลเดิม
    for item in tree_table.get_children():
        tree_table.delete(item)

    # เพิ่มข้อมูลใหม่
    for tree in data:

        tree_table.insert(
            "",
            tk.END,
            values=(
                tree.treeId,
                tree.commonName,
                tree.species,
                tree.age,
                tree.height,
                tree.location,
                tree.healthStatus
            )
        )


# =========================================================
# SEARCH FUNCTION
# Linear Search
# =========================================================
def search_tree():

    keyword = search_entry.get().lower().strip()

    if keyword == "":
        display_trees()
        return

    result = []

    # ตรวจสอบข้อมูลทีละรายการ
    for tree in trees:

        if (
            keyword in tree.treeId.lower()
            or keyword in tree.commonName.lower()
            or keyword in tree.species.lower()
            or keyword in tree.location.lower()
        ):
            result.append(tree)

    display_trees(result)

    if len(result) == 0:
        messagebox.showinfo(
            "ผลการค้นหา",
            "ไม่พบข้อมูลต้นไม้"
        )


# =========================================================
# SORT BY HEIGHT
# =========================================================
def sort_height():

    sorted_data = sorted(
        trees,
        key=lambda tree: tree.height
    )

    display_trees(sorted_data)


# =========================================================
# SORT BY AGE
# =========================================================
def sort_age():

    sorted_data = sorted(
        trees,
        key=lambda tree: tree.age
    )

    display_trees(sorted_data)


# =========================================================
# แสดงรายละเอียดต้นไม้
# =========================================================
def show_details():

    selected = tree_table.selection()

    if not selected:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาเลือกต้นไม้ก่อน"
        )
        return

    item = tree_table.item(selected[0])

    tree_id = item["values"][0]

    for tree in trees:

        if tree.treeId == tree_id:

            messagebox.showinfo(
                "รายละเอียดต้นไม้",
                tree.display_details()
            )

            break


# =========================================================
# QUEUE
# เพิ่มคำขอลง Queue
# =========================================================
def add_queue():

    selected = tree_table.selection()

    if not selected:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาเลือกต้นไม้"
        )
        return

    item = tree_table.item(selected[0])

    tree_id = item["values"][0]

    tree_queue.append(tree_id)

    messagebox.showinfo(
        "Queue",
        f"เพิ่ม {tree_id} เข้าคิวแล้ว\n"
        f"จำนวนใน Queue: {len(tree_queue)}"
    )


# =========================================================
# ประมวลผล Queue
# FIFO
# =========================================================
def process_queue():

    if len(tree_queue) == 0:

        messagebox.showinfo(
            "Queue",
            "ไม่มีข้อมูลใน Queue"
        )

        return

    tree_id = tree_queue.popleft()

    messagebox.showinfo(
        "Queue",
        f"กำลังประมวลผล: {tree_id}\n"
        f"หลักการ FIFO\n"
        f"เข้าก่อน → ออกก่อน"
    )


# =========================================================
# STACK / UNDO
# =========================================================
def undo():

    if len(undo_stack) == 0:

        messagebox.showinfo(
            "Undo",
            "ไม่มีประวัติให้ย้อนกลับ"
        )

        return

    action = undo_stack.pop()

    messagebox.showinfo(
        "Undo",
        f"ย้อนกลับการทำงาน:\n{action}\n\n"
        f"หลักการ Stack: LIFO"
    )


# =========================================================
# จำลองการแก้ไขข้อมูล
# =========================================================
def edit_demo():

    selected = tree_table.selection()

    if not selected:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาเลือกต้นไม้"
        )
        return

    item = tree_table.item(selected[0])

    tree_id = item["values"][0]

    # บันทึกลง Stack
    undo_stack.append(
        f"แก้ไขข้อมูลต้นไม้ {tree_id}"
    )

    messagebox.showinfo(
        "แก้ไขข้อมูล",
        f"จำลองการแก้ไข {tree_id}\n"
        f"การแก้ไขถูกเก็บไว้ใน Stack แล้ว"
    )


# =========================================================
# BUTTON FRAME
# =========================================================
button_frame = tk.Frame(root)
button_frame.pack(pady=10)


tk.Button(
    button_frame,
    text="ค้นหา",
    width=12,
    command=search_tree
).grid(row=0, column=0, padx=5)


tk.Button(
    button_frame,
    text="แสดงทั้งหมด",
    width=12,
    command=display_trees
).grid(row=0, column=1, padx=5)


tk.Button(
    button_frame,
    text="เรียงตามความสูง",
    width=15,
    command=sort_height
).grid(row=0, column=2, padx=5)


tk.Button(
    button_frame,
    text="เรียงตามอายุ",
    width=15,
    command=sort_age
).grid(row=0, column=3, padx=5)


tk.Button(
    button_frame,
    text="รายละเอียด",
    width=12,
    command=show_details
).grid(row=0, column=4, padx=5)

# =========================================================
# เริ่มต้นแสดงข้อมูล
# =========================================================
display_trees()


# =========================================================
# START PROGRAM
# =========================================================
root.mainloop()