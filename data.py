


print("---materi 11 - file handling part 2---")
print("-------UPDATE json----------")
file_path_json = r"C:\Users\ThinkPad\OneDrive\Dokumen\python\__pycache__\materi.json"

with open(file_path_json, "r") as file_materi:
    #json.load() -> membaca isi file json
    data_materi = (file_materi)
    # akses data json dengan 'key' nya
    print(f"->: {data_materi["title"]}")
    print(f"->: {data_materi["total"]}")
    print(f"->: {data_materi["status_santri"]}")
    print(f"->: {data_materi["status_lulus"]}")
    print(f"->: {data_materi["pelajaran"]}")
    print(f"->: {data_materi["apa"]}")
    print(f"->: {data_materi["suroh"]}")

    # ekstrak semua data array of objects sunnah
    print("-" * 50)
    print("| no | nama suroh | ayat | turun |")
    print("-"* 50)
    