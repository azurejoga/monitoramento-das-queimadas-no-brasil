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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de2f5be9-0d5d-39bb-9fea-d453e35b45f7 | -3.71681 | -44.00441 | 2025-11-24 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44e5b8bb-b882-3de6-a6cd-b9dd60348beb | -2.13156 | -45.32479 | 2025-11-24 04:06:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57bf9981-f17d-323a-9130-2c6cd52a90dd | -4.10651 | -49.06907 | 2025-11-24 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e1fb8d1-6c2a-388a-acec-addfe6be916b | -3.45048 | -40.53535 | 2025-11-24 04:06:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 05762933-8a73-3f48-a437-8f59e801277d | -3.81327 | -43.35927 | 2025-11-24 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16fa2adc-3839-3b22-a98a-2994b6640341 | -5.2712 | -44.3724 | 2025-11-24 04:06:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d370a6e2-4ae1-3dfb-bee6-ba2e8f593d41 | -3.21992 | -45.93539 | 2025-11-24 04:06:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 708e49cc-a35a-39ab-8417-fd84c72f3378 | -3.34786 | -43.50139 | 2025-11-24 04:06:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ee8dede-5eb2-3783-8e41-4ecc0c786a6b | -4.61988 | -45.63613 | 2025-11-24 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f5fd920-2888-361c-9454-3c0c776d90b1 | -1.95283 | -45.58529 | 2025-11-24 04:06:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af88be9a-b81f-3ab4-9877-e5f500a98765 | -4.81758 | -43.83765 | 2025-11-24 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72679352-2202-3f27-b4be-ee75ab679a31 | -2.13627 | -46.41544 | 2025-11-24 04:06:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 577d5a2c-42ca-39e8-a760-f88476e23d48 | -3.2907 | -43.40361 | 2025-11-24 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d69e8322-4943-33e1-b78f-95f799ca0ee1 | -4.1979 | -41.64859 | 2025-11-24 04:06:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc0dab5e-b405-34dd-9ff8-043184f351a6 | -4.16588 | -43.98708 | 2025-11-24 04:06:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74730681-d130-3da1-bf1a-33d9405c014b | -3.59564 | -40.97708 | 2025-11-24 04:06:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 10c5e4c3-56e8-3d43-b467-963fe8fd6fbb | -2.465 | -48.1162 | 2025-11-24 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35434d85-6a32-36e0-af81-026b90f0dc42 | -2.14119 | -46.41213 | 2025-11-24 04:06:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d57f1d5-6a7a-3042-a48d-c4c54a7158a9 | -3.82707 | -48.99011 | 2025-11-24 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 55aa2652-e970-3e32-be7c-eb21fb4147e8 | -3.96595 | -46.48014 | 2025-11-24 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9b85fbd-6f85-316e-b41f-971fbaa4ce4b | -4.82593 | -43.83082 | 2025-11-24 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 40d06bdf-9f80-3302-b789-ce4852366799 | -3.96632 | -43.96611 | 2025-11-24 04:06:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46cb2a8f-63b4-3234-8ca9-f1ffbffd4046 | -3.27298 | -46.04481 | 2025-11-24 04:06:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 527a19b8-90a5-3b06-b2b8-22e967451df5 | -3.4947 | -46.01712 | 2025-11-24 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ac1bacd-bce3-397d-a15e-45b0ff94aceb | -4.75292 | -42.77902 | 2025-11-24 04:06:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24727d59-7279-30c3-b6c4-b715ad66d18e | -3.21643 | -45.93109 | 2025-11-24 04:06:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c1ff34d-8a03-378e-ad9b-aca3a020ba0c | -4.70891 | -46.45647 | 2025-11-24 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6995ef3c-c459-335b-90cc-c1ad02512dfe | -4.93576 | -41.1536 | 2025-11-24 04:06:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 39578f16-0097-3bc9-ac99-94dbf6bac40c | -2.10651 | -47.09902 | 2025-11-24 04:06:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84b136a7-6b79-37a3-ae25-916213015bcf | -4.52622 | -45.61818 | 2025-11-24 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7dbb97ac-ecbd-3369-844a-b5fae320c149 | -4.52234 | -45.6174 | 2025-11-24 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 16669970-ae3e-39ed-bf31-f17c2616f769 | -2.46562 | -48.11329 | 2025-11-24 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a3d3774-535b-35ef-8126-5f068f73a0f4 | -4.53792 | -45.49901 | 2025-11-24 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6daa9ee6-9ae2-396a-842d-872f804e7460 | -2.88145 | -45.26199 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab558cd6-973d-3f7f-9d3c-2075c7729c83 | -2.45242 | -45.38118 | 2025-11-24 04:06:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7b574fd-691e-3b03-a8fa-0a7fe9cec8b4 | -3.49529 | -46.01351 | 2025-11-24 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec3e4edf-58f8-37e4-8ffe-611db1a4cba3 | -4.81887 | -43.82972 | 2025-11-24 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a2f4708d-2c2f-3501-8fae-7db3dfc9bca2 | -4.38827 | -40.62995 | 2025-11-24 04:06:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5d96b015-c1d1-3ce2-894c-ec0849e290d3 | -2.97846 | -44.41813 | 2025-11-24 04:06:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86dae1bd-d88e-3819-9c0a-a7953ecd1861 | -4.66322 | -46.05402 | 2025-11-24 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 66a14fe0-830b-396e-ad9e-fc7ffbf3ccb4 | -4.82176 | -43.83423 | 2025-11-24 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 65d82830-2143-3551-ad48-1719407b1baf | -3.71615 | -44.00853 | 2025-11-24 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e618b98-f90e-3878-9d38-e975fbf8bdf2 | -4.52704 | -45.61323 | 2025-11-24 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 59be0ea9-9252-32d9-846b-67cfd394bdfa | -3.2205 | -45.93178 | 2025-11-24 04:06:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9530fcbd-0f80-397b-b66f-0f66b1a37da2 | -4.34338 | -44.32914 | 2025-11-24 04:06:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e1f2b66-f7fa-39bd-a1a7-d347a8ff1ba8 | -5.70569 | -37.94629 | 2025-11-24 04:06:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8116a6bc-ac27-32d2-b316-deef8c16440c | -4.82056 | -45.15215 | 2025-11-24 04:06:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94abea18-5f9a-3d39-a9be-a57b93e67eb4 | -3.22773 | -45.73289 | 2025-11-24 04:06:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f44732a3-3b3c-32da-8822-665d39a35822 | -3.83928 | -42.75651 | 2025-11-24 04:06:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e0d392e-75ce-3ced-b704-353248600f36 | -3.20652 | -45.76183 | 2025-11-24 04:06:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cd217619-75e5-3052-9e58-6cdd640cb539 | -4.66004 | -42.60443 | 2025-11-24 04:06:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ffd65970-6f16-3be0-891c-fc88013be4a5 | -2.88458 | -45.26757 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9564e924-f6e0-39f5-9d98-582b34e09e9a | -4.39448 | -40.67681 | 2025-11-24 04:06:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 50191cda-6e7b-3a81-935a-e022ca015563 | -4.71303 | -46.45709 | 2025-11-24 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 20607076-8bed-33a4-837c-a0be9e4ca49f | -3.22108 | -45.92816 | 2025-11-24 04:06:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 281c64a2-874c-3844-9433-a2fa78d08be3 | -1.22036 | -46.40343 | 2025-11-24 04:06:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fceda04-090d-351a-9c11-37c24eb50bf7 | -4.8301 | -43.82741 | 2025-11-24 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5c225d4-f1c3-325f-994d-8b9b2376514a | -3.03348 | -47.79107 | 2025-11-24 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c90c9851-01de-3736-a503-a4bf9b886998 | -2.27498 | -46.44553 | 2025-11-24 04:06:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fe826e4-b665-3e3a-af74-2edaa903c525 | -3.96208 | -43.96962 | 2025-11-24 04:06:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1848345-762a-354d-8fbe-4b9f5b2ce9bb | -2.79846 | -45.35424 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e543c76-53e8-30e5-be3e-84a2cf6c4f08 | -3.71972 | -43.21888 | 2025-11-24 04:06:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f62cde5d-33bd-319a-8357-07599456bd3f | -4.71652 | -46.46155 | 2025-11-24 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 40331ac6-3565-3c49-b099-56a8e3d785af | -4.26641 | -40.86475 | 2025-11-24 04:06:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d8e971cb-3143-3da3-baac-d1bd3c757f42 | -3.33119 | -43.3297 | 2025-11-24 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12169706-8eb0-3dd1-8fe4-fb35d6fcfb61 | -3.98894 | -43.39801 | 2025-11-24 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a88f6d06-6fc3-37de-905b-af8c2b7f4a47 | -3.27709 | -46.04534 | 2025-11-24 04:06:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dacd05ee-8d39-3af3-8f37-84bb158ec621 | -3.21585 | -45.93471 | 2025-11-24 04:06:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9503c933-d1b6-3de0-b3dd-aa2f653c3bcc | -3.5951 | -40.98052 | 2025-11-24 04:06:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 62939c3a-77fd-3eb5-8b5a-e87c49a25456 | -3.80978 | -43.3587 | 2025-11-24 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3bcac43-a869-383f-b690-4a8dee8e3067 | -1.48143 | -45.87285 | 2025-11-24 04:06:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb0986e9-e7a5-39a6-888f-c5a96fabbadc | -6.07672 | -39.54223 | 2025-11-24 04:06:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 3e1efc1c-0c52-3c4f-a4fe-7e07541e46e0 | -5.35814 | -36.93851 | 2025-11-24 04:06:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a69de6a1-ac1d-3425-9354-f9a83a6a02db | -4.39821 | -45.73448 | 2025-11-24 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14a81a93-d3ab-3b0b-8dde-f58959ee4783 | -3.8264 | -48.98825 | 2025-11-24 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f763357a-b8bb-3c66-a899-b684d415ab8c | -3.59233 | -40.97658 | 2025-11-24 04:06:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2aaee625-e511-3a69-bc07-a1c698650a5f | -4.49059 | -46.0077 | 2025-11-24 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dcf5db5-010d-366a-872d-ded06f8b0738 | -5.89747 | -38.19223 | 2025-11-24 04:06:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bc7905a1-93b5-386a-ac4c-ac77aecf4a58 | -2.39436 | -45.01112 | 2025-11-24 04:06:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1051cd5d-206b-3432-ab82-72c844da10f7 | -2.8814 | -45.2874 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 715d74dd-194a-39d9-8928-c71ddfa5f243 | -2.79758 | -45.35629 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffb1398b-dc41-36ad-83de-0f8828fb5a85 | -3.79891 | -49.18409 | 2025-11-24 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4237867f-e7f4-310f-ad28-5dcdeb30d8c4 | -3.91786 | -43.18623 | 2025-11-24 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36c3182f-6b1d-3ea8-b037-bd99d5e04a3b | -2.98362 | -44.40985 | 2025-11-24 04:06:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fae1e8b-78df-3472-84b3-f3552aa5ce54 | -3.56449 | -41.60899 | 2025-11-24 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f43df11e-9d0d-358f-913d-4362d8b7509b | -4.30529 | -47.5396 | 2025-11-24 04:06:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7687d81-303d-364e-9cef-205506b5163d | -2.88537 | -45.26262 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d81ba39-37ac-3c08-8cf5-b64d1cc0a1b1 | -2.87748 | -45.28679 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d7d09ae-3bf5-3a59-a8d6-fd6ec3c1b3d3 | -4.41318 | -45.74199 | 2025-11-24 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7a12d90f-ae74-3412-854f-373d6750b186 | -2.87167 | -51.79688 | 2025-11-24 04:06:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6db3f337-98b8-3634-a0bb-b6a12a105834 | -5.0448 | -44.09464 | 2025-11-24 04:06:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 464d2f4b-b656-3bbf-a5e5-68105eede542 | -2.8007 | -45.36192 | 2025-11-24 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 717f5927-1511-30c1-bc59-3b111c78ab19 | -3.91725 | -43.19002 | 2025-11-24 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e840c8c-e58e-381a-ae28-0e4c62778b71 | -3.55785 | -41.60796 | 2025-11-24 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00409bae-f56a-3d6e-baaf-4ee29b5c9877 | -2.877 | -51.8023 | 2025-11-24 04:06:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b665b425-9023-32fc-9adb-d44b0f4837b2 | -3.96566 | -43.97021 | 2025-11-24 04:06:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4b60c7d-efa7-3c9f-ae0c-cc99d18e092b | -6.31694 | -43.81648 | 2025-11-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b70e594a-18ef-301c-8a5d-6e64b0753581 | -12.00499 | -49.27478 | 2025-11-24 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8946aa53-db36-394f-86e4-2982e6266ede | -6.28563 | -41.44131 | 2025-11-24 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 94d46ebb-3c30-35e4-9e88-66a83c72a8e8 | -8.86556 | -40.45434 | 2025-11-24 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README6.md)
