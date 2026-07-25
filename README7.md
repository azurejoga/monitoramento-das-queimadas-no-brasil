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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e61d8e7b-3bbe-31f3-8863-ac9b32bc1875 | -10.01649 | -65.05435 | 2026-07-25 04:53:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a6eebf9-e321-3c81-babe-b50b2ba2dd8e | -13.3024 | -54.3341 | 2026-07-25 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7eaf14a1-e12b-35fd-8caa-3dc06acea70d | -12.42512 | -50.41063 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a25f1431-04b1-33d2-9a96-733039dbcea3 | -11.42371 | -47.48521 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ee18971-1da3-3e3f-8555-8abe51d66e1e | -11.72549 | -50.41764 | 2026-07-25 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62425e06-86f5-3b15-a48c-00ff2cfb61aa | -11.41383 | -47.49268 | 2026-07-25 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74418e03-d6b3-382b-9532-f938ea260b73 | -13.19931 | -48.32862 | 2026-07-25 04:53:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d1fd415-769d-3440-b99c-fc5fd201392e | -10.87196 | -53.73821 | 2026-07-25 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2968515b-01c5-32f6-8335-2cc11e9b3e6c | -14.23479 | -51.97667 | 2026-07-25 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b97fa9b1-3c11-3799-9041-6ae85c2295fe | -18.81085 | -53.14428 | 2026-07-25 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 120c6f4b-24c6-39dc-8abe-4ee10062c6c3 | -18.80958 | -53.14334 | 2026-07-25 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81aea6ff-7a74-3a42-bf2c-581d2bc758f8 | -17.55489 | -46.54417 | 2026-07-25 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1684b81-b0ee-3b18-8e42-43453134a83d | -18.8068 | -53.14776 | 2026-07-25 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25803847-26b4-331e-829b-8c46b5ff923a | -19.72568 | -46.16928 | 2026-07-25 04:55:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3749f5da-98ef-386e-a11d-70944ac12688 | -17.89933 | -45.2763 | 2026-07-25 04:55:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef5c4e08-fda9-3041-a2f5-1a6bc043cbc6 | -18.49167 | -51.57515 | 2026-07-25 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab8a23af-e06c-35ec-aef7-7469ae1d27c3 | -21.38782 | -54.57592 | 2026-07-25 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1ce2eda-f690-3fa4-abe8-4d32e536a046 | -18.4886 | -51.56991 | 2026-07-25 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ce71e46-5056-30a2-a033-19bf875390e1 | -18.38131 | -50.34501 | 2026-07-25 04:55:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 60217dc5-8054-37e5-bdcc-caff3aadf46a | -20.233 | -55.41472 | 2026-07-25 04:55:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9546895d-67ca-3c27-8a89-5a14580b2c3e | -18.49015 | -51.57216 | 2026-07-25 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0adb28dc-bdc5-3700-b6d6-2b834eeac23b | -18.382 | -50.33963 | 2026-07-25 04:55:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8903b934-9d2f-3c58-bd8b-da2d85b82ad6 | -18.80901 | -53.14737 | 2026-07-25 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62b0fa5a-7ac3-3045-b3ca-f295a37891da | -18.80738 | -53.14373 | 2026-07-25 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a199ecd-6ec6-3b71-84d3-d2c0cb179eab | -20.19351 | -56.97511 | 2026-07-25 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf1ac3c2-0056-316c-8bfa-01fdd4cd376a | -3.80044 | -51.18431 | 2026-07-25 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f0487f28-99ca-39c4-9a9f-c4d5bcb08e79 | -1.59264 | -50.43529 | 2026-07-25 05:25:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ffea80b-dde3-3d9a-8116-3ebcf7a56b80 | -4.18316 | -48.58411 | 2026-07-25 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 812ec05e-e7bf-38b6-81fe-c759c11729d5 | -4.18257 | -48.58814 | 2026-07-25 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65419c7d-156c-30f7-82eb-27fa06d82c73 | 2.94953 | -60.18349 | 2026-07-25 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 256e42ed-cf33-3f82-9227-f2aba4387592 | -3.72834 | -49.27283 | 2026-07-25 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30af86ef-0855-317e-a15e-9a4ada733d5a | -2.90177 | -54.56053 | 2026-07-25 05:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78184170-aa33-3ead-90ad-f81975d02307 | -3.79971 | -51.18917 | 2026-07-25 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3c36189f-0e00-3343-bc0e-1f542ec88173 | -4.36656 | -47.76648 | 2026-07-25 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ddb184b-11eb-36af-a26d-c7832920502e | -1.58934 | -50.43338 | 2026-07-25 05:25:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9138036-3eb6-3f51-9186-aac91a664e6f | -2.91498 | -52.72903 | 2026-07-25 05:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eaf4725-a0a2-3a9b-98ce-427374a30a6e | -1.7844 | -55.52595 | 2026-07-25 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4c990ae-a1e7-36a6-9450-68bbfcdc2a53 | 2.72869 | -60.86624 | 2026-07-25 05:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac7a8ba6-3a33-3667-9d35-62d8e9299a0c | -2.80785 | -48.66956 | 2026-07-25 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6948061-13d0-3f9e-a86c-903b8c2c22fd | -4.37195 | -47.77185 | 2026-07-25 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 02a1c7f5-6ef1-3d79-8a74-3e563f1b9813 | -4.37258 | -47.76748 | 2026-07-25 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6e4e0aab-4262-3ba2-8a93-fadec820a3e1 | -1.54365 | -54.16154 | 2026-07-25 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 098dd979-733f-3168-a115-2d348563349c | -1.54354 | -54.16401 | 2026-07-25 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 13a3bfaa-5baf-3680-83e7-bfaca183b8e0 | -3.73377 | -49.27356 | 2026-07-25 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cb8be06-49c1-3351-af73-26c822aa4833 | -11.7013 | -49.02139 | 2026-07-25 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c72004bd-0920-3146-b339-b01885b7eea8 | -8.89294 | -60.60337 | 2026-07-25 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a748682-7fc2-38e1-877f-8cd62a57e32b | -9.16416 | -58.32439 | 2026-07-25 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 789f0642-412a-3895-ac9d-fbe2f989a8c8 | -11.7998 | -47.09584 | 2026-07-25 05:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 844f3c5d-5b1d-3a0a-b8ba-aa498781a490 | -8.89351 | -60.59983 | 2026-07-25 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a52452e4-6151-3365-af02-dfb85b8425fc | -11.80689 | -47.09557 | 2026-07-25 05:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43814387-027a-34bd-89ee-b08b8571872f | -11.60656 | -50.15222 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 727c0e43-200f-3fa0-848a-ee6d862c63c1 | -9.47917 | -57.32155 | 2026-07-25 05:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9545f76e-c05a-3dfe-af5f-9ed28266c837 | -9.18994 | -58.06559 | 2026-07-25 05:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1154c6b-b1ac-3e86-930b-13424b1c80f6 | -11.2011 | -54.04381 | 2026-07-25 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7f41848-566a-3695-9e78-6a28dc962552 | -11.80672 | -47.09652 | 2026-07-25 05:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9df83e73-193b-3c25-9344-e933017636a6 | -11.71653 | -50.42168 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f99e2a09-3fd0-335c-83d6-2275d3f33a48 | -7.8669 | -61.49325 | 2026-07-25 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d742bab-8f26-3b33-be8d-6f61cd274350 | -10.0036 | -51.47268 | 2026-07-25 05:27:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3646eb3b-d468-3b5a-ad8e-9132469f385b | -11.71968 | -50.4198 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f239326-a926-3bac-a8cd-f3b875c166db | -11.80056 | -47.08926 | 2026-07-25 05:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 368b60ba-3f10-331a-a6d8-b362132cd202 | -9.10081 | -59.40578 | 2026-07-25 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d01677-50b5-35ca-8085-4e7b5624fca9 | -5.08956 | -47.94588 | 2026-07-25 05:27:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6d278a3-f121-33d5-8ed8-667923a6e1e4 | -9.16078 | -58.32386 | 2026-07-25 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9263e234-f118-36ef-8044-7e25bd9a2cab | -11.72578 | -50.41672 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1235fe70-1b02-3b0a-ae42-47b522c8998c | -11.70011 | -49.02257 | 2026-07-25 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea26b0e0-685c-3d10-89b4-458de93f255c | -10.06141 | -60.4995 | 2026-07-25 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b7673ba-c50f-3cb3-89c6-151b354ce7cf | -10.00793 | -51.47945 | 2026-07-25 05:27:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1586bea1-16e9-3c01-9474-8c7da80e927c | -8.41001 | -61.31735 | 2026-07-25 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d98f4cd0-f9a1-3e40-a96a-ae5e77c229c0 | -11.7253 | -50.42053 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15f8021f-5704-3d6b-b47c-5c4533633ffb | -10.00524 | -51.47876 | 2026-07-25 05:27:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a936344-857b-3afd-96c5-1d0b0db61d90 | -9.87981 | -49.98182 | 2026-07-25 05:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54d798b2-a8cb-3858-a140-4b1cac1f8d1b | -11.71406 | -50.41907 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71471e8e-15ee-3af5-8da3-ae1ced8006ab | -9.08538 | -59.4821 | 2026-07-25 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 252857f6-b913-34f3-8fbb-4d3221c45878 | -11.71358 | -50.42286 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7fa31422-9413-3394-b121-c5f4ff5301b9 | -11.80068 | -47.08824 | 2026-07-25 05:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f96648ce-ee98-3ffa-bcdf-6baa0627b385 | -9.00902 | -64.13411 | 2026-07-25 05:27:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8bac5bdd-793f-3d58-896b-af47f24cf384 | -10.05864 | -60.49544 | 2026-07-25 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fa354cd-8608-351d-a366-5d6c2b441826 | -11.60754 | -50.14426 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13c80bf0-a73f-3cb2-a298-2f57f7726e89 | -8.89685 | -60.60038 | 2026-07-25 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e62a853-2ff2-3983-ad03-73ff97dbb8ed | -11.72777 | -50.42317 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a190b50b-d2e6-3cb3-8f36-842c2f4dd772 | -11.79996 | -47.09485 | 2026-07-25 05:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 86c2870c-e6ed-3140-aaed-5a3c7bc3a60c | -9.16133 | -58.32022 | 2026-07-25 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7fcfe9df-0f4c-362d-a492-6c4c7181efa7 | -11.41221 | -47.49169 | 2026-07-25 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8039dd29-d200-387e-b521-dc295382f7fd | -9.17826 | -58.3229 | 2026-07-25 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8285c647-b48b-3803-a1be-3619fca339f9 | -11.73043 | -50.42506 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f3a345aa-f388-3c07-b539-9f92ec6f3647 | -9.16472 | -58.32076 | 2026-07-25 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b1a879f-274c-34cb-9989-3968e2f8ffdc | -5.09017 | -47.94153 | 2026-07-25 05:27:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d7ddb21-0d84-3df4-8c22-525340aa9c19 | -11.72822 | -50.41936 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c5c0f308-7a7c-3e2c-8b39-9c4cba558caf | -10.07748 | -60.50572 | 2026-07-25 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56bfc3b0-9324-3c90-896e-1cc6a7193c4e | -9.47978 | -57.31761 | 2026-07-25 05:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 462f2dd3-cc17-3865-903e-3f5db4a90f1b | -11.69512 | -49.02087 | 2026-07-25 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0f7776d-863f-322d-89e4-8ce966a588b4 | -9.00819 | -64.13902 | 2026-07-25 05:27:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 33f89df8-33e5-357c-aa34-8043ff6b777b | -11.73092 | -50.42126 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd938d0a-b9b9-339d-a250-4e30c73a0a11 | -10.00565 | -51.47573 | 2026-07-25 05:27:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d853a47-92df-316f-9b2b-eb76318750a0 | -9.47626 | -57.31705 | 2026-07-25 05:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b0408bd8-0e46-330b-aacc-9517126a02a4 | -9.88545 | -49.98258 | 2026-07-25 05:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec3bd9ca-7122-39c7-98da-03ec0b38949a | -10.07415 | -60.50518 | 2026-07-25 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 122e1270-6b56-35bd-a6ff-b7260cb6c3a9 | -9.17487 | -58.32236 | 2026-07-25 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 604090f0-431c-3b30-a18e-2e91a33c0ff8 | -11.60705 | -50.14824 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7bfc1d5-a71f-3809-94c5-3359ed317bd5 | -11.7226 | -50.41862 | 2026-07-25 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README8.md)
