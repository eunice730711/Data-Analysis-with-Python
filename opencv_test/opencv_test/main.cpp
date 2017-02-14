#include <iostream>
#include <opencv/cv.h>
#include <opencv/highgui.h>
#include <opencv/cxcore.h>
//#include "opencv2/opencv.hpp"
//using namespace cv;
using namespace std;
int main()
{
//    VideoCapture cap(0); // open the default camera
//    VideoCapture::VideoCapture("/Users/Emily/Desktop/opencv_test/opencv_test/family.jpg");
    IplImage *img=cvLoadImage("/Users/Emily/Desktop/opencv_test/opencv_test/family.jpg",1);
    CvHaarClassifierCascade *cascade = (CvHaarClassifierCascade *)cvLoad("/Users/Emily/Desktop/opencv_test/opencv_test/haarcascade_frontalface_alt.xml", 0, 0, 0 );
    CvMemStorage *storage =cvCreateMemStorage(0);
    CvSeq* faces = cvHaarDetectObjects( img, cascade,storage,1.1,2,CV_HAAR_DO_CANNY_PRUNING,cvSize(0, 0),cvSize(70, 70));
    int i = 0;
    if (faces)
    {
        for(i = 0; i < faces->total; i++)
        {
            CvPoint pt1, pt2;
            CvRect* rectangle = (CvRect*)cvGetSeqElem(faces, i);
            pt1.x = rectangle->x;
            pt2.x = rectangle->x + rectangle->width;
            pt1.y = rectangle->y;
            pt2.y = rectangle->y + rectangle->height;
            //Draw a red rectanngle
            cvRectangle( img, pt1,pt2, CV_RGB(255,0,0), 3, 8, 0 );
        }
    }
    
    cvShowImage("output", img);
    cvWaitKey(0);
    
    cvClearMemStorage( storage );
    cvReleaseHaarClassifierCascade( &cascade );
    
    
    return 0;
    
}
