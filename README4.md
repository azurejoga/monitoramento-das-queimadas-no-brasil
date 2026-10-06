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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b1ff190-50eb-3f6f-8d68-1f3d04799cb0 | -6.21372 | -57.76863 | 2026-10-06 00:18:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 150719a6-3695-37d0-8324-14e61f211e77 | -2.91597 | -54.12507 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| f375adb2-8621-32c7-940b-020e766d8ac8 | -3.07959 | -54.17094 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 714a9646-5bb1-3ff0-945a-54b3ca5223c6 | -3.85257 | -55.84735 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 619b8f0a-b9de-37d5-a806-b7d66286ce80 | -2.9361 | -54.14028 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 3859ce39-ec84-341c-bbb0-fbc696f6c08c | -3.60901 | -54.60397 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6f9c548e-4f0c-33e0-a7d2-ea1ef049c5c6 | -2.88059 | -54.13003 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 9633aa50-5b6f-3710-8cec-f0952bb38f67 | -2.55363 | -53.97381 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 394d24b0-43c6-3ba4-8a2d-2e45a557f41d | -4.45004 | -54.96748 | 2026-10-06 00:18:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3eb99721-f4e5-38e4-91b0-47963f28cb7c | -2.90129 | -54.01869 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 3d66fe2b-0503-34d3-82da-1b0264cd6139 | -3.16956 | -50.43697 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| a350f0b3-8d35-354c-9b44-2bd9791757fa | -2.79245 | -54.09442 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c7399da3-463a-3f4f-bf72-a2773851c5da | -4.00168 | -56.27186 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| beca347a-afb2-3fa1-9a84-1cce49606e56 | -3.06069 | -54.16459 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 74af4025-9b24-3776-a301-5e30a3acd90a | -2.9753 | -54.08374 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fc063a49-75a7-32bb-b02d-5f14d8f18654 | -2.97925 | -54.04706 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d5daf832-a9d6-36ef-9746-6307c96d3c08 | -3.0872 | -54.16085 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| b715a7ae-5bcc-3047-bc68-34cde0993d0e | -6.37325 | -55.15036 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 389f082b-5e5b-384b-af04-2992ae63d0fe | -6.18598 | -44.86722 | 2026-10-06 00:18:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 4bd07c7a-0e90-38c1-a3c5-0a0ff19ec2f9 | -5.99988 | -47.39212 | 2026-10-06 00:18:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 62e9674b-0553-3102-95d9-a49fee14363e | -2.55706 | -54.73465 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| a8dce195-31b6-3823-8a3d-9640b1550b99 | -3.09336 | -53.73695 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8504b7e0-b158-36af-aa30-c9fa8780f382 | -3.4959 | -49.89121 | 2026-10-06 00:18:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2cac5930-06a3-3a30-8e82-71778b4af413 | -3.09726 | -54.16847 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| b416fb91-c60f-3609-9a47-c890765655b9 | -2.94494 | -54.13903 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 16501466-00d7-3d0e-b5b7-261348eec339 | -6.71841 | -45.98257 | 2026-10-06 00:18:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 882eb9aa-1010-3fbc-9ef0-0688d09fa5b0 | -3.50944 | -54.61489 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cf08269c-2dbe-3625-a875-0e72140598ee | -3.04785 | -54.2177 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| fd78ce42-1954-33bf-9c3e-2c47d8197ac6 | -6.22655 | -51.82069 | 2026-10-06 00:18:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ccf1c1d0-a6c4-364c-bb04-889c00f3df25 | -5.82789 | -45.01617 | 2026-10-06 00:18:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 1800ed6c-45ec-3684-8991-448488e66176 | -8.70293 | -45.21079 | 2026-10-06 00:18:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 836f0630-0cac-3276-bbb5-114d1c25792a | -2.97775 | -54.10145 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d798563d-a09d-387d-89e3-f4f7631de735 | -4.0671 | -54.0465 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1e645de4-4800-32f8-be2a-f463f123030d | -2.77474 | -54.09689 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| cb492bac-2c90-39fa-9d16-7e9aa0ff2d1e | -2.9059 | -54.11747 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 81ac9d4a-3793-3160-a05d-cadea0dfa55e | -5.45145 | -45.51792 | 2026-10-06 00:18:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| be5f222b-228a-32ea-b1e3-2fc17d3c32db | -2.76184 | -54.66974 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 31f637ce-bb08-32de-996a-ed6c0d644280 | -2.95742 | -51.04607 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1ab80cf4-0b0b-3fe2-843d-1027db0baf73 | -3.62783 | -55.28163 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 3420b031-377c-3876-aa7d-aa28c8b4cec6 | -6.21401 | -55.67897 | 2026-10-06 00:18:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b9ba0c74-ebc0-3e48-a01a-c823d61732eb | -3.12525 | -53.70499 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| e3568dc7-d21a-37b5-aa83-26f8a9a64bc2 | -3.23201 | -53.87533 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dccbe0e7-fef1-3f4c-9f2f-9978c66d752a | -3.12506 | -53.76908 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5cf9925-6722-3651-b679-c504b574a7c9 | -5.84371 | -45.01391 | 2026-10-06 00:18:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 214.1 |
| 31c11bab-2883-3de2-9eea-3cbe05245fa1 | -3.70974 | -58.92752 | 2026-10-06 00:18:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 46123d11-6dcd-3f39-b208-9e90ce87fdff | -3.28251 | -54.17522 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1a5c29b4-4d3f-3ee5-b56e-4ae7f6830b2b | -3.14814 | -50.44032 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d6351e32-e9e8-3543-92e6-0cbb0d7b09de | -2.90713 | -54.12632 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ae9289d5-fa76-3052-840e-161fa2cbbb2c | -3.15991 | -50.60013 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 92a02803-ea82-391a-8826-0a0b459f5708 | -2.87664 | -54.16661 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f6ef278c-934a-335b-a75e-c65002b1efa7 | -3.08959 | -53.70997 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1537ead7-4834-33b7-a199-da8d02cf115b | -3.22513 | -54.29731 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1078e7fd-11b4-3c2e-91ac-c687af993a3e | -3.09211 | -53.72797 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 61632eb6-873c-30c8-b178-1372d4eaf238 | -2.88208 | -54.07565 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 42d40f7e-7c18-3b35-af00-96c5b049896f | -2.80742 | -54.13745 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| aa3db77b-0375-3152-bd4c-57aaaecaa73e | -6.21139 | -57.77566 | 2026-10-06 00:18:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 84d1f0f1-2213-34c6-be54-fa50442b026b | -2.91353 | -54.10736 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 75d808a8-3f51-3860-abdf-1a011cf633b9 | -4.72248 | -44.09378 | 2026-10-06 00:18:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 7043c97d-690c-3b45-a62d-3ca3bfdc8e11 | -3.22634 | -54.3061 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 7a0ec28b-dd92-3eff-998b-455dc128011a | -4.0595 | -54.05656 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b192669c-7539-3f64-8b57-f984165d7dfd | -3.90448 | -52.16425 | 2026-10-06 00:18:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dca61d87-accc-37cc-9bdb-1f30b28260c6 | -2.93853 | -54.15796 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3c37f255-7fa3-3cda-bccd-c678566eeac7 | -5.67754 | -53.50176 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 2949a8a2-8c1b-3350-afec-895cf07121bc | -3.66636 | -54.28551 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0917890b-a9c6-35fd-917d-947d0474049f | -2.87541 | -54.15775 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| a897da0e-76ee-3309-9f3f-1e119b6ae075 | -2.78236 | -54.08679 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 1a87201c-a3fe-3065-bffb-8f2047024e9b | -3.27612 | -54.19413 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c6c64ce8-5b29-3bbe-bec9-8c8eee42efb5 | -3.54375 | -59.49879 | 2026-10-06 00:18:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ebc96b57-d9a8-3524-bea8-fad9583b0e8f | -3.67377 | -54.53497 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1d598d82-3d75-3ebe-ae62-6c21a0e3d3e3 | -2.96006 | -54.10393 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4f524767-4c01-3078-ae1c-995eb5925a7d | -3.68213 | -55.94924 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 217.8 |
| bd816074-9631-3303-90e3-c0ff56b3c0a2 | -2.84435 | -54.07811 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8cf432e1-6018-33c0-bef2-07f9f44fc478 | -5.8343 | -45.02043 | 2026-10-06 00:18:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 164.8 |
| c320ad7c-0854-3861-9d75-7636732d3dfb | -3.33633 | -59.49274 | 2026-10-06 00:18:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ca50ef09-5141-3583-afcf-ec949ce06c63 | -3.6078 | -54.5952 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fc6bfa9e-c301-317a-8f4e-0e06b7fee0d9 | -2.99149 | -54.13559 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fc4d624d-d5d1-3345-a1aa-66494e3154a9 | -3.16076 | -50.45219 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c5848075-59b2-38be-a722-6aec665d85b4 | -2.577 | -56.15284 | 2026-10-06 00:18:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bf72edac-565e-390d-8c80-276f25a175c3 | -3.16175 | -50.6131 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 70b7bb8d-c2b8-3137-90b6-74fdbc3152f6 | -3.08598 | -54.15202 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 100575af-9882-3906-9532-bed28e45df87 | -3.38038 | -58.20075 | 2026-10-06 00:18:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 229.4 |
| c9f00eff-cda0-36ba-b4c9-ab3c35110d3e | -6.21274 | -55.6694 | 2026-10-06 00:18:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| fd724c06-b98e-3bd6-ad3a-c8afd80d1456 | -3.70746 | -58.93414 | 2026-10-06 00:18:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 5e697af6-6eb9-3c4f-ba0f-9ca997d071ba | -3.07836 | -54.16209 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| bcb8ded2-6578-3650-832e-d995057403b8 | -2.87936 | -54.12118 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1f51b9ed-3ba9-32b9-8833-7fa7ce3cce7f | -4.00298 | -56.28155 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3d68b585-b655-35e6-99dc-6ef0c6dc0ffd | -2.77351 | -54.08804 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| dd3b824c-4339-34c1-bedb-908b6af0edd8 | -2.93488 | -54.13144 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c02eb54e-739f-3c9a-8aee-6b638a5b130e | -3.58677 | -54.31189 | 2026-10-06 00:18:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| b7d56e43-4e65-3aad-a20a-1049c03e9541 | -2.77692 | -57.67342 | 2026-10-06 00:18:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| f324206f-1e43-352a-89bc-0e6df3ee7fea | -3.54173 | -59.48365 | 2026-10-06 00:18:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 80c76e84-7591-33a3-8fed-5069dbf01c84 | -2.78359 | -54.09565 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 3828b116-4dc6-3584-9645-894c632398e7 | -3.11492 | -53.76137 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 686a490b-ab09-3047-be5a-4c9bae65a3c2 | -4.14789 | -54.02885 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e66e20d7-9127-3deb-a157-c48caf2a4d5b | -2.90101 | -54.08203 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e59abec2-4e60-366b-a944-1a46b4100b32 | -3.06953 | -54.16335 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c2141d3d-097d-3d5c-a4d8-538eb25dd692 | -3.6937 | -55.96661 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e5c1e327-95e7-3fdb-8ec4-1995dbc57f7a | -2.76862 | -57.68576 | 2026-10-06 00:18:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1db43c17-7a42-3408-b5d3-a6366ba66bbd | -2.92847 | -54.15036 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9e6b50fe-a619-3f5f-b02c-33eb9b19f332 | -4.06608 | -56.33169 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |


[Clique aqui para ver as próximas entradas](README5.md)
