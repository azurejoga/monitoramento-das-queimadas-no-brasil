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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6557405-3c94-3edb-bc2e-530c32072b11 | -6.94445 | -52.79235 | 2026-08-26 12:12:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bae2ba03-161a-3b14-8aff-0550bc3a16fb | -6.30786 | -53.57037 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2ae6bcbc-f44a-3005-8f3d-064a3d8b09ae | -9.73201 | -49.35165 | 2026-08-26 12:12:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 6df4b80a-7285-3fc2-96f9-b385359bbd0a | -7.7592 | -44.74446 | 2026-08-26 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 87537d19-903c-3f86-b9ea-b658ea3b1641 | -10.04369 | -46.02671 | 2026-08-26 12:12:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 98a99c89-4698-3c2d-a97d-a22add159aa2 | -8.06543 | -47.53234 | 2026-08-26 12:12:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 4994e688-42a1-3e31-ad75-421daf9e4b05 | -6.27009 | -53.37886 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 12250f09-01d3-3209-a808-2dc61e6ad79c | -10.04044 | -46.04553 | 2026-08-26 12:12:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a154fade-d935-3ab8-b0ed-d2dbb93af456 | -9.65805 | -55.09122 | 2026-08-26 12:12:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| d1023a1c-71fc-3b8e-a39d-c79ea7822eac | -9.08129 | -50.60494 | 2026-08-26 12:12:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f14a75b6-3088-393c-8f73-585b4dd6b9d3 | -9.71139 | -49.33371 | 2026-08-26 12:12:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f7f8b89e-8eca-3e34-9d40-1cb8b0650e25 | -6.50958 | -53.2603 | 2026-08-26 12:12:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1d86c948-e308-3a29-ae8a-75d9e2be14e0 | -9.57956 | -49.28967 | 2026-08-26 12:12:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 04a9f1c7-dbb7-3614-89f3-9b33bfaac67c | -6.23339 | -55.48163 | 2026-08-26 12:12:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4592c1b6-db58-3f82-a3fa-85ae49aa0484 | -7.0655 | -59.2253 | 2026-08-26 12:12:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 0a9b7d2d-afa4-3a9d-bfd4-2f6ef701c793 | -7.49653 | -55.35598 | 2026-08-26 12:12:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 680db199-a546-326c-b0d7-059f563be4f0 | -7.37918 | -55.15279 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 8d5abfdd-6eed-30ea-b216-b07395c32bfd | -9.60785 | -55.11504 | 2026-08-26 12:12:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 511cb47a-eb1a-3a02-8d5d-64fdb4bbb3b2 | -8.27158 | -46.34714 | 2026-08-26 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2cf819fe-8cee-3cf8-b80e-ccd4b1751e01 | -7.38824 | -55.15422 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3db670f7-384e-35f3-bba4-2be4751d751f | -9.01719 | -50.77582 | 2026-08-26 12:12:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 804d39ba-bd4a-3205-b512-c421cf9b65d1 | -4.80521 | -43.14107 | 2026-08-26 12:12:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 91eb4654-5918-3982-a877-c652e97ae3ff | -8.85978 | -49.71954 | 2026-08-26 12:12:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 35f1c406-bc4c-3863-8b6c-393432581565 | -6.28143 | -53.36246 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| aad9b184-6ea8-3a4f-91a9-f73d797793ae | -6.69474 | -58.71761 | 2026-08-26 12:12:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 87d74e32-898d-367e-b322-1eed54694c19 | -8.10158 | -47.56212 | 2026-08-26 12:12:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 05a7cb87-98bf-3578-8568-2d6d51e68b1e | -9.5702 | -49.27323 | 2026-08-26 12:12:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| d1d9dcaf-ca00-381d-bd6b-1f37e4b4f708 | -6.23312 | -55.61391 | 2026-08-26 12:12:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 08cf71b6-7054-38ed-9a77-ff9ca82e5bf0 | -6.68656 | -43.41398 | 2026-08-26 12:12:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 173f02fd-e003-3eb1-b2ae-b4a460a9773a | -8.58858 | -54.83413 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 770ec4d6-bed3-3f59-9444-bb768e93ee93 | -8.15968 | -47.5105 | 2026-08-26 12:12:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 52a80898-01a7-3a8c-aae4-2f806c8d04d8 | -7.00406 | -59.30395 | 2026-08-26 12:12:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 9dfea9c1-ae98-3da9-8443-107e0c058dc4 | -9.57213 | -49.25806 | 2026-08-26 12:12:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f17f6dbb-23c4-30f6-a7eb-6fffb6da7a05 | -6.14627 | -57.70918 | 2026-08-26 12:12:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c1c8fae1-5722-38d6-a4e2-ab85d01b4cfc | -9.59892 | -55.11376 | 2026-08-26 12:12:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 487bcdc0-987f-39ad-9023-beff5c19f1d2 | -8.17451 | -54.94828 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| ec8112e5-b46f-3376-bdb1-aa011d4cfa6c | -9.01559 | -50.78781 | 2026-08-26 12:12:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7e115584-d12a-3e92-9392-ecd4655d2c62 | -8.14694 | -47.50885 | 2026-08-26 12:12:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 810db86a-1fdc-342b-b126-01e022d0d451 | -9.7339 | -49.33676 | 2026-08-26 12:12:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 503f7cb0-b226-39fb-aab9-b8ea58447a5d | -10.04078 | -46.05188 | 2026-08-26 12:12:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 8746709a-9513-3959-b1a8-ea46e588b84b | -6.83662 | -52.50681 | 2026-08-26 12:12:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f535174b-821f-36a4-b467-3714b11c63eb | -8.17583 | -54.93919 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| bb947618-51eb-3e03-8132-3eecc808ec7e | -8.76047 | -49.94379 | 2026-08-26 12:12:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b9c11b7e-b3a7-337b-a7b2-827e0822ce03 | -8.81549 | -49.60986 | 2026-08-26 12:12:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| a605c33a-5440-36d6-a450-8f6c30b0be2f | -8.15123 | -54.9824 | 2026-08-26 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 95a46a93-3b5c-3f55-9301-ce49695c2181 | -4.80053 | -43.1794 | 2026-08-26 12:12:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| c69a75dd-be04-3613-b8ba-6f7ca7aaf7f9 | -8.14941 | -47.48925 | 2026-08-26 12:12:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 1636d46e-232c-33c4-b050-c8f38db71a9b | -8.27655 | -46.35322 | 2026-08-26 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9222073f-962c-36de-a2c6-99ab2acff107 | -13.24377 | -51.53809 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ed180552-a111-348c-972e-ec65da826266 | -13.86257 | -53.97818 | 2026-08-26 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 950610c5-90fb-3cfa-ac27-8e0b0192bfbb | -13.86127 | -53.98751 | 2026-08-26 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 710b0b45-2e8e-317f-93e8-0662dfb4ac55 | -12.64152 | -48.40332 | 2026-08-26 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e54d55e4-b8cf-36e4-95e3-4aca3ace1852 | -13.24532 | -51.52616 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| ad3754d6-0600-3299-ac4a-7a75f20e0192 | -13.27432 | -51.38275 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.3 |
| d5a1f6b0-53e2-340e-bf6d-d2977e514c53 | -12.65425 | -48.40483 | 2026-08-26 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 4e54b267-62a2-3883-8bcb-f2ec43da0f28 | -11.61107 | -46.7482 | 2026-08-26 12:14:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 81927e8a-b4dd-347a-aed9-6f8338fa53e7 | -10.76016 | -54.0309 | 2026-08-26 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 18644119-15d7-3a01-93d9-e43d592a14d3 | -11.41933 | -44.55411 | 2026-08-26 12:14:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 245.1 |
| 79c96036-1671-3736-bd41-9e629ebaab69 | -12.16287 | -50.59054 | 2026-08-26 12:14:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| f2292053-0fbb-3211-be3b-54753bd549af | -12.76313 | -46.46487 | 2026-08-26 12:14:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1da1f97c-0b6c-386a-8992-ba580f8b503b | -9.96969 | -53.9453 | 2026-08-26 12:14:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3278d1b2-2f3c-30c5-ae07-0e54f2c4652c | -14.39837 | -51.7573 | 2026-08-26 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 8163eda0-ed5d-3a74-9d66-e8395413c50f | -15.67092 | -48.2089 | 2026-08-26 12:14:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 9e2fd69b-dbb6-34f6-8724-56336838fad5 | -14.53394 | -52.28235 | 2026-08-26 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a90a061a-7c08-3bc5-9bda-b56331e29e04 | -13.19452 | -51.29107 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d4641f42-c249-38f7-880a-b432db294e56 | -10.75889 | -54.03986 | 2026-08-26 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| abee1f9c-c8a8-3450-847b-2266415ced75 | -13.61499 | -49.00008 | 2026-08-26 12:14:00 | TERRA_M-T | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f07da0ef-f256-33ec-bf1c-8e54e25c2d87 | -12.65185 | -48.42442 | 2026-08-26 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 85055932-2583-35f3-a17c-e119cd31d9d4 | -13.20315 | -51.3047 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 206ef6a6-30cc-39c1-8d59-cd4059fe4d1f | -12.64151 | -48.4104 | 2026-08-26 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f8b4df3d-9d12-3222-b651-cf73104cc814 | -13.87006 | -54.0613 | 2026-08-26 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2b827158-74cb-3fea-bec9-f3a05494c964 | -13.32551 | -51.4571 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 3ddf843a-eb29-3ca1-8207-c931c3b611ee | -10.99916 | -51.14843 | 2026-08-26 12:14:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 77cfcceb-78e9-30ea-8209-6d6841161c08 | -11.28731 | -47.06805 | 2026-08-26 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 9f5384b8-acfd-3f67-93cf-b3187fb13836 | -12.65422 | -48.41203 | 2026-08-26 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 77f07982-8213-332c-b7f7-fb4503cd062f | -15.59013 | -56.40607 | 2026-08-26 12:14:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f83ee5a3-1d69-3616-a3fc-a775a7471224 | -10.56228 | -50.44524 | 2026-08-26 12:14:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| db5e5af9-4f54-3293-9c1e-21859899a2b5 | -15.60068 | -53.10168 | 2026-08-26 12:14:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9ab26024-c15c-394d-8689-12ed42fa43db | -12.69238 | -48.41676 | 2026-08-26 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 9f2c2f23-bae9-3ed2-a932-bd4acdd86b5a | -14.79579 | -48.80689 | 2026-08-26 12:14:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| af5feeca-1ba1-371b-a26a-b55de394a676 | -10.76143 | -54.02194 | 2026-08-26 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| b46f7ed4-51d3-35e3-b834-d16222a4afdb | -11.42728 | -44.52328 | 2026-08-26 12:14:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 281.5 |
| 39c781a2-8d6f-3939-9226-9803e0c3215f | -13.32706 | -51.445 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| a2786c8b-a47b-3d3a-95dd-36758ffc8f1c | -13.20854 | -51.34288 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 81ee2065-9fac-3af8-a624-49792bb69ad9 | -10.76651 | -53.98608 | 2026-08-26 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bffcdb6a-1e49-36f0-a24b-9c764fb388e6 | -10.77028 | -54.02319 | 2026-08-26 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a9c2f552-e588-3928-9741-3aeaca4d2ef2 | -13.86494 | -54.03222 | 2026-08-26 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2f10c82b-647e-357a-bdf7-a428d8d68a42 | -13.2775 | -51.35832 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 45fc7773-09c7-30aa-804f-71a80a82e691 | -13.2091 | -51.32447 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 18e20782-a496-3bc0-affd-e6b8ded28ee4 | -10.65442 | -57.25154 | 2026-08-26 12:14:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 22d773b4-5345-3dc6-aa98-f0388c6d4262 | -13.22088 | -51.31352 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| be2e9421-a875-3fe8-a008-f2b543d8684c | -13.21501 | -51.29373 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 872a3f88-8d6f-3fc5-a4e3-a75957bf972d | -13.21016 | -51.3306 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 39ed81f2-349e-3f00-8822-4874ab0376b4 | -11.4235 | -44.51591 | 2026-08-26 12:14:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 200.2 |
| a738850d-88e1-34b3-a613-fee9a83a5907 | -13.31536 | -51.45578 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 190.0 |
| e6ccf960-1971-3709-9991-69e7be87d89c | -15.67897 | -48.21526 | 2026-08-26 12:14:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 7101988c-648d-3f4a-b5f2-1220e3716fe6 | -15.5915 | -56.39674 | 2026-08-26 12:14:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fe80ffe1-d853-3190-898e-690a48514642 | -13.85474 | -54.03419 | 2026-08-26 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 66122c64-370b-347d-891b-de2d8b4924e6 | -10.76774 | -54.04111 | 2026-08-26 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f8c07c94-e33b-3fb5-a02a-16a92ca5095e | -13.21177 | -51.31832 | 2026-08-26 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |


[Clique aqui para ver as próximas entradas](README79.md)
