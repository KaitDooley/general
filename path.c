#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
int main() {
	int fd = open("path.txt", O_RDONLY);
	char buffer[BUFSIZ];

	while (read(fd, buffer, BUFSIZ) > 0) {
    	printf("%s\n", buffer);
	}

	close(fd);
}
