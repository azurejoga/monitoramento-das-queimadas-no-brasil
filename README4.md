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
| f7f18295-056d-3181-bde7-92ad3064fa09 | -11.46 | -45.098999 | 2025-07-16 00:41:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 08abb98c-4fec-30a2-9f9e-51e5d0d5906d | -7.3452 | -49.598598 | 2025-07-16 00:41:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0e7d242-42b4-36e6-889b-4f6bcae9637a | -13.651 | -45.727001 | 2025-07-16 00:41:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f8bcbbc-1e98-3b07-afe9-37aaccf2d209 | -20.0305 | -47.398102 | 2025-07-16 00:41:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d22ae2b6-c863-38db-9461-8f0cddc81082 | -5.7831 | -45.0672 | 2025-07-16 00:41:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e4c5f61-9583-317f-b593-4c9986cba825 | -9.3118 | -44.838299 | 2025-07-16 00:41:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 23722d34-aff6-37d0-a993-f637acb5e5c5 | -9.8495 | -47.869598 | 2025-07-16 00:41:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 982b6f6f-c1a4-3c3c-879b-f5ab157ab091 | -23.7735 | -47.331402 | 2025-07-16 00:41:00 | METOP-C | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49474935-84ee-385e-93a4-37bdd656112c | -10.9621 | -49.250801 | 2025-07-16 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4fb1d1c4-5c8b-3ec6-9f47-8f974746d909 | -11.4928 | -48.074799 | 2025-07-16 00:41:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfafeb08-a634-39c4-b30d-96c015ec1f5f | -14.3065 | -52.7337 | 2025-07-16 00:41:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7b9384f-5361-30c7-9027-34e1ab921b3f | -5.7274 | -44.830898 | 2025-07-16 00:41:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 649b78ee-91b7-3f68-a69c-a439824ca318 | -13.0293 | -45.050201 | 2025-07-16 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3921d844-8aee-33f1-9994-27fcdcaac70f | -12.0777 | -43.479698 | 2025-07-16 00:41:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b6f84e5-fe0f-3374-a8e7-d5e84d546993 | -5.795 | -45.073601 | 2025-07-16 00:41:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cad710ec-1f33-3758-a6e3-d502bc37c444 | -10.9604 | -49.243401 | 2025-07-16 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1baa66c3-86f8-3bec-84e6-120bc2bd4028 | -13.0213 | -45.060101 | 2025-07-16 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48dcf82d-81f7-34b3-b972-65f92e02c2c8 | -7.1938 | -43.107101 | 2025-07-16 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a2ab926e-b46f-3691-a5d0-b983d180daf8 | -5.8804 | -42.4086 | 2025-07-16 00:41:00 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08ca0b3f-e35e-39cd-960a-38f207bb098d | -12.4914 | -46.927799 | 2025-07-16 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbcd7e38-1548-33a7-9185-9d251e088cf6 | -7.5043 | -46.687302 | 2025-07-16 00:41:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 640d900b-24af-3497-bc1b-9be40d0089e1 | -8.6456 | -47.7444 | 2025-07-16 00:41:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 698bb42f-9f9d-3722-ab1b-4e1f08180b23 | -6.4204 | -45.319 | 2025-07-16 00:41:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ea26399-2b37-3be5-9079-0407605a2f8f | -5.5786 | -46.528099 | 2025-07-16 00:41:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9242e80c-ed8c-3160-a534-ec565a2485a8 | -11.4747 | -47.308701 | 2025-07-16 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5382b4f-5774-3ef7-8c82-26024992a162 | -7.8362 | -44.192402 | 2025-07-16 00:41:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e87cfb8-5a69-3b42-881d-7c210af30167 | -13.0115 | -45.062401 | 2025-07-16 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c697f069-ea62-3f6c-8609-488e4c206024 | -11.9472 | -48.404202 | 2025-07-16 00:41:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e3645c3-6ada-353c-ab4b-25d27fe50464 | -10.5735 | -49.121498 | 2025-07-16 00:41:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79c5608b-1b06-3dae-ba2d-332641433272 | -6.9183 | -52.8563 | 2025-07-16 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 377d8d9a-8257-3e89-a6e9-4cb8a522773f | -6.7307 | -44.318699 | 2025-07-16 00:41:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 727cc4ea-6036-3b61-a8b1-93428ae363d8 | -10.6417 | -44.4776 | 2025-07-16 00:41:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f4d2fda-b292-38d8-a0e6-557bfde73ddf | -12.0659 | -43.473301 | 2025-07-16 00:41:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 66cbc5ce-3799-34a8-b486-d8132c91aa02 | -14.3089 | -52.746201 | 2025-07-16 00:41:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56dcf21e-e6b9-3874-bc15-e3e797951737 | -4.3014 | -48.097801 | 2025-07-16 00:41:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6392a79f-a506-38e7-99c2-6de482de5118 | -12.9967 | -44.8671 | 2025-07-16 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 028071e5-bea4-3f1d-84ec-ed8e347077de | -20.0802 | -47.636501 | 2025-07-16 00:41:00 | METOP-C | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9ff48909-f09b-3f19-9f7d-05af3d1a80a0 | -7.3106 | -45.7682 | 2025-07-16 00:41:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae1ab0a5-2e28-3f53-b116-ceb6283a22ee | -11.9504 | -48.418598 | 2025-07-16 00:41:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20be6444-689b-3d5d-9fc5-4ec36d587740 | -8.537 | -47.856098 | 2025-07-16 00:41:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5461ee08-eb3e-3362-a4a9-472652cde545 | -7.946 | -49.6605 | 2025-07-16 00:41:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb2a9aa-cb5d-32a5-a0c6-77e48972590c | -5.8774 | -42.396198 | 2025-07-16 00:41:00 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8da15775-3805-317c-b951-a910f4b7db36 | -8.7624 | -46.5933 | 2025-07-16 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d4cae33-7d90-3570-9834-035b33a938d1 | -3.8502 | -47.7519 | 2025-07-16 00:41:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b71916f5-dd72-37f0-a35f-73a8cd4edb7f | -8.5452 | -47.846901 | 2025-07-16 00:41:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ce19169-4fb9-34ff-a4b8-68d593233a99 | -12.4207 | -43.744999 | 2025-07-16 00:41:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e42ca49-c052-3280-abfc-4f00919bb71d | -20.3536 | -41.477299 | 2025-07-16 00:41:00 | METOP-C | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 841ccef3-dd5b-3ceb-aee5-241de7588038 | -20.027201 | -47.382401 | 2025-07-16 00:41:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c5134200-3c34-313f-af54-5203f8fa0626 | -3.3291 | -48.714001 | 2025-07-16 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e197e257-a4b4-359a-b840-6afc7ddc11cc | -10.3171 | -49.915501 | 2025-07-16 00:41:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df346c13-ec29-3f06-8ffe-80cd4f0ed09d | -18.595501 | -52.409801 | 2025-07-16 00:41:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a255dbcc-09e7-33bd-abcc-70566eae24a1 | -20.0916 | -47.6423 | 2025-07-16 00:41:00 | METOP-C | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b84c9604-1a3a-37e4-aec0-211d3f0443ef | -5.7325 | -44.504299 | 2025-07-16 00:41:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c73e41b5-9ea6-37e0-9c4d-e210afabf208 | -10.2236 | -55.449402 | 2025-07-16 00:41:00 | METOP-C | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52de3364-94ab-30a5-ab5e-e2514a810ab3 | -5.7892 | -45.093102 | 2025-07-16 00:41:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2de455eb-9927-35a4-992b-369f9dd835c4 | -2.921 | -48.240898 | 2025-07-16 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4af5d30c-a7a0-34c1-a007-d7d88015912f | -18.592899 | -52.396 | 2025-07-16 00:41:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0076b235-bb3f-350b-b052-aa64d9d38417 | -7.1963 | -43.117802 | 2025-07-16 00:41:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c5076619-8f8e-3c57-b50c-bbcf6f3ca5f4 | -6.9162 | -52.8465 | 2025-07-16 00:41:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7da4d842-c98e-3ac4-bbef-c65728b3313a | -10.2854 | -47.610298 | 2025-07-16 00:41:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b33dd4f0-bbde-30fa-a396-5cc51743ab2a | -4.0355 | -48.063 | 2025-07-16 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9cd7cc2-4bef-314d-8129-832440c1d8cb | -2.9194 | -48.234001 | 2025-07-16 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ae28376-3170-3fe4-b7c3-454136d61552 | -5.4653 | -45.338699 | 2025-07-16 00:41:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b7cde09-227e-3da0-869e-2e87622249a3 | -20.0289 | -47.390301 | 2025-07-16 00:41:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 34ad1214-b61b-3765-94bb-9efb80e90ebe | -5.666 | -43.7043 | 2025-07-16 00:41:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3922cc1a-fd01-3cd7-96ad-68ebe794fd4b | -20.355801 | -41.486401 | 2025-07-16 00:41:00 | METOP-C | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a677ee49-5195-32e7-832c-c265fa83dc3f | -13.1594 | -50.777199 | 2025-07-16 00:41:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 61fd0f43-b67d-39fc-a7b6-45a2c2ba5c6e | -14.1573 | -42.8377 | 2025-07-16 00:41:00 | METOP-C | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8d7d9b58-b310-32b0-b990-d5b02654f3e8 | -13.0335 | -45.0794 | 2025-07-16 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| cb473659-f9a1-3abe-9461-69081293211c | -13.0344 | -45.0328 | 2025-07-16 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| b73a1f0f-0bf5-3ebd-9eee-c574994e34fe | -13.0141 | -45.0826 | 2025-07-16 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| e6557364-45ea-3fd7-a830-f6d047e51146 | -7.1837 | -43.1189 | 2025-07-16 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 74f765e3-25b9-3264-86cf-cac315ecb0bf | -6.7194 | -44.3231 | 2025-07-16 00:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| f376f8ee-af7f-3944-b2e0-484cd94bc06f | -7.9374 | -49.6631 | 2025-07-16 00:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8f40a38f-2c76-3852-9eb8-facb383f56ea | -13.0146 | -45.0593 | 2025-07-16 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 0845cf0f-d223-3a7c-aff9-cd23f9fdb5f7 | -7.9562 | -49.6615 | 2025-07-16 00:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5fd0be15-675e-3167-860a-a06f7e86966a | -13.161 | -50.7855 | 2025-07-16 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 2291a2bc-0a70-3182-970e-8897a542fe49 | -7.2025 | -43.1171 | 2025-07-16 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.4 |
| 55a60505-8645-3257-bb3c-49caafeae179 | -5.7943 | -45.0813 | 2025-07-16 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 7b5da55d-2aa2-3d6c-9d8e-f2e501a2c4d9 | -13.1613 | -50.764 | 2025-07-16 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 244ba703-4de5-3128-a3d5-d636a82d4c20 | -13.0339 | -45.0561 | 2025-07-16 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 231.3 |
| bbc870d7-e52f-3add-826e-4899891bdfd0 | -13.161 | -50.7855 | 2025-07-16 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 923f239a-3891-340c-8d51-cb856f4644f9 | -13.0146 | -45.0593 | 2025-07-16 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 155a6cb2-ad1f-3bc6-add9-ed3673e53878 | -7.1837 | -43.1189 | 2025-07-16 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| e6b7e854-d842-3638-baa4-8dae975e91c2 | -6.7194 | -44.3231 | 2025-07-16 01:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ae8f8f45-b7db-3e5d-a35e-8bd566cef2a0 | -12.0825 | -43.4753 | 2025-07-16 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e8f2dd4a-5e17-39b0-96cb-bdd0052fe1a1 | -7.2025 | -43.1171 | 2025-07-16 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| db90e7fd-d878-34d2-9a54-e233908eb096 | -13.0344 | -45.0328 | 2025-07-16 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 95354b5a-024a-3a76-b87b-310b80fb6ea5 | -13.1613 | -50.764 | 2025-07-16 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 3b54ebd0-1195-3205-b2e1-0e42d717dca4 | -5.7943 | -45.0813 | 2025-07-16 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 72f9aa41-e729-38b2-b6fc-15612a26776d | -7.9562 | -49.6615 | 2025-07-16 01:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 87f4ccf7-ea42-32ef-8f96-1b37a82d3508 | -13.0339 | -45.0561 | 2025-07-16 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 15505500-bfcd-3124-96d4-7e355ae71d48 | -12.0825 | -43.4753 | 2025-07-16 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 18762375-48bb-3081-984d-41977bf8e32a | -13.0339 | -45.0561 | 2025-07-16 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 224.4 |
| f7ba66ea-1b24-3994-a5d8-279dd45ff21d | -13.0335 | -45.0794 | 2025-07-16 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 31edfe67-1019-333e-9b04-cbdfe010d9d0 | -7.1837 | -43.1189 | 2025-07-16 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| b6caee8d-88d2-3f3c-ad6e-fd30d8b864ca | -7.2025 | -43.1171 | 2025-07-16 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 67f3659c-e960-3939-9aa4-47a79b682af0 | -13.0344 | -45.0328 | 2025-07-16 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 63af98b1-183f-3abc-b61d-b45aaddb69b4 | -13.0146 | -45.0593 | 2025-07-16 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 49eeaf34-5790-38f8-92f6-b824f513c347 | -5.7943 | -45.0813 | 2025-07-16 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |


[Clique aqui para ver as próximas entradas](README5.md)
