#!/usr/bin/env ruby
# match a three lettered string That:
# Begins with 'h', ends with 'n'
puts ARGV[0].scan(/^h.n$/).join
# /Ah.n/z could have worke too