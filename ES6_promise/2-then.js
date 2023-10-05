export default function handleResponseFromAPI(promise) {
  promise.then(
    console.log('Got a response from the API'),
    { status: 200, body: 'success' }
    ,
    Error()
  );
}
