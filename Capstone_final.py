import statistics
table_header = ["nama", "kota", "umur", "gender", "status_menikah", "diagnosa", "lama_rawat"]
table_1 = {
        "1":{"nama":"Budi",
           "kota":"Bandung",
           "umur":28,
           "gender":"laki-laki",
           "status_menikah":True,
           "diagnosa":"Jantung",
           "lama_rawat":4},
        "2":{"nama":"Cica",
           "kota":"Sumedang",
           "umur":21,
           "gender":"perempuan",
           "status_menikah":False,
           "diagnosa":"Lambung",
           "lama_rawat":2},
        "3":{"nama":"Aldi",
           "kota":"Cirebon",
           "umur":35,
           "gender":"laki-laki",
           "status_menikah":True,
           "diagnosa":"Tipes",
           "lama_rawat":5},
        "4":{"nama":"Santoso",
           "kota":"Cirebon",
           "umur":35,
           "gender":"laki-laki",
           "status_menikah":True,
           "diagnosa":"DBD",
           "lama_rawat":5},
        "5":{"nama":"Elsa",
           "kota":"Bogor",
           "umur":27,
           "gender":"perempuan",
           "status_menikah":False,
           "diagnosa":"Diabetes",
           "lama_rawat":3},
         "6":{"nama":"Ganjar",
           "kota":"Palembang",
           "umur":15,
           "gender":"laki-laki",
           "status_menikah":False,
           "diagnosa":"DBD",
           "lama_rawat":4},
         "7":{"nama":"Hasbi",
           "kota":"Bandung",
           "umur":12,
           "gender":"laki-laki",
           "status_menikah":False,
           "diagnosa":"Ginjal",
           "lama_rawat":3},
         "8":{"nama":"Cline",
           "kota":"Bandung",
           "umur":16,
           "gender":"perempuan",
           "status_menikah":False,
           "diagnosa":"Ginjal",
           "lama_rawat":3},
         "9":{"nama":"Budiman",
           "kota":"Bandung",
           "umur":50,
           "gender":"laki-laki",
           "status_menikah":True,
           "diagnosa":"Jantung",
           "lama_rawat":6},
         "10":{"nama":"Siti",
           "kota":"Bandung",
           "umur":17,
           "gender":"perempuan",
           "status_menikah":False,
           "diagnosa":"DBD",
           "lama_rawat":6},
         }

def main():
    main_menu()

def print_data_table(table: dict, headers:list):
    #Print pemisah menu sebelumnya
    for _ in range(122):
      print("-", end="")
    print("")
    #print header dengan spacing: ID rata kiri spacing 5, header rata kiri spacing 10.
    print(f"{"ID":<3}|"+" ".join(f"{h:^15}|" for h in headers))
    #print dalam data.
    for row_key, row_data in table.items(): # Iterasi dictionary, dapatkan row_key dan row data.
        #Membuat list 'row_values' yang berisikan value dari row_data 
        row_values = [str(row_data.get(h," ")) for h in headers]
        #Menampilkan Row_Key dan Row_Values. Merapihkannya dengan menggunakan f(string)
        print(f"{row_key:<3}|" + " ".join(f"{row_value:^15}|" for row_value in row_values))
    for _ in range(122):
      print("-", end="")
    print("")

def print_individual_data(table: dict, headers: list, id: str):
    #Print pemisah menu sebelumnya
    for _ in range(122):
      print("-", end="")
    print("")
    #print header dengan spacing: ID rata kiri spacing 5, header rata kiri spacing 10.
    print(f"{"ID":<3}|"+" ".join(f"{h:^15}|" for h in headers))

    id_values = table[id]
    row_values = [str(id_values.get(h," ")) for h in headers]
    print(f"{id:<3}|" + " ".join(f"{row_value:^15}|" for row_value in row_values))
    #print pemisah table
    for _ in range(122):
      print("-", end="")
    print("")

def print_modified_value(table: dict, headers:list, modified_id: list):
    #Print pemisah tabel
    for _ in range(122):
      print("-", end="")
    print("")
    #print header dengan spacing: ID rata kiri spacing 5, header rata kiri spacing 10.
    print(f"{"ID":<3}|"+" ".join(f"{h:^15}|" for h in headers))
    
    #Print baris data tabel
    for id in modified_id: # Iterasi list id
        #Membuat list 'row_values' yang berisikan value dari row_data 
        row_values = [str(table[id].get(h," ")) for h in headers]
        #Menampilkan Row_Key dan Row_Values. Merapihkannya dengan menggunakan spacing
        print(f"{id:<3}|" + " ".join(f"{row_value:^15}|" for row_value in row_values))
    #print pemisah tabel
    for _ in range(122):
      print("-", end="")
    print("")

