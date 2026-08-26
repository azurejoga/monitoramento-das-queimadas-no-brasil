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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d288b3e1-5975-3897-9b68-15a8f8bcab7e | -4.8002 | -43.1709 | 2026-08-26 12:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 270.9 |
| 6baecb3d-779d-33e2-8297-97a5cd25bcd7 | -8.1484 | -47.4998 | 2026-08-26 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 2c1c4f30-63d0-3de1-b361-26b4f1ddf35e | -9.5936 | -49.278 | 2026-08-26 12:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 2497c969-963a-3de4-832f-9967b841e923 | -12.6452 | -48.4168 | 2026-08-26 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 9e5631e6-9de0-35d0-b378-a619a2653205 | -8.1482 | -47.5218 | 2026-08-26 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 1be8ac4c-ba32-30f7-af7d-3e61de400b9d | -7.385 | -55.1523 | 2026-08-26 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d38c9978-6b54-3c51-99b5-ff37a83156f0 | -11.4298 | -44.5615 | 2026-08-26 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 5f347466-b513-3718-aafb-f9db5596fff5 | -6.2676 | -53.3768 | 2026-08-26 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c541ffc1-074e-398c-a3f2-5bffe59f0d7b | -10.5596 | -50.4449 | 2026-08-26 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f216ca64-b286-36d2-8505-66edd3a98bff | -8.1857 | -54.9435 | 2026-08-26 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e8646ad7-cfc4-306c-92b4-4dd28232cbd2 | -12.6836 | -48.4116 | 2026-08-26 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 79abe9b2-c918-3e0c-b6bc-d421e43012c0 | -7.6461 | -47.1258 | 2026-08-26 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 1337e8d0-3fb3-30ed-b138-712e8194a67f | -13.6614 | -51.8535 | 2026-08-26 12:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ea96858d-e1fa-3fcc-a12d-8112b0f485f8 | -13.6617 | -51.8323 | 2026-08-26 12:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 5138a143-d7ff-3302-9da1-bd0b5a50aba5 | -8.0733 | -47.5066 | 2026-08-26 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1374646d-620b-312c-9ff9-3cd025240300 | -9.7249 | -49.3296 | 2026-08-26 12:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 989e66fd-c5dd-3f03-817b-21cda43ab601 | -14.3179 | -51.726 | 2026-08-26 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| e536a8a9-408b-39db-bb32-1d51837d39e5 | -4.8004 | -43.1476 | 2026-08-26 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dd5a8f8c-7642-3212-b81f-e57dd2ab8397 | -12.6832 | -48.4337 | 2026-08-26 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| ae8f728b-d9d8-329a-af49-b251886e565a | -7.385 | -55.1523 | 2026-08-26 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| b3b2541b-c495-31d1-afc4-4b2c590c35b7 | -11.4298 | -44.5615 | 2026-08-26 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 92458e7b-ef96-35bf-ac0f-77ffd5ab21d7 | -12.6452 | -48.4168 | 2026-08-26 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 6d6e636f-0c9a-3928-9776-9c82e661a3a3 | -13.2095 | -51.3356 | 2026-08-26 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.2 |
| ef48c439-d568-3f2a-99a7-2ac8b5d463b3 | -10.5596 | -50.4449 | 2026-08-26 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 99e87415-591f-3780-8962-6e748b820b2a | -9.9506 | -46.6251 | 2026-08-26 13:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 48477b3f-0ff1-3d80-bed6-bc4b49b46d9e | -12.6836 | -48.4116 | 2026-08-26 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 3c91f972-f842-371e-93b4-bdb60dcb4866 | -8.1484 | -47.4998 | 2026-08-26 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 09e81a23-c580-3448-8be4-b4e407738a76 | -8.1482 | -47.5218 | 2026-08-26 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 1b251406-d8be-3e7d-9942-8feb6ad66507 | -8.8187 | -49.6093 | 2026-08-26 13:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d72b1b3c-a735-364e-9c47-27e4c6b67e54 | -13.2664 | -51.3711 | 2026-08-26 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 88e0859d-8161-3cba-9078-dfd4d2a7e9e4 | -4.8002 | -43.1709 | 2026-08-26 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 736d5542-f0ee-38c5-a41e-4f3d41f1fc36 | -10.7784 | -54.0368 | 2026-08-26 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b3169809-6ed4-3988-8be7-455cb69cf5e2 | -8.9421 | -45.7253 | 2026-08-26 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 90b73d2c-021b-389b-a88b-e3ee9937cff7 | -9.7249 | -49.3296 | 2026-08-26 13:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| a5136955-f469-347c-bf9d-d84f46d15d24 | -10.7596 | -54.0384 | 2026-08-26 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 6b8c1fbb-a5db-3b02-a674-4a368278ba15 | -7.6461 | -47.1258 | 2026-08-26 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1b318f85-03b8-3c09-bad2-2fa1866ef09b | -11.411 | -44.541 | 2026-08-26 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| eef3302a-b35f-32d6-a0b3-67fd7ac37641 | -13.2661 | -51.3925 | 2026-08-26 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 75f95397-69df-3e85-8578-708afe985d5d | -9.5748 | -49.2799 | 2026-08-26 13:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 36c7b9d5-1d56-3bac-af32-a7cdaa747d88 | -8.9418 | -45.748 | 2026-08-26 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 1031d4b0-df3b-30ee-a377-120cd7033f3e | -12.6644 | -48.4142 | 2026-08-26 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 460edff8-c28b-3f6b-b553-f93bd9414f0d | -14.3179 | -51.726 | 2026-08-26 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d1f6ef4b-ef4d-33e6-8ed3-e1b225f41645 | -13.264 | -51.5205 | 2026-08-26 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 407ae296-801b-3ce0-9812-fad35da57620 | -11.411 | -44.541 | 2026-08-26 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 88ed1d27-c065-3503-a9d3-b1738edd0366 | -10.7784 | -54.0368 | 2026-08-26 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 5faa220a-cd55-3cf6-994c-a45be1f64926 | -14.3179 | -51.726 | 2026-08-26 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| b9f1fd22-a776-3b6c-ad93-39ee9607afbe | -13.264 | -51.5205 | 2026-08-26 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d7830b4c-f0c0-3dd8-9c6b-45adf23db418 | -7.385 | -55.1523 | 2026-08-26 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 3dd73cad-139b-3981-b254-d9516f05e9be | -8.9418 | -45.748 | 2026-08-26 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a9f2ff29-b2d5-3df2-a9f5-363a39415a66 | -12.6836 | -48.4116 | 2026-08-26 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 39ea1099-ce6d-3608-9615-17e976330ed7 | -9.5748 | -49.2799 | 2026-08-26 13:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 2cc72255-39bd-339e-851e-b02ecc2c725f | -8.8187 | -49.6093 | 2026-08-26 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0cdf6ad7-67b7-3834-8ecb-d9740c36b867 | -10.7598 | -54.0179 | 2026-08-26 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 2955d256-4d57-36f5-bfbf-667b14f05ea4 | -11.4306 | -44.5148 | 2026-08-26 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9c179c9f-6fe7-3cce-b209-9fd3e8f80491 | -9.7249 | -49.3296 | 2026-08-26 13:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 117a826a-d193-36ce-96e2-9e80e7a1b98c | -8.1484 | -47.4998 | 2026-08-26 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| d2f937f2-393f-35d4-920c-d8b63107293d | -10.5596 | -50.4449 | 2026-08-26 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| ae203c4b-e655-3e32-ab12-9719d4593594 | -12.6644 | -48.4142 | 2026-08-26 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 7d1a7413-120e-3bd8-b0f7-1bd15cb78122 | -7.6461 | -47.1258 | 2026-08-26 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 222.5 |
| dde7ae89-f77d-3e65-8971-44a07223c83a | -8.1482 | -47.5218 | 2026-08-26 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 3d41285e-a6a8-390a-9ef6-52f070ccfa98 | -10.7596 | -54.0384 | 2026-08-26 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 854e4d3c-770e-3981-9ca8-02dcbaecbcfe | -13.6617 | -51.8323 | 2026-08-26 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 79d7133b-f6d8-3f4c-8770-c8b9d2ab7cf6 | -12.6452 | -48.4168 | 2026-08-26 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| ffa69191-098d-3051-b7b2-c3e60eb04903 | -8.1294 | -47.5235 | 2026-08-26 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 96d0fa81-6576-3e7b-9dfc-01d6f58dc4c5 | -11.7544 | -54.5414 | 2026-08-26 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 3f4e77a5-f988-329b-a92c-d49d556d7577 | -4.8002 | -43.1709 | 2026-08-26 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 6621a3ae-dd30-3657-b465-76ec5270e576 | -8.1484 | -47.4998 | 2026-08-26 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e8524ca8-6c75-392b-a22f-21f5875e4c6d | -7.385 | -55.1523 | 2026-08-26 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 27341030-56c6-3cf9-940b-215c548f8def | -11.7357 | -54.5227 | 2026-08-26 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 25b31aa1-5983-3504-8195-60d6b72e868e | -10.7784 | -54.0368 | 2026-08-26 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b51627e1-1864-3a1e-b2e8-493368429b83 | -12.6456 | -48.3947 | 2026-08-26 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f34b06a9-81c4-35be-a81f-f2ceba8f18b6 | -13.2643 | -51.4992 | 2026-08-26 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 94bf2e55-4cbd-3658-98b0-acb534c7d8d3 | -14.3175 | -51.7474 | 2026-08-26 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 2356d8d7-60ef-3333-aee3-71d79e6d9307 | -7.6649 | -47.1242 | 2026-08-26 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| aaef4508-ac88-3610-9d07-e6363cfb636e | -4.8002 | -43.1709 | 2026-08-26 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 00af296e-864e-3c27-b619-666cc7925520 | -13.2448 | -51.5229 | 2026-08-26 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 57186a91-da57-343a-a855-51717a7dae3d | -11.7354 | -54.5431 | 2026-08-26 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| f4476c5e-3ea6-30e0-a4ec-5424195beefc | -10.7598 | -54.0179 | 2026-08-26 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| a62fc997-51b6-31a6-bc99-307662b0a8b7 | -9.9506 | -46.6251 | 2026-08-26 13:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f149b0ca-cb43-3801-8a80-04f8f4ca4a8f | -4.8004 | -43.1476 | 2026-08-26 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 9aca25d3-23ba-36b7-a5ea-fd6986c53b52 | -9.5748 | -49.2799 | 2026-08-26 13:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 2773d155-67f2-3f46-b8df-527b710141c5 | -11.7544 | -54.5414 | 2026-08-26 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 270.4 |
| 29114b6e-e37b-36d8-a5b7-28a35edff20e | -9.5936 | -49.278 | 2026-08-26 13:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| cf0edaba-a67a-36e5-afbe-e1dc61236f3f | -10.7596 | -54.0384 | 2026-08-26 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 176.9 |
| b8823a25-38bb-3944-9a7f-84961f8ccbeb | -14.3368 | -51.7448 | 2026-08-26 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 225.5 |
| 66a021d9-90a7-3482-89ae-e935e7124fac | -8.7584 | -49.9566 | 2026-08-26 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 34326bcf-b24c-3cb6-85a4-3ae97c022480 | -7.6461 | -47.1258 | 2026-08-26 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 211.5 |
| fa19bb4c-27ba-3256-9433-58369cca2ac5 | -9.7249 | -49.3296 | 2026-08-26 13:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 8d5a5d27-d8c1-3d13-8620-43f872448748 | -13.264 | -51.5205 | 2026-08-26 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 263.3 |
| 64a93ddb-b8d9-3ccb-ab9c-1c5d2d94a865 | -8.1482 | -47.5218 | 2026-08-26 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 149.1 |
| ff25d848-71cd-3318-bf78-968a2ac5e68a | -11.7546 | -54.5209 | 2026-08-26 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 261.9 |
| 952292f8-ed2a-36e1-be91-a6d63579f569 | -8.8187 | -49.6093 | 2026-08-26 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 2c3469d2-8a8b-3201-a8a6-247d862060c9 | -8.9418 | -45.748 | 2026-08-26 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 0bdd3493-d6c7-3c55-8b44-c1b03ac45279 | -14.3179 | -51.726 | 2026-08-26 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 3652018a-83f9-3a60-bacb-ccdad935e437 | -13.8579 | -53.9928 | 2026-08-26 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 634e2ba8-5101-3b42-abe8-d9bb75875178 | -6.2676 | -53.3768 | 2026-08-26 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| dc041f9f-0473-33a2-99e7-f21afc40f197 | -3.2178 | -61.2362 | 2026-08-26 13:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 2717560a-15b1-3ddd-b06f-219f9de849f4 | -12.6836 | -48.4116 | 2026-08-26 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 26fcde36-29da-3c04-82b4-703d6582b1ff | -9.6024 | -55.1078 | 2026-08-26 13:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 0174e167-af95-3f9b-8afd-496faf58dec2 | -12.6452 | -48.4168 | 2026-08-26 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |


[Clique aqui para ver as próximas entradas](README81.md)
