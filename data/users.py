import dataclasses


@dataclasses.dataclass
class Users:
    name: str
    surname: str
    email: str
    gender: str
    number: str
    day: int
    month: str
    year: int
    subject: str
    hobby: ()
    address: str
    state: str
    city: str


student = Users("Lev", "Savinkov", "www@test.ru", "Male", "9997776633", 10, "August", 1993, "Hindi",
                ("Sports", "Music"), "Thailand, Prachuap Khiri Khan, HuaHin, 18/19", "Rajasthan", "Jaipur")
