addOne :: Int -> Int
addOne x = x + 1

-- ~equiv def addOne(x)

addTwoNumbers :: Int -> Int -> Int
-- addTwoNumbers :: Int -> (Int -> Int)
addTwoNumbers x y = x + y

-- ~equiv def addTwoNumbers(x, y)

mapList :: (a -> b) -> [a] -> [b]
mapList f [] = []
mapList f (x : xs) = f x : mapList f xs

-- ~equiv def mapList(func, xs)
