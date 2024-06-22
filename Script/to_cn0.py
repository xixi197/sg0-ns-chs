import sys, os

def get_pos(line):
    start = 0
    end = 0
    if line.startswith(':'):
        start = line.find('[0x02]') + 6
    elif line.startswith('['):
        start = line.find(']') + 1
    else:
        start = 0
    end = line.rfind('[0xFF]') - 6
    return start, end

doc_cnsg = 'cnsg0' # msb doc
doc_ensg = 'ensg0' # msb doc
doc_cn = 'cn' # txt doc
doc_en = 'en' # txt doc
doc_mg = 'mg' # txt doc
doc_re = 're' # msb doc

# cn msb to txt
# for file in os.listdir(doc_cnsg):
#     print(file)
#     if file.startswith('sg'):
#         file_sg_path = os.path.join(doc_cnsg, file)
#         file_cn_path = os.path.join(doc_cn, file) + '.txt'
#         os.system('./MagesTools -type=script -export -skip=false -format=Npcs -charset=charset0.utf8 -source=' + file_sg_path + ' -output=' + file_cn_path)

# en msb to txt
# for file in os.listdir(doc_ensg):
#     if file.startswith('sg'):
#         print(file)
#         file_sg_path = os.path.join(doc_ensg, file)
#         file_en_path = os.path.join(doc_en, file) + '.txt'
#         os.system('./MagesTools -type=script -export -skip=false -format=Npcs -charset=charset0.utf8 -source=' + file_sg_path + ' -output=' + file_en_path)

# merge txt
# for file in os.listdir(doc_cn):
#     if file.startswith('sg'):
#         file_cn = open(os.path.join(doc_cn, file), 'r')
#         file_en = open(os.path.join(doc_en, file), 'r')
#         file_mg = open(os.path.join(doc_mg, file), 'w+')
#         line_cn = file_cn.readline()
#         line_en = file_en.readline()
#         while len(line_cn) > 0:
#             start_cn, end_cn = get_pos(line_cn)
#             start_en, end_en = get_pos(line_en)
#             line_mg = line_cn[:start_cn] + line_en[start_en:end_en] + ' ' + line_cn[start_cn:]
#             file_mg.write(line_mg)
#             line_cn = file_cn.readline()
#             line_en = file_en.readline()

# txt to msb
for file in os.listdir(doc_mg):
    if file.startswith('sg'):
        file_mg_path = os.path.join(doc_mg, file)
        file_sg_path = os.path.join(doc_cnsg, file)[:-4]
        file_re_path = os.path.join(doc_re, file)[:-4]
        print(file_sg_path)
        os.system('./MagesTools -type=script -import -skip=false -format=Npcs -charset=charset0.utf8 -source=' + file_sg_path + ' -input=' + file_mg_path + ' -output=' + file_re_path)
