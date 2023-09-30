import React from "react"
import { Routes, Route } from "react-router-dom"
import Login from "./Components/Login"
import Signup from "./Components/Signup"

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Signup />} />
      <Route path="/login" element={<Login />} />
    </Routes>
  )
}

export default App
