#!/usr/bin/env ruby
# Match a 10-Digit phone number
puts ARGV[0].scan(/^[0-9]{10}$/).join
#/^/\d{10}$/ is also valid