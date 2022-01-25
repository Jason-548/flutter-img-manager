#!/bin/bash

# 只有2倍图被利用
source='/Users/jq/Desktop/image'
destination='/Users/jq/Desktop/mine-app-ui/images'

rename 's/／/-/' $source/*.png
rename 's/ /-/' $source/*.png
mkdir $source/tmp
cp $source/*@2x.png $source/tmp
rename 's/\@2x.png/\.png/' $source/tmp/*.png
cp $source/tmp/*.png $destination
rm -rf $source/tmp
rm $source/*.*
