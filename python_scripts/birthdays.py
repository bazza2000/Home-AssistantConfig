newyear=[1,1,'new_years_day','New Years Day']
christmas=[25,12,'christmas_day','Christmas Day']
baz=[11,10,'baz_birthday','Barrys Birthday']
ruth=[29,4,'ruth_birthday','Ruths Birthday']
zak=[11,9,'zak_birthday','Zaks Birthday']
luke=[31,8,'luke_birthday','Lukes Birthday']
julie=[25,5,'julie_birthday','Julies Birthday']
amy=[20,6,'amy_birthday','Amys Birthday']
phil=[9,3,'phil_birthday','Phils Birthday']
charlotte=[28,5,'charlotte_birthday','Charlotttes Birthday']
sue=[8,5,'sue_birthday','Sues Birthday']
bigalex=[25,8,'bigalex_birthday','Big Alexs Birthday']
shell=[14,9,'shell_birthday','Shells Birthday']
littlealex=[5,3,'littlealex_birthday','Little Alexs Birthday']
sophie=[21,4,'sophie_birthday','Sophies Birthday']
andy=[6,2,'andy_birthday','Andy Birthday']
lorainne=[18,1,'lorraine_birthday','Lorraines Birthday']
grandad=[16,2,'grandad_birthday','Grandads Birthday']
grandma=[24,3,'grandma_birthday','Grandmas Birthday']
rachel=[12,7,'rachel_birthday','Rachels Birthday']

def define_date(hass, date_array):
  diff = datetime.datetime(datetime.datetime.now().year, date_array[1], date_array[0]) - datetime.datetime.now()
  if diff.days < 0:
    diff = datetime.datetime(datetime.datetime.now().year + 1, date_array[1], date_array[0]) - datetime.datetime.now()
  hass.states.set('sensor.' + date_array[2] , diff.days + 1,{ 'unit_of_measurement': 'days', 'friendly_name': 'Days until ' + date_array[3], 'icon': 'mdi:calendar' })

define_date(hass,newyear)
define_date(hass,christmas)
define_date(hass,baz)
define_date(hass,ruth)
define_date(hass,zak)
define_date(hass,luke)
define_date(hass,julie)
define_date(hass,amy)
define_date(hass,phil)
define_date(hass,charlotte)
define_date(hass,sue)
define_date(hass,bigalex)
define_date(hass,shell)
define_date(hass,littlealex)
define_date(hass,sophie)
define_date(hass,andy)
define_date(hass,lorainne)
define_date(hass,grandad)
define_date(hass,grandma)
define_date(hass,rachel)

