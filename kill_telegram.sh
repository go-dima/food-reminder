#!/bin/bash

kill -9 $(ps -a | grep telegram | awk '{print $1}')
