thread1 = Thread.new do
    10.times { |i| puts "Thread 1: #{i}"; sleep(1) }
  end
  
  thread2 = Thread.new do
    5.times { |i| puts "Thread 2: #{i}"; sleep(1) }
  end
  
  thread1.join
  thread2.join
  