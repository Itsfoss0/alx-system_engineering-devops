#!/usr/bin/env ruby
# Match pattern hbttn, hbtttn, hbttttn or hbtttttn
puts ARGV[0].scan(/hbt{2,5}n/).join