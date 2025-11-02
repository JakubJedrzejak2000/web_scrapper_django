Aby uruchomić projekt, należy skopiować plik .env.example i nazwać go .env. Należy uzupełnić tamtejsze wartości i potem wpisać komendę
```
docker-compose up --build
```
Projektowi powinno zająć trochę czasu włączenie i uruchomienie się, możliwe że trzeba go będzie włączyć dwa razy.

Potem, pod adresem `http://localhost:8000/article/` powinniśmy mieć wszystkie artykuły w naszej bazie danych. Scrapper uruchamia się samodzielnie, wraz z projektem w pliku docker-compose.yml w serwisie web w sekcji command.

Dostępny jest także endpoint `http://localhost:8000/article/<uuid>` z id konkretnego artykułu. Przykładowe uuid - 1a7534c5-824b-4ef9-a264-a02684ae3f95. Wyświetli on nam szczegóły dotyczące tego artykułu.

Istnieje także endpoint `http://localhost:8000/article/?source=https://google.com`, który sortuje wyniki po podanej domenie.
