FROM node:12.6.0 as react-build

WORKDIR /frontend

COPY react-frontend /frontend

RUN echo "REACT_APP_BUILD_VERSION=0.0.1" > /frontend/.env
RUN echo "REACT_APP_BUILD_VERSION_TEST=$BUILD_VERSION" > /frontend/.env
RUN yarn
RUN yarn build


FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/
COPY --from=react-build /frontend/build /var/www/html/build/
