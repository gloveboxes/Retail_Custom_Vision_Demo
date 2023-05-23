count=0
while [ 1 ]
do
  curl -s -X POST http://dgnuc/image -F imageData=@fruit1.jpg | jq .
  curl -s -X POST http://dgnuc/image -F imageData=@fruit2.jpg | jq .
  curl -s -X POST http://dgnuc/image -F imageData=@fruit3.jpg | jq .
  ((count++))
  echo $count
done
