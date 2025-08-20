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
| 749c58ec-6704-3c53-aeb4-7d1ce1beb5e1 | -6.0974 | -44.64106 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e31087f-11ad-3b4c-ab64-4d94c30eb668 | -6.57206 | -43.02008 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 595ab8e1-656c-3b10-aa67-5d35fd7daf4d | -5.11529 | -43.22054 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f751903c-497e-353b-b930-be16f45c6f76 | -5.78088 | -43.8944 | 2025-08-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1096e72-34e8-3db1-b982-53db54b470fb | -7.02502 | -44.60005 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b65c4d29-4965-392e-9acd-eb2d617c80b4 | -6.85168 | -43.60741 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15f5fd27-c18c-3e4c-ae29-a13e42f63582 | -5.66034 | -43.50295 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 712cea7b-e291-32b1-a0d8-0f3895f26610 | -6.95531 | -42.87346 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| f80b4d19-2c8a-39da-8415-15c33aadc336 | -6.56091 | -43.49281 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c11ff38-7eb7-3730-9f38-ef72d6e7daac | -4.60339 | -43.32711 | 2025-08-20 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a31a58a8-94b8-3d3b-a7da-e4075f0504a2 | -6.26991 | -43.70892 | 2025-08-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84410090-5be9-3fb9-be1c-3b729531596a | -5.68976 | -46.46772 | 2025-08-20 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a6482c9-7458-35d4-b14e-fcc23f267822 | -6.64807 | -43.89263 | 2025-08-20 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7f20b20-b051-3619-9f75-574f3b50185a | -4.87282 | -47.75942 | 2025-08-20 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b1b2817-0e84-3579-ae29-50c690c4685e | -6.42435 | -42.48957 | 2025-08-20 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50a9cdb8-48b7-3742-a7c2-e0cb5b062059 | -4.91266 | -43.23817 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf6b9012-1013-3ce4-83f7-c85417fb19e1 | -6.55418 | -43.00265 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd5a792e-b499-39ab-bdd0-0af4cab216b3 | -6.9514 | -42.87647 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| d134212f-ee53-3967-b545-af3bcb98c59c | -6.28361 | -43.71124 | 2025-08-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da5b7cf1-21b0-3493-8e6a-3bb3d0065a8f | -6.8585 | -43.60847 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e2f882a-d651-32b7-b106-f1b3ed9dc6d8 | -5.99607 | -42.85167 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7f738db6-030f-37a7-ba42-36e4837758dd | -5.64472 | -43.37916 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17df11f6-a0c2-3eeb-810a-628909fd6cc1 | -6.04681 | -44.11753 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d840bad1-ec97-3d95-b054-6530aee99700 | -10.34714 | -44.90827 | 2025-08-20 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30f3f520-5266-32e8-8af1-e6aaa435caee | -6.18411 | -44.52795 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65960fbe-d746-306d-8218-1b7c9fb2c869 | -9.53315 | -45.17745 | 2025-08-20 04:08:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a409eb1-a91a-372c-8e6b-f7ee294eb846 | -5.86374 | -43.43984 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd280f00-0a85-3ec6-985c-25d4fc2a3666 | -6.0999 | -44.64029 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dea5d17-2a6d-3a46-8569-da785fabe811 | -6.28018 | -43.71073 | 2025-08-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4ce6b05-c646-315e-84f1-2b50e5f7307b | -2.91305 | -48.29991 | 2025-08-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0a211152-d68d-3641-8e72-b5b2010ca936 | -6.07043 | -44.4001 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79e83d14-0bf5-3df5-996a-91e0e8ec1cc6 | -6.5781 | -44.4697 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f06521e3-30f5-3199-95bd-ba07e7123e3a | -7.63199 | -45.27448 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f249b09e-4ff5-3abc-91aa-fa25061b6118 | -5.79056 | -43.89132 | 2025-08-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d0b342ee-5b2f-31e0-9efb-09a6d84f883b | -6.28423 | -43.70744 | 2025-08-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b14c9afa-4e44-3e87-ab63-6c9e146a1074 | -5.88208 | -48.12577 | 2025-08-20 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf4ef427-85af-3556-b8e4-e81474d5abef | -6.91706 | -43.83448 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 050ce9c8-e1ba-3f14-8088-363cea547cbd | -5.79036 | -43.61203 | 2025-08-20 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 126d7437-d4a5-3154-81ec-5371e7bb7b6d | -5.70114 | -45.87119 | 2025-08-20 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb73184c-c291-3b77-82d2-f5a0ec73be87 | -4.91726 | -43.23134 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c46036ba-72f9-3624-85ff-6ab4970c48c0 | -4.29745 | -48.07316 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fa45afe-fa76-3ef6-8eea-413855fa1353 | -7.23277 | -44.25417 | 2025-08-20 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d0c5d37-9de5-3215-b08c-7f1d2c9989bd | -3.4817 | -47.67979 | 2025-08-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dd74a7e-050d-302b-8698-8f1046fa9edb | -8.15494 | -45.56131 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c8d296b-e196-3943-9701-653e6e3050b3 | -6.34586 | -42.92181 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e105936-3a5a-3beb-bc26-3ebf1b1248f1 | -8.03385 | -47.66217 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 75032b1a-d0d5-3639-bd28-71dcfa951363 | -5.40952 | -45.18784 | 2025-08-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1cf83e0-488f-31c1-bd6d-f20a2e469dbc | -8.03255 | -47.66981 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6c752b79-852e-333b-9e4d-3079a50fb49c | -6.27638 | -43.69069 | 2025-08-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da1ebfee-9483-3f0d-a416-f84ebdbc5561 | -5.99107 | -42.83992 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d2681abe-d0fd-3012-8137-ced8e4f22490 | -5.40412 | -45.15087 | 2025-08-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 596ead8c-9cb0-3943-9801-aa4c3bc4f941 | -5.99728 | -42.82251 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0be80c1-a0f5-3773-9452-182d74273805 | -6.02371 | -44.3525 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c20073ee-7f1e-327a-be5a-9bda3f2278a5 | -5.32043 | -44.48582 | 2025-08-20 04:08:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f1bee011-c5d3-352d-9d27-f34877a4bf96 | -5.14014 | -43.72848 | 2025-08-20 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9b56ba0-047f-36ef-8038-4316c8fae7e0 | -4.64681 | -43.1211 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2caa898-44ef-39e3-84c3-709ba9b472dc | -6.61828 | -43.88006 | 2025-08-20 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6ff22ee4-4213-34eb-be4f-9c417d029475 | -4.65022 | -43.12164 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 152b9509-7338-3d7e-bb65-277cc43f85b7 | -7.2929 | -43.68087 | 2025-08-20 04:08:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6327d1ac-7e1d-3d68-808b-e5bd7a0eb855 | -6.00732 | -42.82413 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fd6f0c9f-3499-3e4d-8b7a-f3cef71e9479 | -6.58097 | -44.47435 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13e4b1b2-5ef0-3d96-828a-3f6b4284ab8d | -7.63926 | -45.2756 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b87209c1-81b9-3e46-b563-59785af9bedf | -6.8625 | -43.6053 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d23d17d-5c50-3590-8314-ce0c71aec7ee | -7.1485 | -44.19002 | 2025-08-20 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22bf28fd-c4a2-396d-86a4-0d0710a0d0b6 | -8.65444 | -54.58794 | 2025-08-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1a3744e-e9a1-37bd-a597-e7438733cb4b | -6.00675 | -42.82773 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a83a3bc7-1b9b-32a5-942b-52a07d659b02 | -6.86652 | -43.11467 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b705a81d-bc0c-3a0e-9ed3-3b8888fafc06 | -6.72286 | -43.95138 | 2025-08-20 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f187edb2-755a-3f8a-a6d5-3d24b35c59fb | -9.57558 | -43.32343 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 715a38e9-2597-3d33-bd2d-a5377711a406 | -6.72358 | -44.33378 | 2025-08-20 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d133461b-49bc-3887-97c3-b631720b1964 | -3.81845 | -41.56112 | 2025-08-20 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ff022e4c-3ec7-3af1-a293-b9da3929865e | -6.97034 | -42.86499 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05d36cfa-3ca7-34cd-98a3-e98374f7aa40 | -7.07112 | -46.87977 | 2025-08-20 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd1d9920-c909-3bdc-bbf1-0ceee84d6edd | -8.30626 | -55.10556 | 2025-08-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a695127-80fe-39eb-8196-b35fdb65d000 | -4.48867 | -47.67994 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c7acab4-01da-3d07-be87-077ca002f677 | -7.58398 | -44.40002 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0fdbfd9d-1aad-3537-9f98-e667e308df83 | -6.86532 | -43.60952 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f40bc93c-5b12-322e-ab86-6794c11d8631 | -5.63545 | -43.41571 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb58198f-98e6-32ca-aa3c-99e97d448c6d | -6.00088 | -44.29162 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40d0cad3-7d81-3c6f-9f1d-0a3719eab44a | -4.17406 | -42.02576 | 2025-08-20 04:08:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 3d14a768-6c43-39e5-befe-f5070a6ae1b9 | -5.34275 | -43.5341 | 2025-08-20 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| effdfaa1-353c-3602-bc4d-a4a42e47a413 | -7.65519 | -45.26941 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32162b4f-674e-393c-b8a1-bada9cb56163 | -6.37212 | -43.26821 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed301a8c-0b33-366f-9676-66e31a573cda | -6.00023 | -44.29566 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53f93963-24d1-3470-ba78-feada5d90b91 | -5.43206 | -42.35355 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e58d62a5-104f-36ea-a3ce-7b30aeabf519 | -7.2733 | -50.19153 | 2025-08-20 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b73438e1-a7c5-3c71-8c8e-0ca9b2fb1eef | -8.15056 | -45.56504 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efab1ca4-de8a-38c7-8a78-e6255795001e | -7.63268 | -45.27031 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c307bd4-b728-32f5-ae3d-46159ec628c4 | -6.29024 | -42.79674 | 2025-08-20 04:08:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6ccda48b-0469-34af-b27b-ff859451f19b | -7.20529 | -46.24625 | 2025-08-20 04:08:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a81826f6-12a4-3587-87ac-aeab8a75a969 | -6.23667 | -44.44982 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e26dbcc1-8853-345f-b430-8614f4915deb | -6.56089 | -43.0037 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05881b4e-a1fd-3c75-b462-c215d47894fe | -7.22504 | -44.70887 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 272666db-ea5b-36a7-af82-81b15364cabb | -6.01001 | -42.87216 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2178c2c4-4564-3841-87bb-d98f274a543f | -8.81991 | -52.03358 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd233ef9-28e2-3b4d-9543-6a499a7cfa6b | -4.40988 | -42.14905 | 2025-08-20 04:08:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 595905f4-2b3c-379e-83c2-6ee707433a8f | -5.9775 | -44.14663 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e333165d-bfdf-3851-b405-40f1dfa71909 | -3.97189 | -42.50734 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4b2d6569-2f3d-3f51-a500-13973a26233b | -7.97479 | -55.30394 | 2025-08-20 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddc89e61-e371-3a52-acba-dd16deb26aa3 | -7.59221 | -44.3934 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README15.md)
