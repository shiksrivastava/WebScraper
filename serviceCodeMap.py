from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pickle
from convertFormat import formattedServices, services


###########################################################################################
# web loop to get fill "megaList" with a url for every service, already done
###########################################################################################

# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# megaList = []

# for service in services:
#     driver.get("https://www.homeadvisor.com/c.html")
#     inputZip = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "zip")))
#     inputZip.send_keys("85085")
#     inputService = Select(driver.find_element_by_id('catOid'))
#     inputService.select_by_visible_text(service)
#     button = driver.find_element_by_id("browse-reviews")
#     button.click()
#     megaList.append(driver.current_url)

###########################################################################################


###########################################################################################
# the code below reflects megaList as of December 7th, 2020
###########################################################################################

megaList = ['https://www.homeadvisor.com/c.Air-Conditioning.San_Jose.CA.-12002.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Appliances.San_Jose.CA.-12003.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Appraiser.San_Jose.CA.-12004.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Architects-Engineers.San_Jose.CA.-12005.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Art-Mirror-and-Picture-Hanging.San_Jose.CA.-15213.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Audio-Visual-Computers.San_Jose.CA.-12006.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Awnings.San_Jose.CA.-12007.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Brick-Stone.San_Jose.CA.-12008.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Cabinets.San_Jose.CA.-12009.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Carpenters.San_Jose.CA.-12010.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Carpet-Upholstery-Cleaning.San_Jose.CA.-12011.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Ceilings.San_Jose.CA.-12012.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Central-Vacuum.San_Jose.CA.-12013.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Cleaning-Maid-Services.San_Jose.CA.-12014.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Concrete.San_Jose.CA.-12015.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Countertops.San_Jose.CA.-12016.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Decks.San_Jose.CA.-12017.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Demolition-Service.San_Jose.CA.-12018.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Designers-Decorators.San_Jose.CA.-12019.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Developer.San_Jose.CA.-12020.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Disability-Services.San_Jose.CA.-12021.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Disaster-Recovery-Services.San_Jose.CA.-12022.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Docks.San_Jose.CA.-12023.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Doors.San_Jose.CA.-12024.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Drywall-Plaster.San_Jose.CA.-12025.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Electrical.San_Jose.CA.-12026.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Excavation.San_Jose.CA.-12028.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Fans.San_Jose.CA.-12029.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Fences.San_Jose.CA.-12030.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Fireplace-Wood-Stoves.San_Jose.CA.-12031.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Fitness-and-Sports-Equipment-Assembly.San_Jose.CA.-15212.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Flooring-Carpet.San_Jose.CA.-12032.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Foundations.San_Jose.CA.-12033.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Fountains-Ponds.San_Jose.CA.-12034.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Furniture-Assembly.San_Jose.CA.-15209.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Furniture-Repair-Refinish.San_Jose.CA.-12035.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Garage-Garage-Doors.San_Jose.CA.-12036.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Glass-Mirrors.San_Jose.CA.-12037.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Gutters.San_Jose.CA.-12038.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Handyman-Services.San_Jose.CA.-12039.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Heating-Furnace-Systems.San_Jose.CA.-12040.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Home-Inspection.San_Jose.CA.-12041.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Home-Maintenance.San_Jose.CA.-12042.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Home-Security-Services.San_Jose.CA.-12043.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Hot-Tubs-Spas-Saunas.San_Jose.CA.-12044.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Household-Help.San_Jose.CA.-15088.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Insulation.San_Jose.CA.-12045.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Landscaping.San_Jose.CA.-12046.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Lawn-Garden-Care.San_Jose.CA.-12047.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Lifting-Furniture-and-Heavy-Items.San_Jose.CA.-15211.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Locksmith.San_Jose.CA.-12048.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Metal-Fabrication.San_Jose.CA.-12049.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Mold-Asbestos-Services.San_Jose.CA.-12072.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Moving.San_Jose.CA.-12050.html?zipSearched=95122', 'https://www.homeadvisor.com/c.New-Home-Builders.San_Jose.CA.-12051.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Organizers.San_Jose.CA.-12052.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Outdoor-Playgrounds.San_Jose.CA.-12053.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Packing-and-Unpacking.San_Jose.CA.-15208.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Painting.San_Jose.CA.-12054.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Paving.San_Jose.CA.-12055.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Permit-Services.San_Jose.CA.-12056.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Pest-Control.San_Jose.CA.-12057.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Plumbing.San_Jose.CA.-12058.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Powdercoating.San_Jose.CA.-12059.html?zipSearched=95122', 'https://www.homeadvisor.com/c.powerwashing.San_Jose.CA.-14980.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Roofing.San_Jose.CA.-12061.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Sandblasting-Service.San_Jose.CA.-12062.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Septic-Tanks-Wells.San_Jose.CA.-12081.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Sheds-Enclosures.San_Jose.CA.-12063.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Siding.San_Jose.CA.-12064.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Sign-Making-Service.San_Jose.CA.-12065.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Skylights.San_Jose.CA.-12066.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Snow-Removal-Service.San_Jose.CA.-12067.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Solar.San_Jose.CA.-14820.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Stained-Glass.San_Jose.CA.-12068.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Swimming-Pools.San_Jose.CA.-12070.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Tennis-or-Game-Court.San_Jose.CA.-12071.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Tile.San_Jose.CA.-12073.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Tree-Service.San_Jose.CA.-12074.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Wall-Coverings.San_Jose.CA.-12075.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Waste-Material-Removal.San_Jose.CA.-12076.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Water-Treatment-System.San_Jose.CA.-12077.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Waterproofing.San_Jose.CA.-12078.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Window-Coverings.San_Jose.CA.-12079.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Windows.San_Jose.CA.-12080.html?zipSearched=95122', 'https://www.homeadvisor.com/c.Gardening-and-Yard-Work.San_Jose.CA.-15210.html?zipSearched=95122']


###########################################################################################
# creating a dictionary beteen each service and it's URL code
###########################################################################################

codeMap = {}

def whatServIn(url):
    for serv in formattedServices:
        if serv in url:
            return serv


for url in megaList:
    service = whatServIn(url)
    codeIndex = url.find(".html")
    code = url[codeIndex - 5: codeIndex]
    codeMap[service] = code


#manually handling errored services, can definitely fix this better in v2
codeMap["Additions-Remodeling"] = '12001'
codeMap["Art-Mirror-and-Picture-Hanging"] = '15213'
codeMap["Fitness-and-Sports-Equipment-Assembly"] = '15212'
codeMap["Garage-Garage-Doors"] = '12036'
codeMap["Hot-Tubs-Spas-Saunas"] = '12044'
codeMap["Lifting-Furniture-and-Heavy-Items"] = '15211'
codeMap["Packing-and-Unpacking"] = '15208'
codeMap["powerwashing"] = '14980'
codeMap["Gardening-and-Yard-Work"] = '15210'
del codeMap[None]