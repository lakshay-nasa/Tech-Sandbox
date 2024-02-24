text = "The quick brown fox jumps over the lazy dog."

match_result = text.match(/quick/)
puts match_result[0] 

scan_result = text.scan(/\b\w{3}\b/)
puts scan_result.inspect