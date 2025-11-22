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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7500569-334d-370e-9348-a409a4155509 | -10.07134 | -63.05953 | 2025-11-22 05:37:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d8ebce1-380f-3178-9142-6d8a4a21a75d | -9.77686 | -67.04726 | 2025-11-22 05:37:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6131ae2-fc63-3ba8-814a-e890154ccd60 | -9.81905 | -63.24327 | 2025-11-22 05:37:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1909b2f-619e-34b3-b5e2-5ab6c5dc042d | -9.58426 | -64.31553 | 2025-11-22 05:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 639f32be-6d71-3854-9bf9-1d599c0eeb32 | -9.81849 | -63.24686 | 2025-11-22 05:37:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2751f70-3106-37d6-ac82-0af9da66ae43 | -10.64398 | -61.38852 | 2025-11-22 05:37:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b9968a7-40f1-39b0-871b-268ec2496fec | -9.77622 | -67.05118 | 2025-11-22 05:37:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1735fb3e-85b4-3326-881d-5c8441c26e94 | -9.78887 | -64.63428 | 2025-11-22 05:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ecba8d62-4e46-31b9-b995-7a48f139e94d | -9.8224 | -63.24381 | 2025-11-22 05:37:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 561fd255-5f88-3c7e-a8da-9837037642df | -20.23947 | -56.62493 | 2025-11-22 05:40:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 42f39431-9422-3c47-a77d-9a66f905f6e7 | -20.23986 | -56.62094 | 2025-11-22 05:40:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| aecefe50-2d7b-39ef-8d49-4d6e147d7b5c | -20.20612 | -56.61731 | 2025-11-22 05:40:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1f68b673-4379-3e5c-b631-a416f0209bf5 | -20.24509 | -56.62553 | 2025-11-22 05:40:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0d3c853c-4b90-3e99-bca6-e9ea77c13077 | -2.91111 | -48.23303 | 2025-11-22 05:54:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9219378b-13b5-39b8-a35a-addcb3440ab0 | -4.02758 | -42.51188 | 2025-11-22 05:54:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| eac8579d-edb0-31ba-96bb-a35314249060 | -4.46789 | -44.55968 | 2025-11-22 05:54:00 | AQUA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 55247653-9a45-309d-be19-45d5472c240c | -4.47878 | -44.55894 | 2025-11-22 05:54:00 | AQUA_M-M | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0512ee60-9e24-3b0a-86e5-643f1d5f5e83 | -4.03656 | -42.51318 | 2025-11-22 05:54:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 5439a295-9ea1-3ac4-aad7-fee4a99e4102 | -4.0262 | -42.52106 | 2025-11-22 05:54:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c1588f3f-a10d-3d1a-a4f3-2f146145c8bf | -4.03518 | -42.52234 | 2025-11-22 05:54:00 | AQUA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| a57e3c2d-380b-3a5d-9ed5-bbca378d7032 | -4.46656 | -44.56852 | 2025-11-22 05:54:00 | AQUA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38b93d45-f854-3a7b-9187-7a34d8f9b36f | -3.45892 | -44.99827 | 2025-11-22 05:54:00 | AQUA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e0cfa2f5-b49a-3551-a7f4-0b72b53d3fbb | -3.45063 | -47.62554 | 2025-11-22 05:54:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 62d1a11a-75e2-36dc-8556-5c26fa327676 | -2.92437 | -48.22042 | 2025-11-22 05:54:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 10b915a6-a491-392f-b020-a35c1cc2ba11 | -3.17448 | -48.60764 | 2025-11-22 05:54:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fa8e82e5-a15e-321d-bc31-c30edb6d0876 | -4.14699 | -43.70012 | 2025-11-22 05:54:00 | AQUA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 57f45ccf-f710-37d1-9f24-8273b8032bda | -3.17702 | -45.33229 | 2025-11-22 05:54:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 85cf28aa-8eb6-353f-ae84-e6e45a52e77e | -2.91334 | -48.21883 | 2025-11-22 05:54:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b51fd016-73c0-3228-9f4a-e5d1b30e7997 | -4.14831 | -43.69138 | 2025-11-22 05:54:00 | AQUA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| f4095de3-7696-3b39-887e-e2d9f740c38b | -3.31893 | -44.08529 | 2025-11-22 05:54:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 6c807e94-88e8-3363-82cf-828d93dcfb2d | -4.47744 | -44.56777 | 2025-11-22 05:54:00 | AQUA_M-M | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2787e6b4-80f9-3802-84ff-78b1a0e4dd20 | -4.46922 | -44.55084 | 2025-11-22 05:54:00 | AQUA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ed154e98-fb33-3a59-8b81-6f0d8556faf5 | -2.92216 | -48.23462 | 2025-11-22 05:54:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 1cae5fbc-cda6-3e23-aa2d-f244d51e20ef | -17.38077 | -42.62724 | 2025-11-22 05:57:00 | AQUA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 8f847e8f-a699-389c-a865-eb750d863ade | -17.37362 | -42.63435 | 2025-11-22 05:57:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 75290c5e-b678-38b8-a09e-0d215cbfbc2e | -20.88183 | -52.33851 | 2025-11-22 05:59:00 | AQUA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 3bc169b0-e80b-3760-b48e-5912e9a40350 | -21.52009 | -42.26371 | 2025-11-22 05:59:00 | AQUA_M-M | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 48.5 |
| 0d5f5b9e-8c15-3e81-9a0d-9ab6e00473a6 | -20.88752 | -52.33011 | 2025-11-22 05:59:00 | AQUA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2c7e13f9-acae-398d-8ae9-b470a76fb8c8 | 3.10968 | -60.77066 | 2025-11-22 06:24:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 27.1 |
| b4503d66-1eee-3d8b-87b0-ca2df111244c | 3.11664 | -60.76947 | 2025-11-22 06:24:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f2fea894-cad5-3fce-aa98-4e3a4bcf2413 | 3.10856 | -60.76409 | 2025-11-22 06:24:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 71806caa-eb6a-3487-b1cb-415ac06eec06 | 3.11551 | -60.76289 | 2025-11-22 06:24:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e4e0e5d-4388-3917-bafc-96bdeb6af18a | 3.10902 | -60.75594 | 2025-11-22 07:30:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.0 |
| e959ec3b-6212-3738-b924-77d85a58ca96 | 3.10848 | -60.76305 | 2025-11-22 07:30:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4d700b6b-63f4-32a5-ab90-6b2cf2b7e473 | 3.12103 | -60.76119 | 2025-11-22 07:30:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 40ef8e0d-ef2f-3900-87ea-cb4b6249f056 | -3.4441 | -45.2383 | 2025-11-22 10:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 7d59f370-0820-3904-8a3b-578e09a35912 | -3.4442 | -45.2157 | 2025-11-22 10:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 216.5 |
| 5def5f90-b36e-3445-9c98-5dfc13f9f9f6 | -3.4628 | -45.2149 | 2025-11-22 10:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 97810ac3-e81a-39ee-81e4-18de8c5558e2 | -3.52231 | -41.60119 | 2025-11-22 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 51.4 |
| a7ec9324-2c4c-3579-8100-c41aae23f0f8 | -6.75474 | -35.0944 | 2025-11-22 11:36:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| ba87c90a-415d-3036-9b15-f4fbb6c7b2a4 | -3.61316 | -41.97454 | 2025-11-22 11:36:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 149.0 |
| 47eb03fc-c981-37ff-aab3-1153e8db7395 | -3.49047 | -41.63021 | 2025-11-22 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 49.8 |
| c72ae77f-9209-3859-8272-2f57aafbad77 | -3.7603 | -42.14977 | 2025-11-22 11:36:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| eba79d51-59f0-3d5b-9ba7-e11b9a1eac49 | -4.7618 | -37.77599 | 2025-11-22 11:36:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 1a9731af-8d12-37c8-bd65-6b8b403f13f9 | -3.61517 | -41.96095 | 2025-11-22 11:36:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 28775f83-efae-3056-9234-fd3c5b23239a | -3.76339 | -42.2808 | 2025-11-22 11:36:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 180.8 |
| 3bffa4ed-0635-3a2f-a58a-f36d791791da | -5.50385 | -36.83794 | 2025-11-22 11:36:00 | TERRA_M-M | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ae50b051-041d-3d4a-809c-8d195b4166e1 | -5.25907 | -37.13223 | 2025-11-22 11:36:00 | TERRA_M-M | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 64e0920c-f2ff-3885-b02f-68a8ba40ceed | -3.49238 | -41.61717 | 2025-11-22 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 9da209cf-7f48-3b54-bd6a-d5299dd660b0 | -3.57797 | -42.21254 | 2025-11-22 11:36:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| f68bb253-2c64-3e57-9e42-66dc07a4c018 | -3.76126 | -42.29527 | 2025-11-22 11:36:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 29.4 |
| fd08e5e6-6fa2-392d-85a8-b9e56401e62b | -3.52781 | -41.59585 | 2025-11-22 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| c5f656e9-ce54-3375-81e4-fc61f4b9948b | -3.76238 | -42.13576 | 2025-11-22 11:36:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 132.9 |
| 18f44a62-a0c2-30f1-a0c1-19ca8709e76b | -3.57587 | -42.2267 | 2025-11-22 11:36:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 6816ca2e-a5e9-3ff5-aedb-111267a1ec6d | -3.52595 | -41.60878 | 2025-11-22 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 6addf100-751a-34aa-8a95-d6fb16d9dca0 | -3.74281 | -42.6578 | 2025-11-22 11:36:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 1427bbe4-ba48-30e6-ad05-08f855b1abdf | -3.98075 | -42.525 | 2025-11-22 11:36:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 207e985d-7129-3c6b-9a99-b2ff894e85ef | -4.52071 | -38.16791 | 2025-11-22 11:36:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 873903cc-2111-3755-b577-c6f92aa8dbc0 | -3.49321 | -41.5383 | 2025-11-22 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 8ac6e92e-70e8-3f99-a235-35566567dc2a | -7.79441 | -37.73715 | 2025-11-22 11:38:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 38f12bdd-2441-3140-ba22-bd1008b0b867 | -9.39361 | -36.90891 | 2025-11-22 11:38:00 | TERRA_M-M | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 9.2 |
| cd78c225-120d-3393-91d7-bb4ed92858ba | -10.48946 | -36.79057 | 2025-11-22 11:38:00 | TERRA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1b3f85fd-8332-3b84-b6e3-0b894914c33c | -16.015 | -38.93393 | 2025-11-22 11:40:00 | TERRA_M-M | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 618258b1-9bec-3d64-bb9a-9ea327ae63b6 | -16.02401 | -38.93522 | 2025-11-22 11:40:00 | TERRA_M-M | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| bde491f1-b1d3-3c75-8a00-7de336ab5e32 | -16.20558 | -43.70462 | 2025-11-22 11:40:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d8dccf33-a2b6-3a69-a8f2-d511bcad2207 | -16.75593 | -42.34892 | 2025-11-22 11:40:00 | TERRA_M-M | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| d443a648-5801-3ed5-9a65-8f475d4b1509 | -19.21316 | -40.11963 | 2025-11-22 11:42:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 5bef9161-7da9-3166-a482-a506ac731018 | -19.20426 | -40.11829 | 2025-11-22 11:42:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 43.7 |
| cbe38881-b3af-38f7-93de-e6694f936f35 | -20.03037 | -41.31764 | 2025-11-22 11:42:00 | TERRA_M-M | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 7826874f-14ab-3713-9f48-ebaf8fb0e755 | -20.16292 | -41.85975 | 2025-11-22 11:42:00 | TERRA_M-M | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| dc682fb2-7775-3ee1-9b00-c4fa33e34dbc | -18.30648 | -43.85712 | 2025-11-22 11:42:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6d1fe9a6-5376-35db-8e51-8bdb5fb80184 | -19.31321 | -40.06318 | 2025-11-22 11:42:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 564e6e44-49e5-34ad-9e1e-f2b57a4b21c7 | -20.03171 | -41.30833 | 2025-11-22 11:42:00 | TERRA_M-M | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 4c9a0730-2346-397a-aee9-918ce5a3238b | -18.50682 | -41.94614 | 2025-11-22 11:42:00 | TERRA_M-M | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 6312efed-da15-3c2a-8c0e-725f13f47c4f | -19.23811 | -40.59884 | 2025-11-22 11:42:00 | TERRA_M-M | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 37e6a27e-757c-3495-95c3-378c4b30c75f | -19.23944 | -40.5895 | 2025-11-22 11:42:00 | TERRA_M-M | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 19c34e93-64ed-366e-a1d3-6ebfc4625d73 | -20.8927 | -52.33 | 2025-11-22 11:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 3e5c6574-2563-3f7b-9103-9317b75c63b2 | -3.4033 | -42.4276 | 2025-11-22 11:50:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 1680a5af-ca9b-3a31-b742-1f39cd98a987 | -20.8927 | -52.33 | 2025-11-22 12:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 251.8 |
| 7189a8c2-184d-3e32-a925-23c5d4eba329 | -20.8722 | -52.3339 | 2025-11-22 12:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 17f5df6b-2c0f-3738-a8c5-3b0c6000cf0f | -3.4033 | -42.4276 | 2025-11-22 12:50:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 75ff0c1b-8f61-3704-9a75-fdcef252e94c | -20.8927 | -52.33 | 2025-11-22 13:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 526.9 |
| 649c7407-f801-3dac-94fd-c46cadc35466 | -20.8722 | -52.3339 | 2025-11-22 13:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 09df3bbf-4d1f-3fcb-a9be-e592ed8705f3 | -20.8921 | -52.3522 | 2025-11-22 13:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 144.3 |


