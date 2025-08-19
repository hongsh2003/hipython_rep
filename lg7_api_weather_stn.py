import requests
import mariadb
import sys

URL = "https://apihub.kma.go.kr/api/typ01/url/stn_inf.php?inf=AWS&stn=&tm=202211300900&help=2&authKey=ImPZDKrERzmj2QyqxHc5IQ"

try:
    conn_tar = mariadb.connect(
        user="lguplus7",
        password="lg7p@ssw0rd~!",
        host="localhost",
        port=3310,
        database="cp_data"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
tar_cur = conn_tar.cursor()

cnt = 0
print("="*100)

res = requests.get(URL)
if res is None:
    print(f"API connect error")
    sys.exit(1)
print("successful connect")

print("=" * 100)
tmp = list(res.content.decode('cp949').strip().replace('Gangjin Gun','Gangjin-Gun').replace(' * ','').replace('     ',' ').replace('    ',' ').replace('   ',' ').replace('  ',' ').split('\n'))
print(tmp[0].split())
print(tmp[1].split())
print(len(tmp[13].split()))

for i in tmp:

    line = i.split()
    if len(line) < 13:
        continue
    elif line[0] == "#":
        continue

    try:
        tar_cur.execute(
            "insert into tb_weather_tcn(STN_ID, LON, LAT, STN_SP, HT, HT_WD, LAU_ID, STN_AD, STN_KO, STN_EN, FCT_ID, LAW_ID, BASIN, org_addr, create_dt)"
            "values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,now())",
            (*line, ', '.join(line))
        )
        conn_tar.commit()
        print(f'{line[0]} : insert into tcn_data done')

    except mariadb.Error as e:
        print(f"Error insert to MariaDB Platform: {e}")
        print(line)
        continue