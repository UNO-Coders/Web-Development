import React, { useContext } from "react"
import { motion } from "framer-motion"
import { Context } from "../Context"
import { container, item } from "../Animations/formAnimations"

const Modal = ({ text }) => {
  const { setModal } = useContext(Context)
  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="visible"
      exit={{ opacity: 0, scale: 0 }}
      className="w-[100vw] h-[100vh] fixed inset-0 backdrop-blur-sm flex items-center justify-center"
    >
      <motion.div className="w-[500px] h-[300px] bg-[#f5f5d5] shadow-custom rounded-lg p-3">
        <motion.div
          variants={item}
          onClick={() => setModal(false)}
          className="w-full text-right"
        >
          <i className="fa-regular fa-circle-xmark text-4xl cursor-pointer text-[#3b3a30] opacity-50 hover:opacity-100 duration-300"></i>
        </motion.div>
        <div className="w-full h-[70%] flex flex-col justify-center items-center text-[#3b3a30]">
          <motion.h1 variants={item} className="mb-6 text-2xl font-bold">
            {text}
          </motion.h1>
          <motion.i
            variants={item}
            className="fa-solid fa-user-check text-3xl"
          ></motion.i>
        </div>
      </motion.div>
    </motion.div>
  )
}

export default Modal
