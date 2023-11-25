curl -XDELETE --insecure --user admin:'39fd950e-873f-11ee-913a-470ee3d36827' https://localhost:9200/$1-subdomain
echo
curl -XDELETE --insecure --user admin:'39fd950e-873f-11ee-913a-470ee3d36827' https://localhost:9200/$1-portscan
echo
curl -XDELETE --insecure --user admin:'39fd950e-873f-11ee-913a-470ee3d36827' https://localhost:9200/$1-webenum
echo
curl -XDELETE --insecure --user admin:'39fd950e-873f-11ee-913a-470ee3d36827' https://localhost:9200/$1-webvuln
echo
curl -XDELETE --insecure --user admin:'39fd950e-873f-11ee-913a-470ee3d36827' https://localhost:9200/$1-infravuln
