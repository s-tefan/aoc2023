digs s = [c | c <-s,  elem c "0123456789"]
firstlast s = [head s, last s]
main :: IO ()
main =  do
  indata <- readFile "input.txt"
  let ls = lines indata
  print (sum (fmap ((read::[Char] -> Int) . firstlast . digs) ls))
