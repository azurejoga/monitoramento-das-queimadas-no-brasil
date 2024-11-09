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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d23283a9-b7b3-30be-a09e-68e8e1146cca | -4.52634 | -50.50671 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 641824a9-d454-3b4e-915f-cde4abb0f559 | -6.06839 | -44.14678 | 2024-11-09 04:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 714909be-9682-3ca6-9503-833da0e794db | -3.01277 | -51.03893 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0742f2c9-85b3-3198-976c-713c12b6ee49 | -1.57467 | -54.63528 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bb01025-4668-30a8-bd0c-cd8689e4bc90 | -2.81447 | -52.95167 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28af223e-3b38-3e83-9cf6-e7f9d6281200 | -3.03382 | -51.52861 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e554c2e-2a56-3e1e-a3ec-6f2d0f1a35e4 | -2.21709 | -50.45288 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d770bd87-aabc-3500-8b32-e2c063cf23eb | -3.227 | -50.3791 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88b0451b-5200-367e-9916-9d2503978c48 | -7.45736 | -43.57607 | 2024-11-09 04:55:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 132ae697-9315-3afe-a796-a110930358c5 | -2.76158 | -54.041 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3dc194b-7424-3dab-ab86-d7b3ba4684ef | -2.82085 | -50.43664 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ce288c8-6732-350a-812a-c67b8c43d2e4 | -5.80454 | -50.15042 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3658b565-4f18-337c-9172-3baa06b08ba8 | -1.2186 | -51.75365 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99b60a27-3526-376c-a301-86e02baff3fa | -3.55091 | -43.5651 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| daeb25ba-2af1-304a-955e-5fb41e17b894 | -2.99924 | -49.23727 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 844ef556-9a93-36bb-bde2-40fad0a109a5 | -2.97803 | -50.30537 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 328aef7b-e543-3d36-9fda-666c4362bbec | -0.3713 | -51.42735 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ce54a8a-e8d0-3e58-9c09-e0a5789b6519 | -2.75998 | -53.21169 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd1c63b4-e6cd-3845-b1ea-1a9e828c2f48 | -1.97856 | -52.02658 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cdf10ae-9799-3158-b8ae-f7cda2ae9f20 | -2.21943 | -50.73763 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e033fee-4695-3f27-97b0-f2bcd3b34940 | -3.17679 | -51.30664 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7460f8e-90e1-3c7e-97f8-857861102012 | -2.39937 | -50.43774 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63933e52-8b41-3e5a-aa6b-646f714bbdf6 | -3.25548 | -51.12817 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1c326a8-7d8b-3bb4-a290-e75c9ab73002 | -2.09335 | -50.6676 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce4f56e7-6052-3694-8f05-b2e154cf2ea1 | -1.83274 | -53.72806 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 089e5f23-71ec-3575-aba3-7e69746b9acd | -6.18384 | -45.44787 | 2024-11-09 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a76a70d-c0f4-3c56-ae8d-8f3fe7247cb6 | -6.27703 | -44.53771 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d09b6ebb-b606-323c-8c3d-373b27513450 | -2.93174 | -54.11799 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f943f3ef-60bf-3de8-ae68-11c62202c71f | -2.98543 | -51.46143 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8d8ff56-791f-3d1e-8ea5-45a05b22ba22 | -1.1342 | -53.60462 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb23e780-f1aa-3c28-97ab-bac334b3c6be | -1.6733 | -52.1194 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40387b3e-9f98-353d-af70-1e18f3596806 | -2.88088 | -48.29588 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94da81fc-0ec0-37cb-a73c-3685a71b2945 | -2.91621 | -54.19441 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 883d08b9-dbae-39b0-8d13-8fa7d6a60657 | -3.8267 | -51.90641 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eebcdf0-dc47-3038-be30-ee8d80651926 | -2.11717 | -50.13787 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd017d45-d0fe-3804-ab8c-a8810875cd85 | -3.18842 | -50.58038 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37c1fa04-51df-330f-906a-cdc9edc48498 | -3.36126 | -53.39019 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdcba295-9746-312d-a846-32bf1ea72356 | -0.08237 | -51.40498 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e40dda9-a06c-3f6d-a6fc-1f3604cf7ac0 | -3.03991 | -48.04436 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bf7f5f9-0acb-3d23-a3f0-05def9f366c0 | -3.08827 | -51.22439 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ca19953-aa3f-318b-8d2e-7d5fc14c8c63 | -2.87264 | -49.37833 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d925d70b-e962-3c31-87d0-da72c64c7ecd | 0.6154 | -60.08864 | 2024-11-09 04:55:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0877abc0-846d-32ee-828e-178a39d28f4d | -2.64126 | -54.36747 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cb99c30-591b-31a5-895a-b7b30d8e0b89 | -2.23025 | -48.42582 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a756bc24-eab0-3d4b-b30f-69e5a4f65303 | -3.25455 | -53.40218 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 150e04da-ec7e-348c-afd2-ce8408d2d356 | -3.40744 | -50.01101 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1bb893b-4cac-3a7a-9389-f43d5751eb12 | -3.27091 | -50.34247 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 582cd798-5dc4-33f2-b04e-433717ec5868 | -2.86025 | -53.94918 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2df00159-e745-3b9b-92f9-f9aa37b5c6b0 | -3.1251 | -50.14914 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cc3ef6b6-675e-3133-941a-93c4f24ad091 | -2.87307 | -51.30718 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb32e118-e5af-3f50-a52e-1ce3ec8c7fe9 | -3.73196 | -54.21796 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 06eb2710-11ab-39ee-94c9-9be3347c6ce8 | -3.58971 | -51.43332 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5bfae8e-ced8-3741-b1ad-ab62b7e0e981 | -2.51588 | -47.5823 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6b54d65-953c-35e5-9dec-03e6150700e8 | -2.63504 | -46.77089 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 44e5fc16-3d1c-32a8-a52b-366726bfea99 | -3.01349 | -53.42827 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8e2f34f-6fc1-37ff-a7f1-ebe3b9384bef | -3.95063 | -48.15081 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c57ebdd-cae3-3975-9e28-eb214f4c871f | -1.13984 | -53.6553 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2ee298a-8135-3862-96e6-ac5ba4ed1b08 | -3.11866 | -54.17564 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1959825e-0a08-3975-87f1-15383e22281e | -2.78654 | -52.86953 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be65e4b1-e783-3527-bc68-f46319680c3a | -3.8129 | -50.78363 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 058bcbef-3eb5-3b1e-a42f-c870d20754f1 | -3.92583 | -50.24697 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adb9acd2-597d-311e-bb28-dd28e2f132de | -3.47516 | -50.80064 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 690769bd-a80b-39e7-955a-c38214049e6b | -1.35626 | -51.40513 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b26158a-d125-3f33-9cca-b4db5b7302e4 | -2.57977 | -48.17891 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd9c9e87-a636-357b-b996-cd5dedafc6c9 | -1.19055 | -52.15194 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41cf9908-bc63-37a8-8604-bee33a701ef1 | -2.15901 | -53.65502 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fc1793e-68bf-3265-a0b9-6b3269e11417 | -5.17397 | -44.0051 | 2024-11-09 04:55:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d18e340e-bcf4-3f59-8947-896b4823fd6d | -1.10502 | -46.51019 | 2024-11-09 04:55:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ab55372-ecfb-3f4f-8797-27be1faf1aa4 | -2.81431 | -54.08835 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22d89d6a-6850-3496-a6b7-6544c2e7da19 | -6.27701 | -44.74088 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3243dddc-58e1-37d5-bbc6-0caf30680fec | -3.95746 | -48.98888 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fac3fd55-b486-3cb0-a6f8-0d2a90799401 | -3.28649 | -51.52096 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 586d21f3-c408-3b65-bda1-95e191690506 | -3.09153 | -51.29417 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68089334-231f-3c52-8c29-36a54a109ea6 | -3.21194 | -50.23737 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae2cdb82-8514-3df9-9bd2-81918fe298d4 | -6.10631 | -44.75399 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11cb8e29-d9a7-33fe-afed-1ad82746c14f | -1.91131 | -51.49709 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e6b3f03-d841-37b6-8ff5-cd696bba60de | -2.29158 | -48.72761 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5211603-7fcf-350c-9827-2510874d2111 | -2.96183 | -54.16571 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20638810-02a6-388d-943a-277adc39fa33 | -5.44937 | -43.26135 | 2024-11-09 04:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56239840-7d84-32a6-b3d3-7ee2982a791a | -4.62438 | -48.90993 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 925b9339-0a5d-3aa6-bbe9-1e3d55b7070e | -4.34802 | -48.62482 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b7e3d92-c6df-354a-98b1-4e5ccbbb557f | -2.23141 | -46.54801 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 779a00ae-648c-3d1b-a23e-fdd287202854 | -3.03237 | -54.20864 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4f828a0-797f-3e7b-9d16-00a44c818118 | -1.19714 | -53.70345 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d231b81-d016-3665-bbb1-1ee8c47ccbdd | -2.59485 | -52.92774 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a737413-84f6-3ca3-9bd7-55188107d26c | -0.90004 | -51.75945 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1e3c01e-e9e7-3981-bf8f-6db43e9b3eca | -3.73865 | -50.4467 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4e03628-8330-3ced-8a73-ae2372a4d699 | -3.7622 | -51.76163 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 133e20ee-d17a-3a91-8952-1c06656a22dd | -3.74737 | -52.10083 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5f6cddf-dac6-3f07-8a8a-91879432c898 | -0.9127 | -51.65638 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c020814-2a8e-344e-b467-6ae040a601a2 | -3.96799 | -48.17644 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f4418d29-6923-3cba-a211-21763236fb8a | -3.17378 | -53.84937 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9e61e9f-dd35-3bc2-9fde-415d8475ec9b | -2.86655 | -47.90857 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b693b76b-5a07-34cb-a8ed-c347797cc7ea | -2.75381 | -54.5996 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa540f4a-1c0e-36f5-b407-8927441fbb97 | -1.16046 | -52.00449 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e4fddd5-6c79-3d4d-a3bd-bf5275cd4af9 | -2.98781 | -51.03901 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7ea0133-741b-3cdf-aec7-89357eb3f94b | -1.35548 | -54.65238 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fb73382-1154-37e6-8f11-def083d598f3 | -2.9947 | -49.24135 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3713d41d-6ca5-3e14-bdea-532234dedf87 | -2.67677 | -46.78059 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddecfbcb-ce71-3b2b-964f-d1ad9e8ed525 | -2.97631 | -50.29251 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README68.md)
