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
| f06bfcc5-7f93-3ceb-8950-c02b67d21d1a | -8.5138 | -63.8423 | 2026-09-08 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.3 |
| c2c5a18f-9980-33e9-8887-db1eef34ddac | -8.5137 | -63.8611 | 2026-09-08 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 074459e7-f0b7-3fa3-9ad6-c48fb9bee33c | -3.5407 | -48.1673 | 2026-09-08 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 191.6 |
| 934caba7-54a9-3908-9195-535aa35f750f | -6.6357 | -59.4459 | 2026-09-08 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 98c4cad3-3485-3545-849c-5a2bf024860f | -8.5323 | -63.8416 | 2026-09-08 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 93dd59a8-c391-3eaa-a0a2-b846e05f971e | -13.2859 | -61.7123 | 2026-09-08 00:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 39.9 |
| da1678cd-fa24-3511-8879-5d08efaeb789 | -3.5592 | -48.1666 | 2026-09-08 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| b65cdb97-f245-3df9-839f-b633ea108187 | -11.3525 | -45.7237 | 2026-09-08 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 15f79415-6ef8-34b7-a056-599149618745 | -11.3716 | -45.721 | 2026-09-08 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| e578f200-69c8-39bb-8ada-7f40fae21cbf | -3.5592 | -48.1666 | 2026-09-08 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 3456127b-0118-3dee-ae8c-9e9fd24c7c6e | -11.3904 | -45.7412 | 2026-09-08 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 0fc024aa-388a-33f4-9fbe-20af38b123cc | -8.5138 | -63.8423 | 2026-09-08 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.3 |
| c6565a28-8fe9-3994-9238-8bbe51552ee3 | -13.2479 | -61.7148 | 2026-09-08 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1c1be184-c8df-3ff5-9ffa-3281ceab06ac | -3.5406 | -48.1889 | 2026-09-08 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 220.5 |
| 647ad479-a734-32ff-aaa5-f93aa31a9b4b | -3.5407 | -48.1673 | 2026-09-08 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| e1099b54-9a76-3159-ac29-b952ea716f74 | -8.5323 | -63.8416 | 2026-09-08 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e65a1ddb-b5e4-38d5-9c99-8b967ce328c1 | -3.5591 | -48.1882 | 2026-09-08 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 309.4 |
| 98d07e6f-c48e-3561-a427-576770cd8c67 | -6.6357 | -59.4459 | 2026-09-08 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| aa03d709-699d-30cb-aef0-1fe7b8212afd | -8.5137 | -63.8611 | 2026-09-08 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 945cc898-c1dc-3da9-a715-f9fc33f02282 | -13.2289 | -61.7161 | 2026-09-08 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8142aeec-f26e-376c-89d8-c9cf2f4ac3be | -9.7702 | -43.4589 | 2026-09-08 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e61adfac-d775-3e93-9e36-16a1e51bf40a | -8.5322 | -63.8604 | 2026-09-08 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 1a759b53-fee8-357b-bfe7-28b70dade3f8 | -9.4769 | -40.3365 | 2026-09-08 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 0e1726db-c6e9-3f22-b105-babe239e90fd | -4.9794 | -50.6385 | 2026-09-08 01:08:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc51d063-bf14-36f2-9370-b1900185d9c5 | -13.2525 | -61.703098 | 2026-09-08 01:08:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f9029c09-b91d-3cdc-b2c5-c1dce92d1c3b | -5.9853 | -57.701698 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65521cf0-c814-3206-b788-4a13634d8a07 | -4.0396 | -50.884899 | 2026-09-08 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89e36d58-0f54-3fee-8c9e-e68d959d5d6e | -6.0147 | -57.695202 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50353048-ae6c-3ae9-84cb-74cc5af7d5ff | -15.64 | -54.1819 | 2026-09-08 01:08:00 | METOP-C | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f0914bd-583a-3906-a759-84650c8f19c5 | -13.2135 | -61.711102 | 2026-09-08 01:08:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 91082c8f-badf-3123-8c1d-9171d9768ab4 | -6.1147 | -57.635899 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cb10768-070e-3a8b-adb9-70f3ba788f22 | -13.233 | -61.7071 | 2026-09-08 01:08:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f42c105d-ad9e-32ca-9557-a4aae40b0e7c | -3.5497 | -48.201801 | 2026-09-08 01:08:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02361a9c-85ca-3222-98c9-0e960491089d | 4.145 | -61.225601 | 2026-09-08 01:08:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7564af27-01d0-3ee8-b7e1-77bce3985aee | -6.5095 | -58.291901 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 592d7951-123e-363b-bfee-a27a4fa07f00 | -8.526 | -63.864498 | 2026-09-08 01:08:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| beb430a7-2e53-32bb-9b54-d3f80a4ee110 | -4.4304 | -55.098598 | 2026-09-08 01:08:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7089e2cb-9b21-3234-8c18-4b683a990963 | -4.3703 | -47.783001 | 2026-09-08 01:08:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78a9954c-8a4d-3ae7-83db-87db3ec94999 | -3.3782 | -59.424599 | 2026-09-08 01:08:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d172cbe-1c0e-3e7e-8202-e5af5359d964 | -3.5548 | -48.180698 | 2026-09-08 01:08:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c530149-9751-3f52-b242-8482ede2d330 | -1.2008 | -55.719799 | 2026-09-08 01:08:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c882aed-80fb-34b3-b82d-333354602a2e | -4.0464 | -50.870499 | 2026-09-08 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74ee2013-ec64-344f-96e2-75bb329913c2 | -9.7639 | -43.463001 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52c95364-0798-3240-96a9-0f1c904ff611 | -3.5452 | -48.183102 | 2026-09-08 01:08:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba01e879-f7f7-3e21-b5b0-6ee2ee42a9de | -5.9445 | -51.700699 | 2026-09-08 01:08:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 579a4808-0505-32f4-8318-89b91e49a7ae | -1.704 | -55.173698 | 2026-09-08 01:08:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d49361c1-f012-3f34-94a3-6a557cbffbc1 | -9.7424 | -43.5354 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ac46740-a767-3c21-a7dc-bee9ccd06f2e | -9.7066 | -43.478802 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d53aceb4-dac9-39b8-924a-cc88995483ae | -1.5939 | -60.136902 | 2026-09-08 01:08:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a62c476-3b65-34e8-9f8d-d9119da21113 | -6.7713 | -58.956402 | 2026-09-08 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de96e510-5ac3-31c2-8d9e-d69e70def252 | -13.4257 | -43.823898 | 2026-09-08 01:08:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 615ade7f-0237-3001-8d87-4cd3860597f9 | -9.7352 | -43.470901 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48f23252-ec20-393d-b423-ddee5c2738d5 | -4.0493 | -50.882599 | 2026-09-08 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b68c0bf4-8828-344b-a284-d35560c16906 | -9.7257 | -43.473499 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89135ff2-478b-3ac3-968d-4ef957cbd953 | -4.3655 | -47.763599 | 2026-09-08 01:08:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 213288d5-72c2-3e3c-9b9b-7ebf00e96bf9 | -20.4939 | -57.417801 | 2026-09-08 01:08:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7f3c2da8-a4a0-3260-8f15-244906a3f4bf | -6.0568 | -57.790199 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3897b91c-f784-39fb-ba56-3ca420a24f64 | -4.3559 | -47.598499 | 2026-09-08 01:08:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13216534-60ea-3cd2-961c-b124dd6d1b68 | -9.734 | -43.504501 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d07dceb-968b-3082-8952-ae0b7deb4e8b | -6.0552 | -57.7831 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 621439d1-4128-3fdd-a0b0-39c4e91d0003 | -13.2261 | -61.723202 | 2026-09-08 01:08:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5562d7b2-4de1-34ec-bff4-84fecd3bfcc3 | -20.4958 | -57.4277 | 2026-09-08 01:08:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5ec79941-704d-3aa6-882b-b643d2dd3afc | -5.9901 | -57.723 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43053e8e-e8fb-30d4-a374-402a0f229629 | -3.4205 | -59.247799 | 2026-09-08 01:08:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad9b680-a9a2-303b-8da1-22206e7a87f8 | -10.7741 | -60.7822 | 2026-09-08 01:08:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ccc169a6-320b-3a99-8a25-8540a7530859 | -6.0245 | -57.693001 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccf497d0-09a1-3430-a2e6-a9fa1489c95d | -6.6333 | -59.445301 | 2026-09-08 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a2ea424-bd04-3ccd-8277-482a6f759fb8 | -5.9803 | -57.725201 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b474737a-8c59-34ea-a437-db17f6f0cc25 | -5.9935 | -57.692501 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c09d310-e226-3377-84d4-41a1afe4c317 | -8.519 | -63.831001 | 2026-09-08 01:08:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 85a31d39-bc1b-3cc9-a7a5-cff306d06fd0 | -13.2765 | -61.772499 | 2026-09-08 01:08:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f183fef-0026-3371-9ac0-a3422e85ae9a | -1.1991 | -55.712601 | 2026-09-08 01:08:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3911072-8386-3c47-8169-aec38827b8cd | -4.0661 | -56.2929 | 2026-09-08 01:08:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 485c4180-39c4-3ae2-b59e-21488aaaa1f6 | -9.7077 | -43.444901 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 00c8edc0-5059-33e7-91c1-e61ba9ae606a | -21.9799 | -56.054199 | 2026-09-08 01:08:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 654e2ca0-6da9-3ff2-a9bb-5dc7aee90ec7 | -6.7989 | -58.942101 | 2026-09-08 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bacaf095-c574-3197-856c-2c0aea9fd035 | -9.7245 | -43.507198 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aed818a8-228c-3d1f-b130-10e5eb50406b | -13.2428 | -61.705101 | 2026-09-08 01:08:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8e474dc5-fbbc-37f2-a288-2e646c400283 | -8.5357 | -63.8624 | 2026-09-08 01:08:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 755fc550-21dc-32fd-86b1-0f39b0647797 | -8.5322 | -63.8456 | 2026-09-08 01:08:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68efdb22-3892-3ef1-b57f-8fa935f2a5ec | -8.5225 | -63.847698 | 2026-09-08 01:08:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a900846f-f441-3d23-be49-11798d74640f | -3.5406 | -48.1642 | 2026-09-08 01:08:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 019ba7dc-4a49-364c-8932-360f32713e38 | -5.9885 | -57.7159 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d8e5640-b021-3aac-b947-758f7f5f8f5a | -9.7161 | -43.476101 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2ee4ecd-c81f-3709-b084-77b7134612ed | -9.7544 | -43.465599 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a889ee54-afed-3bea-9938-3e7c83f801a7 | -3.8845 | -55.817902 | 2026-09-08 01:08:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa5d322b-fb03-3fed-8796-b84328b8467b | -9.7088 | -43.4109 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d69c2097-99f7-36f7-ab42-6ac826b46ebc | -4.3558 | -47.7659 | 2026-09-08 01:08:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7465fd6-0e6c-3600-8064-f7baa398ddbe | -9.0845 | -58.9645 | 2026-09-08 01:08:00 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49facdb8-44b6-33e4-990c-a0f070eb1bc3 | -6.1131 | -57.628899 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9854aa21-cb34-3088-a5fd-01bfa9598fa8 | -6.6431 | -59.4431 | 2026-09-08 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae1db7d-ab3c-347f-afe8-001daeb73490 | -9.7436 | -43.5019 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8b7b9f5-8a2c-3845-9125-facb8c918d3c | -5.4926 | -48.1749 | 2026-09-08 01:08:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 15796df0-7d02-3284-a657-0f65acc06b9c | -4.3606 | -47.785301 | 2026-09-08 01:08:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd8c7616-997a-3ad7-a58f-896e571a2004 | -4.3463 | -47.6008 | 2026-09-08 01:08:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8e65009-7416-3fed-8360-02d281ea9d46 | -6.0131 | -57.688099 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3697799e-de73-306a-8352-64d8c9a18921 | -2.8419 | -53.987202 | 2026-09-08 01:08:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 229f2dee-3e36-3346-b25e-42caf8a8e96d | -6.1779 | -57.733501 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38d82bee-51d7-30d6-b299-fe8eaee70f78 | -1.1926 | -55.729301 | 2026-09-08 01:08:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8bf011-e186-3903-8603-5d25adb90f2a | -20.617399 | -58.004902 | 2026-09-08 01:08:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README6.md)
