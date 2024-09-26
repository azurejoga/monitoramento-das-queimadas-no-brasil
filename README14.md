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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9104796a-4469-3df2-82a3-b82aa53750e2 | -4.78955 | -48.10547 | 2024-09-26 00:45:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eae05707-76b6-3bc1-942b-17226de89671 | -4.77662 | -47.6196 | 2024-09-26 00:45:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f9b8be92-aa00-34db-9c04-1223c1a507d5 | -4.77751 | -45.88619 | 2024-09-26 00:45:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 50d03339-5f33-31bf-8504-000b125381e7 | -4.7391 | -46.60148 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0476605b-bd2d-3be5-9b62-903dafac8738 | -4.73012 | -46.60276 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eec04371-5e3c-3776-ae59-0e16c45cd912 | -4.66578 | -48.16103 | 2024-09-26 00:45:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 874a0e02-5df6-392f-acb3-357c7e06a547 | -4.66434 | -48.1503 | 2024-09-26 00:45:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| c06aec61-b67a-3026-af35-93c1f1051f2e | -4.6345 | -48.53723 | 2024-09-26 00:45:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 72ea4a94-44d3-37bf-8d3e-6d4ccb45b5a2 | -4.62998 | -46.34637 | 2024-09-26 00:45:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7fc725d8-4233-36cb-aa9b-bfe8ef15b534 | -4.58811 | -46.30647 | 2024-09-26 00:45:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 00fd53a7-bcd3-3e5e-9af8-99084f4d5014 | -4.58657 | -45.69403 | 2024-09-26 00:45:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 287d0ded-6ae0-3828-a4ba-7bff39b58768 | -4.58535 | -45.6852 | 2024-09-26 00:45:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 262ff5f5-0091-3c28-b1ba-13c23374fed9 | -4.58044 | -46.31675 | 2024-09-26 00:45:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bffc8072-8b80-3a51-b8c4-259e643babad | -4.57921 | -46.30775 | 2024-09-26 00:45:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 90741a8c-9b34-3347-a6ec-6ba232218a83 | -4.57531 | -45.69288 | 2024-09-26 00:45:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 43f053a4-50e3-32ce-bcde-9ef64a7ff30e | -4.51505 | -50.81174 | 2024-09-26 00:45:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 84572191-d63f-3cc5-91b0-ad5cd0ee1ce5 | -4.50403 | -45.90693 | 2024-09-26 00:45:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 5468a17f-0b27-3ce8-bdec-b85a98ebf017 | -4.5028 | -45.89809 | 2024-09-26 00:45:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3ad220f6-c109-3ba7-8da9-75d5dd77eaee | -4.49518 | -45.90816 | 2024-09-26 00:45:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ad103564-8f79-31a8-9ada-e1e2d4f4b858 | -4.49395 | -45.89933 | 2024-09-26 00:45:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6d01bc63-b74a-3455-8e77-663d4071f8e0 | -4.47237 | -47.7373 | 2024-09-26 00:45:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 006ad7c4-406e-3116-baf5-98c5bab89d8f | -4.28506 | -48.06649 | 2024-09-26 00:45:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 81cca06b-a83a-363f-9f0c-af73fa821461 | -4.26512 | -48.23583 | 2024-09-26 00:45:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e9915585-c861-3e82-9303-5d3cd9b0f31f | -4.24242 | -47.00824 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8dfa88d3-e413-38ca-940c-85a06a2b2c31 | -4.22079 | -48.19875 | 2024-09-26 00:45:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ee41dfa-067b-3f5a-9fe7-1e4ebde541a4 | -4.19551 | -48.61712 | 2024-09-26 00:45:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ddc315f8-265d-37cc-9c51-06394ea9d981 | -4.15777 | -47.19862 | 2024-09-26 00:45:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5fe48eab-5c64-3737-a8e2-1866cffd4786 | -4.13678 | -46.71045 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25ad6524-a544-3910-9668-e85fd4208936 | -4.13552 | -46.70133 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 84023be2-3cca-35c4-a2d9-0eb38205c1d6 | -4.1044 | -46.80807 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ef8c25a6-771a-3a05-a0a8-bc313b07d1bc | -4.10315 | -46.79889 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 1fbb422b-1b53-3f0f-bebe-2fbfa407aa64 | -4.06051 | -44.05101 | 2024-09-26 00:45:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 2ffae2fa-76c7-3aee-97ef-7b9c876b4bed | -4.05918 | -44.04158 | 2024-09-26 00:45:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 23bda4c6-d43b-3514-8b9d-7943e8240123 | -3.92522 | -46.44836 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5b95461b-e806-3f30-aca4-ca0da476778c | -3.92398 | -46.43942 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| efee72ba-3f45-300d-a694-7cc5627e4ba0 | -3.91755 | -46.45856 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |
| d60b3d91-08dc-370e-81ae-530cf19bdbcb | -3.91631 | -46.44961 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| afb7bccd-c133-3d4a-adde-bd433b0e3630 | -3.91507 | -46.44065 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9fb95f75-23ad-3281-98ea-870b6c536883 | -3.91259 | -46.4228 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 25c4e4f3-cb84-3bbd-9b24-30544545a17e | -3.72494 | -47.72794 | 2024-09-26 00:45:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dc89ccc1-2115-3199-aa7d-376ee6a26042 | -3.70075 | -47.62133 | 2024-09-26 00:45:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6ab652be-6a4a-33b9-9b30-e5a15b3c2c99 | -3.69941 | -47.61159 | 2024-09-26 00:45:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 471d24eb-86b5-39de-9a3c-eee12c2fc191 | -3.57218 | -50.37835 | 2024-09-26 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3862bf14-d972-3ca8-a65a-5bc400c61008 | -3.56701 | -50.58869 | 2024-09-26 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a7399674-7d22-3f8c-a020-40404fe0d550 | -3.56497 | -50.57383 | 2024-09-26 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 900b9ba3-f8a2-3ad3-bb14-c8c8c70f1637 | -3.56326 | -50.38816 | 2024-09-26 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e86be1c9-dc7d-33dc-8764-554971ce0186 | -3.56136 | -50.37371 | 2024-09-26 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 237ac7b1-e990-34b5-af7f-fd9e91cc7705 | -3.56106 | -50.37994 | 2024-09-26 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 631bcfc8-7759-3a3d-95ad-688c6b4cc99d | -3.34815 | -53.78553 | 2024-09-26 00:45:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| d592f4d3-d1f3-3332-8452-bf75f07b80f4 | -3.3287 | -53.22005 | 2024-09-26 00:45:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 6b28381e-225b-37e0-bf92-363875ccfc53 | -3.32536 | -53.19619 | 2024-09-26 00:45:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 9ab27ec3-4ed2-34da-b9e6-7bfdf2679cf4 | -3.32486 | -49.05212 | 2024-09-26 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0a7eb731-3d32-39f6-946d-e149cc155499 | -3.32417 | -47.02819 | 2024-09-26 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4e1cf8d0-21e8-3264-9446-51a6ff90a4c5 | -3.32329 | -49.04058 | 2024-09-26 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 517f6214-0d5f-3362-a77e-9c64827954b7 | -3.32291 | -47.01903 | 2024-09-26 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dd541dd8-2a5f-374f-8ae7-b44c0dc4ca1b | -3.32282 | -53.24012 | 2024-09-26 00:45:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 988205d6-d15b-3952-83e5-714461694789 | -3.31963 | -53.21588 | 2024-09-26 00:45:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 232.0 |
| 801193a6-1cd0-3545-a660-6cf1885bba43 | -3.31474 | -53.22215 | 2024-09-26 00:45:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 88542a44-b3a2-32da-85b7-87c3214eae34 | -3.25777 | -53.32912 | 2024-09-26 00:45:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 2bcc8f3c-edf1-3b55-a8a2-14a549660761 | -3.2331 | -50.32652 | 2024-09-26 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 7f66eb00-918b-358b-94af-608284627455 | -3.23118 | -50.3124 | 2024-09-26 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 00bdf695-65a6-3145-811c-df4decbbdb6b | -3.22206 | -50.32802 | 2024-09-26 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| dc40e85c-af88-312d-add7-c38be6e18e37 | -3.22016 | -50.31391 | 2024-09-26 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 852013b1-4dd0-33f4-9913-f8884b893aab | -3.21526 | -48.92176 | 2024-09-26 00:45:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 17e185c2-8afb-3e08-a23a-e061cd50c35b | -3.19684 | -51.1467 | 2024-09-26 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| e3772a65-fdfa-3611-8fba-0a642de945d0 | -3.14704 | -50.28739 | 2024-09-26 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 3d301067-6cdc-357f-be74-0f28505fc533 | -3.13606 | -50.28889 | 2024-09-26 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b709e83a-1d14-321c-9d94-7ce17a329aa1 | -3.06495 | -46.55121 | 2024-09-26 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b44617eb-6b51-357e-ad95-30c2014e3303 | -3.06371 | -46.54228 | 2024-09-26 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff5acd9b-0b03-3af1-9e10-21dd6ad0c24b | -3.01662 | -51.08467 | 2024-09-26 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a158fcec-fab1-3d5b-b757-ee1fdb07a63b | -3.01449 | -51.09579 | 2024-09-26 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dc8c2733-02c2-3cff-b9b2-4d40306bd075 | -3.01235 | -51.07949 | 2024-09-26 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 7a49c8a3-0e89-3058-8e81-34d81a22dd81 | -3.00497 | -51.08648 | 2024-09-26 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| b0dbf376-7111-31ff-b3d3-dc8c5a3acf37 | -2.95905 | -49.35994 | 2024-09-26 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 77e6d6f4-1d48-3676-bd74-c1ba040cd301 | -2.94884 | -49.36136 | 2024-09-26 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 733aa790-e7bb-36dd-9f69-5ca4487300e9 | -2.82672 | -49.14552 | 2024-09-26 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 1e1afeba-60f8-350d-b904-86d88d2d9d0f | -2.72161 | -46.73326 | 2024-09-26 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 161342dd-cf7b-3187-9fa7-3dc531573f1d | -2.68551 | -46.74461 | 2024-09-26 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 72a1bb22-dbb0-33a4-9b52-5e60e4e0dfa7 | -2.68426 | -46.73565 | 2024-09-26 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8fc51c2c-10f2-3049-ba68-cf9de8c513c2 | -2.46059 | -47.8401 | 2024-09-26 00:45:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 599eac32-4726-31f1-8eeb-0c36a74499d3 | -5.88908 | -43.88429 | 2024-09-26 00:45:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a308af28-7bcd-380d-af79-5e65cd6f913b | -5.66916 | -43.37943 | 2024-09-26 00:45:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bec35800-bf4d-3677-94ec-8026835c3705 | -5.63257 | -43.63618 | 2024-09-26 00:45:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| d197b833-9627-319a-93eb-e38a3b8e9ee8 | -5.63122 | -43.62666 | 2024-09-26 00:45:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0771226e-7ab6-370b-acfd-8e5cdffaaf57 | -5.62341 | -43.63751 | 2024-09-26 00:45:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f08c8246-2f63-3117-a383-c42ec84c4c9f | -5.62206 | -43.62798 | 2024-09-26 00:45:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 32350363-8aee-360a-8138-ce52b782fd86 | -4.59597 | -43.60863 | 2024-09-26 00:45:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e58a95f5-eb77-3004-be79-e878dc2f1f2f | -4.59458 | -43.5989 | 2024-09-26 00:45:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e3ac9aba-bfd5-33f9-91c2-c9a03139823b | -3.79699 | -41.60818 | 2024-09-26 00:45:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| ba4f9034-1d98-3567-ab72-44baef272222 | -3.79513 | -41.59517 | 2024-09-26 00:45:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 714c9dd5-6b4f-3ebc-b2dc-03a5ebb092cd | -3.79325 | -41.582 | 2024-09-26 00:45:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 420d9174-264d-3b88-b377-9f37c6b500c4 | -3.30235 | -43.51763 | 2024-09-26 00:45:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fbfeca05-bed0-39e1-8b2f-9a0cb414ca00 | -6.09136 | -47.67506 | 2024-09-26 00:45:00 | TERRA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b44ccea4-ea11-36dd-aa00-6440f3f7c057 | -5.96819 | -44.57799 | 2024-09-26 00:45:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5d47e98f-68b3-3e51-8d57-563485387f8a | -5.883 | -48.10148 | 2024-09-26 00:45:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 7891c0e6-4ee6-35de-888f-b13c983ed95c | -5.7353 | -46.47957 | 2024-09-26 00:45:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6bd07201-d7a9-3e64-b78d-f136842c2aeb | -5.72629 | -46.48086 | 2024-09-26 00:45:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1280e062-eef1-3925-a68e-c6bc78f83302 | -1.0553 | -53.3553 | 2024-09-26 00:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c592f92f-add4-3a2c-a14f-9df3cb108060 | -2.6496 | -54.6172 | 2024-09-26 00:45:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 8a039c4a-f607-316c-8dfa-db09499b62c8 | -2.6601 | -57.5507 | 2024-09-26 00:45:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |


[Clique aqui para ver as próximas entradas](README15.md)
