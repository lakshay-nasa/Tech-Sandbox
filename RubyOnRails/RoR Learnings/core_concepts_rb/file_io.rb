File.open("example.txt", "w") do |file|
    file.puts "Hello, World!"
  end
  
  File.open("example.txt", "r") do |file|
    puts file.read
  end  