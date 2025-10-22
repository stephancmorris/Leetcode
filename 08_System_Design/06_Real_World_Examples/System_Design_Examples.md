# Real-World System Design Examples

## 1. URL Shortener (like bit.ly)

### Requirements
- **Functional**: Shorten long URLs, redirect to original URL
- **Non-Functional**: Handle 100M URLs, 1000:1 read/write ratio
- **Scale**: 100M URLs, 100M reads/day, 100K writes/day

### High-Level Design
```
Client → Load Balancer → Web Servers → Database
                    ↓
                Cache Layer (Redis)
```

### Key Components
- **Web Servers**: Handle shortening and redirection requests
- **Database**: Store URL mappings (MySQL/PostgreSQL)
- **Cache**: Store frequently accessed URLs (Redis)
- **Load Balancer**: Distribute traffic

### Database Schema
```sql
CREATE TABLE urls (
    id BIGINT PRIMARY KEY,
    short_url VARCHAR(10) UNIQUE,
    long_url TEXT,
    created_at TIMESTAMP,
    expires_at TIMESTAMP
);
```

### URL Generation
- **Base62 Encoding**: Use 62 characters (a-z, A-Z, 0-9)
- **Counter-Based**: Use database auto-increment counter
- **Hash-Based**: Hash long URL + counter for uniqueness

### Scaling Considerations
- **Database Sharding**: Shard by short URL hash
- **Caching**: Cache popular URLs
- **CDN**: Cache redirect responses globally

## 2. Chat System (like WhatsApp)

### Requirements
- **Functional**: Send/receive messages, group chats, online status
- **Non-Functional**: 1B users, 50M concurrent users
- **Scale**: 1B messages/day, real-time delivery

### High-Level Design
```
Mobile App → Load Balancer → API Gateway → Microservices
                                    ↓
                            Message Queue (Kafka)
                                    ↓
                            Database Cluster
```

### Key Components
- **API Gateway**: Route requests, handle authentication
- **Chat Service**: Handle message sending/receiving
- **User Service**: Manage user profiles and contacts
- **Notification Service**: Send push notifications
- **Message Queue**: Handle real-time message delivery

### Database Design
```sql
-- Users table
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    username VARCHAR(50),
    phone_number VARCHAR(20),
    created_at TIMESTAMP
);

-- Messages table
CREATE TABLE messages (
    message_id BIGINT PRIMARY KEY,
    sender_id BIGINT,
    receiver_id BIGINT,
    content TEXT,
    created_at TIMESTAMP,
    message_type ENUM('text', 'image', 'video')
);

-- Chats table
CREATE TABLE chats (
    chat_id BIGINT PRIMARY KEY,
    chat_type ENUM('private', 'group'),
    created_at TIMESTAMP
);
```

### Real-Time Communication
- **WebSockets**: Persistent connections for real-time messaging
- **Server-Sent Events**: For one-way communication
- **Message Queues**: Handle message delivery and offline messages

### Scaling Strategies
- **Horizontal Scaling**: Multiple chat service instances
- **Database Sharding**: Shard by user ID or chat ID
- **Caching**: Cache user sessions and recent messages
- **CDN**: Cache media files globally

## 3. Social Media Feed (like Twitter)

### Requirements
- **Functional**: Post tweets, follow users, view timeline
- **Non-Functional**: 300M users, 100M tweets/day
- **Scale**: 100K tweets/second, 1M timeline requests/second

### High-Level Design
```
Client → Load Balancer → API Gateway → Services
                            ↓
                    Message Queue (Kafka)
                            ↓
                    Database + Cache
```

### Key Components
- **Tweet Service**: Handle tweet creation and retrieval
- **Timeline Service**: Generate user timelines
- **User Service**: Manage user profiles and relationships
- **Media Service**: Handle image/video uploads
- **Search Service**: Full-text search capabilities

### Database Design
```sql
-- Users table
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100),
    created_at TIMESTAMP
);

-- Tweets table
CREATE TABLE tweets (
    tweet_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    content TEXT,
    created_at TIMESTAMP,
    retweet_count INT DEFAULT 0,
    like_count INT DEFAULT 0
);

-- Follows table
CREATE TABLE follows (
    follower_id BIGINT,
    following_id BIGINT,
    created_at TIMESTAMP,
    PRIMARY KEY (follower_id, following_id)
);
```

### Timeline Generation
- **Pull Model**: Fetch tweets from followed users
- **Push Model**: Pre-compute timelines for active users
- **Hybrid Model**: Push for active users, pull for inactive users

### Scaling Strategies
- **Database Sharding**: Shard by user ID
- **Caching**: Cache timelines and user data
- **CDN**: Cache media files globally
- **Message Queues**: Handle real-time updates

## 4. Video Streaming (like YouTube)

### Requirements
- **Functional**: Upload videos, stream videos, search videos
- **Non-Functional**: 1B users, 1B hours watched/day
- **Scale**: 500K uploads/day, 1M concurrent streams

### High-Level Design
```
Client → CDN → Load Balancer → API Gateway → Services
                                    ↓
                            Video Processing Pipeline
                                    ↓
                            Storage (S3) + Database
```

### Key Components
- **Upload Service**: Handle video uploads
- **Processing Service**: Transcode videos to multiple formats
- **Streaming Service**: Serve video content
- **Search Service**: Index and search video metadata
- **User Service**: Manage user accounts and subscriptions

