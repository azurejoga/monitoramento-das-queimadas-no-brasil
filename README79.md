# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4119acf2-d3a0-3f62-a7b1-fe0e0668b2a0 | -15.21162 | -47.64758 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87062392-6244-31d5-9eeb-0e3be134c563 | -20.0851 | -45.80303 | 2025-10-03 04:14:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b48050c8-e805-3608-bcf7-fc16b942838c | -18.66549 | -46.54126 | 2025-10-03 04:14:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7513b4c8-92c9-3c5a-9adf-32e629a6a840 | -15.34251 | -46.29767 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82c89d52-74d4-3769-a052-35f96283811f | -15.12507 | -48.49397 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96211893-a169-32a3-8755-04c61e282f3c | -18.16603 | -53.35096 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa32f15c-cbba-37d2-8873-280ba3dae41f | -15.35266 | -47.06724 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ac98719-deae-3b0f-afb5-9d7e4ca044ec | -17.85818 | -57.61243 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 44f97ab5-bd37-303d-896a-73ae8b3eac2a | -19.45796 | -43.65334 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2ea4095-ab14-3894-a567-88ad8aa0d822 | -16.17509 | -57.58727 | 2025-10-03 04:14:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ff530610-d1b4-3315-b915-3a36bf0412a8 | -15.73911 | -51.30379 | 2025-10-03 04:14:00 | NPP-375D | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0003d5d2-2c06-3138-bcd6-d770012b843a | -17.41078 | -46.99323 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bba3f0fa-4ca7-3ec2-8a8b-76d14d89f27c | -17.3586 | -45.01916 | 2025-10-03 04:14:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 426d5862-aee3-33e0-a62c-7b3a73bea799 | -17.86627 | -57.60778 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 41bf1808-b210-3572-b718-f3e0afc360d2 | -14.92037 | -48.30182 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c95cbee3-7708-362e-bc1d-3900d7830ebf | -15.8367 | -42.62519 | 2025-10-03 04:14:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 1a8d7ee0-cf3e-3b6c-a123-236c0f1f0f68 | -15.46792 | -51.563 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccbfebc9-8827-374a-8645-846f8b8f93c5 | -15.70391 | -46.25498 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8caa368-8f07-33bf-89af-f6fa716f6712 | -18.81924 | -47.41753 | 2025-10-03 04:14:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c87840e-09f5-3c0f-8e82-00338cd489b7 | -15.50056 | -44.1871 | 2025-10-03 04:14:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc1fab00-781f-3ef5-acc4-f799a57d529e | -14.90362 | -48.29442 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 29683a15-3c6b-36a2-bc22-3f7a5ab8a1c4 | -14.98103 | -49.95859 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00b893b0-0217-3b55-bcc7-1436fdfd281e | -15.39792 | -44.97869 | 2025-10-03 04:14:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7586fb14-70df-38a4-91e8-f9e6f4c6c2d0 | -14.90656 | -48.30061 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 960a14fc-48f8-3c18-a5c4-3037cd0c9203 | -19.75119 | -46.0299 | 2025-10-03 04:14:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7fa4ea23-55c5-3816-9c2c-5634e5c870f6 | -16.03133 | -50.93162 | 2025-10-03 04:14:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f27d313-152d-3c42-8908-7a56d2be4b60 | -17.75402 | -51.83493 | 2025-10-03 04:14:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccdae62f-0a65-3f43-b281-effe45eea51b | -14.7336 | -48.10877 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc2f9234-500d-375d-a30f-9c5be2b87193 | -21.24309 | -45.01427 | 2025-10-03 04:14:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2d8a430c-5d27-396a-8d5b-38a11fb8026a | -19.72609 | -45.88243 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e6a794f-3d6a-3413-b7cd-96083949b261 | -14.80915 | -51.42825 | 2025-10-03 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ffb817fd-af04-39db-a035-768d24c0ba75 | -19.81749 | -46.91724 | 2025-10-03 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b91a7e2d-bc16-31dd-ab01-32e8c7b03949 | -14.89966 | -48.35008 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7fe5b9c2-1469-3ea0-a064-36ab61d7d12f | -18.17902 | -53.28701 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b79ea35f-8a78-3fd1-b7f5-2480370e4c33 | -19.59679 | -45.90533 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e1c1a29-9dc5-3247-9e11-6087622e4606 | -16.4031 | -52.16135 | 2025-10-03 04:14:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc9dea7a-51f8-3957-81c5-b408683b678f | -17.58084 | -48.24426 | 2025-10-03 04:14:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1da407a7-1e18-3f70-91eb-99b3dbd05cf4 | -20.9112 | -46.22303 | 2025-10-03 04:14:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a3f3e96c-4d66-3b5f-a7b9-71f7f25aa79b | -19.89048 | -42.62575 | 2025-10-03 04:14:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 022a8d9b-d1f1-3e22-a5bc-415533cf9de2 | -15.65768 | -44.49262 | 2025-10-03 04:14:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4fb18258-0238-31db-906b-4e1a36a430c5 | -14.73919 | -48.09545 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78cb4110-a87f-38fe-9a70-b572377449cf | -14.93969 | -46.88473 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| add18a87-e01d-3dbf-a9b9-0a977a1c8449 | -17.32122 | -49.37778 | 2025-10-03 04:14:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d783fb8-320b-3356-9eaf-cad80bf98971 | -16.33348 | -49.94452 | 2025-10-03 04:14:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0444b3a7-94a6-3660-8cc2-902c7e53c402 | -15.23769 | -50.1279 | 2025-10-03 04:14:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a14c63d-b163-3831-a86b-e01cad705391 | -15.3238 | -46.38678 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edb2bcd3-a60d-3e1c-948b-6141d8d1f35f | -14.94691 | -47.5237 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d68f51f-9016-3319-9340-20a05aede7c1 | -14.91258 | -48.29983 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b5b1df62-f262-3a12-9976-955f8a50a60e | -16.34912 | -47.10511 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f16ccfc-8809-3ba5-a728-0f6c4e243d37 | -19.96421 | -43.6525 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8c111b53-174e-3677-85af-91dbee8400cd | -15.28621 | -46.39299 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b981c41c-3e63-32f1-8a46-550028882901 | -18.45288 | -43.70776 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf7895b8-ac89-37c7-8738-846befe6d9ef | -17.87703 | -57.60793 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7034b5c2-6608-3c05-8fe7-77859e9af180 | -17.37344 | -47.14694 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcda720a-e89c-3275-9608-95675188aa51 | -15.70445 | -46.2707 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f209ae50-5a34-3749-a7dc-213460b0f056 | -15.3294 | -47.32889 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9650688f-9961-3456-8a47-753a2a214713 | -15.85902 | -46.25602 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2eff902f-5961-3316-b720-7a38a0a02757 | -19.45687 | -44.27157 | 2025-10-03 04:14:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fb6b139-42a7-34cc-ad01-2702a13bbc3f | -18.1629 | -53.34742 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9de2072-86f2-3f22-9017-119beb4a0032 | -15.59968 | -47.04574 | 2025-10-03 04:14:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 761a2cfc-019d-3980-b959-fe52e8bcaf56 | -17.1219 | -47.13324 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0d68187-9098-3658-b3fd-155160b0c819 | -19.45518 | -43.64901 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fb29705-10eb-30fc-ae2a-3e78572925a8 | -14.73266 | -48.1142 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 450a6231-81e2-3ded-998a-8e1817bf318a | -14.86109 | -48.36026 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2bb29f4-b737-3542-8923-ff0387838ef1 | -14.90455 | -48.34546 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d3da97cc-7197-30fd-839a-359759406123 | -16.04863 | -50.9133 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8e37649-f793-3a23-aaca-0e1df6ce1251 | -20.96571 | -42.31796 | 2025-10-03 04:14:00 | NPP-375D | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 735de5de-1457-3365-a488-14a2d2fe192e | -14.88254 | -46.85068 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d45de053-fe0f-34f3-b04a-955ae82ad693 | -18.28524 | -43.57104 | 2025-10-03 04:14:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 522353a3-1e5f-3875-a346-c62608ba5f5f | -15.25303 | -47.91523 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 07358524-9178-3b3c-b3d0-fb761eacf148 | -19.14354 | -41.50351 | 2025-10-03 04:14:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fa99dcbd-757d-38fb-a217-480deb601837 | -19.96701 | -43.65675 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f180134b-fd0d-3c65-9f28-c2fde62f8d6c | -17.62646 | -44.4465 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e314636-94d0-3555-b36b-75de7c69f0b8 | -14.65701 | -48.29013 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ba699b4-7f7d-3a02-90bb-7bef41f484f3 | -15.28448 | -45.09304 | 2025-10-03 04:14:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcf58159-7074-3ba5-adae-bfc12bf899e4 | -15.33591 | -47.33535 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65140766-927d-34d0-9d34-dcd0c471fe22 | -19.89955 | -44.5051 | 2025-10-03 04:14:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 35770078-9421-357a-aee5-6571e77df9ed | -16.29072 | -45.24284 | 2025-10-03 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19417817-5636-3411-82b8-f2b2c8dc9223 | -19.7199 | -45.92 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c009d57f-e0d1-3f3e-ac2e-7286c266705b | -15.45338 | -45.87976 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f136e106-9668-3836-be40-0151f47bf6e0 | -14.98185 | -49.95422 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d3c3f14-a174-3c1e-8b53-fffa1713d309 | -14.63861 | -48.2561 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc90ba99-abc4-3346-8f10-668a76df5181 | -14.73548 | -48.11591 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22ce731f-776a-3186-9920-8049687501be | -18.23144 | -53.35258 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 643327c5-52b5-34c9-8dbe-7752daf802a6 | -17.05689 | -46.62918 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c2ef242-722a-3164-80da-9dac4124fc1c | -14.7226 | -48.12009 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0202a659-66d9-3ddd-8679-798cafcaf099 | -16.93186 | -54.15084 | 2025-10-03 04:14:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9212dcd-9e8c-349f-ab5a-e12b808b6d56 | -15.5846 | -46.91838 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfa57b02-7def-379e-9e9f-32a747111916 | -14.9438 | -46.90957 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 29ff1828-b9ea-3de7-a577-d056aa2590c1 | -15.57732 | -48.1921 | 2025-10-03 04:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7c31f32-d5ba-344d-864d-4f5879512d68 | -14.9349 | -46.89572 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 872bd17b-aec3-337f-bd22-621d6b6fa283 | -15.79027 | -43.6826 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ced7055f-136f-3899-a7c9-5045ddc8b4cc | -19.23563 | -43.71599 | 2025-10-03 04:14:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 079ada8f-bdaa-331d-8d92-bb8d52189423 | -15.5903 | -46.90689 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6609d5ca-57ea-32b7-baee-dde22841491b | -18.16227 | -53.35042 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1b5e5245-4611-3f9f-8967-3784062d74a4 | -18.79189 | -43.74519 | 2025-10-03 04:14:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1568fb74-57cd-3cb3-b5a1-333f3f58f5c0 | -14.8966 | -48.34429 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33da5610-73f2-3f5c-bb12-fab3f172cd89 | -15.21596 | -47.18545 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc7986ee-b564-3db0-9d83-db341d62b9fe | -21.23485 | -45.00134 | 2025-10-03 04:14:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43d8e9da-15dd-3851-be96-842d6b21275a | -18.16913 | -53.34331 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README80.md)
