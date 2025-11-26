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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6b86246-6ca4-3b7c-ae60-3789e4fbe6a3 | -2.46155 | -48.23158 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5ac7ef6-d8fb-323b-8385-4cd79ef254dc | -4.65516 | -43.98298 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8601fb21-0527-3620-ba8a-24d4b1717a86 | -8.54178 | -40.21645 | 2025-11-26 04:21:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1a988b63-b445-3b15-adfe-e63d8e056e25 | -2.47898 | -47.83475 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7d0f424-8cbb-3bd2-a1bb-ea12c8702478 | -5.57364 | -46.28069 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9539c2d5-fd89-35b7-8731-74fabf9b69ca | -3.36893 | -46.25009 | 2025-11-26 04:21:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e47856fa-3753-3625-b7e8-fba2a057429f | -3.02714 | -51.09096 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65c1b80e-b1f9-33cd-a43a-d70349c82109 | -10.20947 | -36.36006 | 2025-11-26 04:21:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ab343bb5-7f8e-3101-ac87-33ede1555254 | -6.57872 | -47.90104 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 52ee0f39-6ade-34f2-ae47-276b9b8cc765 | -4.55886 | -43.29792 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| feaae920-5ecc-3f9c-a3f9-144a1c726558 | -8.05699 | -43.10865 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3984058-45d7-3372-84c0-cfbe30cb68e8 | -4.73972 | -46.42707 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff12d1f7-8d18-3c9c-b350-5f03cf3f406d | -6.07814 | -39.55376 | 2025-11-26 04:21:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 32684f0d-7063-316c-9c13-00927b400bf5 | -4.16394 | -43.73581 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a97b1ce5-6578-368f-8dbf-f4fddeeb13ba | -4.93249 | -49.15192 | 2025-11-26 04:21:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4a2468e-4c90-34f2-a484-5d89e01d0e84 | -2.71444 | -45.69186 | 2025-11-26 04:21:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e904c18-d23a-3c96-9a4e-cb78035bec96 | -3.43776 | -50.17465 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3beb49e9-3b93-3865-8477-a618efeef0c9 | -5.60165 | -35.63918 | 2025-11-26 04:21:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 12b7fd69-fe70-3c30-aa1e-e63620e4b2c0 | -8.04613 | -43.13383 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 07114ad2-cdf0-3cad-a08f-7e0c416bbf33 | -6.30511 | -43.79239 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8aecf43-1e02-36f2-b7f3-69b0e196be50 | -4.09822 | -49.07059 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3440d2ad-0ee0-33e1-afeb-81db3e317a88 | -2.46782 | -47.83014 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59dd59f6-2031-32e5-9070-dd4a871b6027 | -3.50218 | -50.27756 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59519987-f70c-35c7-8fa2-c251be2948c0 | -4.1163 | -44.83386 | 2025-11-26 04:21:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99b71d11-efad-326a-b6cf-0e23226cafe5 | -6.58336 | -46.82642 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1a5b298-b3fa-372c-9c17-e9e0d502e629 | -2.62253 | -49.45995 | 2025-11-26 04:21:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0f1e324-4045-3354-b21f-0fb235fe9109 | -2.98957 | -51.06692 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdeb0855-b6f5-3d79-99b7-15e10ac40726 | -5.50168 | -42.37463 | 2025-11-26 04:21:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f7d85bd4-44dc-3e5c-8503-b7c300cf8e1d | -5.96214 | -46.15245 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09a03cf1-c212-3768-84fd-c35af0afd874 | -2.63863 | -48.45434 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ba1498b-cbdb-321c-bef3-dddf9ba34f07 | -3.66053 | -44.72936 | 2025-11-26 04:21:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe1c066e-5a22-3ff1-9572-7f16360944e3 | -5.17554 | -47.09908 | 2025-11-26 04:21:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2311decb-5883-3730-a01e-eb6f0fe70a9f | -4.55609 | -49.69442 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10500a45-40d9-3519-8a00-8a53381ff4d7 | -4.56075 | -43.80506 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a528e404-f567-34a8-9dc6-9b2404634ce6 | -3.58915 | -40.98678 | 2025-11-26 04:21:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3b96d595-78a4-3e4e-adca-f23cfc4d67a7 | -2.91942 | -48.23071 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9820c600-8df5-3acb-8fd1-3811cd714a09 | -3.02762 | -51.03176 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f16e5a55-d0a1-35f9-801f-2fad9154a312 | -8.0587 | -43.14338 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a68de1b9-1737-38de-8fda-492c7a7daf0b | -6.80817 | -41.7207 | 2025-11-26 04:21:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 76bbcb05-7c82-31b4-a153-86c79b0975bb | -6.30403 | -43.79935 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5312a8f1-3275-3c0b-8fb0-735b2307942b | -3.43575 | -50.18681 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da23b18c-0f31-3deb-b8ef-d35f722f6509 | -6.5085 | -38.82248 | 2025-11-26 04:21:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1400245-7a9f-34f0-b0ec-b0a943dfd089 | -3.13959 | -49.40243 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58c95b43-4d84-3272-9af2-63a69eb9cf75 | -4.01814 | -51.15784 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d88c19e-2576-3bad-b3be-ec3c066a1901 | -7.16581 | -44.99549 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c843ccc8-0ff5-3327-a1cf-7576fb257fc0 | -4.94377 | -41.15344 | 2025-11-26 04:21:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66773fa6-5eb5-3f30-b278-b8d286a7930b | -3.36053 | -49.50721 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57620c07-366c-3d10-8f12-493f7bfe3586 | -4.1399 | -42.54581 | 2025-11-26 04:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 55881303-0c69-3604-8c97-df503416aa2e | -3.6601 | -42.22969 | 2025-11-26 04:21:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 33805a1a-e535-3f8b-a8f8-88a8d1b8a4df | -5.6457 | -47.85849 | 2025-11-26 04:21:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05896744-9933-3d51-b2cb-1f9a48c1571a | -2.69994 | -49.51944 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 169d56a1-651d-3431-987e-7d7d548e833f | -4.707 | -43.99815 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c4bc474-6cb6-3fce-b504-932082b21eb3 | -2.93863 | -48.23375 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2224c030-4d32-38f0-8684-63734bbfd7fc | -8.03584 | -43.10924 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ba2bb38e-d057-3ac3-a5f5-647e226b579f | -2.87791 | -51.81059 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94bf3cb1-e4be-3ad4-838c-c822c6c1d9ee | -5.09809 | -44.21158 | 2025-11-26 04:21:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e209dab-bcbc-3d17-8e6c-5bf473d48538 | -3.20528 | -50.21676 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f16d7d4b-20f9-332d-a0d1-8eb346e3b157 | -3.43141 | -50.18614 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b33fb12f-16d9-3e08-bb99-488788225db2 | -8.06041 | -43.13219 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 5487e72c-2c93-3889-b685-cc3b3b4c6cf1 | -3.49164 | -44.50832 | 2025-11-26 04:21:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f07ccf60-4c87-3100-ac70-9893619f7929 | -6.6848 | -42.47147 | 2025-11-26 04:21:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5befdf59-91ae-347b-b177-667dd65ff9d5 | -5.5504 | -38.14782 | 2025-11-26 04:21:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f4e464b8-64b1-3abe-85cb-9232920ff2ba | -2.4895 | -47.81771 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0cb95bb-afec-3ab9-a777-89f5f9002d9a | -5.06372 | -49.88003 | 2025-11-26 04:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c373247-4ab5-34c1-9532-fcca52dc167d | -4.1029 | -49.06687 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c278ab6e-bde4-3b92-83ec-5537171a580e | -4.16172 | -43.72838 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d6cae185-72ae-3f45-9a95-e59b192b688e | -7.56582 | -45.87954 | 2025-11-26 04:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0316dabb-66bb-3cd0-ac91-a1a5affb8c0d | -3.38953 | -47.18917 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca329f74-136a-3bd4-813a-d1464e11f17e | -4.17111 | -43.73338 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 74988c19-0e9b-38da-b37e-8c9a930ca28a | -2.28934 | -47.04363 | 2025-11-26 04:21:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f32f1669-2cc0-32cf-b178-7cad3868a09d | -4.17052 | -43.71558 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d5486a6f-17a8-3325-bb3a-0c09b3ca19ff | -3.5848 | -50.29145 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 928be2b6-1571-3184-807c-0d201c35a1c6 | -3.81395 | -43.7586 | 2025-11-26 04:21:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 89e34442-b36d-3871-ada3-f724e7ccf48d | -3.92403 | -49.22129 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41e5e4e3-5392-337c-8254-215e35e467fc | -3.45057 | -50.55887 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9c01485-3137-3298-8a15-7708d23b5d33 | -2.93777 | -49.36251 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f11f6837-d234-3ded-9b36-4ef32cc86047 | -2.95802 | -45.57293 | 2025-11-26 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d316e5f4-3069-30b1-b74b-426b6280ed43 | -4.89492 | -42.08694 | 2025-11-26 04:21:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a2be9df-daf7-318c-97b4-479e14f7ba4e | -4.15895 | -43.72441 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b72a3dc-f1d2-3e3c-9702-90ada6f8ae3d | -4.17551 | -43.72698 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9ef2425-d841-37a1-8b9d-c97f976ee2d4 | -4.02193 | -51.16333 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e345f019-72f0-3a85-aa1e-28a4f3fd0466 | -3.23343 | -50.58953 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1568244-0c4b-32ef-b66a-d7356795e63d | -6.30899 | -43.7894 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 44534b46-a6c7-32e6-bbea-211bad359ca3 | -3.13898 | -49.40617 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f3bc96b-1c15-30ee-b805-e7b0b66db2f2 | -8.05013 | -43.1076 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6c77b9f3-88e7-37b5-aa74-09bd9aabac23 | -2.89941 | -48.06333 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbb87d75-5bea-3f38-b824-ccf7abe4433b | -6.1671 | -39.51456 | 2025-11-26 04:21:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3f3ab3de-9738-3c2e-89ac-a16caf878e56 | -5.38055 | -45.21884 | 2025-11-26 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7aa5ccb0-74a8-3a10-9dd9-977187c93742 | -8.06841 | -43.12576 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1da2f38-efc4-30a3-bf4c-3bb384f83f05 | -6.957 | -39.21454 | 2025-11-26 04:21:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9c50a438-a19a-3066-9cfb-590c880bfc45 | -2.93247 | -48.22298 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8f2c063-c2d4-3296-abf0-b347d1137b86 | -6.05102 | -45.83277 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd19e28f-90a0-3962-963c-adc1660c742e | -3.59273 | -40.9875 | 2025-11-26 04:21:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 789d8de9-a42e-35ba-9c91-84b4849fb591 | -5.98827 | -44.59933 | 2025-11-26 04:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9ae4145-4d0d-33a9-83cc-76945d544913 | -3.4476 | -50.54935 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 621f0dd0-8164-3060-ab77-47dad40a4d3c | -4.3091 | -45.37212 | 2025-11-26 04:21:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9ae1278-fc5e-35cc-9c18-fe49721b43ab | -5.57207 | -44.97586 | 2025-11-26 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17e806da-0432-3571-9ac1-9c56260b401e | -3.74788 | -46.15835 | 2025-11-26 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3989cb23-2345-30a3-b5ce-b45f642a2a7d | -8.03813 | -43.11727 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e96dc01d-fefe-3c0b-88e9-0277ec75ea75 | -3.44922 | -50.54704 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README22.md)
