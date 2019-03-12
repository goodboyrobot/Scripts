#/usr/bin/bash

echo "---Orion---"
echo "--Folders--"
for filename in *; do
	if [ -d $filename ]
		then du -sh $filename 2>/dev/null
	fi
done
echo "--Total--"
du -sh ./ 2>/dev/null

echo "---Iris---"
echo "--Folders--"
for filename in /media/iris/*; do
	if [ -d $filename ]
		then du -sh $filename 2>/dev/null
	fi
done
echo "--Total--"
du -sh /media/iris 2>/dev/null

