sed 's=https://annuel.framapad.org/p/=./offline/=g' ../influence.html > ../influence.tmp 
sed 's=/export/txt==g' ../influence.tmp >> ../influence.tmp2 

mv ../influence.tmp2 ../influence.html
rm ../influence.tmp


sed 's=https://annuel.framapad.org/p/=./offline/=g' ../usability.html > ../usability.tmp 
sed 's=/export/txt==g' ../usability.tmp >> ../usability.tmp2 

mv ../usability.tmp2 ../usability.html
rm ../usability.tmp

sed 's=https://annuel.framapad.org/p/=./offline/=g' ../negotiation.html > ../negotiation.tmp 
sed 's=/export/txt==g' ../negotiation.tmp >> ../negotiation.tmp2 

mv ../negotiation.tmp2 ../negotiation.html
rm ../negotiation.tmp