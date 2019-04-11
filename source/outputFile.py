class OutputFile:
    def __init__(self, name = ''):
        self.name = name


    def output_file(self, _time, sensor_value):
        self.time = _time
        self.sensor_value = sensor_value

        file_name = self.name + str(self.time) + '.txt'

        with open(file_name, 'w') as f:
            f.write(str(self.sensor_value))
            f.flush()

        with open(file_name, 'r') as f:
            file_str = f.read()
            print(file_str)
