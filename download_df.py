from huggingface_hub import snapshot_download

# 定义目标目录，例如将仓库内容下载到当前目录下的 checkpoint 文件夹中
destination = "./checkpoint"

# 下载整个模型仓库，指定 repo_id、仓库类型以及目标目录
local_path = snapshot_download(
    repo_id="takuzennn/pi0_transfer_cube",
    repo_type="model",
    local_dir=destination
)

print(f"仓库已下载到: {local_path}")
