class OutputFile:
    def __init__(self, name = ''):
        self.name = name

    def output_file(self, time, sensor_value):
        self.time = time
        self.sensor_value = sensor_value

        file_name = self.name + str(self.time) + '.txt'

        with open(file_name, 'w') as file:
            file.write(str(self.sensor_value))
