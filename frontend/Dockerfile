# Use official Node.js image as the base image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the entire frontend project
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Start the frontend application
CMD ["npm", "start"]
