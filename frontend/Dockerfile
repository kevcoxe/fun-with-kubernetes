FROM node:12.6.0 as react-build

WORKDIR /frontend

COPY react-frontend /frontend
COPY run.sh /frontend/

ENV REACT_APP_BUILD_VERSION=0.0.7

RUN yarn
RUN yarn build


FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/
COPY --from=react-build /frontend/build /var/www/html/build/
