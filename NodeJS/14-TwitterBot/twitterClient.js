const { TwitterApi } = require("twitter-api-v2");

// All the Credentilas Will be Available in The Twitter Developer Website

const client = new TwitterApi({
    appKey: "Enter API key",
    appSecret: "Enter Secret Key",
    accessToken: "Enter Access Token",
    accessSecret: "Enter Access Secret"
})

const rwClient = client.readWrite
ss

module.exports = rwClient;