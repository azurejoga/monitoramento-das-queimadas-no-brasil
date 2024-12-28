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
| 87637a4f-a251-3772-bc84-77dde3929b18 | -5.49158 | -41.74238 | 2024-12-28 04:14:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bda104b5-1743-3673-8e2b-b594b56c12ef | -5.23389 | -41.39792 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 18b008bf-c768-3daa-a8b7-bc071b966146 | -3.96589 | -46.67092 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc4bcc31-12f6-394d-b65f-52f96e8928fa | -3.90793 | -46.91056 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1506552-ceec-3c1f-945a-24d656f84b21 | -3.99005 | -46.68855 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0d00633-58e3-3bd7-8820-e0688fa59cdf | -3.88362 | -47.01406 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ade5892b-b779-358b-be20-5d44f0776e8f | -4.5612 | -45.9862 | 2024-12-28 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3d01bcc3-e8cc-361b-bc70-79d2241b82a3 | -4.04436 | -46.71123 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf7fd831-bed7-32af-b62d-6ae6b011eb2b | -3.84622 | -46.68811 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4098c03-fc57-3b44-8523-7b4d41b851ea | -5.23838 | -41.39117 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 23548f6a-9dee-3c6d-ba58-4bf195a5e7ac | -2.12344 | -45.51354 | 2024-12-28 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6d7f023-6ba4-35a0-83aa-fe43b4c553b4 | -3.91176 | -46.91111 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4555496-bc4e-39db-92db-3f5c97666f5f | -4.03466 | -47.05835 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9241e401-e0fd-3aed-ba28-3273c2bb58e0 | -4.51782 | -46.02596 | 2024-12-28 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae6563d0-376c-3da4-80ef-f10a5759f268 | -1.36995 | -46.61074 | 2024-12-28 04:14:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cec37abc-d5d2-36a2-8cce-820c472f3c2d | -2.90136 | -54.48934 | 2024-12-28 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d66aa78a-a4f2-3b37-abaf-c1a4dc994cf6 | -3.84378 | -46.68111 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d58c3904-a127-3583-a4e2-1d8ad9deb970 | -4.012 | -46.72018 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9256174b-cc7d-313f-b9c3-31dd2259d6c1 | -2.9005 | -54.49434 | 2024-12-28 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 464fe153-d8f7-344f-8893-7bf82efc0a67 | -3.86491 | -46.6702 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbaee8da-8f4b-3a29-8c7b-0b0d46e4c4ae | -1.82232 | -45.63828 | 2024-12-28 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 181536d8-4562-38b5-9d09-e697ffc274d2 | -5.52171 | -41.73949 | 2024-12-28 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 37e3ae99-69df-3026-857d-6b052770c4b5 | -6.39055 | -39.397 | 2024-12-28 04:14:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0128c579-bea4-3781-9214-ad753a8bca8c | -5.58011 | -46.14269 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b36a1741-0afd-339a-a8ee-60bc98367d59 | -2.16992 | -45.40621 | 2024-12-28 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7efafa00-9222-3f8c-b559-29dcdae5ea3e | -3.89761 | -47.01453 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8de02435-2fa9-358f-be09-a868840c5a3b | -3.81806 | -46.05769 | 2024-12-28 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 97c0fd89-e8b1-3dd5-80be-cc922847387e | -4.08786 | -47.09591 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e7015459-ca9a-354e-888f-5221fd4233a9 | -3.84316 | -46.68299 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd01cab5-d897-3665-8c1e-516d4d6e69b4 | -4.08399 | -47.09541 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e73b4dd5-2ebf-3799-bc86-1d2cdb2facd8 | -5.923 | -45.99891 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc0a607d-ad09-35dc-9c9d-6e881e956a18 | -5.57255 | -46.12976 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3a16991-2ff8-3eaf-9b0c-f5ca3534e66a | -4.0497 | -46.72637 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef394c36-88c6-3e0b-8e46-80c2b9299952 | -5.31747 | -46.06561 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1013bc4a-5fef-303e-bc4b-6a78c4a4a977 | -1.93042 | -46.43222 | 2024-12-28 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1fe4d7f-4d68-322b-b881-626037176e56 | -3.94852 | -49.44179 | 2024-12-28 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7ca4468-07f5-37fc-8f67-eba5a19a0960 | -4.02577 | -47.18587 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3e014dc-7d14-3143-9273-fcb3b1a4898d | -2.52432 | -44.9989 | 2024-12-28 04:14:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 74883533-7152-3f93-8e5d-51803ff817cc | -3.97607 | -46.55317 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e34b1a0e-cb7c-33f6-ad31-502e37a33f7e | -3.89364 | -47.00068 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdeb39bb-07e9-3034-b705-f2391d955615 | -3.53367 | -40.9257 | 2024-12-28 04:14:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 801c589c-6467-370e-8f57-e299d2642d2f | -2.44268 | -46.02639 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7adfc70-6c03-3427-993b-52de6d25c60e | -2.29102 | -45.57124 | 2024-12-28 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17f191f4-70da-3288-877e-d5b966f5f9e4 | -4.25985 | -46.36671 | 2024-12-28 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f94c78af-edac-3d72-a283-4018dc453e07 | -2.55398 | -46.87844 | 2024-12-28 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cea9c56-5292-34be-8bca-08e284859aeb | -5.31389 | -46.06503 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a2cc24c-fefd-3722-a109-1c8b7f07db74 | -4.1174 | -46.71662 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7377379f-69d0-39d9-b23d-422fe5e0896a | -2.48846 | -54.17327 | 2024-12-28 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0df4f1f0-5768-3171-904f-10885f77b224 | -6.7175 | -44.15424 | 2024-12-28 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6a0dd14-d9cb-39fe-ba85-a9cb18e10d5b | -4.0393 | -47.05412 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 07111e31-8e8c-32e6-b1c6-12beeb8cc802 | -2.52837 | -46.86427 | 2024-12-28 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bae1449f-f6f1-3e70-a9e7-533154275005 | -5.23672 | -41.40205 | 2024-12-28 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5d6ab500-f69b-332a-aeaf-0b18cf1eaa1f | -3.98513 | -46.91161 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0394ef61-89f8-3524-8ed7-fe4b31d1fc01 | -3.92696 | -46.97983 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0bd78cb-6c3e-374f-8bf4-fdb01a84bf83 | -4.06554 | -46.98957 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9465025-06a8-3e8e-ab84-dfc688a36ee8 | -4.12633 | -46.6851 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e482f850-a8f3-309f-af64-de5210a6b028 | -5.81904 | -42.80982 | 2024-12-28 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 752134cf-ff19-3b33-8c63-fc16c0986017 | -3.98021 | -46.67779 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68ba5828-e0ec-39e9-99c4-de69e311570a | -6.19995 | -41.57004 | 2024-12-28 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1fbb54ad-1ccf-39b3-9719-bf4d7133cce9 | -3.90637 | -46.89574 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff1c2113-9352-3a29-8f92-5620e81822ec | -4.0316 | -47.05293 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edc3b1e1-3ed7-3fc3-bfbb-664d0c95c6a7 | -2.48569 | -54.17086 | 2024-12-28 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 886038ac-12cc-34f1-8a35-6fad7708e212 | -3.77428 | -46.60672 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97391aaa-6f24-3688-af68-c8d917e4ad73 | -2.38771 | -51.91339 | 2024-12-28 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2152aefd-38c8-39d8-85a3-c93b16e5860c | -5.24522 | -41.41438 | 2024-12-28 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 31d9e492-ffb1-385a-9e45-6baa305f24b3 | -3.88582 | -46.95086 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b14256e9-6b2e-35ee-809b-e5493ff5c19e | -7.17571 | -44.99257 | 2024-12-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bedd0d7-7923-3039-abe0-73a21a1b1a91 | -6.76508 | -39.40839 | 2024-12-28 04:14:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0aa23cb1-f715-3a30-a0d1-d8a388ac3967 | -5.83728 | -44.01788 | 2024-12-28 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c060395-d21c-3989-b17b-d1a617a3957d | -3.75826 | -47.22333 | 2024-12-28 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 131f71b0-a776-3142-a40f-f23bac0dc25c | -3.89285 | -47.0056 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a1c3b39-2652-3274-b5bb-0a06f0528d13 | -1.81272 | -45.58031 | 2024-12-28 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5a14a7a-c14b-3c10-98f1-7bbaf4989d08 | -3.56269 | -53.10236 | 2024-12-28 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf758f6-7a50-30e8-9873-02f2c4dca8d5 | -5.0722 | -37.71569 | 2024-12-28 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a0504b97-7560-30f6-b1a9-54210957516d | -3.94401 | -46.75696 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 82e82c99-5d55-3742-a1c7-fb4942dfec46 | -3.90645 | -46.91987 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5f51721-a9ec-37eb-bfd1-2d3055294226 | -3.95765 | -46.76851 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b14e917d-c499-3813-855a-4f83e6e590ff | -3.89681 | -47.01935 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf251953-b254-3bd4-abef-c30f59f60d01 | -2.62807 | -48.08673 | 2024-12-28 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d8961c2b-201f-3024-bebb-4a15a14a3fa9 | -3.85592 | -46.67564 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d2aa147-a68b-3fa0-84d4-7a4248a26c2c | -4.56591 | -44.12051 | 2024-12-28 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 214e0638-d858-3dac-8f31-9219c9bd6843 | -4.0142 | -46.70648 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1929f9e1-13ce-3f80-acae-2cf1263c6947 | -3.97495 | -46.68636 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8dd32da3-5b8f-3517-b987-40e815260e72 | -3.91682 | -46.65977 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e298fce-743f-34a9-9372-f5b7e9a3d290 | -4.0091 | -46.57116 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89ddf834-044d-3ec6-b3a7-9599d4d535ce | -3.89826 | -47.02126 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58e8f6d3-54fe-3865-b2c7-e94e15558701 | -6.44679 | -44.38127 | 2024-12-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc556064-ddec-39e6-84d0-7494c1b2fe76 | -3.86038 | -46.67425 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78815c08-8ed1-37ed-acfd-b15a867b0434 | -4.11813 | -46.71211 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ff1319f3-f80a-35e3-a15f-f12861187bb8 | -3.89442 | -46.99572 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e48e8b39-e739-3f14-8aa7-3ccf831eeb35 | -4.04235 | -47.0596 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 257b5684-2b1c-35f9-9191-27031c6d5bb5 | -3.84101 | -46.69661 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d35c9919-e941-3ae4-9852-5c91a0a5b913 | -4.1158 | -46.67872 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 52ce9bb6-408a-31e1-9713-18950072d5da | -5.57007 | -46.3629 | 2024-12-28 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9075198-6bd1-3779-8153-4637ef9a6460 | -4.00142 | -46.71381 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d73a4e32-00b0-3bce-83be-88f080637acd | -3.56311 | -40.84806 | 2024-12-28 04:14:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4c6cd7ef-f484-3f7c-8858-b729f1e3e7ad | -3.90944 | -46.90105 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b0716c8a-21c8-38ac-b512-6ebb4a16b407 | -2.55009 | -46.87784 | 2024-12-28 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ae08327-d5e3-3b2b-aefd-d4568b5acb73 | -5.59105 | -39.53547 | 2024-12-28 04:14:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6ac37786-4621-3f22-8b31-e1e5fb184a20 | -4.6416 | -43.96185 | 2024-12-28 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README8.md)
