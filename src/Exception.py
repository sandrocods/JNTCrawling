class error_no_billCode(Exception):
    def __init__(self):
        super().__init__("Error: No billCode")


class connection_error(Exception):
    def __init__(self):
        super().__init__("Error: Connection Error or timeout")


class no_data_found(Exception):
    def __init__(self):
        super().__init__("Error: No Data")


class parameter_error(Exception):
    def __init__(self):
        super().__init__("Error: Parameter Error")
