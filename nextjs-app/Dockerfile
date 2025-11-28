FROM node:20

WORKDIR /app

COPY package.json .
# Só copie o lock se existir
# COPY package-lock.json .

RUN npm install

COPY . .

EXPOSE 3000
CMD ["npm", "run", "dev"]