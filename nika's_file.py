 LastUpd = mods.findall('span', class_= 'detail-updated') 
    CreatDate = mods.findall('span', class_= 'detail-created')
    filesize = mods.findall('span', class_= 'detail-size')

    Lastest_realise = LastUpd.text
    Create_date = CreatDate.text
    Filesize = filesize.text

    Downloads = mods.find('span', class_= 'detail-downloads').text

    c+=1