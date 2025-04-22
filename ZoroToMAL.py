file = open("export.txt", "r", encoding="utf-8")
importFile = open("import.xml", "w", encoding="utf-8")
status = ""
animeCode = ""

importFile.write("""<?xml version="1.0" encoding="UTF-8" ?>		
		<myanimelist>
			<myinfo>
				<user_export_type>1</user_export_type>
			</myinfo>""")
for line in file:
    line = line.strip()
    sep = line.split("/")
    if sep[-1] == "# Plan to Watch":
        status = "Plan to Watch"
    elif sep[-1] == "# Completed":
        status = "Completed"
    elif sep[-1] == "# Watching":
        status = "Watching"
    elif sep[-1] == "# On-Hold":
        status = "On-Hold"
    elif sep[-1] == "# Dropped":
        status = "Dropped"
    else:
        animeCode = sep[-1]
        importFile.write(
                f"""
                <anime>
                    <series_animedb_id>{animeCode}</series_animedb_id>
                    <my_status>{status}</my_status>
                    <update_on_import>1</update_on_import>
                </anime>\n"""
            )
importFile.write("</myanimelist>")
file.close()
importFile.close()
