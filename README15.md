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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c20d5791-9d8a-3f9a-8bb3-161509882cb7 | -4.06103 | -47.11254 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eeecd13-2f8d-3f8f-8cc5-ff8a99d61756 | -3.91552 | -46.6576 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57097048-d29c-38c6-845f-ba7648d72736 | -2.67429 | -45.92229 | 2024-12-28 04:38:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efecc454-8758-33c3-8449-99f0d7e029ea | -3.96039 | -46.67128 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a21df386-b5d5-3253-9723-9e722fcf84ba | -3.70937 | -41.69593 | 2024-12-28 04:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dc2e3fcd-172e-3e76-ab03-28fea336f5d8 | -3.99229 | -46.71962 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 869ffee0-d092-3d2f-879a-805a95f3c98c | -6.19766 | -41.56828 | 2024-12-28 04:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2f08584d-cc46-326c-9c88-a567becd935e | -4.29735 | -46.5413 | 2024-12-28 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1f0d1b0-b4dd-33f1-98eb-0af52af013ac | -3.80636 | -46.73197 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b13df23-b4eb-33bb-b4b7-25bcf4f5f617 | -3.9569 | -46.67068 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6cd76b1-f051-3144-9d59-61de82276e20 | -3.90416 | -46.91294 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd201c00-3584-398c-8b02-3a43251b470a | -4.04235 | -46.71942 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fec4d9d-45f6-3a4a-82e9-62ebbf3ebcae | -3.12094 | -54.50413 | 2024-12-28 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b5069f1-410f-3673-a686-13771bf1adb0 | -3.98076 | -46.67842 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ed207a6-9188-3ac4-b7a3-ff32afa3b080 | -3.99659 | -46.34564 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cf87e6e-4cd6-341f-b0a3-1018536f9f83 | -3.97043 | -46.58192 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20463810-3caf-332b-9352-e972c362a37a | -3.8935 | -47.00352 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e53d88dd-3082-3a79-907b-857f6b7f763b | -3.90593 | -46.90166 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eecba162-6275-3e1f-a7ef-94ab216a1b33 | -3.95122 | -49.4467 | 2024-12-28 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 245c5507-2107-3e1d-98c6-3849e3230de1 | -5.31382 | -46.07103 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be8ccf35-6e76-3e36-b622-7d69c57668a2 | -5.83645 | -44.02029 | 2024-12-28 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7a8f410-efac-3754-b491-95b0ce51af72 | -5.90767 | -43.48349 | 2024-12-28 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88e9a3c1-9703-3a2a-b342-2250760e9de2 | -3.91166 | -46.91029 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c98225b8-2c12-39bf-84a8-87b3ee53a64f | -3.73224 | -47.18423 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 369dded4-91cc-3e1a-8ca7-fcb04c628c08 | -1.99873 | -45.58642 | 2024-12-28 04:38:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 835cd431-fa6d-34c6-8d7a-fae82499701e | -4.04874 | -46.72424 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d63aa71e-46e7-337e-a830-e53b13f0b497 | -4.05543 | -47.01225 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59fadb40-db19-3fd6-a018-780519b3aee9 | -3.90584 | -46.92484 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00da093d-ce27-37c3-9a6c-14d898ac7e02 | -4.08515 | -47.09347 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d4e9787f-c6f2-39d0-93ca-634676c5c0de | -4.11575 | -46.71445 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd29469b-ec49-38c5-8505-f6c3eedc2265 | -3.94896 | -49.44651 | 2024-12-28 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b18989b7-962c-30f4-b5df-5774a8ad119c | -3.90929 | -46.93595 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 268f6c43-2344-3bb6-97fc-d0ac3ae1b7ac | -3.89407 | -46.99984 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f07ab35f-e45b-3557-bc07-714ee0c5a957 | -5.92797 | -43.7783 | 2024-12-28 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82ad47ed-1b3b-310e-81e0-f92579211e92 | -3.73794 | -47.19264 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 70c1d5a0-32d6-3621-b980-49b069997c20 | -5.22148 | -41.23813 | 2024-12-28 04:38:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1c277f86-44f3-3b7f-92d3-c80a5a7f638b | -3.88919 | -46.68901 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8d8b793-373c-351d-bd02-0a8980c64f2b | -1.55472 | -53.50133 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4db111eb-8ceb-3c99-b6c1-3c83d1efdd43 | -4.02547 | -47.18297 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a81c803-b5c7-3218-bde6-e012a8a2b2d0 | -3.98945 | -46.69168 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fd9cc2b-0d09-3f23-9170-b0c0eda7b89b | -3.9781 | -46.55516 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bdb5bf6-aeb4-39ab-b273-a34b1a657081 | -4.11001 | -46.68213 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9747f704-3a5e-31f3-80f5-409944b38579 | -4.03929 | -47.04811 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aebb5acb-1a4f-3dca-bbda-14c480b6ebe4 | -3.818 | -46.72594 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82d6e95d-fd68-34a6-bf07-9da657995eeb | -2.216 | -53.64692 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28262f76-a7e4-307e-88e4-2fc5612dd6a3 | -3.7254 | -47.18316 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5cf2388-50de-34ae-b9b7-2ea0a666f13a | -1.71749 | -46.21237 | 2024-12-28 04:38:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2958e092-6a68-3a55-94f0-470695f4edb4 | -3.1935 | -45.99756 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eae41c88-3e45-3eab-9a58-e7516d1a3f4e | -3.18946 | -46.13092 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09d34b54-a863-318b-a39b-c1f0a68e5948 | -3.94952 | -46.62331 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6b402ac-be75-33a3-acf5-72679ebd10d0 | -3.99994 | -46.69325 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e4b96c3-e71a-375c-83ab-19fa40867401 | -3.91512 | -46.91084 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a94e9fe-5764-3bbe-8759-d54c2e2a4d0f | -3.89806 | -47.01946 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ac91491-5723-3658-8f23-767c54b5a8b7 | -6.21402 | -46.21896 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1456d47a-fbf5-3942-8ba3-2637e5906bca | -3.88328 | -46.95592 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00ad6c9e-3fa3-3676-a2d8-a2f5627d916c | -3.89927 | -46.98921 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94814de1-0cce-3424-be72-356a2afef7d0 | -2.48057 | -54.16867 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15ef1910-2dc8-313b-b439-1d14fdb0bfcc | -1.52301 | -53.8727 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 304f7622-68cc-3d87-95ed-cf7506ff497b | -2.3744 | -53.88181 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25a160dc-35a7-337c-8756-a3f5e7cfd841 | -4.04044 | -47.04066 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be7bd5ca-46b2-38cb-80bc-c3eda519677c | -3.77138 | -46.8196 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb9fc4f6-0c49-3946-a7f7-8c6fa76e952e | -3.87797 | -47.01252 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffb29229-e3e2-3354-9795-e645b7559979 | -4.01153 | -46.71077 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57e1cf72-a046-36c6-a51b-9e339f8ea3ff | -4.64003 | -43.96098 | 2024-12-28 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 459a7cc1-1449-38bb-ab78-713bd7645cdf | -3.76732 | -46.82286 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f12779f-cabf-3423-b419-ff1eab1a3e63 | -3.8183 | -46.05733 | 2024-12-28 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c7c7e75e-a087-3c52-90fa-81fb99a85840 | -3.72824 | -47.18738 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e622a06b-a575-3745-a760-d80617ab4162 | -3.9302 | -46.63229 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47e8c5f7-0e6d-30e2-810a-6183406d8ed9 | -4.07484 | -47.09181 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a44af8d7-dd6f-3198-b616-402b135842ca | -3.72882 | -47.18369 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8028e5b3-10d4-3d70-abcd-cbcf8afe045e | -4.06235 | -46.99039 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 97f655c5-dae1-37ac-9514-2a8741bf6744 | -4.10499 | -46.80692 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3032b98b-eb8f-3415-a47a-741ae8aa89ff | -4.0249 | -47.18666 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f3bfcec-cf5b-37f2-b3e4-c1558e6d4378 | -4.01735 | -46.55717 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ff8fb33-7e69-3430-b420-3a83810b6475 | -2.33337 | -45.80427 | 2024-12-28 04:38:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7862f512-f2b6-3df8-bf86-c4d439c09b08 | -5.31083 | -46.06618 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9670b107-6aad-338b-91df-3262d28e6690 | -3.81461 | -46.70193 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33499c04-04ff-3b72-afd9-79f4fd154d17 | -5.91198 | -43.48423 | 2024-12-28 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58eaa44e-8b78-3335-a2e9-e21879d164b6 | -5.31448 | -46.06671 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a50ebd62-50d2-375f-8523-ff3537990c3c | -4.11926 | -46.71492 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68797e83-ccb9-3bc0-9471-1e99e4479dd9 | -3.96388 | -46.67186 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b792df94-e4ec-3534-a692-ccd065956db4 | -3.99528 | -46.90683 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 338eac9c-1c53-3d12-8324-0599cd79b15d | -1.73754 | -45.66478 | 2024-12-28 04:38:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ca54dbb3-0141-37a0-9d71-132bff34d435 | -1.94493 | -53.34797 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03940a0f-eaf2-364c-ae69-c0b32f600bdb | -2.17255 | -45.40389 | 2024-12-28 04:38:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92084f30-a4a8-3cff-90ad-73a2fd0b826f | -3.96271 | -46.67955 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e277d8d1-5640-3a06-8db5-ecf2d172b7c4 | -3.94344 | -46.75893 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72e6bb81-4d03-3413-8758-ffaf7aef079d | -4.09914 | -46.82167 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b06b7150-6623-365b-9078-70ff191bf15b | -3.84116 | -47.04496 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e3da81c-bcd5-369f-aa37-36424dd4d744 | -3.90927 | -46.9823 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8dd0cc1d-8b05-3e77-b862-cf8336b7d994 | -2.96483 | -52.70227 | 2024-12-28 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e673984-7d26-3db3-baf5-c4e36cf2e083 | -3.97028 | -46.67683 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bbf3898-4462-3ec1-956f-970c5291e5b3 | -3.80072 | -46.85908 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 398291d6-fc8f-3f8a-ab77-4447469dea67 | -3.9071 | -46.89416 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e1063c8-19c3-36c2-b430-740c2d163316 | -3.92367 | -46.98058 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0cb5e748-84a7-3490-b46e-045a590dff82 | -4.44646 | -46.8331 | 2024-12-28 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bf53cf3-82b6-3d54-8372-c064a18d8247 | -5.98552 | -44.5993 | 2024-12-28 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 141762bc-6d1f-3494-b134-555ead8add23 | -3.84059 | -47.04867 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d374604d-6d5e-3a89-9c32-a9e2b0731d92 | -4.73484 | -44.65458 | 2024-12-28 04:38:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0214ed4-1758-3a38-bab3-cadc60163e99 | -3.83916 | -46.6892 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
