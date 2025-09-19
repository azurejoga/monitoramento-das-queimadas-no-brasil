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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16bad128-7a61-31bc-92d1-c252cd18f8b5 | -10.29167 | -46.47041 | 2025-09-19 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 727526e1-ebf4-3d58-88bf-75b826848719 | -10.04188 | -49.20412 | 2025-09-19 03:55:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 374d09d9-0225-36af-bca3-cac7140a4449 | -16.51926 | -43.54609 | 2025-09-19 03:55:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b046deef-1c8d-332e-8c47-100ccb1da645 | -14.43289 | -47.38246 | 2025-09-19 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9de197a-1c11-3697-a4da-6a8e3e4e2bad | -12.09621 | -44.80776 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a796e725-c7fe-3797-b66a-55df2030c9d4 | -12.88287 | -50.53354 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 30.9 |
| b625d2bb-2db0-34d8-971c-f14b0f67580a | -12.6195 | -45.06569 | 2025-09-19 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f25e87f-ee4d-3ed6-9862-0f3ee40d64cd | -12.09774 | -44.84635 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af6da7f0-5e2a-3610-8012-8fa91971a9e3 | -13.15505 | -40.6835 | 2025-09-19 03:55:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f00d7866-430a-3ef3-b0a0-14fbe4a52104 | -12.89358 | -50.54019 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31ff7a6e-445a-3830-a7c2-a7d75dfc450b | -10.302 | -50.22091 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5904aa74-2861-376d-bc6e-c69172dca132 | -10.32765 | -45.2493 | 2025-09-19 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 089d1e9e-3eab-363a-943c-8d76177798fa | -10.87203 | -47.7815 | 2025-09-19 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d61374ba-fff7-3d40-8250-604dcac534c5 | -16.30974 | -43.11307 | 2025-09-19 03:55:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27d806d4-257c-378d-8e1e-84a46d341229 | -17.08751 | -43.33896 | 2025-09-19 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ecb0fd2-f4b1-3e00-8329-80247259dc10 | -12.1018 | -44.84701 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 752e1f87-063f-3809-be3e-ea4688a218a4 | -10.28219 | -50.24351 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 817bb33c-bb55-3d85-9167-8e01aa3db6c7 | -12.93053 | -50.56388 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d0f99401-6137-3d08-99de-0ab1852b74b3 | -11.20416 | -49.63925 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e67e4450-08a4-3dc4-a54a-31cb5e96e304 | -10.87769 | -47.80663 | 2025-09-19 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 377c8a62-8202-3197-a7e5-2b6844f0ff14 | -17.16439 | -44.79457 | 2025-09-19 03:55:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c433556-a44a-3604-a9da-3c23e300d7c3 | -14.69659 | -43.9832 | 2025-09-19 03:55:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 88b2b953-8953-3e50-81ce-96ed162194f9 | -12.91748 | -50.57159 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acc528ad-ad34-3b39-a424-5f83503db222 | -17.34613 | -46.81663 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7e9c7bf-805d-3e95-a52c-688c28cc3f10 | -11.21766 | -49.6299 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e857ac38-760a-3ede-8a31-6ec271110c11 | -11.93112 | -38.33108 | 2025-09-19 03:55:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b90d0299-825b-3a26-b0e5-0b7bad0bc00c | -10.28132 | -50.24794 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ce1728e-86fa-3328-849b-b343f068e490 | -17.95727 | -39.71062 | 2025-09-19 03:55:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 85a72adb-a6ef-303f-b001-5d36bc0e8c8e | -17.21942 | -45.95394 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9e8434bf-568f-3ac6-b964-a016eda8df8c | -17.18162 | -45.90268 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24279158-4b45-38da-90bc-a6f6fd7d3788 | -12.92409 | -50.56864 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c581b0f-6685-342d-856e-3b4f8f68cec3 | -10.92039 | -45.66053 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5982c1bc-18c8-3e73-95ac-5e18124ef2d9 | -17.352 | -46.80847 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb823e8a-060f-363e-8645-01a3fff7ea4a | -10.67307 | -46.4509 | 2025-09-19 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f203b36-9251-3b74-a46b-e7f3e20f951c | -11.16776 | -45.36094 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdaa08c9-c20c-3dc5-950e-b4840fcc867e | -11.20903 | -49.64428 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 065243a9-0433-3d72-b95b-7294be6f6605 | -12.14546 | -44.95409 | 2025-09-19 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bbb9782-247a-364f-8aca-01c3007b6ca9 | -11.50291 | -43.62303 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38aaed44-864d-3fd4-88c3-25c17b114bb2 | -21.85901 | -41.27628 | 2025-09-19 03:57:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ae4b7b2c-519e-39e1-87c2-31ec72ac6b5a | -22.67852 | -47.49715 | 2025-09-19 03:57:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 459bd4dc-2f7c-3288-aaff-f16f7e5913bc | -22.68573 | -47.50283 | 2025-09-19 03:57:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0abc4467-51cd-3c0b-a970-6d9ab2445f6d | -23.38734 | -47.14018 | 2025-09-19 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 62b82028-6aad-38d3-af8b-45f156ae890d | -23.38494 | -47.1496 | 2025-09-19 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f9a0fbae-38f8-3144-ba7e-803df42222a1 | -19.91887 | -44.14979 | 2025-09-19 03:57:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e162faad-18c9-3c78-ae3c-861a80f670d1 | -21.40459 | -44.27794 | 2025-09-19 03:57:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 38d64029-f27c-391d-8e21-b59fca6dde7c | -22.04363 | -45.58741 | 2025-09-19 03:57:00 | NOAA-20 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8b26e878-cc0e-3cb1-b502-f8657af9a4bb | -20.2091 | -44.6102 | 2025-09-19 03:57:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 153d6c5b-b705-39b7-ac97-727bf7c89e0a | -18.64754 | -43.89902 | 2025-09-19 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0d766634-7ff4-3b51-9acc-5436482ccd3a | -20.79577 | -47.23683 | 2025-09-19 03:57:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 108927f4-b95b-30af-a9d2-38d25a823506 | -18.72599 | -40.40791 | 2025-09-19 03:57:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f64260bc-5633-3c6f-ba82-e7e853c8d5f7 | -20.21338 | -44.60675 | 2025-09-19 03:57:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 50debe29-9c50-32d1-8289-e2b95afe7120 | -17.09097 | -55.51514 | 2025-09-19 03:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c968b8f3-5d3e-3b76-9520-7576e03f175f | -19.66438 | -44.90866 | 2025-09-19 03:57:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 939f645c-0f37-3962-9906-5703d84b8239 | -20.81775 | -44.51478 | 2025-09-19 03:57:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f4a5d083-c11c-3700-ad38-b6730938bb7a | -22.67566 | -43.47891 | 2025-09-19 03:57:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ff571bda-976c-305a-9847-2b1a4b18e9a8 | -20.79167 | -47.23624 | 2025-09-19 03:57:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9db1fbe4-49f3-33d4-93cd-c03ec27f31cc | -23.23377 | -47.62413 | 2025-09-19 03:57:00 | NOAA-20 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f47ddefd-90ba-3e0e-a24f-78475f4f3410 | -20.34885 | -48.79078 | 2025-09-19 03:57:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ff084aa-1f4e-3ae6-b466-5a6d89c0db25 | -22.04344 | -45.5892 | 2025-09-19 03:57:00 | NOAA-20 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| be79dd87-2957-31bf-a7f3-b585b15109cf | -22.8139 | -43.27963 | 2025-09-19 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 65367685-492f-3201-b1a9-1b6dd3873d62 | -20.34285 | -48.79158 | 2025-09-19 03:57:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 264245b9-3fbc-3ab8-b82b-b5dea21cdd30 | -23.67627 | -51.72515 | 2025-09-19 03:57:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 0eed0cd3-2474-33ab-9579-2d4b0d6b8ec7 | -20.3438 | -48.78674 | 2025-09-19 03:57:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2754b412-6d4f-3274-98ea-b1e6107c6e1c | -20.20985 | -44.60592 | 2025-09-19 03:57:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2a47e024-875e-3b48-8c11-5598e0f6068c | -22.67777 | -47.501 | 2025-09-19 03:57:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| eb5cf4c4-70c9-3385-8392-2ab667bc2113 | -23.3859 | -47.14444 | 2025-09-19 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ce7543e2-d628-3d9f-a21a-a3ce35caaa32 | -18.11655 | -44.67253 | 2025-09-19 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a312d787-1b4f-37de-bb0c-019c6dfcbd0b | -20.35902 | -42.73766 | 2025-09-19 03:57:00 | NOAA-20 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c3a28574-e1af-3da9-9615-0e67eb2fccd7 | -22.59126 | -46.23317 | 2025-09-19 03:57:00 | NOAA-20 | SENADOR AMARAL | MINAS GERAIS | Brasil | 3165578 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2104a4e3-c8af-3699-9c71-e71ca5614141 | -18.64058 | -43.89735 | 2025-09-19 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d91eb2f-2e63-3207-bf11-5392cd96de32 | -23.36506 | -47.27789 | 2025-09-19 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 847b6215-f39d-3fc4-b752-2ec93c2e58a2 | -23.38637 | -47.14523 | 2025-09-19 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ef97e32c-390e-3d1e-8d45-62c943d3ecf6 | -22.85705 | -51.78906 | 2025-09-19 03:57:00 | NOAA-20 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7d01e852-5dde-3a61-ae48-e9d86019cc96 | -20.51833 | -42.39312 | 2025-09-19 03:57:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 90608213-9017-31a0-907a-88bb221f9358 | -21.28161 | -54.81249 | 2025-09-19 03:57:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e4a64f7-028e-3f72-9ea3-af875bc39f39 | -19.96521 | -42.11201 | 2025-09-19 03:57:00 | NOAA-20 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4e4d9483-b028-30f9-8e71-c0ef33a0a441 | -20.1574 | -41.48151 | 2025-09-19 03:57:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 283abc85-208c-3584-bca0-22b6e03701dc | -18.70044 | -43.73953 | 2025-09-19 03:57:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9c0adbf-3e1d-3123-88cb-f101f389dd4a | -21.35421 | -45.78712 | 2025-09-19 03:57:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0348c762-efb9-354e-9430-eb8bb67c7ec2 | -22.93641 | -46.95517 | 2025-09-19 03:57:00 | NOAA-20 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8e32f17d-f8a1-3d28-aa38-f1a2e19c9e4c | -22.25647 | -56.77955 | 2025-09-19 03:57:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2fa3cfd-ac91-397b-8ae0-a4ceb3a46f46 | -22.35239 | -46.74594 | 2025-09-19 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0676cf83-dfed-3353-b536-315de83fc7f6 | -20.09639 | -48.28441 | 2025-09-19 03:57:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9710eaa7-637e-33fe-a0d4-de3376b7ca59 | -22.74895 | -51.40257 | 2025-09-19 03:57:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7990d101-66f8-3477-b40a-5979e0d3ec5a | -17.50019 | -46.73996 | 2025-09-19 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5afdb71-9b15-3a1f-be24-3763ff3d2b58 | -21.94974 | -42.19456 | 2025-09-19 03:57:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ebcc61e5-5508-33f7-9a62-bcff1d7402ed | -17.0927 | -55.50777 | 2025-09-19 03:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8d9a91ac-0cd6-3fdf-887d-e3c9ade14b85 | -20.24243 | -42.26762 | 2025-09-19 03:57:00 | NOAA-20 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9635e963-0460-37f2-9044-dfc736ded313 | -20.34828 | -48.78781 | 2025-09-19 03:57:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6060e3f5-de1f-3137-a99c-f5e78ce5702c | -23.41069 | -50.68999 | 2025-09-19 03:57:00 | NOAA-20 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| eac19e4e-5ff7-3a2d-a47c-800358bac307 | -19.96188 | -42.11146 | 2025-09-19 03:57:00 | NOAA-20 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aaa477ae-28b3-3b26-b471-9eadf3fa2d7c | -19.63346 | -43.73435 | 2025-09-19 03:57:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f81588a-93df-3ccc-9496-c4fdb4c16c3b | -21.3524 | -45.78454 | 2025-09-19 03:57:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ac1c68ac-894d-3c0f-b31c-27003da111d6 | -22.03899 | -45.59308 | 2025-09-19 03:57:00 | NOAA-20 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 078abe5e-750b-34ee-b7e5-a8852e4a675f | -22.03916 | -45.59129 | 2025-09-19 03:57:00 | NOAA-20 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 7d63863f-aea6-323d-b4d0-906c43c2f78b | -16.6868 | -54.96836 | 2025-09-19 03:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd30383d-a95c-3d4e-9c6e-daba85eb39ca | -20.54634 | -44.02393 | 2025-09-19 03:57:00 | NOAA-20 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8e4b311a-5969-3e63-84f0-d485bdf34032 | -21.15697 | -47.12656 | 2025-09-19 03:57:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37d20a42-131c-33de-a133-5a2303b271bd | -20.78493 | -46.1124 | 2025-09-19 03:57:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 211a4a21-e2a8-32d4-b9a7-039c71e57da5 | -22.9315 | -46.95998 | 2025-09-19 03:57:00 | NOAA-20 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README19.md)
