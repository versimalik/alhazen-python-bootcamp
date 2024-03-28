import platform

info = {}

os_details = platform.platform()
os_name = platform.system()
processor_name = platform.processor()
architectur_detail = platform.architecture()

info["Detail Sistem Operasi: "]= os_details
info["Nama sistem operasi: "] = os_name
info["Prosesor: "] = processor_name
info["Detail: "]= architectur_detail

for key, value in info.items():
    print(key, "=", value)