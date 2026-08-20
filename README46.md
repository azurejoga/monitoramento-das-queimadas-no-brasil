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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab1b6233-812c-3977-adcc-55e0bbe7c989 | -7.35121 | -45.81496 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8691093d-df71-325a-bb8d-0f476eb8d322 | -6.38421 | -54.94805 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b18d1de0-18ea-320c-81fd-7f7605fa8cac | -6.43733 | -52.71788 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1167e96e-e776-3508-ad29-0b003852281a | -6.35761 | -51.74066 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 484f5108-5e8d-3950-a77a-79f571075b2e | -4.39522 | -55.47485 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37321078-8aad-3b8a-9b5c-5c0c2eb21330 | -6.00571 | -57.8653 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b7fbc52-4747-30f4-bd45-9323e91f57d3 | -3.10099 | -61.20285 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68334fda-0533-3ff1-baa2-33425ec03fac | -6.59098 | -58.9718 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 089ed258-9698-3a5f-aaad-a1f578cf5f16 | -6.95499 | -52.81084 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ceedd15-ba5f-384d-8624-6153baffe1e7 | -5.79649 | -55.73406 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c2bb459-5015-3707-be7e-3580ec7db228 | -4.09743 | -42.49712 | 2026-08-20 05:04:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f097817b-2858-31b5-ae5f-5a27dcc692db | -5.80033 | -55.73112 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 557329c3-a7fd-3ded-9dfa-3f6804823952 | -8.36194 | -46.33801 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad20c992-bd3a-322c-a4f6-7288d4654cc3 | -6.00061 | -57.85298 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 589f8241-fc90-3d14-8431-ebf41987cb1b | -6.59325 | -58.98064 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aada0327-d12c-318b-b628-8b8b7c4d102d | -4.53087 | -56.12943 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff89b2c2-6f9f-38d0-b8b9-d65331e7e19a | -6.59165 | -58.96767 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1921cad4-a887-3157-b06c-694a1f862c7f | -4.5117 | -55.44716 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d6011fc-1c0a-39ad-9968-da106557dccb | -2.57362 | -47.24148 | 2026-08-20 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47142445-940a-3a88-be23-f6bcfebe4674 | -6.61935 | -56.32452 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ac29f5d-2ac5-34f9-864c-de361f4de77e | -1.83529 | -54.48602 | 2026-08-20 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 682b5a9e-92f2-3703-9a3d-5c3080605104 | -5.49474 | -60.13456 | 2026-08-20 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 737d0c08-50a5-3e8f-ae1f-4cf7e439eab6 | -6.25115 | -55.41328 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa3e85e6-f5b3-3eb0-8ba4-d43406684f8b | -3.01393 | -51.05688 | 2026-08-20 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a70a4b3-43cb-3269-b6d1-978c967dfa8a | -6.53752 | -56.17352 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47ba0922-f1a6-3a4a-9d85-66adb9991882 | -6.59523 | -58.96827 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4b11763-75b3-316f-899c-7543d21b2d52 | -6.24892 | -55.40583 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e684ba3c-4cbc-3a45-b2d7-9a0e51e7e04b | -6.59881 | -58.96885 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca4041d0-d0b5-36d4-a935-4c9e37059fd1 | -2.11852 | -47.11516 | 2026-08-20 05:04:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8487ff66-f75a-35f1-a8e1-8615042c6e6a | -7.35539 | -45.82791 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4ddaf035-4373-3a8f-b3ed-9467a818e07b | -11.22072 | -55.06518 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4653972c-5fe3-327b-a4fc-9797c2cc6a04 | -11.41964 | -54.31328 | 2026-08-20 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50345138-02f3-3d44-b922-f3fc751534e5 | -9.25728 | -56.91638 | 2026-08-20 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c20da3e9-1270-3d63-99ad-f2bc569585e4 | -8.10912 | -51.66343 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8319c65-3e14-303b-b032-797ba79e1487 | -12.04919 | -55.44975 | 2026-08-20 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee2db859-a5f0-35b9-981f-e5ec81dd2b1f | -9.39504 | -60.55742 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d4cfe8b-1a69-3a14-a5ab-22855a57a9d0 | -7.36549 | -55.50565 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5de07e2f-5e92-3c2a-bd7f-b21de7b99207 | -11.42258 | -54.31786 | 2026-08-20 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a58f0d8f-5078-3620-8474-e82fc9824428 | -8.53117 | -54.86451 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7df60b1-10a6-3f08-b43b-96640a53cb95 | -8.68276 | -54.65199 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c678dbf9-bea8-32ef-9715-b70e740a36d4 | -6.95853 | -59.049 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9b26fde-430c-3e9a-9fe6-ab0427358b91 | -6.91956 | -59.3555 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94fc8693-b5e6-3479-aace-0a4654401f78 | -8.55127 | -54.77815 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c47517a-21c9-35c2-9b4c-8de663a2a416 | -9.51327 | -51.64717 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cf6b25c9-8cfa-3a20-bbfc-6e36b9888fd4 | -8.53828 | -54.77245 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee9ad377-e6a9-3846-948b-0a788a2368d5 | -8.58404 | -54.75341 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b38ddb05-9eb2-3fce-8ee2-6008633d6563 | -8.58624 | -54.73872 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75549c78-78fc-33c5-b965-24a0c336d3eb | -11.19583 | -54.01118 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a130d93e-4434-3e6f-8da4-636b0ac56b4c | -7.04933 | -59.84429 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96de5c7f-d5f2-39bd-86f9-9f91b852c1b8 | -8.57604 | -54.72955 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 600d7b01-cc72-37e7-acf0-5f16f32fc991 | -7.77864 | -61.16771 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 266ccdc5-0518-3687-befb-6d39e39957e9 | -8.12141 | -55.05236 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edd9281e-1106-35a7-a446-ecfd72897445 | -11.81094 | -44.80736 | 2026-08-20 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dba17ebb-7b29-3b88-9e87-9a3ca03bb4f3 | -8.56238 | -54.65976 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ffd3456-3654-3123-83ca-43c9c29c0bce | -8.67764 | -54.63987 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 961d9ccc-806e-368c-be48-374a70c57467 | -11.82198 | -56.60303 | 2026-08-20 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98f271f4-8032-39a7-b81d-e65f1b53d5b5 | -12.05202 | -55.45399 | 2026-08-20 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 344f5013-4d03-366a-9360-dace33b5f1ee | -12.79551 | -48.42103 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc41e817-3cd9-318a-a73b-7caf56172052 | -8.50359 | -54.86404 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5c1effc-72b4-3518-9465-28da3b22c480 | -8.5295 | -54.8754 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51083c57-8519-3c9d-9b00-a0fe705278af | -8.57037 | -54.72123 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 775d99f0-9fd2-3bc9-bb8c-46e32488c454 | -7.53384 | -55.58217 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecb32031-09ff-322e-9063-cdfa319b6302 | -8.66338 | -54.59608 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67b9f402-021d-3132-9b88-77346000f9d6 | -7.86503 | -63.75089 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba3b8db3-6c6d-373e-9115-721dd87b12a8 | -13.44503 | -43.84649 | 2026-08-20 05:06:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c0eb1a70-c41a-354c-a838-4921f7887d03 | -8.57965 | -54.78263 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1186d9f-9fcb-3f4c-aa42-929b3e8b7b47 | -7.8719 | -63.76795 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4643f956-3c33-3d73-808a-42a9cf912044 | -8.67947 | -54.74184 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a8283aa-7836-3664-b7e6-213648269304 | -8.97538 | -50.70634 | 2026-08-20 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1a142deb-76f1-307b-be72-b6c0348858f7 | -8.57214 | -54.77764 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1465682-a470-3bf9-9e7b-9b298dbe8ce0 | -11.8328 | -58.84043 | 2026-08-20 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f86b16b-4ea6-3621-8d87-4cd34ec6b369 | -11.2173 | -55.06465 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8716117f-bfc9-362d-8d38-233ca7528797 | -9.17973 | -59.46783 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fd24df2-c089-37df-beb6-90511a837b4d | -8.58459 | -54.74976 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50f860ec-18cd-3749-a43d-3e125a506185 | -9.95217 | -53.32866 | 2026-08-20 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a29d1b3-d0d8-3662-9d43-fa0541f84851 | -10.761 | -50.34964 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1472b42-1121-3890-b4f4-1eb2dc0cf624 | -7.56191 | -55.55442 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14d71bd5-7ed4-357c-8874-ad19e6d87ad2 | -8.53736 | -54.86922 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce044051-2e33-3ecf-b7d5-96a0e5469eae | -11.44102 | -47.53311 | 2026-08-20 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31aa7d01-491e-32b2-ab55-6f6c6c216a8d | -6.80488 | -59.01743 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 920280c6-808e-3936-ae9a-0e004d4dc472 | -7.34564 | -55.67714 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 07ebdcba-5be5-361b-ad5c-75496002552d | -11.81589 | -56.59845 | 2026-08-20 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be99024c-f6aa-34ae-84f5-6e957dfab56c | -9.50722 | -51.63207 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97f8c63a-8f4e-3289-880d-4d90bd183ae3 | -8.53847 | -54.86194 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9b6aa48-7f78-3b8d-b08b-ed3dd508c123 | -7.86417 | -63.75966 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1911dfce-ec82-3aae-8645-5082a9601149 | -11.91421 | -50.18274 | 2026-08-20 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08885b41-c418-36b1-9d6e-687ad790e9a0 | -13.40457 | -54.37424 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 70caa623-c8a1-3e96-af70-887132968c59 | -9.50389 | -51.68487 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d58f255-d0f7-3b29-b618-31d1dbcc3530 | -6.8711 | -59.03101 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ab0550c-a36d-3f2a-97d5-5a4744ce39a6 | -8.40535 | -62.70018 | 2026-08-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be0db670-4fdd-3af5-b145-47fc8a17d13d | -7.5488 | -55.5952 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06402bc0-0ae3-3457-86b7-61597887c2d9 | -8.09272 | -51.66617 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08734bc7-f0db-3950-bf76-1f99a91fabd7 | -7.77585 | -61.16001 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c96b765d-00c8-35e6-8d06-197ca816a81e | -8.56013 | -54.6745 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbabb13f-d158-3aee-8dd3-b5bb1dbd464e | -12.48735 | -54.72223 | 2026-08-20 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1e3a07f-5777-312a-b74a-21aba296b0c2 | -8.52724 | -54.86761 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11afd0fa-d287-308a-a6ec-2ab84570a3fc | -9.13634 | -60.61515 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc8fb7a2-a850-3285-a64b-6b57e079a1d0 | -9.22318 | -59.77315 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56387f2f-4baf-3003-926f-31356cfa4832 | -8.56258 | -54.79482 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 577b3bfb-f257-37d4-827a-3185e5344976 | -12.79936 | -48.43252 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README47.md)
