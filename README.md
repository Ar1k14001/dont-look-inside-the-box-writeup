# dont-look-inside-the-box-writeup
[noxCTF:dont look inside the box] Just some file fixing, sql and hash.

![1](https://user-images.githubusercontent.com/41908916/45264352-fc176400-b443-11e8-9d6c-d0833c8e31ba.JPG)

after entering the dropbox and downloading there is "hashTable" file

![2](https://user-images.githubusercontent.com/41908916/45264372-46004a00-b444-11e8-8448-9a90dbf494b2.JPG)

the file wont open so i checked it in hex editor(hxd) and saw this:

![3](https://user-images.githubusercontent.com/41908916/45264407-b14a1c00-b444-11e8-9e53-ff2f42556f0a.JPG)

sqlite format 3 signature as ascii is "SQLite format 3." and not "sqlite format 3." so i fixed it.

i opend it in DB Browser for SQLite to see what inside it and saw 3 tables: Hashs(XorMe), Plains(XorMe) and Flags(values).

![4](https://user-images.githubusercontent.com/41908916/45264459-667cd400-b445-11e8-926d-d56634290131.JPG)

in Hashs and Plains there were only one value in each table and both were "XorMe": 
* Hashs - 6c7a634e058812fb329863ff42fec497
* Plains - JohnE

in Flags table there were 16777216 values in the form of noxCTF{XXXXXXX}:

![5](https://user-images.githubusercontent.com/41908916/45264493-1c482280-b446-11e8-81ad-a294695c80cc.JPG)

in a python program I did xor to Hashs value and Plains after convering Plains to md5 and hex and got new hash
i run in for loop on every value from Flags table, encrypted it as md5 and compared it with the new xored hash. (the code i in cyber.py)
the answer is noxCTF{h4shUL1t3}
