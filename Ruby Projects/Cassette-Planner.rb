#Cassette Planer

puts "Put in the length on ONE side of your tape, in mins"
totalLength = gets.chomp.split(":") 
totalsecs = Integer(totalLength[0])*60 
puts "The length is #{totalsecs}s"
puts"Alright now input the length of your first song, in the format 'mins:seconds'"
i = 0 
for i != -1;
    if i == 0;
        next
    else;
        puts "Input the length of song number #{i} in 'mins:seconds'. Enter a blank to end"
    song = Integer(gets.chomp.split(":"))
    if song == ""
        break
    song = song[0]*60 + song[1]
    puts "The song length is #{song}s"
    case totalsecs - song
    when <0;
        puts "This song is too long to fully keep on the tape by #{totalsecs-song}, please choose another song"
        next
    when  =0:
        puts "This song perfectly ends at the end of the tape."
        next
    when >0;
        pass
    puts "Remaining time on tape is #{totalsecs}s"
    