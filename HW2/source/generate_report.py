import argparse
from sklearn.metrics import classification_report

def main():
    parser = argparse.ArgumentParser(description="Classification Report for CRF classifier")
    parser.add_argument("file", help="classification results file")
    args = parser.parse_args()
    analyseFile = args.file
    y_true_dict = {'cause' : 0, 'effect': 0, 'irrelevant': 0, 'month': 0, 'noAffected': 0, 'place': 0, 'year': 0}
    y_pred_dict = {'cause' : 0, 'effect': 0, 'irrelevant': 0, 'month': 0, 'noAffected': 0, 'place': 0, 'year': 0}
    tp_dict = {'cause' : 0, 'effect': 0, 'irrelevant': 0, 'month': 0, 'noAffected': 0, 'place': 0, 'year': 0}
    fp_dict = {'cause' : 0, 'effect': 0, 'irrelevant': 0, 'month': 0, 'noAffected': 0, 'place': 0, 'year': 0}
    y_true = []
    y_pred = []
    lines = open(analyseFile, "r").readlines()
    for line in lines:
		token = line.split()
		if(len(token) == 8):
			if token[6] == token[7]:
				tp_dict[token[6]] +=1
				#print(token[6],token[7])
			elif token[6] != token[7]:
				fp_dict[token[7]] +=1
				#print("\t\t\tDiscrepany : ", token[6],token[7])
			y_true_dict[token[6]] += 1
			y_pred_dict[token[7]] += 1
			y_true.append(token[6])
			y_pred.append(token[7])
    #print(y_true[:11])
    #print(y_pred[:11])
    print("y_true_dict : ",y_true_dict)
    print("y_pred_dict : ",y_pred_dict)
    print("tp_dict : ",tp_dict)
    print("fp_dict : ",fp_dict)
    
    recall_dict = {'cause' : 0.0, 'effect': 0.0, 'irrelevant': 0.0, 'month': 0.0, 'noAffected': 0.0, 'place': 0.0, 'year': 0.0}
    precision_dict = {'cause' : 0.0, 'effect': 0.0, 'irrelevant': 0.0, 'month': 0.0, 'noAffected': 0.0, 'place': 0.0, 'year': 0.0}
    f1_score = {'cause' : 0.0, 'effect': 0.0, 'irrelevant': 0.0, 'month': 0.0, 'noAffected': 0.0, 'place': 0.0, 'year': 0.0}
    
    weighted_avg = 0.0
    total_samples = 0
    for keyClass in y_true_dict.keys():
		recall_dict[keyClass] = round(float(tp_dict[keyClass]) / y_true_dict[keyClass], 2)
		precision_dict[keyClass] = round(float(tp_dict[keyClass]) / (tp_dict[keyClass] + fp_dict[keyClass]),2)
		recall_precision_sum = recall_dict[keyClass] + precision_dict[keyClass]
		if recall_precision_sum != 0:
			f1_score[keyClass] = round((2*recall_dict[keyClass]*precision_dict[keyClass])/(recall_dict[keyClass] + precision_dict[keyClass]),2)
		else:
			print("NOTE:")
			print("Unable to compute f1_score for : ", keyClass)
			print("recall_dict[keyClass] : ",recall_dict[keyClass])
			print("precision_dict[keyClass] : ",precision_dict[keyClass])
		weighted_avg += y_true_dict[keyClass]*f1_score[keyClass]
		total_samples += y_true_dict[keyClass]
    weighted_avg /= total_samples
    print("")
    print("recall_dict : ",recall_dict)
    print("precision_dict : ",precision_dict)
    print("f1_score : ",f1_score)
    print("weighted_avg of f1-scores for all classes: ",round(weighted_avg,2))
    
    print(classification_report(y_true, y_pred))

if __name__=="__main__" : main()
