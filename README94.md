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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54c60761-3416-30e0-8ba0-33ae58e50785 | -14.98775 | -46.9017 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7469ab87-1af4-3822-8765-f487fa14fac3 | -13.52297 | -47.25952 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0be18bd9-7164-32c0-b018-e0fd98dd45ff | -15.92924 | -46.24414 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e606d85-31e8-352b-834a-23500131391c | -14.3739 | -45.96929 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f6c0ea9-233d-3f2e-aef0-b1c73b8ac7d0 | -12.7 | -48.58521 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43bea477-cefa-3982-8824-bc072305ad78 | -15.25889 | -49.31264 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5c5b0af5-7502-33bb-a8e1-5b42834350a9 | -12.81366 | -46.90733 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e15a9e17-7f7e-3876-bdf8-2cca82a31783 | -13.00695 | -45.21344 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1d209469-ef0e-33c0-96b2-dc9217922817 | -13.31454 | -47.85379 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ac9a0a1-c6de-3e24-bc13-0c908ee1ce3f | -14.89864 | -47.18501 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80446334-1490-386d-8845-f323766c32a2 | -19.51678 | -43.60468 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f255d18-b85b-3cee-a298-ecced16a9734 | -18.17662 | -53.27253 | 2025-10-02 04:32:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0227f90b-83eb-3dc8-a432-0fe263bb6219 | -15.59781 | -46.92037 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a83427e1-5537-3362-9c7f-df863ecf398b | -19.95995 | -43.6529 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 88426c70-d29a-30a2-9502-2388a607cb56 | -14.90257 | -47.1819 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7597e62-e9ef-343a-9298-e7a68c348279 | -13.00813 | -45.20539 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6ceca028-0129-321d-9502-2390bc207066 | -13.17671 | -47.80532 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3db7ad3d-f3af-3cb3-b0c1-6e86284159cf | -17.08761 | -48.56388 | 2025-10-02 04:32:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 842b402f-e2d3-3c7e-8cc4-d7794c0e9451 | -17.07344 | -44.90633 | 2025-10-02 04:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54bd869e-db5a-3323-904f-cb548c9f57ea | -14.86609 | -48.28728 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d1f0ae90-a00a-36a9-9ef6-5c1f41a24bdb | -16.0381 | -50.89329 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 204b8645-072c-3fa3-8069-3386ad103973 | -12.46355 | -54.32679 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a46b5a2-b06e-300c-8bb5-639a8125773d | -11.59325 | -50.17252 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2413e8b9-e021-3489-b6f4-a10492ee1b65 | -12.46074 | -54.31709 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 099d6139-e242-3aee-bd64-5168d3a9291e | -15.18274 | -46.41051 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb98637b-2b86-39aa-a48a-b0111301b6e9 | -13.95978 | -48.112 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ff8ed31-03cf-370e-b39a-faf762704bbd | -14.89982 | -48.09496 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b8c29cd-252a-367c-919f-bc922ad12e9c | -13.7883 | -48.0003 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ef88f7b-11ad-39ec-a63e-48de290badc8 | -15.23223 | -48.73011 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc52c53e-8b45-36d2-b156-9e82b00cfed6 | -16.28709 | -45.24445 | 2025-10-02 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe8fb054-685f-3810-b90a-fddd474c0e2f | -14.40173 | -46.09265 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3f0c13e-a589-3e7a-b593-1897280db23c | -14.70198 | -49.61496 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35c8547c-8587-334b-a1a6-09d53f60a113 | -12.75227 | -46.90468 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 106c77a9-e64c-3940-8cf1-42d1047e1a9c | -14.68507 | -49.61198 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac085b61-280c-3eaa-a943-dec54315d4c2 | -13.17282 | -47.80832 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8e66b19-24bb-3c2d-872b-ec6db5beb74f | -14.31413 | -45.88549 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 779afcdb-efb1-3589-8fae-eec7ca46bbf1 | -16.05436 | -51.03218 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86531047-a7e4-3de3-a859-3d2e5a8baf0a | -13.21479 | -48.43905 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ee805f0-78a7-3cc7-9a5f-5d65224f8360 | -13.56426 | -47.26925 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d580a521-54d0-32b7-b948-1ff4419e5dea | -15.23131 | -50.11705 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 499411ac-c013-3483-8f79-64d88b1d8d19 | -15.64447 | -49.25496 | 2025-10-02 04:32:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6535a27-6c85-302f-bac4-4a8a2680166e | -15.36292 | -47.06647 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77cd63ee-52dc-3485-bc04-7a788a4f9d9d | -15.25419 | -49.26714 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11a7757a-708c-32d1-9e23-5a4a10c176b3 | -12.01961 | -46.63846 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc5d0fb7-62f5-3b10-8fd6-a5e19dfa705b | -13.40042 | -47.7803 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68778a90-f39f-39d1-b175-d6cc59f40c63 | -15.61089 | -46.52967 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ab3a006-be71-3296-b5d0-5b3915ee4413 | -13.77376 | -48.04901 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6997cfa6-b320-38fa-a2ea-dec1c65cc79c | -14.98464 | -46.91695 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e498d31f-b87e-32f8-85b8-5a1bb538f429 | -13.34102 | -47.33639 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f81899d-f265-3566-bb70-84929f44fd12 | -13.14612 | -47.84762 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55d115e5-1dbf-36d4-a624-9949251c7d7d | -17.68151 | -43.83605 | 2025-10-02 04:32:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 324a48a8-49fe-34ef-af72-a172d602fbe9 | -13.16781 | -47.81842 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cf9184f1-69ff-3816-89fc-a0e57b0c58ba | -18.19784 | -53.30727 | 2025-10-02 04:32:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c36b7a78-9e72-3b6f-967f-1a8db6cbb996 | -13.30292 | -47.84097 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16469831-11e9-3c60-84e5-89df1e32da99 | -14.0316 | -48.00337 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4e96f78-bbac-3894-a8fb-f41b4eeb294c | -15.69781 | -46.2536 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5de33ac-63b5-3ddf-8fe6-c6167e7d721b | -14.59105 | -48.33349 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f95f749-a54a-302c-a3f8-539cc939229b | -17.97593 | -45.01398 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67d57502-658e-3eb5-b432-e485c05cf8f8 | -14.48462 | -48.40698 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b8d41dc-f971-3d06-ab58-e332cf4207d5 | -15.22165 | -48.27981 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72adac99-4521-39cf-ab04-77ae2519dc1a | -14.57724 | -48.31287 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 315ee4f7-26cb-3553-ba5a-e1efc896cfa4 | -15.18789 | -46.39949 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b45e4de5-6ce3-34d5-af5b-91e3c365c66a | -13.57848 | -48.19541 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42e4c9db-9887-3fb0-802f-34a7808f1c57 | -13.06976 | -47.0178 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 774fb77d-b502-38ba-be53-207f844049a5 | -15.7823 | -43.6829 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a34d3ef-fa61-31ef-85be-40fea9251368 | -11.90575 | -47.88895 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db60bb0d-f075-3e33-ba8d-f5b9fb0b92a4 | -15.39866 | -49.20245 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 977615b4-c9dc-3651-95d4-35e14b591abb | -13.1567 | -47.82388 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4f71e765-5bde-356f-87d3-0da423f40d3f | -13.37271 | -47.28673 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c926744c-3480-3748-9477-a755ff733b5d | -14.30141 | -45.89935 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab99c209-ff93-36b8-acab-d7a50967b28b | -13.52862 | -47.27817 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bf72425-d5d7-31b3-9ca0-ba4c850f088a | -12.50407 | -50.2553 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f06597cc-5399-392d-b1b8-1dbad897cfbf | -14.41093 | -46.10208 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f3986b1-26b4-3ea4-8f08-198a4c0e0018 | -14.18067 | -46.66159 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f4f851b-db73-3523-b407-1f39ddf7c970 | -12.68769 | -46.91311 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 635b89b8-ea9f-31b9-b99e-d403ed8d075f | -13.71512 | -48.6319 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 560e44b7-26c4-3f37-9527-e60e88ba963f | -12.95912 | -46.37469 | 2025-10-02 04:32:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfccc43d-4f23-38f6-b639-a93632166c15 | -16.06188 | -51.00877 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c21466ad-e725-3bea-879d-a87075d20290 | -15.1472 | -48.38887 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 762d8d02-d9bf-3036-95c3-df43f3e7de78 | -14.65541 | -48.12079 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7974d40a-deb0-32d7-99ab-cabbae59183d | -12.00789 | -46.64761 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb13aa9e-8fb3-3237-871f-ee7af81ac8dd | -12.19 | -47.90557 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bff468c-f3fd-35fd-8e0b-7834a5d34934 | -12.27739 | -45.37964 | 2025-10-02 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23f5a297-f3e5-305a-9feb-edbb7f6601ec | -15.35275 | -47.08773 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 570f8358-8644-31a2-9413-2a35d3012890 | -19.59823 | -45.89577 | 2025-10-02 04:32:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 444af6da-8c79-33b0-8fcc-e0d49ace5028 | -19.05185 | -48.13456 | 2025-10-02 04:32:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14a80d99-136e-319c-83d7-72899ad7f5b6 | -12.68777 | -48.57579 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9f74cc13-7525-3902-8ae1-c0db187596c2 | -13.96255 | -48.11611 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 842d9fe9-827b-338c-87c2-ccbe5ae9466f | -13.16059 | -47.82088 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d6fe50b-0dbc-3d5b-83c4-91cad75cfef2 | -19.45909 | -44.27797 | 2025-10-02 04:32:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3529310f-62a6-3350-b87a-ed83e1d3d3fc | -19.5933 | -43.81129 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4997dad5-f4f2-362c-a43c-79979d35be65 | -13.24528 | -47.32427 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d67cb9d-d0cb-3475-b8b6-c37af4a713a0 | -13.74998 | -48.00492 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbd4f6a5-5751-35ef-9485-e83b3f200073 | -11.85266 | -48.02914 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7628be95-a18f-384d-b0ec-8caf0e750313 | -19.85446 | -44.08202 | 2025-10-02 04:32:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a448c7f9-5af7-330d-b0ca-53d8e0a8c135 | -14.35596 | -43.8384 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a5ca9f1-c700-370e-ae1c-827370d82e90 | -15.21716 | -47.1789 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94266654-54de-39f0-881f-273f5982b036 | -13.87043 | -47.94778 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbee9f81-3f2b-328c-ae51-74e687cfc70f | -11.90964 | -47.88596 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 475e883f-bd81-3203-b3d9-c58c0c192dfc | -15.26343 | -49.30595 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README95.md)
