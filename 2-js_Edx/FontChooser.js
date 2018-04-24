 class FontChooser extends React.Component {

   constructor(props) {
         super(props);
         var min = Math.max(1,this.props.min);
         var max = this.props.max;
         if (min >= max){
            max = min;
         }

         var baseSize = Math.max(min, parseInt(this.props.size));
         if (baseSize >= max){
            baseSize = max;
         }

         var bold = 'normal';
         if (this.props.bold == 'true') {
            bold = 'bold'
         }

         this.state = { visibility: true,
                        bold: bold,
                        baseSize: baseSize,
                        fontSize: baseSize,
                        color: 'black',
                        min: min,
                        max: max};
         console.log("bold:"+this.props.bold);
   }

   toggleVisibility() {
      this.setState( { visibility: (!this.state.visibility) } );
   }

   toggleBold() {
      var bold = 'normal';
      if (this.state.bold == 'normal') {
         bold = 'bold'
      }
      this.setState( { bold: bold } );
   }

   increaseSize() {
      var color = 'black';
      var size =  this.state.fontSize;
      if ( this.state.fontSize < this.state.max) {
         ++size;
      }
      if (size == this.state.max) {
         color = 'red'
      }
      this.setState( { fontSize: size, color: color } )
   }

   decreaseSize() {
      var color = 'black';
      var size =  this.state.fontSize;
      if ( this.state.fontSize > this.state.min) {
         --size;
      }
      if (size == this.state.min) {
         color = 'red'
      }
      this.setState( { fontSize: size, color: color } )
   }

   cancelSizeChange() {
      this.setState( { color: 'black',
                        fontSize: this.state.baseSize})
   }

   render() {
      return(
         <div>
            <input type="checkbox" id="boldCheckbox"
                  hidden = { this.state.visibility }
                  checked = { this.state.bold != 'normal'}
                  onChange = { this.toggleBold.bind(this) }/>
            <button id="decreaseButton"
                  hidden = { this.state.visibility }
                  onClick = { this.decreaseSize.bind(this) }>-</button>
            <span id="fontSizeSpan" hidden = { this.state.visibility }
                  style = {{color: this.state.color}}
                  onDoubleClick = { this.cancelSizeChange.bind(this) }>
               { this.state.fontSize }
            </span>
            <button id="increaseButton"
                  hidden = { this.state.visibility }
                  onClick = { this.increaseSize.bind(this) }>+</button>
            <span id="textSpan"
                  onClick = { this.toggleVisibility.bind(this) }
                  style = {{fontWeight: this.state.bold,
                           fontFamily: "Roboto, sans serif",
                           fontSize: this.state.fontSize}}>
               {this.props.text}
            </span>
         </div>

      );
   }
}
