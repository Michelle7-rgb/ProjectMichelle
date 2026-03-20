const main = document.getElementById("mainContent");
const themeToggle = document.getElementById("themeToggle");
const collapseBtn = document.getElementById("collapseBtn");
const sidebar = document.getElementById("sidebar");
const navLinks = document.querySelectorAll("nav a");

const baseTemplate = ({ title, subtitle, badge, content }) => `
<section class="view">
    <header class="view-head">
        <div>
            <h2>${title}</h2>
            <p>${subtitle}</p>
        </div>
        ${badge ? `<span class="badge">${badge}</span>` : ""}
    </header>
    ${content}
</section>
`;

const views = {
    "owner-listings": () =>
        baseTemplate({
            title: "Dashboard Propriétaire",
            subtitle: "Suivi de vos biens, performances et statut de publication.",
            badge: "Mise à jour aujourd'hui",
            content: `
            <div class="cards">
                <article class="card">
                    <p class="card-label">Total annonces</p>
                    <p class="card-value">12</p>
                    <p class="card-trend">+2 ce mois-ci</p>
                </article>
                <article class="card">
                    <p class="card-label">Validées</p>
                    <p class="card-value">8</p>
                    <p class="card-trend">Taux de validation 67%</p>
                </article>
                <article class="card">
                    <p class="card-label">En attente</p>
                    <p class="card-value">4</p>
                    <p class="card-trend">Action requise</p>
                </article>
                <article class="card">
                    <p class="card-label">Taux de contact</p>
                    <p class="card-value">64%</p>
                    <p class="card-trend">+8% sur 30 jours</p>
                </article>
            </div>

            <div class="dashboard-grid">
                <div class="panel">
                    <p class="panel-title">Annonces récentes</p>
                    <table>
                        <thead>
                            <tr>
                                <th>Image</th>
                                <th>Titre</th>
                                <th>Statut</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><img class="thumb" src="https://picsum.photos/seed/immo-1/120/80" alt="Appartement"></td>
                                <td>Appartement Douala</td>
                                <td><span class="status success">Validé</span></td>
                                <td>
                                    <div class="btn-row">
                                        <button>Modifier</button>
                                        <button class="btn-secondary">Supprimer</button>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td><img class="thumb" src="https://picsum.photos/seed/immo-2/120/80" alt="Studio"></td>
                                <td>Studio Bepanda</td>
                                <td><span class="status warning">En attente</span></td>
                                <td>
                                    <div class="btn-row">
                                        <button>Modifier</button>
                                        <button class="btn-secondary">Supprimer</button>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td><img class="thumb" src="https://picsum.photos/seed/immo-8/120/80" alt="Maison"></td>
                                <td>Maison Makepe</td>
                                <td><span class="status success">Validé</span></td>
                                <td>
                                    <div class="btn-row">
                                        <button>Modifier</button>
                                        <button class="btn-secondary">Supprimer</button>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="stack">
                    <div class="panel">
                        <p class="panel-title">Priorités du jour</p>
                        <div class="panel-body">
                            <ul class="list-clean">
                                <li class="list-item">
                                    <span>Valider les photos en attente</span>
                                    <span class="list-meta">2</span>
                                </li>
                                <li class="list-item">
                                    <span>Répondre aux demandes</span>
                                    <span class="list-meta">5</span>
                                </li>
                                <li class="list-item">
                                    <span>Mettre à jour les prix</span>
                                    <span class="list-meta">1</span>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div class="panel">
                        <p class="panel-title">Actions rapides</p>
                        <div class="panel-body">
                            <div class="btn-row">
                                <button>Nouvelle annonce</button>
                                <button class="btn-secondary">Exporter</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <section class="feed-section">
                <div class="feed-section-head">
                    <h3>Fil d'actualité immobilier</h3>
                    <p>Nouveautés des biens publiés aujourd'hui</p>
                </div>

                <div class="feed-grid">
                    <div class="feed-list">
                        <article class="feed-post panel">
                            <div class="feed-post-head">
                                <div class="feed-author-avatar">AD</div>
                                <div>
                                    <p class="feed-author">Agence Delta</p>
                                    <p class="feed-time">Il y a 12 min · Douala, Akwa</p>
                                </div>
                            </div>
                            <p class="feed-text">Nouveau 3 pièces lumineux avec parking sécurisé et gardiennage 24/7. Visites disponibles dès demain.</p>
                            <img class="feed-image" src="https://picsum.photos/seed/feed-immo-1/1100/560" alt="Appartement moderne">
                            <div class="feed-actions">
                                <button class="btn-secondary" type="button">👍 Intéressé (24)</button>
                                <button class="btn-secondary" type="button">💬 Commenter (8)</button>
                                <button class="btn-secondary" type="button">↗ Partager</button>
                            </div>
                        </article>

                        <article class="feed-post panel">
                            <div class="feed-post-head">
                                <div class="feed-author-avatar">IM</div>
                                <div>
                                    <p class="feed-author">IMMOPlus</p>
                                    <p class="feed-time">Il y a 38 min · Yaoundé, Bastos</p>
                                </div>
                            </div>
                            <p class="feed-text">Studio meublé premium, internet inclus, proche des axes principaux. Offre spéciale pour signature avant fin de semaine.</p>
                            <img class="feed-image" src="https://picsum.photos/seed/feed-immo-2/1100/560" alt="Studio meublé">
                            <div class="feed-actions">
                                <button class="btn-secondary" type="button">👍 Intéressé (17)</button>
                                <button class="btn-secondary" type="button">💬 Commenter (5)</button>
                                <button class="btn-secondary" type="button">↗ Partager</button>
                            </div>
                        </article>
                    </div>

                    <aside class="feed-side stack">
                        <div class="panel">
                            <p class="panel-title">Tendances recherches</p>
                            <div class="panel-body">
                                <ul class="list-clean">
                                    <li class="list-item"><span>Studios meublés</span><span class="list-meta">+22%</span></li>
                                    <li class="list-item"><span>Douala centre</span><span class="list-meta">+17%</span></li>
                                    <li class="list-item"><span>2 chambres</span><span class="list-meta">+14%</span></li>
                                </ul>
                            </div>
                        </div>

                        <div class="panel">
                            <p class="panel-title">Astuce publication</p>
                            <div class="panel-body">
                                <p class="list-meta">Ajoute 5 à 8 photos lumineuses et une description orientée quartier pour augmenter les prises de contact.</p>
                            </div>
                        </div>
                    </aside>
                </div>
            </section>
            `
        }),

    "owner-publish": () =>
        baseTemplate({
            title: "Publier une annonce",
            subtitle: "Créez une fiche complète pour augmenter votre visibilité.",
            badge: "Brouillon",
            content: `
            <div class="panel" style="padding:16px;">
                <form class="form-grid">
                    <div class="field">
                        <label>Titre</label>
                        <input type="text" placeholder="Appartement moderne à Akwa">
                    </div>
                    <div class="field">
                        <label>Type de bien</label>
                        <select>
                            <option>Appartement</option>
                            <option>Studio</option>
                            <option>Maison</option>
                        </select>
                    </div>
                    <div class="field">
                        <label>Prix mensuel (FCFA)</label>
                        <input type="number" placeholder="150000">
                    </div>
                    <div class="field">
                        <label>Localisation</label>
                        <input type="text" placeholder="Douala, Bonamoussadi">
                    </div>
                    <div class="field" style="grid-column: 1 / -1;">
                        <label>Description</label>
                        <textarea placeholder="Décrivez les points forts du bien..."></textarea>
                    </div>
                </form>
                <div class="btn-row" style="margin-top: 12px;">
                    <button type="button">Publier</button>
                    <button type="button" class="btn-secondary">Enregistrer le brouillon</button>
                </div>
            </div>
            `
        }),

    "tenant-profile": () =>
        baseTemplate({
            title: "Profil Locataire",
            subtitle: "Gardez vos informations à jour pour accélérer vos candidatures.",
            badge: "Profil vérifié",
            content: `
            <div class="cards">
                <article class="card"><p class="card-label">Dossiers envoyés</p><p class="card-value">7</p></article>
                <article class="card"><p class="card-label">Réponses reçues</p><p class="card-value">4</p></article>
                <article class="card"><p class="card-label">Messages non lus</p><p class="card-value">3</p></article>
            </div>
            `
        }),

    "tenant-favorites": () =>
        baseTemplate({
            title: "Mes favoris",
            subtitle: "Retrouvez les biens sauvegardés et suivez leur disponibilité.",
            badge: "5 biens",
            content: `
            <div class="panel">
                <table>
                    <thead>
                        <tr>
                            <th>Bien</th>
                            <th>Zone</th>
                            <th>Prix</th>
                            <th>Statut</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Loft Akwa</td>
                            <td>Douala</td>
                            <td>220 000 FCFA</td>
                            <td><span class="status success">Disponible</span></td>
                        </tr>
                        <tr>
                            <td>Studio Melen</td>
                            <td>Yaoundé</td>
                            <td>95 000 FCFA</td>
                            <td><span class="status warning">Très demandé</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            `
        }),

    "admin-review": () =>
        baseTemplate({
            title: "Dashboard Admin",
            subtitle: "Validation et modération des annonces en attente.",
            badge: "2 en attente",
            content: `
            <div class="panel">
                <table>
                    <thead>
                        <tr>
                            <th>Image</th>
                            <th>Titre</th>
                            <th>Propriétaire</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><img class="thumb" src="https://picsum.photos/seed/immo-3/120/80" alt="Annonce"></td>
                            <td>Studio Yaoundé</td>
                            <td>Jean N.</td>
                            <td>
                                <div class="btn-row">
                                    <button>Valider</button>
                                    <button class="btn-secondary">Refuser</button>
                                    <button class="btn-secondary">Supprimer</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            `
        }),

    messages: () =>
        baseTemplate({
            title: "Messagerie",
            subtitle: "Échangez rapidement entre propriétaires, locataires et administration.",
            badge: "2 conversations actives",
            content: `
            <div class="messages-container">
                <aside class="conversations">
                    <p class="conversations-head">Conversations</p>
                    <div class="conversation-item active">Jean (Propriétaire)</div>
                    <div class="conversation-item">Marie (Locataire)</div>
                    <div class="conversation-item">Support Admin</div>
                </aside>
                <section class="chat">
                    <div class="chat-head">Discussion avec Jean (Propriétaire)</div>
                    <div class="chat-messages" id="chatMessages">
                        <div class="message received">Bonjour, le bien est-il toujours disponible ?</div>
                    </div>
                    <form class="chat-input" id="chatForm">
                        <input type="text" id="msgInput" placeholder="Écrire un message...">
                        <button type="submit">Envoyer</button>
                    </form>
                </section>
            </div>
            `
        })
};

