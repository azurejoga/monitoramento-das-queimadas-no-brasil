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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85eaface-8c3d-3479-a515-ae37b05699ad | 0.49991 | -60.59587 | 2026-09-25 06:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a14145cb-7845-350a-ae11-0bc8cb3f5558 | -1.14131 | -54.10477 | 2026-09-25 06:03:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 84e04cd0-512f-310d-a5e6-2e720d2b67b1 | -1.1502 | -54.09285 | 2026-09-25 06:03:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eabeb1ab-0b3f-360e-ab40-cab56b89d5ee | 0.49482 | -60.59224 | 2026-09-25 06:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 455ecc68-3310-3491-a74a-5d0e43756ece | 2.00854 | -61.09019 | 2026-09-25 06:03:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a9e18ac-ee82-32c0-aaab-629011ed5bed | 3.56205 | -61.16357 | 2026-09-25 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 923b789c-8fd5-38f8-a080-a18b9889fa3e | 2.00792 | -61.0864 | 2026-09-25 06:03:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3340229c-90bf-333b-bcb1-78ace5b66dcb | 1.62826 | -55.93979 | 2026-09-25 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b2744265-ca2e-3c51-9a99-187a982fe436 | 1.5872 | -55.83964 | 2026-09-25 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0e0ab6fb-6178-3043-bd22-01ad6066b67f | 1.59603 | -55.85578 | 2026-09-25 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc218e67-c33d-3667-a220-3c20d67c555c | -1.1439 | -54.09662 | 2026-09-25 06:03:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 44f3ce71-9af9-3dea-abec-6e04436b8016 | 1.58648 | -55.83529 | 2026-09-25 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a98218db-73fa-3a2c-97ac-3750dbaabd20 | 2.01209 | -61.08575 | 2026-09-25 06:03:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2b48426-0654-3d64-9d3a-0c91f1c3028b | 4.29034 | -60.72271 | 2026-09-25 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc018578-c013-3283-a29e-617244d71b0f | 4.28771 | -60.72255 | 2026-09-25 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47ea9a9d-9573-367e-96bf-d8dc2fc4c771 | 1.62898 | -55.94411 | 2026-09-25 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bc20a67-bb7b-35e5-bba0-e30f92381d65 | 3.55856 | -61.16761 | 2026-09-25 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4120243d-d2ac-3519-93d2-75cbab7c4906 | 1.58559 | -56.0126 | 2026-09-25 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31d83c8e-819b-3675-9988-28407c8167a6 | -1.21765 | -54.55847 | 2026-09-25 06:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4a3f4d5-34a6-39f0-8452-534aaa9c72a7 | -1.22008 | -54.55891 | 2026-09-25 06:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8dad27ac-886a-38c8-9fc5-9c6f8fd7c5f6 | -1.21655 | -54.56533 | 2026-09-25 06:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 417eab1f-b56b-3620-ba44-8627ddcc5c3e | -1.21231 | -54.5645 | 2026-09-25 06:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 798c62b8-536f-3639-8ca5-03d3cc0a7ab1 | -1.21903 | -54.56571 | 2026-09-25 06:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04b918f0-9b21-376e-aac4-45b478ed9eca | -8.66246 | -70.91594 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ab6e9b4-27f6-37fc-ac08-0b8cbd059d0b | -10.56273 | -59.49069 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4364977-f66b-33ae-adc3-0de51f3cc7f1 | -9.47035 | -67.07003 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f2f741d-3856-31ff-b12b-2fdbe43d1b45 | -9.21227 | -60.45925 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8b4baf6-5286-378c-91b1-01a127bf8230 | -8.95838 | -72.85428 | 2026-09-25 06:08:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f930c8d-87ac-3196-a81d-ca26548b520f | -10.56882 | -59.48773 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d708b9eb-1381-3a32-83c0-8deaef90a8db | -9.62602 | -62.3017 | 2026-09-25 06:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 803478ac-2534-3dc6-b22e-c08913f1e156 | -9.02722 | -60.52305 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13422f1c-1844-320a-a2fb-0923f4b377c4 | -9.02123 | -60.52858 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93f249d7-98cb-3d20-ac0a-13da29014060 | -10.56044 | -59.48813 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7abf535c-b9a0-320e-86f9-486c19e63df5 | -7.3582 | -72.46026 | 2026-09-25 06:08:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e57c846e-bcc7-3fa1-aab2-90326e9a8675 | -9.07969 | -61.43745 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bcec170-0500-33d2-ba23-0f401e404a12 | -9.02249 | -60.51934 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55d57afd-9cbf-35a0-9b63-709386d958cc | -9.02596 | -60.53222 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e69acaf-728e-3fc7-801d-b1d61601ec78 | -10.44762 | -69.30327 | 2026-09-25 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53fd885e-bf01-3bac-af7b-6fd515f1e4e8 | -8.0033 | -71.30584 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1a07cd9-546e-34fb-835e-33a464a7a5e7 | -7.9433 | -63.50241 | 2026-09-25 06:08:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20be110f-039d-3a55-be05-7cfe7c575623 | -7.67375 | -67.14345 | 2026-09-25 06:08:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e481c158-8a9c-3513-87ea-c992db009ffe | -7.6709 | -67.13927 | 2026-09-25 06:08:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e06ee3e1-af4d-304d-a161-53916eb3ca00 | -9.92928 | -60.71772 | 2026-09-25 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b49713e-e76b-36f3-bf60-0984f30b294c | -8.90698 | -71.34195 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d0b10e7-7263-373a-ac9c-28a364e67bb9 | -9.86424 | -65.19155 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cae63ef-766f-34ea-93a8-d162b4c21c25 | -9.58764 | -60.51846 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56e5aa79-7428-3599-bd55-ef16287f6b6e | -8.0356 | -71.26302 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b89e3b79-1a5e-3d5a-980d-227dd9027a50 | -8.90286 | -71.34522 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45d6d303-ebf9-3715-b416-bc1304508199 | -9.16885 | -60.78201 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 31697a1b-8e3d-3997-a4b3-c47c92e4c3be | -7.70721 | -67.03943 | 2026-09-25 06:08:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ff79cd4-9eae-306e-9c43-bb9a50dc6e68 | -9.54555 | -65.98306 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8a8a08b-9026-35de-a50b-7dc2bf9654e0 | -8.17893 | -64.04326 | 2026-09-25 06:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17d3d721-f631-3bd4-b74a-3d0855d8e75f | -7.86619 | -72.86549 | 2026-09-25 06:08:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cdcbd057-b53a-3ca3-99c1-65184d73175e | -6.99724 | -71.58592 | 2026-09-25 06:08:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55d5f252-25b3-3d9d-8c80-4d53f536e5c7 | -9.58245 | -60.51776 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14e4187c-9af2-3076-a2f2-5ad04e91fe11 | -10.59439 | -69.26893 | 2026-09-25 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42984e28-b551-3078-b759-3b65d6359ae4 | -9.93401 | -60.72148 | 2026-09-25 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf375301-c02c-3d9b-b5c9-55fe8f51ebbf | -6.92066 | -71.75394 | 2026-09-25 06:08:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa2f1dd6-d87e-3cb2-9940-25e8fe0ed3e3 | -9.03414 | -61.66323 | 2026-09-25 06:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e534665-98e3-327f-b7d3-bef9bcf302e5 | -7.9477 | -71.33829 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26851115-d9ba-3966-bc0b-8e52310a8dec | -9.15259 | -59.47692 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42d9f28d-5e68-3627-a20f-a9d872df02de | -9.46977 | -67.07383 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d228ac1d-4749-3b51-8654-d04d01647297 | -8.85144 | -71.35259 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b54d0b93-b82a-3f86-bc3d-352c3608f007 | -7.60527 | -69.89301 | 2026-09-25 06:08:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86e14a14-3ffa-3c09-8731-d35728607d72 | -10.98713 | -58.95784 | 2026-09-25 06:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f1d2bb8-16c3-3ea4-b82d-65add60d3c3c | -10.28261 | -60.53975 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a992057f-d2e2-3215-bac2-a00ee6957114 | -8.51296 | -71.39114 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85c9bb7b-8e76-3e24-a51c-ff2551dfccb0 | -9.49819 | -64.75178 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d308113-ba8e-368c-bb47-30dba7a8f181 | -11.56554 | -61.23802 | 2026-09-25 06:08:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88729322-e520-3298-836c-949177bdb12a | -9.58827 | -60.5183 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7a33b5a-de70-38dc-a190-73a1a6994181 | -10.5571 | -59.48992 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b997ca-3a17-3940-be9a-570263afe01f | -8.26484 | -70.80606 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63bbfdd9-f41a-354b-bda7-3e70d67eaaef | -9.38262 | -66.50759 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1c6f22e-bfc1-307b-bc12-864993b472ea | -9.15117 | -59.48758 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73c409b6-ad94-308c-b81c-4219aea35213 | -8.50945 | -71.39056 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e346c32b-8f4b-3121-a3ef-4369b7dfdbfa | -9.58309 | -60.51759 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1b7dc43-be58-3630-94d4-13c56c35323a | -8.02717 | -71.35832 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37b98526-fe8a-33b6-9e00-b4fd87e50d01 | -6.91703 | -71.75333 | 2026-09-25 06:08:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26b9c01b-753d-3307-9282-744fd4372fd3 | -9.22522 | -71.86267 | 2026-09-25 06:08:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72f3fa11-d2e9-3de1-8907-8ed6d8b8d57b | -10.56606 | -59.48892 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a88d8322-0077-3da8-a69e-c460717e0358 | -9.06748 | -65.70155 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9260e33-2e91-3180-b90e-3246ce048437 | -9.02637 | -60.52918 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5626d276-7f11-3c73-93bf-2a286c243994 | -9.11569 | -59.50111 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 500a3d29-ffc0-389c-ac7d-6e767f6318b0 | -9.57021 | -66.48602 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 830fe4d6-cdd0-387d-ade6-d279394f545a | -9.08452 | -61.43813 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9eac4449-73e1-3daa-9166-74993216f6bf | -10.98079 | -58.96098 | 2026-09-25 06:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56c61566-d0fc-3068-9987-0564eef66b6d | -12.14735 | -61.17432 | 2026-09-25 06:08:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc0958af-42a8-38d5-b69c-2e838497d474 | -9.38556 | -66.51215 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa78bb4c-e370-3343-86df-251d703108e0 | -10.28304 | -60.53655 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f6f60a3-d84e-35f8-b480-51380dcd15e7 | -9.21148 | -64.50644 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24845a1f-6556-3c47-87d1-9f1fa4add678 | -9.81641 | -65.06386 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87b7b529-1d6f-347d-9dfc-6e27ff00c85a | -7.66337 | -67.07471 | 2026-09-25 06:08:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73c39204-cbf3-3ae6-9913-560fe65b5c31 | -9.40097 | -65.90672 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9230d5b-51c4-36f1-946b-fcf89adc7626 | -9.72585 | -65.02901 | 2026-09-25 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63ffa29b-9eb2-3f69-b0e5-9f03777fa691 | -9.1739 | -60.78276 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e7a303d-8e04-3a47-b925-3295df2de9f7 | -10.55994 | -59.49192 | 2026-09-25 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9b7860d-5d05-37e7-9677-22bc2af7f9eb | -7.67431 | -67.13979 | 2026-09-25 06:08:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3d285fb-b47d-373e-aa9f-3a2c4dd6a18f | -6.9176 | -71.75191 | 2026-09-25 06:08:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acf8ac0a-df53-364f-8cd6-d50926ed12df | -8.95914 | -72.84977 | 2026-09-25 06:08:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa254c19-25b7-3efb-8dd7-99f81e57ea65 | -9.15907 | -59.4705 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README37.md)
