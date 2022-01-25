FROM node:9-slim
WORKDIR /app
COPY package.json /app
RUN npm install --save express
COPY . /app
CMD ["npm", "start"]
EXPOSE 8080