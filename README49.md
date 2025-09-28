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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89bbc202-45a5-390b-b152-5749f9ae5e64 | -16.58648 | -50.66843 | 2025-09-28 04:08:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bae97932-0312-3b5b-936a-23c0bd4ec041 | -17.18544 | -43.38416 | 2025-09-28 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0460dcdf-1e7b-3531-b4b7-80ef7c70327c | -19.32263 | -43.81686 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84641077-d5cd-3901-92a0-cf1d522678f7 | -17.18484 | -43.38782 | 2025-09-28 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21cfa6bf-38a3-3070-bd9b-3772e9904202 | -18.11317 | -42.18433 | 2025-09-28 04:08:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dde1a71c-e044-318d-9063-00546fde6449 | -17.71788 | -46.71531 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f31eb12-c121-3db7-acc7-87eb05d2c500 | -19.94349 | -41.65045 | 2025-09-28 04:08:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3fb00774-cc9b-3777-85c5-163c4052a84d | -19.86902 | -43.80627 | 2025-09-28 04:08:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 905e8474-9517-3598-bfaa-b9292e5584b1 | -18.17723 | -53.33454 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4865ad8f-08fc-31c9-ab2d-5f746f92a378 | -22.06397 | -43.01458 | 2025-09-28 04:08:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 26604c2e-6f01-3312-86af-576922ce0572 | -18.0616 | -42.39333 | 2025-09-28 04:08:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 04c6494e-321d-3e72-abdb-9882c518cea2 | -17.43404 | -45.80318 | 2025-09-28 04:08:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 106dff48-2b54-3fc5-802f-3fe4be5daccb | -15.27072 | -56.80421 | 2025-09-28 04:08:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3f7ae3b-91fd-3480-8a37-b825b044c314 | -16.96028 | -53.70871 | 2025-09-28 04:08:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3d24a2c0-288c-32e6-925d-67b887dd4b3e | -23.14878 | -47.06322 | 2025-09-28 04:08:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8a3d4cc-437f-39cc-85fa-750e74ecb897 | -18.18047 | -53.31936 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8eb60bf-cc80-3554-a620-4bfa79afe2e1 | -19.1102 | -41.60967 | 2025-09-28 04:08:00 | NPP-375D | TUMIRITINGA | MINAS GERAIS | Brasil | 3169505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e3d4bb94-454d-3eee-90ae-3e031b2815ec | -22.98079 | -48.35807 | 2025-09-28 04:08:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2cd5061-b05c-3abf-9c96-939a84d371cb | -16.40505 | -47.023 | 2025-09-28 04:08:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d3bb908-7585-3bf7-9828-181e9db56943 | -17.72508 | -46.69697 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4eb95f43-8483-3c1d-9714-2d6099b990e8 | -21.58508 | -48.846 | 2025-09-28 04:08:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10c7c8c9-3a87-3ffb-8088-5f95b7b21190 | -15.95374 | -50.42646 | 2025-09-28 04:08:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2613dc6d-8019-33fe-9e0e-b4d3507ce76c | -20.22219 | -42.72731 | 2025-09-28 04:08:00 | NPP-375D | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 51e5234a-b4a8-33da-a7b4-d6997779558b | -18.20235 | -53.32776 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a61eabe7-c17e-3016-a0fb-961517af0bc7 | -21.00394 | -50.03053 | 2025-09-28 04:08:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2e3c89d1-7728-3e13-a093-e62495e14b7b | -17.75575 | -48.76485 | 2025-09-28 04:08:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaa02c64-68d6-3acd-bdb0-4810926f77b4 | -17.73178 | -46.70315 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e3fe4fb-8aba-3b04-bd8a-2b75f2c80eea | -18.56312 | -44.02044 | 2025-09-28 04:08:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1fcb7fa-bddb-314e-9782-2f200fbc4b64 | -19.32454 | -44.17019 | 2025-09-28 04:08:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7a3007d-baa3-3092-ba0a-8cc1da0cde35 | -22.0567 | -43.01715 | 2025-09-28 04:08:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a1e26e49-0cf2-33eb-a372-e74b28cd2886 | -16.23656 | -49.70208 | 2025-09-28 04:08:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a90f8ce-d803-3f85-aaba-1a3f9e70596d | -20.69618 | -50.71429 | 2025-09-28 04:08:00 | NPP-375D | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 8eb199be-7b4f-3982-88ae-a024638dca06 | -19.85842 | -42.59378 | 2025-09-28 04:08:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8eeae4f6-2e49-3986-ba73-64b49d8a0249 | -21.58366 | -48.85348 | 2025-09-28 04:08:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| e17ad098-aa91-3714-8e19-25c560f7e019 | -21.58037 | -48.84878 | 2025-09-28 04:08:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 07bab758-13b0-3486-964e-dd68970652ef | -17.73261 | -46.6985 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c126d9d-f53f-31f4-b9d9-64f6f6cfe675 | -17.72885 | -46.69769 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b24b766d-2978-39ca-94ef-a88401fead61 | -17.19154 | -43.38903 | 2025-09-28 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b4600bd-ab02-30cc-b797-ef38adf997d3 | -20.1651 | -41.72885 | 2025-09-28 04:08:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| e1d97900-ad45-3aef-808a-ed22296c0d6d | -17.72253 | -46.7112 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fc377de-70d1-3bb9-b699-dfad3bdd77a5 | -19.50438 | -42.13153 | 2025-09-28 04:08:00 | NPP-375D | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| b302c721-10fc-3e01-9cf1-5f3074cae8ae | -18.19895 | -53.31592 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e47463f4-9e98-3a5d-af3c-9f8dd83db0b3 | -22.1383 | -50.01886 | 2025-09-28 04:08:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 90755914-2c1b-32c8-8182-315728ed490e | -16.82296 | -45.51119 | 2025-09-28 04:08:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c627f152-d3ff-3fb8-9ff2-ba1f2953341d | -20.6942 | -50.70695 | 2025-09-28 04:08:00 | NPP-375D | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 430ee83e-00bd-3215-ac3f-f09cdc0bfb90 | -15.59844 | -53.15349 | 2025-09-28 04:08:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4463c89e-f2d1-302f-b876-fcc93fbeab9a | -21.39711 | -40.99874 | 2025-09-28 04:08:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8042dc04-a7a7-3f04-bd19-41d9fb0dd016 | -20.69677 | -50.71801 | 2025-09-28 04:08:00 | NPP-375D | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 08506527-b948-367b-9964-500f19f3856c | -17.71582 | -46.70501 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| baf89b2b-153a-30a5-b515-ba690445a9a8 | -19.31473 | -43.82307 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a6d4479-5af4-3de3-bea5-ed7c6fcba647 | -20.99977 | -50.00579 | 2025-09-28 04:08:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 06a5b127-7795-3f0c-a07c-e689d4a70e59 | -17.42966 | -45.80687 | 2025-09-28 04:08:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be1b5514-b700-3c3e-bb64-ecee05aa64f0 | -22.14258 | -50.01969 | 2025-09-28 04:08:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f190dac4-34ad-35ec-a8c4-0f74d0ed1796 | -18.06436 | -42.39754 | 2025-09-28 04:08:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d061fc0a-bd76-3889-bb53-4796ab0c0ba2 | -16.96324 | -53.69517 | 2025-09-28 04:08:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 37b61d02-4874-304b-908a-68fdcd0d49c7 | -18.90744 | -41.12931 | 2025-09-28 04:08:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| a11d80bc-0de0-3c5e-aad0-9bca730eea91 | -19.33145 | -43.82625 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21b00b68-effc-32dd-9007-c53d3cb48092 | -21.44361 | -44.9041 | 2025-09-28 04:08:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 333c8449-d39f-3043-a8b6-8baa9cf9482e | -17.71961 | -46.70569 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3277f3b5-3f60-3462-b5b9-aeeb77b2743d | -18.19698 | -53.32518 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45c75919-0984-3e73-a334-2833ddcc13fc | -15.26886 | -56.81241 | 2025-09-28 04:08:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22aebc6c-ab62-31ce-8e62-2e7f108990eb | -19.50814 | -41.69772 | 2025-09-28 04:08:00 | NPP-375D | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 12f6dd68-767e-3019-8df6-bed7c07cf02f | -22.89715 | -43.58344 | 2025-09-28 04:08:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 86795506-f28e-342b-86a5-90f4904ff751 | -18.03354 | -51.14603 | 2025-09-28 04:08:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b86565e-2ebf-3db6-842c-57d26fcfcc68 | -22.06121 | -43.01021 | 2025-09-28 04:08:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 50a87c4e-c4f8-3e25-b754-a3d65eafb54e | -19.92758 | -46.95341 | 2025-09-28 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e2ba492-39d6-3532-b47d-c846d2715dd5 | -17.43328 | -45.80755 | 2025-09-28 04:08:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efbc354b-2561-304c-b55e-4cf02bcff552 | -20.08672 | -46.16681 | 2025-09-28 04:08:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 15b28e10-d30a-32a8-afb9-e1aa54cc3a43 | -19.98914 | -42.33797 | 2025-09-28 04:08:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e43ba236-1c22-3e1c-8dc9-723f8d4dbd94 | -22.94411 | -49.88029 | 2025-09-28 04:08:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4767b36a-0a87-305e-8bce-8aced480f689 | -19.12648 | -46.66317 | 2025-09-28 04:08:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3580afdd-a7e5-339e-8f1a-89bfb65a8a93 | -19.47946 | -43.80292 | 2025-09-28 04:08:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7378d7bf-3caf-3039-a295-6d258400c0db | -20.69875 | -50.7081 | 2025-09-28 04:08:00 | NPP-375D | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 19c8edcb-e138-3974-bc38-19d2ec081b9f | -20.15508 | -41.53804 | 2025-09-28 04:08:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8ed457c8-a81d-3507-9629-bf151fa48ddf | -19.86628 | -43.80196 | 2025-09-28 04:08:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 8c504f8e-cf7d-3fec-b2b5-0c4862999421 | -18.19981 | -53.31187 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d4cfd57-6dc0-34c6-8fe6-a43fde2856fb | -17.7263 | -46.71195 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 117a5dee-9be5-36fd-ba79-fa25a651b857 | -19.2055 | -43.97631 | 2025-09-28 04:08:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2cfd9dc4-5731-3736-b7ed-53877de1a423 | -18.17937 | -53.32452 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 023f4059-f111-35fc-8bb3-89b74a8fba9b | -20.52463 | -43.0453 | 2025-09-28 04:08:00 | NPP-375D | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 067c51a9-bc17-3691-bbf1-5cad2b14998b | -17.1809 | -43.39086 | 2025-09-28 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcd01b8e-1dc6-3ddc-a5da-220149d4e16b | -18.11261 | -42.18795 | 2025-09-28 04:08:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2c501d4c-0743-3bac-8c63-f512a9d5c8b8 | -20.40441 | -46.4678 | 2025-09-28 04:08:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d83a3b1c-6165-3f6c-bfe7-9470a5ce6679 | -20.69221 | -50.71693 | 2025-09-28 04:08:00 | NPP-375D | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 452a18d9-8f3e-3f8b-9aed-0163924af330 | -21.8001 | -45.32565 | 2025-09-28 04:08:00 | NPP-375D | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 97343fc4-e465-3b98-9d0c-f156532855db | -21.0032 | -50.01137 | 2025-09-28 04:08:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 82b4ed8a-01a5-3cd4-bcfb-58c0d6ef1e81 | -17.18425 | -43.39148 | 2025-09-28 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36a57c5b-34c1-3cd6-9bf5-e8672761e437 | -16.40597 | -47.01785 | 2025-09-28 04:08:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b3bed84-fda8-3429-ac39-ed49cfccec71 | -19.67614 | -43.72326 | 2025-09-28 04:08:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccb5da10-5663-3516-8009-314b598a59ef | -19.32142 | -43.82431 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f716724-c49b-3276-b42e-62dd95bc5b76 | -21.1267 | -46.82812 | 2025-09-28 04:08:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27b9aea7-75c4-348e-a16d-6d6d218cb562 | -23.27804 | -46.60357 | 2025-09-28 04:08:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 65685099-79b2-32ea-865b-b32e726365eb | -18.19802 | -53.32026 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 17c93bcc-3a73-37b2-a937-69cd6e84706f | -20.70174 | -50.71046 | 2025-09-28 04:08:00 | NPP-375D | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 56e9160c-8093-3c33-bae9-d28b72f1a12f | -15.6074 | -53.16922 | 2025-09-28 04:08:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f93d083-4b6f-3c87-87be-e57cd82abf02 | -19.31199 | -43.81873 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bed1fbe-83e5-3137-9ca1-03b361583a07 | -19.32657 | -43.81378 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7439c7a1-63bb-3e68-932b-770b50eee2ad | -19.31808 | -43.82368 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40694cf4-9e47-33a0-8c21-7b1876573f34 | -19.32444 | -43.80571 | 2025-09-28 04:08:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7ccca19-0181-3b2c-b792-59caa8da8ab2 | -19.608 | -43.82545 | 2025-09-28 04:08:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README50.md)
