#!/bin/sh
# This scripts makes the gifs using ImageMagick
DATE=`date +%Y-%m-%d`
DATE='2017-06-26'
echo "Generating VAPOR images into gifs"
convert -delay 50 -loop 0 ./output/$DATE/D01_VAPOR_*.png ./output/D01_VAPOR.gif
convert -delay 50 -loop 0 ./output/$DATE/D02_VAPOR_*.png ./output/D02_VAPOR.gif
convert -delay 50 -loop 0 -resize 50% ./output/$DATE/D03_VAPOR_*.png ./output/D03_VAPOR-resized.gif

echo "Generating TEMP images into gifs"
convert -delay 50 -loop 0 ./output/$DATE/D01_TEMP_*.png ./output/D01_TEMP.gif
convert -delay 50 -loop 0 ./output/$DATE/D02_TEMP_*.png ./output/D02_TEMP.gif
convert -delay 50 -loop 0 -resize 50% ./output/$DATE/D03_TEMP_*.png ./output/D03_TEMP-resized.gif

echo "Generating WIND images into gifs"
convert -delay 50 -loop 0 ./output/$DATE/D01_WIND_*.png ./output/D01_WIND.gif
convert -delay 50 -loop 0 ./output/$DATE/D02_WIND_*.png ./output/D02_WIND.gif
convert -delay 50 -loop 0 -resize 50% ./output/$DATE/D03_WIND_*.png ./output/D03_WIND-resized.gif

echo "Generating SWDOWN images into gifs"
convert -delay 50 -loop 0 ./output/$DATE/D01_SWDOWN_*.png ./output/D01_SWDOWN.gif
convert -delay 50 -loop 0 ./output/$DATE/D02_SWDOWN_*.png ./output/D02_SWDOWN.gif
convert -delay 50 -loop 0 -resize 50% ./output/$DATE/D03_SWDOWN_*.png ./output/D03_SWDOWN-resized.gif

echo "Generating PRES images into gifs"
convert -delay 50 -loop 0 ./output/$DATE/D01_PRES_*.png ./output/D01_PRES.gif
convert -delay 50 -loop 0 ./output/$DATE/D02_PRES_*.png ./output/D02_PRES.gif
convert -delay 50 -loop 0 -resize 50% ./output/$DATE/D03_PRES_*.png ./output/D03_PRES-resized.gif

echo "Generating LH images into gifs"
convert -delay 50 -loop 0 ./output/$DATE/D01_LH_*.png ./output/D01_LH.gif
convert -delay 50 -loop 0 ./output/$DATE/D02_LH_*.png ./output/D02_LH.gif
convert -delay 50 -loop 0 -resize 50% ./output/$DATE/D03_LH_*.png ./output/D03_LH-resized.gif

echo "Generating HFX images into gifs"
convert -delay 50 -loop 0 ./output/$DATE/D01_HFX_*.png ./output/D01_HFX.gif
convert -delay 50 -loop 0 ./output/$DATE/D02_HFX_*.png ./output/D02_HFX.gif
convert -delay 50 -loop 0 -resize 50% ./output/$DATE/D03_HFX_*.png ./output/D03_HFX-resized.gif

echo "Generating RAIN images into gifs"
convert -delay 50 -loop 0 ./output/$DATE/D01_RAIN_*.png ./output/D01_RAIN.gif
convert -delay 50 -loop 0 ./output/$DATE/D02_RAIN_*.png ./output/D02_RAIN.gif
convert -delay 50 -loop 0 -resize 50% ./output/$DATE/D03_RAIN_*.png ./output/D03_RAIN-resized.gif