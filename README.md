# Random Sampling

This tool is used to random sampling of chloroplast genome. The alinged whole chloroplast genome was first divided into 100 bp seeds, and the seeds will be randomly sampled at the percentage user set (such as 15%). 

## Installing software
`git clone https://github.com/Mycroft-behind/random-sampling.git`


## Software dependencies
* python(>=3.7)

## Usage
`python randomSampling.py --input/-i input_file --lengthSeed/-l  seed_length_of_sequence [--percentage/-p] extraction_rate [--repeat/-rep] repeat_time`

## Result
The result will be saved in "result" directory. 
