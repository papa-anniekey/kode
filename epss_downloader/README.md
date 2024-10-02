EPSSのデータをバルクでダウンロードするPython Programです。<P>
EPSSのデータは以下のサイトで公開されています。<BR>
https://www.first.org/epss/data_stats<P>
URLの形式は https://epss.cyentia.com/epss_scores-YYYY-mm-dd.csv.gz となっており、公開が開始された2021年4月14日から日次で公開されています。
このPython3プログラムは2021年4月14日から実行日までのデータをダウンロードします。<P>

なお、ダウンロードしたデータをSplunkで分析するためのパーサー(props.confとtransforms.conf)については以下で公開をしています。<BR>
https://github.com/papa-anniekey/Splunk_Add-on/tree/main/TA-EPSS<P>
ご活用ください。

