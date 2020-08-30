arr = [-5,-4,-3,1,2,4]
arr = sorted(arr)
lena = len(arr)
que = [4,-2,-3,5] 

def binary_search(strt,end,val,a):
	while True:
		n = end-strt+1
		if n%2==0:
			if a[(n/2)-1]<val<a[n/2]:
				return n/2
			else:
				if val<a[n/2]:
					strt = strt
					end = (n/2)-1
				else:
					strt = n/2
					end = end
		else:
			if val<a[(n-1)/2]:
				if a[(n-3)/2]<val:
					end = (n-3)/2	
					strt = strt
				else:
					return (n-1)/2
			else:
				if a[(n+1)/2]<val:
					return (n+1)/2
				else:
					strt = (n+1)/2
					end = end 


def abs_sum(arr,que):
	pz,z = 0,0
	base_sum = [0 for _ in arr]
	for i in range(lena):
		if arr[i]>=0:
			idx = i
			break
		base_sum[i] = base_sum[i-1]-arr[i]
	base_sum[idx] = arr[idx]
	for i in range(idx+1,lena):
		base_sum[i] = base_sum[i-1]+arr[i]
	base_idx = idx
	if idx!=0:
		neg = base_sum[idx-1]
	else:
		neg = 0
	if idx!=lena:
		pos = base_sum[lena]
	else:
		pos = 0

	for q in que:
		pz = z
		pidx = idx
		if q>0:
			z = z-q
			if z<=arr[0]:
				idx = 0
			else:
				idx = binary_search(0,idx-1,z-0.1,arr)
			if pz<0:
				if idx!=0:
					diff = neg[pidx]-neg[idx-1]
					dz = 
				else:
					diff = neg[pidx]
			elif z>0:
				if idx!=0:
					diff = pos[pidx]-pos[idx-1]
				else:
					diff = pos[pidx]
			else:
				if idx!=0:
					diff = neg[base_idx-1]-neg[idx-1]+pos[pidx]
				else:
					diff = neg[base_idx-1]+pos[pidx]
		elif q<z:
			pass
		else:
			return neg+pos


