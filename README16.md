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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d867375-11d3-3c9b-94af-a290ad2992e4 | -11.79204 | -51.01436 | 2026-09-26 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a90972ca-e6be-39bb-864f-377099ce22f9 | -14.86446 | -47.13818 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51278ce9-4cb7-39d3-8f04-322a4492a3eb | -12.24188 | -50.35371 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a53ec311-89c8-3d32-8702-1d812fcea20c | -12.27265 | -50.72257 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f6c4ae4-cbc8-30ac-9403-a80054d650db | -12.59866 | -51.9526 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4449be07-f242-3955-b846-b869cbfcebfe | -8.9189 | -43.87592 | 2026-09-26 04:27:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b57b4852-92ad-3165-a397-82f8bc17306b | -16.35661 | -42.56783 | 2026-09-26 04:27:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b63ead1-3690-35be-9a1f-180c503e2f5c | -15.23643 | -43.2693 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 092929c5-a57f-390d-8414-6cd9457321dd | -12.13414 | -50.30237 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b6a46c62-5fd7-3099-9e6f-efcd882f0c9c | -14.87772 | -47.14042 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c92dee4d-7430-3f0e-a857-69d9238de5ec | -15.24076 | -43.26533 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8fa95a2d-e4fa-3cdc-9331-8b9c97b263c8 | -14.86503 | -47.13462 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0bb674d-cbdf-3c8a-884c-a94b5cdbac36 | -12.26936 | -50.72396 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c734f6d8-3e59-338a-981b-cbfecbdb3687 | -15.43152 | -47.90121 | 2026-09-26 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4e543d6-2af9-3449-b8de-bc41884939a9 | -10.41282 | -53.80781 | 2026-09-26 04:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3139260a-5189-33a6-882d-0760327f1588 | -12.13792 | -50.30305 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e645af5d-4664-325c-b34d-a961c33e00cd | -8.23314 | -54.66965 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6187e494-64ff-35dd-9271-269353a1d771 | -12.94605 | -51.06741 | 2026-09-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 1117f744-685f-3d33-a8d8-82ec8dd41355 | -11.03158 | -54.05072 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2ad73500-a564-37a9-82d0-7e519a4c931e | -13.42595 | -43.67239 | 2026-09-26 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01ed9fd5-1d10-3121-bdd4-55d0af85d45b | -14.87166 | -47.13574 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 93d72802-d788-32d2-9244-079647e2030f | -12.94693 | -51.06235 | 2026-09-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 95be65be-8176-3c76-820b-497840b4fa7e | -15.16275 | -48.8118 | 2026-09-26 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da6f2cab-9a05-3317-b7fe-8e3f3446cfe8 | -13.71385 | -48.80272 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91474181-bb46-39e3-8db5-6b742fde14b7 | -12.1274 | -50.29632 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1358ceb4-7aa1-34da-a3aa-425672e904fa | -14.22141 | -43.73905 | 2026-09-26 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb555014-7046-397c-8a66-dca46e8aea97 | -14.32965 | -52.72588 | 2026-09-26 04:27:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ca4a477-6085-3fff-a971-c30249e9aeaf | -9.50478 | -54.65933 | 2026-09-26 04:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e5199e12-35f1-368a-b471-d109b789bab1 | -13.27063 | -51.32587 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43dad034-d87f-3159-b2ac-96f21be97770 | -15.19467 | -49.29168 | 2026-09-26 04:27:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4386aa39-736c-3f91-b152-b30b1bee25a6 | -12.27084 | -50.34438 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ef127d2c-08ad-30bf-b486-cbe6744cfba7 | -13.20408 | -48.32453 | 2026-09-26 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4d999c2-9ce6-3faf-9535-007f95bb980e | -12.27181 | -50.72752 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 489a2d21-b514-3849-b55f-cff0707b1d88 | -12.25685 | -50.3128 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cae05bb9-15f0-3773-8e3c-3376f3ca2cbc | -11.9449 | -50.68981 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e8bd2e8-27a0-3a54-b9b5-a43b060f35ff | -13.92063 | -46.1697 | 2026-09-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d49db07-39b5-33db-97a8-2810fbf4f02b | -15.20526 | -50.2441 | 2026-09-26 04:27:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d402597-7504-3906-b58e-34edea1ba8b1 | -15.24815 | -43.26647 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 10.6 |
| f469ee02-cd83-3c3f-8210-34c62be41db6 | -11.27082 | -54.43203 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99a7dc5c-22a8-3584-8ba2-be9095c505e9 | -9.77247 | -48.18664 | 2026-09-26 04:27:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a82506e5-b5b5-33ed-abe9-3bd6a3fe663b | -15.24012 | -43.26987 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e9d9aed6-1882-37d4-b4ba-da148534c6e5 | -15.2512 | -43.27154 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 084ecf4b-b282-3892-9ec8-119c1bdef603 | -12.01642 | -50.64669 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87884fd2-bdf8-3b25-a462-c84b19558c25 | -15.42994 | -47.88987 | 2026-09-26 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45b79b3d-e8c5-3baf-b072-74206d57e878 | -9.54175 | -56.1624 | 2026-09-26 04:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c31ec270-b335-37bc-87bc-75cd0f5537e9 | -11.79088 | -51.01047 | 2026-09-26 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 439e36af-ee42-34a2-98e9-51d99a5e2e03 | -11.76756 | -50.64281 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa1af63b-050f-3504-bc9b-3e969fd4b8aa | -12.76565 | -52.82261 | 2026-09-26 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61e39c12-2672-3815-a125-54b70ab9e72b | -12.27024 | -50.71902 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0d64588c-d64e-3dfc-af63-e46bc076b939 | -8.2344 | -54.66284 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c488c2b9-e5d8-3382-a27a-02d9ad43d6d4 | -12.7835 | -53.25014 | 2026-09-26 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0ec0951-7534-3e7a-bf1d-f24fa0517a0c | -11.93575 | -50.59901 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 752356d4-3bde-331a-93ea-893d75b330e7 | -12.26377 | -50.36253 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbf9411e-487f-34b4-a414-8fb81124161b | -12.26756 | -50.36322 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9daece99-b4f3-32b2-bcdc-aed3f9a6cda3 | -13.41886 | -43.6713 | 2026-09-26 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d233d9bb-0230-3fea-ac2d-28a7b1ed8f8a | -12.89734 | -52.06538 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dcdb289-bb5a-36a2-a44e-266373fd8a37 | -11.66987 | -43.75689 | 2026-09-26 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2abf08c4-27e8-36b2-be1f-4b7ba3531274 | -11.88944 | -50.59061 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f478909c-470c-33ad-a013-ecd01d8c83a8 | -10.41666 | -53.81427 | 2026-09-26 04:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c858ec7-4208-303f-b21d-9717b0935dde | -9.53672 | -56.15724 | 2026-09-26 04:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26249ccf-7d4e-3752-86ab-1d8852d9d973 | -11.86059 | -50.54296 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58d3286a-7ca3-354d-b8da-de936979145e | -12.156 | -50.31116 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c703b0b3-1079-38d7-ada9-91da3e4c3542 | -12.59169 | -51.94341 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e62573b1-5174-3843-9e40-75c67ed3bd59 | -11.93191 | -38.30228 | 2026-09-26 04:27:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 9110acb8-4d7e-3995-9cf6-17cb48757d56 | -11.94014 | -50.69406 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83e24b1a-50d1-357d-86c7-784112537032 | -12.18383 | -50.33073 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a540a43-70a6-389c-bcb0-cbb9e0713480 | -14.86899 | -48.20684 | 2026-09-26 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cda11c6-7d80-3bfd-b3ce-54b29a8c1a4a | -12.19437 | -50.3375 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bb9822f-dcc1-3f09-85e6-118d87ab9c0e | -12.26163 | -50.72254 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| dd7f476b-1a1d-3cb0-9a47-6604d25561ac | -13.70215 | -48.80883 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d891a3f1-1b87-3281-9c85-598020fb2b78 | -13.92007 | -46.17325 | 2026-09-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11d26dc6-c62d-36ff-9e7a-1139f304d956 | -11.94926 | -50.68293 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 640456db-fc1a-315b-945f-48cf4952ab29 | -11.92704 | -38.30167 | 2026-09-26 04:27:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cf989f2b-7934-3a69-b1d9-da8a20e6552d | -11.9553 | -50.67634 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 189148bb-8d9d-3d94-9718-afd2255ca328 | -15.4221 | -47.8959 | 2026-09-26 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acba75e9-3816-3460-8a00-f971700028a2 | -14.83233 | -43.30772 | 2026-09-26 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4898e4d3-7415-36b9-8033-ea1917aab19b | -12.13709 | -50.30775 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a3cdfd75-a470-3bf5-92c1-9625e8d00852 | -12.94303 | -51.06161 | 2026-09-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 6fb109da-cdee-37b0-b888-17ccbe7360a4 | -12.23784 | -50.71619 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff39261f-d9eb-3f94-b62f-51aa6e3e0676 | -16.67356 | -41.85537 | 2026-09-26 04:27:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 656373dc-735b-3e3f-9af1-3fe0de058663 | -11.74305 | -50.62304 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ff47ee9-f8b4-3aac-9836-b7b4b21026b0 | -9.51003 | -54.66035 | 2026-09-26 04:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93d0c5a0-f8e8-3a44-ae00-d0f33c5b7861 | -13.69869 | -48.80825 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58885893-02cb-3ceb-9f18-07c4afee1bc2 | -12.26794 | -50.7268 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| adfa8777-071b-39bb-a5cc-b74058d0dd9a | -11.27584 | -54.43297 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f4ad2f11-239b-3fa8-b9f5-327727e73a88 | -11.79685 | -50.65836 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd4bfe6c-9a8f-3c46-bf7a-54ff5b5b9024 | -12.13331 | -50.30706 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4437ac02-740b-308e-a68b-00b892fc2bbf | -11.40323 | -47.42657 | 2026-09-26 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49bde84c-458e-3919-8d42-4f842a6081af | -14.8744 | -47.13985 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| d1ce3321-1770-32d6-943e-5c461f3b0eb5 | -14.87828 | -47.13685 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ee91b5f-98fb-315a-8d68-ae82146a82a8 | -12.28608 | -50.74229 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 762b6947-bd0e-358d-bc4a-16ae8863d39f | -12.26577 | -50.71621 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cdd6414-488a-3451-b2d9-37bf0fbdcf15 | -11.80462 | -50.65977 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19a5c522-f70c-3dcb-ba8b-fda69d3402d6 | -12.08323 | -50.23864 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 487d3fa3-a817-3d0e-ad6a-98127e3c9e57 | -11.6693 | -43.76074 | 2026-09-26 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bbd1fbf-f0ad-3d45-8c0e-41e084119bc0 | -16.67454 | -41.84806 | 2026-09-26 04:27:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ccbf0d99-7459-3bc1-9ae9-f09697d9453a | -11.85507 | -50.55204 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 902cc88a-a034-3772-8653-99c8de5f90a6 | -11.73618 | -50.6167 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92f7b0d7-ce79-348e-b46f-30926cdba78b | -11.92774 | -38.29623 | 2026-09-26 04:27:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d7b9e907-4922-3ba5-8d34-1204410d24d3 | -12.0233 | -50.65302 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README17.md)
