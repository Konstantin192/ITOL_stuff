import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import PasswordGenerator from './components/PasswordGenerator.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <PasswordGenerator />
  </StrictMode>,
)
