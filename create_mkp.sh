#!/bin/bash
#set -x

if [ $1 ] ; then
	echo "Good start!"
else
	echo "No $1"
	exit 1
fi

package=$(echo $1 | tr -d '/')
version=$(grep "'version'" $package/info | cut -d "'" -f 4)
homedir=$(pwd)

cd $package

jq -c . < info > info.json

tar -cvf $package"-"$version.tar info info.json

ls -d1 */ | while read line
do
	dir=$(echo $line | tr -d '/')
	cd $homedir/$package/$dir
	tar -cf ../$dir.tar *
	cd $homedir/$package
	tar -rvf $package"-"$version.tar $dir.tar
	rm $dir.tar
done

rm -v $package"-"*.mkp

gzip $package"-"$version.tar
mv $package"-"$version.tar.gz $package"-"$version.mkp
cp -vf $package"-"$version.mkp $package.mkp

echo "GIT"
git add --all
git commit -a -m "$package v$version - build"
git push origin master

cd ..

echo "Enter for deploy"
read

echo "TBD"
