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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1e25ec1-febb-3ecf-9ffb-1514d1792c25 | -2.22847 | -50.84994 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1edb95d-06c1-3791-9d3e-c94c11b37a7f | -3.2717 | -50.20494 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a6c5dd01-0641-3fed-9f16-3a55bcbdc8c6 | -1.15793 | -52.23911 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1391b67c-3ebc-33f9-b57a-55cf6024df0f | -3.29286 | -53.83472 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0577ab2a-7fa8-3a15-8bb1-4b71efaadcd7 | -2.57824 | -54.21427 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1815c0c3-8a0e-382e-bd5c-c1d86126c381 | -3.32442 | -50.19202 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cb2a7ff8-5b80-31d6-96e1-a55b9726358b | -2.73796 | -47.97525 | 2024-12-01 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba561759-da62-3fa9-ac14-206042782b23 | -4.10889 | -48.53549 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc491511-784f-3e1d-a952-85d8b93d78fd | -2.06525 | -51.19599 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69c802fd-2466-3922-8b9c-04a0eed86bbe | -4.70086 | -42.39757 | 2024-12-01 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| af09e7fe-4240-3656-8815-6112febc35c1 | -2.75515 | -51.66552 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb0236f4-322f-3d40-803d-3a601139be2b | -0.24739 | -53.76235 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0fdf2c21-d451-39d3-a3ad-fc3ad0bc159d | -0.04149 | -51.26667 | 2024-12-01 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb169807-db8c-3054-a83f-58d96745eb31 | -3.69026 | -51.8222 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 96512207-4dcf-369e-a3d4-7f94311b85ce | -3.06468 | -53.68451 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41d3140f-cc49-337a-9e2a-6abc5a3ecdbf | -2.90519 | -51.57891 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a96cea04-c1b4-338b-9782-651b94ae2f6a | -2.44051 | -53.62592 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 043dadc7-2ef8-3f78-af7b-4b8a53531a21 | -3.31928 | -50.1382 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91cbd410-3682-399a-b3a5-afd0547623de | -3.00975 | -52.01926 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 532028cb-c721-3624-bae1-6ae769374b6e | -2.83888 | -54.10896 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fc8948ca-fd63-3fed-bd67-e198630b1d99 | -1.2478 | -51.78679 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8444135-935c-3baf-8441-aec00a6a0c56 | -5.19962 | -50.48941 | 2024-12-01 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bca91f74-1d3b-32a9-a74c-3edb9b53dc6b | -3.75063 | -52.6747 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a891d018-ae51-30a0-bbdb-573a8242fec3 | -2.37699 | -50.42858 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad203a7d-815d-31f5-b252-054413c3efbb | -1.17664 | -51.95699 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83ed9901-fa4c-3d48-91dc-3af0b066909f | -4.00157 | -46.94063 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54ad1bc8-8d81-3d77-8839-7d6aa1e0978a | -3.06837 | -53.68507 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b65dc11e-6512-3130-be3d-964ff7a1134e | -2.04917 | -54.68406 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec1e0a27-fb2a-3f06-b11b-f758b71fa9f4 | -3.26635 | -48.77192 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03823eb6-4f38-3fcf-8005-97869ed5d123 | -2.65332 | -46.5799 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f23d79b-4ddd-3416-b264-45fc4feee140 | -1.32764 | -51.74552 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 000e196c-aca3-34fd-adb4-ae4118c9bd80 | -3.6164 | -50.18848 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1759d8a8-1998-349b-88b6-14d916db848f | -3.07277 | -50.98938 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 83cdae6e-dae8-3e34-ba2b-52c5aabd64ce | -2.85242 | -54.09709 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed4aeda0-f009-381d-8253-ee4d8ce4fc53 | -2.74465 | -51.75287 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 50d023c9-e77b-3a8d-8d0c-75bca5311f90 | -1.70095 | -52.63804 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eac9c6e4-8a33-381a-a8ea-93c6fb4aadad | -2.12055 | -50.33564 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30b05ef8-d054-3b4e-8de9-c9a37230ab3d | -1.0809 | -53.39545 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3db899a7-d3cd-3bc4-bc01-ea8f185bcdad | -3.34446 | -50.23755 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d11e794-fac6-39ff-8091-ce7489929120 | -2.04686 | -54.67333 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 27e2711f-7a86-3609-86ba-710e913e8b74 | -3.10048 | -53.271 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3648c564-7ec5-3680-8e93-3bba6f2e7eca | -2.39154 | -50.48751 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 870cc0b9-01b4-3684-852e-8af633eab277 | -3.26013 | -48.76727 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60822167-1484-328f-821f-7ed74d2a5002 | -1.44164 | -55.13165 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6976eae9-f7ba-38bc-972b-4437488cab11 | -3.28731 | -53.66756 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77a1e6e7-cd53-3c33-8515-796895afac5f | -2.70804 | -51.87473 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85e7921c-0255-3866-ade8-dbd9db081270 | -2.52457 | -54.07156 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c643e24d-d28a-382c-9e0d-393e891a656d | -2.76785 | -54.19503 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fced0e2-aa6f-389f-befc-987052390625 | -3.78133 | -46.69614 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5386c664-fea0-35db-b968-a2584ba7b4ab | -2.84791 | -54.10103 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50ed6260-0fcd-397b-a2a4-d80860b263b8 | -2.96231 | -53.89664 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b57df1a0-755b-3425-af98-afe11b442859 | -3.05437 | -52.76669 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 120d8b0a-82b0-39bf-822c-9444f48d332e | -2.81005 | -54.0716 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 094f0b3f-3402-3b17-9d5d-8ced90805de7 | -1.50075 | -52.60454 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 25ebcaff-538e-3bc9-a42a-4b74f8580256 | -2.45057 | -53.62106 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d7064e7-604c-37cb-8fe0-7189563f2560 | -3.5378 | -54.08344 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1507a73e-7671-36ea-83ee-157a97a27837 | -0.26378 | -51.49682 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af226da8-d8a8-35b9-9564-b6aacf0f3d4c | -2.85385 | -53.9444 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb209c35-7fb4-34e4-9927-0ea420146b09 | -1.35098 | -52.82195 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 570596fe-d6d1-3efe-b6f5-2d13732055b6 | -2.63774 | -49.91097 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 088483eb-e899-33bf-970f-bd8b202e69a1 | -3.34494 | -50.74696 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ec08758-1895-3d57-86e2-f0482d4a5707 | -2.86841 | -53.99735 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d0ba920-b315-3d45-84fe-97ccea28b3e3 | -3.31542 | -50.14114 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 377b247f-f306-35b5-a551-c7fe3b7ec890 | -3.84604 | -40.98036 | 2024-12-01 04:44:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| ad893cfc-8fa6-3c6d-a564-a32feec6a3ed | -2.92165 | -54.26768 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3194b6f3-115d-3733-a36f-55ee37e79404 | -3.12261 | -45.98559 | 2024-12-01 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbc4de7d-774b-3534-8f3b-6a9c887203bc | -6.71486 | -47.27682 | 2024-12-01 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7076b670-5967-30ae-bd4e-7d16dab0c5fc | -2.7964 | -54.0368 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68478af9-b159-3c5d-8c2d-2bc9619a0545 | -4.06864 | -49.06728 | 2024-12-01 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13673705-0210-3ad6-b61b-11ec8776550e | -3.90879 | -52.33953 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ac3be2d-d40b-3359-88b7-5fe29b907b7d | -3.09931 | -54.02608 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3ce91bb-59d3-32b7-9b44-58702158109c | -3.86921 | -51.00702 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ece8579-f52a-33b4-8f6d-e1d2a9fd7140 | -1.00015 | -51.72325 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a009b95b-fb10-3050-b435-77e0a9a473e3 | -1.64635 | -52.75253 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d36754e3-c4e6-3e03-b6d0-4116555c6080 | -4.05272 | -46.8177 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f051469-266f-360c-91c3-8cf6f29be71b | -2.99398 | -51.06325 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e068b12-5dff-39f8-a8e4-34775a3d0d01 | -3.07015 | -53.80364 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf7b4b17-2ef1-30da-8325-09a90fa06cca | -2.78584 | -49.83205 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be16e7b9-584f-31e2-b9c1-37d9dcd159ea | -2.65909 | -51.87453 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f1dcd079-1aeb-3288-bcd9-6d9c7d94b70a | -4.61784 | -46.47084 | 2024-12-01 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0be5da8a-a9ee-38a5-af1d-df763b0545c3 | -3.46749 | -50.38027 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46be06b4-b328-3b7a-830f-22a988fd5e25 | -3.25408 | -53.64012 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca678a95-431f-3848-b5e7-fdd40f4b9b53 | -3.75851 | -52.27066 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f31fc7f9-01c1-37ff-9159-09d43825e41f | -1.31904 | -51.73703 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fa8db51-134d-3ed2-a02f-d2f9ebdfdf2a | -2.12332 | -50.3396 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3043ceb9-e9af-3152-add4-2714e2d337c4 | -3.28916 | -53.83414 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79aaf410-6314-37be-8ed6-377be4a9f0b2 | -2.94433 | -45.71154 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90533cc2-7d2a-3db4-b571-786dcaf208fa | -2.68963 | -51.72612 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95fcaa5e-5140-3ca9-9e2f-e5b8b4c29dcc | -3.69083 | -51.81858 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4195a071-cf52-3a24-a040-5026258be646 | -3.02719 | -51.53523 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78c9aa50-b349-3d88-bfa8-79d0bdf0757d | -3.95445 | -49.90769 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 702d7774-b500-3762-b145-e3d541bd6287 | -2.92623 | -51.44673 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 80f020e5-8f56-3268-8da2-2f20ba2d7cc2 | -2.04256 | -54.66076 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d58e129-b050-34d3-bd84-33ba4ec58bb9 | -2.31219 | -50.68816 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53278912-198f-3aad-bf65-803b964b1215 | -3.5491 | -54.81899 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5528326-b858-3057-9448-88adee70ca8d | -1.7222 | -45.76176 | 2024-12-01 04:44:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d35e2e9-3452-33ec-b0a6-029383e66e18 | -3.0924 | -51.40687 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05afaf9d-43fd-32fb-8e3a-87b74759e9d4 | -2.65284 | -51.86981 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 309fa65e-ddf0-3712-b56f-375cf21c2ddf | -2.43298 | -50.39491 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b75d01e3-9320-3024-94c7-168e0f4e6f2d | -3.48698 | -53.81952 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README51.md)
