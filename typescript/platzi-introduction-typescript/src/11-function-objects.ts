(() => {
  const login = (email: string, password: string) => {
    console.log(`Login succesful. Email: ${email}. Password: ${password}`);
  }

  login("andrescc143@hotmail.com", "password");

  //The same but implemented using object as parameters:
  const loginObject = (data: {email: string, password: number}) => {
    console.log(`Login succesful. Email: ${data.email}. Password: ${data.password}`);
  };

  loginObject({email: "andrescc143@hotmail.com", password: 123456});
})();