def get_int(to_print: str):
   #Memaksa user untuk memasukan data integer
   while True:
      data = input(f"{to_print}")
      if data.isnumeric():
         return int(data)
      else:
         print("Tolong masukan data yang valid.")

def get_status_menikah(to_print: str):
   #Memaksa user untuk memasukan data sudah/belum
   while True:
      data = input(f"{to_print}").lower()
      if data == "sudah":
         return True
      elif data == "belum":
         return False
      else:
         "Tolong masukan data yang valid: sudah/belum"

def get_yes_no(to_print: str):
   """Memaksa user untuk memasukan data ya/tidak"""
   while True:
      data = input(f"{to_print}").lower()
      if data == "ya" or data == "y":
         return True
      elif data == "tidak" or data == "t":
         return False
      else:
         print("Tolong masukan data yang valid: ya/tidak")

def get_gender(to_print: str):
   """Memaksa user untuk memasukan data laki-laki/perempuan"""
   while True:
      pool = ["laki-laki", "perempuan"]
      data = input(f"{to_print}").lower()
      if data in pool:
         return data
      else:
         print("Tolong tmasukan data yang valid: laki-laki/perempuan")

def get_kolom(to_print:str, header: list,):
   """Memaksa user untuk memasukan data kolom yang valid"""
   while True:
      data = input(f"{to_print}").lower()
      if data in header:
         return data
      else:
         print("Tolong masukan data kolom yang valid")

def check_id_eksisting(table: dict):
   ''''Fungsi untuk mengecek apakah id yang di input oleh user ada dalam list id eksiting.
   Input:
   tabele dengan id (primary key) yang akan dicek.

   Output:
   Jika ID yang akan dicek ada dalam primary key table. Return nilai boolean True dan id yang akan dicek.
   Jka ID yang akan dicek tidak ada dalam primary key table. Return nilai boolean False dan id yang akan dicek.'''
   id_eksisting = [h for h in table ] # Membuat list id eksiting
   id_to_check = input("Silahkan masukan ID pasien: ")
   if id_to_check in id_eksisting:
      return True, id_to_check
   else:
      return False, id_to_check

def get_ascending():
   """Memaksa user untuk mamasukan data ascending/descending"""
   while True:
      data = input("Urutkan data secara ascending/descending? ")
      if data == "descending" or data == "d":
         return True
      elif data == "ascending" or data == "a":
         return False
      else:
         print("Tolong masukan data yang valid: a/d")

def sorting_id(table: dict, sorted_by: str, tipe: bool):
   """Menyortir data kolom secara ascending/descending
   Input: 1. Table: Table yang akan disortir
   2. sorted_by: Kolom yang akan disortir.
   3. tipe: Ascending/Descending
   Output: 1. List id yang telah disortir
   """
   #Mempersiapkan dictionary yang akan disroting
   to_sort_dict = {}
   for key, data in table.items():
      to_sort_dict[key] = data[sorted_by]
   #Menyortir dictionary
   sorted_dict = dict(sorted(to_sort_dict.items(), key= lambda item: item[1], reverse= tipe))

   key_after_sorted = [i for i in sorted_dict]
   return key_after_sorted

def filter_umur(table: dict, umur=18):
   """
   Fungsi ini mengfilter/menampilkan pasien yang umurnya lebih dari 18 tahun.
   Input: 
   1. Table:  yang datanya akan difilter.
   2. Umur: Default 18 tahun, namun bisa diubah sesuai keperluan user
   Output:
   1. List ID pasien yang umurnya sesuai dengan kriteri di atas.
   """
   # Menyiapkan list dictionary yang akan difilter
   to_filter = []
   for key, data in table.items():
      temp_dict = {"ID": key, "umur": data["umur"]}
      to_filter.append(temp_dict)
   filtered_dict = list(filter(lambda p: p["umur"] > umur, to_filter))
   # Ekstrak id dari dictionary yang sudah difilter
   filtered_id = [i["ID"] for i in filtered_dict]
   return(filtered_id)
    
