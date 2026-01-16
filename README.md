## Get Started

pip install -r requirments.txt

## Run with BehaveX

 - Run all feature files with specified tags

       behavex -t this

   The command above should yield 2 features passed, 16 scenarios passed
   The command above should yield:
    - 2 features passed 
    - 8 scenarios passed (those tagged with @this)
    - 8 scenarios skipped (those not tagged with @this)

 - Run a specifc feature with specified tags

       behavex -t this features/set-1/example-tags-1.feature

   The command above should yield:
    - 1 feature passed (only that matching the specified path)
    - 4 scenarios passed (those tagged with @this)
    - 4 scenarios skipped (those not tagged with @this)

## See all BehaveX cli Options

    behavex --help