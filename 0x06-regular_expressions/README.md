![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
  > Regular expressions

![meme](https://intranet.alxswe.com/images/contents/sysadmin/concepts/29/regex_now_2_problems.jpg)

## Intro 
Regex is a powerful tool for text processing, and can be used in a variety of applications, including search and replace operations, data validation, and pattern matching. Through this project we  will learn the basics of regex syntax, how to write simple and complex regex patterns, and how to use regex in practical examples. The project is intended for those who have limited or no experience with regex and wish to learn more about this versatile tool, or those who have been using it for a while and would like to refresh their minds about some of the concepts

## Background context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the ```//```

```
itsfoss@itsfoss$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
itsfoss@itsfoss$
itsfoss@itsfoss$ ./example.rb 127.0.0.2
127.0.0.2
itfoss@itsfoss$ ./example.rb 127.0.0.1
127.0.0.1
itsfoss@itsfoss$ ./example.rb 127.0.0.a
```
## Resources
__Read or Watch__:
1. [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
2. [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
3. [Rubular is your best friend](https://rubular.com/)
3. [Use  a regular expression against a problem: now you have two problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
4. [Learn Regexs with simple interactive exercises](https://regexone.com/)
5. [Regex101](https://regex101.com/)
6. [Youtube](https://www.youtube.com/results?search_query=regex)
7. [Google](https://www.google.com/search?q=regular+expressions)

## Requirements
### General 
- Allowed editors ```vi```, ```vim```, ```emacs```
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A ```README```.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly ```#!/usr/bin/env ruby```
- All your regex must be built for the Oniguruma library

## Quiz
[Quizes](./quiz.md)