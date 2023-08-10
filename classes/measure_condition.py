class MeasureCondition(object):
    def __init__(self):
        self.measure_sid = None
        self.condition_string = ""
        self.certificate = ""

    def get_condition_string_old(self):
        # Set action code to empty string if it is empty
        if self.action_code is None:
            self.action_code = ""

        s = "condition:"
        s += self.condition_code + ","
        if self.certificate_type_code != "":
            s += "certificate:" + self.certificate_type_code + self.certificate_code + ","
        s += "action:" + self.action_code
        self.condition_string = s
        a = 1

    def get_condition_string(self):
        if self.certificate_type_code != "":
            self.certificate = self.certificate_type_code + self.certificate_code
            self.condition_string = self.certificate_type_code + self.certificate_code
