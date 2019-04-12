import std.stdio;
import margeData;

void main()
{
  string fileName = readln;

  loadData(fileName[0 .. $ - 1]);
}