def main_menu():
    while True:
      print("-------------------------------------------\nSelamat datang! \nProgram 'Data Pasien rumah sakit'")
      print("Anda dapat berinteraksi dengan 'Data Pasien Rumah Sakit'. Silahkan pilih salah satu menu berikut:")
      menus = ["1. Membaca data pasien rumah sakit",
               "2. Mengubah data pasien rumah sakit",
               "3. Menambah data pasien rumah sakit",
               "4. Menghapus data pasien rumah sakit",
               "5. Quit"
               ]
      for menu in menus:
         print(menu)
      choose = input("Silahkan pilih menu 1-5: ")
      if choose == "1":
         menu_1()
      elif choose == "2":
         menu_2()
      elif choose == "3": 
         menu_3()
      elif choose == "4":
         menu_4()
      elif choose == "5":
         print("Bye!")
         break
      else:
         print("----------------------------------------\nPilihan menu tidak valid. Silahkan input angka 1-5.")

def menu_1():
   while True:
      print("--------------------------------------------\nMembaca data pasien")
      print("1. Tampilkan data pasien.")
      print("2. Tampilkan data individu pasien.")
      print("3. Tampilkan data pasien yang telah diurutkan.")
      print("4. Tampilkan data kota pasien.")
      print("5. Tampilkan statistik umur pasien.")
      print("6. Tampilkan statistik lama rawat.")
      print("7. Tampilkan pasien dewasa (Umur > 17)")
      print("8. Kembali ke menu utama.")
      choose = input("Please inter number: ")
      if choose == "1":
         if bool(table_1): #Cek apakah table_1 memiliki data.
            print_data_table(table_1, table_header)
         else:
            print("----------------------------------------\nTidak ada data.")
      elif choose == "2":
         if bool(table_1): #Cek apakah table_1 memiliki data.
            check_bool, id_to_check = check_id_eksisting(table_1)
            if check_bool: #Cek jika data yang diinput user terdapat pada table
               print_individual_data(table_1, table_header, id_to_check) 
            else:
               print("----------------------------------------\nTidak ada data.")
         else:
            print("----------------------------------------\nTidak ada data.")
      elif choose == "3":
         kolom = get_kolom("Masukan data kolom yang akan diurutkan: ", table_header)
         tipe = get_ascending()
         sorted_id = sorting_id(table_1, kolom, tipe)
         print_modified_value(table_1, table_header, sorted_id)
         print(f"--------------------------------------------\nBerhasil mengurutkan data berdasarkan {kolom}.")
      elif choose == "4":
         list_kota = []
         for data in table_1.values():
            list_kota.append(data["kota"])
         set_kota = set(list_kota)
         print("----------------------------------------\nData kota pasien:")
         print(f"Jumlah kota asal pasien adalah sebanyak: {len(set_kota)}\nKota asal pasein: "+", ".join(set_kota))
      elif choose == "5":
         list_umur = []
         for data in table_1.values():
            list_umur.append(data["umur"])
         mean_umur = statistics.mean(list_umur)
         median_umur = statistics.median(list_umur)
         stdv_umur = statistics.stdev(list_umur)
         var_umur = statistics.variance(list_umur)
         max_umur = max(list_umur)
         min_umur = min(list_umur)
         print("----------------------------------------\nData statistik umur.")
         print(f"1. Mean Umur: {mean_umur}\n2. Median Umur: {median_umur}\n3. Standard Deviasi Umur: {stdv_umur:.4}")
         print(f"4. Variance Umur: {var_umur:.4}\n5. Max Umur: {max_umur}\n6. Min Umur: {min_umur}")
      elif choose == "6":
         list_rawat = []
         for data in table_1.values():
            list_rawat.append(data["lama_rawat"])
         mean_rawat = statistics.mean(list_rawat)
         median_rawat = statistics.median(list_rawat)
         stdv_rawat = statistics.stdev(list_rawat)
         var_rawat = statistics.variance(list_rawat)
         max_rawat = max(list_rawat)
         min_rawat = min(list_rawat)
         print("----------------------------------------\nData statistik lama_rawat.")
         print(f"1. Mean lama rawat: {mean_rawat}\n2. Median lama rawat: {median_rawat}\n3. Standard Deviasi lama rawat: {stdv_rawat:.4}")
         print(f"4. Variance lama rawat: {var_rawat:.4}\n5. Max lama rawat: {max_rawat}\n6. Min lama rawat: {min_rawat}")
      elif choose == "7":
         filtered_id = filter_umur(table_1)
         print_modified_value(table_1, table_header, filtered_id)
      elif choose == "8":
         break
      else:
         print("----------------------------------------\nPilihan menu tidak valid. Silahkan input angka 1-4.")

