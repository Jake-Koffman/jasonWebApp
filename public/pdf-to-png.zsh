
#!/bin/zsh
//COMMENT: needs to be removed to run USE IMAGEMAGICK to accomplish same task on Windows
FILES="$1"
cd "$FILES"
for FILE in *.pdf
do
  mkdir ${FILE%.*}
  sips -s format png $FILE --out "${FILE%.*}.png"
  mv $FILE ${FILE%.*}
  mv "${FILE%.*}.png" ${FILE%.*}
done
