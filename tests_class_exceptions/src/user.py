class User:
    age: int
    working_status: str

    def __init__(self, age: int, working_status: str):
        self.age = age
        self.working_status = working_status
        if self.age < 62 and self.working_status == "retired":
            raise ValueError(f"age must be > 62 with status retired. Given : {self.age = } {self.working_status = }")

