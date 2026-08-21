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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e00831c7-8564-3317-a9ca-560e88dce522 | -6.52037 | -45.90509 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1888a82-7da7-3952-aada-0849222798b7 | -6.39137 | -54.93769 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb66b1d5-b835-3b09-8e2f-58ea253973d5 | -6.89848 | -58.98982 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| edfe7a0c-6bb4-34f0-a753-0479415deb45 | -10.76742 | -50.31466 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e50ab366-815f-3b88-a8f9-092374619493 | -7.72391 | -46.15409 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f21df57b-147c-340c-ad93-bf89fb5927df | -9.45034 | -51.60404 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce7298b0-2c9e-3504-92d5-81c72015771c | -7.15441 | -43.75297 | 2026-08-21 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2478c44-2faf-3767-a8d2-295119cae024 | -9.06937 | -50.88012 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44ec36e3-51ed-3537-b6af-ffe445c3ca5a | -9.44709 | -51.62491 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| beddf212-12e6-3703-8bfe-77ea586ebe48 | -7.37759 | -45.81982 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 21597ee2-b024-3f0b-ba84-f8df00a4ea77 | -8.589 | -54.78193 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 022956fc-8943-357e-a668-01b592b29ba3 | -6.38617 | -54.94608 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73ff5e36-cc2b-3d97-87a9-fe640a07f462 | -6.11621 | -59.91624 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da6af557-bdea-368c-bdb8-cb586bf612be | -10.53248 | -50.82269 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2d26d55-f90e-34ab-82a4-af2a2e0c043d | -6.47516 | -43.53961 | 2026-08-21 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88de88ff-780c-3fdd-a244-91757c0dba59 | -10.27777 | -50.28352 | 2026-08-21 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e8a7386-5797-3fc1-b874-5f5d2f96240b | -6.23889 | -55.39911 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fe921a3-1c8f-328d-af54-d542496b0072 | -9.45148 | -51.61847 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3651c2a-35b8-3843-b81e-c18ae7579274 | -8.59222 | -54.73971 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a464fd3c-2956-31a7-87fd-1658318e55a4 | -6.57872 | -56.36838 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55df6e5c-be98-3396-a437-08f062e01e06 | -6.43006 | -52.73069 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20fda87a-91a8-38c5-b710-9ff0f011fa28 | -10.45552 | -54.6637 | 2026-08-21 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 687f9b03-61d7-34a0-a3e3-8be17480ff9d | -6.23045 | -55.40254 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c24c372b-12ef-3d91-bc4f-e9370a872c6e | -7.96074 | -52.42813 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f522a6f-1fd8-390b-bc84-f4938817a46f | -9.24615 | -59.81003 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11f8400b-a192-3a2b-8969-1b0909456439 | -10.82459 | -51.00022 | 2026-08-21 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7cb8d4a-5998-3525-9fa8-f2476ce47fae | -10.79742 | -50.27729 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aa2b5d50-5d74-3740-8dee-fd6db9e9e476 | -8.03353 | -51.79491 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08e4a48f-38a4-3613-b256-ea19ec8734fb | -8.11171 | -50.03106 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 964b9997-d7e3-3628-baaf-fba9be2b6405 | -7.60604 | -60.95664 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 848b7e83-558a-36ad-bea2-1d2913a899a4 | -5.60457 | -44.00296 | 2026-08-21 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0b849d61-2292-3e45-88cd-d7dfaeba9374 | -9.06163 | -60.43993 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 763902da-cebb-3a5e-acce-1ce0ec95ebc8 | -9.41372 | -60.4216 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 235ff48e-0c07-37bf-a3ea-de9b9177267b | -6.55097 | -56.26101 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2500ab9a-b2f2-3349-be12-010822b10b3e | -9.27075 | -45.64701 | 2026-08-21 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4811487e-4669-37b5-842f-225c50a4b5be | -9.41826 | -60.42553 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dab6e444-1a38-3610-8089-2c0915b5b2e1 | -8.6697 | -54.57935 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a92d302d-b902-3497-8778-a6e3674ba0be | -7.25736 | -49.88649 | 2026-08-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e3eeee3-0f23-3a33-9444-dbdcfc6fefc1 | -7.35316 | -45.81232 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6fe67785-ca3f-3db3-9801-291ebfa32fc3 | -6.57928 | -55.44645 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bd7289d-130c-3b29-a326-614a12917d1e | -4.53363 | -55.61909 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 377fd487-109b-3d29-bbcf-636e5579b481 | -7.35623 | -45.82056 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3e9b9e5e-8295-33dd-8999-ea946e2d3970 | -8.11005 | -50.04206 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea061d8b-be8e-386d-a1ed-a0a98442f1f4 | -6.12143 | -59.91708 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6aa0a04b-0d8b-39bf-8d08-e845d5a65ec0 | -6.86691 | -59.02839 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 34d4028f-cb0d-3eed-98e3-aa167b2b5ac9 | -6.70638 | -59.09754 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63348118-a80a-389f-b48b-6a30c3aba5d6 | -9.39285 | -60.56325 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c07be13b-5299-3c91-9be7-fc9d12fac991 | -7.63872 | -42.73085 | 2026-08-21 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1e54a637-cde0-3d92-8e03-986230895b3a | -5.59931 | -44.00707 | 2026-08-21 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 8ddad3ee-93dd-39c9-be78-4b391a91b3f5 | -6.42833 | -52.74158 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04139a47-dda3-3fd5-b7a0-43191dde8dd7 | -6.35946 | -58.34228 | 2026-08-21 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2202d657-0921-39ad-bf83-68206ff12df8 | -7.2546 | -49.90469 | 2026-08-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4814cb9a-13dc-3538-897e-92ddb807b69c | -9.21299 | -59.76982 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 56b28671-34a6-3c70-b539-966819120322 | -7.06843 | -59.97119 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6f7dec8-e7f4-3949-9c7e-54212add9910 | -10.75031 | -50.33181 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1ce67ff-c8c3-3a42-b8e2-8f3fecd50f57 | -6.12251 | -59.91074 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f6097ac7-8787-3a1b-ab7a-ab24532e4a7e | -6.97455 | -59.59097 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcbb88b7-70cb-30e9-b90e-f32ba74271ef | -9.45377 | -51.64736 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 609c8c7a-ff8b-3006-b5a1-f930d999b0ab | -10.76909 | -50.30347 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d10ccbb-814b-338d-801b-55512ba10697 | -6.44296 | -52.75882 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 116b50b4-a62a-3eb8-b251-2fc1664e5d8b | -7.27693 | -47.45702 | 2026-08-21 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4326dece-f750-3fd4-96d6-44f687d594e3 | -9.98769 | -53.93494 | 2026-08-21 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aac58f59-0a4b-3310-958b-57fa5547fcdd | -6.87652 | -43.74621 | 2026-08-21 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2d8e06b3-f92f-3182-be13-f929c2a2442d | -10.75063 | -47.90542 | 2026-08-21 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f4b9bbb-7b4a-3f34-bc8b-cd29c118432c | -6.16605 | -52.48897 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef242d8e-c0cd-3093-8b8d-3af874d39ec8 | -9.41567 | -60.55461 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1572d65a-ec6e-3391-b027-9c36bea9eac3 | -6.25142 | -55.40866 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1966a5bc-76a1-3ab2-93ab-8564d0d5d2be | -7.35678 | -45.81675 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| cf759791-71ca-3e95-a82c-9ce3373f3790 | -10.62392 | -51.62164 | 2026-08-21 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abc12b0f-27ae-38bb-bf0f-b789d2cff4f8 | -9.07124 | -60.43 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca6bba5e-1016-3383-ae9a-4e361b3b8678 | -6.65844 | -56.34185 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c9a2ff2-f888-3dd5-91ea-5e61f05e800a | -6.43241 | -56.1904 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fca70c0c-3a73-32fd-a316-2b050051f56f | -9.46092 | -51.64492 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bbc46f2-9b34-3379-9dca-087b82faab06 | -6.9652 | -50.42002 | 2026-08-21 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e113ce49-8418-34f9-9533-0b5495c33dc8 | -4.91673 | -56.25913 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cd72d78-4ea0-36e2-845f-77efe04ec38c | -10.27042 | -50.28618 | 2026-08-21 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 282312bf-8905-3f5d-939e-6e22cb783a71 | -6.21794 | -55.47974 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75cf63b1-ce38-349d-ac92-a2ff09a620d1 | -7.60174 | -60.82667 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cec8dee-728b-329d-8ff2-e3b0e828b64d | -6.572 | -58.97087 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5a2bed1-7b1b-384a-8819-92276866e4f5 | -9.0511 | -50.88815 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4cfad221-8ae8-3c44-9d3c-2c3d5b7ba78d | -6.43453 | -52.74629 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 923ec08f-4364-3d96-b39f-81bdedf48055 | -6.2249 | -55.48579 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61cd1931-fcc4-3c8e-9f48-960a8cb90d81 | -8.58863 | -54.73912 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22ab3877-420c-3bf2-98fa-b06369783402 | -6.89044 | -56.42844 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b728b1b2-eb2c-30a6-b56f-2ea5008b285c | -10.75784 | -50.33223 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c10c6632-e2f9-352c-b398-c8febe59e301 | -10.74634 | -50.335 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e77f3065-f240-37a7-bf62-50ef3fde1622 | -6.85657 | -59.43957 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88e77d82-b286-3bcd-a8b1-10c29b4468a0 | -9.41937 | -60.41945 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 625440f6-fd52-31f7-bf54-10517ba9ad88 | -10.81844 | -50.99559 | 2026-08-21 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a300407-dcaf-3ba0-bc05-ca43f3e17889 | -9.40637 | -60.43294 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 935b0c6b-c7f6-31ed-92ed-6a3afaa481b0 | -6.81246 | -59.39848 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5690f42f-2eb7-37d7-a640-6b14abb08b69 | -7.73206 | -46.15556 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93787515-106e-3de9-a9ff-8f123740ce21 | -5.82193 | -55.71314 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d9dee54-a52e-3c95-abe9-dd735f9accbf | -8.39438 | -62.69858 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fad9581b-1d1f-31c4-ad55-81b0487ac99a | -9.06841 | -60.43158 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abd4f6a8-5e22-35e5-b91c-d514d9699736 | -4.97316 | -50.89927 | 2026-08-21 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 123d9234-1d51-34c2-882d-b9883e7c8cf1 | -6.97506 | -59.58808 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dd33556-6c6a-33d3-83fd-1724f5b3e62c | -10.36196 | -48.24181 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd73d198-9fb0-3500-82c4-e1a5d326224a | -9.40749 | -60.42686 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 936d22ec-d10a-3d4e-bcf8-87d1148be980 | -7.74001 | -61.09465 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README40.md)
