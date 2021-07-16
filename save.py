import csv

def save_to_file(jobs) : 
  file = open("jobs.csv", mode="w")
  # jobs.csv 파일 생성 -> file에 저장

  # writer 작성하기
  # file이라는 파일에 csv 형식으로 쓰는 writer
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs :
    writer.writerow(list(job.values()))
  # print(jobs) 
  return