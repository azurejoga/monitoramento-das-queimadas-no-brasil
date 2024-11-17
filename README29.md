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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00a67268-db39-38ec-ad8b-05434a11da21 | -6.37556 | -41.54937 | 2024-11-17 04:06:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d4f093a4-5255-3497-bb2b-84652ee36d76 | -1.84279 | -46.53064 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d4f7124-073e-34db-b645-9c0bf3a6c2db | -6.51712 | -41.44741 | 2024-11-17 04:06:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0a8f0eda-446c-3e1e-81e7-f62baab003d9 | -2.60404 | -47.56167 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 702a5ad6-052b-3ce4-98a8-290f2487b43b | -3.58129 | -50.53205 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb34b791-f629-3231-9a48-ca0f4d365f9a | -3.07184 | -45.37841 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b630aeb-7411-3f08-a144-6f3cdaed1b2b | -5.31481 | -45.44695 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 73aa8881-8155-3670-b482-c808c49d6682 | -1.84717 | -46.53134 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29ecc9e0-ad72-30fd-ac92-1fc1af0d5e0d | -2.66477 | -46.21045 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab8009fc-d37d-3911-bd00-8ae3c5a9eb03 | -3.53096 | -50.25395 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4dd40b72-ca5c-31f7-9d02-84dae1c8b836 | -3.5224 | -50.27098 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d0128e3-50ef-385c-b4fa-48eff404cb0b | -2.53357 | -47.13719 | 2024-11-17 04:06:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99d011f4-94aa-38e8-b361-43aa95af9ed9 | -2.1579 | -50.70671 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 71134d75-d75d-3e3d-a665-5b19b037fb4b | -5.46767 | -42.15695 | 2024-11-17 04:06:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0ecd57bf-fb63-39cb-bb56-3c40cb3d3ed9 | -6.52044 | -41.44794 | 2024-11-17 04:06:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dab9d155-ab68-3fb8-a26d-32d7839cab5a | -2.66435 | -46.21524 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cc07cd5-7a5c-3d55-b5a6-2cd42e13643e | -3.04011 | -47.97779 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 578436c7-beb5-35aa-9394-cae81ebd5a67 | -4.51803 | -46.59988 | 2024-11-17 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adcb8766-9115-3e47-bb93-32bc84c0f783 | -2.15183 | -50.70667 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6fa852b-b777-35a1-a67e-5b62b4bab333 | -4.00838 | -47.42936 | 2024-11-17 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30dc29a2-bd5a-3b8e-b87d-a679cf8209ef | -7.22066 | -38.00314 | 2024-11-17 04:06:00 | NPP-375D | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e543a93b-e4dd-3131-adb7-eda718f93562 | -3.51933 | -50.2559 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4788066-3dfb-39a7-ab41-0f04968ab9e7 | -3.62793 | -43.15754 | 2024-11-17 04:06:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec6168dd-7cde-33f9-90db-4ea8d38e953e | -2.58309 | -47.57309 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| fe0505d1-6f3e-3184-8d44-6fbc29b0ff44 | -4.47665 | -48.10506 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 384ae7f0-8886-33bf-91ff-3190d931410b | -2.22409 | -53.6125 | 2024-11-17 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f5ce7c6-4036-3cc6-a6a6-7d1b600255a8 | -3.53037 | -50.25743 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 88de536f-a482-3cb7-85b2-3b80807e1b49 | -2.60542 | -46.25753 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f5e7fad-b090-359c-bc33-3f740f3b9be7 | -3.09284 | -45.96627 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 353f24f1-347e-35fb-b20b-5d8bd05ca8ef | -2.45585 | -45.58937 | 2024-11-17 04:06:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 564b923f-a14c-3c8e-a50c-b8ccb5db54da | -3.8099 | -46.51968 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64664732-a3b0-356e-8f3d-7507f8ddb598 | -2.66374 | -46.21909 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58f59109-ad06-3de3-ae30-3444cf1edfbe | -2.66835 | -46.215 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d82fa73-2b57-3cb0-b29b-77d5242df0d8 | -7.04786 | -40.41388 | 2024-11-17 04:06:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc1794de-2659-3613-999b-6850e8c32ba5 | -2.67227 | -46.19261 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f69e582-2155-36c7-9634-6ce74d90f129 | -2.17858 | -49.10823 | 2024-11-17 04:06:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 238f3954-0afc-3913-9fcf-790aabe415c3 | -2.63988 | -46.15157 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4c6ab44-ea11-3e48-b4b1-1b8977bcdea1 | -2.67772 | -46.1855 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3d35849-d3d7-3604-a08d-eb2e2de498ad | -3.81187 | -46.50793 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a80cd9f2-a4f4-30d5-81d8-95816deaad40 | -3.62151 | -50.21837 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aade280-c392-344a-a0aa-0c71022aaae7 | -2.86231 | -46.72419 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 3d1c3e09-f958-3442-9f30-6e7fb4dcd51a | -3.8905 | -43.13828 | 2024-11-17 04:06:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4075fef1-bcec-3a3d-be54-28488b06d91e | -5.314 | -45.4518 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d9eb3801-b080-325c-bfd5-28650d72694d | -3.5316 | -50.25021 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 43664d3e-0cfd-35b2-b170-a21a5329b126 | -3.8922 | -46.62189 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98e7fb20-8dc5-3827-889b-7ad763814d40 | -5.33946 | -44.99413 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b5dc6b2-80d4-3d5b-911a-3d0022bbe741 | -3.58534 | -50.52738 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e0ed116-7510-38a2-8e71-f53e8fa01d43 | -3.35414 | -46.06497 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e84e13c7-0995-30f2-9ce0-86807f02e5ef | -1.20686 | -51.77267 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94f7e161-a95a-39aa-afeb-fbc19d88acdc | -5.46488 | -42.15289 | 2024-11-17 04:06:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ee6ddc1-5a21-39ae-96d5-3adb0a83bae8 | -2.99422 | -52.60181 | 2024-11-17 04:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3f4858f-f854-3bb3-81b7-3ff292c6459c | -3.78654 | -43.90694 | 2024-11-17 04:06:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47f4f20f-e06a-3e11-8c4d-cc6a427346e3 | -4.58269 | -48.03031 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 84efb2a8-ab52-320e-940a-ecd2c6d2c375 | -6.87441 | -41.92744 | 2024-11-17 04:06:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a7640c80-9ebe-3892-bf5a-b6e82b8cb022 | -3.0926 | -45.17542 | 2024-11-17 04:06:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24bef77c-93a9-3f95-9252-aedffc3a68de | -3.575 | -45.68251 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e20930b-229f-34c9-acc3-8944b91bd390 | -2.72619 | -44.96655 | 2024-11-17 04:06:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63b8e892-b8c9-3549-bc5a-47a48aa8242a | -4.77001 | -48.02853 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64b86ac6-14f1-3936-8747-753bab74bbbd | -2.47787 | -45.40485 | 2024-11-17 04:06:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a1a31cf-fc9a-35ac-a0d7-8282dcb2287a | -6.93293 | -42.81186 | 2024-11-17 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3cf48a89-c1bb-3f88-85db-c564c99da7e0 | -7.65873 | -38.83622 | 2024-11-17 04:06:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 96f57d4e-82d4-3f25-a149-688842b5f5ba | -2.67872 | -46.20476 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3f7e06f-6374-3b3f-adbf-c78da06f20c5 | -3.51937 | -50.25565 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6220b9df-733b-3e03-9d74-45ee544713a0 | -7.48094 | -47.17955 | 2024-11-17 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| daaaecb8-d538-33a1-86f3-908bba09e25b | -4.55787 | -43.20593 | 2024-11-17 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca89380a-3e03-3986-8d0d-cc6dfd0a7c72 | -2.70916 | -47.72575 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a047b907-8007-33c9-a175-ffb406c13402 | -3.3494 | -46.06794 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38f248fc-ab63-3b16-8761-3df0ff3fc4ca | -3.52426 | -50.26011 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 58bc1246-922c-38f4-8f6e-a1a43eae3a32 | -7.65813 | -38.84024 | 2024-11-17 04:06:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3bce4caa-b32f-389a-af00-4ff3ae7962de | -3.92074 | -46.52991 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b5012ac5-782b-3802-b855-7aaaa58f556a | -2.28083 | -48.81639 | 2024-11-17 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8f26bc6-f470-359d-93d4-37dd73b7f799 | -3.91783 | -46.52131 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e6bfaabd-530e-3745-bd04-7d5003573478 | -2.67051 | -46.17636 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28dced66-9fb7-3348-b238-7d9692ab2c96 | -2.67286 | -46.1878 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50bcaef9-d71f-3d7c-9960-845daae61649 | -0.95245 | -51.7346 | 2024-11-17 04:06:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e447c3a-109c-3db2-bac0-2228af925524 | -2.60018 | -47.55618 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d5a0b945-1bd3-3d57-b089-111116a53ea4 | -2.66928 | -46.1841 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa8a2d4f-e3ba-3367-ac43-431196abffe9 | -1.2894 | -51.74082 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7a7f85d2-1ebe-3b9a-a898-760462766705 | -1.20603 | -51.77757 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 618f1501-4d93-3f3d-b94a-d37bcda46904 | -4.10789 | -46.10535 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 377fc5ab-3b39-3a45-8308-85c5bfffbd6a | -3.2153 | -42.08828 | 2024-11-17 04:06:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbcfb318-2d92-3a97-a06b-3f1432e090da | -3.53283 | -50.24297 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59bfb73c-2499-342f-96c8-9c434f95c03c | -1.13556 | -51.69499 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 27ce02a6-b33c-388f-886f-55d44719daf5 | -2.67028 | -46.2034 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04c69b19-cefa-3750-80e3-fb7878f6e7c1 | -6.94809 | -46.4 | 2024-11-17 04:06:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95c562cf-7759-3e7f-bfa5-a4c8a494ad60 | -3.09578 | -45.97426 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b829da1-b246-3016-a194-bd697cff3edc | -7.58086 | -39.04554 | 2024-11-17 04:06:00 | NPP-375D | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1401397b-ca05-3efa-93e1-1244314ea32c | -4.7292 | -46.84293 | 2024-11-17 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90a163c0-4cf9-3d09-be8f-f196b5e03ae0 | -2.67808 | -46.20866 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c1894e4-e62d-3126-a211-1716fec1d95e | -2.57542 | -49.07723 | 2024-11-17 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e74a0dd-b937-3bdb-8185-e762a6693e7e | -4.67252 | -46.73545 | 2024-11-17 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f02d29e8-9ee2-3b91-bb2e-c0c7c7ba0379 | -2.55406 | -45.77913 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7fb1bed-8865-3d61-9756-b927b15e36d0 | -2.33011 | -53.57213 | 2024-11-17 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 439b4370-064d-30c8-8997-ffca9b4f1666 | -4.66578 | -49.51506 | 2024-11-17 04:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4de45390-2adb-362e-864b-d8a43225a4d7 | -1.29645 | -51.73696 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 322776cf-4c9a-35ce-88d4-d827268c945a | -7.5214 | -40.58529 | 2024-11-17 04:06:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 78b8583a-7dbc-382b-98d2-b210f4adcc9c | -4.48133 | -48.1058 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7966cb17-977c-300d-aa62-2ead35e21d8d | -6.93909 | -42.81659 | 2024-11-17 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 80dec3b4-210a-33d8-af56-cd242524fedd | -3.04342 | -45.76054 | 2024-11-17 04:06:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c156d9b1-39fc-30e2-89cf-42bbabe1a5f5 | -2.67871 | -46.86301 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README30.md)
