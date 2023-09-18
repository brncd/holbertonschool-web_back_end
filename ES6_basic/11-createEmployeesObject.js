export default function createEmployeesObject(departmentName, employees) {
  const objeto = { [departmentName]: employees };
  return objeto;
}
