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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ccfb5a9-3736-3dc0-8adb-7034421d1d2c | -17.33129 | -46.66898 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce6e9f56-115c-3f37-bdde-d6ae732f2b02 | -15.11672 | -48.60696 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3a46aa1-9085-3380-be24-8c867ccebbe6 | -11.87177 | -58.8185 | 2025-09-12 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 732928e2-0993-3613-a6b9-eefb47e5523e | -14.45414 | -47.30937 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef654a05-4491-3cfd-b978-978373051407 | -18.44729 | -47.1813 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cba15e1-62b2-32fe-8d41-201a171721ef | -14.50601 | -53.91005 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 396dd14b-2003-334e-9928-ada2224aaba5 | -11.98718 | -51.13529 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf336493-c9a3-3048-b261-7e43ad0f567c | -13.27045 | -51.71867 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9966207e-a5de-317c-8695-b4a7259ff12c | -18.92036 | -46.81562 | 2025-09-12 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 953bdaab-1c32-37e0-b58f-a16422bd36d8 | -16.49544 | -51.98558 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e991755-63a0-3ff0-bc28-3dd2b5a81389 | -12.46992 | -47.49902 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f0a7e36-0542-3f1e-b407-63ef58cac8ac | -11.81164 | -50.57593 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a38bd1b-88a2-3423-a0f9-009bca918de2 | -14.26441 | -54.78782 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cde1199-d78f-3269-ae0c-9e114bdf92a4 | -15.10686 | -48.00173 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7bd9ac2-7eb1-3464-9116-71b7675f36c9 | -15.92339 | -51.79701 | 2025-09-12 04:27:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 7565286b-697f-3c0f-bdbc-051abc7c2c54 | -15.48428 | -47.34065 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8683362a-3748-39cc-9c6c-050b1dd9eaa6 | -12.86006 | -47.95354 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cce295da-8de8-3a96-a4bc-426fbdfbfbf0 | -17.47474 | -43.72005 | 2025-09-12 04:27:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6ed6f0c-8c56-39b8-a853-41f5583b7095 | -13.98354 | -48.21399 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b39589e-105a-3196-893c-573767cb4d7c | -18.06091 | -50.7317 | 2025-09-12 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ae86bae-bba3-32ce-8cb7-e31cbaf608a8 | -16.49406 | -51.9722 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bf905718-08d5-3fcd-8ecc-8d753d7f0818 | -12.8424 | -47.95784 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 99c6f4bd-e880-3836-8320-82c63663186e | -17.54589 | -44.54279 | 2025-09-12 04:27:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52cb9ada-352e-316c-8b1a-e4d67dd5a18c | -18.61436 | -43.96597 | 2025-09-12 04:27:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8db5b913-f817-31f7-873c-b68ffbf0484f | -18.61745 | -48.25279 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2bbafcfb-f420-3a0d-baa2-248865674b73 | -15.10563 | -52.44984 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a73bc622-eb74-33b5-b607-3dbb4a03f75a | -14.42361 | -47.33395 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 829946c7-3c52-35f1-b0ce-a0bd038c4891 | -19.6414 | -41.58286 | 2025-09-12 04:27:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 413593ab-8da5-3016-8da9-ddb31d41cd03 | -12.82878 | -52.96846 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba456141-3dcf-3949-90e6-0aa301e1e1a4 | -17.38055 | -52.93397 | 2025-09-12 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71586a56-5cd5-3ab9-b2c3-34e3ef83abe6 | -17.34668 | -46.67814 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e91f158f-f0a1-33c8-b47b-d9e5e3024e2b | -18.62565 | -48.68219 | 2025-09-12 04:27:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8961b867-2bfb-3416-9d3f-5fb1583afc9c | -15.60425 | -52.73465 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7ac1f3e-9580-30f0-a0ce-acfb68600a5b | -15.88337 | -48.18151 | 2025-09-12 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93f1bfd7-e809-30b6-864b-fc9c174d533c | -16.30524 | -50.07895 | 2025-09-12 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d26a1385-773f-372b-ac3e-edee6bfb0f3a | -17.20196 | -50.1507 | 2025-09-12 04:27:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90784c9a-01c1-36c6-ac31-cf66df9e6766 | -15.68491 | -47.04139 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05583c9f-aeec-37a0-b77c-4bddec2b37f7 | -15.53306 | -48.55172 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04222937-8803-3a07-9b6b-ccb7f982b048 | -13.95934 | -48.19614 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f429dcc-5be9-34af-9166-40ed73f05596 | -12.95713 | -54.74505 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7968baeb-8f6c-3985-a5fa-c078b90b53e9 | -14.42305 | -47.33755 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b931e70-2e18-3da7-ab64-6715cb6a2592 | -17.90385 | -44.60604 | 2025-09-12 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cde1b009-cc5e-318d-b7c8-9792e6962912 | -12.86525 | -52.95305 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ebb1e0b-a3f5-3f5d-87fc-f52b7f2e9fbd | -15.22998 | -44.03599 | 2025-09-12 04:27:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ee1dbba-3df7-3308-a4ef-1780da84638c | -18.06158 | -45.43628 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50dd5e36-5739-3a69-9470-642f76ddfd73 | -11.98566 | -51.14412 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6bc69b90-527d-3e78-a7a9-4f7c66c57b76 | -15.1206 | -48.60395 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71eb1506-7f65-326c-a591-cc76925118c9 | -13.91675 | -47.97095 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10a7c5c3-dde0-390c-a2d2-b5f27a258e29 | -14.45026 | -47.31246 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0eb4a546-e233-3f3b-a44b-7f39347c9793 | -17.78269 | -49.98878 | 2025-09-12 04:27:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 249614d9-aa92-3761-9eb0-9a7cd888126f | -19.24325 | -48.03514 | 2025-09-12 04:27:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b727950-5bb7-341e-a617-299eded98fca | -14.50877 | -53.91875 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9c119062-4473-31db-9373-f70e253ed5e5 | -13.32021 | -44.65047 | 2025-09-12 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff69c0e9-b8a6-3a54-8e27-85ac4869567e | -16.42286 | -49.04414 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6acacdf9-3434-3241-b682-8321003726aa | -13.92226 | -47.97913 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16d8fd35-7bab-3001-93aa-a90a687d40ab | -12.47213 | -47.48493 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cf2001b-39c0-30bd-bf8b-3d28cb6ed88e | -14.92315 | -55.84256 | 2025-09-12 04:27:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dac66b99-1b62-3e53-b294-2550d86b99b4 | -13.02931 | -46.75892 | 2025-09-12 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6e14b6d-e544-35c3-83ec-c6b0352a991e | -18.44388 | -47.18073 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14bce206-1e5b-3016-b410-e4dfba16b5c9 | -11.64557 | -50.58671 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a120e649-fa83-3238-9384-b30c02219d09 | -18.77635 | -48.54184 | 2025-09-12 04:27:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1da220a0-63ad-39f3-bab6-4e20c67a212c | -18.34422 | -47.02657 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c57093f-d5f5-3a51-a267-4f8ba677e5d6 | -14.55382 | -54.52588 | 2025-09-12 04:27:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1946ab5e-ccd9-3dbf-a059-e4b8ec636bb1 | -12.85278 | -47.612 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e69eb72-3a55-3802-9574-7b29c22a3f5e | -15.53032 | -48.54758 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6014644b-4007-3ea7-a311-85c886906cb1 | -10.33326 | -58.02565 | 2025-09-12 04:27:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baac229d-09b0-393f-9a1e-00cf1f77a7b2 | -13.9516 | -48.35071 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3b23f99-fb63-356f-a8eb-60582cfd1ebe | -15.0781 | -48.03353 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 162fa354-6578-38da-bf62-47fe81e44848 | -14.32283 | -54.1284 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 51b7ff9b-22fc-3612-8c7c-13bc76eeb699 | -18.44598 | -49.56182 | 2025-09-12 04:27:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aee6c41a-bb81-3b2d-ae6e-23d6e05b710c | -20.26978 | -42.11305 | 2025-09-12 04:27:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 48d0361e-8e2b-3d3b-8e1b-52dcd78c6e83 | -20.11636 | -42.35433 | 2025-09-12 04:27:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 08595898-013e-381a-bfb5-7a01d0f5284e | -18.30929 | -50.42136 | 2025-09-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 2b57ab20-aee3-37f0-a7d0-4474cff992bd | -13.00899 | -47.99905 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff750996-ea59-3b02-896c-1bf94880d9b6 | -13.53955 | -43.00881 | 2025-09-12 04:27:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5910535e-05cb-3749-9b71-6beafd039efb | -13.90062 | -48.26635 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| c451f61d-8881-33df-9ff2-7512744ea213 | -17.13489 | -48.49176 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b9490cb-619d-3669-9628-9ec15e0f7c21 | -15.48762 | -47.34121 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92faaf89-b52c-35e6-a67a-602de1f9861d | -14.40633 | -48.37494 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8eb8eed5-27cc-3d6c-80a9-d3f32d6b76d2 | -17.20807 | -50.15564 | 2025-09-12 04:27:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7097ffc3-30db-3f4e-9fcb-c60582013317 | -17.35131 | -46.69483 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f046b182-0b13-3364-9c49-d304f3d6c888 | -18.66207 | -47.66449 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6307148-113e-301d-9001-0fdc66e1f9d0 | -16.19378 | -47.86318 | 2025-09-12 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f678fbb0-7524-3882-a232-f7fe5049fe67 | -20.17577 | -44.62534 | 2025-09-12 04:27:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3b0146d-bea1-34b0-91c5-c825b4effd8d | -12.61888 | -56.96174 | 2025-09-12 04:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f9f683c-469c-3f58-b58a-dc09eab469a7 | -14.38399 | -45.18303 | 2025-09-12 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0278c1b-54c1-3901-adf2-044ae1593d23 | -13.02227 | -48.00144 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58812fff-293c-3cf7-b154-fecd4b52da63 | -15.082 | -48.0086 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 170e302e-5224-3a97-81de-58026d9b6d6d | -13.35553 | -41.92936 | 2025-09-12 04:27:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1a491a50-d473-3c42-8080-a0b865860422 | -15.74382 | -48.37812 | 2025-09-12 04:27:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47ba9f6c-5364-3c84-8538-547095542210 | -18.17907 | -50.48704 | 2025-09-12 04:27:00 | NOAA-20 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba259a2b-7c6b-3c75-947e-e237d1811abe | -15.68828 | -47.04195 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e1e287a-fecf-3543-9de4-a8902f77e6b9 | -12.84925 | -52.9724 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff6a3694-981e-3e34-a2ca-c8a519a767a9 | -14.51157 | -53.90311 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04577908-098f-39f6-99cd-fa11c98e90c0 | -16.49456 | -51.96584 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b02d7cb-87ab-3bab-a38a-db393d24f94b | -18.05747 | -45.44301 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83ff11f6-0824-3c89-85c6-0eb456848af0 | -13.91619 | -47.97449 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c012a3d-9413-3d6d-a3f5-3ca4b97f4c75 | -17.47427 | -43.72363 | 2025-09-12 04:27:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| daac8b53-ed4c-329e-bdb6-15787b493b16 | -15.52945 | -41.43345 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cf3e33f2-84d8-383a-a38d-c2c8bd75e002 | -12.479 | -48.93042 | 2025-09-12 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README89.md)
