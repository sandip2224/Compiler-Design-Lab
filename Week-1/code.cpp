// Author: Sandipan Das

#include<bits/stdc++.h>
using namespace std;

void createFile(){
	fstream file;
	file.open("test.txt", ios::out);
	if(!file){
	   cout<<"Error in creating file!!\n";
	   return;
   }
   cout<<"File created successfully!!\n";
   file.close();
   cout<<"\n";
}

void readFile(){
	ifstream file;
	file.open("test.txt");
	char ch;
	if(!file){
      cout<<"Error: File could not be opened!!\n";
      return;
   	}
	cout<<"Contents of file are as follows: "<<"\n";
	file>>ch;
	while(!file.eof()){
		cout<<ch;
		file>>ch;
	}
	file.close();
	cout<<"\n\n";
}

void writeToFile(){
	ofstream file;
	file.open("test.txt");
	string contents="My name is Sandipan Das!!\n";
	file<<contents;
	file.close();
}

void deleteFile(){
	int status=remove("test.txt");
    if(status==0)
        cout<<"File Deleted Successfully!!\n";
    else
        cout<<"Error Occurred! File could not be deleted!!\n";
}

int main(){
	createFile();
	writeToFile();
	readFile();
	deleteFile();
}