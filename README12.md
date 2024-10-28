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
| 1c9a5ff2-d28b-3e0c-87a1-b86905eb85b6 | -3.85641 | -51.7008 | 2024-10-28 00:50:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f4d92116-2c2c-367a-ba38-6159fe3b6f28 | -3.8557 | -45.72923 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f24657f7-2a59-3432-98fc-877242ff0f96 | -3.84651 | -45.73054 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d0298a78-e44b-3524-a81e-5d86ce8755bb | -3.84517 | -45.72099 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f579212f-4181-38be-9e50-3df8492f9fe3 | -3.83188 | -46.47741 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| adf4ab5c-818b-37c5-99ec-68be66cac736 | -3.82294 | -46.47869 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| abf08bcb-6b72-39e5-b668-92cb801d86f8 | -3.82016 | -46.00104 | 2024-10-28 00:50:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 8a450d6a-847e-3fb5-979f-bf36600d3500 | -3.81286 | -46.93309 | 2024-10-28 00:50:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 644d41e4-6889-3d8a-9c0a-7c90cb436367 | -3.78658 | -46.09138 | 2024-10-28 00:50:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 93e44c60-6bd7-376b-b504-2c0565256199 | -3.69253 | -51.84584 | 2024-10-28 00:50:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9c6229aa-113f-3829-992d-cc54752ce9aa | -3.68129 | -51.56854 | 2024-10-28 00:50:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 20d11de3-99aa-3e7c-bb4f-0d45787500ed | -3.67272 | -50.30003 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| d28ac76c-f1b2-3d82-8773-8399dbaa1f07 | -3.67202 | -45.93233 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f02fe3ff-b9c2-3892-9dff-579dffb51d4b | -3.67123 | -50.28931 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bef3f916-0524-37e7-9475-0134daaa3734 | -3.65339 | -50.16113 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 6cb2f531-6c4a-39a9-b5a3-952c3de29c53 | -3.65193 | -50.15058 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0f94f89f-3732-3d06-b8a4-74aebfa89c25 | -3.62595 | -50.17579 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c481266f-3eb7-37bf-81b6-ddd55f8cf128 | -3.6178 | -47.25849 | 2024-10-28 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| aedcc6ab-6d8a-305b-b885-edaf3cd591d2 | -3.61631 | -50.17718 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a12ad48d-e61b-34ee-aefa-7da251758b29 | -3.61019 | -47.26855 | 2024-10-28 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7d60db84-8902-35ea-99f5-5863170673aa | -3.60896 | -47.25975 | 2024-10-28 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f6f3df93-95c6-3469-9808-bde473ed00d4 | -3.60774 | -47.25093 | 2024-10-28 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 95a69f77-da87-30bf-b0a4-7868f4c77cbf | -3.60579 | -49.36001 | 2024-10-28 00:50:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 44365aa7-0745-3d23-b461-aedd8fc8ace5 | -3.59657 | -49.36132 | 2024-10-28 00:50:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9aaf9623-3777-3ee4-83a0-3a2b5083a6e1 | -3.59375 | -47.27987 | 2024-10-28 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 8d93d1dd-5fd2-39f1-9738-37d504d98b36 | -3.51082 | -50.29513 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e5c14b9d-96c8-3eaf-b855-ba9c72b3b68b | -3.50204 | -49.9436 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d5b8d812-8869-382c-8e2b-b68ce0cf60c5 | -3.4591 | -51.64394 | 2024-10-28 00:50:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e3d5e539-c3f3-349c-af1d-1e9825d5f07f | -3.43338 | -50.25791 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7c27bfe1-9988-3489-bbcd-7c07d45a883f | -3.43192 | -50.24722 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b71ff62f-a28f-311b-97f4-68f0634f83fc | -3.40497 | -46.32695 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 57dda72a-f17e-36ab-8128-2f3277e5804e | -3.40369 | -46.31777 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 5ff40efd-255b-3e8b-a72e-edb7e8ba8528 | -3.3908 | -46.35705 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 89fb8a4a-4c20-3a31-9b0d-e8eac4db48fc | -3.38348 | -52.43644 | 2024-10-28 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 49ec1a5e-a30f-34e2-b523-9c688f072fe8 | -3.35081 | -46.20315 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c94844af-0e78-384d-b2a3-a2612022796f | -3.34763 | -52.17366 | 2024-10-28 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 6dd367f9-6857-3535-b660-6c36025b50b4 | -3.34142 | -51.53378 | 2024-10-28 00:50:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 86d2e1b9-9521-3f49-a1c1-069339918792 | -3.33868 | -50.09457 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c70e5acf-4ec7-329b-b837-a10b60b0156d | -3.33491 | -49.92705 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 24076596-7b80-3895-9776-4f19c479e83c | -3.33466 | -45.88939 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c86665c5-5292-30d7-a0f4-eb7a4f890678 | -3.3335 | -49.91685 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e6042558-d2bc-3bb2-bc4d-8f0d95951dab | -3.33249 | -51.62726 | 2024-10-28 00:50:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| b44d98ba-4bb9-36ba-9ff2-f8d0ef22db5f | -3.33075 | -51.61429 | 2024-10-28 00:50:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 10c7068b-e2fe-3b39-8a25-8915c7d1f9bc | -3.32544 | -49.92833 | 2024-10-28 00:50:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5fb2e0e5-5412-3f24-9529-f6fe967d4a93 | -3.32403 | -49.91816 | 2024-10-28 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6d8f2fb1-7296-36b2-82d9-e791eb3e6107 | -3.27931 | -46.21949 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 88e94ec9-68a5-3a7d-93af-4184968d7008 | -3.27026 | -46.22078 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| fa174bd9-f0b3-3aea-b23a-3d077c0eccc2 | -3.26896 | -46.21151 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ed1f7fe5-f419-3543-86e4-839b09d51295 | -3.26623 | -50.02636 | 2024-10-28 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8d56e4c2-45f6-394a-a4d3-33c13109f444 | -3.26121 | -46.22206 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6396796e-941b-3738-a199-17fa41873140 | -3.2599 | -46.21279 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 04fd0aad-2829-33f0-a373-ca0b1ae8e4f8 | -3.24273 | -46.02467 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c3fec8d2-e32d-3789-b41a-0b61ee3d15f0 | -3.24192 | -46.28148 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f73fc8b-b385-36f7-b020-8af38537dc66 | -3.24061 | -46.27223 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 321e11af-79a1-366b-b8a5-2c73d0af423f | -3.23361 | -46.02599 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c169da96-fe62-30c1-a77b-74d237da6265 | -3.23289 | -46.28272 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8c591cda-bbec-3a13-8e54-9af25732b1ea | -3.23095 | -46.00713 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c20f92e7-6b14-3d1d-b5b7-946b10a16f40 | -3.22963 | -45.99772 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 67e122fe-4ed9-33db-97fc-94caad573c3b | -3.22894 | -50.17989 | 2024-10-28 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e2b3ab26-9e17-35c2-bf7b-2c646f2ef57c | -3.21933 | -50.18117 | 2024-10-28 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 19531b30-ecc8-36a5-8650-beec5039d2d5 | -3.21792 | -50.17068 | 2024-10-28 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4e9ad2a1-820e-3a84-9a22-3733eefa256b | -3.19113 | -46.18118 | 2024-10-28 00:50:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3db83202-8a7d-3342-b546-5ba0a1eb7225 | -3.17353 | -45.01793 | 2024-10-28 00:50:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 72b6d602-e9fc-3ab4-ae36-097f01ef5e1a | -3.17203 | -45.00743 | 2024-10-28 00:50:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 3dd3dae1-ad21-3cf1-bad7-6b5d7fbd6b1c | -3.1705 | -49.14461 | 2024-10-28 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c70b5237-cb61-31c4-af60-dd203f6ee3ba | -3.16806 | -46.61149 | 2024-10-28 00:50:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 6d31f3aa-9e44-3f30-98b4-0a2bca31389c | -3.1668 | -46.60245 | 2024-10-28 00:50:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| edc2059c-d96a-3d81-8185-a97040f317ba | -3.13945 | -49.18381 | 2024-10-28 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9f083f2c-69c5-3a1d-9920-0ca9e9727b95 | -3.12903 | -49.17566 | 2024-10-28 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0c4dd42a-dbdf-316e-bfab-4c751cc55201 | -3.10625 | -48.60989 | 2024-10-28 00:50:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2a3e1ce6-6965-32ed-9446-c2cf2caf4b15 | -3.10501 | -48.60086 | 2024-10-28 00:50:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9a945986-e8ac-31f9-bd8f-1afc011e3b46 | -3.07593 | -44.3356 | 2024-10-28 00:50:00 | TERRA_M-M | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| a6968c2c-eb15-3a41-ba81-b87dac0865a4 | -3.05407 | -49.50304 | 2024-10-28 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c4fc6f62-b78b-3c84-b3d7-7708ca5c1d47 | -3.05274 | -49.49335 | 2024-10-28 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 6fc47eae-6354-309c-9eec-a121100af761 | -3.05142 | -49.4837 | 2024-10-28 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 20df64ab-0690-34a3-8ad2-c346e771808f | -3.04484 | -49.50435 | 2024-10-28 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e1366512-153f-3807-a031-f8bc6fce5287 | -3.04351 | -49.49465 | 2024-10-28 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 70fccf2f-9de2-36a5-a7e4-e593aafdaa7a | -2.96078 | -48.95855 | 2024-10-28 00:50:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c96c032a-9c6c-3e96-9b16-e00e84bb8cda | -2.93315 | -49.55185 | 2024-10-28 00:50:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 53ecd216-8524-380d-bcb6-bc31a43b94b4 | -2.90471 | -45.27623 | 2024-10-28 00:50:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| f40e486c-f889-39a8-9776-dc59cb54af19 | -2.90324 | -45.26601 | 2024-10-28 00:50:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7a16d16e-4959-3482-8ba0-1c370ef36e05 | -2.87477 | -49.2678 | 2024-10-28 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4e4eb698-ab20-392c-9fec-5c7c06670dac | -2.87346 | -49.25838 | 2024-10-28 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 217.7 |
| 5f132b58-5f37-3c40-abb5-ce13cb5c801f | -2.87215 | -49.24896 | 2024-10-28 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6687c86d-f11a-3a00-beb7-44ad96a3b6c8 | -2.81541 | -48.44041 | 2024-10-28 00:50:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 754b74f5-f8c6-31b0-aa31-9d11ec73b99d | -2.80543 | -48.70409 | 2024-10-28 00:50:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7dca4c1b-2aad-3f16-a945-4f57c56581e7 | -2.79938 | -45.35572 | 2024-10-28 00:50:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ba39a095-f7af-3239-b092-57819a317313 | -2.77534 | -45.97703 | 2024-10-28 00:50:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b8a3ee37-e62b-3823-86bc-322ae1a3e926 | -2.74271 | -46.01091 | 2024-10-28 00:50:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8378f0a0-a5ea-3fb1-9a34-c0f85d3ced11 | -2.74136 | -46.00139 | 2024-10-28 00:50:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e831d49e-b90d-392a-84be-90e4cb34778d | -2.72813 | -46.6892 | 2024-10-28 00:50:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3dda0e59-42e4-3e1b-a110-e45c624f59ef | -2.71914 | -46.69638 | 2024-10-28 00:50:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 084432da-a38e-3583-8adf-f0b54c8aba7f | -2.71788 | -46.68734 | 2024-10-28 00:50:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 22e0f4d1-e7ce-35f7-bf6f-9bf1ab68417a | -2.61358 | -46.13795 | 2024-10-28 00:50:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3cc4c925-5d43-377d-9343-c2f58d7e52a1 | -2.54636 | -45.9926 | 2024-10-28 00:50:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| afa3a95a-61c1-385a-b4c6-61dc7aecad45 | -2.545 | -45.98304 | 2024-10-28 00:50:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6693ad20-ed85-3353-8973-5b497472923d | -12.67339 | -46.58635 | 2024-10-28 00:50:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 59e7e0e3-c690-3718-a831-90103ea4195a | -12.67214 | -46.5771 | 2024-10-28 00:50:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d411240a-6e29-312b-81d7-c8cf27f9321c | -10.30468 | -51.88783 | 2024-10-28 00:50:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ce00e71a-8121-3b65-8b1d-dc0a26ec0834 | -10.30062 | -51.89472 | 2024-10-28 00:50:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |


[Clique aqui para ver as próximas entradas](README13.md)
