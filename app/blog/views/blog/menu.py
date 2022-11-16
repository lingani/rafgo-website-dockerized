class Menu:	
	def __init__(self):
		self.page_menus = [
		{
			"page":"home",  "menu_items": [
			{"position": "1", "name":"Accueil", "href": "#"},
			{"position": "2", "name":"A Propos", "href": "#about"},
			{"position": "3", "name":"Notre Leadership", "href": "#team"},
			{"position": "4", "name":"Nos Membres", "href": "#portfolio"},
			{"position": "5", "name":"Nos Projets", "href": "#services"},
			{"position": "6", "name":"Blog", "href": "#recent-blog-posts"},
			{"position": "7", "name":"Nous Contacter", "href": "#contact"}]
		},

		{
			"page":"blog",  "menu_items": [
			{"position": "1", "name":"Accueil", "href": "../home"},
			{"position": "2", "name":"A Propos", "href": "../home/#about"},
			{"position": "3", "name":"Notre Leadership", "href": "../home/#team"},
			{"position": "4", "name":"Nos Membres", "href": "../home/#portfolio"},
			{"position": "5", "name":"Nos Projets", "href": "../blog/#services"},
			{"position": "6", "name":"Blog", "href": "#"},
			{"position": "7", "name":"Nous Contact", "href": "../blog/#contact"}]
		},

		{
			"page":"blog-details",  "menu_items": [
			{"position": "1", "name":"Accueil", "href": "../home"},
			{"position": "2", "name":"A Propos", "href": "../home/#about"},
			{"position": "3", "name":"Notre Leadership", "href": "../home/#team"},
			{"position": "4", "name":"Nos Membres", "href": "../home/#portfolio"},
			{"position": "5", "name":"Nos Projets", "href": "../home/#services"},			
			{"position": "6", "name":"Bolg", "href": "../blog"},
			{"position": "7", "name":"Nous Contact", "href": "../home/#contact"},]
		},

		{
			"page":"member-details",  "menu_items": [
			{"position": "1", "name":"Accueil", "href": "../home"},
			{"position": "2", "name":"A Propos", "href": "../home/#about"},
			{"position": "3", "name":"Notre Leadership", "href": "../home/#team"},
			{"position": "4", "name":"Nos Membres", "href": "../home/#portfolio"},
			{"position": "5", "name":"Nos Projets", "href": "../home/#services"},
			{"position": "6", "name":"Bolg", "href": "../blog"},
			{"position": "7", "name":"Nous Contact", "href": "../home/#contact"}]
		},
		
		{
			"page":"project-details",  "menu_items": [
			{"position": "1", "name":"Accueil", "href": "../home"},
			{"position": "2", "name":"A Propos", "href": "../home/#about"},
			{"position": "3", "name":"Notre Leadership", "href": "../home/#team"},
			{"position": "4", "name":"Nos Membres", "href": "../home/#portfolio"},
			{"position": "5", "name":"Nos Projets", "href": "../home/#services"},
			{"position": "6", "name":"Bolg", "href": "../blog"},
			{"position": "7", "name":"Nous Contact", "href": "../home/#contact"}]
		}
	]	
	
	def get_page_menus(self, page):
		lst_menu = [p["menu_items"] for p in self.page_menus if p["page"] == page]
		if lst_menu:
			return lst_menu[0]
		else:
			return []