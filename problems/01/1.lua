--
--To run:
--  lua 1.lua
--
--Problem:
--    If we list all the natural numbers below 10 that are multiples of 3 or 5,
--    we get 3, 5, 6 and 9. The sum of these multiples is 23.
--
--    Find the sum of all the multiples of 3 or 5 below 1000.
--

function solve()
    sum = 0     up_to = 1e3-1
    for i=0,up_to,1 do
        if (i % 3 == 0) or (i % 5 == 0) then
            sum = sum + i
        end
    end
    return sum
end

start = os.clock()
result = solve()
finish = os.clock()

print(result, string.format("in %f seconds", finish - start))
