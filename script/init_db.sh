#!/usr/bin/env bash


# 第一次创建makemigrations时需要带上app name
#echo `ls /work/dev/db_tools`
python /work/dev/db_tools/manage.py makemigrations --noinput

python /work/dev/db_tools/manage.py migrate --noinput




# 执行数据初始化
if [ "$DEBUG" == "True" ]; then
    echo "use debug mode"
#    python manage.py loaddata auto_test_account.json
else
    echo "use product mode"

fi



exec "$@"