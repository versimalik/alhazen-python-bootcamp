def fullname(**kwargs):
    result = kwargs.values()
    print(" ".join(result))

fullname(
    fname = "Ahmad",
    mname = "Kurniawan", 
    lname = "Budi"
)

fullname(
    fname = "Budi",
    lname = "Santoso"
)

fullname(
    name = "Budi",
)