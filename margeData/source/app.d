import std.stdio;
import margeData;

void main()
{
  write("Please input sensor name >> ");
  string fileName = readln;

  loadData(fileName[0 .. $ - 1]);
}
