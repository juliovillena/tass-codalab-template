#!/bin/bash
rm -f *.zip

echo "Building competition bundle (tass-codalab-template.zip)..."
cd reference_data; zip ../reference_data.zip *; cd ..
cd scoring_program; zip ../scoring_program.zip *; cd ..
zip tass-codalab-template.zip competition.yaml data.html evaluation.html logo.png overview.html reference_data.zip scoring_program.zip terms.html
rm -f reference_data.zip
rm -f scoring_program.zip
echo "Done!"

echo "Building test submission (tass-codalab-template-submission.zip)"
cd test/input/res; zip ../../../tass-codalab-template-submission.zip *; cd ../../../
echo "Done!"
