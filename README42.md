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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36fe66a1-d4e7-35ec-9d6d-6a44b784e3c4 | -3.03874 | -49.54178 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d6013015-17a4-360c-9020-3c156b28c3f2 | -3.62525 | -47.52005 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7213d11-c283-3016-b710-92954c38eced | -1.22513 | -51.96519 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6114dfab-088a-3347-bad5-f24ae8141e2d | -3.1124 | -45.96307 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bfa191c-99c3-35e9-a677-053c8ea57972 | -2.71331 | -51.34274 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7aa6d4b1-506c-31f3-91be-7b9f501c1346 | -5.69262 | -47.01191 | 2024-11-10 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ac7d692-ad65-347a-ad87-5576c72aeed0 | -1.78146 | -46.14912 | 2024-11-10 04:14:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cb933a28-6ebe-3f17-a9c8-5abd6bea6cf8 | -3.45901 | -47.66501 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c5e573c-482b-3d0b-aee0-b050e1b9ddf7 | -3.95207 | -48.15152 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 140dca78-8df3-3a0c-a985-52c2a455f17a | -3.24956 | -45.99621 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 059e4cfd-b023-369f-8b6c-9addf74af9cd | -1.50645 | -52.1497 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e883164-e410-3670-8180-2ce534025b3d | -1.14773 | -53.7909 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6877d745-bed0-3139-878e-958d7d13d0e0 | -2.14921 | -46.69207 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5e19007-396b-379e-8331-8d72c5fcc8c8 | -2.9089 | -50.40356 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 59dee03b-1094-3b5b-9ff3-2c379875e7bf | -3.02915 | -49.54757 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf6f0261-4e32-3e7f-b467-d8f2c0276a3f | -2.68242 | -49.27603 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51518a41-c806-3401-a430-b4d8cd752974 | -2.5095 | -47.46873 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fea864f7-18d4-3828-b328-07ed2e62b1fb | -2.61258 | -46.16468 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0b7e2a7-735f-3620-93a2-3f1bfa7401ed | -1.98349 | -46.44128 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 906155db-51f4-372a-89ff-320a4cb3a63a | -2.60388 | -48.19338 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88123b9e-e619-3cf1-9bd8-7f2fcbc1d220 | -3.11038 | -51.2902 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7024e493-bf98-31ae-b2db-47016eb007fa | -3.17609 | -49.10534 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13489631-b8a6-326f-b8a9-909eb785ab6b | -3.79599 | -47.46424 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ce3b4bc-8fac-3bec-ba73-c3e5b91b32d3 | -3.28074 | -42.34089 | 2024-11-10 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d5e56f7-d82f-359e-be36-80d6f3ea9677 | -1.83984 | -52.15127 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eac34380-b903-3c4c-9f60-171915de5b08 | -4.3099 | -48.61447 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0748eccd-51e0-320c-b6a8-687ab6069bfd | -2.18846 | -48.37352 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 840068b2-127c-3f02-9070-0ed391ff4b00 | -6.21204 | -41.65741 | 2024-11-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 509fb276-a849-3fc1-8a78-481e5d50507f | -4.49704 | -45.69965 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fd4fe98-cabe-3027-9648-f6e120761062 | -4.34747 | -48.62453 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8b92380-20d5-341d-8773-681924c466f2 | -2.2512 | -48.22943 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08e53f26-b599-32af-8988-6ab24ee43ba0 | -4.27631 | -50.67855 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ff23b4f-3f3a-3fb0-ba45-19b1155e5ce0 | -2.81878 | -51.81042 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e316b227-3220-3bcf-ac75-186e879d6721 | -2.36594 | -46.79585 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19283928-bb9c-3bd4-a149-9fda465db802 | -5.25125 | -48.07928 | 2024-11-10 04:14:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a322a5a5-3f09-38f5-ad7b-b3e8f83d16f0 | -5.01569 | -45.0432 | 2024-11-10 04:14:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 805260b0-3d36-33db-a0ee-5cdac412e098 | -5.05255 | -44.27733 | 2024-11-10 04:14:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60618af4-8a47-3c47-842a-aa3b4ca4f286 | -2.05346 | -52.08833 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7d151f8-1eb4-3755-b5b2-c443517369bc | -3.84333 | -49.96782 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5cfa443-9e9e-37f1-8c4c-139cf350c53c | -3.59588 | -42.85167 | 2024-11-10 04:14:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fa7acb8-6eb6-33ad-9d15-0a6acf2dfadc | -2.52551 | -46.30322 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 062a2930-2252-3897-aace-a7c52ab10cd9 | -2.61074 | -47.96018 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f400204-de16-3e82-8dad-6ff3b9a9f069 | -4.18487 | -50.42444 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cdbaac0d-46a5-318d-8906-720eda3c02d6 | -3.35091 | -50.35805 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a48697a-cbcd-3685-bd8e-a3065c2c8470 | -3.52133 | -44.03804 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 114ab363-5bd4-37fe-a077-9ff978edaee2 | -1.4849 | -55.43794 | 2024-11-10 04:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| efd11113-7ae8-3427-9ad9-c2ba583decab | -3.8425 | -49.97274 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2621246-3b96-3455-a846-767bf47b2689 | -3.11837 | -50.15341 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ee3982d5-4782-3f2e-984d-01078d45cd52 | -2.23773 | -53.77874 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9890e24-ff02-30a6-9f4a-44b6107cc4b8 | -2.92721 | -48.31129 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ba6c355-ccc0-3428-8cec-9d43d677d5e7 | -3.96325 | -49.01326 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5cd8bc7c-7d5e-34c0-940a-c6940a385720 | -3.24106 | -50.26933 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4a607ffd-451f-354b-b4a8-7f2be14fb5e7 | -5.45539 | -43.27094 | 2024-11-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a0cfdbd-bad1-3df0-9f03-b73cbf72f41b | -4.21134 | -48.12772 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ff5d74e-5fb4-3d1b-b1c1-7844ca450d73 | -2.10638 | -45.33615 | 2024-11-10 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdae66ed-199e-3355-b47a-4f4ffd596a17 | -3.22563 | -50.44961 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2787f1d8-8f18-3785-be13-adc4a7490bd2 | -3.06305 | -51.38016 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1523eba7-d3b7-3a65-9f93-7b223bad6da2 | -6.73228 | -40.81213 | 2024-11-10 04:14:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 617029db-db8c-3feb-aba6-b152599df1f4 | -5.73005 | -41.9854 | 2024-11-10 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cf817390-a844-3bcd-abe9-5b6c490f773e | -3.81284 | -50.78499 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c1ece83a-340e-30d0-961c-80c82c6aa3e5 | -3.22412 | -50.31931 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe62b08f-8cf3-30ea-b950-79df799003c1 | -2.37288 | -46.7771 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b82ef6d-f389-3d6a-8594-042cca3fd06d | -1.52118 | -54.99416 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 79f79404-0268-338c-b7f3-ef74bada6805 | -1.51087 | -52.15826 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b0e205e-9c22-365d-88b3-40eb8cb21705 | -3.24356 | -50.32242 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77b9cdac-974c-37f3-a699-9193e185b9c4 | -2.3202 | -46.73409 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52874212-d4a2-3c31-b6c3-d5b41f5460eb | -2.95058 | -54.68401 | 2024-11-10 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93db57a4-f936-3ce0-81c5-b59746b16784 | -0.47005 | -52.02589 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff010d09-e825-3a7e-89d3-08f9097d5584 | -2.71189 | -49.18143 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e05b23aa-fdef-3db8-b741-2a8e500ea486 | -3.09282 | -51.2928 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fbd2bc8-b30d-3ef7-899d-7d21ffdb6c73 | -3.03283 | -51.53062 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d130e3d-95df-3712-91d1-68b52b4001f1 | -2.93353 | -52.76926 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 862671c6-2beb-39e2-9e8d-3db4c5725b12 | -2.51759 | -46.37689 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4afde22-158b-37d0-8a0b-ed57c2250338 | -5.32189 | -45.06029 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6d3f5916-e359-3f12-be94-fa910c27a07c | -4.57819 | -46.03527 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31d61268-2025-3410-a9c3-081ff2084a44 | -2.57141 | -47.34578 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45388de5-7a88-387d-8e29-e47674c4024a | -5.66708 | -41.75434 | 2024-11-10 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 23d05199-a429-3a6a-b76b-9a7946e233cd | -3.06674 | -48.03523 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f493f6cd-2943-3390-83a3-a1f24df3f382 | -2.63691 | -46.76688 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 017cf973-91ef-38e2-820f-e29761c17036 | -3.54944 | -49.98475 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1e850ef6-4329-3be3-8ba3-1ee47fd8bb90 | -3.95435 | -48.16348 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 178314d7-45fd-3d69-8e52-598ce4dcdb03 | -3.08236 | -50.56706 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7492fe29-ecb4-3ed1-81bf-73dcbffbd72b | -3.41737 | -42.29225 | 2024-11-10 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 258939e5-351e-31c7-b7cc-72b33221c296 | -4.4362 | -47.26271 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b8c539a-600f-3782-a729-85256a2f2740 | -1.52736 | -52.20034 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0543f9c7-6304-3052-8afe-6a5374bb57e5 | -4.19829 | -40.67506 | 2024-11-10 04:14:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e9334287-faf3-3092-baec-518419e213b4 | -4.27353 | -50.18667 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 026f9435-d863-30ff-a113-56764036565c | -1.64236 | -50.4381 | 2024-11-10 04:14:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd038822-0651-398b-a317-02875ffbed09 | -2.89263 | -45.36545 | 2024-11-10 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdd60b54-3fef-3b62-a07d-cc600072cfdf | -2.67863 | -46.80298 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51bc47f2-af7c-3cc0-bc74-46b9e1031691 | -4.24779 | -48.54455 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18bbd1de-6921-32b7-a767-902625587492 | -3.12705 | -45.96532 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67aef3d6-413d-3f24-a5a8-72d419c26b85 | -4.58777 | -37.80849 | 2024-11-10 04:14:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c9ff668-020e-34c7-9aae-b0e7920c03cd | -4.79997 | -45.38927 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25a6d693-0a12-3840-a5f5-c9c9ffab1e13 | -4.49865 | -48.49583 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2cd53ddc-af72-379f-90f5-df5be43fc844 | -1.17502 | -52.09777 | 2024-11-10 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3f354c21-07c9-3b92-a89f-58975b080a2d | -3.38828 | -51.46639 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 082ca1b5-2e93-38a4-b962-1332085831b4 | -4.505 | -45.46854 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77379158-920d-334e-859f-8ba16b9756df | -2.68485 | -46.81375 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c24ed6e1-fdd3-378b-b98e-f43fe7c40344 | -3.70271 | -47.63585 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README43.md)
