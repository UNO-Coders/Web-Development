import { motion, AnimatePresence } from "framer-motion"
import React, { useState, useContext } from "react"
import { Link } from "react-router-dom"
import { container, item } from "../Animations/formAnimations"
import { Context } from "../Context"
import Modal from "./Modal"

const Signup = () => {
  const { modal, setModal, signupOrLogin } = useContext(Context)
  const [signupInfo, setSignupInfo] = useState({
    email: "",
    password: "",
  })

  const handleChange = (event) => {
    const { name, value } = event.target
    setSignupInfo((prev) => ({
      ...prev,
      [name]: value,
    }))
  }

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="visible"
      className="w-[400px] h-[500px] rounded-lg shadow-custom relative"
    >
      <div className="w-full h-full p-6 flex flex-col items-center justify-between">
        <motion.h1
          variants={item}
          className="text-[#f5f5d5] font-bold text-3xl"
        >
          Sign Up
        </motion.h1>
        <div className="w-full h-[50%] rounded-lg flex flex-col items-center justify-between">
          <motion.div className="w-full" variants={item}>
            <input
              type="text"
              onChange={handleChange}
              name="email"
              placeholder="Email..."
              className="w-full opacity-50 hover:opacity-100 duration-300 focus:opacity-100 p-4 mb-3 rounded-lg outline-none bg-transparent border-2 border-[#f5f5d5] placeholder:text-[#f5f5d5] text-[#f5f5d5]"
            />
          </motion.div>
          <motion.div className="w-full" variants={item}>
            <input
              type="password"
              onChange={handleChange}
              name="password"
              placeholder="Password..."
              className="w-full opacity-50 hover:opacity-100 duration-300 focus:opacity-100 p-4 mb-3 rounded-lg outline-none bg-transparent border-2 border-[#f5f5d5] placeholder:text-[#f5f5d5] text-[#f5f5d5]"
            />
          </motion.div>
          <motion.div className="w-full" variants={item}>
            <button
              onClick={signupOrLogin}
              className="w-full opacity-50 hover:opacity-100 duration-300 rounded-lg p-4 border-2 border-[#f5f5d5] text-[#f5f5d5]"
            >
              Sign Up
            </button>
          </motion.div>
        </div>
        <motion.div variants={item} className="w-full">
          <p className="text-center text-[#f5f5d5]">
            Already have an Account?{" "}
            <Link
              to="/login"
              className="underline underline-offset-2 cursor-pointer opacity-50 hover:opacity-100 duration-300"
            >
              Login here.
            </Link>
          </p>
        </motion.div>
      </div>
      <AnimatePresence>
        {modal && <Modal text="Successfully signed up!" />}
      </AnimatePresence>
    </motion.div>
  )
}

export default Signup
