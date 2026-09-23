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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8a5acb1-994e-35de-87bf-210eb7cb16b8 | -13.54874 | -47.65882 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5247d746-356d-3a3c-96c4-bc1e28271795 | -6.67686 | -50.9478 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b46d3ef-065c-322c-9a75-3fa5411c3581 | -9.01372 | -49.81824 | 2026-09-23 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1d7cd8b-8832-3760-950d-7392690c7ccd | -12.67203 | -45.03751 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47779846-caa1-3fe1-94da-6951e6ae515f | -13.3916 | -48.03497 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5584a3bf-cabf-3fc3-81f7-2afe0e5b296f | -6.70378 | -58.92729 | 2026-09-23 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ddc7e14-4fb9-3dc8-b251-0d3f26284301 | -9.59646 | -48.45382 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2dbbce50-55c1-35a8-be6b-6dcb144639c8 | -13.45656 | -46.26385 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de9588da-2424-3ee7-a49d-a3374705d709 | -6.68186 | -55.05207 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eaa70d75-3148-3dba-bfc2-3a4a50af2ae9 | -10.2988 | -50.52086 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76fe18bf-967c-3b65-819d-024963c22419 | -8.31224 | -54.7731 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5619de5b-206e-36d6-a204-3eab4f7da31b | -8.0901 | -44.34517 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71fd208e-8701-32b0-b3e5-7e16d99cec92 | -12.78735 | -50.86951 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8bcd6f8d-a204-3b7e-b7fa-ee0e2137aedd | -12.41794 | -46.96554 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| c2213014-3795-3b02-b9af-ad4c4255b7ea | -9.60295 | -43.9424 | 2026-09-23 04:27:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c3a3e7d5-ddf1-395c-977a-506d91bb5ea8 | -14.60397 | -45.62624 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 290.3 |
| 9a03de8d-2faa-3d3e-ad95-a720dd941ebd | -14.64453 | -45.59799 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a00acdf-158d-3652-9045-0551d85b97de | -13.30478 | -47.89396 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5118ad95-a16a-31d3-a5c0-8f4d70f0bae2 | -12.84426 | -50.87467 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f22d3d3-9366-3a80-9688-c56c3ec4124f | -11.75266 | -50.05153 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f476e7e3-6010-3849-9f01-6b8b151d5b5e | -6.46422 | -59.99387 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 00a99b96-29c4-3d65-b155-f626bd6f2cc9 | -6.09576 | -57.68055 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16dd66d5-65cf-3487-8b47-92467fd5d283 | -12.13054 | -47.39803 | 2026-09-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87800396-c15b-3b9b-9713-924fb3cae886 | -6.61952 | -59.96463 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70be37f4-1359-33b3-8f87-c0f81f6fca7f | -10.25797 | -49.98285 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3de014d7-df72-3eec-854f-948854bed618 | -12.7838 | -50.86889 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 086d1227-1234-34d2-ac85-78d8b16f9db9 | -14.63227 | -45.63378 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaa84051-c0b8-3e64-92f1-2debc10342f8 | -9.72443 | -48.33449 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03c6cebc-e0e1-3936-8a32-0d71f5014fe8 | -8.48733 | -57.60785 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9850504-b11d-394d-8e6a-6b5d81ce6548 | -6.18348 | -52.80024 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbb03c04-021b-36a4-8932-720150b89158 | -7.33448 | -55.59637 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7571c6f9-a926-3a1d-b0ec-7ebc6a843da0 | -8.08953 | -44.34907 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1349101c-a7ae-39c4-82ab-8cbef869ec56 | -14.64047 | -45.62664 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 364b27ec-99ac-3325-8dfa-3359c8026587 | -13.07693 | -47.41244 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5409c20b-e0fe-3bda-94e3-4c6418d43950 | -12.06825 | -50.05515 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f47f62ec-3ab5-3ad4-bd14-bdb9c051dc31 | -6.6708 | -58.55727 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ff9f94e-fe1f-31fe-929e-3a7f43dfb2d0 | -11.53467 | -45.35268 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 0013688e-f0c3-3235-bcd1-880048b94974 | -6.3125 | -57.74461 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b04b53bb-ff55-3485-a6a4-f5a440b2d965 | -9.93867 | -48.465 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11c453d9-9b88-3c8b-8a2c-5a04ad2a3b0b | -10.34305 | -48.25298 | 2026-09-23 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6992f85b-e159-373c-bf0b-5677b9d141d8 | -8.37085 | -45.60561 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6af5776f-06e1-341e-a0a0-ff196b0071f3 | -8.83434 | -50.49366 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7a5e14cc-6f5e-3ecf-a56c-658dec475d61 | -5.93112 | -59.91399 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ef701dc8-51e9-355b-ad39-e68858e81d1a | -10.25712 | -49.98303 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0167479a-e6ec-390a-aedc-aa06618dc5f9 | -13.29542 | -47.88884 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d05660c-4587-34fe-81c3-07d4c294386f | -6.66354 | -55.06726 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64c964db-b768-34e8-9839-504942652ef9 | -11.95504 | -50.08074 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db179b71-b932-38d9-bd70-8f6e3a528836 | -14.70621 | -45.59504 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 514590e6-7505-3df9-87f4-719fe46df5c8 | -8.46074 | -48.70275 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc910b02-52b0-34de-9124-caa076c64233 | -6.23628 | -51.00682 | 2026-09-23 04:27:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cb63939-2ce2-36a2-a30e-65baa03228f8 | -6.66704 | -55.06588 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3cea63a9-17e3-3a8a-aa60-67f7982c03a1 | -14.59927 | -45.63388 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| aa45bb2e-c343-37ac-879f-7d1d3924adff | -8.28121 | -54.77875 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 588b55dc-da7a-3515-9fdf-ffda67509503 | -11.28102 | -44.04625 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5b8e26b-3b7b-3a71-bed3-8d382d3070b9 | -10.44979 | -45.09187 | 2026-09-23 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3632642-7e3f-345e-8dab-f31e47430786 | -8.83112 | -45.92804 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01ac4440-36cf-39fb-9d11-4cb91d2b7eb9 | -12.05468 | -50.363 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7702f40-1335-326c-a5c8-644cab5c2331 | -9.71499 | -48.32923 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8c192b9-4056-3244-85d6-ebce83a40c1b | -11.1823 | -48.04583 | 2026-09-23 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25f11202-8369-340a-be71-e0acb3c94aa5 | -14.61449 | -45.65278 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5bbdc5d-a171-3db8-af20-c0550bfb1809 | -6.53903 | -55.47792 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14889489-db11-3be0-88eb-1178374b27c7 | -14.62795 | -45.65897 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e7ba8f38-41aa-3269-bd40-6d0772a90a7d | -8.9017 | -45.91351 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbc7cf64-cbaf-3945-814c-43655a30ea33 | -13.93657 | -47.83361 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2f40f7c-aa9d-30ea-9160-89140534cb87 | -12.80717 | -50.86022 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a74c58b7-8512-39a6-90be-c9383f3826dd | -12.68247 | -47.0146 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d89ff52-7230-3715-ad64-6befd923efd5 | -14.59516 | -45.6374 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe4c1683-3fa4-3a42-934d-925852a95c06 | -8.73201 | -47.59618 | 2026-09-23 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de0121a4-a560-3c2a-aace-f6c6f8d60d85 | -8.35752 | -45.62552 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c05108d6-4a1a-32d1-ad53-c0d477a445e6 | -8.80808 | -44.28259 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d4afac66-b67c-3790-9bb6-09fa89732891 | -14.61626 | -45.64062 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 8c818fd5-5737-32ef-8427-0315da5ef8b3 | -14.63873 | -45.63888 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53e4c38f-8385-34a2-9ce5-ebe0d264f8d8 | -6.6697 | -55.0619 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 95c62aae-c310-352a-83db-7458a7cf2fd6 | -6.46218 | -59.96655 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 762e67e6-9a16-3d1c-9f90-1239a6d18bc8 | -10.44864 | -45.09956 | 2026-09-23 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e983ae6-2646-3f34-9889-9ea5c700073e | -7.32885 | -55.59779 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77e795b7-7a14-3e1f-af0b-0fa8d2b96c1a | -13.85809 | -48.57484 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf539456-00e7-310c-9567-f90931d984aa | -14.59575 | -45.63334 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9edcd96-decb-3b60-8f7c-533fed496a8d | -6.0448 | -53.26983 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4897c5a3-8a2c-32a5-a5f8-93f93671ccdb | -13.70831 | -48.79074 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fd61312-2938-34d7-8a2f-ab5fec31bcd0 | -14.61805 | -45.62836 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 588719e1-f9c1-31f3-8c1d-587b52747085 | -11.68766 | -43.45685 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90aa8326-5aec-3fb4-974a-24320c6ac065 | -13.90259 | -42.76108 | 2026-09-23 04:27:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5910da6f-29d4-3aaa-bf68-5f2ed6bffb50 | -11.03513 | -57.23333 | 2026-09-23 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 321a0616-73e1-3723-88de-c8f4a12bec09 | -12.04484 | -50.35725 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0018e268-175a-3c17-965f-fccd750fa5ab | -11.66854 | -43.4861 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b87c142-7e37-3cb4-99f7-9e2d111abe1a | -6.75126 | -50.68506 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e168cdd1-1b3c-3029-8ff7-214b3a828c62 | -12.05118 | -50.36242 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c417476-537b-3f67-a59d-bec633717c12 | -6.63937 | -59.93464 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| fcc03d54-d14e-31c2-9c12-a65d66bb05dc | -6.67672 | -58.57124 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9eece5dd-0a2f-3ab7-b60d-e175ac82794a | -11.29773 | -51.37354 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8fd92de8-6f11-3078-9c45-83094aa62461 | -8.80631 | -44.27022 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f546c27e-22d9-3179-baef-241ab122d44f | -8.3597 | -45.61121 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e31eb37e-c037-3587-b8e2-fb380b3c50c8 | -6.61299 | -59.9229 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 54bd8ca8-6c7e-34f2-b2ef-fe7702a584d4 | -12.87258 | -50.8584 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca3aad0d-29c1-3861-8c06-d9bd94776901 | -9.84597 | -46.38352 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aae0a7a0-3109-34eb-b10c-910115a32efe | -6.74069 | -55.30944 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a55cbb3a-a604-3090-a5bf-6594d21c9e1b | -14.60982 | -45.63549 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 329a7191-eb3e-33dc-bfb3-d615206a41a6 | -7.39956 | -55.21729 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9818aa2-93ef-393c-abc3-b0e9546772ae | -10.71437 | -48.71941 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README59.md)
