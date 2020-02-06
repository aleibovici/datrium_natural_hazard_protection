# Datrium Proactive Protection for Natural Hazards

## Synopsis

The Datrium Proactive Protection for Natural Hazards script constantly
check for hatural hazards (wind, temperature and earthquakes) and
proactively increase snapshot frequency and replication for virtual
machines running on Datrium infrastructure.

## Usage

Add environment configuration to main.config before executing.
Add virtual machines to be protected in vms_to_protect.txt

You MUST register for a free API key with OpenWeather at
https://home.openweathermap.org/users/sign_up and add to the key to
the main.config file.

Events are logged to main.log and docker logs.

## Author

Andre Leibovici

## License

Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements. See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