/* ================= THEME ================= */

if(localStorage.getItem("theme") === "dark"){
    document.body.classList.add("dark");
}

themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    localStorage.setItem("theme",
        document.body.classList.contains("dark") ? "dark" : "light"
    );
    themeToggle.textContent = document.body.classList.contains("dark") ? "☀️" : "🌙";
});

themeToggle.textContent = document.body.classList.contains("dark") ? "☀️" : "🌙";

/* =============== SIDEBAR COLLAPSE =============== */

collapseBtn.addEventListener("click", () => {
    sidebar.classList.toggle("collapsed");
});

/* ================= VIEWS ================= */

document.querySelectorAll("nav a").forEach(link => {
    link.addEventListener("click", (e)=>{
        e.preventDefault();
        loadView(link.dataset.view);
    });
});

function loadView(view){
    const renderer = views[view] || views["owner-listings"];
    main.innerHTML = renderer();

    navLinks.forEach((link) => {
        link.classList.toggle("active", link.dataset.view === view);
    });
}

/* ================= MESSAGE ================= */

function sendMessage(){
    const input = document.getElementById("msgInput");
    const chat = document.getElementById("chatMessages");

    if(input.value.trim() !== ""){
        const msg = document.createElement("div");
        msg.classList.add("message","sent");
        msg.innerText = input.value;
        chat.appendChild(msg);
        input.value = "";
        chat.scrollTop = chat.scrollHeight;
    }
}

document.addEventListener("submit", (event) => {
    if(event.target && event.target.id === "chatForm"){
        event.preventDefault();
        sendMessage();
    }
});

loadView("owner-listings");
