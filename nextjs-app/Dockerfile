# Estágio de Build
FROM node:20 AS builder
WORKDIR /app

# Copiar e instalar dependências
COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build

EXPOSE 3000
CMD ["npm", "start"]