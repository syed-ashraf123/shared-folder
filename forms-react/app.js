const Joi = require("joi");
const Complexity = require("joi-password-complexity");
const regex = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/g;

const complexityOptions = {
  min: 8,
  max: 16,
  lowerCase: 1,
  upperCase: 1,
  numeric: 1,
  symbol: 1,
};
const adminRegisterationValidation = (data, res) => {
  const schema = Joi.object({
    name: Complexity(complexityOptions)
      .regex(/^[a-zA-Z0-9_. ]*$/, "Other special characters not allowed")
      .required()
      .custom((value, helper) => {
        if (regex.test(value[0]) || regex.test(value[value.length - 1]))
          return helper.message("Username Not accecpted");
        return true;
      }),
    password: Complexity(complexityOptions).required(),
    email: Joi.string().email().required(),
    mobile: Joi.number().min(6000000000).max(9999999999).integer().positive(),

    role: Joi.number().integer().positive().min(2),
  });
  return schema.validate(data);
};

module.exports.adminRegisterationValidation = adminRegisterationValidation;

const loginValidation = (data, res) => {
  const schema = Joi.object({
    name: Complexity(complexityOptions)
      .regex(/^[a-zA-Z0-9_. ]*$/, "Other special characters not allowed")
      .required()
      .custom((value, helper) => {
        if (regex.test(value[0]) || regex.test(value[value.length - 1]))
          return helper.message("Username Not accecpted");
        return true;
      }),
    password: Complexity(complexityOptions).required(),
  });
  return schema.validate(data);
};

module.exports.loginValidation = loginValidation;

const roleValidation = (data, res) => {
  //Validating role

  const schema = Joi.object({
    role: Joi.number().integer().positive().min(1).required(),
    id: Joi.number().integer().positive().min(1).required(),
  });
  return schema.validate(data);
};

module.exports.roleValidation = roleValidation;
