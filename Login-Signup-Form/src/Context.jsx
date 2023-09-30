import React, { createContext, useState } from "react"

const Context = createContext()

const ContextProvider = ({ children }) => {
  const [modal, setModal] = useState(false)
  const [isLoading, setIsLoading] = useState(false)

  const signupOrLogin = () => {
    setModal(true)
  }
  return (
    <Context.Provider value={{ modal, setModal, signupOrLogin }}>
      {children}
    </Context.Provider>
  )
}

export { Context, ContextProvider }
