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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d88ab0cd-3904-3deb-8a0a-c911f13a5355 | -12.05179 | -47.50671 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bf1f4db-9d77-3817-9821-a73cbbc7b8c7 | -11.72791 | -47.48802 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63c17010-c198-3826-b06d-f14b7bc9b516 | -15.76353 | -48.05235 | 2025-08-09 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59437e36-6bfb-3ff3-acff-f837c68865ee | -14.35003 | -47.09723 | 2025-08-09 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1bdac81-2337-3e4b-9787-a903df1bcefe | -11.7353 | -45.01527 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a6fc475-a0df-36b1-85d9-9416fc1fd691 | -20.22912 | -50.90296 | 2025-08-09 04:17:00 | NOAA-21 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5b828542-878c-3274-9741-056d7800f71d | -21.18048 | -45.87234 | 2025-08-09 04:17:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8b280528-567f-398e-86ac-e5766964a31c | -20.9558 | -43.04969 | 2025-08-09 04:17:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f0a92d56-e37e-3f39-a75f-9b850d54f1e6 | -11.77296 | -47.39439 | 2025-08-09 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dd08b90-b2ce-3885-aea3-820f0352a967 | -10.45029 | -44.34264 | 2025-08-09 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60d01784-83c4-3f4f-ae5e-f579adc9b98a | -9.86448 | -44.69267 | 2025-08-09 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a64fbc85-07f8-3708-9ef4-38a21d9366e5 | -11.74581 | -47.49073 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8b2a51b-d366-304d-89fd-2e4f3b4c952a | -13.06744 | -43.8359 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6cb2b2e9-1ce9-38a0-862d-846b930329f3 | -22.46842 | -47.58239 | 2025-08-09 04:17:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8d522242-3bd0-34df-836c-5bb7e1505e80 | -11.73799 | -47.49359 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b19cc6d8-a2f8-3bdc-a4de-1c31b82e0c9c | -11.75651 | -47.49253 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b1fa351-ae46-3ea8-bc23-35c3f00a153a | -12.5622 | -47.10765 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67095c82-1a12-3d91-b244-445b5e6d54b0 | -12.71494 | -46.37418 | 2025-08-09 04:17:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3943155-7cee-374c-b455-94a475224734 | -14.1942 | -42.09089 | 2025-08-09 04:17:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0a610fa-11b7-3987-8167-719f24fd2811 | -13.48149 | -43.10152 | 2025-08-09 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 093a14d4-ec5d-342d-b21b-aaa067810ecc | -13.55597 | -55.25354 | 2025-08-09 04:17:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 04c2c474-c92f-3b2c-8096-99c27c471554 | -21.38441 | -44.12682 | 2025-08-09 04:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ed2a2e30-50bf-3b9c-a89a-6345bb54fb49 | -23.12838 | -48.77744 | 2025-08-09 04:17:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4fe3bf4-63a8-3757-9be5-d871d397a87e | -10.60496 | -48.36545 | 2025-08-09 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0aee1a2c-216a-3f65-af35-1339519116e9 | -11.25115 | -50.18757 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2fca7f8-a8dd-329f-92ec-b86ed8944dcd | -21.63458 | -49.84204 | 2025-08-09 04:17:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a5dfdc54-5581-3d56-8872-30c4997386db | -17.34744 | -43.18089 | 2025-08-09 04:17:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1445375e-2483-36da-a4c0-53be2792d93d | -11.7409 | -44.95839 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d6bc557-cf6b-3704-b400-5c11c7c86769 | -16.25202 | -48.45214 | 2025-08-09 04:17:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f6926a1c-7076-3083-9b59-ded62a475edb | -12.72351 | -46.36427 | 2025-08-09 04:17:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bffa5e3-19dd-349a-a2bf-db7808949943 | -12.71893 | -46.37106 | 2025-08-09 04:17:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cb5ac65-e46a-3dbd-bd33-2fdb87be179e | -12.65101 | -44.48975 | 2025-08-09 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34b2b963-93ff-315a-8df9-dc5a9aa990f6 | -16.09207 | -49.32305 | 2025-08-09 04:17:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11c88720-24ad-319a-9981-2c83f8945e19 | -13.04961 | -43.84445 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8e88f74c-4162-395d-9d0f-b3f8b9e0c354 | -15.18316 | -48.71387 | 2025-08-09 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24fd6c5d-b4bf-3c69-92bb-17ea56c91011 | -11.79614 | -44.93115 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1b2053a-edd9-34e8-be59-08ac5d584cb1 | -10.74452 | -48.18695 | 2025-08-09 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05f6e829-4bdb-3840-a7df-98dae1539f4b | -12.10304 | -44.73258 | 2025-08-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27bb039c-cc7f-35bb-914b-c2952fca74c8 | -14.5295 | -52.12308 | 2025-08-09 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16ac217a-68a6-3dd4-8019-5d33f1147f87 | -11.74975 | -44.94536 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eeb4e9f-7a82-3372-a526-27ef6981264b | -13.04517 | -43.8511 | 2025-08-09 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ff8cfa7e-de2f-3ae8-a3e4-cd45298925b7 | -13.364 | -43.76478 | 2025-08-09 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41b4d4e4-57a0-3a2e-887d-2e880c1f4fa8 | -14.49771 | -52.10997 | 2025-08-09 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c272e31-4292-339d-a6fb-1d457adbda12 | -11.21727 | -45.36257 | 2025-08-09 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aefc0ac1-44db-35c9-bcd0-6b54a3055879 | -12.6151 | -48.10453 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e7918ce-4d72-35bd-aa4e-6f44e09d3eb8 | -12.56584 | -47.12866 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 83d94c1b-f44b-35af-a83d-eb54af00c430 | -22.46901 | -47.57865 | 2025-08-09 04:17:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9f207b22-c4d1-39c6-bd54-ca543507fa48 | -14.49428 | -52.11168 | 2025-08-09 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 337eccfe-517b-3d3e-9d5c-73be625daccd | -11.08101 | -50.4651 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| c25bf747-9737-3797-a862-85665b182846 | -11.77651 | -47.395 | 2025-08-09 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f888ec47-1f5d-3837-aca2-91b5e0e7085a | -13.33673 | -40.33806 | 2025-08-09 04:17:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d70ed886-47aa-36ad-a605-13c6de994b73 | -12.57168 | -43.79115 | 2025-08-09 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ddb794ed-f110-3057-b702-c4d39f06c8ec | -11.08959 | -50.46666 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3cda5c85-1192-33eb-bc30-5b28d4f5e374 | -16.25627 | -48.44869 | 2025-08-09 04:17:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2356b02b-2db4-36da-a4c6-2817980c0c9a | -11.74357 | -45.02747 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc835e8a-bc64-34aa-9cee-509cbf5f5c5b | -12.72291 | -46.36796 | 2025-08-09 04:17:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b4bdb07-b080-33a1-a558-8fd633e6da90 | -10.46467 | -44.40223 | 2025-08-09 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38205b79-384e-3923-94b1-740d455c3b9b | -11.75294 | -47.49192 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d247a27-3f84-3215-b760-88da6f94fc1f | -11.37891 | -54.35558 | 2025-08-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35e7d8bf-8591-31ef-8043-e99555bb2091 | -11.0853 | -50.46588 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 61341c07-e555-38cd-a605-398eb06045be | -12.71235 | -47.79367 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b196abea-7de0-3d8a-93a0-3db5973f8732 | -11.09171 | -50.50551 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27c9e51a-99f4-31c6-abeb-39624d3e2efd | -13.63277 | -49.01678 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21ff3c39-f41b-3517-8a25-fb599544f523 | -21.3775 | -44.97015 | 2025-08-09 04:17:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cdbc84cc-8f24-3fe6-8590-771e9a397a2f | -12.4094 | -47.78311 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80fccb72-5bfd-3414-af69-35c896eccc76 | -10.63523 | -45.23816 | 2025-08-09 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd0fa243-d5fc-3b98-9f28-78226ba1eaf1 | -12.65046 | -44.49327 | 2025-08-09 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f30fe0c1-c431-39c6-a8e9-f7f1fb59b5f1 | -13.61925 | -49.00504 | 2025-08-09 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 45c0c526-9722-31fa-a3d8-fa4d12859f93 | -12.7195 | -47.79493 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2101242f-7724-3a3c-b0b1-b1267390c63f | -13.38002 | -44.30275 | 2025-08-09 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23f02f00-2226-31f7-9270-194d35002f84 | -14.11493 | -45.41064 | 2025-08-09 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b6da182-8da4-339d-b268-15867822cb8f | -11.24694 | -50.18682 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21e9f51b-d528-3578-8fc5-f0d79ca0e861 | -11.94147 | -44.54777 | 2025-08-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4a5c284a-8e67-35a9-bb4d-07be4dedd420 | -9.01842 | -51.11408 | 2025-08-09 04:17:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8606072-cfdf-3ba3-aa89-62b28cc61339 | -12.57113 | -43.79473 | 2025-08-09 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbe7cd8b-c42d-3f0a-9730-5e2655004d83 | -12.59061 | -47.17357 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c956ac7e-0b16-33bc-b3e6-fbe04d935aaa | -11.77514 | -47.40318 | 2025-08-09 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 688ab2c2-82fe-3a6e-974c-bae14157d851 | -20.87885 | -48.45295 | 2025-08-09 04:17:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e65517a9-ac65-32f5-8f86-392e366ec553 | -11.72115 | -48.34425 | 2025-08-09 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f689d751-1cb0-37c6-a904-4d0a99ac909c | -9.86669 | -44.70024 | 2025-08-09 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5fcd186-c38b-3e08-943c-4efe79e7f9cb | -22.18093 | -47.12066 | 2025-08-09 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f325ef68-776a-3a2c-8315-3a8551f7576b | -21.30649 | -46.51453 | 2025-08-09 04:17:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d63f3492-1404-3b48-a45b-385fdc629b26 | -11.73254 | -45.01121 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 783e8771-5849-3120-b2b4-f029b717f48e | -13.55516 | -55.25747 | 2025-08-09 04:17:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb4497e2-4173-3f2c-9dc7-298644f1e89d | -11.74146 | -44.95488 | 2025-08-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b9f9e17-eb97-3a38-b91b-c5f4fd2e0002 | -14.35408 | -47.09401 | 2025-08-09 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71fa08a3-2ab5-370c-8676-e35ba60f2f70 | -15.2628 | -41.25835 | 2025-08-09 04:17:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ef7dec22-0786-3bdc-bf51-48432146e97e | -12.49429 | -47.51164 | 2025-08-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cea95c87-5709-318c-9c32-c726d9aabfec | -11.74158 | -47.49408 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2510b353-12ce-372f-96bb-6d248bd67fac | -21.37693 | -44.97409 | 2025-08-09 04:17:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f36555f8-6de6-3150-a9e4-f59ac4020372 | -11.73507 | -47.4891 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4909968a-80c2-3698-a0c2-dfe36d3c9794 | -11.32362 | -55.21984 | 2025-08-09 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ebfed50-140c-345e-bd85-ce8a81dfca80 | -22.18152 | -47.11694 | 2025-08-09 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5750a292-c232-36ca-ada2-c4aa90a4ea5d | -12.0325 | -47.5173 | 2025-08-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29d12359-e7cf-332b-a2b5-f283700854a3 | -22.18541 | -47.11383 | 2025-08-09 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf258909-2d37-3d5c-9c99-52f94b6e46a1 | -11.09395 | -50.50562 | 2025-08-09 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba0602ce-a42b-3cb3-9e1c-6219279a7dad | -12.58536 | -47.20521 | 2025-08-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 227ba453-c18d-3275-a8b7-fa977cf81768 | -16.612 | -49.08442 | 2025-08-09 04:17:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c39d072b-b0bc-398c-a12e-88d45ef7eb85 | -11.91901 | -41.63682 | 2025-08-09 04:17:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc147d51-dcee-3bda-bcf9-5bb60eb3491e | -11.32444 | -55.21568 | 2025-08-09 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README15.md)
