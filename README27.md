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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d33a4f41-6b89-35d4-ac36-1e92c8cfa9e2 | -7.9943 | -43.1298 | 2025-08-04 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 2ce7d50e-c16a-38ae-acdf-a9b0e85f0c74 | -8.0324 | -43.1022 | 2025-08-04 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 192.6 |
| 7c513cf5-ba76-3aeb-abcc-db068b0f56c7 | -7.994 | -43.1534 | 2025-08-04 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| 2be81180-4816-3086-ab27-cc46ff189bf7 | -8.0132 | -43.1278 | 2025-08-04 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 174.4 |
| acdea8df-d32f-392c-baef-fc89c4c2ad85 | -8.0129 | -43.1513 | 2025-08-04 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.0 |
| c01b8257-2618-3966-a747-e89bd7856e00 | -7.9931 | -43.224 | 2025-08-04 11:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 149.1 |
| 98eedbad-0c2c-35ac-ab72-d84bdb313443 | -8.0129 | -43.1513 | 2025-08-04 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.8 |
| f413ca2a-5a31-373d-bf7c-2d05d30f2218 | -8.0324 | -43.1022 | 2025-08-04 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 159.3 |
| 63815433-5735-31ec-a1ae-7eb56cff392c | -7.9931 | -43.224 | 2025-08-04 12:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 225.0 |
| 6d37ec16-8dc0-3715-a6d2-49085228767f | -8.0321 | -43.1257 | 2025-08-04 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.2 |
| 648f7ad8-053d-3650-a9c9-8cedbc416d87 | -8.0513 | -43.1001 | 2025-08-04 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 006a87cd-ece6-3c86-a342-5f3beb551567 | -7.9934 | -43.2005 | 2025-08-04 12:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| d0c8c25d-0c87-3552-bbc0-5409748d4019 | -7.994 | -43.1534 | 2025-08-04 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 78051d1f-025f-32b4-b998-83c5f3c7de33 | -8.0132 | -43.1278 | 2025-08-04 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 181.8 |
| 6c9d95b4-a873-3b13-8fd6-46f073f05043 | -7.994 | -43.1534 | 2025-08-04 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 0520b3d0-e6dd-30e0-ab19-feeabfdc4439 | -8.051 | -43.1237 | 2025-08-04 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 657a71f4-5500-3f91-96d6-7e791db0c647 | -8.0321 | -43.1257 | 2025-08-04 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 143.0 |
| 1dcafa51-2476-353c-9157-94d05c43650c | -7.7629 | -45.0972 | 2025-08-04 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 220.1 |
| 43a78891-c6b6-30c1-b591-1a0b4993ffda | -8.0132 | -43.1278 | 2025-08-04 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.9 |
| 7176c71e-913e-385d-a96d-f8453b1a7b42 | -8.0129 | -43.1513 | 2025-08-04 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 159.4 |
| 616702b1-1aa5-3ff7-b999-8a4358e66bb5 | -7.9931 | -43.224 | 2025-08-04 12:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 176.9 |
| 5793f3e2-5736-3a06-94e1-b1d6a513b961 | -8.0513 | -43.1001 | 2025-08-04 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 723c715d-cbe5-385f-a7bb-24069a322581 | -8.0324 | -43.1022 | 2025-08-04 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.7 |
| f70b7ef2-6763-36dc-86bb-1d6790ddd088 | -8.0129 | -43.1513 | 2025-08-04 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 166.9 |
| 3a09a00a-7ef5-3cd1-bd86-3eff6f4acf13 | -7.994 | -43.1534 | 2025-08-04 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 17103292-3bfc-384e-953d-da5373a190d7 | -7.7629 | -45.0972 | 2025-08-04 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 57c9b349-e01d-3155-8b12-b6a9357b632d | -8.0321 | -43.1257 | 2025-08-04 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| d0e15970-6627-3c6c-905f-0bfd2f90ed98 | -8.0324 | -43.1022 | 2025-08-04 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| 18aca478-a848-3a87-acfb-a3c353767031 | -7.9931 | -43.224 | 2025-08-04 12:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 191.2 |
| b02da523-4f75-3866-82e3-1d48902dda0b | -8.0132 | -43.1278 | 2025-08-04 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 177.0 |
| f69b5a21-4c36-389b-b402-8bc88240f948 | -8.0129 | -43.1513 | 2025-08-04 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 181.6 |
| 38d82e19-8c98-35d8-b191-5624a6846854 | -8.0132 | -43.1278 | 2025-08-04 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 197.3 |
| 2c9c9c15-a73d-36ef-be65-dd565292ab09 | -7.9943 | -43.1298 | 2025-08-04 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| d1912c79-cab8-3a50-8a2c-9f82a9aa8fcc | -7.994 | -43.1534 | 2025-08-04 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 9a036684-5a4c-37cc-b1b6-1acc7f0e9fcf | -8.0321 | -43.1257 | 2025-08-04 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.5 |
| e805bd14-0b44-3307-91fb-5dc4e850175f | -7.9931 | -43.224 | 2025-08-04 12:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 149.0 |
| df6e60c3-d26e-3b73-a1c5-30d446b06924 | -8.0324 | -43.1022 | 2025-08-04 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 203f8895-a5f7-309f-9fd3-5af36734b235 | -7.7629 | -45.0972 | 2025-08-04 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 253.0 |
| d728d20e-4b4d-3c67-9c29-36b573d5df96 | -8.0129 | -43.1513 | 2025-08-04 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 219.1 |
| 46e655b7-7047-3505-8895-3213f979faa9 | -8.0132 | -43.1278 | 2025-08-04 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 194.9 |
| aeb1d2b9-8971-360b-8b11-5f1634c2e370 | -8.0324 | -43.1022 | 2025-08-04 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 424108ff-1649-379c-8449-108fec663994 | -7.9931 | -43.224 | 2025-08-04 12:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 173.2 |
| d6d9c3c4-5a00-35fc-a3b7-d5122d4392fe | -7.7629 | -45.0972 | 2025-08-04 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 9f737265-1316-35f0-b987-6c8afe402463 | -7.9943 | -43.1298 | 2025-08-04 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 55796691-f753-3872-aa23-c340eb3abfa7 | -8.0321 | -43.1257 | 2025-08-04 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 2b07e6e6-4011-35f1-9264-4b2f6cc8aed4 | -7.994 | -43.1534 | 2025-08-04 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| 2c4bd29a-3e52-383a-8c97-e9800a59773f | -8.0132 | -43.1278 | 2025-08-04 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 162.8 |
| 7852d025-f44c-31f2-91c6-6563ff0f6f4d | -8.0129 | -43.1513 | 2025-08-04 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 206.0 |
| 5d8b83f8-afb2-3694-b1aa-4a222e18cf06 | -8.0321 | -43.1257 | 2025-08-04 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 1b799af9-8a7c-332e-93cd-b4ff02bf2079 | -7.994 | -43.1534 | 2025-08-04 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| 730bca1a-a7c6-3ad3-be65-f6a5f86b4b48 | -8.0324 | -43.1022 | 2025-08-04 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.2 |
| 4ae8c33a-9c3a-3834-9022-f0f5a59a6a03 | -8.0513 | -43.1001 | 2025-08-04 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| e000233a-16b1-393c-bee5-cc762b00fef0 | -7.7629 | -45.0972 | 2025-08-04 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 21899c7a-f9a8-394f-80e1-499a2379b41f | -7.9931 | -43.224 | 2025-08-04 12:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 208.7 |
| 866d3f19-3e3c-38b7-91f8-3c07e68f74f3 | -7.9943 | -43.1298 | 2025-08-04 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 19491990-31eb-345a-ba82-a9be87dcd9ed | -8.012 | -43.2219 | 2025-08-04 13:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| f566a75b-05cf-34f0-b4b0-8f4875a1ab48 | -7.7629 | -45.0972 | 2025-08-04 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| dc80358f-8a32-3fbd-90c3-c35fc9279fe4 | -7.9931 | -43.224 | 2025-08-04 13:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 236.8 |
| d069b76c-a9a6-31e6-846e-1798463ea5ab | -8.0324 | -43.1022 | 2025-08-04 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |
| 9f9f1595-e68e-3eb8-9ca0-f66b1ac2d7fd | -7.9934 | -43.2005 | 2025-08-04 13:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 051d075c-fd19-370b-9050-204c6c2d188d | -8.0123 | -43.1984 | 2025-08-04 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 7156aa20-94ca-3909-87f9-3cfec13cfc75 | -7.0946 | -44.3589 | 2025-08-04 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 377a4a1e-1f71-38db-b566-2b4e0b9ceda4 | -7.994 | -43.1534 | 2025-08-04 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 162.1 |
| 4164ff7e-b95d-3b00-9126-ecf1c66bf584 | -8.0324 | -43.1022 | 2025-08-04 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 159.1 |
| 66be8094-f588-3bd8-b0f5-3ef7a2549938 | -8.0129 | -43.1513 | 2025-08-04 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 159.1 |
| a1b51a0a-7f06-3194-a4f9-e3dd9d5e635b | -8.0321 | -43.1257 | 2025-08-04 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 178.6 |
| f86db0c4-29eb-343a-b73f-dcb66a3c1d41 | -7.7629 | -45.0972 | 2025-08-04 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| e5854550-7096-38c6-a621-e012c6a6896c | -7.9943 | -43.1298 | 2025-08-04 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 8046c68c-f68b-3442-a3f8-77b24b510c5e | -8.0132 | -43.1278 | 2025-08-04 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.9 |
| 55f33c55-87ac-3d57-8160-8d35f2c0a3eb | -8.0126 | -43.1749 | 2025-08-04 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.3 |
| ff37d3b9-8c8c-34d9-b4d9-3c0529a49886 | -8.012 | -43.2219 | 2025-08-04 13:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 312.0 |
| f2050dca-161c-3cbe-99f5-c18045ab845e | -8.0321 | -43.1257 | 2025-08-04 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.3 |
| b68762c3-dd82-34e1-921a-daafcfe5828f | -7.9943 | -43.1298 | 2025-08-04 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.3 |
| 83e11001-2bb6-3336-aec3-a909b7f27dfb | -6.5263 | -44.8659 | 2025-08-04 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 33ce0372-f8e5-3cb5-82a2-0ec4ef268321 | -8.0129 | -43.1513 | 2025-08-04 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 174.0 |
| 620a7bf0-300c-324f-b111-44cfac2d1d7a | -7.994 | -43.1534 | 2025-08-04 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.0 |
| c0426cde-43c3-3428-b9d6-6d0853c278d2 | -7.7629 | -45.0972 | 2025-08-04 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 08163898-9952-36c7-bce2-20604921be12 | -8.0132 | -43.1278 | 2025-08-04 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.8 |
| 15ae7bde-c1be-372b-a87f-7749c8df288a | -6.5261 | -44.8887 | 2025-08-04 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 80ffe96e-765d-3485-9799-a886bd129994 | -7.0946 | -44.3589 | 2025-08-04 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 884943fd-a9ca-3cb9-95f4-2f2ccbd77d82 | -8.0324 | -43.1022 | 2025-08-04 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.3 |
| a818972e-e02e-376a-8064-16053f65d9f3 | -7.9934 | -43.2005 | 2025-08-04 13:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| b74108cb-1f58-3775-9833-9c2dce9f0be2 | -8.0126 | -43.1749 | 2025-08-04 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 921c70ba-0e1a-3d00-a55c-1a8be7d03c49 | -8.0123 | -43.1984 | 2025-08-04 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 1811bdea-987c-3f11-8e4e-0c4a6504db1b | -7.0946 | -44.3589 | 2025-08-04 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 75a3d02b-1a51-39ad-8b72-b1242b9b9a08 | -7.629 | -45.2918 | 2025-08-04 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| cd02032e-b7d3-37aa-821d-1e072246d184 | -8.0324 | -43.1022 | 2025-08-04 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 0bbfa030-6425-32ce-be65-728500cbfc35 | -7.9931 | -43.224 | 2025-08-04 13:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 441.6 |
| 751dd45b-0986-385b-b54f-71ad4320a691 | -7.0757 | -44.3606 | 2025-08-04 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 5549465a-ef78-3ff9-96b7-67de3c238d48 | -8.012 | -43.2219 | 2025-08-04 13:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 247.7 |
| dd133f1a-2505-3d53-8ee3-84a31fba33bd | -7.5585 | -44.8887 | 2025-08-04 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| f5c8991d-fca8-3966-aca6-01a2aaff44f2 | -7.9934 | -43.2005 | 2025-08-04 13:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 152.3 |
| 34742b48-f9e7-3c22-b583-bd1ae360da51 | -7.7629 | -45.0972 | 2025-08-04 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 48bdff72-d3f8-3c70-82c5-99409929740e | -6.5261 | -44.8887 | 2025-08-04 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 520334c4-4b82-3ead-9df1-97bca4587a7c | -8.0123 | -43.1984 | 2025-08-04 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.7 |
| 349c8b5f-aa03-300a-b991-078c4ec38b7a | -7.7629 | -45.0972 | 2025-08-04 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| ce40737d-d90d-3c6b-a4c1-0c497a1cf8fd | -8.0513 | -43.1001 | 2025-08-04 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 626059d0-a218-3380-832b-3fd9875ab8fc | -7.0946 | -44.3589 | 2025-08-04 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1ab0a687-1fb8-3334-9590-d85bc447bef7 | -7.0757 | -44.3606 | 2025-08-04 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| d9db953b-24a6-3ad4-852b-e6fbe99dd14b | -7.5585 | -44.8887 | 2025-08-04 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |


[Clique aqui para ver as próximas entradas](README28.md)
