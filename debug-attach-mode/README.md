# Debugging with VS Code "attach mode"

1. Start the Docker container:

```bash
docker build -t buggy_calculator/docker-debugging-attach-mode:v1 .

docker run --name buggy_calculator-docker-remote-debugging-v1 -it --rm -v .:/app -p 5678:5678 buggy_calculator/docker-debugging-attach-mode:v1 /bin/bash

2. In VS Code, go to the Debug view (Ctrl+Shift+D).

3. Click on "create a launch.json file", then select "Python".

4. Modify the generated `launch.json` to include the following configuration:

   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Python: Attach",
               "type": "python",
               "request": "attach",
               "connect": {
                   "host": "localhost",
                   "port": 5678
               }
           }
       ]
   }
   ```

5. Set breakpoints in your code.

6. Start the debugging session by selecting the "Python: Attach" configuration and clicking the green play button.

7. Your breakpoints should now be hit when you run the code in the Docker container.