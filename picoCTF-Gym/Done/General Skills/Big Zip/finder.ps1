$result = "C:\Users\iRewiewer\Documents\Github Tmp\picoCTF-Gym-Training\Done\General Skills\Big Zip\result.txt"
$zipPath = "C:\Users\iRewiewer\Documents\Github Tmp\picoCTF-Gym-Training\Done\General Skills\Big Zip\big-zip-files\"
$files = Get-ChildItem -Path $zipPath -Filter *.txt -Recurse | %{$_.FullName} #| Where-Object {$_.PSIsContainer -eq $false}

foreach($file in $files)
{
	type $file >> $result
}