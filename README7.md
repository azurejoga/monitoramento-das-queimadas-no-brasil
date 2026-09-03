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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b99f41a-7a33-31fe-b63f-b248594a05c1 | -9.0415 | -65.7349 | 2026-09-03 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 463a88e7-ba2a-38a7-adda-19dfc242a4ab | -6.4209 | -58.2943 | 2026-09-03 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9215af38-bfab-3e75-afe6-ac459dd9dde4 | -8.7798 | -62.6051 | 2026-09-03 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 65e506ea-ac9d-32da-aef5-03199f0cac70 | -6.1474 | -57.7605 | 2026-09-03 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f5e0f3ac-13c1-33d4-8153-e2962d0ade64 | -18.15 | -51.8156 | 2026-09-03 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0417a8ff-aa54-35e9-889c-7dc113208500 | -11.001 | -45.0617 | 2026-09-03 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 7bb72eb3-1094-30d3-9d2e-798a8f60f90f | -6.3052 | -56.0442 | 2026-09-03 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| e1f360aa-67f9-39b9-95f1-d2d124fb432e | -12.4033 | -44.8089 | 2026-09-03 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| e16ededd-e1f6-368c-b840-b182fe12442f | -10.9815 | -45.0874 | 2026-09-03 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| e1a02112-f551-3ab4-a62b-a6566e7c1b41 | -6.3237 | -56.0434 | 2026-09-03 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 036dd32a-0e78-325c-a1f1-fa97bc44019d | -6.7464 | -59.4223 | 2026-09-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 7fe62a55-42ce-35d9-a05c-d279388a1ee9 | -6.6542 | -59.426 | 2026-09-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 691dd878-9050-38f6-85f4-e86717ba9a03 | -6.6884 | -59.9244 | 2026-09-03 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8c117a39-90d5-38ba-8205-48b911ea1a58 | -8.4677 | -54.6429 | 2026-09-03 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| c4b9f4c5-70d8-377d-8e6c-b629a3e555d9 | -8.4675 | -54.6631 | 2026-09-03 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 056a5503-8eb9-34a6-bb81-7f11e1125985 | -8.7613 | -62.5869 | 2026-09-03 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d07b0c19-3c0c-3640-b685-66473121c832 | -6.6698 | -59.9443 | 2026-09-03 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.6 |
| bede9d0c-2450-3e8b-9331-7eaf3697947d | -6.6913 | -43.4222 | 2026-09-03 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 8bc6433f-0d48-3ea3-91f3-61b3a6240452 | -8.7612 | -62.6058 | 2026-09-03 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| cfeb6ac0-94d5-3d31-b9e9-7b183ef6fef5 | -6.6248 | -55.2331 | 2026-09-03 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 64b6f32c-008f-3757-9602-e01143473fca | -10.9017 | -45.3049 | 2026-09-03 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 0afd86c8-7381-31da-8f81-fbf9fc42cf50 | -12.4225 | -44.8059 | 2026-09-03 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 35ae6a7c-8823-3925-8472-84b5e1fd9004 | -8.0924 | -50.9642 | 2026-09-03 00:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 192.8 |
| ff93133e-b38a-3b7e-9d0c-1d1c2870b515 | -8.5916 | -67.1788 | 2026-09-03 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| aca3e86d-3d0a-3c5e-a3ea-9a9e4af08f5e | -8.8925 | -62.3538 | 2026-09-03 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 12ed8def-b721-37bb-933f-04be09c36133 | -11.0003 | -45.1078 | 2026-09-03 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 66918a0a-13fd-3121-a284-c242396dd037 | -18.776 | -48.9226 | 2026-09-03 00:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| dc432a8c-9e98-314e-91f3-f1ef23bf1810 | -6.6541 | -59.4452 | 2026-09-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.8 |
| dc8125cd-8f50-3200-a6cd-c191ab651ddd | -7.3295 | -55.1354 | 2026-09-03 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 04ba8013-d890-35df-903b-6b79a57f04c4 | -9.0231 | -65.7169 | 2026-09-03 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f70a294d-729b-3baa-9634-d0f93cbadae6 | -18.1704 | -51.7904 | 2026-09-03 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 5b660917-e5fe-32aa-814a-742edb8a81dd | -8.4481 | -54.7452 | 2026-09-03 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 77d9f434-13e6-395e-bbdd-ea40734a0c4a | -8.0926 | -50.9431 | 2026-09-03 00:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 76c614b4-ee52-3c33-b67d-ca01be89bac5 | -18.7766 | -48.8999 | 2026-09-03 00:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 405b0a16-cdf1-3bb8-851d-bb65ede7ff64 | -12.4037 | -44.7856 | 2026-09-03 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 3f955b1d-e5e5-3e04-921b-f4b0f4232ac9 | -18.1699 | -51.8122 | 2026-09-03 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 84cbf35e-dc17-3ef3-9d31-a6cb75db45b1 | -8.7799 | -62.5861 | 2026-09-03 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| aadc6c00-378b-3cdf-ab8f-f05c70397021 | -6.6883 | -59.9436 | 2026-09-03 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 182.6 |
| 3e0b33a0-bd47-3b18-a735-f3cc3fa79aae | -13.4162 | -42.4755 | 2026-09-03 00:50:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 94.3 |
| f1c47900-ef38-36e7-9bc0-9332df9cb366 | -6.6357 | -59.4459 | 2026-09-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 4a3cd0f1-59f5-3def-b69d-6075844369c7 | -13.4157 | -42.4999 | 2026-09-03 00:50:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 0a74d252-4742-3e31-bd88-4e0f1ca26580 | -10.8826 | -45.3075 | 2026-09-03 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d4fc6b92-9524-3a6e-9219-1bd06faf5967 | -6.3052 | -56.0442 | 2026-09-03 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| e27aae14-6c47-3b8d-bc72-5cc947044c5d | -6.6698 | -59.9443 | 2026-09-03 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 5beef342-c471-3f82-8e27-20dcc757bd48 | -6.6727 | -43.4006 | 2026-09-03 01:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f1b95ba2-2364-3652-9d01-d50344522d6c | -12.4033 | -44.8089 | 2026-09-03 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| cbc1756a-e6ac-3aa2-bf9d-c80d641dbe73 | -18.1704 | -51.7904 | 2026-09-03 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 18a05f67-d816-381d-9192-c7d69cda7e1d | -10.9013 | -45.3279 | 2026-09-03 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 195.3 |
| d7f5b28e-83de-3b02-bd81-a34b02a9f7c5 | -8.7612 | -62.6058 | 2026-09-03 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 8003b564-68a2-3dc8-8a92-405e87e3c852 | -8.0924 | -50.9642 | 2026-09-03 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 155.9 |
| 9db7321a-9a3c-3fcd-9b57-e099c1c1e153 | -10.883 | -45.2845 | 2026-09-03 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 53a12982-7d65-33b2-81ad-6265b1441d08 | -6.7463 | -59.4416 | 2026-09-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 394017d7-81d1-3cf8-b1a0-b5ad08320241 | -6.3237 | -56.0434 | 2026-09-03 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 215f1294-473d-31b8-aba6-f7e7d934973e | -11.0006 | -45.0847 | 2026-09-03 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 261.6 |
| ef36a229-4c5f-3712-868a-bc7b6b82db70 | -10.8826 | -45.3075 | 2026-09-03 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 224.2 |
| fbd9cf53-68f2-3ad9-9243-ca1dba30910b | -6.6248 | -55.2331 | 2026-09-03 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 755ab56d-c3c1-30ec-a5ff-af1756db7644 | -6.7648 | -59.4408 | 2026-09-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2e151335-74e4-3bf1-94c5-01881e13a590 | -6.6882 | -59.9628 | 2026-09-03 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 455f6799-2775-37c9-8e81-e3f79a576f1f | -10.9017 | -45.3049 | 2026-09-03 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.9 |
| ba1324cb-e750-3211-a07d-6a58f0da9243 | -8.7613 | -62.5869 | 2026-09-03 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 5546efc7-5374-33a4-89c0-95c8196c0647 | -8.4677 | -54.6429 | 2026-09-03 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 67219563-b01b-336f-9cad-8fea70572ab5 | -10.9815 | -45.0874 | 2026-09-03 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 219.5 |
| faec56e9-3836-3f5a-a740-f278cc8903d1 | -18.1699 | -51.8122 | 2026-09-03 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b60d5365-9503-32d4-a647-866c3d052ab4 | -6.6883 | -59.9436 | 2026-09-03 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 202.9 |
| 263b6291-b93f-314e-ba49-64409bb8d737 | -8.0926 | -50.9431 | 2026-09-03 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| b34eae91-a7c5-32f3-8b79-c0fedad84bab | -6.6357 | -59.4459 | 2026-09-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ac3c8563-2650-3465-a939-d1e0e1e56c6a | -8.7798 | -62.6051 | 2026-09-03 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ed96af7f-27ef-3e7b-8640-6632b8f847de | -8.0737 | -50.9656 | 2026-09-03 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| c1348bd5-6969-3c01-b40c-58b6ec03de08 | -6.3051 | -56.064 | 2026-09-03 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 1c8bae3b-8ec7-3ae0-afe1-c882033d5edc | -10.2028 | -50.2895 | 2026-09-03 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| f16d5a25-daf8-37f5-bd30-7c3d542ff12c | -6.6884 | -59.9244 | 2026-09-03 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| f6f8b4b7-6a2f-360f-a478-c3626e72a1c0 | -18.8407 | -46.4417 | 2026-09-03 01:00:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| be554e1c-c149-3651-b9dc-d0668416ac30 | -8.4675 | -54.6631 | 2026-09-03 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| cf17820a-3387-3525-a951-8c73f71b5ba4 | -8.7799 | -62.5861 | 2026-09-03 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 671bd9ac-4a5a-37ce-86bb-45769042de7b | -6.6434 | -55.2322 | 2026-09-03 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 50a712cb-0ed3-32b0-8fec-0d405f5b1c39 | -8.5916 | -67.1788 | 2026-09-03 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| dfa0087e-b51f-3cd3-b15d-52ee79aef719 | -10.9811 | -45.1104 | 2026-09-03 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 96856ef9-1c2a-307d-aa03-105cac53d2ab | -10.8822 | -45.3305 | 2026-09-03 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 284ac5f2-6012-3e98-98f9-82c0af581d16 | -12.4225 | -44.8059 | 2026-09-03 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 7dbeeb86-53a8-3705-b428-5cf762bcf857 | -6.6725 | -43.4239 | 2026-09-03 01:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 65d40ea9-3438-39ac-9097-47a10d7d3863 | -9.0415 | -65.7349 | 2026-09-03 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a3d1d73c-1591-32bd-a7d6-f78be74243b6 | -7.3295 | -55.1354 | 2026-09-03 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 1d094c2b-2aa1-3b75-8615-fc5838252ddc | -6.3236 | -56.0632 | 2026-09-03 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| b8e35f4d-6968-33a5-b4e8-84f287cb72ea | -8.4295 | -54.7464 | 2026-09-03 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 4d2d589e-d5c2-3257-896b-3e68bd1b5a20 | -6.6697 | -59.9635 | 2026-09-03 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 81252eb5-069b-3045-85d7-47cbc963457c | -6.6542 | -59.426 | 2026-09-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 6390c673-bea2-3c92-9e66-a039d3bf12b2 | -9.0231 | -65.7169 | 2026-09-03 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a7cb942e-cc0f-32fd-9e40-f1d0c243c124 | -6.6541 | -59.4452 | 2026-09-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4f1945ef-c859-3f56-b91a-c0133a9404b5 | -6.6358 | -59.4267 | 2026-09-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| aefcb35f-f0ca-3aec-ba42-eaddcc64edfe | -13.4157 | -42.4999 | 2026-09-03 01:00:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 8fd001d3-e405-3cd8-ae51-3eca154d8801 | -9.0414 | -65.7536 | 2026-09-03 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 67bb1bd9-ff49-3850-994a-a64bdf8462cc | -8.4295 | -54.7464 | 2026-09-03 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| cf52d15d-6a41-3f97-95a5-95162bcef9dc | -10.8822 | -45.3305 | 2026-09-03 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 698888ed-56c7-3141-84f3-606b8695ccc1 | -11.0003 | -45.1078 | 2026-09-03 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e3f74f76-fc8e-361b-bc58-9856a8954da5 | -6.3237 | -56.0434 | 2026-09-03 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 607fe6ee-1465-3be5-881f-775a8e6ed634 | -10.8826 | -45.3075 | 2026-09-03 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 291.8 |
| 3e5bcc45-7e2a-3891-aeee-e1f0af5ff99a | -18.8407 | -46.4417 | 2026-09-03 01:10:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 384d5447-eaad-34a2-9cda-2214b61c312a | -6.6698 | -59.9443 | 2026-09-03 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a7f15473-bdc2-3fb5-83ac-75d8779bc65c | -10.9013 | -45.3279 | 2026-09-03 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 6bf65741-ed70-3ab8-94b7-049c706be8c8 | -9.0415 | -65.7349 | 2026-09-03 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |


[Clique aqui para ver as próximas entradas](README8.md)
