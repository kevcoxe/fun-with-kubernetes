FROM node:8.6.0

ADD ./app /app

WORKDIR /app

EXPOSE 3000

ENV REACT_APP_BUILD_VERSION=0.0.10

RUN yarn install
RUN yarn

CMD ["yarn", "start"]

