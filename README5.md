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
| 891b3394-64b1-3257-8c8c-b2481f81fdf8 | -4.3605 | -46.804699 | 2024-10-17 00:21:37 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d352d5c4-6661-3865-8756-e9cb70bfa7c1 | -4.3621 | -46.811699 | 2024-10-17 00:21:37 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fcf32754-5946-354d-87bb-395afbff2c32 | -4.3636 | -46.818802 | 2024-10-17 00:21:37 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8151c3cc-37c4-3b11-be44-75e2877d5966 | -3.5217 | -43.230202 | 2024-10-17 00:21:38 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 376e2613-1c70-33d5-b343-f001c034fa62 | -3.5119 | -43.232399 | 2024-10-17 00:21:38 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29eff761-63b0-34ae-88e8-ae59cec230e8 | -4.5769 | -48.008301 | 2024-10-17 00:21:38 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0f218d7-ec33-36c4-9971-2f28bced9895 | -4.5786 | -48.016102 | 2024-10-17 00:21:38 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16594c55-416f-3b99-a879-c7f0dce858f0 | -4.5804 | -48.023899 | 2024-10-17 00:21:38 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f26cd651-2ab8-3939-8b8a-470f5e4d7d49 | -4.3523 | -46.8139 | 2024-10-17 00:21:38 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6b74ad1-d5e6-3843-bc82-997efaac3f56 | -4.947 | -49.922401 | 2024-10-17 00:21:39 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 469e4ca6-a1e9-3ce3-ae27-07172947dfad | -4.4668 | -48.114498 | 2024-10-17 00:21:40 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6687f7c4-f5d8-36c6-b4f3-5bba65676982 | -4.3236 | -47.701302 | 2024-10-17 00:21:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94b60728-9c77-3aba-be7b-11f61dbb9414 | -4.3253 | -47.708801 | 2024-10-17 00:21:41 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2efb1eb5-2347-3783-b538-e4dbc1d3dabd | -4.9901 | -50.871201 | 2024-10-17 00:21:42 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61800ebf-cb75-3051-88ad-58ec20b18fc0 | -4.5132 | -48.788799 | 2024-10-17 00:21:42 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 730ba053-2cf6-3f0c-b3c5-ed7867677762 | -3.6061 | -44.780102 | 2024-10-17 00:21:42 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58d13908-c58c-3f65-bda2-b3dc87314a18 | -3.6077 | -44.786999 | 2024-10-17 00:21:42 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc1933f-362e-3528-b2f5-6e7bfb810118 | -4.5016 | -48.782501 | 2024-10-17 00:21:42 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d1f936a-3094-3e41-ab76-100c2fffbcd7 | -4.5034 | -48.790901 | 2024-10-17 00:21:42 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e66028b0-6f07-3fe2-a4fc-b0a3a56f9ca4 | -4.2671 | -48.002499 | 2024-10-17 00:21:43 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 746d7d34-f430-34eb-82a4-89b82a774347 | -3.9574 | -46.430099 | 2024-10-17 00:21:43 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bed0a063-22ad-3e18-9020-bf5991a189c1 | -3.93 | -46.3997 | 2024-10-17 00:21:43 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dddae2c7-9d28-37ad-b1c1-7ab7f7418381 | -3.9315 | -46.406601 | 2024-10-17 00:21:43 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76d0b425-37be-3b37-9549-da9b32c01a65 | -4.2654 | -47.994701 | 2024-10-17 00:21:43 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67546d62-7371-335c-9675-449f0a43d19c | -4.2214 | -47.843102 | 2024-10-17 00:21:43 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0243c9a-4acc-32c4-bc1d-2500e988f8c0 | -4.3316 | -48.617599 | 2024-10-17 00:21:44 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99adf93e-01ca-33e3-8b37-93c83bb88508 | -4.3218 | -48.619701 | 2024-10-17 00:21:45 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 875284a6-009f-39f8-aa08-17c5c2573362 | -3.7047 | -45.9011 | 2024-10-17 00:21:45 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d649fee1-3cd4-36af-8acc-b5dc88587c01 | -3.7062 | -45.908001 | 2024-10-17 00:21:45 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b7fee4d-f97c-3331-a041-aaf8454fe740 | -3.6933 | -45.8964 | 2024-10-17 00:21:45 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b795bef1-e6d4-3499-b956-15fb4d7993a5 | -3.6949 | -45.903301 | 2024-10-17 00:21:45 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78a1da61-5beb-3e00-b5a7-cd42c25220b5 | -3.6964 | -45.910099 | 2024-10-17 00:21:45 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d289343f-4650-32ce-bc20-e13dfe205f6c | -3.698 | -45.916901 | 2024-10-17 00:21:45 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 886b9b78-4c8b-3e04-aa84-db8d89d44753 | -4.2887 | -48.609699 | 2024-10-17 00:21:45 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 076e50a3-e223-3da2-9847-997748d105e7 | -4.2905 | -48.617901 | 2024-10-17 00:21:45 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad1d6ae0-832a-3b1c-9bbf-79e44fa1d1dd | -4.2269 | -48.562599 | 2024-10-17 00:21:46 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c63df2d1-061c-35c2-aaa4-cae2af3d0101 | -3.5946 | -45.961399 | 2024-10-17 00:21:47 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dec272bb-85d1-329b-ba9a-45f7d17a149d | -3.5961 | -45.9683 | 2024-10-17 00:21:47 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff26cc3c-8dff-3061-8a07-d47df4b196e9 | -4.1942 | -49.390099 | 2024-10-17 00:21:49 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6cb43f1-b418-347e-8484-e1b8bb52b91a | -3.2924 | -45.3979 | 2024-10-17 00:21:50 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e14e788-d83a-3035-bfe6-574c068f1716 | -3.7954 | -47.7775 | 2024-10-17 00:21:50 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d2cc661-5c83-33b2-8894-6e3afd3a126c | -3.7971 | -47.785 | 2024-10-17 00:21:50 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70b2d735-31e5-38bb-9065-056f94984402 | -3.9174 | -48.325699 | 2024-10-17 00:21:50 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 235bb061-19df-391f-a4ae-e84fe6f5e904 | -3.9192 | -48.333599 | 2024-10-17 00:21:50 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f7447a3-ff24-3c56-ad98-4de84e6bb42c | -3.9209 | -48.341599 | 2024-10-17 00:21:50 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec0804c0-e3d0-3e32-ba10-efcca89c9df0 | -3.9227 | -48.349499 | 2024-10-17 00:21:50 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e1e3083-0290-356e-96fc-4bad0375e63e | -3.9147 | -48.3596 | 2024-10-17 00:21:50 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b212bfbb-f9e1-3b29-b559-40716535bf8d | -3.896 | -48.321999 | 2024-10-17 00:21:50 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2ebe7e-8931-3628-9dc5-f2845db62320 | -3.9031 | -48.353802 | 2024-10-17 00:21:50 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09f16596-11ce-3555-9022-15ef70c5baaf | -3.9049 | -48.361698 | 2024-10-17 00:21:50 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc4858b3-839f-383b-8f0b-688e5a80a4a1 | -3.8978 | -48.329899 | 2024-10-17 00:21:50 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42a4c358-a44a-387d-b555-e61d81a04284 | -3.8996 | -48.337898 | 2024-10-17 00:21:50 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7fdd953-1b11-3cd2-baa4-9126ead65b38 | -3.2908 | -45.391102 | 2024-10-17 00:21:50 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fdc4c5c5-7bd0-35b4-8efb-98b9011df1c6 | -3.8933 | -48.3559 | 2024-10-17 00:21:51 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5385647f-dd5d-37d5-a4d4-0b325ca364a9 | -3.6966 | -47.611198 | 2024-10-17 00:21:51 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94bd2d60-d0a6-39a7-ae0b-b36e879189eb | -3.6982 | -47.618599 | 2024-10-17 00:21:51 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c1b9180-1ece-30fa-b9eb-27666909a0e7 | -3.0747 | -45.9403 | 2024-10-17 00:21:55 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6817b062-ca44-3428-8838-202210d692e8 | -3.0763 | -45.947201 | 2024-10-17 00:21:55 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 855fce3a-8cd8-307b-b492-803a7c434689 | -3.4612 | -47.662899 | 2024-10-17 00:21:55 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab5fa95-4f87-3e1b-ab42-71b08e5560d3 | -3.4628 | -47.6703 | 2024-10-17 00:21:55 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b0f8a22-61c1-38b9-a20c-19cf25622bac | -3.7368 | -48.993401 | 2024-10-17 00:21:55 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d37f5da0-7f23-3436-af53-356d52aa2c11 | -4.0291 | -50.363602 | 2024-10-17 00:21:56 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19728f26-24f5-3767-8cd8-667b475c7f07 | -4.0907 | -50.737598 | 2024-10-17 00:21:56 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29f658f1-11f8-325e-96f0-c418364f580e | -4.0931 | -50.748402 | 2024-10-17 00:21:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9429eabe-11f5-3641-b368-72ea1e336964 | -4.0955 | -50.7593 | 2024-10-17 00:21:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6d70f3-d6e5-31f1-a64d-5d39375a52c0 | -2.8653 | -45.5144 | 2024-10-17 00:21:57 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76ef98d4-b4d8-3d39-a90c-f2dd1b6750e7 | -4.0759 | -51.0434 | 2024-10-17 00:21:57 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d95d152-0d01-3820-8c08-87f8659ca9cd | -3.8831 | -51.1446 | 2024-10-17 00:22:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb8be96d-b0ea-388e-a7a5-127be324dfed | -3.6506 | -50.1814 | 2024-10-17 00:22:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8167155e-cdd9-3eca-9fd9-d36218426461 | -3.6408 | -50.183498 | 2024-10-17 00:22:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09bc6cd3-6db0-3a5e-bbe6-fb27569da16e | -3.6527 | -50.191299 | 2024-10-17 00:22:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fcf7ed4-876b-3448-8b76-cf72f870a756 | -2.6543 | -46.040699 | 2024-10-17 00:22:02 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fe32dd53-ab5a-362f-9c49-8cae4e086458 | -2.6558 | -46.047501 | 2024-10-17 00:22:02 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 07bc95ae-bf83-351b-b19b-81f496a73a42 | -3.785 | -51.117802 | 2024-10-17 00:22:02 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62eec6e1-5c3c-3403-a5f6-e392a1bb58f5 | -3.1638 | -48.3582 | 2024-10-17 00:22:02 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e39db9b-85d3-378e-87be-8540b7a790dd | -3.1655 | -48.366001 | 2024-10-17 00:22:02 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57746a04-f6ef-3e75-8acf-143698f5f27e | -3.7984 | -51.271801 | 2024-10-17 00:22:03 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a277a5-a147-3efa-9650-681eefc27f29 | -3.8009 | -51.283401 | 2024-10-17 00:22:03 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4229fe5e-7677-3af3-be65-83c5678f86de | -3.8035 | -51.295101 | 2024-10-17 00:22:03 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8164a7b-4890-3742-b8d3-6abe1dcf5d10 | -3.7721 | -51.338699 | 2024-10-17 00:22:03 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03fbd373-582e-3be4-b87f-f51784aca294 | -3.6968 | -51.042099 | 2024-10-17 00:22:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dfd2012-698e-385f-82af-847f60262fa2 | -3.6992 | -51.053398 | 2024-10-17 00:22:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21da1ec2-452b-3a57-9477-0e95a6ef3b8c | -3.2135 | -48.9048 | 2024-10-17 00:22:04 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfbeebbc-5aa4-3583-85fe-f2405c43f8ab | -3.2154 | -48.913101 | 2024-10-17 00:22:04 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9911f491-5aec-3880-9da5-fe5a96f304bf | -3.2172 | -48.921398 | 2024-10-17 00:22:04 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b945280-4ba3-3518-bf5b-f4a8ac739115 | -2.321 | -45.066399 | 2024-10-17 00:22:04 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8abfcc89-4041-357c-a6ad-1e0a2c87cd18 | -2.3226 | -45.073299 | 2024-10-17 00:22:04 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20be03e1-20ad-3114-b3bc-424705618d5b | -2.3112 | -45.0686 | 2024-10-17 00:22:04 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e271a870-f8c3-39cd-a303-c93ee27216db | -2.9668 | -47.982899 | 2024-10-17 00:22:04 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5b5b27-b3d4-3efd-9ee0-bb65f2961292 | -2.9684 | -47.990398 | 2024-10-17 00:22:04 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6259b394-b9e3-3a17-8c39-e2916c43e18c | -2.9701 | -47.998001 | 2024-10-17 00:22:04 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e4ce7ed-a941-3a19-8ad9-51cdce71e22f | -2.9718 | -48.005501 | 2024-10-17 00:22:04 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de46a95e-93e6-36fb-94c2-10d70b2237e0 | -2.9603 | -48.000099 | 2024-10-17 00:22:04 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74d41be6-c76b-3371-aebc-55d73b00e67a | -2.962 | -48.007599 | 2024-10-17 00:22:04 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2341e002-50a1-3f26-9c1f-ac7145f44c93 | -3.8293 | -51.879002 | 2024-10-17 00:22:04 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a57e130f-e1f6-38ff-800f-2e2f0bfee4a5 | -3.8321 | -51.8918 | 2024-10-17 00:22:04 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78747e54-ad22-3bab-8a2c-247a6aa4ec6e | -2.957 | -47.985001 | 2024-10-17 00:22:04 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad532f49-484a-3aaf-af3f-b68851bc5733 | -2.9586 | -47.992599 | 2024-10-17 00:22:04 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e7784c8-fed7-3f0c-ab7b-8d90b8559c0f | -3.594 | -50.994202 | 2024-10-17 00:22:05 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cdce0c5-c286-302b-ba3d-713ce715d704 | -3.5012 | -51.084301 | 2024-10-17 00:22:07 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
