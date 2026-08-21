export class AccountService {
  getProfile(userId: string): { id: string; name: string } {
    return { id: userId, name: "Demo User" };
  }

  login(email: string, password: string): { token: string } {
    if (!email.includes("@") || password.length === 0) {
      throw new Error("Invalid credentials");
    }

    return { token: `session-${email}` };
  }
}
