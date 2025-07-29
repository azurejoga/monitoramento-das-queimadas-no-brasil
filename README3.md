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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b83acf2-549a-36b2-b358-2c85738c1612 | -14.8227 | -49.250099 | 2025-07-29 00:22:00 | METOP-B | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cede1617-eafb-3e1b-b937-0f777930d156 | -14.5027 | -46.533699 | 2025-07-29 00:22:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c7fd0fb8-a5df-3229-ab2c-15187d9bbb90 | -8.9479 | -46.743599 | 2025-07-29 00:22:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6401f4ed-a3ac-3ac1-a291-34c3fcdbe997 | -7.7329 | -51.107101 | 2025-07-29 00:22:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a69f88d-b642-3fe6-a0b5-14f04c0a8ce5 | -6.8333 | -46.386101 | 2025-07-29 00:22:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 642aac09-9f0c-3f66-b009-c3fb991cdcea | -15.1194 | -45.323601 | 2025-07-29 00:22:00 | METOP-B | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7f202e0b-d5cb-377a-9211-7515e4dc4a23 | -4.7987 | -48.555901 | 2025-07-29 00:22:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d8adffc-9390-3fe1-a227-c656b53fb567 | -11.7524 | -48.176201 | 2025-07-29 00:22:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37124f03-7e91-3135-b884-8d9a5c8a948d | -7.4597 | -49.381599 | 2025-07-29 00:22:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 296d60a5-1933-39e1-baed-466f4455a1bc | -10.5285 | -50.257702 | 2025-07-29 00:22:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7aef4c9-a6fb-3e3d-9fa4-35b432a6508a | -9.2189 | -48.594799 | 2025-07-29 00:22:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71e24875-5a0b-32ce-96a0-e9418337de81 | -11.4249 | -45.121498 | 2025-07-29 00:22:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 165a9bc4-f339-3444-920b-9dfe110bffd5 | -2.896 | -48.297901 | 2025-07-29 00:22:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26eadfef-42b6-300b-88c7-5b7448a48f28 | -11.2676 | -44.636101 | 2025-07-29 00:22:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e3ae734f-7cc7-36db-b3d9-5ab41dbbeb45 | -11.3498 | -51.240898 | 2025-07-29 00:22:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 671d0505-673a-3b37-bc67-f4559a10de4c | -9.9989 | -48.1264 | 2025-07-29 00:22:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de784191-586d-3612-82ee-75b8e858fe47 | -3.2724 | -49.137199 | 2025-07-29 00:22:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe23c3a0-6c97-31c1-bd3b-710a60f5bc61 | -7.9242 | -44.073002 | 2025-07-29 00:22:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e03904b9-3853-357b-9fe7-274fd018a329 | -4.1253 | -49.263699 | 2025-07-29 00:22:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459d0873-00ce-34eb-9d1a-4d8915ef17fc | -2.9058 | -48.2957 | 2025-07-29 00:22:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f1cec10-0be1-3ca5-9e7b-1a0b9775b652 | -7.238 | -43.063999 | 2025-07-29 00:22:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ea614bf7-8357-357a-928c-949f8ee9264a | -13.0003 | -44.8843 | 2025-07-29 00:22:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6fa0969d-cc14-35fd-a4e1-95d5916e4963 | -5.6408 | -44.338799 | 2025-07-29 00:22:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a91a4df-2d4a-33af-8456-8b3bb993ea42 | -7.8681 | -47.8717 | 2025-07-29 00:22:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3105700d-50ed-3f4f-baaf-851ec7662747 | -10.7333 | -51.571499 | 2025-07-29 00:22:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf2c0bb1-2bad-3cc1-8fcc-63d11b4d1f7f | -11.9992 | -46.9547 | 2025-07-29 00:22:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ce52294-c7be-396c-8b6e-5072c87756c5 | -15.488 | -50.049702 | 2025-07-29 00:22:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 462288e7-3519-3960-85be-4f34f989ecd8 | -9.2252 | -43.148102 | 2025-07-29 00:22:00 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 85a8d464-fc73-3d53-bf08-7cfd5c3a24ea | -7.9369 | -44.083 | 2025-07-29 00:22:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8dd533c7-2041-3443-b38c-5ea4b14dba7a | -4.0985 | -48.196499 | 2025-07-29 00:22:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acc03b5b-828e-3dd4-a5b1-77a5bc7ad3fd | -13.01 | -44.881901 | 2025-07-29 00:22:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a451c4b-2c0a-3464-a48c-0e133f77ed18 | -7.7344 | -51.114101 | 2025-07-29 00:22:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f1d7847-06dc-3ae9-94b1-850c16286bb8 | -8.946 | -46.735298 | 2025-07-29 00:22:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 020689e5-88ad-3d60-8687-2b4edfd76c99 | -8.3708 | -51.061298 | 2025-07-29 00:22:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd706220-ba06-3451-bc46-578d6af1fc09 | -7.8664 | -47.864101 | 2025-07-29 00:22:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb045e6d-ee5d-3664-b97b-ed0b8f89fa25 | -7.8128 | -50.218399 | 2025-07-29 00:22:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 734dc0cf-81ea-3ea2-9419-2a4feb16cd11 | -11.5283 | -54.6698 | 2025-07-29 00:22:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 247f43b5-13c2-3cab-8e11-1a908d8ef458 | -9.9972 | -48.119099 | 2025-07-29 00:22:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3c6f517-70a1-37c0-95dc-bd2d28f48e51 | -6.4586 | -53.3508 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea18a0e2-0875-3571-a203-77ddc9d79654 | -7.8068 | -44.961399 | 2025-07-29 00:22:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e48e91bf-c6dd-3f97-8c70-c148dd8be080 | -13.4861 | -45.582802 | 2025-07-29 00:22:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4798e24-ecf1-3612-9a7e-b3bc50a4da7a | -18.456301 | -54.641602 | 2025-07-29 00:22:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2610a190-e5ba-3e7e-b7e2-172d552e0764 | -7.8036 | -46.568199 | 2025-07-29 00:22:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb1e1eef-f2cc-3625-8fad-04e9dd2047a3 | -2.9021 | -48.2794 | 2025-07-29 00:22:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9df5b78e-736e-392e-b04f-5bb71d91b331 | -6.4061 | -53.345501 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46c1ec97-5f07-3547-b515-5a23731fd72f | -7.5217 | -49.7477 | 2025-07-29 00:22:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24471d32-4bfe-31e9-be73-74df73259c78 | -5.401 | -45.284302 | 2025-07-29 00:22:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aba5e8b2-7741-3e8d-aae2-173a0687f7a4 | -18.443899 | -54.629601 | 2025-07-29 00:22:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4742acd7-86d7-37d9-9176-b016b0e9a997 | -2.9832 | -48.59 | 2025-07-29 00:22:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68f1fecb-0855-3b64-aa13-b9bbff2459ec | -6.3813 | -53.325901 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93ec2071-c6e0-3c0e-8381-1b1e01fd3c0f | -6.4257 | -53.341301 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9915083-acee-3854-bcfe-43e87c36b50b | -14.3529 | -47.095798 | 2025-07-29 00:22:00 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8a1a834f-6cc2-3c7f-8ef5-ad0572dc200e | -8.4994 | -43.2985 | 2025-07-29 00:22:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2d2824aa-2764-32cd-9579-243e807ad0f6 | -8.5124 | -43.3097 | 2025-07-29 00:22:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3b065b25-6e4d-39b1-be31-3a8d8c50ab5e | -11.7426 | -48.178501 | 2025-07-29 00:22:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 752b5696-eafb-35c3-9b08-cfda5004fc84 | -12.998 | -44.874901 | 2025-07-29 00:22:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e8032a5-e52f-3fb2-915a-6ca730f7e436 | -13.4881 | -45.5914 | 2025-07-29 00:22:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2de7a3c-1b10-399b-9410-4e014ad02135 | -2.8825 | -48.283798 | 2025-07-29 00:22:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57038352-185e-3962-a89c-8dfd4c9128f8 | -6.9424 | -44.230301 | 2025-07-29 00:22:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27ccb11d-cac2-3673-8b16-ab64d00b74e6 | -13.0077 | -44.872501 | 2025-07-29 00:22:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd9aa9b7-c62c-3def-8b10-a45e92f1509d | -9.7282 | -48.296001 | 2025-07-29 00:22:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cadbb3b-f4b4-32d3-83e4-73d5ba3f2531 | -7.8479 | -46.714199 | 2025-07-29 00:22:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f182d40-b920-3e6e-9384-8edaabe07b92 | -7.8566 | -47.866299 | 2025-07-29 00:22:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34d25acf-163b-35c7-9f48-6a35523ccc12 | -9.3604 | -45.730598 | 2025-07-29 00:22:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a19445b1-d85e-3991-b6b4-3464278e1148 | -18.458799 | -54.655602 | 2025-07-29 00:22:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fc9ead2e-366b-3eca-90f2-59dacaf1e461 | -6.4079 | -53.3535 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54aca4a8-c383-31b9-bde2-6e5df3e7cb80 | -11.4324 | -45.109501 | 2025-07-29 00:22:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3474a06a-aad0-308a-be76-0ad17139d53c | -13.0025 | -44.8937 | 2025-07-29 00:22:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc921752-fb2d-39a7-bb1b-5f6244d8fdbd | -5.3523 | -53.784698 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75a7caf6-4d57-32d4-8300-f5412ac3bf91 | -6.4159 | -53.343399 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 655720a7-62b0-3ab4-b0ec-c0f66bca37c7 | -8.3361 | -54.737999 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed9fcc08-e158-3ba0-b870-b0ae773d5b39 | -7.4629 | -49.395599 | 2025-07-29 00:22:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f755541-a99e-3330-86a5-55c217dfa218 | -6.3848 | -53.341801 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb0baa74-f5cd-3f7c-88d2-045cde29ff81 | -3.5813 | -47.5126 | 2025-07-29 00:22:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01ca28a9-d091-3097-b2e1-9a7d5162e863 | -14.492 | -50.288399 | 2025-07-29 00:22:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 517eba18-8eef-3eee-85d9-710510868351 | -16.665501 | -47.707199 | 2025-07-29 00:22:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9196695d-2932-30c1-8e4b-dbed66455821 | -14.4904 | -50.280998 | 2025-07-29 00:22:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bf4bcdb3-29d0-3bb5-9e3f-dd03fb9c56a4 | -7.8112 | -50.211498 | 2025-07-29 00:22:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5526da98-c7df-39da-854a-371d6f587ab5 | -10.5549 | -50.237099 | 2025-07-29 00:22:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abbe2ddb-898b-3029-a62b-e88aef30c9a5 | -11.4226 | -45.1119 | 2025-07-29 00:22:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cae86511-78ab-3136-9911-b90e73d637a4 | -7.5233 | -49.7547 | 2025-07-29 00:22:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64ce96a6-f6dd-3fd4-b989-db9f94abe6b7 | -3.3653 | -47.1548 | 2025-07-29 00:22:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f926bb08-a83e-351e-afe8-c36a96b307df | -6.4096 | -53.3615 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e0e4f2c-dd50-31b2-b51e-202a9ea74823 | -14.8212 | -49.243 | 2025-07-29 00:22:00 | METOP-B | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 092f0a30-8549-3fac-b3ba-37dcf89c3cf3 | -15.7245 | -43.236599 | 2025-07-29 00:22:00 | METOP-B | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| be3a7cb1-3a44-3fbd-9073-2d9dc8b3f954 | -7.9145 | -44.075401 | 2025-07-29 00:22:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1aced6a0-9d70-343c-991f-9612d31fc29f | -9.7053 | -48.6035 | 2025-07-29 00:22:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc4a225c-32f1-3e80-a70e-ed7f3eae6228 | -7.2477 | -43.0616 | 2025-07-29 00:22:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 679602c7-0dad-3a03-a9b9-19f0486afd7d | -12.9927 | -44.896099 | 2025-07-29 00:22:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ef35e55-37ab-3353-9db6-f3bf42fc47cd | -9.7069 | -48.6106 | 2025-07-29 00:22:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b6566aa-6987-3386-80f9-a5644e78c007 | -9.6374 | -50.7878 | 2025-07-29 00:22:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a00df35-d14b-32f2-a67b-37f0ff0d34ca | -15.8091 | -41.870899 | 2025-07-29 00:22:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b4bea061-3699-33ba-9c28-eb39937775f1 | -8.3724 | -51.068298 | 2025-07-29 00:22:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4719bf68-5e85-371c-90dd-7d3e9ae15fd9 | -15.1291 | -45.321201 | 2025-07-29 00:22:00 | METOP-B | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b77e9d29-68d1-3b4c-a2a3-3f4d45db8407 | -11.7442 | -48.1856 | 2025-07-29 00:22:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 727b16e6-5ef0-33d6-bda0-2d7378dd3b83 | -7.9339 | -44.070702 | 2025-07-29 00:22:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fcad252e-8e2f-3e3c-9970-4ec04e92083d | -13.0901 | -47.302399 | 2025-07-29 00:22:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c432cab7-d4c3-3425-bdfa-3e999fc652de | -3.7365 | -49.048801 | 2025-07-29 00:22:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49747a9b-987f-33da-8033-fe97cf4cf7cb | -13.096 | -52.122101 | 2025-07-29 00:22:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2314cdfa-8032-32ff-895c-8941b6db16bd | -14.4888 | -50.273602 | 2025-07-29 00:22:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
