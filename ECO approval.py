from playwright.sync_api import sync_playwright

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
USER_DATA_DIR = "edge_profile"

ERP_URL = "http://hkerpapp.hk.globaltti.net:8068/OA_HTML/OA.jsp?page=/oracle/apps/fnd/wf/worklist/webui/AdvancWorklistPG&addBreadCrumb=Y&ebizHomeList=Y&_ti=43070547&oapc=5&oas=3pKUMBJFqt6OXJru7LgJsw.."

USERNAME = "TVN550501"
PASSWORD = "2025Vietnam2"

Approval_list = []
print("Input Approval_list (Enter to Finish):")

while True:
    val = input()
    if val == "":   # nếu dòng trống thì dừng
        break
    Approval_list.append(val)

print("Approval_list =", Approval_list)

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=False,
        executable_path=EDGE_PATH
    )
    page = context.new_page()
    page.goto(ERP_URL)

    # Đợi đến khi trang login hiện ra (nếu có)
    page.wait_for_selector('input[name="username"], input[name="UserName"], input[type="text"]')

    # Điền thông tin login - dùng các selector phổ biến
    page.fill('input[type="text"]', USERNAME)      # ô username
    page.fill('input[type="password"]', PASSWORD)  # ô password

    # Click nút Log In
    page.click('input[type="submit"], button:has-text("Log In")')

    page.wait_for_load_state('networkidle')

        # Tìm tất cả <a> có id bắt đầu bằng "N42:NtFSubject:"
    page.wait_for_timeout(3000)

    base = 'http://hkerpapp.hk.globaltti.net:8068/OA_HTML/'

    rows = page.locator("tr")
    row_count = rows.count()
    print(f"🔍 Tổng số <tr> tìm được: {row_count}")

    for i in range(row_count):
        row = rows.nth(i)
        link = row.locator("a[href]").first
        if link.count() > 0:
            href = link.get_attribute("href")
            ECO = link.get_attribute("title")
            if ECO is not None:
                if ECO.split()[1] in Approval_list:
                    print(f"Hàng {i+1}: {ECO} with {href}")
                    if href:
                        # Nếu href bắt đầu bằng "/", ghép vào base
                        full_url = href if href.startswith("http") else base + href
                        new_tab = context.new_page()
                        new_tab.goto(full_url)
                        print(f"Opened tab {ECO}")
                        try:
                            new_tab.wait_for_load_state('domcontentloaded')  # đợi trang tải xong cơ bản
                            new_tab.locator('button[title="Approve"]').first.click(force=True)
                            print(f"Clicked Approve in tab {ECO}")
                        except Exception as e:
                            print(f"Not found Approve buttom in tab {ECO}: {e}")
    page.wait_for_timeout(2000)
    context.close()