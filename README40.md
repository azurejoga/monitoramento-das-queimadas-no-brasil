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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3612a5c-5501-36f1-9a08-0ad54e37c253 | -16.1778 | -49.977 | 2024-09-27 01:56:37 | GOES-16 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 8662a69d-74bf-37b4-993c-83473a50b676 | -16.8737 | -58.0235 | 2024-09-27 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 48a1584e-5dbc-37dd-b5dc-a32dd7d0068a | -16.8933 | -58.0213 | 2024-09-27 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| f63db0c0-4ea3-38ce-94a5-2e2fd3098554 | -19.3773 | -42.5809 | 2024-09-27 01:56:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.1 |
| 8b6816b8-96d1-31be-be27-b5f407859d02 | -19.2991 | -49.6765 | 2024-09-27 01:56:53 | GOES-16 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 0392790c-5e3d-3379-9c92-2c22d00aec6e | -19.6136 | -42.8159 | 2024-09-27 01:56:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.9 |
| 08860f78-c1ae-3131-8d17-0a0461b3ef30 | -19.6342 | -42.8103 | 2024-09-27 01:56:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| cb443339-f935-3808-bd90-054d9852109b | -19.5272 | -47.872 | 2024-09-27 01:56:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 8514772c-6335-35ae-95f0-3e8b5932d55a | -21.4123 | -42.9778 | 2024-09-27 01:57:03 | GOES-16 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| b589d6e9-c769-3c27-83ef-03c775cd80da | -22.7433 | -44.8035 | 2024-09-27 01:57:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 125.8 |
| 2152dbdf-dacb-38ae-9991-3d5f390e1284 | -22.7442 | -44.7785 | 2024-09-27 01:57:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| a8b0441b-881f-38d3-9454-3bf102b6b581 | -22.7645 | -44.7973 | 2024-09-27 01:57:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.9 |
| 44fa00c5-bb7f-3766-b158-75f2e23790c0 | -2.358 | -47.5989 | 2024-09-27 02:05:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| f1f9389a-373a-37e7-a945-d579b44be707 | -2.3579 | -47.6206 | 2024-09-27 02:05:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f8364146-6948-37ad-914d-bc753a279168 | -2.8611 | -51.6699 | 2024-09-27 02:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2ae4e105-5e8b-38bf-beee-593f2f280def | -2.6783 | -57.5893 | 2024-09-27 02:05:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 277c3ced-4d1b-3649-b314-8f761a83ce3e | -2.6783 | -57.6087 | 2024-09-27 02:05:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 245a9f6f-b6a4-33de-8e22-ce95cc6210f5 | -2.8795 | -51.6695 | 2024-09-27 02:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| c0565ff2-ceba-39e5-b39e-caeb5708ff93 | -3.2136 | -46.7843 | 2024-09-27 02:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| d48b3635-efdb-30f7-a603-f77eed557e9d | -4.1423 | -46.7007 | 2024-09-27 02:05:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 3dc5079c-bd01-3e2c-94aa-bc0a01e520d9 | -5.397 | -43.4332 | 2024-09-27 02:05:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f55b684e-7504-3f69-9833-2661c4626a8f | -6.8927 | -59.6475 | 2024-09-27 02:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| a8d4c8de-b117-3071-8766-17689a46676f | -7.309 | -61.0862 | 2024-09-27 02:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 34a86eb0-1179-38d8-a47d-a829d01f1b63 | -7.3089 | -61.1053 | 2024-09-27 02:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 074d9b17-7c90-360f-b225-f64107098a80 | -7.2906 | -61.0869 | 2024-09-27 02:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c15a89f2-3fac-3b15-a8bf-5169f393c495 | -7.2905 | -61.106 | 2024-09-27 02:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| abfd5607-90c6-3908-8a6a-6a11acc7388a | -7.2006 | -60.6706 | 2024-09-27 02:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 07da10bb-50b1-3cc3-b9d4-871fc64d3070 | -7.5289 | -61.3825 | 2024-09-27 02:05:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 295ce6b7-0d4e-350f-a1a2-9d398c75bd2b | -7.6072 | -60.5969 | 2024-09-27 02:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0f697f10-e15c-3da5-8fc1-32c3d2eb933b | -7.5888 | -60.5785 | 2024-09-27 02:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 1e42a1b6-690a-32af-a940-497e4652b487 | -7.5887 | -60.5976 | 2024-09-27 02:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 7516c78c-9290-3de3-ad84-1d037f0ba17c | -7.5703 | -60.5984 | 2024-09-27 02:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| dae963c0-d790-3bc9-a1b7-c6ab79dc349d | -7.7886 | -61.1817 | 2024-09-27 02:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 201.2 |
| f4ae0e55-f75b-3869-8114-f6742537964c | -7.7885 | -61.2008 | 2024-09-27 02:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 90959df2-fbf8-3441-a0a2-478eb62ff64f | -7.8156 | -54.7252 | 2024-09-27 02:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 08dcccec-3eae-388e-b487-0945a31965fb | -7.7701 | -61.1825 | 2024-09-27 02:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 178.9 |
| 755dea64-a259-34e2-bce0-852da74ddfa2 | -7.77 | -61.2015 | 2024-09-27 02:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 489877ea-b840-30a7-a6e2-12b9f205b806 | -7.936 | -61.271 | 2024-09-27 02:05:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 751ea263-0d9e-3e9d-9155-368ae89780ef | -7.9359 | -61.2901 | 2024-09-27 02:05:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| a0e544ba-b721-3cc8-8ee0-8933c4208680 | -7.9175 | -61.2718 | 2024-09-27 02:05:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 88863bdc-2d9f-3a05-80e0-fc7784ce2cd8 | -7.9174 | -61.2909 | 2024-09-27 02:05:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| dcb90b16-14b4-33a2-a34f-6b947fefff05 | -8.1579 | -61.2809 | 2024-09-27 02:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9b377eb4-8726-3bb0-b775-90357623ed5d | -8.1394 | -61.2817 | 2024-09-27 02:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| cf676314-e790-35e6-8bd4-c9344c7922d2 | -8.556 | -49.6112 | 2024-09-27 02:05:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 4246e843-aa37-33bd-a783-fcfd12f7bcf7 | -8.8117 | -67.6732 | 2024-09-27 02:05:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 08ed413a-bfd3-3c5b-a95e-5d85d6724fbc | -8.8116 | -67.6917 | 2024-09-27 02:05:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 22ff4eed-6255-35a5-ba4a-2f021b4fb3fc | -9.086 | -61.1245 | 2024-09-27 02:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 20698074-1ceb-3366-afc7-112907faa268 | -9.107 | -67.8881 | 2024-09-27 02:05:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| fcb922a0-16b6-35db-814a-faf7bdeda890 | -9.6206 | -50.1334 | 2024-09-27 02:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e79223f7-988e-3e6e-9493-3a751243bf8b | -9.6018 | -50.1352 | 2024-09-27 02:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 7f84e395-1d75-3658-8139-af68ef3b5f17 | -9.5829 | -50.137 | 2024-09-27 02:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 27b8e4bf-1e90-392f-a23e-b1f90566f1d0 | -10.0513 | -53.4638 | 2024-09-27 02:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 125ad739-a4e6-3d31-8900-73f72387aacd | -10.0327 | -53.4448 | 2024-09-27 02:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0f3426fb-aafc-3172-b731-9a83ccd2bd82 | -10.0324 | -53.4654 | 2024-09-27 02:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c7a0b5b9-181e-3c1f-9cd4-d6a1efefebd8 | -10.0322 | -53.4859 | 2024-09-27 02:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 2852eb10-4328-33af-b87f-f9e8879ea38e | -10.3672 | -53.7858 | 2024-09-27 02:06:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 4ebd60ac-87e0-323b-80e7-04f189ad402f | -10.4799 | -50.751 | 2024-09-27 02:06:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| ab38b27a-d9ab-314b-ae71-947638d76d5f | -10.6643 | -45.861 | 2024-09-27 02:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 1007bb72-f404-3172-8e50-26e11720af53 | -10.6639 | -45.8838 | 2024-09-27 02:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| ef60e3af-7b5d-3448-93a3-27a34a5e065a | -10.6452 | -45.8635 | 2024-09-27 02:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 8c97a936-4521-3767-84bd-390b3310505a | -10.6449 | -45.8862 | 2024-09-27 02:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 22d25788-8e8b-32e1-9382-80cdd190fb02 | -10.7211 | -51.0869 | 2024-09-27 02:06:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 132df60e-053e-3def-ae3b-d9ed1bd45500 | -10.9453 | -54.2676 | 2024-09-27 02:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 64eb4390-db98-3a75-b92c-44d53b615af1 | -10.9267 | -54.2488 | 2024-09-27 02:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 227.0 |
| 9b7a82bf-221b-3524-b9e4-e4ea47c1350d | -10.9264 | -54.2692 | 2024-09-27 02:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 211.9 |
| a65a3ed8-ba23-35b8-a677-87fd1572c88a | -11.2223 | -54.7735 | 2024-09-27 02:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| eb1f34d7-262e-3583-a524-ff458c0ca79d | -11.2034 | -54.7752 | 2024-09-27 02:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 0856a35d-5bb7-3bf8-97c7-d0066206bfd4 | -12.6826 | -54.6763 | 2024-09-27 02:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 74f62a3a-3e83-3752-8fab-f627ffac1ed6 | -12.6824 | -54.6968 | 2024-09-27 02:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 7b6380a7-fbce-3b05-8f09-f25f05ef5eea | -12.6636 | -54.6782 | 2024-09-27 02:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 0b2f22b2-c18d-37d2-94b1-62b8f2fa0d95 | -12.8631 | -54.0195 | 2024-09-27 02:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| fe32bed7-567b-349a-bbb6-711ad6bf862e | -12.8628 | -54.0402 | 2024-09-27 02:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 6871ccdb-facb-3148-a86c-3c4d08cd3886 | -12.844 | -54.0215 | 2024-09-27 02:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 0ed0b885-38b6-3858-ab6b-7f46c0f5db36 | -13.4413 | -44.0267 | 2024-09-27 02:06:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 9d257456-03fd-3855-98cb-0cf07075372a | -14.7305 | -45.5061 | 2024-09-27 02:06:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| bbe5ee6d-ba9b-3952-9ca9-dd43c33efe8d | -16.8933 | -58.0213 | 2024-09-27 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 21230da1-d567-33a8-902f-06fb8f7adc3e | -16.893 | -58.0417 | 2024-09-27 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 7fbb9063-c5c9-3f1b-b9f4-22fd4cdf6307 | -16.8737 | -58.0235 | 2024-09-27 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 6fe26de2-ed7b-398b-bdfe-0843c35ed25f | -17.0988 | -56.1919 | 2024-09-27 02:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 7a0c0719-8bf6-33b8-844d-4d288d98244d | -17.1188 | -56.1686 | 2024-09-27 02:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| e2f00ae0-c77f-3b00-b754-f05427430c44 | -17.1184 | -56.1894 | 2024-09-27 02:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 120.7 |
| 50e3e476-05b4-3d4f-879c-df6365a67835 | -19.2991 | -49.6765 | 2024-09-27 02:06:53 | GOES-16 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 2bc3556a-26f3-3734-bcda-13d06dae0828 | -19.6136 | -42.8159 | 2024-09-27 02:06:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.6 |
| b43f3632-bbca-318f-8d61-548a9f823974 | -22.7442 | -44.7785 | 2024-09-27 02:07:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| f2266a45-e1bc-35e9-a450-767a724812c4 | -22.7433 | -44.8035 | 2024-09-27 02:07:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.5 |
| 2f3a5549-d452-3926-802f-171b20a3f7ec | -11.5571 | -63.975201 | 2024-09-27 02:14:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1188c034-5f1c-3332-83c5-0740a9fba8f3 | -11.5524 | -63.956902 | 2024-09-27 02:14:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd4880e2-68fd-3056-ba5a-4c6260efa319 | -11.5667 | -63.972599 | 2024-09-27 02:14:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 15d08d72-d0c7-3531-a874-b1ee0512ae42 | -11.562 | -63.9543 | 2024-09-27 02:14:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77a37273-8956-395a-b433-8504545516a3 | -11.5573 | -63.936001 | 2024-09-27 02:14:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 122fd962-2528-36a1-a835-00f4f3f614eb | -11.533 | -63.962002 | 2024-09-27 02:14:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb3ddac-6932-38e9-b132-bef00b5fc768 | -11.5427 | -63.9594 | 2024-09-27 02:14:42 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b3728744-e26e-35f7-8612-2ea1340929e3 | -2.358 | -47.5989 | 2024-09-27 02:15:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| a00d97f2-7819-30bc-91e0-757c30b05da5 | -2.3579 | -47.6206 | 2024-09-27 02:15:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d9c043a7-76de-34f2-96a7-0a28a39d2fc9 | -2.8611 | -51.6699 | 2024-09-27 02:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| fde83877-fc5d-3676-b431-7d2ef69a6af1 | -2.6783 | -57.5893 | 2024-09-27 02:15:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| b49d939b-f404-32bd-97f2-2ee3dd8c31d9 | -2.8795 | -51.6695 | 2024-09-27 02:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 1730ceee-a2ec-3e64-87a7-590d963d0551 | -3.2136 | -46.7843 | 2024-09-27 02:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0e432f86-53f0-3996-9c2e-95fe24916412 | -9.266 | -65.352997 | 2024-09-27 02:15:24 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed935a44-30a6-3556-bc0a-ddf3f265579d | -8.5881 | -63.153599 | 2024-09-27 02:15:26 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README41.md)
