#!/usr/bin/env python
#!/usr/bin/env python

#This is the first step in creating a scraper to grab details from PDFs
#This just goes to one page, grabs the description, and grabs the PDF url
#There's no need to define a function or loop yet - that happens in the next version of the scraper once we've tested it

import scraperwiki
import lxml.html

#store the base url which all our specific ones will be added to
baseurl = 'http://www.ofcom.org.uk/static/radiolicensing/html/radio-stations/community/'

#store the relative urls that will go on the end of that. This is pasted from a spreadsheet, exported from a quick scrape using Outwit Hub
#The downside of this approach is that if the page listing these URLs change, this scraper will not reflect that.
#Because this goes over more than one line, I've used ''' to mark the start and end of the string
urls = '''cr000214ba11ummahfm.htm
cr000109ba210radio.htm
cr000141ba13tfmcommunityradioforhealth.htm
cr100059ba1abc-fm.htm
cr000243ba1air.htm
cr000023ba2allfm.htm
cr000235ba1abbey104.htm
cr000203ba2academyfm1059.htm
cr000202ba2academyfm1078.htm
cr000240ba1accessfm.htm
cr100143ba1akashradioleeds.htm
cr000129ba1aldergroveandantrimfm.htm
cr000126ba2aliveradio.htm
cr000170ba2ambersoundfm.htm
cr000175ba2amburradio.htm
cr000002ba3angelradio.htm
cr000007ba1angelradioisleofwight.htm
cr000241ba1applefm.htm
cr000067ba1asianstar1016fm.htm
cr000208ba2awaazradio.htm
cr000019ba2awazfm.htm
cr000068ba3bangradio.htm
cr000021ba2bcb1066fm.htm
cr000096ba2bfbs.htm
cr000092ba2bfbs.htm
cr000147ba2bfbs.htm
cr000058ba3bfbs.htm
cr000234ba3bfbs.htm
cr000079ba3bfbs.htm
cr000045ba3bfbslisburnfm.htm
cr000110ba1brfm.htm
cr000107ba2brfm956fm.htm
cr000122ba2broradio.htm
cr000127ba1bangorfm.htm
cr000236ba1bayfmradio.htm
cr100062ba1belfastfm.htm
cr000222ba2betarbanglaradio.htm
cr100138ba1beverleyfm.htm
cr000038ba2bigcityradio.htm
cr000196ba3bigglesfm.htm
cr000146ba3bishopfm1059.htm
cr000041ba1blackcountryradio.htm
cr000081ba2blackdiamondfm.htm
cr000140ba2blast106.htm
cr000188ba2blythvalleyradio.htm
cr000163ba2boltonfm.htm
cr000232ba1bradleystokeradio.htm
cr000085ba1branchfm.htm
cr000135ba1brickfm.htm
cr000078ba1bristolcommunityfm.htm
cr000124ba3buteislandradio.htm
cr000248ba1chbn.htm
cr000066ba2csr.htm
cr000091ba1calonfm.htm
cr000193ba2camfm.htm
cr000256ba1camglenradio.htm
cr000095ba1cambridge105fm.htm
cr000160ba3canalsidesthethread1028fm.htm
cr101253ba1candofm.htm
cr000093ba3castledownradio.htm
cr000257ba1celticmusicradio.htm
cr000025ba1chorleyfm.htm
cr000158ba3citybeatpreston.htm
cr000144ba3communityvoicefm.htm
cr000185ba2corbyradio.htm
cr000026ba2crescentradio.htm
cr000003ba2crossrhythmscityradio.htm
cr000059ba1crossrhythmsplymouth.htm
cr000098ba1crossrhythmsteesside.htm
cr000258ba1crystalfm.htm
cr100180ba1dalesradio.htm
cr000179ba2demonfm.htm
cr000061ba2desiradio.htm
cr000215ba2destiny105.htm
cr000265ba1deveronfm.htm
cr000089ba1diversefm.htm
cr000047ba2downfm.htm
cr000132ba2drive105fm.htm
cr000148ba2drystoneradio.htm
cr000136ba3dunooncommunityradio.htm
cr000178ba2eavafm.htm
cr000259ba1eastcoastfm.htm
cr100181ba1edenfm.htm
cr000171ba3erewashsound.htm
cr000006ba2expressfm.htm
cr000231ba1fantasyradio.htm
cr000190ba3felixstoweradio.htm
cr000155ba2flameccr.htm
cr000063ba2forestfm.htm
cr000230ba1fromefm.htm
cr000192ba2futureradio.htm
cr000004ba2gtfmpontypridd.htm
cr000218ba3gateway978.htm
cr000186ba2gaydio.htm
cr000117ba2glastonburyfm.htm
cr000054ba3gloucesterfm.htm
cr000168ba2gravityfm.htm
cr100527ba1gulshanradio.htm
cr000199ba3hcrfm.htm
cr000102ba1haltoncommunityradio.htm
cr000013ba1harboroughfmhfm.htm
cr000073ba2hayesfm.htm
cr000181ba2hermitagefm.htm
cr100399ba1hitmixradio.htm
cr000131ba1holywoodfm.htm
cr000086ba1hopefm.htm
cr000120ba1hotradio1028.htm
cr100147ba1hullkingstonradio.htm
cr100152ba1imanfm.htm
cr000200ba3in2beatsfm.htm
cr000217ba1insanityradio.htm
cr000017ba1insightradio.htm
cr000184ba2inspirationfm.htm
cr000198ba2inspirefm.htm
cr000087ba3ipswichcommunityradio.htm
cr000263ba2irvinebeatfm.htm
cr000261ba1k107fm.htm
cr000162ba3kcclive.htm
cr000264ba1kcr.htm
cr000220ba2kanefm.htm
cr000016ba1kemetradio.htm
cr100214ba1koastradio.htm
cr000180ba1kohinoorfm.htm
cr000164ba3legacy901.htm
cr000195ba2leisurefm.htm
cr000166ba3lincolncityradio.htm
cr100157ba1linkfm.htm
cr000049ba2lionheartradio.htm
cr100797ba1mkfm.htm
cr000209ba3marlowfm.htm
cr000134ba2mearnsfm.htm
cr000206ba2meridianfm.htm
cr000245ba1monfm.htm
cr000161ba2moorlandsradio.htm
cr000050ba2ne1fm1025.htm
cr000262ba1nevisradio.htm
cr000037ba2newstyleradio987fm.htm
cr000165ba3northmanchesterfm.htm
cr100520ba1novafm.htm
cr000069ba1nusoundradio.htm
cr000032ba2oldhamcommunityradio.htm
cr000099ba1pendlecommunityradio.htm
cr000153ba2penistonefm.htm
cr000249ba2penwithradio.htm
cr000075ba1phoenixfm.htm
cr000022ba2phoenixfm.htm
cr000118ba1phonicfm.htm
cr000157ba2pointfm.htm
cr000239ba1pulse.htm
cr000138ba3pulsecommunityradio.htm
cr000034ba1pure1078fm.htm
cr100346ba1quayfm.htm
cr000189ba3rwsfm1033.htm
cr000177ba1raajfm.htm
cr000201ba2radioashford.htm
cr000031ba2radioasianfever.htm
cr000210ba1radiobgws.htm
cr000094ba2radiocardiff.htm
cr000015ba2radiodawn.htm
cr000014ba3radiofaza971fm.htm
cr000244ba1radioglanclwyd.htm
cr000145ba1radiohartlepool.htm
cr000011ba3radioikhlas.htm
cr000149ba2radiojcom.htm
cr000197ba2radiolab.htm
cr100523ba1radionewark.htm
cr000182ba3radioplus.htm
cr000057ba1radioreverb.htm
cr000030ba2radioscilly.htm
cr000115ba2radiostaustellbay.htm
cr000082ba1radioteesdale.htm
cr000111ba1radiotircoed.htm
cr000090ba1radioverulam.htm
cr000233ba1radiowinchcombe.htm
cr000151ba3redroadfm.htm
cr000224ba2reprezent1073fm.htm
cr000060ba3resonancefm.htm
cr000020ba1revivalfm.htm
cr000225ba2rinsefm.htm
cr000219ba2sfm.htm
cr000106ba1saintfm.htm
cr000035ba1salfordcityradio.htm
cr000211ba3seahavenfm.htm
cr000052ba1seasidefm1053.htm
cr000083ba1sheffieldlive!932fm.htm
cr000150ba1sinefm.htm
cr000088ba1sirenfm.htm
cr000009ba2skylinegold1025.htm
cr000113ba2somervalleyfm.htm
cr000112ba2soundartradio.htm
cr000143ba2sparkfm.htm
cr000133ba3speysoundradio.htm
cr000142ba2spicefm.htm
cr100531ba1staffordfm.htm
cr000018ba1sunnygovanradio.htm
cr000223ba1susyradio.htm
cr000119ba1swindon1055.htm
cr000174ba3switchradio1075.htm
cr000173ba3tcrfm.htm
cr000266ba1td1radio.htm
cr000154ba2tmcr.htm
cr000010ba2takeoverradio.htm
cr000169ba2takeoverradio1069.htm
cr000033ba1tamesideradio.htm
cr000064ba2tempo1074fm.htm
cr100139ba1thecat.htm
cr000012ba2theeye.htm
cr000183ba2thehillzfm.htm
cr000252ba1thehub.htm
cr000114ba2thesource.htm
cr000238ba1thevoice.htm
cr000242ba2tonefm.htm
cr000156ba1tudnofm.htm
cr000172ba2tulipradio.htm
cr000207ba2uckfieldfm.htm
cr000116ba2ujimaradio.htm
cr000008ba2unity101.htm
cr000039ba3unityfm.htm
cr000187ba2unityradio.htm
cr000216ba2vibe1076fm.htm
cr000152ba2vixen101.htm
cr000213ba2voicefm.htm
cr000070ba1voiceofafricaradio.htm
cr000229ba1wcr.htm
cr000042ba2wcrfm.htm
cr000056ba1westhullcommunityradio.htm
cr100133ba1westwoldsradio.htm
cr000072ba1westside896fm.htm
cr000100ba2wirralradio.htm
cr000024ba2wythenshawefm.htm
cr000053ba1youthcommradio.htm
cr000191ba2zackfm1053.htm
cr100123ba1zetlandfm.htm
cr100061ba1fusefm.htm
cr000028ba1shmufm.htm'''

