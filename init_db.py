from app import app, db, Artwork, Client, ContactMessage, MailingList

def init_database():
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Add sample artworks
        sample_artworks = [
            Artwork(
                title="Murderbot Concept Design",
                category="concept-art",
                description="Concept design for Apple TV+ series Murderbot",
                image_url="https://via.placeholder.com/600x400/667eea/ffffff?text=Murderbot",
                client="Apple TV+",
                year=2024,
                featured=True
            ),
            Artwork(
                title="Gideon the Ninth Cover",
                category="illustration",
                description="Book cover illustration for New York Times Bestseller",
                image_url="https://via.placeholder.com/600x400/764ba2/ffffff?text=Gideon",
                client="Tor.com Publishing",
                year=2023,
                featured=True
            ),
            Artwork(
                title="Starfield: Shattered Space",
                category="concept-art",
                description="Key art for Bethesda's Starfield expansion",
                image_url="https://via.placeholder.com/600x400/667eea/ffffff?text=Starfield",
                client="Bethesda Softworks",
                year=2024,
                featured=True
            ),
            Artwork(
                title="The Wandering Emperor",
                category="illustration",
                description="Magic: The Gathering card illustration",
                image_url="https://via.placeholder.com/600x400/764ba2/ffffff?text=MTG",
                client="Wizards of the Coast",
                year=2022,
                featured=True
            ),
            Artwork(
                title="The Witcher Cover Art",
                category="illustration",
                description="Book cover for The Witcher series",
                image_url="https://via.placeholder.com/600x400/667eea/ffffff?text=Witcher",
                client="Orbit Books",
                year=2023,
                featured=True
            ),
            Artwork(
                title="Harrow the Ninth",
                category="illustration",
                description="Book cover illustration for NYT Bestseller",
                image_url="https://via.placeholder.com/600x400/764ba2/ffffff?text=Harrow",
                client="Tor.com Publishing",
                year=2023,
                featured=True
            )
        ]
        
        # Add sample clients
        entertainment_clients = [
            Client(name="AKQA", category="Entertainment", website_url="https://www.akqa.com"),
            Client(name="Apple TV+", category="Entertainment", website_url="https://tv.apple.com"),
            Client(name="Bethesda", category="Entertainment", website_url="https://www.bethesda.net"),
            Client(name="Hi-Rez", category="Entertainment", website_url="https://www.hirezstudios.com"),
            Client(name="Paramount", category="Entertainment", website_url="https://www.paramount.com"),
            Client(name="Sony Pictures Entertainment", category="Entertainment", website_url="https://www.sonypictures.com"),
            Client(name="Sony PlayStation", category="Entertainment", website_url="https://www.playstation.com"),
            Client(name="Valve Software", category="Entertainment", website_url="https://www.valvesoftware.com"),
            Client(name="Wizards of the Coast", category="Entertainment", website_url="https://www.wizards.com")
        ]
        
        publishing_clients = [
            Client(name="Ace Books", category="Publishing", website_url="https://www.acebooks.com"),
            Client(name="Curious King", category="Publishing"),
            Client(name="DAW Books", category="Publishing", website_url="https://www.dawbooks.com"),
            Client(name="Del Rey Books", category="Publishing", website_url="https://www.delreybooks.com"),
            Client(name="Daphne Press + Illumicrate", category="Publishing"),
            Client(name="Orbit Books", category="Publishing", website_url="https://www.orbitbooks.net"),
            Client(name="Saga Press · Simon & Schuster", category="Publishing", website_url="https://www.simonandschuster.com"),
            Client(name="Subterranean Press", category="Publishing", website_url="https://www.subterraneanpress.com"),
            Client(name="Tor Books", category="Publishing", website_url="https://us.macmillan.com/torbooks"),
            Client(name="Tor.com Publishing", category="Publishing", website_url="https://www.tor.com")
        ]
        
        # Add artworks to database
        for artwork in sample_artworks:
            db.session.add(artwork)
        
        # Add clients to database
        for client in entertainment_clients + publishing_clients:
            db.session.add(client)
        
        # Commit changes
        db.session.commit()
        print("Database initialized successfully!")
        print(f"Added {len(sample_artworks)} artworks")
        print(f"Added {len(entertainment_clients + publishing_clients)} clients")

if __name__ == "__main__":
    init_database()
