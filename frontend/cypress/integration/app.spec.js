describe("Live Sensor Data Dashboard", () => {
    it("Visits the dashboard and checks table content", () => {
      cy.visit("http://localhost:3000");
      cy.contains("Live Sensor Data");
      cy.get("table").should("exist");
    });
  });
  