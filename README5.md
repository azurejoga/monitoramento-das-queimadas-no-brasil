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
| ab17fde9-0904-3cc2-8150-a0d68ae6eef7 | -9.0158 | -60.5138 | 2026-08-19 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 78c0c2b6-09ac-39d7-b2df-106a0c959be5 | -7.5301 | -55.5839 | 2026-08-19 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 118d82c0-7a7a-3faf-b76a-54d71d7dc264 | -6.0913 | -57.8992 | 2026-08-19 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| bba1b900-a571-3482-89ae-8b63b3f5a7da | -9.4058 | -60.5904 | 2026-08-19 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a113e716-de1e-34be-8eb7-54ce44cdaaa4 | -6.0178 | -57.8631 | 2026-08-19 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| b2eae66f-db6c-38bb-8212-8528ff258cfd | -19.7442 | -57.9425 | 2026-08-19 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 234.1 |
| 2ead54a1-d4a3-3c2a-882f-5ba7b9c0e2ea | -6.8778 | -59.031 | 2026-08-19 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 19349c33-32fa-3043-8ba7-00923954430e | -9.3875 | -60.5528 | 2026-08-19 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 136.4 |
| d99b4e2b-0481-35ba-8117-cf47a4ddaeb8 | -7.0577 | -59.8331 | 2026-08-19 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| eb79f6ae-d315-34fb-87cf-bd6de71916cc | -5.9011 | -43.6279 | 2026-08-19 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 8bb0cc6e-3057-3657-91cb-f03abc89fe83 | -9.4256 | -60.4353 | 2026-08-19 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| d3e230cb-9263-360b-abcb-1961f6d6d6f3 | -9.0865 | -50.7979 | 2026-08-19 00:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| b35b30bc-d921-31dc-934b-ec6807a59360 | -7.5487 | -55.5829 | 2026-08-19 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| bc08bdbe-1ae2-357b-beee-26716adbbb0c | -4.70951 | -47.15215 | 2026-08-19 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a0061182-5af8-3463-8352-adf8158a32e6 | -4.00784 | -48.05593 | 2026-08-19 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c949ff3c-f223-3b81-8df7-9136e22f8d6b | -3.69224 | -47.65396 | 2026-08-19 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9a1fb5ca-081e-3d8d-9f62-1dda7715bd97 | -3.01339 | -51.05925 | 2026-08-19 00:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 44dbfc97-a20d-3a68-b12f-6b9e0b59bd09 | -3.27042 | -49.51979 | 2026-08-19 00:11:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| cce26fcb-4a0d-3bac-bcd4-07581000ac34 | -4.71435 | -47.15902 | 2026-08-19 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| d405c0a2-9698-3ba1-9763-00fce3965527 | -4.71143 | -47.16575 | 2026-08-19 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| b63d9290-932a-3029-a9ca-d03048116dd9 | -5.99314 | -57.865 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| a82a4bfd-552d-3899-a832-c01c86ecd143 | -3.28223 | -49.46664 | 2026-08-19 00:11:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7aae6c09-1608-34be-83a4-9e26d93235e4 | -3.9356 | -50.99532 | 2026-08-19 00:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3c45f973-42b8-311e-b30a-faadaa0e18db | -3.42734 | -51.51618 | 2026-08-19 00:11:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 96fce080-ff74-31f1-b348-b55a5c824692 | -5.99532 | -57.87139 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 0e1220ca-ef9e-31d5-8f07-4b383968ebb3 | -6.1187 | -57.71893 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| ddcf63cc-1ccb-3671-a18b-557664fac818 | -4.17552 | -49.40112 | 2026-08-19 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| dc258cb8-840f-3c9e-90c7-d55ffcd74f2d | -4.46514 | -55.46033 | 2026-08-19 00:11:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a4ba3213-0868-3d48-815d-ebf7d5311383 | -3.67499 | -47.64963 | 2026-08-19 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| f0f4cb7d-a851-3c41-93cf-aa6c20e27e05 | -5.50165 | -60.13523 | 2026-08-19 00:11:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| e74543b4-9d64-35bd-9901-ed5c0e2c2920 | -4.00952 | -48.06792 | 2026-08-19 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 38849ce0-2fce-3553-9911-4630d310e790 | -6.09297 | -57.91587 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| a523292c-576e-3d6b-b96a-7db0fcb3a1d3 | -2.82329 | -52.29172 | 2026-08-19 00:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2f03a9c1-2687-33a3-a04b-fef87026d06d | 2.48467 | -50.96982 | 2026-08-19 00:11:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 97d6e502-fe00-39c5-b9ab-07a8e97f5667 | -6.00362 | -57.84278 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| ec4b61f8-1dc2-31a6-ac2f-bc284368d4ce | -6.13999 | -57.88348 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 0ca253f5-f4de-3036-a707-cd21c226fbaa | -3.68168 | -47.65559 | 2026-08-19 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 303b3477-99f8-3f6e-af47-e65977536c1c | -3.67681 | -47.66269 | 2026-08-19 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| b1eb00bb-182d-38e9-b95d-fd0c97193447 | -4.45467 | -55.46184 | 2026-08-19 00:11:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 732db0ae-7747-308b-a005-79e37d38b123 | -3.51762 | -44.23355 | 2026-08-19 00:11:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 80a2f6a8-f88b-3546-9565-9f0d812baff5 | -5.99256 | -57.85067 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| d4c5a626-a6f4-3a9b-b8f4-08d68c6c7d58 | -6.0901 | -57.91096 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 191.5 |
| e135f631-a54c-384a-a561-ed6943702282 | -6.13727 | -57.86248 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 7bd0f580-5da5-3d40-aa0e-5d10c58ffd28 | -2.77021 | -48.57279 | 2026-08-19 00:11:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 6d61ebff-b06c-3821-be81-481fdd469815 | -6.0798 | -57.91737 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 0f17219a-ebd0-35c0-b99d-9c1fa291bc9d | -3.27181 | -49.52977 | 2026-08-19 00:11:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 01197cfb-8116-38df-b9ab-76cb924f6dfe | -6.01669 | -57.84122 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| d67ed207-9a1a-3e88-9432-a56ca71e14f9 | -6.03746 | -57.79677 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 5fa495c3-a474-39c0-a154-33589ce6dd17 | -3.66412 | -48.9682 | 2026-08-19 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f258419b-e6d5-3a7c-b001-15d325fed516 | -6.09273 | -57.93204 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| cb917d22-36a8-3932-a6ff-9563ee9eeb3c | -6.00623 | -57.86341 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 280.8 |
| 8a3ed225-4416-370d-9db8-7be59596800e | -2.08151 | -56.59044 | 2026-08-19 00:11:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 10224ed0-52ee-3884-867e-7ba20b96ecf4 | -3.52259 | -44.22634 | 2026-08-19 00:11:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| f6501164-ffeb-3c96-8a11-f38078694891 | -6.098 | -57.86763 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ab4573aa-14b8-3af1-a427-6bb1c64f72d6 | -2.8245 | -52.30051 | 2026-08-19 00:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b37f3892-aed4-3fad-937f-b43e6c7307c9 | -6.04013 | -57.81736 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| fe010cd2-2b8d-37b8-af05-70d948d50672 | -4.00699 | -48.06223 | 2026-08-19 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 6a6adda3-9bef-347b-8970-8f203aa4828a | -6.00883 | -57.88406 | 2026-08-19 00:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 4fdf7930-9427-3698-b613-6471b9c8ed83 | -8.57 | -54.73 | 2026-08-19 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db5267d1-1b55-3cd4-b2ce-65400156ea9b | -19.74 | -57.96 | 2026-08-19 00:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 84c90d26-ed08-3251-94a1-cff9c8b06c02 | -8.55 | -54.78 | 2026-08-19 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aabc34aa-921d-3d21-a6d3-ab65e8010b2a | -8.54 | -54.72 | 2026-08-19 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec7d3e97-bfed-31f5-b4ce-ab47a8742507 | -8.58 | -54.79 | 2026-08-19 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8ddb0dd-bfa9-3eab-8025-a00bc6e40453 | -5.9995 | -57.8444 | 2026-08-19 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8e9a001b-baef-3ae0-8d02-83d84f52ff6f | -6.0913 | -57.8992 | 2026-08-19 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d35ded5b-a3c5-3fed-ba36-36a6c8fa7475 | -6.8593 | -59.0318 | 2026-08-19 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ee85e8a0-0389-395c-afcf-21b39258f975 | -6.6938 | -58.942 | 2026-08-19 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.2 |
| f80e79cc-3ca3-352b-88be-ce3195ba89ea | -9.4257 | -60.416 | 2026-08-19 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 1af010a8-6b4a-35be-a6cf-a6e793b69da1 | -7.5488 | -55.5629 | 2026-08-19 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ad220edb-5d9b-34df-84bc-755761134a74 | -8.503 | -54.8625 | 2026-08-19 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5acd7af1-c0fd-3924-a68e-3a073d1f6b4d | -9.0801 | -65.3976 | 2026-08-19 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6fc00bbd-c5d9-3de5-a52d-7b1c50b5774d | -9.0158 | -60.5138 | 2026-08-19 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 3a97bd3b-86d5-34c5-b2b5-b3b8bb158386 | -6.6937 | -58.9613 | 2026-08-19 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6678528a-7573-3640-9c4d-5d590107eb44 | -6.3496 | -54.9068 | 2026-08-19 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 0c43383c-daac-3d95-a6a0-b1c4c0e72c02 | -9.406 | -60.5711 | 2026-08-19 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 4fdb9259-1371-36c6-b034-cf14df8336c7 | -7.5301 | -55.5839 | 2026-08-19 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 7678bc8d-96a6-3097-a4c1-2bf4c5383080 | -6.8961 | -59.0496 | 2026-08-19 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9865a697-1995-3253-bd13-a0e4f2c6a764 | -9.0868 | -50.7768 | 2026-08-19 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 5583565e-8e2c-38ea-8ef5-ad0835271ebe | -9.08 | -65.4163 | 2026-08-19 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2e3ad4bc-ec8d-396c-90ff-16be40af3fd9 | -6.7123 | -58.9412 | 2026-08-19 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| e85b0e11-58fe-3305-97d1-235365895594 | -5.92 | -43.6032 | 2026-08-19 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 635b846b-9ebf-38e4-8585-866843f830f2 | -7.0577 | -59.8331 | 2026-08-19 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| eaa68ac5-6ad2-3834-9ec8-9cecf1b5cbcf | -19.7438 | -57.9633 | 2026-08-19 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.4 |
| d2d61f1b-1039-30d9-a64d-f1f7e82fabf9 | -14.4934 | -45.6647 | 2026-08-19 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 527e6be5-2169-32b2-b339-595e6440d367 | -9.4061 | -60.5518 | 2026-08-19 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| bea51346-e4ab-37d3-af5d-3c847e79fe6d | -9.3875 | -60.5528 | 2026-08-19 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| ac581d63-693e-3b19-b0bd-6abbd6afc1a9 | -5.9198 | -43.6264 | 2026-08-19 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 160.4 |
| c501084b-e52f-37e2-807c-151429611c05 | -8.5792 | -54.6758 | 2026-08-19 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| af1c156e-0e3c-374a-b972-145a3af917d7 | -9.3873 | -60.5721 | 2026-08-19 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 8d513dea-4b21-3825-94ce-bc46f740f72e | -6.0178 | -57.8631 | 2026-08-19 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 618d0d96-d638-35de-9604-e061591b06eb | -7.5487 | -55.5829 | 2026-08-19 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 3d3dd2a7-8147-3fbb-afb1-2a3a2f8cc00c | -14.4554 | -45.6251 | 2026-08-19 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| dc3cfbc0-26a2-3cf3-9e78-c67f2db962e8 | -6.8777 | -59.0504 | 2026-08-19 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a22a9656-7e2e-3d26-8cfb-b5f567c819fa | -6.0179 | -57.8437 | 2026-08-19 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 84bd08c3-84a6-3a0f-a85e-2c4c00429922 | -5.9011 | -43.6279 | 2026-08-19 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 83bb52a9-8342-3e65-90e9-4e0abf2abdf0 | -9.4254 | -60.4545 | 2026-08-19 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| f857fe10-8539-3ad1-9beb-9c94b3f303b6 | -9.4058 | -60.5904 | 2026-08-19 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d5d7b925-cd1a-38e4-afd5-4d36149c7f07 | -6.8778 | -59.031 | 2026-08-19 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| e70e6f29-cb72-3ee6-acee-213e4c4065a8 | -9.0865 | -50.7979 | 2026-08-19 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 075ef3db-f80d-3cc3-8c3e-5dfd955cae2a | -6.8962 | -59.0303 | 2026-08-19 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |


[Clique aqui para ver as próximas entradas](README6.md)
