import requests
import base64

def fetch_url(url):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.text.splitlines()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

def main():
    # 定义订阅源URL
    urls = [
        "https://raw.githubusercontent.com/net5705632/ss/refs/heads/main/ss.txt",
        "https://raw.githubusercontent.com/net5705632/workers_jm/refs/heads/main/hy2.txt"
    ]

    # 获取并合并订阅节点
    nodes = []
    for url in urls:
        nodes.extend(fetch_url(url))
    
    # 去重处理
    unique_nodes = list(set(nodes))
    
    # 转换为字符串并Base64编码
    merged_content = "\n".join(unique_nodes).encode("utf-8")
    base64_content = base64.b64encode(merged_content).decode("utf-8")
    
    # 保存到文件
    with open("bypass_subscribe.txt", "w") as f:
        f.write(base64_content)
    
    print(f"Generated {len(unique_nodes)} nodes in bypass_subscribe.txt")

if __name__ == "__main__":
    main()
