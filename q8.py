

col_list = df["Stats_Access_Link"].values.tolist()
for (i in col_list){
    i = i.replace('<url>https://', ''))
    i = i.replace('<url/>', '' )
}