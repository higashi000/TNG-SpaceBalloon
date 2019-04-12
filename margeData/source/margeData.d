module margeData;

import std.stdio;
import std.conv;
import std.string;
import std.file;

void loadData(string sensorName) {
  int cntFileNum = 1;
  string outputFileName = sensorName ~ ".csv";
  bool isFirst = true;

  while (1) {
    string fileName = sensorName ~ to!string(cntFileNum) ~ ".txt";

    chdir("../outputData/");
    if (!exists(fileName))
      break;

    auto outputStr = to!string(cntFileNum) ~ ',' ~ readText(fileName);

    if (isFirst) {
      std.file.write(outputFileName, outputStr);
      isFirst = false;
    } else {
      append(outputFileName, outputStr);
    }

    cntFileNum++;
  }
}
