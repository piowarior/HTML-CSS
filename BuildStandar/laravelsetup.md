
> 👉 **SETUP ENVIRONMENT → BARU INSTALL LARAVEL → BARU CONFIG API + REALTIME**


---

# 🚀 ROADMAP SETUP PROJECT (STEP BY STEP)

```
1️⃣ Setup Docker *** (cuman setup ini saja) ***
2️⃣ Buat Project Laravel 12 *** (cuman setup ini saja) ***
3️⃣ Setup Database
4️⃣ Setup API Auth
5️⃣ Setup Realtime
6️⃣ Setup React
```

Sekarang kita mulai dari:

# ✅ STEP 1 — SETUP DOCKER (WAJIB DULU)

---

# 🐳 Struktur Folder Project

Bikin folder project:

```bash
mkdir servesync
cd servesync
```

Struktur:

```
servesync/
 ├── backend/   (Laravel)
 ├── frontend/  (React)
 └── docker/
```

---

# 🐳 Buat File docker-compose.yml

Di folder `servesync/`:

```bash
touch docker-compose.yml
```

Isi:

```yaml
version: '3.8'

services:

  app:
    image: php:8.3-fpm
    container_name: servesync_app
    working_dir: /var/www
    volumes:
      - ./backend:/var/www
    depends_on:
      - db
    networks:
      - servesync

  web:
    image: nginx:alpine
    container_name: servesync_nginx
    ports:
      - "8000:80"
    volumes:
      - ./backend:/var/www
      - ./docker/nginx:/etc/nginx/conf.d
    depends_on:
      - app
    networks:
      - servesync

  db:
    image: mysql:8.0
    container_name: servesync_db
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: servesync
      MYSQL_USER: servesync
      MYSQL_PASSWORD: secret
    ports:
      - "3307:3306"
    volumes:
      - dbdata:/var/lib/mysql
    networks:
      - servesync

  redis:
    image: redis:alpine
    container_name: servesync_redis
    ports:
      - "6379:6379"
    networks:
      - servesync

networks:
  servesync:

volumes:
  dbdata:
```

---

# 🧱 Buat Config NGINX

```bash
mkdir -p docker/nginx
touch docker/nginx/default.conf
```

Isi:

```nginx
server {
    listen 80;
    index index.php index.html;
    root /var/www/public;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        fastcgi_pass app:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        fastcgi_param DOCUMENT_ROOT $realpath_root;
    }
}
```

---

# 🟢 Jalankan Docker

```bash
docker compose up -d
```

Kalau sukses:

```bash
docker ps
```

Harus muncul:

```
servesync_app
servesync_nginx
servesync_db
servesync_redis
```

---

# ✅ STEP 2 — INSTALL LARAVEL 12 DI DOCKER

```bash
docker compose exec app bash
```

Masuk container, lalu:

```bash
composer create-project laravel/laravel:^12.0 .
```

---

# ⚙️ Setup ENV Database

Edit `.env`:

```env
DB_CONNECTION=mysql
DB_HOST=db
DB_PORT=3306
DB_DATABASE=servesync
DB_USERNAME=servesync
DB_PASSWORD=secret
```

---

# 🔄 Migrate

```bash
php artisan migrate
```

---

# ✅ Kasih IZIN Permision 

- chmod 755 storage
- chown -R www-data:www-data storage bootstrap/cache


---


# 🌐 TEST

Buka:

```
http://localhost:8000
```

Kalau muncul **Laravel 12 page** → ✅ SUKSES

