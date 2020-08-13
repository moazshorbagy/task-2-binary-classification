import React from 'react';

import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles((theme) => ({
  root: {
    textAlign: "center"
  },
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
  inputs: {
    textAlign: "center",
    marginLeft: "3em",
    marginRight: "3em",
    padding: "3em",
  },
  output: {
    padding: "1.5em",
    margin: "1.5em",
    fontSize: "1.5em"
  },
}));

function App() {

  const classes = useStyles();

  const [response, setResponse] = React.useState('');
  const handleResponse = (event) => {
    setResponse(event);
  };

  const [model, setModel] = React.useState('neural_n');
  const handleModel = (event) => {
    setModel(event.target.value);
  };

  const [variable1, setVariable1] = React.useState('a');
  const handleVariable1 = (event) => {
    setVariable1(event.target.value);
  };

  const [variable2, setVariable2] = React.useState('nan');
  const handleVariable2 = (event) => {
    setVariable2(event.target.value);
  };

  const [variable3, setVariable3] = React.useState(0);
  const handleVariable3 = (event) => {
    setVariable3(event.target.value);
  };

  const [variable4, setVariable4] = React.useState('l');
  const handleVariable4 = (event) => {
    setVariable4(event.target.value);
  };

  const [variable5, setVariable5] = React.useState('g');
  const handleVariable5 = (event) => {
    setVariable5(event.target.value);
  };

  const [variable6, setVariable6] = React.useState('aa');
  const handleVariable6 = (event) => {
    setVariable6(event.target.value);
  };

  const [variable7, setVariable7] = React.useState('v');
  const handleVariable7 = (event) => {
    setVariable7(event.target.value);
  };

  const [variable8, setVariable8] = React.useState(0);
  const handleVariable8 = (event) => {
    setVariable8(event.target.value);
  };

  const [variable9, setVariable9] = React.useState('t');
  const handleVariable9 = (event) => {
    setVariable9(event.target.value);
  };

  const [variable10, setVariable10] = React.useState('t');
  const handleVariable10 = (event) => {
    setVariable10(event.target.value);
  };

  const [variable11, setVariable11] = React.useState(0);
  const handleVariable11 = (event) => {
    setVariable11(event.target.value);
  };

  const [variable12, setVariable12] = React.useState('t');
  const handleVariable12 = (event) => {
    setVariable12(event.target.value);
  };

  const [variable13, setVariable13] = React.useState('g');
  const handleVariable13 = (event) => {
    setVariable13(event.target.value);
  };

  const [variable14, setVariable14] = React.useState('nan');
  const handleVariable14 = (event) => {
    setVariable14(event.target.value);
  };

  const [variable15, setVariable15] = React.useState(0);
  const handleVariable15 = (event) => {
    setVariable15(event.target.value);
  };

  const [variable17, setVariable17] = React.useState('nan');
  const handleVariable17 = (event) => {
    setVariable17(event.target.value);
  };

  const [variable18, setVariable18] = React.useState('');
  const handleVariable18 = (event) => {
    setVariable18(event.target.value);
  };

  const [variable19, setVariable19] = React.useState('');
  const handleVariable19 = (event) => {
    setVariable19(event.target.value);
  };

  const handleClick = async () => {
    const response = await fetch('/api', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model,
        variable1, variable2, variable3, variable4, variable5, variable6,
        variable7, variable8, variable9, variable10, variable11, variable12,
        variable13, variable14, variable15, variable17, variable18, variable19
      }),
    });
    if (response.status === 500) {
      handleResponse(response.statusText + ": try starting the python backend.");
    } else {
      handleResponse(await response.text());
    }
  };

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar variant="dense">
          <Typography variant="h6" color="inherit">
            WideBot - Binary Classification
          </Typography>
        </Toolbar>
      </AppBar>

      <div className={classes.inputs}>
        <FormControl className={classes.formControl}>
          <InputLabel id="model-label">Model</InputLabel>
          <Select
            labelId="model-label"
            id="model"
            value={model}
            onChange={handleModel}
          >
            <MenuItem value={'neural_n'}>Neural Network</MenuItem>
            <MenuItem value={'knn'}>kNN</MenuItem>
          </Select>
        </FormControl>
      </div>

      <div className={classes.inputs}>
        <FormControl className={classes.formControl}>
          <InputLabel id="variable1-label">Variable 1</InputLabel>
          <Select
            labelId="variable1-label"
            id="variable1"
            value={variable1}
            onChange={handleVariable1}
            className={classes.selectEmpty}
          >
            <MenuItem value={'a'}>a</MenuItem>
            <MenuItem value={'b'}>b</MenuItem>
          </Select>
        </FormControl>

        <TextField
          id="variable2"
          label="Variable 2"
          type="number"
          className={classes.formControl}
          onChange={handleVariable2}
          value={variable2}
        />

        <TextField
          id="variable3"
          label="Variable 3"
          type="number"
          required
          className={classes.formControl}
          onChange={handleVariable3}
          value={variable3}
        />

        <FormControl className={classes.formControl}>
          <InputLabel id="variable4-label">Variable 4</InputLabel>
          <Select
            labelId="variable4-label"
            id="variable4"
            value={variable4}
            onChange={handleVariable4}
          >
            <MenuItem value={'l'}>l</MenuItem>
            <MenuItem value={'u'}>u</MenuItem>
            <MenuItem value={'y'}>y</MenuItem>
          </Select>
        </FormControl>

        <FormControl className={classes.formControl}>
          <InputLabel id="variable5-label">Variable 5</InputLabel>
          <Select
            labelId="variable5-label"
            id="variable5"
            value={variable5}
            onChange={handleVariable5}
          >
            <MenuItem value={'g'}>g</MenuItem>
            <MenuItem value={'p'}>p</MenuItem>
            <MenuItem value={'gg'}>gg</MenuItem>
          </Select>
        </FormControl>

        <FormControl className={classes.formControl}>
          <InputLabel id="variable6-label">Variable 6</InputLabel>
          <Select
            labelId="variable6-label"
            id="variable6"
            value={variable6}
            onChange={handleVariable6}
          >
            <MenuItem value={'aa'}>aa</MenuItem>
            <MenuItem value={'c'}>c</MenuItem>
            <MenuItem value={'k'}>k</MenuItem>
            <MenuItem value={'ff'}>ff</MenuItem>
            <MenuItem value={'i'}>i</MenuItem>
            <MenuItem value={'j'}>j</MenuItem>
            <MenuItem value={'q'}>q</MenuItem>
            <MenuItem value={'w'}>w</MenuItem>
            <MenuItem value={'d'}>d</MenuItem>
            <MenuItem value={'m'}>m</MenuItem>
            <MenuItem value={'cc'}>cc</MenuItem>
            <MenuItem value={'r'}>r</MenuItem>
            <MenuItem value={'x'}>x</MenuItem>
            <MenuItem value={'e'}>e</MenuItem>
          </Select>
        </FormControl>

        <FormControl className={classes.formControl}>
          <InputLabel id="variable7-label">Variable 7</InputLabel>
          <Select
            labelId="variable7-label"
            id="variable7"
            value={variable7}
            onChange={handleVariable7}
          >
            <MenuItem value={'v'}>v</MenuItem>
            <MenuItem value={'ff'}>ff</MenuItem>
            <MenuItem value={'o'}>o</MenuItem>
            <MenuItem value={'h'}>h</MenuItem>
            <MenuItem value={'j'}>j</MenuItem>
            <MenuItem value={'bb'}>bb</MenuItem>
            <MenuItem value={'n'}>n</MenuItem>
            <MenuItem value={'z'}>z</MenuItem>
            <MenuItem value={'dd'}>dd</MenuItem>
          </Select>
        </FormControl>

        <TextField
          id="variable8"
          label="Variable 8"
          type="number"
          required
          className={classes.formControl}
          onChange={handleVariable8}
          value={variable8}
        />

        <FormControl className={classes.formControl}>
          <InputLabel id="variable9-label">Variable 9</InputLabel>
          <Select
            labelId="variable9-label"
            id="variable9"
            value={variable9}
            onChange={handleVariable9}
          >
            <MenuItem value={'t'}>t</MenuItem>
            <MenuItem value={'f'}>f</MenuItem>
          </Select>
        </FormControl>

        <FormControl className={classes.formControl}>
          <InputLabel id="variable10-label">Variable 10</InputLabel>
          <Select
            labelId="variable10-label"
            id="variable10"
            value={variable10}
            onChange={handleVariable10}
          >
            <MenuItem value={'t'}>t</MenuItem>
            <MenuItem value={'f'}>f</MenuItem>
          </Select>
        </FormControl>

        <TextField
          id="variable11"
          label="Variable 11"
          type="number"
          required
          className={classes.formControl}
          onChange={handleVariable11}
          value={variable11}
        />

        <FormControl className={classes.formControl}>
          <InputLabel id="variable12-label">Variable 12</InputLabel>
          <Select
            labelId="variable12-label"
            id="variable12"
            value={variable12}
            onChange={handleVariable12}
          >
            <MenuItem value={'t'}>t</MenuItem>
            <MenuItem value={'f'}>f</MenuItem>
          </Select>
        </FormControl>

        <FormControl className={classes.formControl}>
          <InputLabel id="variable13-label">Variable 13</InputLabel>
          <Select
            labelId="variable13-label"
            id="variable13"
            value={variable13}
            onChange={handleVariable13}
          >
            <MenuItem value={'g'}>g</MenuItem>
            <MenuItem value={'s'}>s</MenuItem>
            <MenuItem value={'p'}>p</MenuItem>
          </Select>
        </FormControl>

        <TextField
          id="variable14"
          label="Variable 14"
          type="number"
          className={classes.formControl}
          onChange={handleVariable14}
          value={variable14}
        />

        <TextField
          id="variable15"
          label="Variable 15"
          type="number"
          required
          className={classes.formControl}
          onChange={handleVariable15}
          value={variable15}
        />

        <TextField
          id="variable17"
          label="Variable 17"
          type="number"
          className={classes.formControl}
          onChange={handleVariable17}
          value={variable17}
        />

        <FormControl className={classes.formControl}>
          <InputLabel shrink id="variable18-label">Variable 18</InputLabel>
          <Select
            labelId="variable18-label"
            id="variable18"
            value={variable18}
            onChange={handleVariable18}
            displayEmpty
            className={classes.selectEmpty}
          >
            <MenuItem value="">
              <em>None</em>
            </MenuItem>
            <MenuItem value={'t'}>t</MenuItem>
            <MenuItem value={'f'}>f</MenuItem>
          </Select>
        </FormControl>

        <FormControl className={classes.formControl}>
          <InputLabel shrink id="variable19-label">Variable 19</InputLabel>
          <Select
            labelId="variable19-label"
            id="variable19"
            value={variable19}
            onChange={handleVariable19}
            displayEmpty
            className={classes.selectEmpty}
          >
            <MenuItem value="">
              <em>None</em>
            </MenuItem>
            <MenuItem value={0}>0</MenuItem>
            <MenuItem value={1}>1</MenuItem>
          </Select>
        </FormControl>
      </div>

      <Button variant="contained" onClick={handleClick}>Classify</Button>
      <Button variant="contained" onClick={() => { setResponse('') }}>Clear Output</Button>
      <div className={classes.output}><b>Classification:</b> {response}</div>
    </div>
  );
}

export default App;
