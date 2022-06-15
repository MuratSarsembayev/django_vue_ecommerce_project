FROM node:16-alpine3.12 AS build

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json ./
RUN npm i --silent
RUN npm install react-scripts@3.4.1 -g --silent
COPY . ./
# ENV REACT_APP_HOST_IP_ADDRESS $API_URL
RUN npm run build


FROM nginx:1.21.6-alpine AS prod
RUN  apk update \
  && apk add wget \
  && rm -rf /var/lib/apt/lists/*
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/nginx.conf /etc/nginx/conf.d/default.conf:ro
COPY --from=build /app/dist /usr/share/nginx/html


