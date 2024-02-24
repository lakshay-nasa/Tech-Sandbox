[1, 2, 3].each do |num|
    puts num * 2
  end
  
  multiply_by_2 = Proc.new do |num|
    num * 2
  end
  
  puts multiply_by_2.call(3)