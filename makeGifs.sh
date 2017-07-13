#!/bin/sh
# This scripts makes the gifs using ImageMagick
DATE=`date +%Y-%m-%d`

echo "Generating VAPOR images into gifs"
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D01_VAPOR_*.png /home/edson/d-wrf-op/py-output/D01_VAPOR-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D02_VAPOR_*.png /home/edson/d-wrf-op/py-output/D02_VAPOR-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D03_VAPOR_*.png /home/edson/d-wrf-op/py-output/D03_VAPOR-resized.gif

echo "Generating TEMP images into gifs"
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D01_TEMP_*.png /home/edson/d-wrf-op/py-output/D01_TEMP-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D02_TEMP_*.png /home/edson/d-wrf-op/py-output/D02_TEMP-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D03_TEMP_*.png /home/edson/d-wrf-op/py-output/D03_TEMP-resized.gif

echo "Generating WIND images into gifs"
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D01_WIND_*.png /home/edson/d-wrf-op/py-output/D01_WIND-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D02_WIND_*.png /home/edson/d-wrf-op/py-output/D02_WIND-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D03_WIND_*.png /home/edson/d-wrf-op/py-output/D03_WIND-resized.gif

echo "Generating SWDOWN images into gifs"
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D01_SWDOWN_*.png /home/edson/d-wrf-op/py-output/D01_SWDOWN-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D02_SWDOWN_*.png /home/edson/d-wrf-op/py-output/D02_SWDOWN-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D03_SWDOWN_*.png /home/edson/d-wrf-op/py-output/D03_SWDOWN-resized.gif

echo "Generating PRES images into gifs"
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D01_PRES_*.png /home/edson/d-wrf-op/py-output/D01_PRES-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D02_PRES_*.png /home/edson/d-wrf-op/py-output/D02_PRES-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D03_PRES_*.png /home/edson/d-wrf-op/py-output/D03_PRES-resized.gif

echo "Generating LH images into gifs"
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D01_LH_*.png /home/edson/d-wrf-op/py-output/D01_LH-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D02_LH_*.png /home/edson/d-wrf-op/py-output/D02_LH-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D03_LH_*.png /home/edson/d-wrf-op/py-output/D03_LH-resized.gif

echo "Generating HFX images into gifs"
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D01_HFX_*.png /home/edson/d-wrf-op/py-output/D01_HFX-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D02_HFX_*.png /home/edson/d-wrf-op/py-output/D02_HFX-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D03_HFX_*.png /home/edson/d-wrf-op/py-output/D03_HFX-resized.gif

echo "Generating RAIN images into gifs"
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D01_RAIN_*.png /home/edson/d-wrf-op/py-output/D01_RAIN-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D02_RAIN_*.png /home/edson/d-wrf-op/py-output/D02_RAIN-resized.gif
convert -delay 50 -loop 0 -resize 50% /home/edson/d-wrf-op/py-output/$DATE/D03_RAIN_*.png /home/edson/d-wrf-op/py-output/D03_RAIN-resized.gif