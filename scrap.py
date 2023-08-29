import modules.Scrapping as scraper
import modules.util as utils
from tqdm import tqdm
import os

for i in tqdm(range(69, len(utils.getSubjectCode()))):
    output_path = 'D:\KULIAH\RISET STKI 2023\Scrapping by Subjects\output\\'
    subjectCode = utils.mergedSortedSubject()[i]
    if not os.path.exists(output_path + subjectCode  + '/'):
        os.makedirs(output_path + subjectCode  + '/')

    url = f'http://repository.lppm.unila.ac.id/cgi/exportview/subjects/{subjectCode}/JSON/{subjectCode}.js'
    scrap_result = scraper.parsePage(scraper.getDriver(), url)
    json_content = scraper.getRawJSON(scrap_result)
    
    with open(output_path + subjectCode +'\\' + subjectCode + '.json', 'w', encoding="utf-8") as f:
        f.write(json_content)
