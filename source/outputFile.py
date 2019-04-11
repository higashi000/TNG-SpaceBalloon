import os
class OutputFile:
    def __init__(self, name = ''):
        self.name = name


    def output_file(self, value_time, sensor_value):
        os.chdir("../outputDate")
        self.time = value_time
        self.sensor_value = sensor_value

        file_name = self.name + str(value_time) + '.txt'

        print(file_name)
        with open(file_name, 'w') as f:
            f.write(str(self.sensor_value))
            f.flush()

        with open(file_name, 'r') as f:
            file_str = f.read()
            print(file_str)
