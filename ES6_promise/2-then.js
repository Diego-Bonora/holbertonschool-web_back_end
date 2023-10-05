export default function handleResponseFromAPI(promise) {
  promise.then(
    success()
    ,
    Error()
  );
};

function success() {
  console.log('Got a response from the API')
  return { status: 200, body: 'success' }
}
