# System Design Fundamentals

## What is System Design?

System design is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements. It's about designing large-scale distributed systems that can handle millions of users.

## Key Principles

### 1. Scalability
- **Horizontal Scaling**: Adding more machines/servers
- **Vertical Scaling**: Adding more power (CPU, RAM) to existing machines
- **Load Balancing**: Distributing traffic across multiple servers

### 2. Reliability
- **Fault Tolerance**: System continues operating despite component failures
- **Redundancy**: Having backup components
- **Monitoring**: Continuous system health checks

### 3. Availability
- **Uptime**: Percentage of time system is operational
- **SLA (Service Level Agreement)**: Guaranteed uptime percentage
- **MTBF/MTTR**: Mean Time Between Failures / Mean Time To Repair

### 4. Performance
- **Latency**: Time taken for a request to complete
- **Throughput**: Number of requests processed per unit time
- **Response Time**: Time from request to response

### 5. Consistency
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition tolerance
- **Eventual Consistency**: System becomes consistent over time

## Design Process

### 1. Requirements Gathering
- **Functional Requirements**: What the system should do
- **Non-Functional Requirements**: Performance, scalability, reliability
- **Scale Requirements**: Users, requests per second, data volume

### 2. Capacity Estimation
- **Traffic Estimates**: Requests per second, concurrent users
- **Storage Requirements**: Data volume, growth rate
- **Bandwidth Requirements**: Data transfer needs

### 3. High-Level Design
- **System Architecture**: Overall structure and components
- **API Design**: Interface definitions
- **Database Schema**: Data organization

### 4. Detailed Design
- **Component Design**: Individual service specifications
- **Data Flow**: How data moves through the system
- **Error Handling**: Failure scenarios and recovery

### 5. Scaling and Optimization
- **Bottleneck Identification**: Performance limiting factors
- **Optimization Strategies**: Caching, indexing, partitioning
- **Monitoring and Metrics**: System health tracking

## Common Design Patterns

### 1. Microservices Architecture
- **Service Decomposition**: Breaking monolith into services
- **Service Communication**: Inter-service messaging
- **Service Discovery**: Finding and connecting to services

### 2. Event-Driven Architecture
- **Event Sourcing**: Storing events instead of state
- **CQRS**: Command Query Responsibility Segregation
- **Message Queues**: Asynchronous communication

### 3. Caching Strategies
- **Cache-Aside**: Application manages cache
- **Write-Through**: Write to cache and database simultaneously
- **Write-Behind**: Write to cache, batch write to database

### 4. Database Patterns
- **Master-Slave Replication**: Read replicas
- **Sharding**: Horizontal data partitioning
- **Denormalization**: Trading storage for query performance

## Interview Tips

### 1. Start with Requirements
- Clarify functional and non-functional requirements
- Ask about scale (users, requests, data)
- Understand constraints and assumptions

### 2. Think Out Loud
- Explain your reasoning process
- Discuss trade-offs and alternatives
- Consider edge cases and failure scenarios

### 3. Use Diagrams
- Draw system architecture diagrams
- Show data flow and component interactions
- Illustrate scaling strategies

### 4. Be Practical
- Consider real-world constraints
- Discuss implementation challenges
- Mention monitoring and maintenance

## Key Metrics to Track

### Performance Metrics
- **Response Time**: P50, P95, P99 latencies
- **Throughput**: Requests per second
- **Error Rate**: Percentage of failed requests

### Business Metrics
- **User Engagement**: DAU, MAU, session duration
- **Conversion Rate**: User actions completion
- **Revenue**: Business impact metrics

### Infrastructure Metrics
- **CPU Utilization**: Server resource usage
- **Memory Usage**: RAM consumption
- **Network I/O**: Bandwidth utilization
- **Disk I/O**: Storage performance
