`std::IO importext
`std::Time importext
`std::Control importext /* Import the IO, Time and Control modules */
'file.txt' "r" IO::open IO::readall IO::close /*Open, read, and close the file 'file.txt' */
show /*Show the contents of the file*/
{ "spam" show /*Print spam*/
  1 Time::sleep /*Pause for 1 second*/
} `spam define
{ spam } Control::forever
