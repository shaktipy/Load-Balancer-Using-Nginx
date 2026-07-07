# Dockerized Microservices Load Balancer using Nginx

A practical DevOps project that demonstrates **Load Balancing**, **Microservices Architecture**, and **Containerization** using Docker, Nginx, and Python Flask.

---

## Architecture

```
             Browser (Client)
                    │
                    ▼
         ┌─────────────────┐
         │      Nginx      │  ← Reverse Proxy / Load Balancer
         │   (Port 80)     │     Distributes traffic using Round Robin
         └─────────────────┘
           │    │    │    │
           ▼    ▼    ▼    ▼
        Flask Flask Flask Flask
         App1  App2  App3  App4   ← 4 Identical containers, each with a unique SERVER_ID
```

---

## Features

- **Nginx Reverse Proxy** — Acts as the single entry point. All browser traffic goes through it.
- **Round Robin Load Balancing** — Nginx distributes requests sequentially across all 4 Flask servers.
- **Least Connections** — Can be enabled with one line change in `nginx/nginx.conf`.
- **High Availability** — If one container goes down, Nginx automatically skips it and routes to healthy ones.
- **Docker Compose** — Entire 5-container stack starts with a single command.
- **Interactive 3D Dashboard** — Isometric UI showing live traffic flow, server hit counts, and request logs.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.9, Flask |
| Load Balancer | Nginx |
| Containerization | Docker, Docker Compose |
| Frontend | HTML, CSS (3D Isometric), Vanilla JS |

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

---

## Setup & Run

```bash
# 1. Clone this repository
git clone <your-repo-url>
cd Load-Balancer-Demo

# 2. Build images and start all 5 containers in detached mode
docker compose up --build -d

# 3. Open your browser and visit:
#    http://localhost
```

Refresh the page multiple times — you will see the **server badge cycle** through Server 1 → Server 2 → Server 3 → Server 4, proving Round Robin is working.

---

## Testing Load Balancing (Interactive Dashboard)

The UI has a built-in traffic generator:
- **Send Single Request** — fires one request and highlights the server that responded.
- **Continuous Traffic Mode** — auto-fires requests every second, so you can watch the rotation live.
- **Reset Scoreboard** — clears session counters.

---

## Testing High Availability

```bash
# Stop one backend container
docker stop load-balancer-demo-app2-1

# Keep refreshing http://localhost — Server 2 will no longer appear.
# Nginx automatically routes to the remaining 3 healthy servers.

# Bring it back
docker start load-balancer-demo-app2-1
```

---

## Switching to Least Connections Algorithm

By default, Nginx uses **Round Robin**. To switch to **Least Connections** (routes to the server with fewest active connections):

1. Open `nginx/nginx.conf`
2. Find the `upstream flask_servers {` block
3. Uncomment `# least_conn;` → `least_conn;`
4. Restart Nginx: `docker compose restart nginx`

---

## Useful Commands

```bash
# Check running containers
docker compose ps

# View logs of a specific service
docker compose logs app1

# Stop all containers
docker compose down

# Rebuild after code changes
docker compose up --build -d
```
