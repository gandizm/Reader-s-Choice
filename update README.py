import os

# 设置文件夹路径和GitHub信息
folder = "-24春"  # 文件夹名称
github_user = "gandizm"  # GitHub用户名
github_repo = "Reader-s-Choice"  # GitHub仓库名

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 构造文件夹的绝对路径
folder_path = os.path.join(current_dir, folder)

# 检查文件夹是否存在
if not os.path.exists(folder_path):
    print(f"文件夹 '{folder}' 不存在！")
    exit()

# 生成Markdown链接
markdown_links = []
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        # 构造Markdown链接
        link = f'- [{filename}](<https://github.com/{github_user}/{github_repo}/blob/main/{folder}/{filename}>)'
        markdown_links.append(link)

# 将生成的链接添加到README.md
readme_path = os.path.join(current_dir, "README.md")
with open(readme_path, "a", encoding="utf-8") as readme_file:
    readme_file.write("\n".join(markdown_links) + "\n")

print("链接已成功添加到README.md！")