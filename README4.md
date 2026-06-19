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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6d5a1e9-e723-306c-b4a3-2d22bd2f4c4c | -4.35425 | -47.76831 | 2026-06-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 73782af0-4677-3ced-b180-bc435ff65662 | -7.36533 | -49.85587 | 2026-06-19 04:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e582ed5-e810-321d-a804-70da43a19c4b | -3.51033 | -48.03755 | 2026-06-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b84afc7-7375-3c68-b9e0-4d1ff7413117 | -6.52331 | -49.86423 | 2026-06-19 04:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a9951d2-0ea4-309b-b47d-1dff0bd4e844 | -6.72745 | -39.27524 | 2026-06-19 04:25:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a03f9f0e-1a46-3493-9363-a2261760ca26 | -8.31848 | -45.3956 | 2026-06-19 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c23861b-be78-3fd2-9de3-bc50410e26dd | -8.31514 | -45.39507 | 2026-06-19 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db739434-517f-3cec-a4f4-0156d9527916 | -4.35141 | -47.76406 | 2026-06-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a7ce8ab7-1fc4-3cfc-8c6c-904643b442d0 | -6.64992 | -43.91364 | 2026-06-19 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55571060-7f6c-3ddb-a2f1-d9781a4f3902 | -7.80172 | -46.45042 | 2026-06-19 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8a41567-bc8b-37fb-87bb-f2faf806050f | -5.52305 | -37.62373 | 2026-06-19 04:25:00 | NOAA-21 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 916b026f-479f-3b07-b229-ade2ae25702b | -6.7326 | -43.07437 | 2026-06-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 591c598b-a402-39cd-a4b2-111d9bd3503a | -3.85355 | -54.22144 | 2026-06-19 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0eb6178-ef5a-31e7-961a-f692f134adfe | -7.47874 | -38.95674 | 2026-06-19 04:25:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| e8b114a7-c945-3f01-82d2-d2027bed3334 | -6.91014 | -42.84396 | 2026-06-19 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9baecc04-3bd5-3d13-b4ce-f3411527da44 | -3.72879 | -49.27238 | 2026-06-19 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70822e06-5728-3ae5-b5f2-d5262d2dd6af | -5.52347 | -37.62078 | 2026-06-19 04:25:00 | NOAA-21 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 763e43cd-29b6-3273-94e6-9f303a1bf016 | -6.91379 | -42.84449 | 2026-06-19 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54226549-14f0-38f6-84a8-793a1ff2e747 | -5.82835 | -45.06876 | 2026-06-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 496a5bd5-4f6b-3850-9a8f-f23caa1a236e | -6.75226 | -47.12943 | 2026-06-19 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9fd4d15-20be-3543-9d2d-0ae28ad86982 | -6.15152 | -48.50178 | 2026-06-19 04:25:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e5b45c8-a531-3507-a793-d163c5f545d5 | -6.63707 | -44.58031 | 2026-06-19 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c37e32f-3539-3b55-9141-f50d7c9e288f | -4.35543 | -47.76084 | 2026-06-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 200b7d23-e38b-356d-9b67-bd8605f06f9a | -7.80118 | -46.45387 | 2026-06-19 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4e636e8e-2493-3e4f-809f-2b022c4efdac | -4.35199 | -47.76032 | 2026-06-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c8006274-75db-31a3-a677-c69da43ed60d | -7.72371 | -44.1648 | 2026-06-19 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40c4b81c-9f49-35fd-8279-dd04d233b7a4 | -5.52188 | -37.48446 | 2026-06-19 04:25:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d76ab796-e869-379c-839a-442db3107d83 | -5.52146 | -37.48749 | 2026-06-19 04:25:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 15b4fff6-ff73-3caa-947f-d224788cdcba | -6.15091 | -48.5056 | 2026-06-19 04:25:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13585ecc-20e1-31d1-bd4e-f22e6dab8831 | -6.03132 | -43.99303 | 2026-06-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e8cbf1a-7d45-3d28-86db-7aaa526a272e | -4.23623 | -49.17634 | 2026-06-19 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b4f2a6a-50d4-30e3-a9f7-be39717d5c20 | -3.51095 | -48.03367 | 2026-06-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3017b21-dbce-3d55-99cf-93a16470f052 | -8.89472 | -48.0027 | 2026-06-19 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cacabfc1-cd20-38ed-90b4-1d8743212350 | -10.74996 | -50.20241 | 2026-06-19 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50ed84cd-0cc7-34d1-93bc-c9226c8e8f31 | -12.78699 | -44.50571 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27236cd8-8bfe-3af1-81d9-67768e1e0e79 | -16.02454 | -43.41744 | 2026-06-19 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9260cb5e-8c9a-380c-8477-ed00783d3965 | -8.57042 | -45.98948 | 2026-06-19 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4dc3b4d-433b-32cb-a43a-3f9a102483c5 | -12.50027 | -43.77277 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8777cd8c-4b38-31c3-9e1c-609c0318f06e | -9.80571 | -48.9206 | 2026-06-19 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 097c61af-ef05-368a-8863-98b3cac0bf11 | -11.33596 | -47.99865 | 2026-06-19 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81151f01-0f32-3f11-819b-c013c3be1f1a | -16.02386 | -43.42271 | 2026-06-19 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8c570e2e-5ee0-33f1-b954-dd2676fcdf60 | -8.91007 | -46.95723 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18f13a92-ca31-3fa7-b428-cd331ba81122 | -11.44987 | -47.40549 | 2026-06-19 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b3bdc35-1f28-3c7f-8ae9-96eb60671109 | -13.49792 | -56.57547 | 2026-06-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0bd34a9-9f04-3c3c-a3ac-a8b5718355e7 | -12.15195 | -48.45351 | 2026-06-19 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3633444e-9dda-3019-9abf-1d533c1a2307 | -13.32347 | -45.17009 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7a5d5d5-ba79-3222-a2ab-7c0e4d1cece3 | -10.69863 | -49.61213 | 2026-06-19 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1c969f1-a70f-3f18-b761-dc4e30a33c49 | -11.58362 | -47.44123 | 2026-06-19 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b733a9f-7928-35c0-a61a-65ffdcc6dd5a | -10.90955 | -54.13451 | 2026-06-19 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da6bfb6d-3ff4-3313-9613-df5867256f55 | -14.20971 | -54.71206 | 2026-06-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f26c5bfa-5eb9-3175-b5cf-c54c70f951fb | -10.06148 | -48.0924 | 2026-06-19 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b6277ec2-a599-3c00-a2a2-8e6d54c1c05f | -13.49296 | -47.50304 | 2026-06-19 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cf8ee87-4d97-35af-9faf-7cdb5ce1652a | -10.12834 | -48.33506 | 2026-06-19 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5d40b48-76e5-3819-a32b-b80373994e9d | -8.68531 | -48.30693 | 2026-06-19 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b350a333-5709-35e0-a8b9-86e81942f014 | -12.83949 | -44.37165 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 78fd53d4-1725-32c4-8aa6-538befb4032d | -13.48857 | -47.50955 | 2026-06-19 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c358048-9cd8-30f5-b9e8-f76484e495d3 | -12.781 | -44.52183 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4849b665-939c-314c-99ac-0f1a8ae48dbe | -16.02713 | -43.42854 | 2026-06-19 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 20460216-056f-335c-9e61-abb8a645401c | -14.1559 | -41.95636 | 2026-06-19 04:27:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 29c20f3c-4b6f-38cb-af71-c087f126c7f5 | -12.29135 | -44.18407 | 2026-06-19 04:27:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25a08d42-30f4-323a-bac0-80f423cf5845 | -10.15673 | -56.61947 | 2026-06-19 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22617679-09c8-32db-a963-09e11266b183 | -10.05758 | -48.09541 | 2026-06-19 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fb139831-ae5a-3525-ae1d-a224f3dc7222 | -11.55253 | -48.26344 | 2026-06-19 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4ea93dc-ef80-34a7-bdff-888fdbd79d33 | -12.78997 | -44.51041 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eec332f3-e918-3f66-bcb1-e12ca227264c | -11.33484 | -48.0057 | 2026-06-19 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db9f9222-ea9c-3648-aa64-6e211d690dc6 | -10.64966 | -49.20015 | 2026-06-19 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d799f9a-576f-304f-9287-4ea440559635 | -14.76015 | -52.69645 | 2026-06-19 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 450bd152-aa82-3e69-8e67-89f0541a444d | -11.0634 | -52.46321 | 2026-06-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd3d56f6-4502-3bd0-87e5-f9bce9c66732 | -12.1347 | -48.26356 | 2026-06-19 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1e14c3aa-f62e-32a7-a1d0-acea144e37eb | -11.33152 | -48.00517 | 2026-06-19 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e261e141-28d6-3f11-ad3c-157564a032a5 | -10.75284 | -50.20715 | 2026-06-19 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88bf0336-c5d3-35ed-b830-d455ca644c0f | -12.1531 | -48.44637 | 2026-06-19 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 921a791a-b452-3037-8cf7-d3ebe6fdec57 | -13.31706 | -45.16507 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b723804e-1775-3f93-ab65-fa54f249bbc9 | -11.3354 | -48.00217 | 2026-06-19 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d47dabe-5a2f-37c4-a8a4-ad49ccbefa85 | -14.10592 | -47.03015 | 2026-06-19 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3b7af93-0f68-3947-9827-37fc78b93a66 | -10.96477 | -47.95626 | 2026-06-19 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f890f32f-c052-340c-b040-390f987f7ec8 | -9.74894 | -47.87441 | 2026-06-19 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08e3f5a4-aef7-3a08-ba15-9b43310c50df | -10.25545 | -47.34096 | 2026-06-19 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf8b62eb-2019-3ade-9799-ae67d399e600 | -10.99372 | -47.75156 | 2026-06-19 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9f2c984-379a-30fc-bdf7-c09ba0a778e7 | -10.69578 | -49.60766 | 2026-06-19 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3746d952-9792-3b94-bb72-0e11de4c2c8e | -16.0285 | -43.41805 | 2026-06-19 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 39.7 |
| d59d1560-d44d-3847-a734-5e0c549b3adb | -12.78341 | -44.50517 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5f54c58-1137-3ea1-ada1-8f456ec1cf38 | -13.97128 | -47.37764 | 2026-06-19 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b849c1e0-42f7-3353-964c-04399c707fe2 | -11.45371 | -47.40253 | 2026-06-19 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00060855-7357-3793-afe9-e8f74f23383d | -11.35662 | -52.9577 | 2026-06-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0ccbcc7-84f3-39ed-ab1c-7e15753b62b1 | -12.78398 | -44.52652 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38e13128-4586-3cfa-8912-53bc0f078d84 | -10.9871 | -47.7505 | 2026-06-19 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c6d8030-22e4-3438-969d-9a0e6f3fac79 | -13.32814 | -45.18707 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4aa7e039-54f5-3164-9bcc-187a58270581 | -11.48525 | -52.9203 | 2026-06-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6cd89d0c-6581-3352-bea7-f110aebc9025 | -10.16216 | -56.62047 | 2026-06-19 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 841049f9-a830-3a16-ae2c-ded8b4bc5068 | -16.03178 | -43.42388 | 2026-06-19 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 45a7b28d-89e8-3d09-afb6-f6e4ce5e1657 | -10.91084 | -56.8572 | 2026-06-19 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97a49d12-a948-3668-9baf-34dc9f806339 | -11.21156 | -46.57152 | 2026-06-19 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dab88557-68c6-3e6e-9190-02eea2804680 | -10.90541 | -56.85616 | 2026-06-19 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4ba68c0-0c9d-37de-9fe1-faaf8e15d16a | -9.21919 | -47.93051 | 2026-06-19 04:27:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 056ec154-d53e-3987-80ab-14dba877ab3d | -13.93673 | -53.56134 | 2026-06-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 45b51d72-6431-35ad-8413-5687abda570d | -13.93603 | -53.5652 | 2026-06-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e670c67-eee4-3851-9f42-f4f9634b12ff | -10.05092 | -48.09431 | 2026-06-19 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3402737b-ec41-3612-98c6-bdef3fe8b0a1 | -10.69926 | -49.60822 | 2026-06-19 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1390370-fc9e-33e4-8917-aa0bf8b98c9d | -11.33872 | -48.0027 | 2026-06-19 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README5.md)
