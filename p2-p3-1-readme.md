第一大条：自动任务   P3………….py
  1.P3 是给自动任务使用的，请自行修改好端口  账户名  钱包密码  每次任务取单数量
  
  ps -ef | grep cron    （查看是否有CRON 自动任务）  /user/sbin/cron -f  就是有
  
sudo service cron start   启动命令

sudo crontab -e   编辑命令  然后会跳出来让你选编辑器  我选VIM

0 9 * * * python3 /home/user/....../p3*****.py

分 时 天 月 周 命令

假设  每20分钟就是

*/20 * * * * py***  *****.py

假设  每小时的 第9分钟 就是

19 * * * * py***  *****.py    其他用法自己百度

编辑完 ESC   :wq  保存退出

sudo service cron restart    重启服务， 验证看有没有自动运行。 

每二条： 手动确认价格   p2**.py

自己看READ.ME 钱包设好，  py脚本内的 端口   账户名   密码填好。

主要用来ssh连接的时候 人工确认价格 是不是要取这价喂


第三条 1***.py

主要用来SSH连接  python3 /***/1**.py

输入喂价 直接喂的。



以上三个脚本， 请自行改好  脚本内的 端口   账户名   密码填好。
