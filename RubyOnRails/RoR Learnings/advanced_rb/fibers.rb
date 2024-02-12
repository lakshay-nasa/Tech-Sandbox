fiber1 = Fiber.new do
    5.times { |i| puts "Fiber 1: #{i}"; Fiber.yield }
  end
  
  fiber2 = Fiber.new do
    5.times { |i| puts "Fiber 2: #{i}"; Fiber.yield }
  end
  
  fiber1.resume
  fiber2.resume
  fiber1.resume until fiber1.alive? && fiber2.alive?
  fiber2.resume until fiber1.alive? && fiber2.alive?
  