#split that string on each new line, to create a list
urllist = urls.split('\n')

#define a function which will grab the description and link
#It uses one argument: a parameter (variable) it calls url
def grablinks(url):
    #This line uses the url variable
    html = scraperwiki.scrape(baseurl+url)
    #Turn it into an lxml 'object' we call root
    root = lxml.html.fromstring(html)
    #grab the items in that page within div class='body' and within p tags - this is put in a list variable called ps
    ps = root.cssselect("div.body p")
    #turn the first item in that list [0] to a string and print it
    print lxml.html.tostring(ps[0])
    #use text_content() to just grab the text, not the HTML tags, from the same item
    description = ps[0].text_content()
    print description
    #grab the items in that page within div class='body' in p tags and then a tags - this is put in a list variable called links
    links = root.cssselect("div.body p a")
    #this time we don't want the text but the actual link attribute itself
    #the method .attrib will grab the specified attribute of the first item [0] in links
    pdflink = links[0].attrib['href']
    print pdflink

    #At this stage nothing is stored but we have used print to check we are getting what we want.
    #What we don't know yet is whether the first p is ALWAYS the description, and whether the first link in that div is ALWAYS the PDF.
    #That's what we text next, but I'm going to put that in a fork of this.

#loop through the list and run the 'grablinks' function defined above on each url
for url in urllist:
    print 'scraping', url
    grablinks(url)
    #First time this generated an error on this url: cr000254ba1anr%C3%A8idio.htm
    #Testing it, this is a dead link from the Ofcom page: http://www.ofcom.org.uk/static/radiolicensing/html/radio-stations/community/community-main.htm
    #So it is removed from the list
    #This is also an error: 'cr000046ba1irfm.htm'
    #cr000139ba1lisburn%E2%80%99s98fm.htm
    #cr000044ba2raidi%C3%B3f%C3%A1ilte.htm

#Next step is to do something with the PDF links grabbed from each page. That will be on another fork.
