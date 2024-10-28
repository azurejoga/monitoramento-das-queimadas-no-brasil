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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce355da3-ddcd-364e-a0a0-b65c5844b496 | -2.8699 | -49.2615 | 2024-10-28 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 33df5344-5fd3-3983-8517-4fbd839b6e45 | -2.87 | -49.2402 | 2024-10-28 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b902db38-f12e-3e36-a126-4ca931d5dd6a | -2.8884 | -49.2609 | 2024-10-28 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 0fa5e80b-4b3e-32a4-9e6c-f9ae28c0cf59 | -2.8885 | -49.2397 | 2024-10-28 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a0a76221-f9af-33ad-a53e-64440eb7eb9e | -3.0317 | -50.4176 | 2024-10-28 05:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 26397d7e-20ea-3bf6-a7ea-4da6594c8c08 | -3.0501 | -50.4171 | 2024-10-28 05:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 1250cb5e-76af-3ca2-b572-98e43fa67dca | -3.497 | -45.7971 | 2024-10-28 05:05:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 23e08f94-cdd9-3992-8a50-7fc63956c160 | -3.5155 | -45.7964 | 2024-10-28 05:05:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 2ae70684-110c-3ee5-8882-74d66a2efaaf | -1.9763 | -52.0804 | 2024-10-28 05:15:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ce8c6c0a-b8d7-311d-9c1d-2c3faf62c90e | -2.0497 | -52.1611 | 2024-10-28 05:15:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| da1ab70e-3348-3865-bcf6-6688931b13a5 | -2.2662 | -53.7825 | 2024-10-28 05:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| afdbb4ff-cf80-359c-87de-2bb4ff9c1335 | -2.2846 | -53.7822 | 2024-10-28 05:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| fde4a48d-171d-306a-8cdb-5d8d919b9b47 | -2.4104 | -48.5479 | 2024-10-28 05:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 4bedda15-8c09-3b00-a35d-abf9868755d7 | -2.833 | -49.2413 | 2024-10-28 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 38b6123c-9865-3ec7-a086-1b1575403ba7 | -2.8699 | -49.2615 | 2024-10-28 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c22eb7f2-cc61-37e0-b1b6-629494bcfc46 | -2.87 | -49.2402 | 2024-10-28 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c679b917-6373-3eab-936e-ed749ed80028 | -2.8884 | -49.2609 | 2024-10-28 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| befe535b-b76e-3ce3-8e78-51bd6ae7ebf1 | -2.8885 | -49.2397 | 2024-10-28 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| aa145803-f995-31f7-b8e9-d85842fe956e | -3.0317 | -50.4176 | 2024-10-28 05:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 7399f8e5-e9bb-3ec3-be25-44a7ea4e19a4 | -3.0501 | -50.4171 | 2024-10-28 05:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 105a9c19-22b4-39b2-9a41-1864052d9dc2 | -3.497 | -45.7971 | 2024-10-28 05:15:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 4de62987-ebf9-3b5b-93f9-f6ec5c642195 | -3.5155 | -45.7964 | 2024-10-28 05:15:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 9fc3c4f2-11c6-36de-bab1-56b1ffc7b436 | 0.35939 | -53.85243 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71a29037-70de-3b25-b72e-a16c5b2b403e | -2.20762 | -53.68439 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cf2be88-d878-3e59-8192-0fa7bb5724bd | -2.20702 | -53.68831 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c477984-78c5-3c64-8d9c-a346e833a77b | -2.20334 | -53.68377 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0876ac7f-5a6e-36cc-89b1-2d05c4581a19 | -2.20274 | -53.68769 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c28a5760-57d6-336d-a482-ef4bc28a741f | -2.20215 | -53.69161 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 09d481ba-0e93-3868-a85d-fc15560bd362 | -2.20155 | -53.6955 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5974c507-51e1-3e79-a481-f6d2499f162e | -2.19847 | -53.68709 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bdb53137-27be-371d-8804-8579e6f68e0f | -2.19787 | -53.69102 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de1385b3-968c-37b5-b90e-edc9a3405f23 | -2.19727 | -53.69493 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c0e057a-6690-30dc-a6c2-2592df139702 | -1.9085 | -53.5309 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb71181a-0f54-314d-817c-8f73c59b58da | -1.9042 | -53.53024 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 76b4e1fe-5b67-366e-b726-c5d9a9601483 | -1.7621 | -54.00224 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 116cdedb-7f5e-37a7-bbc4-1f5f5c30213f | -1.75795 | -54.00159 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d33006d-9648-392e-bcb8-1945c44437c1 | -1.65875 | -53.3978 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79ef7570-1e09-3a54-bc7c-819f8c7b692a | -1.51933 | -53.51736 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df147c97-e334-3cd1-b43f-da3a8c05cac0 | -1.44422 | -54.07621 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bec1a38b-c7bd-3f5a-bfaf-99ee196b1fbb | -1.44011 | -54.07557 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0288494f-2130-39fb-83ca-e995963605be | -1.436 | -54.07492 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c1e6c67-9d69-38b1-9a67-ac16c6436246 | -1.43128 | -54.07817 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 473e2ddf-9938-3a5f-8cad-41d47151b87d | -1.42655 | -54.24073 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 889c5cdc-e566-36c6-81a9-5033fe20d2c5 | -1.4258 | -54.24105 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| add610b3-776f-3eab-a60c-7a6ac7d64608 | -1.42089 | -54.11756 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0475e55d-0480-3a07-b9b9-2a82aa423443 | -1.40541 | -54.05506 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4e37c1d-6653-388a-97c4-16dd6e4084c2 | -1.40128 | -54.0545 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dc26c9e-ed51-34bb-bc3d-fccb684b66bc | -1.292 | -54.19672 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 837ce4ed-ef5d-3388-985a-972ee2b090ba | -1.27712 | -54.13137 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05f528ae-3787-37c1-943c-e44c713fecff | -1.27652 | -54.13529 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 056149bb-5720-3d2a-95b5-9165a54fde7b | -1.18836 | -53.50862 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f54851fe-b2ad-3f57-a5d7-dcebc1602570 | -1.18471 | -53.5041 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4fe2c663-5783-3c48-9c93-9137ac5f8845 | -1.1841 | -53.50801 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1e522ff-a0b5-3ea5-9849-9014e2016c9b | -1.1835 | -53.51183 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c34ba59-0eab-379b-9888-d93194dc938f | -1.18044 | -53.50357 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9a7e008c-7796-3a46-a51f-11b1033f46c7 | -1.17984 | -53.50739 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6466b6e5-6dad-3cc0-9278-693039d190f7 | -1.1796 | -54.12057 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89b18bbd-459d-3f1a-9937-da8a2ecd5e13 | -1.17683 | -53.49872 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a052a95e-fe31-30ec-92fb-b114da48981b | -1.17618 | -53.50292 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 71d1e247-255d-35ab-9773-be078de644c0 | -1.17558 | -53.50676 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c8741bc8-d636-3f13-9054-31fea02d7063 | -1.17501 | -53.51043 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b2a4261-2941-3f77-a2df-17cc9168a4d1 | -1.17257 | -53.4981 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26df8e6e-9921-3427-be5e-eeb6123c004b | -1.17193 | -53.50222 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80ed57e7-6ddc-3c69-8c25-0d0e7a2cba85 | -1.17133 | -53.50609 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71b05d2e-0fdf-3279-8ba1-5178bffe06ae | -1.16831 | -53.49747 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71e6a9a1-7dbd-3e13-ab07-67be2b57364a | -1.1677 | -53.50143 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb0917f0-7982-38d5-aaf7-7e954f910887 | -1.11955 | -54.13322 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9523bbc-83c6-3d33-bb6f-b92d15e9b8d5 | -1.11928 | -54.13263 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cae72a9-d831-30ab-81bb-87ad40b5239d | -1.11898 | -54.13678 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edf57054-ed16-3787-86cc-29853ee9b119 | -1.11874 | -54.1362 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c643ce4c-c9d8-329a-ae4f-aa6455dcec64 | -1.11599 | -54.12929 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ff93bd4-5ca5-3bf2-bc18-bdbf2990df62 | -1.11544 | -54.13281 | 2024-10-28 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 800c2593-f0c7-3593-90bc-a48b83be3978 | -1.08626 | -53.66615 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f69f10d8-3e59-3e55-99c7-5c3efce27c32 | -1.08576 | -53.66872 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b6e9718c-8a9b-391a-9242-263717d53f8e | -1.08568 | -53.66981 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97484817-e6ab-3b63-ac48-82ee06b99cb9 | -1.0852 | -53.67247 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 028a8bab-448c-3da8-a15f-ccf73ef04715 | -1.08384 | -53.65426 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1b05f63-2da5-3daa-901f-4020c9d24521 | -1.08383 | -53.65306 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85a7d88a-83f0-37a9-9b47-5ea3dd62d07a | -1.08324 | -53.65698 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbdcc1d7-829b-3a16-815c-405ea3f19e6d | -1.08322 | -53.65815 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 709de883-cea3-3e5b-ad22-8f3e92f1ca16 | -1.08266 | -53.66085 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e03c6d46-c6d0-3215-a636-e724bef8521e | -1.08261 | -53.662 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd11758c-3329-3fa9-8258-cec6dbb3a71e | -1.08209 | -53.6646 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4c3d8187-17ef-3dbe-8ad7-b023a59ce1ca | -1.08203 | -53.66568 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c10f5c7-856a-3a22-8401-506391e29eb4 | -1.08154 | -53.66822 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c4ec8376-bc49-338f-a0dd-6a33785905d4 | -1.08146 | -53.6693 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 37fab3f8-e8ba-3b18-ba00-032e49423fb6 | -1.08098 | -53.67191 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8e93a6f-cd69-3c72-b78a-2bf0b7815f1d | -1.08086 | -53.67305 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9524f37-9517-325b-8acf-359b7c671906 | -1.07962 | -53.65371 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d79504a-3e39-3c12-b671-94205d439278 | -1.079 | -53.65762 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5c009fd5-4978-3d0e-b27e-756e50258a67 | -1.07839 | -53.66149 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d71f207-afab-3403-bbd5-ee08ed99236f | -1.07781 | -53.66517 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3800211-fc20-32c0-b724-d5fc209125a9 | -1.07723 | -53.66878 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d442491e-35b9-30ba-8377-ce2a66b780db | -1.07546 | -53.65282 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11063ef0-cee2-3f76-8ed2-46ecd4f10183 | -1.07066 | -53.65594 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d282140-20ee-3af8-8084-f24fa3595ee0 | -1.07002 | -53.66 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18795c45-7e26-3846-8d6c-e54e5a7f809e | -1.06582 | -53.65933 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df103ade-82b4-3671-9e18-6d0ef64d55c9 | -0.99508 | -53.69991 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fae2b6a2-8b41-3aec-a70a-4abb98d77668 | -0.99449 | -53.70374 | 2024-10-28 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b96d3689-07a6-3db7-8839-8db0cb296109 | -0.99147 | -53.69549 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README72.md)
