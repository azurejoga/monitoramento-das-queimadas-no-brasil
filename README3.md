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
| 5db40fb5-f966-3bc1-a59e-1752fc7b73d7 | -17.36442 | -42.69976 | 2026-05-14 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 220abe3b-77f1-3863-be84-bf9df4fa7ab6 | -17.37548 | -42.69423 | 2026-05-14 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7973cc4f-6937-344d-8233-203bcdaa0109 | -11.73465 | -54.24089 | 2026-05-14 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e22facf-55e8-3254-88e8-3aebbcf0caa9 | -17.36499 | -42.69616 | 2026-05-14 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 69d5a72e-bd8e-30c7-bfda-12f4081701ab | -11.97073 | -43.83715 | 2026-05-14 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c41acba5-d759-3ae4-b35d-cb99846de0a8 | -13.3128 | -43.02708 | 2026-05-14 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 767c18b4-2478-3477-955d-34ee4728134a | -17.36829 | -42.69672 | 2026-05-14 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6b0abc72-7fe4-3115-b210-1e36efeac2a5 | -11.79286 | -40.08141 | 2026-05-14 04:04:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 222d6fd8-4598-35c0-a382-44165d9c92b7 | -11.97892 | -46.79023 | 2026-05-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 451e2591-b746-35b2-bf3e-49d5e833140e | -12.21371 | -46.5778 | 2026-05-14 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e74bf4a5-d157-3933-9f74-544ec71425be | -11.98307 | -46.79101 | 2026-05-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 858a8ee8-a0dc-3458-adda-e1f674521abc | -14.11174 | -45.29103 | 2026-05-14 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e048d356-2351-35f1-bf51-2f0eac043b29 | -11.78167 | -43.6629 | 2026-05-14 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d3f1f19-c504-338b-9ac4-ac61f81bb5bc | -11.73899 | -44.52576 | 2026-05-14 04:04:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 558db01d-eaa9-3382-bbfc-be7779bc048d | -11.31089 | -54.03865 | 2026-05-14 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9d2c43e-0504-3313-a398-f184a395a73c | -11.73723 | -54.24189 | 2026-05-14 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 64c52298-7fae-32f7-bff0-510692e1414c | -17.36773 | -42.70032 | 2026-05-14 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f86d3ac-97a7-3011-99ae-d8dab7c94b7a | -12.21472 | -46.57727 | 2026-05-14 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75116897-29a9-3741-9730-204b78882e15 | -15.9 | -43.21766 | 2026-05-14 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e6a0de5a-12c6-3810-a078-90ab32e62efe | -13.68549 | -44.2935 | 2026-05-14 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55a7d89b-d552-3ee4-8c66-1796e04895f4 | -14.10729 | -45.29486 | 2026-05-14 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4957a87d-d004-39f0-8740-08bd0f0a04e2 | -16.76523 | -45.8225 | 2026-05-14 04:04:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ac8f02b-318c-3ea6-9e44-5304891a24c7 | -11.9094 | -43.74532 | 2026-05-14 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c09bda87-9eda-3a2b-9617-fe41c1d5f48d | -12.21438 | -46.57405 | 2026-05-14 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82677804-cf67-3bf8-b972-b41180e6d0a4 | -21.56211 | -47.03244 | 2026-05-14 04:06:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6f4d084-83fb-3f99-90fa-6722b06a7b59 | -22.92852 | -48.91146 | 2026-05-14 04:06:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6db89de-424a-3c61-afda-e47543e36351 | -22.93352 | -48.9068 | 2026-05-14 04:06:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d6dfe80-734b-376c-916e-c307f4f40161 | -22.05973 | -41.52463 | 2026-05-14 04:06:00 | NOAA-21 | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6ea4ba3f-e287-3907-8be5-699f26619ba3 | -22.06315 | -41.5252 | 2026-05-14 04:06:00 | NOAA-21 | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 19efc427-10a2-3680-bac0-4891b871c76f | -21.55847 | -47.0317 | 2026-05-14 04:06:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc73938c-9ff3-3bf9-80b3-d17ce024651a | -22.84341 | -47.22081 | 2026-05-14 04:06:00 | NOAA-21 | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| fa9f4e6f-8f88-3304-8bf4-4be0a60447a7 | -23.40772 | -46.4359 | 2026-05-14 04:06:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e2307c50-9c8d-3e6f-8903-b1d97f0a9f58 | -22.87348 | -48.62721 | 2026-05-14 04:06:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 904e8113-5b81-3545-ab9a-217da1be19a2 | -20.22414 | -40.36494 | 2026-05-14 04:06:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 80717ec8-c831-3cf5-bffb-de6323a21830 | -19.19277 | -49.12976 | 2026-05-14 04:06:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a86b328c-fdfb-3a84-94b0-dd40700e5e6a | -19.19784 | -49.1265 | 2026-05-14 04:06:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 331a5af6-e419-3db2-8f8a-5bcb559c96cc | -19.19703 | -49.13067 | 2026-05-14 04:06:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7e09894-fe1e-3e53-a7e7-fef0a44c3973 | -12.61962 | -44.51447 | 2026-05-14 04:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 083755f2-f6f6-313b-95fb-594c30bb3522 | -9.3913 | -48.43666 | 2026-05-14 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab7ddc95-057b-39f7-b3e4-1a642752b5e7 | -11.98301 | -46.79066 | 2026-05-14 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0ef1a79-79e3-3604-876e-3bd52d7d9228 | -10.54899 | -42.44737 | 2026-05-14 04:36:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 25a03bdd-1667-3284-958c-7c76077a7fc4 | -12.30269 | -47.90466 | 2026-05-14 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83e844b3-e861-3c87-90f4-86fb063e5485 | -8.53794 | -51.58104 | 2026-05-14 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f53dbc33-f3c5-3350-9da3-a2109e855559 | -8.27028 | -48.24147 | 2026-05-14 04:36:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6224022a-b0e1-35f8-b817-3390df58b33a | -12.65054 | -47.09122 | 2026-05-14 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9752cf01-ba2e-3dde-8022-1fd38d58305b | -12.05207 | -45.2823 | 2026-05-14 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e492148-af46-3cc8-8470-6a7e6a5eee4f | -11.18193 | -55.925 | 2026-05-14 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 10dbf3d7-12c2-356a-8c1f-da4b9651db2f | -11.73688 | -44.52829 | 2026-05-14 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50ac12ca-fc8f-3732-b3aa-ccfcb31e013c | -10.11835 | -47.9363 | 2026-05-14 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12d2ca51-7e29-3de7-a2f2-7ee64109b2a1 | -11.76523 | -47.06407 | 2026-05-14 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f85da6ea-c84d-3419-9a39-a134f3bb3970 | -11.77989 | -43.66208 | 2026-05-14 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5b00b33-6c5d-3fad-b239-ca1d875a9fcf | -11.97324 | -43.83746 | 2026-05-14 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e589e3a-289f-32ff-811d-c23b47cb6623 | -9.46552 | -40.33475 | 2026-05-14 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 63f3a488-abe7-3dad-91a0-6b7a88ac8918 | -11.41958 | -47.09241 | 2026-05-14 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3ca3e36-5362-3cf9-aca6-f85c10a89265 | -11.62913 | -54.15664 | 2026-05-14 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f345296e-1ade-3d41-98e7-091cad9372a7 | -12.21407 | -46.57613 | 2026-05-14 04:36:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f90f6bd-3d4c-36f7-897d-d6698201a03a | -11.3095 | -54.0332 | 2026-05-14 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfdbf603-3767-3c4a-a83f-fd2747e641fd | -11.73813 | -44.51984 | 2026-05-14 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a87e5134-90cb-32f2-a2d4-4ba577bca355 | -12.11653 | -43.64594 | 2026-05-14 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bedf2fb4-6b20-3a3e-a777-2427fee15170 | -10.66399 | -49.71457 | 2026-05-14 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03d8fe21-2e17-3f4e-b217-1bb4eb3287a2 | -10.40196 | -49.4428 | 2026-05-14 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f78cfde-591d-3fab-9b60-1ef400a61102 | -12.61596 | -44.51393 | 2026-05-14 04:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ef91f78-638d-375e-b862-1b82b883ca8c | -11.4377 | -54.09687 | 2026-05-14 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c283b8e9-4195-3872-b382-b166f1a3b1b0 | -11.93388 | -43.36956 | 2026-05-14 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 180e702c-caeb-3d04-a4c4-0dfb9531f49d | -12.64719 | -47.09068 | 2026-05-14 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd6a0497-b42f-328c-9c40-1d44c4737402 | -11.97965 | -46.79013 | 2026-05-14 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 010dc4b8-4de6-3f26-b052-48814058a89a | -8.10821 | -44.18335 | 2026-05-14 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a73d570b-c27a-3221-b2eb-aa88623d8a30 | -11.76467 | -47.06762 | 2026-05-14 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7873000-699e-3066-9c26-014943980f6d | -11.04408 | -49.53205 | 2026-05-14 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7063ad7d-0c85-38fa-8ea2-6c3a6a3f66bf | -9.46597 | -40.33339 | 2026-05-14 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 56941e33-07ce-3e55-881a-6566d0d5914d | -12.04796 | -45.28571 | 2026-05-14 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01878b8e-d4d7-3f5c-919a-6fc1f015dc50 | -11.79753 | -43.62135 | 2026-05-14 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cce557c0-9736-39c9-be81-e18cd62f18b1 | -8.2697 | -48.24509 | 2026-05-14 04:36:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07fa97e2-2ba7-3db5-a053-d4f3fdf5ab9f | -11.82297 | -46.64849 | 2026-05-14 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 984dad79-b74a-3e2e-9194-5bed81538e06 | -11.96822 | -46.78883 | 2026-05-14 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f6ee9573-fbcb-3b40-ada9-27779db0e073 | -10.12169 | -47.93683 | 2026-05-14 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6398aac8-44f2-38e8-97c4-7e57ecc5d21d | -9.46489 | -40.33941 | 2026-05-14 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 99c52922-6e40-3ac5-8636-e227d398be18 | -7.22603 | -47.02348 | 2026-05-14 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 285d1c06-6754-3b3e-ab87-070625bd1ab5 | -12.85337 | -43.76131 | 2026-05-14 04:36:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6756345a-7a86-3a8d-90d9-eba39f68996b | -11.43849 | -54.09249 | 2026-05-14 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5b4227f-d00d-3300-91ec-9839228e5100 | -8.11529 | -44.18443 | 2026-05-14 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd55270e-7075-359a-90aa-a7b34d3e41bf | -11.90975 | -43.74288 | 2026-05-14 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 33e8c43c-f67a-3556-a9cc-c364516982e0 | -11.17885 | -55.92228 | 2026-05-14 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e580568f-c920-3e75-bbb3-24b96bc9ac01 | -10.12112 | -47.94037 | 2026-05-14 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76d96146-9307-3f64-9887-c9317103c296 | -8.10882 | -44.17935 | 2026-05-14 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2116901f-bee6-3f57-a510-64a06e04b0d8 | -12.61532 | -44.51827 | 2026-05-14 04:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec0a56b9-d93d-30c5-8f3a-be1b0566f38f | -8.85397 | -50.21212 | 2026-05-14 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4b24bed-16b1-3372-94b7-4b019abc6c3d | -8.54199 | -45.98847 | 2026-05-14 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ada69a4-30e5-3c27-8222-202720a1f3cc | -11.44291 | -54.09332 | 2026-05-14 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ae48e4f-80e2-3c6f-959d-8d9094b7ea30 | -8.10528 | -44.17881 | 2026-05-14 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 239bc46e-84f1-364b-8622-41a7fbd51748 | -11.18694 | -55.92597 | 2026-05-14 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc79d2dd-cea3-334c-ac75-57b094a13779 | -11.42292 | -47.09295 | 2026-05-14 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5425e746-23da-35b6-9feb-ec1fcf7b7992 | -9.55998 | -44.57728 | 2026-05-14 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60578caf-cf49-38d3-8d5b-ef33d766511f | -10.55704 | -42.44853 | 2026-05-14 04:36:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a2308a1-8e3e-3d56-9ec3-2aa1b0b96b06 | -8.11883 | -44.18496 | 2026-05-14 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21e01a30-0dbf-30d1-9aae-c1b500b1ca7c | -9.46987 | -40.33869 | 2026-05-14 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a976b970-8663-3556-a518-12e23ae1c6d9 | -12.11552 | -43.64381 | 2026-05-14 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cf981762-0c56-3ea0-9968-9edbb6af70b3 | -8.27366 | -48.24203 | 2026-05-14 04:36:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fc3b187-1661-3ec5-93af-0f3de8320621 | -11.63596 | -47.88342 | 2026-05-14 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fad06172-60b4-31a7-bba7-248fbaad9630 | -9.76475 | -55.62571 | 2026-05-14 04:36:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
