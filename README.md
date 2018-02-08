# target-json

A [Singer](https://singer.io) target that writes data to JSON files.

## How to use it

`target-json` works together with any other [Singer Tap] to move data
from sources like [Braintree], [Freshdesk] and [Hubspot] to
JSON-formatted files. It is commonly used for loading data into a database
like Bigquery or simply storing a backup of the source data set.

### Install and Run

First, make sure Python 3 is installed on your system or follow these
installation instructions for [Mac](python-mac) or
[Ubuntu](python-ubuntu).

`target-json` can be run with any [Singer Tap], but we'll use
[`tap-fixerio`][Fixerio] - which pulls currency exchange rate data
from a public data set - as an example.

These commands will install `tap-fixerio` and `target-json` with pip,
and then run them together, piping the output of `tap-fixerio` to
`target-json`:

```bash
› pip install target-json tap-fixerio
› tap-fixerio | target-json
  INFO Replicating exchange rate data from fixer.io starting from 2018-02-08
  INFO Tap exiting normally
  {"start_date": "2018-02-08"}
```

The data will be written to a file called `exchange_rate.json` in your
working directory.

```bash
› cat exchange_rate.json
{"AUD": 1.2712, "BGN": 1.5852, "BRL": 3.2477, "CAD": 1.2518, "CHF": 0.941, "CNY": 6.2746, "CZK": 20.449, "DKK": 6.0326, "EUR": 0.8105, "GBP": 0.71871, "HKD": 7.8184, "HRK": 6.0312, "HUF": 251.1, "IDR": 13559.0, "ILS": 3.4913, "INR": 64.245, "ISK": 101.31, "JPY": 109.29, "KRW": 1082.6, "MXN": 18.68, "MYR": 3.903, "NOK": 7.8309, "NZD": 1.3695, "PHP": 51.253, "PLN": 3.3713, "RON": 3.7733, "RUB": 57.158, "SEK": 7.9904, "SGD": 1.3204, "THB": 31.59, "TRY": 3.7835, "ZAR": 11.966, "USD": 1.0, "date": "2018-02-07T00:00:00Z"}
```

If you're using a different Tap, substitute `tap-fixerio` in the final
command above to the command used to run your Tap.

### Optional Configuration

`target-json` takes an optional configuration file that can be used to
set formatting parameters like the delimiter - see
[config.sample.json](config.sample.json) for examples. To run
`target-json` with the configuration file, use this command:

```bash
› tap-fixerio | target-json -c my-config.json
```

### Save State (optional)

When `target-json` is run as above it writes log lines to `stderr`,
but `stdout` is reserved for outputting **State** messages. A State
message is a JSON-formatted line with data that the Tap wants
persisted between runs - often "high water mark" information that the
Tap can use to pick up where it left off on the next run. Read more
about State messages in the [Singer spec].

Targets write State messages to `stdout` once all data that appeared
in the stream before the State message has been processed by the
Target. Note that although the State message is sent into the target,
in most cases the target's process won't actually store it anywhere or
do anything with it other than repeat it back to `stdout`.

Taps like the [`tap-fixerio`][Fixerio] can also accept a `--state` argument
that, if present, points to a file containing the last persisted State
value.  This enables Taps to work incrementally - the State
checkpoints the last value that was handled by the Target, and the
next time the Tap is run it should pick up from that point.

To run the [`tap-fixerio`][Fixerio] incrementally, point it to a State file like this:

```bash
› tap-fixerio --state state.json | target-json -c config.json -s state.json
```

---

[Singer Tap]: https://singer.io
[Singer spec]: https://github.com/singer-io/getting-started/blob/master/SPEC.md
[Braintree]: https://github.com/singer-io/tap-braintree
[Freshdesk]: https://github.com/singer-io/tap-freshdesk
[Hubspot]: https://github.com/singer-io/tap-hubspot
[Fixerio]: https://github.com/singer-io/tap-fixerio
[python-mac]: http://docs.python-guide.org/en/latest/starting/install3/osx/
[python-ubuntu]: https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04