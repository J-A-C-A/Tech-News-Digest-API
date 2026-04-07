====OPIS PROJEKTU====

Tech News Digest API jest to aplikacja backendowa służąca do pobierania, przechowywania oraz przeszukiwania artykułów technologicznych.

Aplikacja integruje się z zewnętrznym API (NewsAPI), zapisuje artykuły w bazie danych oraz udostępnia endpointy umożliwiające:
- przeglądanie artykułów
- wyszukiwanie artykułów różnymi metodami
- filtrowanie danych
- paginację wyników

Dane artykułu składają się z:
- id
- title
- summary
- date
- author
- source
- url

Dane tagu składają się z:
- id
- name

====FUNKCJONALNOŚCI====
- automatyczne pobieranie artykułów z zewnętrznego API
- zapisywanie danych w bazie MySQL
-zapobieganie duplikatom (unikalny URL)
- pobieranie listy artykułów z paginacją
- pobieranie pojedynczego artykułu po ID
- wyszukiwanie artykułów:
LIKE (dopasowanie tekstu)
FULLTEXT NATURAL LANGUAGE MODE
FULLTEXT BOOLEAN MODE
- relacja artykuł–tag (many-to-many)
- filtrowanie artykułów po dacie i tagach

====WYKORZYSTANE NARZĘDZIA====
- FastAPI – framework do tworzenia API
- PyDantic – walidacja danych
- Uvicorn – serwer aplikacji
- MySQL – baza danych
- mysql-connector – komunikacja z bazą danych
- APScheduler – automatyczne wykonywanie zadań (np. pobieranie artykułów)
- Enum – ograniczenie wartości parametrów (np. tryb wyszukiwania)
- Typing – adnotacje typów

====ENDPOINTY====
- pobieranie artykułów z paginacją i filtrami
- pobieranie pojedynczego artykułu
- wyszukiwanie artykułów
- pobieranie wszystkich tagów
- dodawanie tagu
- usuwanie tagu
- przypisanie tagu do artykułu

====PLIKI====
endpoints.py - zawiera definicje endpointów działających na bazie danych użytkownika
external_db.py - zawiera połączenie z News API
internal_db.py - zawiera połączenie z bazą danych użytkownika, które przechowuje pobrane z News API artykuły oraz definicje funkcji z zapytaniami SQL wykonujące operacje na bazie
schemas.py - zawiera schematy pydantic oraz enum
main.py - zawiera synchronizację danych z News API przy użyciu scheduler'a wraz z obsługą duplikatów artykułów

====URUCHOMIENIE PROJEKTU====

1. Należy pobrać wszystkie pliki z repo
2. Zainstalować wszystkie potrzebne biblioteki
3. W terminalu wpisać polecenie: uvicorn main:app --reload
4. Zostanie wyświetlony komunikat: Uvicorn running on http://127.0.0.1:8000 (podany port może się różnić)
5.Wejść w podany link z dopiskiem na końcu /docs
