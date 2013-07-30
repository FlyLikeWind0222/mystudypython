import urllib
file = urllib.urlopen("https://raw.github.com/huyinghuan/MyMath/master/T1.java");
java = file.read();
print java
