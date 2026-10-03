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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1524b345-c51a-342b-a40e-c757ce2bdc0e | -6.31586 | -43.34386 | 2026-10-03 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3e83fc8d-eeb9-376e-9d4b-6f1f07b7e47d | -4.42156 | -55.74987 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6af93443-8630-3ffc-b916-87e8de9e13e7 | -4.40675 | -49.97277 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d13c5675-cac8-3eaf-9c9c-39865f268bd6 | -4.80619 | -49.87931 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0480553-5fa3-39f7-9134-27b421705af8 | -5.55888 | -43.96225 | 2026-10-03 04:40:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d74c4ac8-b1c7-3b06-9e6a-620a4af3a436 | -4.26039 | -50.74686 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aba2449-62f0-3431-b621-307a3774e053 | -4.29635 | -50.78207 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 059072d3-4396-33d2-934b-365095619e6e | -5.14093 | -45.57785 | 2026-10-03 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 349f487b-3205-30a6-8a4b-96505608b056 | -4.42597 | -55.75084 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c87f7bdd-452d-31b7-91f5-53563b8632d1 | -8.64663 | -45.82599 | 2026-10-03 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10bfc41c-ba85-39d9-83f2-33ef9038454b | -10.99059 | -59.12803 | 2026-10-03 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a1f7f063-7027-3c26-9f3f-6a423b32483b | -12.13381 | -63.17514 | 2026-10-03 04:42:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b7f24aa-f1a0-3545-84ac-dda94f6d200d | -10.98952 | -59.13374 | 2026-10-03 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0841a00b-6548-3c2b-8953-939b289cc1e2 | -12.14298 | -63.17393 | 2026-10-03 04:42:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51610c3f-da9f-3256-bade-4dfa38149ba2 | -12.13014 | -61.1571 | 2026-10-03 04:42:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edeb3db2-05e7-34b2-8016-c36e4dfeacdf | -12.86035 | -44.69445 | 2026-10-03 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b8ebceb-c46d-3102-822d-37719d8d11a1 | -10.99452 | -59.1347 | 2026-10-03 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a1d43514-bc9f-3343-aeea-2146ce61f75a | -12.85269 | -44.68449 | 2026-10-03 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a8b45cc-2609-33b0-812e-6a9aaeafb573 | -10.99006 | -59.13089 | 2026-10-03 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 683610d4-953c-3279-ae1c-49d9d134bbcd | -15.11661 | -43.62231 | 2026-10-03 04:42:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 51aba2db-d90c-33d3-a1bb-4fc6c39182d7 | -12.13665 | -63.17263 | 2026-10-03 04:42:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47756225-ddcf-3678-8fad-bc06d33a1ac9 | -12.85213 | -44.68886 | 2026-10-03 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 68ba8666-9e26-3537-a698-635d4bccf2f9 | -13.38607 | -41.34449 | 2026-10-03 04:42:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0ad3eae-c487-3dab-81f4-695ef5795c2f | -10.87705 | -57.10707 | 2026-10-03 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93c0a1ea-6559-338e-a5e7-17d2f00b7c08 | -17.24693 | -39.43378 | 2026-10-03 04:42:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 64ab24eb-470e-37a4-a798-f25700b370d3 | -10.99399 | -59.13758 | 2026-10-03 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d64651da-e032-3f53-9259-2cd554d6e0fe | -12.05799 | -58.0413 | 2026-10-03 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d5afc18-d236-3e17-a759-c030222fb372 | -12.85595 | -44.69387 | 2026-10-03 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 420403f3-6592-3ffc-9c60-9a6f7ca41b55 | -12.8581 | -44.71185 | 2026-10-03 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df28cc8f-f6a6-3243-901b-e0d2b871ef31 | -15.1186 | -43.63023 | 2026-10-03 04:42:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 76a56ec4-4253-3691-bee1-02c9b87f6bb3 | -13.50428 | -61.13379 | 2026-10-03 04:42:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2275a031-1818-3232-9bee-3b92dfecb2b5 | -10.99506 | -59.13186 | 2026-10-03 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a12e705b-2036-308c-8fed-6b8cb6f5aea8 | -12.14013 | -63.17644 | 2026-10-03 04:42:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00463e00-73f3-3571-814f-4c658f904bf7 | -15.11925 | -43.62465 | 2026-10-03 04:42:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0861a8cb-b41f-3f86-8ab7-c70685f032aa | -12.86632 | -44.7174 | 2026-10-03 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9a2ae760-f39b-3ccc-b2b0-1e39d961a278 | -10.14306 | -61.74255 | 2026-10-03 04:42:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32e1dde4-a12d-35f6-b3ff-7a0cf534d3ca | -12.86092 | -44.69006 | 2026-10-03 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c91bab6-4b3a-3ba2-96c1-7739dbc5ed48 | -15.11373 | -43.62955 | 2026-10-03 04:42:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 80da024b-a66b-3802-925d-38c34197ab6d | -12.13556 | -63.17791 | 2026-10-03 04:42:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0796ab7-dbb3-3f93-a7ea-966ce9b93dff | -12.85652 | -44.68946 | 2026-10-03 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 401aa75e-e5f9-34de-92c1-5da0e5a7f276 | -15.11592 | -43.62786 | 2026-10-03 04:42:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 31fbdfc4-541d-3c83-9ebe-318dd77ace4e | -15.11437 | -43.62399 | 2026-10-03 04:42:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bdc3dfb8-03c7-3ebe-a8fc-9f01ee6716c1 | -13.62602 | -42.47849 | 2026-10-03 04:42:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7b0e0730-38b0-3555-bbd4-fd6e2483fd67 | -10.13906 | -61.74155 | 2026-10-03 04:42:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a502f832-a708-3d30-9517-9eff27d8e27d | -10.98898 | -59.13662 | 2026-10-03 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4916351b-2acd-3018-832c-0d6d11fd700f | -10.99559 | -59.129 | 2026-10-03 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cfad70d9-d0ee-30ab-ba85-8ee7c768c227 | -15.12079 | -43.62852 | 2026-10-03 04:42:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b7f040c9-52b5-320e-9611-e41a364ae0fc | -13.38567 | -41.34795 | 2026-10-03 04:42:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0091631-74e9-3ce4-bd9a-b42f3341d564 | -12.86193 | -44.71678 | 2026-10-03 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b014896b-d249-3690-9957-b7140044b730 | -16.07427 | -57.02097 | 2026-10-03 04:42:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cdb8faf-1daa-30f7-963b-8ec9a66161eb | -30.44838 | -52.69016 | 2026-10-03 04:46:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| daf86887-53ee-3e82-8fe9-7b53663069a6 | -0.3489 | -51.99492 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dedd9d71-7f35-31a8-8907-1e4f98ee15a7 | 1.77861 | -55.60745 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d35893e-b0f6-364c-b918-74eb14c2d262 | 1.91131 | -55.78383 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4bc2c5c-223c-30d6-84e5-75ed63d4f8b7 | 1.90852 | -55.81097 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adc5322e-c448-3da7-8880-bd51fdce9adb | 1.90845 | -55.78808 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45383989-ec32-37e5-9aae-268584386209 | 1.1359 | -59.5245 | 2026-10-03 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0477e972-a7c9-3d0f-8c0a-817b76ca1129 | 1.92573 | -55.80827 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a72510ff-bde3-3f59-a264-e977b3b9b2c1 | -0.40669 | -51.99493 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d709f81-32e6-3007-961b-0557800c7e87 | 1.78313 | -55.59174 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09e94f56-a064-33bd-99cd-d6471066b89e | 1.91189 | -55.78755 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 131b2667-c664-3ef1-9485-069ff9da2561 | 1.74301 | -50.8024 | 2026-10-03 05:14:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bb44e29-145b-3c4d-8f41-5e336e9ed209 | -0.35632 | -52.01568 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6b66a240-83e9-3e58-b516-8007261a98b1 | 1.7877 | -55.59853 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae792c23-fe31-333d-8b64-07e5b79ff45b | -0.4079 | -51.98725 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf3d7e81-cf8a-3795-a938-aef64831886d | 0.4992 | -60.60154 | 2026-10-03 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d53ac2c0-e823-3ffc-912c-69344de444e5 | 0.98097 | -50.12699 | 2026-10-03 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5959fd52-813a-3b7e-874e-5dbbb24b54eb | -0.36332 | -52.01674 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 150ea881-f3a4-35e0-80e1-93cae9857efd | 0.62773 | -54.40458 | 2026-10-03 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cd0ec33-d4cf-31d7-b16e-adb672b26ba3 | 1.79002 | -55.61317 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cd058db-8359-3213-bc98-601727fd92e2 | 1.91416 | -55.77957 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d25aa094-b95a-39e4-a55f-8ea5d1e52c66 | 1.7394 | -50.80296 | 2026-10-03 05:14:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df6dda7c-4f47-3239-ad39-b696f627b38e | 1.82286 | -55.55555 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4508c81-7d44-345c-8395-ae14d26674c0 | -1.05893 | -53.58693 | 2026-10-03 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be488d0b-941c-3cca-918a-d15accd48f38 | -1.39917 | -49.27016 | 2026-10-03 05:14:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 809f26eb-f26d-307c-a772-015d88e5baa4 | -1.4033 | -49.2708 | 2026-10-03 05:14:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38089e61-7ec8-3f23-a384-0bcf242706a3 | 1.78487 | -55.60272 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a64159f-b89b-35b3-a838-8fbcec44be19 | 1.80021 | -55.58907 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 071e239e-144f-3145-88a4-044a10037526 | 1.91475 | -55.78329 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| debc774a-4944-38ce-a6f6-b1d3fa206f2e | 1.93144 | -55.79974 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a08be9d-9edb-3ce5-997b-76b42a81fb70 | 1.90507 | -55.81149 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 339ae357-b31b-3acc-ae35-9404893611ad | -0.95541 | -52.33086 | 2026-10-03 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df418aef-0ace-38b0-b461-023e5c9ca3c1 | 4.80567 | -60.27665 | 2026-10-03 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b44030ba-b17a-3ef6-8bb1-5136f6ab39e7 | 1.96163 | -50.88412 | 2026-10-03 05:14:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0248fabd-4f0a-38c6-9532-8658327fd2e0 | 1.22202 | -59.97209 | 2026-10-03 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db4a8c25-a563-39b6-97ef-af01892ba2f3 | -0.35694 | -52.01185 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c328868f-d872-3bff-ab0b-8ee51e2d756b | 1.93805 | -55.7302 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae1e5520-3196-3876-a052-c9c114dffd40 | 0.60307 | -51.56253 | 2026-10-03 05:14:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29c6c011-62fc-3091-9d7a-ad2f3ce3d63a | 1.80304 | -55.58488 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d239859d-44eb-3aa7-ae87-0f33d0be3eb9 | 1.92892 | -55.73921 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e7875be-07a4-39af-b42b-967791e59e52 | 1.90793 | -55.80724 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5899affc-7738-360e-9698-52124e2a7e55 | -0.36399 | -52.01592 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49742240-6448-3a35-ac3b-489a80b96645 | 1.93177 | -55.73497 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| adfa826d-0d29-3cb1-9199-3e196c64b322 | -1.32991 | -47.58958 | 2026-10-03 05:14:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c1edc0e-c8d7-39f9-9fd8-0815c5cbd101 | 1.78718 | -55.61736 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bac7d782-dea0-3d44-ab0e-99a3d0f76e68 | -0.38525 | -51.74518 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac6d528d-2c48-33d4-9895-1ac5dc083c48 | -1.44661 | -48.91245 | 2026-10-03 05:14:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ba45c78-3056-3eb2-8020-e393108f8f8f | -0.4582 | -52.17465 | 2026-10-03 05:14:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b31cacf-10fd-35f3-8515-73642c9c8c02 | 1.78371 | -55.59541 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ced71f9-8e89-3b0f-955d-f69316fd34bb | -0.36689 | -52.0203 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README30.md)
