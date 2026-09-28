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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e214052-812a-321b-8b2d-b0017904f421 | -7.67793 | -54.85249 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2b0dd98-239f-321b-a056-45c098637751 | -7.37459 | -41.79306 | 2026-09-28 17:09:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 34.8 |
| 85725abd-3086-3c7e-8713-9ecc49e514f9 | -7.98731 | -43.25446 | 2026-09-28 17:09:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 1f23e13b-b5b6-38b7-9320-5b2f73082319 | -9.45688 | -45.967 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| baac7b04-7565-3fae-b07a-8eef7a4c5144 | -7.38243 | -44.76866 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| a5d90f6e-a10b-3ea0-85d1-d9ab105354f4 | -10.92433 | -50.70889 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| bd1cb9a5-420e-35b0-987c-f001b9233508 | -12.76218 | -54.04816 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a57d8d43-1d83-3167-8d4a-103bf655bcf8 | -9.96833 | -50.13412 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5e9ec75d-5382-30f8-9893-c6c5588587da | -11.07424 | -46.08535 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0b23a346-1721-38cf-a21d-2948e33c9d7a | -9.297 | -46.45015 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8caad72a-f9de-383f-98d6-ffe8f242fd4d | -10.88353 | -54.03355 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 50bfa1a5-aa2f-3af0-b001-825bc0c059fd | -10.72418 | -53.9909 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c1d2612b-29b8-3fd3-88d0-0ce7ba5492a0 | -9.81946 | -46.28506 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 336c8655-b584-35dd-9ee6-5ab083e443e9 | -7.70101 | -54.76007 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d5e3d179-3612-3316-9c71-d54f655c8964 | -11.49866 | -47.3617 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| c534de56-a94d-3b7a-8e12-60ee2e5782f5 | -13.50669 | -61.13801 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c065b103-e29e-3695-8707-b975b2e73da8 | -9.94039 | -60.71658 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7476eeed-8fc1-318d-a36e-c48ebc630888 | -8.66475 | -45.37254 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b367b222-0588-3789-856e-4d281855c8e4 | -6.89205 | -52.47519 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6fb3a83c-c5a1-35e6-9bc7-bc2e7ce42b7f | -8.47527 | -44.65147 | 2026-09-28 17:09:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e03893d0-4e0b-3542-8359-49bf486593b1 | -11.54318 | -47.39454 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| b0a13c24-a4cd-3c05-ab27-efd83c41e1cf | -8.60158 | -48.37051 | 2026-09-28 17:09:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2b430cdf-e69e-3150-976a-a70093212609 | -7.44036 | -55.63464 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| c0416303-0ade-359d-af56-3f90e5edbca3 | -10.89287 | -53.93772 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fdd85c7d-d158-39bc-9258-7cb5605c8c75 | -9.77331 | -45.9774 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| cf224cdc-e6a1-3138-a87f-b8acfed5cd67 | -8.32971 | -45.41171 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 86577364-be21-3985-b12d-53ff7c5b1b5a | -5.85557 | -53.82651 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| aab502d0-a0ab-39a2-af6e-9c98e1772bb6 | -6.16321 | -52.81811 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 589e4cc7-fadb-3469-a2b7-042c48d73944 | -9.39872 | -46.38457 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 97f8a2e7-6c6c-3c17-ac88-b412308d0b6a | -10.82097 | -57.21811 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b8ca8510-679d-3abe-8c44-9e57f4a38cbd | -9.81087 | -45.71335 | 2026-09-28 17:09:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8928a7e-41a0-3c04-adc9-e80abd4272c8 | -11.15811 | -48.31904 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6120434a-94c5-30d9-89d3-d7e1723e416b | -9.49464 | -60.39216 | 2026-09-28 17:09:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| acdf56a4-863b-3256-9b8b-39fe488108ce | -10.90504 | -44.65767 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 1a48f321-c7ca-3006-b04c-6f3aaa2b931e | -4.94977 | -45.10702 | 2026-09-28 17:09:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d92585dd-766c-3a9e-a63a-8569700db635 | -4.95827 | -42.98992 | 2026-09-28 17:09:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e5f13f0a-36f4-3ea8-af4f-43a652861cba | -8.29534 | -54.73251 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4962b95b-2e34-321a-b367-44f504381cc1 | -10.82062 | -57.19268 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 8ff9d56e-b18d-3af4-ae5e-4ccba331e352 | -11.56578 | -47.39038 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4baa3881-28e6-3ff2-9670-5141c87f0be3 | -8.70585 | -46.83323 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a17bc74d-ff63-3db5-848b-35fd1c8f24ff | -6.14937 | -53.12496 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d36c528f-eab1-3aa2-ad83-e0255cebbee8 | -11.061 | -52.46455 | 2026-09-28 17:09:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 349cb1ff-1301-3ecd-8354-eebcf9bd5437 | -5.74475 | -47.38758 | 2026-09-28 17:09:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bada3aeb-7f1a-3490-8011-de684c068599 | -7.43386 | -55.63989 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 83da7186-3967-3543-9ae4-d47f8b78e878 | -10.92498 | -50.66716 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 76d99f9f-02a8-3bba-a362-2393f410ce88 | -10.08593 | -50.38918 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7958f999-dccb-3f29-8c13-cc2fd8957484 | -12.78211 | -54.02336 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 7a20552a-c7ef-3460-8b4c-14e0f205101b | -11.30251 | -48.7322 | 2026-09-28 17:09:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d22dd7b9-f122-3c15-8a0e-800387528a45 | -7.29496 | -44.31069 | 2026-09-28 17:09:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c78a345c-c486-3f06-8d5d-e641ebdb1a95 | -8.03403 | -54.89173 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7544184d-9273-37e5-94d1-e5af29f76324 | -8.75868 | -50.80318 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4629d3c3-840a-3c1d-920a-cbb29e2d872a | -8.23736 | -45.4672 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 59d4fc2c-fc2c-3340-8d08-437eeaaae382 | -10.08531 | -50.39194 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 67fcebd2-5f3b-345c-bd48-5ec1260d3b78 | -10.09357 | -50.38788 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 5ca3abc1-9c8e-381b-8b58-f18e21b83b64 | -8.71465 | -46.71222 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a05118ae-ce4e-3c2e-ab61-e6509a55da0e | -7.06672 | -55.48146 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 6b3a4a0e-fdae-367b-88fc-e929e5d4135f | -13.51074 | -61.13246 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c0d75487-43ba-3068-9053-17bdc93a6ccb | -10.69752 | -60.73877 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b98cefba-7b9c-3843-a333-05d35265393a | -5.77004 | -49.24566 | 2026-09-28 17:09:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| efed11c5-623e-3bae-8f97-641f48731fa9 | -11.0531 | -47.66642 | 2026-09-28 17:09:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6f9d77d3-ea87-3b25-a96c-6e005d07aed4 | -6.14147 | -52.7271 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9ff47be1-7edc-3a90-b5be-834a573f4e03 | -12.16036 | -50.38897 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c9603201-9b09-3698-8102-f7d38064fb1d | -11.53073 | -47.38447 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| fa0b77a5-2d06-3054-9185-e98c61f92214 | -3.93549 | -42.5537 | 2026-09-28 17:09:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 46fe470a-be72-31d6-bdec-826b4e5d0490 | -6.3545 | -45.80385 | 2026-09-28 17:09:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b155f4a9-4aae-3dce-8ccb-d087e73f9f6b | -9.96177 | -46.09926 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a52a821d-7e14-378c-bb6d-bc2eeaec1e26 | -11.20216 | -47.71114 | 2026-09-28 17:09:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 85ab6745-449f-39e7-b559-486f5dfc89f2 | -11.69801 | -50.03867 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| a5326dfc-c698-3de4-931a-474cf9147271 | -9.95669 | -46.10015 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f2f33ab3-3f68-328d-a315-f0537e5324a6 | -11.54885 | -47.37424 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 712890e1-d7b7-3fec-ba17-20deedc162b1 | -10.91422 | -43.87162 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 599fa324-f10a-3c57-a9a7-a930507dce4d | -7.45018 | -64.34933 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| afdd1319-708e-369a-88ce-21c44d5d7ba9 | -7.38527 | -47.01169 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e6247f37-8d9e-3c17-9483-742bef91c313 | -11.5788 | -45.46046 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 70690239-408a-35f1-891d-3fe5d28f11d2 | -8.55068 | -55.24978 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c34b656c-5be2-3001-b3e7-92f210e9a857 | -6.70668 | -45.67558 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 53b7300c-11fe-3374-9ce2-dd78617e325f | -10.92282 | -50.69991 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 29ed51b8-2416-3a75-8139-671d4296e013 | -10.45537 | -45.09079 | 2026-09-28 17:09:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cf06061d-d38f-3849-8377-899d1afab21b | -9.13615 | -49.97358 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 02473b24-29e0-314f-a998-f677e7def1db | -11.06159 | -52.46832 | 2026-09-28 17:09:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 32c171e9-53c6-3114-b008-72a75059daf4 | -8.48525 | -49.60219 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4d9663d4-5bb8-3044-9273-d50aacacd01d | -11.54969 | -47.37888 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 849e20fd-2b6e-3510-a5a2-57bce37f619c | -6.37802 | -55.13413 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 23cd07a5-2c71-30a8-a0a5-57b1987edf72 | -8.61121 | -64.06357 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f36ae89-60d1-34ca-bfa7-6c36bc1733e0 | -11.72221 | -49.13305 | 2026-09-28 17:09:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eca27a27-d5b2-378d-8839-c95bd340cb26 | -8.27678 | -54.7466 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b4b990ab-0980-3ab6-b5e7-aa155b76f5ee | -8.97774 | -44.15908 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 4eb7842e-8c22-3a8f-8e79-8f60fe199710 | -7.32041 | -55.00564 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| aa70d731-90e8-324c-ab14-b3da828d5aaf | -10.21025 | -50.01632 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| fa09b33a-57f3-3af7-9674-03d32d80b3fb | -7.12446 | -47.60943 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 50654c5b-758f-38fd-aee8-22bcbe9904ca | -9.95615 | -46.09718 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d97cee19-94f3-338e-99de-10d64bc9f05d | -10.11969 | -50.19727 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| fc9afdbf-9cea-325a-885e-524378b0cfd1 | -7.00991 | -45.30195 | 2026-09-28 17:09:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 40b7ff5b-5972-35f8-ad5d-4769e96f6c94 | -10.86384 | -48.50954 | 2026-09-28 17:09:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3b61f525-a553-30c8-b95d-80590daef421 | -11.45524 | -44.91534 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 52434918-7822-36d1-b925-c9963754f56e | -8.23828 | -45.4089 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bb8173d4-7dd8-3abf-9b79-7dd43604a91f | -11.07917 | -46.08419 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 520e1eb8-4dfc-39fd-87fd-e7b3cfee3ad7 | -11.2075 | -61.27225 | 2026-09-28 17:09:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 50839e41-98e8-3401-b05b-4477406387f9 | -6.13207 | -53.06 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ef0d48f1-7ee5-343b-9cd1-d55ea02dc052 | -11.85801 | -50.88098 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README155.md)
