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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcb5a6e2-7d5a-3848-a5c4-d19fb61a92f6 | -4.04007 | -54.11201 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0afb10a8-fdf7-32ac-a0e4-f286a8e2e84d | -2.37401 | -50.40507 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2290fb8-227a-3273-8b09-22250d6a92ec | -2.65266 | -46.581 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 908c5b1a-2152-3463-961d-0c3564e45edb | -3.84411 | -46.65389 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9cdd75e-09b4-3789-afb9-72c9ef72f433 | -2.36034 | -55.87712 | 2024-11-30 04:40:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0003b928-d218-3a4c-a570-bea4848a6d09 | -2.52179 | -48.18317 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72a8c4bc-fdbf-3ea6-9f7e-7e339ae55157 | -2.89121 | -55.22817 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 83c26718-1bef-3737-9de7-8496e3aa2079 | -3.60931 | -49.99675 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eccb4cf2-ef6d-399e-905e-f60528b3a780 | -2.95113 | -45.72021 | 2024-11-30 04:40:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e208878-dd04-32e0-bff8-c9ae9db1d266 | -4.14674 | -48.22882 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 976549fd-fc0a-35b4-9853-a66d95b71cf8 | -3.83286 | -47.46309 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fae7e298-4535-3c7b-a8d1-6842fa38fabb | -1.23998 | -51.79466 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7fbc937-e656-3d78-a192-33c6f8affee0 | -2.09283 | -48.62025 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 490f87dd-58b0-38e2-a27d-7e2ba1125530 | -3.24208 | -53.41792 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9aa80514-078a-3336-938b-ef3051d8b6aa | -3.27469 | -53.4129 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09db7f3b-8cb5-3288-a2fe-b5396136f186 | -3.30307 | -50.27732 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76fb0ee5-fac0-3091-9a68-315fa58c5f04 | -3.31123 | -46.65477 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ba25d58-a0ce-338f-a63d-b5e33eacea2d | -3.9324 | -48.14162 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18ebcdd8-f87f-3e98-9ea1-5f28099607aa | -1.63716 | -54.35867 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0c790dd-c68d-302f-a02e-d93b3ed9c3ed | -1.07504 | -53.38927 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4790f81c-5f69-309d-9e97-1fade2570117 | -2.71831 | -48.6022 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e78b6882-4017-3ee4-9ad7-96f1e00fa6d7 | -3.73409 | -52.33677 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35c7486d-b7b3-3814-a18c-0633f3d2d4cf | -2.27986 | -48.49167 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e83fe417-93b7-3de3-9389-9680b4e76ba3 | -2.63474 | -46.88168 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 93ed1edc-e0dc-3ebf-ab64-9aeb3da1b09b | -3.38049 | -50.11174 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38d482be-650b-3f5f-acc1-4558fba11bb6 | -1.6186 | -53.88193 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc5084b8-44b1-336b-b287-2e55dcc88142 | -4.14179 | -48.23882 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff653763-100a-380f-b42a-8c71b85ee697 | -4.43802 | -46.01315 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| fee858ae-a428-31a6-9625-9232dc976abc | -3.05075 | -50.27848 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd2eb606-467f-3645-9c99-2f13eddb3715 | -2.71608 | -48.59481 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18a2cb5c-b3eb-3924-b8a8-7a13e147eeaf | -1.80747 | -50.90174 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76acf227-3347-3a86-bd89-2873e6c701b9 | -3.13056 | -53.26332 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 887c4b22-db28-3e1e-8f75-ca305f877297 | -3.4231 | -49.44835 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d37c4c7-2c36-31fa-b1df-c9d356732cd7 | -1.03858 | -51.73982 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0fb3040c-958d-389b-b1f9-866ddeef919a | -2.82315 | -51.95698 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6218cbc7-62bc-3b76-bacb-13c747a18d9f | -5.38946 | -44.82829 | 2024-11-30 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb704ce0-25c7-34b8-a64e-bcf7f93631ab | -1.32301 | -51.74612 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3b2d3dff-f6eb-3114-b504-ea613546381f | -2.44457 | -50.37524 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa3e609d-fe80-358e-a080-85bd1363a746 | -4.05301 | -46.82631 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 304438de-0426-39b1-ac75-6a9265956db8 | -1.57263 | -51.24207 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9985d30f-8198-3e8f-90b1-2f8a04bb2ee6 | -4.54892 | -50.83521 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 306b30b1-5db1-337f-a78d-edc9a732d83b | -3.33217 | -46.61094 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01a5a67c-3bbe-33c5-b9cf-b7d96b836da1 | -1.77625 | -52.94975 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e028b5f-0c27-38c4-a0bc-e6151b968ecd | -2.88392 | -53.98026 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b31964ba-6546-3191-975e-dd8b8af6770c | -3.84484 | -46.53066 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3094854c-9b00-3197-8148-c4473ff29366 | -2.25353 | -51.11733 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f90a5bed-0b4e-3a8a-98ae-65bd36c0a2c1 | -3.97804 | -46.7217 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfcaa92a-67e7-3d7f-a637-d1a379b822c9 | -2.83711 | -48.47265 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a993f031-ddf9-390b-9c6d-6883ce6c99c8 | -2.71331 | -48.59087 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f77a906-9254-329f-bffc-1ebf6e73e9c2 | -2.69082 | -46.11561 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7dc1e57-5a4a-3425-a82b-ed6fcd1bd7ee | -3.29175 | -53.83475 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cf89852-71df-32cd-ab5d-ec147014957a | -2.98209 | -53.35378 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42fa3006-1ee7-3d9f-8d78-ba9b32985981 | -2.18436 | -47.90343 | 2024-11-30 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc6c4443-e3ec-3553-b6bd-41b438e5c65d | -4.03952 | -54.11547 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4edc73ba-51b1-3ce7-a447-3d2f8a27f321 | -4.36629 | -45.52332 | 2024-11-30 04:40:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83b33732-1bc2-35d7-84c1-4f51aaf3d851 | -1.26694 | -54.55429 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2ff193c3-191a-3b57-bd4b-4cc6b4260666 | -2.9525 | -47.99372 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc9cbaa8-9a8c-3b52-82fc-0eb8686b572b | -1.0865 | -53.3945 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cd1ad1d-1506-344a-b693-3edb4340a7c6 | -2.70371 | -46.12572 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94757e02-d5b6-3370-817d-2c90cb27c631 | -2.43838 | -46.51421 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ce5e0a3-49a8-3cc7-8633-c84948e78eb3 | -1.26171 | -51.63195 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5f73ca8f-dff3-3830-aeb6-aaf9754c014c | -3.98325 | -46.73422 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f671b9b9-e24d-373d-bbc8-e71e3a8d5e2e | -2.63388 | -46.20391 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bebdca7-a6fa-35c6-a118-c7589874529a | -3.22464 | -54.17429 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dc58d3f8-bf15-38b2-91b5-339f3776c20f | -2.61215 | -46.57562 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 287c6ad2-7171-3f56-9668-2c56091b6ec8 | -3.06066 | -48.52184 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e26dde78-74f7-3379-9f45-d5555095e29f | -1.10257 | -51.93107 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ace1edf-1943-3636-af0f-5fc2e6a9d6f9 | -2.1898 | -47.14758 | 2024-11-30 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 48ce9631-c232-3614-ba75-f1d8d8b21c8b | -7.13539 | -46.4194 | 2024-11-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb83c7f7-4b87-32ec-b7e5-4acf21ad38f6 | -2.54141 | -47.32986 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0dc627eb-8511-3e61-9111-b157af823d7f | -4.14728 | -48.22532 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d39d9b7-bf96-35b1-a586-b184608dbf1f | -3.03124 | -53.0374 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb40dbf5-4a06-3de4-a88f-83ac7ad58ad7 | -3.15453 | -53.83509 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e508a45d-787a-34e4-a9fd-c305e2a636be | -2.72501 | -48.62434 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b48d2208-443c-3de3-bce1-1ad9b60c5a10 | -2.97777 | -53.89031 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bca8e897-79a0-34f5-963f-ce43027cddb7 | -3.14904 | -53.24661 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eac06938-5657-3b0c-93dd-7b60deca3024 | -3.28167 | -45.56766 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 86e75a68-8c26-3ff4-b6c5-9f1d4f1bf48d | -3.78682 | -52.4081 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d640fa98-cac2-3e47-9a14-8b6e072205b7 | -3.08899 | -49.47429 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6a98b61-65d1-34fb-a0fc-795ae6c02f1b | -2.6567 | -46.57774 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 32b4d949-fd7a-383f-8047-3a196675aec7 | -1.49215 | -52.43898 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7c79720d-bb73-3926-9f22-1829573569a7 | -4.06075 | -46.68171 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6413b00-3af8-3278-a893-3d7e902a87f7 | -6.08655 | -48.04144 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dc4e516-a6f8-3502-a11f-5700c3a4cfa9 | -2.01177 | -51.19173 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eea37a6f-919f-3c03-8abe-daa767649d1e | -3.65296 | -50.21592 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e8ee845b-bc75-388e-a7fc-9decca272330 | -2.76285 | -54.08619 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92bb7719-bdd8-3b4f-a852-10d49083fafa | -3.08904 | -51.40477 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba0e0b1b-f2af-32bc-874d-01beab10a360 | -3.97306 | -49.91095 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b04f524f-1f34-3e03-8628-1a99ec7bcb89 | -1.12565 | -53.62391 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44621d86-a72c-3073-a214-a940d4d6fd63 | -3.09516 | -54.02193 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8773d82a-522c-3039-9251-f8273a22f9aa | -3.0275 | -54.02475 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8de27463-cd26-349b-98c6-9f0d30908e33 | -2.61374 | -54.2126 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24e7dbb8-3304-315e-97cf-5d2ed7ff8e8c | -4.04494 | -48.33825 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05ce180b-291a-30fc-8671-12469c3d7c04 | -3.70112 | -47.13186 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e032855d-52ed-36de-9e50-6256ceaaf390 | -2.83721 | -49.88685 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ce24054-2441-3fb8-966f-25df44280335 | -4.58523 | -50.96396 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d763306c-d65b-3504-922d-4dc1f11742f4 | -3.30083 | -50.35715 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81abdbb6-6b6f-38fc-9990-1d9552e04a88 | -2.8705 | -49.08699 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05a89bff-475b-3b78-af0c-7fc0420813f9 | -3.38176 | -50.33741 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b6cac85-8d42-3709-a627-ef3f5e5ad2d0 | -2.27265 | -46.43186 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README36.md)
