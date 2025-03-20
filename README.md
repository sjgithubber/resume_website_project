```mermaid
flowchart TD
    subgraph "User Interaction"
        A[User] -->|Requests website| B[Domain Name]
    end

    subgraph "DNS Layer"
        B -->|Points to| C[DNS Records]
    end

    subgraph "Web Hosting"
        C -->|Directs to| D[Hosting Provider]
        D -->|Runs| E[Django Application]
    end

    subgraph "Database Layer"
        E -->|Connects to| F[Supabase]
        F -->|Stores data in| G[PostgreSQL]
    end

    subgraph "Additional Services"
        F -->|Provides| H[Authentication]
        F -->|Provides| I[Storage]
        F -->|Provides| J[Real-time subscriptions]
    end

    E -->|Processes request| K[Response]
    K -->|Returns to| A

    style E fill:#4B8BBE,stroke:#306998,color:white
    style F fill:#3ECF8E,stroke:#24A06B,color:white
    style G fill:#336791,stroke:#264D71,color:white