def menu_2():
   while True:
      print("--------------------------------------------\nMengubah data data pasien rumah sakit.")
      print("1. Ubah data pasien rumah sakit")
      print("2. Kembali ke main menu")
      inputan = input("Silahkan pilih menu 1-2: ")
      if inputan == "1":
         id_bool, id_to_check = check_id_eksisting(table_1)
         if id_bool:
            print_individual_data(table_1, table_header, id_to_check)
            continue_update = get_yes_no(f"Apakah anda ingin mengupdate data pasien {table_1[id_to_check]['nama']}? ")
            if continue_update:
               kolom_to_update = get_kolom("Masukan nama kolom data yang aakan diupdate: ", table_header)
               new_value = input(f"Masukan data {kolom_to_update} baru: ")
               confirmation = get_yes_no(f"Apakah anda yakin ingin menupdate data {kolom_to_update} {table_1[id_to_check]["nama"]} menjadi {new_value}? ")
               if confirmation:
                  table_1[id_to_check][kolom_to_update] = new_value
                  print("----------------------------------------\nData berhasil diperbaharui")
         else:
            print("----------------------------------------\nID tidak tersedia.")
      elif inputan == "2":
         break
      else:
         print("----------------------------------------\nPilihan menu tidak valid. Silahkan input angka 1-2.")

def menu_3():
   while True:
      print("--------------------------------------------\nMenambah data pasien rumah sakit.")
      print("1. Tambah data pasien rumah sakit")
      print("2. Kembali ke main menu")
      inputan = input("Silahkan pilih menu 1-2: ")
      if inputan == "1":
         id_bool, new_id = check_id_eksisting(table_1)
         if id_bool:
            print("----------------------------------------\nData sudah ada")
         else:
            new_nama = input("Silahkan masukan nama pasien baru: ")
            new_kota = input("Silahkan masukan kota asal pasien baru: ")
            new_umur = get_int("Silahkan masukan umur pasien baru: ")
            new_gender = get_gender("Silahkan masukan data gender pasion baru (laki-laki/perempuan): ")
            new_status_menikah = get_status_menikah("Silahkan masukan status pernikahan pasien baru (sudah/belum): ")
            new_diagnosa = input("Silahkan masukan diagnosa pasien baru: ")
            new_lama_rawat = get_int("Silahkan masukan lama pasien dirawat dalam hari: ")
            yes_no = get_yes_no("Anda yakin ingin menyimpan data? ya/tidak: ")
            if yes_no:
               table_1[new_id] = {"nama": new_nama,
                              "kota":new_kota,
                              "umur":new_umur,
                              "gender":new_gender,
                              "status_menikah":new_status_menikah,
                              "diagnosa":new_diagnosa,
                              "lama_rawat":new_lama_rawat}
               print("----------------------------------------\nData berhasil disimpan")

      elif inputan == "2":
         break
      else:
         print("----------------------------------------\nPilihan menu tidak valid. Silahkan input angka 1-2.")


def menu_4():
   while True:
      print("--------------------------------------------\nMenghapus data pasien rumah sakit.")
      print("1. Hapus satu data pasien rumah sakit")
      print("2. Hapus seluruh data pasien rumah sakit")
      print("3. Kembali ke menu utama")
      inputan = input("Silahakn pilih menu 1-3: ")
      if inputan == "1":
         id_bool, id_to_check = check_id_eksisting(table_1)
         if id_bool:
            continue_delete = get_yes_no(f"Apakah anda yakin akan menghapus data {table_1[id_to_check]["nama"]} dari database? ")
            if continue_delete:
               table_1.pop(id_to_check)
               print(f"----------------------------------------\nData berhasil dihapus")
         else:
            print("----------------------------------------\nData yang anda cari tidak tersedia.")
      elif inputan == "2":
         if get_yes_no("Apakah anda yakin ingin menhapus emua data pasien rumah sakit? "):
            table_1.clear()
            print("--------------------------------------------\nSeluruh data pasien berhasil dihapus.")
      elif inputan == "3":
         break
      else:
         print("----------------------------------------\nPilihan menu tidak valid. Silahkan input angka 1-3.")

main()