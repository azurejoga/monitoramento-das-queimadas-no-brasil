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
| ee7144dc-1736-3c37-afc8-139ba8d8f971 | -2.96346 | -49.1775 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5f7700af-fb3f-3895-9b28-a1c8316a2f76 | -3.177 | -45.60957 | 2025-11-29 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0951ba9b-c98c-3e75-b478-3391398d3e39 | -3.66261 | -50.22297 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 79f31a18-cf74-380f-9350-ec48fe7dfc04 | -3.39027 | -50.25276 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d48f54e-5caa-3c30-9447-968cd4eab58b | -4.16956 | -43.73982 | 2025-11-29 00:34:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6ef70db2-0867-33ce-b2d6-de652d1e5725 | -2.63806 | -48.55101 | 2025-11-29 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 6338ef3c-613e-3317-8c45-b13ddd374ba3 | -3.37919 | -50.10794 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 906a78b6-1ee0-300e-8ffd-39697c1d6dce | -1.50134 | -47.80149 | 2025-11-29 00:34:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 15a172c3-7e70-3e64-96b9-2533286c7a3d | -2.54638 | -46.00061 | 2025-11-29 00:34:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 32b551d5-4eeb-38f7-b800-791303c069e3 | -2.48357 | -45.97719 | 2025-11-29 00:34:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 9adf0436-f386-3c3c-ac98-c0d082bfd972 | -3.33388 | -50.24838 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5d5dee2-597b-388e-a16a-d80e8f7bfe14 | -2.96778 | -45.26548 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d51e9472-a427-3735-82b9-962a3317cc3d | -1.37197 | -52.51138 | 2025-11-29 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 83adf2e0-204b-3b29-ac17-fbf740460490 | -2.63316 | -49.17913 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 303c7aab-7e75-3f28-a0af-4adbd354d1ac | -1.49107 | -47.80301 | 2025-11-29 00:34:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b3092742-483e-3e22-abc9-009e75a9987d | -1.76213 | -54.78228 | 2025-11-29 00:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bce8a17a-5694-3ef0-a217-97f9dc8072f3 | -2.89339 | -49.46804 | 2025-11-29 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b37e8240-4473-3b67-b67f-d7447eadcc1b | -1.35039 | -53.09545 | 2025-11-29 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0208a494-32b5-3c70-849f-57c4b7025034 | -2.74417 | -47.13515 | 2025-11-29 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 62a68087-acdf-380f-826a-ec592fd13422 | -3.46021 | -47.62936 | 2025-11-29 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 5e7a97ff-d94f-32f9-bf01-21827ddd74f5 | -3.29362 | -50.08922 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0249e9cc-a2d9-3015-98bc-515b01772969 | -2.3954 | -49.39015 | 2025-11-29 00:34:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cc7520c3-99f9-3f6b-a012-9b013006f70e | -3.56095 | -47.1755 | 2025-11-29 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7c2d0d51-944d-3d63-9440-60668a32e8e9 | -2.60003 | -47.33783 | 2025-11-29 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| d0ed4af4-7079-3d5a-bc3b-de653288f847 | -3.10956 | -45.77713 | 2025-11-29 00:34:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ca5c8f05-de38-35d6-82c7-457f0f78a871 | -3.22816 | -50.15063 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3416b86f-200b-3550-843d-0b0a84800a31 | -2.33919 | -45.70257 | 2025-11-29 00:34:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| e4fefd85-9705-307c-a7cf-9ab34c3471b4 | -2.47178 | -46.2875 | 2025-11-29 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bc71c8b9-6117-3daa-8183-427894eae9b1 | 1.66864 | -50.71329 | 2025-11-29 00:34:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 68fc9c1d-fb92-3765-8602-95c182d3f923 | 0.49202 | -51.16669 | 2025-11-29 00:34:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ed007411-c80a-3062-a4f2-6d5a521dca84 | 0.49324 | -51.15781 | 2025-11-29 00:34:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1e4c0caa-5188-38a1-b3cd-88b96fab2aeb | 0.85723 | -50.18524 | 2025-11-29 00:34:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fe5cf103-6a49-38a4-ade0-311d4edaf45d | -2.6322 | -48.542 | 2025-11-29 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 0874d688-ce76-39a5-a0e0-9215068c543d | -8.0324 | -43.1022 | 2025-11-29 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| bb696339-bd08-3ba6-a937-1182cee22811 | -1.4923 | -45.7903 | 2025-11-29 00:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3e6f761e-4849-353e-890e-6414567cbbe4 | -17.6155 | -46.6607 | 2025-11-29 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 7c82da7b-43fb-3e1f-b9da-452a33e93d7a | -2.9116 | -53.0606 | 2025-11-29 00:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f897ce37-ccc7-3c7d-a440-09206db4e214 | -8.0507 | -43.1472 | 2025-11-29 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 211.8 |
| 2144e76f-ff0c-359a-a4c3-8a542130f38b | -8.0318 | -43.1493 | 2025-11-29 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 322.0 |
| 17f5ebbd-537e-3cad-a6ad-ad0579d57501 | -20.4496 | -47.523 | 2025-11-29 00:40:00 | GOES-19 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 474075b9-f258-3c38-a9a9-32f7e12ae254 | -20.2016 | -52.3717 | 2025-11-29 00:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 115.3 |
| cc0cf4d1-8b4c-3fd7-9fdc-d438c479b580 | -8.051 | -43.1237 | 2025-11-29 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 373.5 |
| fc113f33-bd42-336c-8472-ec8b5341ded1 | -2.3459 | -45.7036 | 2025-11-29 00:40:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 1485bf10-bfc5-38c5-ab33-e4012fcf295f | -20.1807 | -52.3975 | 2025-11-29 00:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 128f0a10-847a-3f68-b649-417ab8f5119b | -20.2262 | -47.5051 | 2025-11-29 00:40:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f484b0a4-16d7-34af-bd5a-fe032aa7487b | -20.1813 | -52.3754 | 2025-11-29 00:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 212.6 |
| fd35b158-5058-3a8e-a7f1-71b546e156b8 | -1.4737 | -45.7907 | 2025-11-29 00:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 98007021-342e-363e-9730-26a2a28d75c8 | -3.1068 | -45.7903 | 2025-11-29 00:40:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 95.3 |
| b3b2babe-99ce-34a0-b22e-e26f87e21012 | -3.1069 | -45.768 | 2025-11-29 00:40:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b8946c42-8622-37c4-92c5-0d4c319218cf | -20.4503 | -47.4995 | 2025-11-29 00:40:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 136.4 |
| f85266b3-0f7f-35f1-95cb-8486ace3e901 | -20.201 | -52.3937 | 2025-11-29 00:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 68.1 |
| b1b43afd-8c36-374c-848c-230da2e58caa | -8.1633 | -43.2055 | 2025-11-29 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 4eea05b6-4bef-36cd-9bfd-fdcb85db59ed | -20.2256 | -47.5285 | 2025-11-29 00:40:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 115.5 |
| f3ac97d8-19ba-318d-9c77-246960c3b8c9 | -8.0321 | -43.1257 | 2025-11-29 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 556.8 |
| 4dfdc005-9fcb-33f7-9434-d7b12e3aa340 | -8.0507 | -43.1472 | 2025-11-29 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 147.4 |
| 3f852fd5-fecb-3114-bb20-4f72307aec8e | -8.051 | -43.1237 | 2025-11-29 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 355.4 |
| 908873c8-f0e7-3220-ad38-db6891ab02f3 | -20.4503 | -47.4995 | 2025-11-29 00:50:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 6ddd51b1-20cd-33f0-8d08-1a80becc594a | -2.6322 | -48.542 | 2025-11-29 00:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2b8d42f8-7c09-3b89-8eb3-ad80322e9422 | -17.6155 | -46.6607 | 2025-11-29 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d03cb17a-95eb-3fb6-9baf-3e94312d3758 | -20.4496 | -47.523 | 2025-11-29 00:50:00 | GOES-19 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 64.2 |
| f839dc6a-3ed6-3d13-b1b0-ff7a36e4a7c8 | -20.1813 | -52.3754 | 2025-11-29 00:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 174.2 |
| ea79d7b3-4b3a-320a-b777-2db61ff8e254 | -2.9626 | -49.1736 | 2025-11-29 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 8865a202-f1b1-33a8-ac37-f9591011b777 | -8.0324 | -43.1022 | 2025-11-29 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 833ca77b-02e6-3123-8ada-0c4c5033a2e6 | -8.0318 | -43.1493 | 2025-11-29 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 205.1 |
| 517d9d01-a892-3c39-ae09-6bd7e1d9c1c0 | -2.7845 | -47.4343 | 2025-11-29 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 96876246-da46-3c58-91f5-ca00036ab46b | -2.7845 | -47.4125 | 2025-11-29 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b3138684-906d-3188-848b-01c127b997ae | -2.9232 | -45.3037 | 2025-11-29 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 1cbe00b1-425c-3ef5-b9e2-b360dcf84f7c | -20.2016 | -52.3717 | 2025-11-29 00:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 821d77e4-e5e2-37da-97f9-efaa5251657c | -2.9116 | -53.0606 | 2025-11-29 00:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| b78cf87d-5ac2-3546-b541-a4fdd3e84956 | -8.0321 | -43.1257 | 2025-11-29 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 518.9 |
| 61e2ee5a-4633-30be-8c99-a3faf5f99ed2 | -3.1068 | -45.7903 | 2025-11-29 00:50:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| a9b3c4d8-8deb-3f4c-b2d6-8dd41c955327 | -3.1069 | -45.768 | 2025-11-29 00:50:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 9daebaca-e1fb-3c35-806b-62fa692d10f9 | -2.3459 | -45.7036 | 2025-11-29 00:50:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 2704d626-0182-36b3-802d-e627e20845a3 | -20.2256 | -47.5285 | 2025-11-29 00:50:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 133.1 |
| d578c1a5-42b8-3944-80b8-765bf1e9a363 | -8.1633 | -43.2055 | 2025-11-29 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 4891d00c-508c-3a56-8002-497e2656e590 | -1.4737 | -45.7907 | 2025-11-29 00:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| bc9eae21-ee26-34ba-a518-2aadf8d0eb15 | -20.1807 | -52.3975 | 2025-11-29 00:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 042b714c-26f8-3c82-b3e0-6b5c68e1a168 | -17.6155 | -46.6607 | 2025-11-29 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ec2ad52e-ae64-35a3-b416-ec9c78492245 | -8.1633 | -43.2055 | 2025-11-29 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 042a0cd7-268a-3dce-8972-0575bc91420a | -3.0626 | -43.3324 | 2025-11-29 01:00:00 | GOES-19 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 717df347-861a-334c-a172-09a7792748ad | -1.4923 | -45.7903 | 2025-11-29 01:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| de66dab9-e4f1-3981-98c2-e5f13cb73fcc | -2.3459 | -45.7036 | 2025-11-29 01:00:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| d9401137-5703-3961-8b3c-4e2818bd095f | -2.7845 | -47.4343 | 2025-11-29 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 3783bc38-ff63-378b-a96b-ec9ce56e91ea | -3.3573 | -44.0361 | 2025-11-29 01:00:00 | GOES-19 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5f127f16-9d44-38b5-83b9-60f478fa51ec | -20.4496 | -47.523 | 2025-11-29 01:00:00 | GOES-19 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 2be01d8f-c65e-39aa-ba2d-8155e2f1b7f0 | -3.5994 | -40.8622 | 2025-11-29 01:00:00 | GOES-19 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 813f43a2-be0c-35b5-8c23-87500c303ce7 | -3.0625 | -43.3556 | 2025-11-29 01:00:00 | GOES-19 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| ce9d8b0e-39a2-3224-82e6-88fb29f43b7b | -20.2256 | -47.5285 | 2025-11-29 01:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 4ddb6ebe-9659-3f09-a4b9-a576588b4d50 | -8.0513 | -43.1001 | 2025-11-29 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| b58d5aa1-c5ba-37d9-bb48-693b6f671d83 | -8.0324 | -43.1022 | 2025-11-29 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 0bcf0acf-ed4c-3a26-a475-61be5928a18a | -3.2135 | -46.8063 | 2025-11-29 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 086e0718-7701-3492-8fbd-ef5e0da717e9 | -4.3914 | -45.5528 | 2025-11-29 01:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 101.8 |
| d71c7791-c1e7-30bf-87de-fdffe4ac201a | -3.5807 | -40.8632 | 2025-11-29 01:00:00 | GOES-19 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 13bc359b-3af2-3617-a274-962368562eb1 | -2.7845 | -47.4125 | 2025-11-29 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 7f115c08-099a-3bcb-a3e7-4f8ab46f7b11 | -3.1948 | -46.829 | 2025-11-29 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| ee398c69-c8b5-38cb-8dfb-28739844650c | -4.3727 | -45.5538 | 2025-11-29 01:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| ef717ac6-e3ff-32fd-b871-b1483446fde4 | -8.051 | -43.1237 | 2025-11-29 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 332.1 |
| 99c24301-0fd2-3f03-b9f1-68269879c2e0 | -1.4737 | -45.7907 | 2025-11-29 01:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1addaba4-7a99-3643-a5da-522045f15d3f | -19.1273 | -52.7152 | 2025-11-29 01:00:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 8113d1e4-2d04-3f1f-9386-0aa4a0ac4b22 | -3.2134 | -46.8283 | 2025-11-29 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |


[Clique aqui para ver as próximas entradas](README8.md)
