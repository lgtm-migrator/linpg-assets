from linpg import Builder  # type: ignore

# compile all files
additional_files: tuple[str, ...] = ("README.md", "LICENSE")
Builder.compile(
    "linpgassets",
    update_the_one_in_sitepackages=False,
    additional_files=additional_files,
)

if input("Do you want to package and upload the latest build (Y/n):") == "Y":
    Builder.upload_package()
