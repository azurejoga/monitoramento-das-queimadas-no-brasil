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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2a4a841-28c5-3fc6-91b5-3c0ce8a51ff8 | -12.93538 | -54.77457 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7040342f-9e90-3d07-836e-2a00e2c9808c | -12.95098 | -54.81792 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| cf688c88-2cb3-301b-9b2a-8bf6a0181ffd | -12.4729 | -53.85919 | 2025-09-08 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a0fac4f5-1cf1-377a-826d-d1a3f805f23e | -12.94951 | -54.80672 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| d52f70fa-5923-3c11-a98a-d54f0d58c3ea | -10.45571 | -53.63292 | 2025-09-08 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d9d5cbb1-ec36-3647-95d6-afd0874344fe | -19.44728 | -47.88609 | 2025-09-08 00:50:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| beaca961-4684-36c7-bf35-f059d16f7934 | -15.25058 | -53.79877 | 2025-09-08 00:50:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cb3279ce-b623-3673-861b-4c328f524411 | -14.50891 | -48.78769 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b7e81c1e-c0e6-31bb-8fcf-2f9b15f71491 | -14.80909 | -48.1879 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 47976bfe-ab58-3ea7-8723-f2fdb32724f2 | -14.51981 | -52.02361 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e334daf4-38a7-36de-8307-919dd584f960 | -12.62078 | -56.98816 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| d04ed4e1-f5bc-3c00-a418-36beaa4d90ed | -9.99706 | -51.64576 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 601c9b6c-6ab6-3970-b011-3552fc775053 | -8.74445 | -46.68478 | 2025-09-08 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 1927c78f-e48b-3bc5-9969-805ba3ce2b15 | -12.93829 | -54.79688 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| c715a5cf-2ac6-30f0-ab2d-37fc5d3e77d3 | -12.92565 | -54.77597 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3699b7d6-5ed6-348f-b16e-ff21980f6d1e | -11.13077 | -48.38866 | 2025-09-08 00:50:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| e639a547-0606-3f2e-83d7-e5bb304ea8ae | -14.47039 | -48.7937 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 00c3fbfc-643d-3ab6-b16f-3d8bb5b42be9 | -18.02913 | -47.12843 | 2025-09-08 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dd99050f-8132-3f78-9d51-f747788d04ae | -11.31711 | -55.12472 | 2025-09-08 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| de93c06a-a22a-3bc5-8878-0f0c7bb6df3b | -14.99883 | -48.02261 | 2025-09-08 00:50:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 69395782-6a47-3ff3-ab04-dfa6c4717b81 | -15.11612 | -52.3504 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 63cb501b-70b4-3468-8ef7-3c73a1557352 | -12.94512 | -54.77325 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 986d69a6-db9c-3aed-88fb-1a1525adcdd3 | -12.75845 | -52.9595 | 2025-09-08 00:50:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d53576db-d610-34f4-a718-6a67ec21b4a1 | -10.80368 | -47.73501 | 2025-09-08 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ebbb512a-2273-319c-9b95-342428d715c0 | -12.95661 | -54.76601 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 689a22bd-d5f3-37b3-a477-1e122584e9cc | -12.63217 | -56.98664 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.8 |
| f4b8e74b-80c8-3e9a-a4b6-014f5d5ed912 | -12.82389 | -52.89666 | 2025-09-08 00:50:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c5a26dbf-ceb9-3b11-8436-e395852ee89a | -15.83659 | -52.3079 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b798f479-6be6-310a-9148-3eebaebbc78d | -11.2792 | -46.45969 | 2025-09-08 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| dce1052f-0758-3bcb-bc69-1003382d670f | -14.51778 | -48.75841 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 1bc9a95f-6efc-36ae-937d-dedc4204c07b | -12.93394 | -54.76353 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 372aa5b8-2e7a-3e04-94db-007c77ebe4e3 | -14.51476 | -48.80306 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 5a12d501-64bd-33e3-9e40-b409aae9ba45 | -12.61891 | -56.97266 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 339.6 |
| 01a1aea8-30c4-34d6-8557-421e7dc13df5 | -11.21031 | -55.01184 | 2025-09-08 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 7020fccd-616f-357b-99c0-a4e0e14e6ac0 | -9.9615 | -51.20039 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 845d4ca3-05df-3e7e-bbc4-a2f9469ad293 | -14.88247 | -55.82732 | 2025-09-08 00:50:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 8660a781-1632-3334-8e9c-85e4389997d0 | -15.68863 | -53.55808 | 2025-09-08 00:50:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9dfae9b8-69f2-3063-b1ff-2263c2d5c035 | -15.76062 | -53.55296 | 2025-09-08 00:50:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d1839afb-6f95-3afc-80ea-0e7cc27fa805 | -17.26275 | -46.70682 | 2025-09-08 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b094cd31-e6b5-31a1-8aaf-4c62bbd11537 | -16.91154 | -45.83702 | 2025-09-08 00:50:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d2c332a8-ec1e-3888-ba66-992219b32571 | -16.33457 | -52.94237 | 2025-09-08 00:50:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a4c6db8e-fafb-3ba9-bff9-82ba4bb9bf45 | -11.39641 | -50.40258 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9ad254cd-25a6-3539-a653-99935af8f7eb | -9.44419 | -49.44719 | 2025-09-08 00:50:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8ab79722-ea11-3752-a512-46ebd41a12df | -12.82886 | -52.93364 | 2025-09-08 00:50:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 19d138e0-b52d-3697-8680-954a4653db5b | -11.2718 | -46.44942 | 2025-09-08 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 5ce9e61f-dd02-3b8d-bae6-79ba4e671a23 | -9.88808 | -56.13969 | 2025-09-08 00:50:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7c6559ea-0788-34b1-ab50-7508b4920bec | -11.13928 | -46.35059 | 2025-09-08 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 1a601059-663c-3b1a-91e0-01b5572a3ce3 | -9.55711 | -53.59526 | 2025-09-08 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea3b1566-e6fa-3ed0-955e-93e848b15019 | -10.32751 | -52.56304 | 2025-09-08 00:50:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6d7428ef-dd93-3316-a251-441b298a2f5b | -17.56888 | -44.5313 | 2025-09-08 00:50:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b8778a97-1b37-3bd5-8ab2-30994d599e75 | -14.51311 | -48.79231 | 2025-09-08 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 1db3d827-9e36-3619-93e0-470bd7c4db5f | -11.3717 | -50.42628 | 2025-09-08 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| d19619d9-6842-3b0b-8b79-e513f11f04ce | -13.83024 | -43.87437 | 2025-09-08 00:50:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 060d1627-370d-3bc5-b128-4cb48ca45c77 | -17.83812 | -44.26117 | 2025-09-08 00:50:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9bbd57a7-b5b6-351a-9945-beaac7220719 | -12.94825 | -54.77838 | 2025-09-08 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 52c67fb4-8b9d-3f96-b118-4fc068e951a0 | -11.28205 | -46.47704 | 2025-09-08 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 639506f3-ddbf-33a1-8774-d01f0ff95e90 | -10.29017 | -48.80778 | 2025-09-08 00:50:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| d0223195-15d0-3481-a04c-8014427ebee7 | -12.83011 | -52.9429 | 2025-09-08 00:50:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 0eb4d9f2-7b8d-3fc5-9d8a-3b786121e984 | -11.05216 | -54.17382 | 2025-09-08 00:50:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9b4c510d-88a1-34e7-9344-f4672087dedd | -15.83404 | -52.28904 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9f18702b-0d2f-330d-8d9b-9a46baac82ac | -11.45492 | -49.25301 | 2025-09-08 00:50:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 43c96708-b475-38eb-926e-ec3f837401bc | -18.02512 | -47.1026 | 2025-09-08 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 2795203e-4675-3e32-a2c8-0e743013e6c1 | -19.45106 | -47.87908 | 2025-09-08 00:50:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 86163023-e3a8-3576-8e4a-6a8a5d011ebf | -12.82265 | -52.88742 | 2025-09-08 00:50:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bc341f40-1469-32f5-80a8-b6d2f8cdb8f2 | -9.96018 | -51.19108 | 2025-09-08 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a825ed3b-4b52-3e21-9d93-836b1193da98 | -17.5787 | -49.79268 | 2025-09-08 00:50:00 | TERRA_M-M | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 32a4e687-135d-3128-9d15-a86a9b348782 | -11.41376 | -43.64737 | 2025-09-08 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 7d19b652-858b-3d5b-9b16-24bfb77aaee6 | -10.47117 | -53.6118 | 2025-09-08 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 2b2ed9f3-33b5-3265-8927-2def15f019bb | -14.99696 | -48.01046 | 2025-09-08 00:50:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5944efab-9a20-322b-9f1f-c6769b0cede2 | -14.73281 | -47.76746 | 2025-09-08 00:50:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c670b4cb-5a29-3e70-9247-82139336685c | -16.34245 | -52.93108 | 2025-09-08 00:50:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 81a8d0b4-4b78-3537-85f2-7a541a16161e | -5.0001 | -56.25314 | 2025-09-08 00:52:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8c8f7ceb-55b1-3f33-86fa-4484f30156cc | -5.87717 | -43.974 | 2025-09-08 00:52:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 85954a71-c70f-3d2c-ac1f-d7b1e4f54fa6 | -7.09783 | -49.93514 | 2025-09-08 00:52:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 58fcd0d9-1c8d-3314-8e24-c9be76222e4d | -7.08094 | -45.20487 | 2025-09-08 00:52:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| f4e36d21-ca81-3b5f-ad8d-cb318d99aec6 | -6.20391 | -53.2711 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 64898a2f-2ea4-3640-8dc7-565a25a46f1f | -7.78775 | -52.13062 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a0d404f1-5dd3-3252-9b15-b33dab017bd8 | -9.46403 | -60.48761 | 2025-09-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| d90b3ada-388b-3d2f-978e-a06061504828 | -6.87216 | -47.92768 | 2025-09-08 00:52:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| eb2f422a-496e-34a7-b04e-f9ca1cc3e870 | -4.9919 | -56.26515 | 2025-09-08 00:52:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 14de9f93-ede0-36ed-a8b5-ed6af9b27d58 | -9.60952 | -55.01903 | 2025-09-08 00:52:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| fa356e83-af6b-3cc1-90b9-8d3c831830b4 | -5.21954 | -43.71581 | 2025-09-08 00:52:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| f339cc1e-b7ce-30d5-b629-759e2e288bf3 | -9.44429 | -59.22127 | 2025-09-08 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 4c7ee569-4932-3903-b56f-a6c4228931e3 | -6.62337 | -53.36057 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 74d4bf77-85a7-3ae7-90eb-a23cd3caa417 | -10.08968 | -59.17724 | 2025-09-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 66ee5bba-a1f3-3e9c-9831-ae6593130738 | -6.28148 | -53.42444 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 334d5ea0-82ea-38ad-9677-240622cae813 | -10.09203 | -59.18346 | 2025-09-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 3d8dc0d9-57b0-38c3-a02b-1f46eaf4dd6a | -7.40602 | -61.64614 | 2025-09-08 00:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 191.6 |
| 38fe3e64-93d3-32e4-ab11-32f5bdd1bc43 | -6.63096 | -53.3505 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b65177d5-8a3e-3509-bbb8-f72aaa498ce1 | -9.18092 | -60.78129 | 2025-09-08 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| a3a96f67-dce9-3fd7-bf84-4dc71311506a | -4.44913 | -50.67165 | 2025-09-08 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fbf205a8-149b-32e3-876e-5be327380f1e | -4.26715 | -48.18414 | 2025-09-08 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| b747ce4e-3e20-334a-85df-876af04a6347 | -5.88516 | -46.04022 | 2025-09-08 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 29bf1c84-cbcd-380b-bf4e-4b334e03df34 | -7.73365 | -50.3474 | 2025-09-08 00:52:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2cfb1c08-0fe9-320a-b4b1-68f4097f091c | -6.54288 | -55.00249 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c08da962-3802-35a6-abcd-9d674e574589 | -7.72914 | -50.34338 | 2025-09-08 00:52:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e8e33da4-f121-3469-bd10-c4c65aad1b41 | -8.14009 | -48.47169 | 2025-09-08 00:52:00 | TERRA_M-M | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9dd41686-d781-3ae2-9427-062d0af5c7d3 | -8.07232 | -52.38246 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c89c35f6-2f9b-3ee5-a8ad-f68defb1bad9 | -6.83228 | -52.80891 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0b55ed40-5fb0-3e0b-a207-9bc187b98b01 | -4.2944 | -50.58633 | 2025-09-08 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |


[Clique aqui para ver as próximas entradas](README12.md)
