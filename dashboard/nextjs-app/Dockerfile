# Estágio de Build
FROM node:20 AS builder
WORKDIR /app

# Copiar e instalar dependências
COPY package.json package-lock.json ./
RUN npm install --legacy-peer-deps

# Copiar o código fonte e buildar
COPY . .
RUN npm run build

# Estágio de Produção (Imagem menor)
FROM node:20-slim
WORKDIR /app

# Configurar o usuário não-root (boa prática)
ENV NODE_ENV production

# Copiar arquivos de produção e Next.js build
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY package.json ./

EXPOSE 3000

# Comando de execução
CMD ["npm", "start"]