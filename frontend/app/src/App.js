import React, { useEffect, useState } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

function App() {

  const build_version = process.env.REACT_APP_BUILD_VERSION || 'unknown';
  const [products, setProducts] = useState([])
  const fetchProducts = async () => {
    try {
      const response = await axios.get('/api/products')
      console.log(response.data.data)
      setProducts(response.data.data)
    } catch (err) {
      console.log('error: ', err)
    }
  }

  useEffect(() => {
    fetchProducts()
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          current build: <code>{ build_version }</code>
        </p>
        <h1>Here are my products</h1>
        {products.length > 0 ? products.map((product, i) => {
          return (
            <div className="post-container" key={ i }>
              <h5>{ product.name }</h5>
              <hr />
              <p>{ product.description }</p>
            </div>
          )
        }) : <p>No products yet, come back latter</p>}
      </header>
    </div>
  );
}

export default App;
