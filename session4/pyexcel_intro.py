import pyexcel

data = [
    {
        "name": "huy",
        "age":29,
    },
    {
        "name": "quang",
        "age": 19,
    },
    {
        "name":"duc",
        "age": 18,
    }
]
#2.save
pyexcel.save_as(records=data, dest_file_name="samle.xlsx")