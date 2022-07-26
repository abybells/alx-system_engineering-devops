#!/usr/bin/env ruby
puts ARGV[0].match(/\[from:([^\]]*)\] \[to:([^\]]*)\] \[flags:([^\]]*)\]/).captures.join(',')
