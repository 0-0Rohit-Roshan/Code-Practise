cd Pictures/
pwd
img=$(sxiv *.jpg *.jpeg *.png -o)
echo $img
wal -i=$img -b=#000000

imgpath=/home/miku/Pictures/$img
cat ../Wallpaper.sh
echo "Your imgpath = $imgpath"
