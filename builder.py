from linpg import Builder  # type: ignore

# 编译所有文件
additional_files: tuple[str, ...] = ("README.md", "LICENSE")
Builder.compile("linpgassets", additional_files=additional_files)

# 打包上传最新的文件
if input("Do you want to package and upload the lastest build (Y/n):") == "Y":
    Builder.upload_package()
