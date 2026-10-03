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
| 3e23e892-4a5c-371b-8e03-eb982cbd5607 | -9.0987 | -65.3783 | 2026-10-03 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| e413ae8b-d4f3-3f32-8588-9f032a09c789 | -8.6665 | -66.936 | 2026-10-03 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| b00b2c7e-fb15-339a-bef1-44162d721e87 | -9.7499 | -65.075 | 2026-10-03 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| a02aea5e-948c-30d3-b2a6-8c123affb167 | 1.7583 | -50.8232 | 2026-10-03 15:40:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 6f354bb8-e325-3a14-9959-cd06eb53793b | -9.8989 | -65.032 | 2026-10-03 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.0 |
| d532f5f8-3eac-3fdd-b7ef-caa1fbdd5a72 | 1.8037 | -55.6051 | 2026-10-03 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a5245b5d-04de-3709-b645-c0c5f57d54f3 | -12.1383 | -63.1879 | 2026-10-03 15:40:00 | GOES-19 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| dd4b3fef-13cc-3726-86a8-425b5d487b52 | -9.0045 | -65.7174 | 2026-10-03 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e474ac75-fb20-3bb2-9204-200ba68e9db0 | 1.8692 | -50.6753 | 2026-10-03 15:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 63.5 |
| acb6e4c3-08db-38f9-a91d-8bc655be56f4 | -8.852 | -66.7827 | 2026-10-03 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 91c7fd54-567f-3729-a4cd-77ede26fea8d | -13.5007 | -61.1333 | 2026-10-03 15:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 44def660-f3e8-3047-840b-279aa0ce5906 | 1.4268 | -50.7866 | 2026-10-03 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 33c0c36f-a987-3323-8ab0-7dd0faea7c60 | 1.8037 | -55.6249 | 2026-10-03 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 6a03da82-c5ac-34c4-afc6-d5d155cfc297 | 1.8319 | -50.8427 | 2026-10-03 15:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 659846cd-ecda-38c5-8690-b129d24b4340 | -9.9174 | -65.0501 | 2026-10-03 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 63487330-6e9b-3c2e-ba6b-3c49e367e6fc | 2.0138 | -61.0826 | 2026-10-03 15:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 96.7 |
| e0682521-912a-38d9-950f-3c1b4a861c20 | -9.7498 | -65.0938 | 2026-10-03 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9062c773-ce14-3a3d-b6fe-770ac9b292e7 | -9.0046 | -65.6988 | 2026-10-03 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 234.1 |
| b5b75acb-9612-3af2-ab4b-b4ebabd52660 | -9.0045 | -65.7174 | 2026-10-03 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d9d2a3ef-a618-3a9a-a40f-d871cf68a9bf | -9.0584 | -66.1073 | 2026-10-03 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 049af709-8101-3dc9-96b0-865480ea37a6 | -8.852 | -66.7827 | 2026-10-03 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2e25ef16-e859-3e09-8c2c-7ed88e9203af | 2.0138 | -61.0826 | 2026-10-03 15:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 95d0fd90-1969-37ec-bb1d-e5117c9e1667 | -9.7498 | -65.0938 | 2026-10-03 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3a5a553a-f355-30c9-9c0a-1f01864c3c29 | -9.9174 | -65.0501 | 2026-10-03 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 189.0 |
| b11d8cdf-3ce3-39d6-8eb2-ab6289369c59 | 1.7854 | -55.6054 | 2026-10-03 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| c6350033-58c1-3821-922d-f0d07c31f02a | 1.8038 | -55.5656 | 2026-10-03 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 8118e16a-6460-3d85-92a0-d4c4822d0b24 | -8.8705 | -66.7822 | 2026-10-03 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ad92cca4-0279-3a7a-a83d-a0a6c8228d0e | 1.9608 | -50.8612 | 2026-10-03 15:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 89.3 |
| cb7300d1-1d3b-39cf-8ddb-4d1a77838e98 | -8.9195 | -64.1473 | 2026-10-03 15:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 02a27357-5624-3143-a5c8-a348576d71f5 | -9.4565 | -64.3344 | 2026-10-03 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 04762d4b-1052-3fa3-a3e6-901d1893d107 | -8.6665 | -66.936 | 2026-10-03 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0105a5a3-8a8b-314f-921b-74fb081ad0df | -8.648 | -66.9365 | 2026-10-03 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 3eda6064-7fa5-3153-b4db-1add2b5674cc | -9.8989 | -65.032 | 2026-10-03 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 28d72ea6-35c5-31bb-8d53-557da7afebdd | 1.9317 | -55.7416 | 2026-10-03 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 5b94b0f5-8a2c-33d7-8e68-95b19524efa4 | 1.8319 | -50.8427 | 2026-10-03 15:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 400b269d-cbb2-340a-aab2-d0f0b61db062 | 1.9132 | -55.8011 | 2026-10-03 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 181d0b66-263f-3854-8c6f-ee0b26566d2b | 1.9316 | -55.7614 | 2026-10-03 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 290ee9f5-a298-310c-8938-cf3c903109fc | -9.7499 | -65.075 | 2026-10-03 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 125.9 |
| ddad52c0-afdb-38d3-bb61-201a19cb4bfd | 1.9133 | -55.7813 | 2026-10-03 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 02063695-f320-3462-839e-b70ae7c3e929 | -9.0046 | -65.6988 | 2026-10-03 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 144.4 |
| f94b48ff-a335-309b-b0c9-c47f30e39dda | 1.8037 | -55.6051 | 2026-10-03 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 909046ff-d188-329d-9b35-f05c16722cb9 | 1.7583 | -50.8232 | 2026-10-03 15:50:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 2ad38a9b-ce49-3de3-a84e-8e57f61703e1 | 1.9317 | -55.7416 | 2026-10-03 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 592864c8-04fd-37f1-93bd-b33fe00952e7 | 1.9316 | -55.7614 | 2026-10-03 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| bc1c21b6-839f-3303-ba5f-900d670be7a0 | -9.8989 | -65.032 | 2026-10-03 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 0bb88c74-99ec-3da3-94dd-f58d1d13da3a | -8.5554 | -66.9945 | 2026-10-03 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 86afb45e-8885-3e97-ab66-6bfb4779c570 | -9.7498 | -65.0938 | 2026-10-03 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 9e4c3b88-da0a-3ab5-b044-06cb29480f91 | -9.9174 | -65.0501 | 2026-10-03 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 317.5 |
| 29524320-ff42-385a-b6e4-cbcb426a095c | -9.0584 | -66.1073 | 2026-10-03 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 66e13fe8-7568-3296-83fd-8d8ce1554a03 | 1.9132 | -55.8011 | 2026-10-03 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 76f98a26-3801-315b-bf65-dbfd39c737c3 | -9.4819 | -66.7836 | 2026-10-03 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 36497408-c3b4-38b4-9850-226ad149a759 | -11.8814 | -64.9323 | 2026-10-03 16:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 76f35194-6581-3353-a2c4-e7f27f3d4482 | -9.3764 | -65.4813 | 2026-10-03 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 843d5f9d-7693-35ff-a4b7-f357339553c4 | 1.9608 | -50.8612 | 2026-10-03 16:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 90.1 |
| d78b2a85-4fcb-34c2-8b2b-6e0775724b15 | -8.8886 | -66.893 | 2026-10-03 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 7ef6e05b-cadf-3660-9c32-f33751f03ca1 | -8.9195 | -64.1473 | 2026-10-03 16:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| bbe03266-0a93-3e5b-9a2a-ec323c11c061 | 1.9133 | -55.7813 | 2026-10-03 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| ab2a9751-d9d9-3f1e-b82a-e5d2ecd6ca4c | -9.0045 | -65.7174 | 2026-10-03 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 1e38a841-3f3a-3417-a5a1-00340576ce5f | -8.5554 | -66.9945 | 2026-10-03 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2310bbca-7568-3462-8a84-6613786d8d14 | -9.8061 | -64.9979 | 2026-10-03 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 74832333-5607-3a28-ac1f-03b5663c2b64 | -8.8706 | -66.7636 | 2026-10-03 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 4b381f1c-b04f-3e53-b24c-b72208f8520f | -8.6476 | -67.0292 | 2026-10-03 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| cbcedcdb-3116-334d-b7d7-c9ce0c952fc9 | -9.4819 | -66.7836 | 2026-10-03 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 617accee-fc45-302e-8db6-802872f6fb08 | -8.852 | -66.7827 | 2026-10-03 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| c5608afd-c83c-32b2-8fd7-7c19e37778f6 | -9.3765 | -65.4626 | 2026-10-03 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 264de4ba-789b-3972-acd9-3361a1c87111 | -9.7319 | -64.9631 | 2026-10-03 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 622b9882-574a-3424-8dd6-410b60cdf84d | -8.8705 | -66.7822 | 2026-10-03 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d6de1c60-f29d-3180-840d-40b20594f13a | -9.1147 | -65.9379 | 2026-10-03 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| d0a8585c-ae82-303e-a771-41beb521d490 | -9.077 | -66.0881 | 2026-10-03 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 037d912d-7820-3ecb-8065-271ac8675437 | -8.8886 | -66.8745 | 2026-10-03 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| ff923ad0-714f-30a7-ac3b-87adc26d833c | -8.8886 | -66.893 | 2026-10-03 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c155daa5-0b85-3059-bf13-7119e04f4f92 | -2.82 | -54.09 | 2026-10-03 16:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1aecc3-ee7c-3cbe-b1e9-a312958ab9df | -3.14 | -53.75 | 2026-10-03 16:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8107aac-4fa2-3461-aaf6-3b5c49af4574 | -2.82 | -54.15 | 2026-10-03 16:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8897d215-0bcb-377c-8d10-a48c1e014869 | -3.11 | -53.75 | 2026-10-03 16:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0c0aae6-8b1e-3c15-934f-17033e111fb3 | -2.79 | -54.09 | 2026-10-03 16:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c3fda1d-7164-325d-aa56-6d336d8f73c3 | -8.9195 | -64.1473 | 2026-10-03 16:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| e588e363-0547-30ac-91f9-63f011b5057b | -8.5554 | -66.9945 | 2026-10-03 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f304cb44-a8fd-3ef5-b90f-c59ae0c9fb37 | -8.5738 | -66.994 | 2026-10-03 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 2f877973-e93b-312a-9108-ddb9a4c7e53a | -1.2818 | -49.3803 | 2026-10-03 16:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| af88b66a-4720-32cd-85ea-4c5dc793d5fe | -9.8061 | -64.9979 | 2026-10-03 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 90f6f705-fb7e-3a5e-9314-59f17f0598c3 | -9.1147 | -65.9379 | 2026-10-03 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 9e454b64-129c-36e6-bc3a-3fc49f1645c1 | -9.1335 | -65.8813 | 2026-10-03 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 2888de83-7376-33f8-bf77-22f8f16e162c | -8.87 | -66.8935 | 2026-10-03 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| e74d78cf-9be5-3b3a-87ee-eeac67b1d1d8 | -1.245 | -49.3172 | 2026-10-03 16:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 4c794ce7-5b90-36a8-bd23-49edf329d69e | -8.8705 | -66.7822 | 2026-10-03 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 7622201c-cc22-3270-9506-c86908da9a0b | -9.4819 | -66.7836 | 2026-10-03 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 9bc504b4-2e5b-3866-ac00-56a8a999ea3c | -8.852 | -66.7827 | 2026-10-03 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| a7892fd1-9877-3b1b-949a-838e81c7dc9c | -9.2745 | -67.6433 | 2026-10-03 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 0218a242-6ddf-3846-8cda-d62256a41013 | -9.1147 | -65.9379 | 2026-10-03 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 6e2891aa-9da7-3cc7-9d11-835245bad53b | -8.5554 | -66.9945 | 2026-10-03 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a139c62c-22bf-393c-9ec8-767de4982533 | -1.1897 | -49.2966 | 2026-10-03 16:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 9833eeb9-9bc6-342c-b3ae-d56bd4e7953e | -1.1897 | -49.2966 | 2026-10-03 16:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 32caba0b-3a0f-34de-ba3a-9610df486349 | -8.9257 | -66.8549 | 2026-10-03 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 2cb44e9d-9051-3d57-94ca-f9a3fd9ac55d | -9.1147 | -65.9379 | 2026-10-03 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 30ee9335-c67d-30e0-bbc9-d35544614ca2 | -8.5554 | -66.9945 | 2026-10-03 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1c8137bb-1dfb-312d-946e-c31234b64ecd | -1.1897 | -49.2966 | 2026-10-03 16:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| cde1de65-d3ea-3657-a07e-2bc30d7d792b | -8.5554 | -66.9945 | 2026-10-03 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ead40ff5-a47f-3a54-af12-3fb21a4baef4 | -1.1715 | -49.1694 | 2026-10-03 16:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 0a15707a-60dd-30b4-b6d6-9de8dd727bec | -8.5554 | -66.9945 | 2026-10-03 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |


[Clique aqui para ver as próximas entradas](README51.md)
