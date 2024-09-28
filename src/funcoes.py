

def formatar_cpf(event=None, insereCpf):
            cpf = insereCpf.get()
            cpf = ''.join(filter(str.isdigit, cpf))
            if len(cpf) > 3:
                cpf = cpf[:3] + '.' + cpf[3:]
            if len(cpf) > 6:
                cpf = cpf[:7] + '.' + cpf[7:]
            if len(cpf) > 9:
                cpf = cpf[:11] + '-' + cpf[11:]
            
            
            cpf = cpf[:14]

            
            insereCpf.delete(0, tk.END)
            insereCpf.insert(0, cpf)