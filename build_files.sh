# echo " BUILD START"
# python3.10.4  -m pip install -r requirements.txt
# python3.10.4 manage.py collectstatic  --noinput --clear
# echo " BUILD END"

pip install -r requirements.txt
python3.9 manage.py collectstatic