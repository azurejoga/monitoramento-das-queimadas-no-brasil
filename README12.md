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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdf9dbc8-fc19-3194-b69d-b112e6a2aee4 | -3.1877 | -48.4172 | 2024-11-26 03:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| b4976685-9eb2-3781-af36-a52d4dbcc562 | -3.9859 | -48.0843 | 2024-11-26 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 3ca85ab6-707b-3afd-acc6-6d7277083a01 | -3.986 | -48.0626 | 2024-11-26 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 168.7 |
| 32e89a99-7d07-358b-a115-854789d74405 | -3.9861 | -48.041 | 2024-11-26 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| dad26ff3-d97a-3c1d-9530-321889ff1793 | -17.6453 | -57.5874 | 2024-11-26 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| 92cc3ea5-89d2-3e78-964a-aaf819775fa6 | -6.0676 | -48.0352 | 2024-11-26 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e1cbcf9a-f004-36b7-adb1-979398f8576b | -3.1876 | -48.4387 | 2024-11-26 04:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 148.4 |
| ec75b055-8169-3e10-8be2-2a3ff28a05a6 | -17.6453 | -57.5874 | 2024-11-26 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| bd776811-7e50-3385-bf6e-6f06a4634f5e | -4.3232 | -47.5039 | 2024-11-26 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 8433bce7-fed4-3782-9e36-f3e3bb0043a2 | -3.1691 | -48.4394 | 2024-11-26 04:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 96bb348f-e898-3182-8773-7d6c35b947d2 | -3.6042 | -50.3781 | 2024-11-26 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7806e5b4-5b56-3903-8215-aa849ed94cae | -3.1877 | -48.4172 | 2024-11-26 04:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 2bc0976f-6a8a-3c8a-bc54-1852eed5d7c2 | -3.1875 | -48.4603 | 2024-11-26 04:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| a3e6b46a-8d51-3270-a8a2-945783f299b0 | -6.0862 | -48.0339 | 2024-11-26 04:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 308c9059-45fc-3934-b82c-e6e067a33114 | -4.3231 | -47.5258 | 2024-11-26 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 6ab1e838-5b0e-3ef9-b60e-47ba50bab05a | -4.0 | -48.09 | 2024-11-26 04:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32d43450-aaac-332e-a2db-3414a610b92a | -4.0 | -48.04 | 2024-11-26 04:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dd0ec6a-8dde-396a-9b4b-3882de14a49b | -3.97 | -48.09 | 2024-11-26 04:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5c7561e-d447-3e35-a58d-a2a6124f8467 | -3.97 | -48.04 | 2024-11-26 04:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45e15092-48fa-3b17-81e3-5a1ea86f175d | -4.3232 | -47.5039 | 2024-11-26 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 49ce303d-c94a-3ba2-827d-12a10740fb3c | -6.0862 | -48.0339 | 2024-11-26 04:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 8c2c359e-3be4-3202-8479-c038af96ba04 | -3.1877 | -48.4172 | 2024-11-26 04:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f25ed0d6-79ad-3323-8259-39c31bcbe4d5 | -17.6453 | -57.5874 | 2024-11-26 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 6173c286-8353-3904-afec-e46d66c6d714 | -3.1691 | -48.4394 | 2024-11-26 04:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 748df9c4-7270-3815-8438-9e5af067ef3c | -3.1876 | -48.4387 | 2024-11-26 04:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 561895b5-0441-3ec9-ab17-e64b70f8d88d | -4.5376 | -43.2807 | 2024-11-26 04:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| d0482d53-d485-3003-b4ec-fb57178e9b4e | -4.5375 | -43.304 | 2024-11-26 04:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 7ca8a1a0-87c1-3ac2-ade2-b0f698907e6f | -2.72069 | -46.27033 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36312d9e-71de-3db1-a6d6-cf5352cf09b6 | -2.82035 | -51.79681 | 2024-11-26 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6140a59-69c6-33be-b152-edf0e9fd0940 | -3.99058 | -48.32428 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 627cbb08-2488-3001-89c9-6dcedd493130 | -4.11564 | -47.97398 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a83a1a50-89aa-3cfd-9ab0-65fe5ca85dba | -2.88984 | -48.73649 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97de398d-8f46-38b5-bdc3-c356958a2599 | -3.46783 | -50.25716 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48f0423f-d700-31bc-9759-8faedabdc7af | -3.19141 | -48.4291 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7b78e33-7e6c-3b70-ac94-a153a05340a7 | -2.9336 | -48.82977 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b35db77-c005-3065-86cf-8e21656811ff | -4.54179 | -43.29121 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 47efb0f2-ab60-31e8-83bb-592e42b22a93 | -1.92207 | -50.57207 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 042df53b-f9c3-3867-a7d7-c43b36415fdc | -3.38448 | -50.10328 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9bd3710-1dd3-3497-b051-b90822d1695c | -3.08751 | -45.31782 | 2024-11-26 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8550ec76-1903-387f-9bb9-681e06c2417a | -3.18127 | -48.57496 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f492dfd-d3f6-3e3c-b013-684b26b94852 | -3.95901 | -48.06345 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6b8012d4-97d8-38df-9691-d00148357f7f | -4.54455 | -43.29518 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 36423b7f-80a1-30f5-b0af-4f55063f604f | -3.97421 | -46.73234 | 2024-11-26 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fe6b2e9-f693-3987-892d-33c988ce4321 | -4.37737 | -48.49891 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b62dff43-4b1c-3bd3-98dc-ef787fa72bcd | -3.95133 | -48.08461 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94fe5a22-a798-311e-8256-4fb2db7f35b7 | -3.97007 | -48.09855 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c166000-c73c-3053-af9c-8740ad355785 | -3.38005 | -50.10616 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 104baab5-1900-3cab-aba4-f196ba1b093e | -2.89062 | -45.25575 | 2024-11-26 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2618a65-0d77-3e34-94cf-16d904c737f8 | -3.96191 | -48.07136 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3ae51e8f-ad45-3d12-bb91-c97cea98cfa8 | -4.95275 | -45.78902 | 2024-11-26 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db3e60f3-82d7-3782-9b0d-ced0eebd3e14 | -3.5937 | -50.38831 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1988b360-0123-3c86-a12f-f6d7e7ba0328 | -3.96025 | -48.05589 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9e8b2df-6223-304d-9b10-864cf65530bf | -3.38965 | -44.17043 | 2024-11-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 79717faa-49d9-362d-a81b-0251eb4047f2 | -1.92254 | -50.56919 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a133fa1-38d8-38b3-9627-d4a4886ac556 | -1.78713 | -52.73625 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c176ec29-9706-3894-8b21-edded4cebb0b | -3.28038 | -50.01687 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b5a46af1-f815-349b-84a4-7a959db312b4 | -3.49888 | -50.45846 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 503d985e-e560-395c-af2b-e3711928a623 | -3.1859 | -48.43631 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| c5f80195-58cc-370e-b3a2-99c19c65179b | -4.25434 | -48.67068 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 220c1602-690f-3984-b0e5-dcf8a2903f55 | -3.39746 | -50.02205 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d5cc66b-7c17-3b38-868e-ce13d32dcf28 | -3.4812 | -50.44481 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25d902ea-8863-3b9b-9370-44aaf154aeae | -3.47374 | -47.68455 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bf854c3f-c9cd-3553-8efa-6801a420497d | -3.9795 | -48.06644 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5331a411-5c29-392f-a5d8-011dae1581c5 | -2.77148 | -48.57909 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f8def51-d2e2-3c8c-ab82-fb6f216b4e9d | -4.50709 | -42.0727 | 2024-11-26 04:14:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26413ba7-7f0f-312d-b7e6-88e3c445b182 | -4.6543 | -47.94876 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e351cf65-b697-3c39-a094-a863581c5e32 | -3.07672 | -49.20273 | 2024-11-26 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bbc90e42-ff44-3c5e-8d77-2e22cae540a9 | -3.81866 | -47.46931 | 2024-11-26 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3503a5cc-8603-36fd-9809-6058ce93a103 | -2.49464 | -45.03175 | 2024-11-26 04:14:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d3cf2a2-7d0c-3ad7-8604-4a23ae4a1b75 | -1.92472 | -50.58733 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30efef53-1404-3907-89f2-6ac0f544e322 | -3.1763 | -45.25886 | 2024-11-26 04:14:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab700040-6e72-3072-ae17-ebba60f483a4 | -3.95602 | -48.08165 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afe35d8d-826e-3592-a614-2119f8341e9d | -3.95835 | -48.09307 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed685e57-613c-3af8-87c5-90764cbe5d9f | -3.45602 | -49.99922 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 262fcb00-295c-3ab7-829d-245245e5db3e | -4.45273 | -45.80897 | 2024-11-26 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d01bfd7-d3b9-3514-bad1-5035ecf5693e | -2.17526 | -45.6025 | 2024-11-26 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0761dae-6e9d-34a5-9184-563d34094d4b | -3.97359 | -48.1028 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87beadbc-f973-3caa-8691-cdb6871d62f6 | -3.96065 | -48.10468 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b354e74a-cf8c-3448-ac8f-08c45561b5fe | -1.82568 | -45.58571 | 2024-11-26 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f708ab9a-451d-3f0f-896a-657b16b4e87f | -4.09441 | -48.48125 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c02612df-29e8-3812-80ec-6f1d8601da32 | -2.38822 | -48.51354 | 2024-11-26 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aacab349-c388-305c-9c5d-7dbcb946bce3 | -2.5437 | -46.4024 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54a92714-6f84-38fe-9034-fdcbbf78ce03 | -4.31842 | -48.64888 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84281569-e1e8-3e4f-9a6d-03edd0069f50 | -4.23225 | -48.69963 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6fe37eb-bba8-3428-82cc-2062a836ba9c | -4.24587 | -48.66923 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dea90029-bc70-31ac-9151-1410e972e39b | -3.98706 | -48.0716 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b87e82a-520d-32c9-9739-c3bf4853f3b4 | -2.55645 | -44.15201 | 2024-11-26 04:14:00 | NOAA-21 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 192f12e0-13d0-3097-946b-ae893a207cdf | -3.29892 | -47.02324 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc1363db-b711-3dc7-b52d-bb39215b7b34 | -1.90501 | -47.04026 | 2024-11-26 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aca3b2e2-8209-3615-bb29-4d95aebd44ac | -1.70436 | -47.72711 | 2024-11-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5110b21f-9477-368a-842d-9c93888b8e0d | -1.48422 | -53.81533 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48a169e5-531b-3e77-a320-d8451fc67b8b | -3.97061 | -42.19897 | 2024-11-26 04:14:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2fd8071c-02fa-3803-8f2b-910d6a5394e1 | -1.56299 | -45.67892 | 2024-11-26 04:14:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b28947ec-e56d-3f27-aa38-917a61ba7d48 | -4.1672 | -44.07226 | 2024-11-26 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb038006-527e-37ce-82a4-c4178d4c2c55 | -3.97365 | -48.07658 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b7ec4f11-1b9a-3785-8435-e550513bf6f0 | -3.39451 | -50.02011 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7aa09463-20d1-3dcb-a2d2-3c94346bbf7e | -3.39189 | -44.17817 | 2024-11-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dabf40b7-f235-359b-bc00-fb3382105168 | -3.38914 | -44.74864 | 2024-11-26 04:14:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0477af1d-277e-3722-b0ec-d479c2c56f37 | -3.97716 | -48.08085 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ad132ce0-8f2d-3237-a67e-59da6465b3ba | -3.32948 | -50.05259 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README13.md)
