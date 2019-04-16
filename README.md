# elasticgroup-cli

elasticgroup-cli is a Command Line Interface (CLI) to interact with SpotInst API. it allows you to do some functionalities from the command line like updating autoscaling, configure schedule tasks, check Instances health, and more.

#### These Functions are supported
 We plan to add support for more functions

 :heavy_check_mark: List and Filter Configured ElasticGroups

 :heavy_check_mark: List and Filter Configured Scheduled Tasks

 :heavy_check_mark: List and Describe Autoscaling

 :heavy_check_mark: Update Autoscaling Configuration

 :heavy_check_mark: Describe Scheduled Tasks for Specific ElasticGroup

 :heavy_check_mark: Configure Scheduled Tasks for Specific ElasticGroup

 :heavy_check_mark: Check Instances health

## Installation:
#### First:
You need to configure SpotInst Credentials.you can configure the credentials by creating a file ~/.spotinst/credentials and add a profile

Example

```bash
default:
  token: 7df2e7df2e42344860de001de-xxxxxx
  account: act-xxxxxx
```
Or export them in environment variables
```bash
export spotinst_token="7df2e7df2e42344860de001de-xxxxxx"
export account_id="act-xxxxx"
```
#### Second:
Install the Package
```bash
pip install elasticgroup-cli
```
## Usage

Get the help
```bash
elasticgroup-cli -h
```

List all configured Elasticgroups
```bash
elasticgroup-cli --list
```
List Elasticgroups and filter based on different criteria like environment or stackgroup
```bash
elasticgroup-cli --list --filter=live
elasticgroup-cli --list --filter=checkout
```
List all configured scheduled tasks
```bash
elasticgroup-cli -lt
elasticgroup-cli --list-tasks
```
List and filter configured scheduled tasks
```bash
elasticgroup-cli --list-tasks --filter=live
```

Check the instance health of specific Elasticgroup
```bash
elasticgroup-cli --instances-health <Elasticgroup-Name>
```
List configured Autoscaling Actions of specific Elasticgroup
```bash
elasticgroup-cli --describe-autoscaling <Elasticgroup-Name>
```
Configure Autoscaling for specific Elasticgroup
```bash
elasticgroup-cli --configure-autoscaling <Elasticgroup-Name> --min=x --max=x --target=x
```

List configured Scheduled Tasks of specific Elasticgroup
```bash
elasticgroup-cli --describe-scheduled-tasks <Elasticgroup-Name>
```
Configure Scheduled Tasks of specific Elasticgroup
```bash
elasticgroup-cli --configure-scheduled-tasks <Elasticgroup-Name> --cron-expression="expression" --min=x --max=x --target=x
```
#### Note
If the Cron Expression exist, the schedule will be updated, if not, the schedule will be created

## Examples:

```bash
└─ $ ▶ elasticgroup-cli --list --filter=checkout
 Elasticgroups
+-------------------------------------------+
| Elasticgroup Name                         |
+-------------------------------------------+
| checkout-staging-508                      |
| checkout-staging-199                      |
+-------------------------------------------+
```

```bash
└─ $ ▶ elasticgroup-cli --describe-autoscaling token-staging-52

 Configured AutoScaling
+-----------+--------------------------------------------------------------------+
| Type      | Properties                                                         |
+-----------+--------------------------------------------------------------------+
| Scaleup   | Cooldown = 60                                                      |
|           | Statistic = average                                                |
|           | Namespace = AWS/EC2                                                |
|           | Threshold = 50                                                     |
|           | Policy_name = Scale if CPU >= 50 percent for 4.0 minutes (average) |
|           | Adjustment = 1                                                     |
|           | Metric_name = CPUUtilization                                       |
|           | Minimum = 2                                                        |
|           | Maximum = 10                                                       |
|           | Target = 2                                                         |
|           | Unit = instance                                                    |
|           |                                                                    |
| Scaledown | Cooldown = 60                                                      |
|           | Statistic = average                                                |
|           | Namespace = AWS/EC2                                                |
|           | Threshold = 20                                                     |
|           | Policy_name = Scale if CPU < 20 percent for 4.0 minutes (average)  |
|           | Adjustment = 1                                                     |
|           | Metric_name = CPUUtilization                                       |
|           | Minimum = 2                                                        |
|           | Maximum = 10                                                       |
|           | Target = 2                                                         |
|           | Unit = instance                                                    |
|           |                                                                    |
+-----------+--------------------------------------------------------------------+
```
```bash
└─ $ ▶ elasticgroup-cli --describe-scheduled-tasks cart-staging-green-80

 Scheduled Actions of Elasticgroup cart-staging-green-80
+-----------------+--------------------+--------------------+-----------------------+------------+
| cron_expression | scale_min_capacity | scale_max_capacity | scale_target_capacity | is_enabled |
+-----------------+--------------------+--------------------+-----------------------+------------+
| 0 5 * * 1-5     | 2                  | 10                 | 2                     | True       |
| 0 21 * * 1-5    | 0                  | 0                  | 0                     | True       |
+-----------------+--------------------+--------------------+-----------------------+------------+
```
```bash
└─ $ ▶ elasticgroup-cli --update-autoscaling cart-staging-green-80 --min=2 --max=3 --target=2

 Updating Elasticgroup cart-staging-green-80 Capacity...
 Elasticgroup cart-staging-green-80 has been scaled successfully. it may takes few seconds to reflect....
```

```bash
└─ $ ▶ elasticgroup-cli --configure-scheduled-tasks cart-staging-green-80 --cron-expression="0 21 * * 1-5" --min=1 --target=1 --max=2

 Scheduled Tasks of Elasticgroup cart-staging-green-80 have been configured successfully.
```
