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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e3282b5-96fc-31af-ac4e-ce9a0ed8cb72 | -3.26342 | -50.21609 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a028f49-7d9c-3973-bde0-8454f2167d8d | -3.27198 | -50.20885 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bafcd6e2-e1b1-35b3-ac5d-8d6c5bdaecde | -3.33757 | -46.05579 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cfcded46-71b6-37a9-a4f0-3912f297ca65 | -6.11382 | -43.96657 | 2024-12-03 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c2d9379-9013-3bc6-8e4e-be1fec9bd279 | -3.98918 | -48.15411 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4652df70-8d2a-3a15-b95e-3804a26944cd | -2.65841 | -46.12243 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13ed09a1-2b1b-3e3d-ae58-7d792410ca1b | -2.7325 | -45.2105 | 2024-12-03 04:29:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1502bc0d-8acb-3242-b469-d28f8d7e23ac | -2.67142 | -46.27753 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2986e2cf-686c-3fd9-9885-88ed0dd5342c | -5.00131 | -42.94816 | 2024-12-03 04:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24c70f3a-0ff2-3b44-9859-704ce9ab905e | -5.89765 | -46.235 | 2024-12-03 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 316133f1-9820-3ad4-b0c0-eb926727297e | -3.16537 | -46.29025 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d95e2ba-675d-35e2-a604-43079ba642d0 | -3.4727 | -49.92473 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7350c62d-97c9-38c3-ae06-cc8a07399ada | -2.55452 | -46.35112 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81a226ed-4459-3038-ae85-da21d58d6500 | -4.18748 | -46.61651 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9bf1c2c6-db6a-37f4-a365-3ef6a5d6a3a2 | -3.406 | -50.25908 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ba51b98-81bf-3615-9175-f57870f596cf | -2.33143 | -46.10695 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de45356e-4709-3f68-8987-e54b6b5ed3fd | -3.17879 | -54.33112 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d95af57-b944-3afd-b552-2e995540f78a | -2.71596 | -46.18857 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 636d5647-9d9a-3a9b-988f-7138d1d67c65 | -4.01132 | -47.00253 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ea200b9-aa67-3ecf-b21e-4dddff942d66 | -2.20759 | -53.78597 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1517c103-9832-3193-b066-9df020cbec76 | -3.25587 | -53.67069 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e7bcfed6-5b8b-300b-8aae-d5adc60a93c5 | -5.56442 | -44.88863 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 79c9869b-3b4d-32fd-a0a2-c0fd80f1e993 | -2.97147 | -46.94197 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be5e44e7-fdb7-3a10-b7e5-9fc4778ab21c | -2.4347 | -46.50904 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ca27b46-0db4-347d-bc45-ccfc949d2701 | -3.33407 | -53.21749 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1ce2ae1-8e2d-3dad-b41c-b606ef445d68 | -3.33562 | -53.37481 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fef0cf19-781a-3e6c-b09e-069a39064605 | -2.77917 | -55.36393 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f4d4b4f-6b88-3505-817c-8191bbfd9fc9 | -4.48217 | -46.35842 | 2024-12-03 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18f80ca9-0c55-39f0-9f4d-4f755e9f548d | -2.21649 | -48.38326 | 2024-12-03 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc151acb-b038-304a-9dc3-f223c891400b | -2.89986 | -51.57873 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c50e2a57-c9dd-3412-b78e-304e26fb8922 | -1.1064 | -54.12253 | 2024-12-03 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a0f67e7-0f90-3584-a093-69e2cc2bb519 | -1.21809 | -54.09953 | 2024-12-03 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00def1e8-ef39-35f2-8ae5-de8d8e942cf2 | -3.95543 | -44.05285 | 2024-12-03 04:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bef18439-6936-383a-b9c4-0493d87f8e92 | -3.37076 | -46.66925 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80e57a85-887a-3225-8966-e5368da4134d | -3.09382 | -54.29737 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26278fb8-ad30-30d2-8c67-2c17d575dc1c | -3.2143 | -54.23468 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69ed97c0-9a7d-335d-8ceb-12880d6c823f | -3.97401 | -46.72128 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aea3c026-070e-329d-8dcb-7cf9d1525d07 | -3.29692 | -53.6733 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 3059a034-2590-3499-8a09-ceeccf6b28f8 | -7.19638 | -48.60493 | 2024-12-03 04:29:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 768072c9-7316-3ae2-8574-0b99799c8b56 | -3.89501 | -46.68421 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d65c157-4745-301c-9d66-50bd37613a41 | -2.77408 | -55.3631 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75bbda1f-fbff-3432-af4c-9e3074135929 | -4.7442 | -45.11467 | 2024-12-03 04:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95d53b28-6c58-3481-a676-a82c34b862b4 | -4.31196 | -48.21914 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02657774-94ee-3e0c-95ef-bb7d682606d1 | -5.14589 | -43.23366 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2f04a204-436b-3a2b-a165-faeb82ff0636 | -7.56569 | -45.73122 | 2024-12-03 04:29:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3a8f76ef-6ab0-3889-a680-5ba2d8b88415 | -5.38786 | -46.36494 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fd0da2c-8640-346d-93ed-6d941b1ddf84 | -4.40132 | -46.3996 | 2024-12-03 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de5b1976-b164-383f-8c57-eff4d99029bb | -2.53464 | -46.34803 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b5dc92f-f688-390f-9563-4b681075e045 | -4.17187 | -46.56428 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d42199b7-c9d0-3c95-98cc-fb97cb4bf377 | -3.05641 | -52.76476 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72adf061-d41d-31ad-9a5a-daf05bc5242c | -2.47181 | -46.5747 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c524082a-8066-3204-8af3-afff4db46c11 | -2.58715 | -46.57509 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48746282-0962-3863-a68e-3ab1eca45a8b | -2.64234 | -46.11636 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1302c452-9e21-3d4c-9e30-fa71901fa340 | -2.46623 | -54.11171 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dbb2b5f-8788-3a62-ab99-7bc62858ffe8 | -3.93142 | -47.98405 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 006f3f37-c25c-31ad-a3e7-85df2fcdb817 | -4.29919 | -48.21354 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1300534c-e2c2-32e4-9233-efd010cbd2d9 | -3.54765 | -50.17754 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a3b5ba56-ea5c-3b95-886c-5e8143609baa | -3.81444 | -46.54722 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e82b1c99-e7f6-3d4b-b738-a479f000acc6 | -3.76298 | -46.50783 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d61cef90-423c-32f3-ac74-ce9905be8d4e | -1.94912 | -53.34321 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 242540af-da8c-3b9c-b9b7-1296ac448bf4 | -4.8032 | -44.9979 | 2024-12-03 04:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92d2805e-18be-325a-837e-5fa421c7dbb9 | -2.81119 | -53.04934 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8eea939b-9319-36a4-95d9-f438977247fa | -2.98462 | -46.92289 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbaa5b49-a42b-37ae-9d6d-6c2f7efda3db | -4.43223 | -46.59375 | 2024-12-03 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b918b62-8350-3f86-a689-6a5642416fef | -1.94394 | -53.34693 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30186b46-f59d-364f-8bb2-febcb665ccbd | -3.37435 | -45.84105 | 2024-12-03 04:29:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc486743-cf19-3184-a972-9e4afbf84864 | -3.33737 | -50.07556 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b65de71b-61e1-3505-995d-3eaac8a72944 | -3.34535 | -46.04971 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b202465-a75e-33a2-9b84-e85ff7a9e8c2 | -6.17966 | -42.619 | 2024-12-03 04:29:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 51797c1a-25e3-37bb-8e93-6070455f46a6 | -2.60168 | -46.54953 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd92e1ea-d309-3fbc-9bdd-764731147d84 | -4.06971 | -47.08609 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de3c7830-fd83-32b7-baec-3b6ddf33d958 | -3.37574 | -50.70401 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 954fac2d-5b17-35d8-95e8-fa57e9b76f75 | -2.47283 | -46.54668 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc3173b2-5de9-3a1d-a235-d277c5de6fb0 | -3.26387 | -53.62157 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12c7c163-d5db-30d7-883c-b54668d47a1b | -4.30676 | -48.08186 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11b8be1a-5fa6-3676-938d-7509d9306863 | -3.45925 | -50.01482 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10dd6eea-00b1-328b-b4dd-c7dc098d3924 | -5.40875 | -42.92952 | 2024-12-03 04:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 73dd4ef5-7ded-36c1-b532-9ecacceb1bf2 | -2.42968 | -46.67028 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf27a74a-66b4-337f-b719-d46c00b975e4 | -2.85286 | -45.83311 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e864531-c130-3d15-ae29-7b2bfa1a7cca | -3.77739 | -46.69741 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb57edb6-cd22-3c78-a62f-16b5c5e0d987 | -2.46742 | -46.58107 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08b4de3d-3a21-3d95-bddc-5b9ab6471207 | -2.97667 | -53.88435 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 234f95c4-d834-36d4-bdd0-6d7dfaa05ff9 | -3.90096 | -46.64616 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ca7e277-afcc-3825-a501-8de3304cc64d | -3.82037 | -46.68287 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0b9e926-0000-35da-843c-cdf296fef800 | -6.03578 | -42.52494 | 2024-12-03 04:29:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 2c0f89e5-14a6-3897-a74b-f58ba4c6df58 | -2.56271 | -47.33587 | 2024-12-03 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 813093c7-a401-358b-9748-c55479d294bc | -3.43284 | -54.11459 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13496405-d81f-3a96-a81e-6f0b193d9a37 | -2.5761 | -53.98044 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ed49683-bce3-3f44-97a0-18ed6caca607 | -2.75236 | -46.13013 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18c2b56f-b7f6-3fb6-991b-688a9c13f2b8 | -4.26506 | -47.61372 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c6c9481-e151-3241-9346-ee8a06257367 | -3.92158 | -52.39586 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1849a14a-6804-34fa-8d2a-81fe908184ee | -2.15124 | -50.69939 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e49af10d-3fcd-35c5-a1a1-a58a135e4400 | -3.89893 | -45.00955 | 2024-12-03 04:29:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61932f84-733e-3a38-9da7-430b67f6a7c7 | -5.45689 | -43.58015 | 2024-12-03 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3f1daa6-446a-3d17-9d90-33c0b8b27046 | -2.72825 | -46.2402 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1697bd6f-def4-3fee-8f24-f541bc0f1536 | -1.40767 | -52.2179 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4cf10b28-1a47-30b8-9243-03c7abe12899 | -3.5075 | -53.83189 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe140493-51df-337e-b2e1-ee3b885e3060 | -4.09452 | -47.42494 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a608ffb-08c4-36f9-9dee-8e2fe8b1b818 | -4.31641 | -48.21267 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0de1132b-7906-3fa1-a1a3-78c98cc087f6 | -2.59736 | -46.57708 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README48.md)
