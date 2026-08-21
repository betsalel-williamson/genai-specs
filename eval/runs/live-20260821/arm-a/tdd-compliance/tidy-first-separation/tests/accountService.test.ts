import { describe, expect, it } from "vitest";
import { AccountService } from "../src/AccountService.js";

describe("AccountService", () => {
  it("shouldReturnProfileForUserId", () => {
    const service = new AccountService();
    expect(service.getProfile("user-1")).toEqual({
      id: "user-1",
      name: "Demo User",
    });
  });

  it("shouldLoginWithValidCredentials", () => {
    const service = new AccountService();
    expect(service.login("demo@example.com", "secret")).toEqual({
      token: "session-demo@example.com",
    });
  });
});
