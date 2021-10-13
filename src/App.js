import logo from './logo.svg';
import './App.css';
import React, {useState, Component} from 'react';
import logo1 from './QRCodes/qrcode.jpeg'
import QrReader from 'react-qr-reader'

class LegacyModeExample extends Component {
  constructor(props){
    super(props)
    this.myRef = React.createRef();
    this.state = {
      delay: 100,
      username: 'N/A',
      password: 'N/A',


    }

    this.handleScan = this.handleScan.bind(this)
    this.openImageDialog = this.openImageDialog.bind(this)
  }
  handleScan(result){
    if(result){

      const splitted = result.split('\n')
      this.setState({username: splitted[0], password: splitted[1]})
      //this is where I should make API fetch call
    }
  }
  handleError(err){
    console.error(err)
  }
  openImageDialog() {
    this.myRef.current.openImageDialog()
  }

  render(){
    const previewStyle = {
      height: 340,
      width: 320,
    }

    return(
      <div>
        <QrReader
          ref={this.myRef}
          delay={this.state.delay}
          style={previewStyle}
          onError={this.handleError}
          onScan={this.handleScan}
          legacyMode
        />

        <button id="submitQR" className="triggerscan" onClick={this.openImageDialog}>
          Submit QR Code!
        </button>
        <p>Username: {this.state.username}</p>
        <p>Password: {this.state.password}</p>
      </div>
    )
  }
}



function App() {

  const [shouldDisplay, setDisplay] = useState(false);
  const [pathToQR, setPathToQR] = useState("");
  const [qrData, setQrData] = useState("");

  const onButtonPress = () => {
    setDisplay(!shouldDisplay)
    console.log("hi")

  }


  const ImgDisplay = () => {
    if (shouldDisplay) {
      return (
        <img src={logo1} className="QRCode" alt="QR" />
      )
    } else {
      return (null)
    }
  }

  // const AddQR = () => {
  //
  //
  // }
  //
  // const handleScan = data => {
  //   if (data) {
  //     console.log(data)
  //   } else {
  //     console.log("No data!!!")
  //   }
  //
  // }
  //
  // const handleError = err => {
  //   console.log(err)
  // }
  // <QrReader
  //   delay={300}
  //   className="QR-Reader"
  //   onError={handleError}
  //   onScan={handleScan}
  //   style={{ width: '100%' }}
  //   legacyMode={true}
  // />

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <LegacyModeExample />

        <input type="text" id="textBox" onChange={(e) => {setPathToQR(e.target.value)}} />
        <button className="loadFileName" onClick={onButtonPress}>
          Click Me!
        </button>
        <p>I am the path: {pathToQR} </p>
        <ImgDisplay />
      </header>
    </div>
  );
}

export default App;
