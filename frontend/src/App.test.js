import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders Live Sensor Data heading", () => {
  render(<App />);
  const headingElement = screen.getByText(/Live Sensor Data/i);
  expect(headingElement).toBeInTheDocument();
});