### Video Processing Pipeline
- **Upload**: Store original video file
- **Transcoding**: Convert to multiple resolutions/formats
- **Thumbnail Generation**: Create video thumbnails
- **Metadata Extraction**: Extract video metadata
- **CDN Distribution**: Distribute processed videos

### Database Design
```sql
-- Videos table
CREATE TABLE videos (
    video_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    title VARCHAR(200),
    description TEXT,
    duration INT,
    views BIGINT DEFAULT 0,
    created_at TIMESTAMP
);

-- Video formats table
CREATE TABLE video_formats (
    video_id BIGINT,
    format VARCHAR(20),
    resolution VARCHAR(20),
    file_path VARCHAR(500),
    file_size BIGINT,
    PRIMARY KEY (video_id, format, resolution)
);
```

### Scaling Strategies
- **CDN**: Global video distribution
- **Database Sharding**: Shard by video ID or user ID
- **Caching**: Cache popular videos and metadata
- **Load Balancing**: Distribute streaming requests

## 5. E-commerce Platform (like Amazon)

### Requirements
- **Functional**: Browse products, add to cart, checkout, order tracking
- **Non-Functional**: 100M products, 1M orders/day
- **Scale**: 10M users, 100K concurrent users

### High-Level Design
```
Client → CDN → Load Balancer → API Gateway → Microservices
                                    ↓
                            Message Queue + Database
```

### Key Components
- **Product Service**: Manage product catalog
- **User Service**: Handle user accounts and authentication
- **Cart Service**: Manage shopping carts
- **Order Service**: Process orders and payments
- **Inventory Service**: Track product availability
- **Recommendation Service**: Suggest products

### Database Design
```sql
-- Products table
CREATE TABLE products (
    product_id BIGINT PRIMARY KEY,
    name VARCHAR(200),
    description TEXT,
    price DECIMAL(10,2),
    category_id BIGINT,
    stock_quantity INT,
    created_at TIMESTAMP
);

-- Orders table
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    total_amount DECIMAL(10,2),
    status ENUM('pending', 'confirmed', 'shipped', 'delivered'),
    created_at TIMESTAMP
);

-- Order items table
CREATE TABLE order_items (
    order_id BIGINT,
    product_id BIGINT,
    quantity INT,
    price DECIMAL(10,2),
    PRIMARY KEY (order_id, product_id)
);
```

### Key Features
- **Product Search**: Full-text search with filters
- **Shopping Cart**: Persistent cart across sessions
- **Payment Processing**: Secure payment handling
- **Order Tracking**: Real-time order status updates
- **Recommendations**: Personalized product suggestions

### Scaling Strategies
- **Database Sharding**: Shard by user ID or product ID
- **Caching**: Cache product data and user sessions
- **CDN**: Cache product images globally
- **Message Queues**: Handle asynchronous order processing

## 6. Ride-Sharing Service (like Uber)

### Requirements
- **Functional**: Request rides, match drivers, track rides, payments
- **Non-Functional**: 1M rides/day, real-time matching
- **Scale**: 100K concurrent users, 50K active drivers

### High-Level Design
```
Mobile App → Load Balancer → API Gateway → Microservices
                                    ↓
                            Real-time Processing + Database
```

### Key Components
- **Ride Service**: Handle ride requests and matching
- **Driver Service**: Manage driver locations and availability
- **Payment Service**: Process payments and billing
- **Notification Service**: Send real-time updates
- **Location Service**: Track real-time locations

### Database Design
```sql
-- Users table
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    created_at TIMESTAMP
);

-- Drivers table
CREATE TABLE drivers (
    driver_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    vehicle_info JSON,
    is_available BOOLEAN,
    current_location POINT,
    updated_at TIMESTAMP
);

-- Rides table
CREATE TABLE rides (
    ride_id BIGINT PRIMARY KEY,
    rider_id BIGINT,
    driver_id BIGINT,
    pickup_location POINT,
    dropoff_location POINT,
    status ENUM('requested', 'matched', 'picked_up', 'completed'),
    created_at TIMESTAMP
);
```

### Real-Time Features
- **Location Tracking**: Real-time GPS tracking
- **Driver Matching**: Match riders with nearby drivers
- **Live Updates**: Real-time ride status updates
- **Dynamic Pricing**: Adjust prices based on demand

### Scaling Strategies
- **Geographic Sharding**: Shard by geographic regions
- **Caching**: Cache driver locations and ride data
- **Message Queues**: Handle real-time location updates
- **Load Balancing**: Distribute requests across regions

## Common Patterns Across Examples

### 1. Microservices Architecture
- **Service Decomposition**: Break monolith into services
- **API Gateway**: Single entry point for clients
- **Service Discovery**: Dynamic service location
- **Inter-Service Communication**: REST APIs, message queues

### 2. Data Management
- **Database Sharding**: Horizontal data partitioning
- **Caching**: Multiple levels of caching
- **CDN**: Global content distribution
- **Data Replication**: High availability and performance

### 3. Real-Time Features
- **WebSockets**: Persistent connections
- **Message Queues**: Asynchronous processing
- **Event Streaming**: Real-time data processing
- **Push Notifications**: Real-time user updates

### 4. Scalability Patterns
- **Horizontal Scaling**: Add more servers
- **Load Balancing**: Distribute traffic
- **Auto-Scaling**: Automatic resource management
- **Caching**: Reduce database load
