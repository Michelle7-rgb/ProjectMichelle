# Changements appliqués

## Ce qui a été corrigé
- Le projet est passé sur des réglages plus proches de la production: `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`, `TIME_ZONE`, `LANGUAGE_CODE` et les URLs de login sont maintenant mieux cadrés.
- Les favoris ont été unifiés sur l'app `favoris`, qui est désormais la seule source utilisée par le feed, le dashboard locataire et la page des favoris.
- La messagerie a été réalignée avec le vrai modèle `User` via une migration corrective `message.0002_fix_user_foreign_keys`.
- Les pages de dashboard, le feed, la messagerie et les favoris affichent maintenant des données réelles ou des états vides, au lieu de compteurs et contenus figés.
- Le doublon de modèle `Favoris` dans `appartement` a été retiré pour éviter les conflits et la confusion métier.
- Les écrans publics et internes qui donnaient une impression de démo ont été réécrits pour rester cohérents avec les données en base.

## Pourquoi ces changements
- Une application Django devient vite fragile quand plusieurs apps portent la même responsabilité métier. Unifier les favoris évite les bugs de relation et les incohérences entre templates et ORM.
- Les données fictives dans une UI de production créent des attentes fausses et cachent les vrais problèmes de flux. Les remplacer par des requêtes réelles permet de voir immédiatement ce qui existe vraiment en base.
- Les settings prod sont essentiels même en phase de développement local, car ils obligent à penser sécurité et déploiement propre dès le départ.
- La messagerie avait un problème structurel dans ses migrations. Corriger seulement les vues n’aurait pas suffi: il fallait aussi réaligner la base.

## Points techniques utiles
- Le dashboard locataire et le feed utilisent maintenant `select_related` / `prefetch_related` pour limiter le nombre de requêtes SQL.
- Les vues sensibles sont protégées avec `login_required`, ce qui évite l’accès public à des écrans de gestion.
- La page de messagerie ne simule plus une saisie JS locale. Le flux passe désormais par les vraies vues Django.

## Conseils Django pour un niveau intermédiaire
- Centralise la logique métier dans les vues ou des services légers, pas dans les templates.
- Garde une seule source de vérité pour chaque concept métier. Ici, un seul modèle `Favoris` suffisait.
- Quand un template affiche des chiffres fixes, demande-toi immédiatement d’où ils viennent en base. Si la réponse est “nulle part”, remplace-les.
- Utilise `select_related` pour les ForeignKey et `prefetch_related` pour les relations inverses ou many-to-many.
- Vérifie toujours `manage.py check` et `showmigrations` après une refonte structurelle.
- Si une migration historique est cassée, corrige-la proprement avec une migration de rattrapage plutôt que de bricoler les vues.
- En production, lis les valeurs sensibles depuis les variables d’environnement.

## Prochaines améliorations recommandées
- Ajouter des formulaires Django pour la création et la modification d'appartements au lieu de lire directement `request.POST`.
- Introduire un vrai statut de modération pour les annonces si tu veux un workflow admin complet.
- Ajouter des tests sur les vues principales: feed, favoris, conversation et dashboards.
- Remplacer les derniers tableaux de démonstration restants par des indicateurs calculés si tu veux aller jusqu'à une vraie dashboard analytics.
