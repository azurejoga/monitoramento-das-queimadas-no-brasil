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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc1dccf0-f9e0-38fd-be3a-4018337f8897 | -1.61051 | -52.40504 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97ac74df-2632-383d-b39e-ada475dc16b4 | -2.37656 | -53.83603 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cd62068-c1ee-3f9d-b832-1062ad1f196c | -2.22561 | -48.39826 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 926746de-c2dd-3f89-b314-f146bf4c8276 | -2.31641 | -50.69664 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e401ee7-ac43-31e9-9ab0-afcee5d3805a | -2.25588 | -48.38182 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eecd6258-670c-3a72-872e-e1ce1abe3d50 | -4.02583 | -46.54627 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 964a0bb1-1f77-3eef-ab4e-cfe031f3e627 | -3.77454 | -47.49298 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04d05dc0-174d-33b2-9425-efa2a5f50cf0 | -2.90662 | -47.89088 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f1ba52f-cfac-327c-8869-9e52f21a8bef | -2.64845 | -46.17445 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 928eed69-17cd-36e0-b623-0eec0895a37b | -2.12166 | -50.68585 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60f1fc31-d5d3-3fbd-9e8d-c1bbd7db55c3 | -3.76361 | -47.75516 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4d9ac15-8251-3014-a6b4-eb0582d7da5a | -2.24105 | -48.40767 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f275d62-c93b-3a0c-8f14-f50ddc6d4d51 | -1.40538 | -52.39211 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adbbf0dd-5b82-34b5-aa21-dcfe0fda9507 | -3.27664 | -50.57458 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f74cff4-878b-3fad-8060-dbed35047a1e | -2.93182 | -48.32146 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4d9efa1-d65b-34e2-abe7-4ddc655be71a | -2.16181 | -53.63243 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c839f90b-3007-3edf-8372-d5962e785634 | -2.38915 | -47.93901 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19e99aba-8065-3e52-88c4-5f752266fc1c | -3.94604 | -48.99447 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0e5fbf3-2540-30fc-b3bc-c2b6a7e3ede2 | -2.08742 | -47.73535 | 2024-11-14 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 5672a592-c8a3-3296-ab67-e6b81a1c6d57 | -1.95765 | -47.95748 | 2024-11-14 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4ed148b-b2fd-349f-a064-61c50f77972f | -3.81687 | -46.89967 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fa43cd7-426d-3a89-82ab-fc779c9755ba | -3.471 | -50.30747 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74bf8a4a-d34b-3425-8176-0bf2da4c3b9a | -3.10355 | -45.97019 | 2024-11-14 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f222d0e-b4be-3754-9ab7-b8f8ee820246 | -3.51513 | -45.52903 | 2024-11-14 04:40:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 437fadc2-bbf6-3b1c-943a-42fdb85c5e3c | -5.90802 | -49.32365 | 2024-11-14 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e80ff4e3-7404-361e-908c-eff89a46f432 | -3.81127 | -47.80242 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4b37021-efac-33fe-aa7d-859f97d54b49 | -3.23687 | -50.67262 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8e30814-9e7d-3f4a-b52c-b884acb98511 | -0.90061 | -51.73232 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b126f41c-7d88-370f-9535-7c92e9540d0a | -1.28443 | -52.47271 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16f41068-09ce-305b-a11c-01e53e7f1f45 | -2.13986 | -48.11998 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b9357a5-711b-3493-af34-5bf6bcf54a3d | -1.28897 | -52.47142 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc7e08f3-648d-385f-9102-8be0f83d4f05 | -2.11715 | -46.52468 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e52d669b-6023-3ac1-880f-356b7526822d | -2.17844 | -48.31005 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7911c894-3f84-3ef3-9202-aafa3d9c58f4 | -3.01936 | -47.97604 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6d67d50-5689-3633-88e6-1287939ab20e | -4.27638 | -48.2027 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28bd0f63-0906-3834-bbd6-f3b76bb5078d | -4.4332 | -49.68462 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63ba9b00-4bdd-3e3d-9c7c-dbf8cf8da7a8 | -1.38947 | -51.11624 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67eb48d5-6abd-35d9-a96f-730cec366718 | -5.85902 | -46.41982 | 2024-11-14 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d75ca0b-0135-395c-9e03-93e3347d5ac4 | -2.23123 | -48.42726 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b6b7396-d0bc-3ede-a490-2cad74d46c86 | -2.25764 | -50.84791 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 046aaea9-d512-34ab-b65e-921aec3efce8 | -2.58495 | -51.92108 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dcbb275-a0cd-342f-bd8b-c270e58fd2c5 | -2.63379 | -46.17624 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d63bd07e-ae99-3854-a1df-c77f20e20711 | -4.92515 | -45.71163 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b236dd0-c3cb-309e-b2d8-31ec053d1e80 | -2.34839 | -53.87883 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1d5259e-41b2-32e5-9c98-380d7ac0e129 | -7.1931 | -48.6007 | 2024-11-14 04:40:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e9ad259-36d8-3487-94fe-c1cbd72354e6 | -1.41136 | -52.38644 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6aad9894-58b3-3495-b528-f46d02e62b32 | -3.45941 | -49.19278 | 2024-11-14 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1182685-b1cd-399f-af27-0823f441bf59 | -3.23463 | -50.6648 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a4d9fa7-06bb-3eee-9b75-dbd929f8cd55 | -2.92387 | -48.06497 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f8a81c0-78b9-34c8-8c59-c551cd8ebf59 | -2.64906 | -46.17052 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e44ab0cd-3844-3760-a5ed-65eca85ae024 | -2.27122 | -49.15412 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e6033e7-9454-327c-ab2c-fadacc49c32c | -2.40604 | -48.50711 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d422f3ac-692a-3420-b74e-30c69eafb7b7 | -2.25526 | -48.73308 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd298b69-9915-394e-b08a-7e278f792f01 | -3.29324 | -50.22862 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 594fb709-0c59-3f15-a2ec-eca343b17769 | -4.42989 | -49.6841 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6a87ae6-62ad-3cd2-a618-21b13c7b730f | -2.65202 | -46.83355 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a24ba7bc-af1e-3a05-8de5-9f02ea48da72 | -1.34305 | -51.43003 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abdffc81-a65c-3665-a110-e07c215af2bf | -4.26325 | -47.0775 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 065e227a-33b4-30ef-be3d-e31b6c25885f | -4.26031 | -44.75101 | 2024-11-14 04:40:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f77bc5b-d236-30f4-a267-026a98a0b45f | -3.17328 | -45.43803 | 2024-11-14 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ce2f147-d3d4-3d90-b64b-0f08130459f6 | -0.9026 | -51.71968 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d6e7fef-7acc-38d7-a5d2-9e976edfe37d | -2.27404 | -45.34187 | 2024-11-14 04:40:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 477492f3-0056-341c-91c8-6e5e789931ae | -2.59809 | -47.02514 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9198d01-7a18-3401-8fea-196e20b384cc | -3.01959 | -48.04036 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d05fa11-2e30-3a93-8c36-d67c108327e8 | -4.16492 | -46.25377 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b05311a-b497-306b-85de-d320c7b5d9ee | -3.95042 | -48.98811 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 728b2d78-48f9-3124-adca-85f849ec3b41 | -3.24637 | -46.5277 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4004c67f-5802-3707-97b8-94182ddebce7 | -3.03296 | -48.06379 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2447444-e139-3b26-b9e4-8cce4aefcde3 | -5.08648 | -45.97987 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a600866-95d5-3e07-83af-7bc71893871e | -2.89028 | -51.69147 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a77f42a-c086-3cc7-a8f1-b1e3abd7d53c | -1.38391 | -51.5652 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6c25c26-3e53-379e-96b8-9b92fb903ba3 | -3.05487 | -45.52723 | 2024-11-14 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ed2cccc-827a-3953-9305-ba8398eaa85e | -2.20355 | -48.38783 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e98780bb-4153-39bf-9619-7419667f509a | -1.6694 | -52.5671 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d24f2169-7f2d-3cb1-a775-ef1244b74645 | -4.15071 | -46.25145 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 137285e7-71e8-3d49-8769-ab9908ac808e | -2.92279 | -48.07191 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| beb836c3-e045-35d1-8357-40d031e27492 | -2.23958 | -51.82004 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 943d66cc-a12e-3de6-85a9-7935c1442783 | -1.21162 | -51.7812 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13639640-803b-37fe-8949-809486e0deca | -1.46765 | -51.98808 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9285b9c-329e-3065-8862-6343c4faa3f0 | -3.92414 | -50.9891 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b22529ee-83d5-3222-a3ff-1cbabea84554 | -3.88886 | -46.09468 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 273eaaa2-b3e4-32b2-8292-61aa0bf68ef4 | -2.42298 | -46.27296 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b04194a7-dcd2-31de-af4e-5b16532aacf7 | -2.29698 | -49.11933 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85321074-dc15-33b6-bbad-7e55e07d3c30 | -1.93648 | -46.28398 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1b85a45-64ee-3a3c-a784-099d93eef1bc | -2.98507 | -45.86604 | 2024-11-14 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c9389f0-b4b6-3273-bc4f-ffa158fd6c5c | -3.03921 | -50.32747 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd6fc1e6-3836-309b-8913-4e280e392f35 | -2.95086 | -48.0228 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b14f04c9-ecd5-314c-be9c-330fb58c484f | -3.78151 | -41.59758 | 2024-11-14 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8925c287-49cd-35ca-9aee-0efaf165292b | -2.8851 | -51.79385 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1fe9b096-fa11-3143-9476-29a0436bf946 | -4.44802 | -45.365 | 2024-11-14 04:40:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b1fae8e-63f5-3cf7-81ad-818495851a25 | -2.21322 | -50.88342 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10a73c98-cefb-3095-b38b-eb32bfcbbbb8 | -2.61269 | -46.17302 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5177b148-108a-3c2f-8cea-a46f50dbeccb | -1.57136 | -52.01944 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c516587-9bfc-3342-9549-5b4db82525f0 | -4.26693 | -48.19766 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70d08032-a052-3960-b2e7-56092d8760b2 | -2.6406 | -46.81669 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 850b5413-83d4-38e0-bb37-5dd3a9dbf0d6 | -2.88574 | -46.8649 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 018e7116-41ea-3a4f-bd01-2105b1fbcadd | -2.07528 | -46.47983 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| efa6621f-d8c4-32a0-acfb-1bae32cecbdd | -3.99078 | -48.31213 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 861efe73-e46a-3de0-b770-d4cd499e1ea7 | -3.77116 | -47.49246 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b9868e1-42d4-3e79-a085-dfc19b3b08df | -2.116 | -46.5322 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README35.md)
