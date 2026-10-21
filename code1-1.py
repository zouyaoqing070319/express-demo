from bs4 import BeautifulSoup

def get_schedule():
    # 读取360导航   html文件
    with open("schedule.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, features="html.parser")
    # 获取页面里面全部table表格
    table_list = soup.find_all("table")
    print(f"页面一共找到 {len(table_list)} 个表格\n")

    # 遍历打印每一张表格
    for idx, table in enumerate(table_list):
        print(f"==========第{idx+1}张表格==========")
        all_rows = table.find_all("tr")
        for row in all_rows:
            cells = row.find_all("td")
            cell_text = [cell.get_text(strip=True) for cell in cells]
            print(cell_text)
        print("\n")

if __name__ == '__main__':
    get_schedule()
