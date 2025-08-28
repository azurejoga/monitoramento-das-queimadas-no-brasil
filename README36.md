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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b1de814-1c33-3d5f-9fd6-999d2c21f458 | -11.65069 | -46.39236 | 2025-08-28 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d991d9b-37b6-398c-8921-5308be444cbf | -14.13939 | -45.40617 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 249f2ddd-be77-359f-8943-54b3d51b137a | -12.72453 | -48.1852 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 637abb68-a888-36af-acb4-12f122a738db | -13.53928 | -46.88914 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9e6a834-abd3-3732-b52a-e1fae3195ede | -13.53189 | -46.88786 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96741d63-a3bf-3c38-a135-ebb5fd7f6b63 | -13.18249 | -45.29348 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a6d4aed-d7b6-3b3f-b2ac-ac3365a1db20 | -12.9563 | -44.57888 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8cf61b6e-514e-3966-9414-d1857cf46762 | -10.93368 | -47.43206 | 2025-08-28 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de159020-5006-3810-b62c-ba86cc1f97dd | -13.47503 | -46.85043 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddec3bcd-df24-33bb-87e7-3e4e5e73f44d | -8.29842 | -45.16382 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0b14450-78ad-3465-9719-a6f629966909 | -8.29759 | -45.14651 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 4bd52bf4-c489-3900-8b12-e307253c66bd | -13.38366 | -46.88262 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8df69554-5381-38a0-bb5b-ba7d68b23e79 | -11.84405 | -46.80145 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e923655d-e69f-35a2-bbf5-69260d199f19 | -11.81002 | -46.8191 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 103eb06d-79ff-375a-b185-9b162306aefa | -11.33078 | -43.5178 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7706646-68f2-393d-b7b3-45fdef34d638 | -11.57563 | -44.65313 | 2025-08-28 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10c9a472-4215-3ffa-a2af-ae70ca57200c | -12.80865 | -48.15921 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c9460ec-743b-3bec-95ca-49a6845c1b5f | -8.47692 | -43.64421 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b081b256-f8a7-3721-8972-23470da320d8 | -11.06491 | -44.59981 | 2025-08-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a71f7a62-1928-3e70-ae19-ec4280580a3d | -13.61612 | -48.23438 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4257d6c-28dc-38a6-a55f-16e0650dd360 | -12.71848 | -48.17222 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 09213be4-9a87-357d-b36e-9f8e7863736f | -14.13597 | -45.40557 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ddf6b31-0a61-3a74-a09a-46e369991dbd | -13.55009 | -46.91464 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b520c03f-accc-3ce1-8395-9a721950117b | -10.32311 | -46.77033 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4a0cb3fc-8c86-3cb5-bb99-36445eb428d6 | -8.28179 | -45.1525 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c1ededc-92a9-35eb-bd2d-300e22d4a417 | -11.22906 | -55.0697 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aee22a5b-8683-3a67-aef7-848e1b86ecc6 | -12.18206 | -47.18295 | 2025-08-28 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ea0f06e9-9eb2-38b7-9a0b-6401c2f9876b | -12.78675 | -48.18921 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 535159aa-7728-3b50-8898-ddc3372b788d | -11.5771 | -46.38564 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fc2ece8-82e5-3368-bed7-c62dc51a543d | -12.41558 | -46.48402 | 2025-08-28 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e112681-7fd3-3152-a562-53bd07704a5b | -13.598 | -48.22085 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0db2451f-c111-3745-a6d2-5eb1631e1ecd | -8.44213 | -43.68747 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91ff9bf6-dcde-3b36-a42c-5b70dcb74506 | -8.28332 | -45.16553 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 833e991c-95d3-3f69-96af-f64b552f25a9 | -13.51681 | -46.93074 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd790a23-0ecd-3a72-919d-ead0d910e460 | -13.07951 | -46.3336 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f48a68f-83a8-3ea7-b0a9-01fa736fdfe9 | -9.66216 | -48.31195 | 2025-08-28 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f6997c8-4a6c-3f61-9dde-f4609239d49a | -11.22249 | -55.06714 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f5ae431d-286d-3239-b9a5-9ad0f8e58657 | -8.90245 | -47.33167 | 2025-08-28 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2438eb50-ce9e-3092-9469-41fc19e59802 | -9.18817 | -46.74329 | 2025-08-28 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4b80272-10f1-32b7-99fa-1494f2334067 | -12.03163 | -47.20602 | 2025-08-28 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 249bddff-1548-3f84-92cb-3fa0142af83b | -8.02191 | -44.79743 | 2025-08-28 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 200bf748-6060-321b-8dd1-bac238de70f8 | -11.32957 | -43.54675 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b51471b-e454-331b-a3d7-86556b0848ec | -13.43213 | -46.96684 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3b4d9ac9-6c22-368e-bdb5-15615b56874a | -11.93062 | -46.70578 | 2025-08-28 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a487618c-fd9b-3b82-b1dc-42235bfc91ed | -12.93559 | -46.33743 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fdfef1f4-49b7-3380-bc46-974d7ea9eca0 | -13.6684 | -46.90315 | 2025-08-28 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2213998e-3b93-31b1-bd86-54f8cba69c5c | -13.37752 | -51.77057 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 268196d2-0e35-3dcf-be8a-5387bce29c26 | -10.5317 | -46.68441 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 38c099b8-1ce0-3c3e-b98e-bfb5757f4ef0 | -10.49464 | -51.58758 | 2025-08-28 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f74ece80-5e82-37a0-804b-146730df391c | -12.50748 | -47.23349 | 2025-08-28 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ef9e303-5998-31ff-bcdb-d16c3ee8bb27 | -11.34127 | -43.53774 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 22209031-ea7d-3d5d-98aa-1202f9788120 | -12.96365 | -44.57637 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91877d19-d41f-39f2-92f2-fdf0764b7ae3 | -13.17344 | -45.28399 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9cf00cad-e72a-3b61-aef4-e0064e7755d3 | -13.54588 | -46.89492 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| aff42d9b-1ddf-3ce2-9425-c8a4e8b23e98 | -6.4904 | -53.3991 | 2025-08-28 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f539ae4a-d591-3f00-9c96-5e7fa61a4b6d | -9.20605 | -46.75942 | 2025-08-28 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dad57b64-06a9-3152-a7b9-05ca861e272b | -13.52784 | -46.93309 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56c0a51a-8a37-30e3-816c-dacb3ff1caa0 | -14.13876 | -45.41 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1de782bd-1a2a-3be9-bc05-0ff80a82c80f | -8.30271 | -45.1603 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aef42a0-4c9c-3b28-a07f-8c5ff7a68850 | -8.44773 | -43.6959 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66cbe79f-4d7a-393f-a11d-9ce5a5ac5d7c | -11.32681 | -43.54265 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18a05aa3-a295-3581-af8c-ce7bb7993874 | -13.60021 | -48.22129 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e383dd3-dfb9-3a03-9a08-3c0394f53675 | -12.72519 | -48.18142 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9120bbce-e1d1-376c-adda-020d51b5d703 | -7.73307 | -50.28117 | 2025-08-28 04:08:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 098100b6-8cee-3a08-9ca4-fe83114a7e72 | -7.78661 | -43.18106 | 2025-08-28 04:08:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5f57ccbe-1fb5-3897-96d8-9378ccf89a44 | -11.34278 | -43.54513 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| be478aec-38ed-3a03-9b41-c92aef3fd609 | -11.79978 | -46.78874 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2421b60c-bc68-3ffd-8389-735f16d4f449 | -8.45231 | -43.6891 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b328a89-90a4-3c52-b23d-607525501bc5 | -7.39924 | -49.19431 | 2025-08-28 04:08:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d771052f-4a0a-3195-95c7-0ed57983f5b6 | -13.37993 | -46.88216 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6168b45a-f755-38e7-ac7f-03bbcfbccad9 | -12.67625 | -48.17601 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e1d16f0-600d-312b-b61e-c16ae10f9b82 | -13.51868 | -46.87638 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ed16fa3a-1bbf-34f3-9b7d-db1932f5d688 | -11.22359 | -55.06161 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4e95300c-ef46-305e-9476-63138c5e7b64 | -9.66564 | -48.31736 | 2025-08-28 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebbf8188-df33-37e5-990f-e2259151907b | -13.55169 | -46.90537 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d5aef4b-1abc-31a0-a0c0-74e84317040b | -9.45006 | -51.96086 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 842edffd-1bff-37a6-8552-e2c63317f04f | -13.3911 | -46.8836 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39d62b4b-a177-3f14-8397-b611081fcbe3 | -13.17816 | -45.27688 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4bb99a5-648e-303b-bfed-156caac04c5a | -9.67567 | -47.0699 | 2025-08-28 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81fe2535-1d01-39fc-ad5d-b41a2f35884b | -12.43211 | -45.96507 | 2025-08-28 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 46082f93-3046-3b91-b944-c482e6f0a795 | -8.27611 | -45.16431 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| ebdfdb75-0588-3b20-845d-4a617871797d | -12.50664 | -47.2383 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbf3c691-2392-3513-8dcd-f1b1f69ba0d1 | -13.53226 | -46.92955 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc2427a1-30fa-3cf3-b88c-0f07523be207 | -7.7446 | -50.27487 | 2025-08-28 04:08:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2479110-d464-3ba1-bfc7-4add4136c1c1 | -13.48059 | -46.9967 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea94d2db-1851-3514-842b-7c16eed78f9f | -13.43738 | -46.84849 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7e91d31-ba46-365e-a1fe-7d7e7ea87741 | -13.52417 | -46.93222 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 219202f6-912c-3164-9b7a-6e02d5699345 | -12.67688 | -48.17246 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0757b423-6a2e-32d8-bc5d-70ed7219f6eb | -13.55089 | -46.91001 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a771462-83fe-3dde-be74-d7a708e4dd0b | -11.24932 | -44.97033 | 2025-08-28 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dd77327-9954-36cb-ab8e-826e373e73b9 | -10.29197 | -46.74493 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bdc04af-e9d5-3d92-92e6-f620be1a3e6a | -12.80527 | -48.15485 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb6793f1-99e9-321b-bd5a-6ab06e5a5069 | -7.44577 | -46.12931 | 2025-08-28 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44edc555-5536-3fad-9b66-893846ddd967 | -13.66474 | -46.88038 | 2025-08-28 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e0964b6-a765-386f-9e98-5cee13a4b267 | -11.23656 | -55.06572 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ea2353c-72c8-3852-a36e-bbe5fca1b9ff | -11.23125 | -55.05901 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f40cfe2b-9845-3714-bcf8-4b7544952b86 | -14.1319 | -45.40879 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cdd23b9-6cfa-3485-9adb-d68739eca7f2 | -13.54665 | -46.89052 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 65ac1e81-13c5-31b6-9b13-a0dd2f971493 | -13.47872 | -46.85107 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b3dfb24-b664-30eb-a734-481d01c0640c | -8.86019 | -47.16171 | 2025-08-28 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README37.md)
