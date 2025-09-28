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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59c66c50-ca96-3afb-970a-2dd9c05053ff | -5.73493 | -42.66416 | 2025-09-28 03:36:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eb46d22c-880a-3328-b570-c696a4c89dd5 | -6.27686 | -43.62797 | 2025-09-28 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d88165c-146b-3390-8339-ad960ad8599f | -5.73861 | -42.83583 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c1b9192b-d2d6-30b2-905f-b0b89d87af88 | -5.91021 | -42.93189 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| acc7c4e7-a691-34a2-925a-256592c149d3 | -5.05549 | -45.31675 | 2025-09-28 03:36:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb294eb9-1c0e-3c9b-9383-b2ae9e890285 | -6.57998 | -43.74232 | 2025-09-28 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76c3da44-e9ad-30e7-89e5-ba90119dabe0 | -7.86734 | -44.57294 | 2025-09-28 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc0f60f9-6e91-398d-94d5-cf68e3033a0d | -8.28995 | -45.44098 | 2025-09-28 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 79eb28d1-70c9-3336-a152-f9bdbba2d052 | -6.45194 | -44.22113 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d846a40-dfb2-3d9f-a9e8-acfe4089ef50 | -5.54294 | -42.83146 | 2025-09-28 03:36:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 81f05285-2874-37c9-ba97-ee162f6ebe49 | -6.27127 | -43.62694 | 2025-09-28 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46fff7d5-a64a-3c0f-a793-066c3ccba1f0 | -8.64942 | -43.99055 | 2025-09-28 03:36:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb9b9a9c-94e5-37a6-b995-ef6752a60af6 | -5.76086 | -42.88343 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 76602e50-3bf0-3818-81c3-e4f7dc648ecf | -6.71059 | -42.76914 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2fa51de1-46b3-32c4-af87-191f968a991c | -7.92419 | -42.67414 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 579a7186-6dd5-3298-a9a7-169ddb424997 | -5.37522 | -42.30339 | 2025-09-28 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5ac9e731-508f-3417-a528-a1cf82031fdf | -7.17004 | -45.50425 | 2025-09-28 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88e35cb5-4974-3c62-92ce-91519b222d9a | -6.69818 | -44.57444 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2142a0db-820b-3e3a-a519-8665f3ae01ee | -4.14829 | -40.0046 | 2025-09-28 03:36:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cce99162-87de-3324-a48d-0f97fee57eec | -6.60913 | -45.08447 | 2025-09-28 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ebff6581-dc92-399b-a3b2-905702bec38b | -5.27487 | -44.73567 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53b42c6b-f0ea-3e57-9f9a-328d519328a3 | -6.53849 | -43.82813 | 2025-09-28 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58fb386d-e0df-3b7a-8beb-9ce64ec42a44 | -8.64676 | -44.86157 | 2025-09-28 03:36:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0b94d0b-cc63-3fad-a9d8-3f1594f46c29 | -5.83319 | -44.4383 | 2025-09-28 03:36:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5c52cf49-faf3-398d-b736-69d86076c64c | -6.27571 | -43.63444 | 2025-09-28 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba45bc28-6ce8-3197-aef9-b970bd729201 | -7.1515 | -45.50876 | 2025-09-28 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ab5aed8-d7a6-3007-ad65-17c0379ae48a | -6.88396 | -35.09315 | 2025-09-28 03:36:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 003d5185-2485-3f3c-8d7c-b56c241dc64d | -3.42194 | -43.16803 | 2025-09-28 03:36:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a5118bb-d1bb-3e16-bac2-544e2334cbbb | -4.15364 | -40.00035 | 2025-09-28 03:36:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bf1357d6-4411-3659-9e05-a1abeac33ad7 | -6.7117 | -42.7627 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7ceba208-96db-3423-b3c7-5e51c4321668 | -5.63885 | -44.92797 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e04d9a30-f7a1-3075-a2d1-2a7df7c56f76 | -6.6934 | -42.74341 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 145bdb95-fc1b-3ab5-89a7-220f44e318f0 | -6.70531 | -42.7684 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b70e876a-be22-37a2-86fa-d219b8e108cc | -4.68306 | -41.95527 | 2025-09-28 03:36:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8d2f4c70-80fa-3d3d-bbd5-b3bdedc44184 | -7.10149 | -44.23613 | 2025-09-28 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3115b03f-3e5c-3692-9d54-c3a634c33eb3 | -6.27327 | -42.48824 | 2025-09-28 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b8dd475d-fa2b-38bf-9b05-375a79d945cd | -6.70067 | -44.57196 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 936700f0-7876-3d86-ae21-8d7739bc6ff1 | -6.35147 | -44.31364 | 2025-09-28 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a448cc68-841a-3493-9274-1b6268a5e926 | -7.04748 | -44.76508 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f07ca13d-8281-36c5-b568-06703afa39ac | -7.23149 | -44.7694 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bcccf4e-a4fc-39a7-ac97-6caa48969242 | -5.7378 | -43.37324 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d1030b7c-ed57-3214-b5ca-c8ba45a6c28f | -6.69313 | -42.77611 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 396a3837-4617-35ff-aa3e-055c0d0743ac | -6.3177 | -43.46289 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f15e3811-955c-3694-beb6-226ebe0fdf66 | -6.49962 | -43.71881 | 2025-09-28 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dfe1ff12-b437-3f37-aedd-906d1d06bb31 | -5.41165 | -42.28428 | 2025-09-28 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e1417ac2-731a-39b0-b6c0-f04433b5cff6 | -4.87145 | -45.8556 | 2025-09-28 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff513930-7e5e-3f15-b079-7469ea5a3ffe | -5.90964 | -42.93523 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| bd5c7824-dd9e-3dc3-b17f-2ccba9cbf609 | -5.35354 | -45.03641 | 2025-09-28 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a0c9c13-05f5-3608-871e-12c4f9e27dc8 | -4.85462 | -45.759 | 2025-09-28 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f7d8f15-2ce9-352c-9936-db6ba7c761e6 | -7.03309 | -44.77655 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| cda515a6-e369-371e-847e-9ffc1d8e782a | -7.74475 | -47.01718 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5a934a1f-8b95-327f-baca-769dfcc2fc70 | -6.90351 | -44.76226 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 16ca33da-07f3-3ae8-ad49-a548fdacc08d | -7.16391 | -45.51115 | 2025-09-28 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9693f768-c788-31ae-a9a0-70b42b8bdc4f | -7.87025 | -44.55699 | 2025-09-28 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41e4546e-af45-3271-b035-cbdff20843d7 | -6.3164 | -43.4702 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 69dd799c-a018-379e-819e-13e0b191764d | -8.28743 | -45.45474 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| deab9f69-c43e-3c33-acac-f5aaf8d0c8f4 | -6.70602 | -44.59803 | 2025-09-28 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 470c521b-27dd-3a34-bfe9-6b057de8234e | -6.70475 | -42.76939 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 80492479-0c48-3c5a-b9c5-2db2f2e67cf2 | -7.5388 | -46.10406 | 2025-09-28 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 29d9cdf4-3fff-3c92-b10a-e7084169498f | -5.35883 | -45.04259 | 2025-09-28 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a19e24aa-2ca2-3d4a-84d6-9b9d3b4bebe2 | -6.42217 | -43.51394 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4ac0fa70-996b-3d4d-adbc-2fc0e574fc29 | -6.27748 | -43.62451 | 2025-09-28 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdf54dcf-0c63-3122-82ed-b0e9f6aceea3 | -7.17197 | -45.50216 | 2025-09-28 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b091b6e1-f385-32dc-883b-d364b23aa6b7 | -4.68551 | -41.95368 | 2025-09-28 03:36:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ebf2cc2c-f707-3ffb-91a5-4ff6cfbd38e4 | -7.86949 | -44.56118 | 2025-09-28 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d7c20f6d-4079-3351-b932-57bf0ade9192 | -5.73266 | -42.83833 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4f649a91-5256-393d-a3fe-70bde58affed | -6.7879 | -44.08976 | 2025-09-28 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0efead7f-8842-3f66-9db9-497fdee240d9 | -6.78116 | -44.08542 | 2025-09-28 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f8863005-e0e4-3ef5-bde5-644bfa3cbbe4 | -6.78179 | -44.04872 | 2025-09-28 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8d0ee4d-21b4-3a9b-abb7-206d7827f494 | -5.81772 | -42.81063 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| d163cc51-bb85-3730-9196-ec931870a166 | -6.11792 | -41.80856 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f5b284d3-9859-3dc0-ab06-50ef53d7b623 | -5.74302 | -42.30582 | 2025-09-28 03:36:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cfe764ae-49df-3b7f-8103-4e2423f09159 | -5.61949 | -43.36792 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 23e02ddc-f0ae-3db6-b3c2-9ef70240be95 | -6.70417 | -42.77261 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3cf2ad5e-a549-3b79-967a-705139b4f8b9 | -5.73545 | -42.83918 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 47d9e51c-9ea1-375c-b808-e28940bc2524 | -5.73626 | -42.84971 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| f63b958d-8ec7-38dd-9411-4410b6b23b6e | -7.92672 | -42.67388 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 91adf68e-ff42-3aa7-829c-3858c29588c2 | -6.77663 | -41.75236 | 2025-09-28 03:36:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2791bba1-5979-38a1-b521-3f0fd85b7f8e | -8.17513 | -43.34752 | 2025-09-28 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 18c85ff7-7185-336f-92cb-03490dead0ca | -6.90275 | -44.76635 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e7d5c6d9-3dc5-31ca-9964-2476dea7df53 | -6.12056 | -43.45498 | 2025-09-28 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5446994e-1b13-38a7-8afc-a23de21bc4ec | -8.6432 | -43.99329 | 2025-09-28 03:36:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5447c6cd-e9ff-3607-b098-47a2e8fd7ba4 | -6.48463 | -44.50829 | 2025-09-28 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9fac9aa-19ef-3f7c-b12c-82b53ac999b2 | -5.94567 | -42.90374 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2a356d19-1e35-37de-b41e-a97c12ee6486 | -6.27011 | -43.63343 | 2025-09-28 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df7fbcf6-8632-3257-88e4-15bede50bf8f | -7.31748 | -45.98846 | 2025-09-28 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae8c9bc3-1017-3bc3-95a8-800568aea8ce | -6.11697 | -41.8142 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4b04c6ac-7c6e-30c1-ad78-548bb8cec985 | -8.29079 | -45.44115 | 2025-09-28 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a9c5692f-ccd9-347f-bff4-9ab48e939332 | -7.8666 | -44.57698 | 2025-09-28 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9db9c40b-c50f-3666-a03f-5aa775968921 | -6.69838 | -44.60626 | 2025-09-28 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ca8b17ee-3807-3dfc-b5c5-17bf90833fbc | -7.79306 | -47.00593 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 51cf22f0-13cc-3af8-8eb8-d269bf3b9d2c | -6.25631 | -42.463 | 2025-09-28 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bbc27f57-4e24-3cea-a763-25735d56d9c2 | -6.58069 | -43.73838 | 2025-09-28 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb31ab51-929f-3d9a-908e-2cc340ed83a0 | -5.81886 | -42.80397 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d2d06178-45ec-36b1-9983-92967d0443e4 | -5.88231 | -43.19603 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 034ab3fc-f18c-3b9e-ab9c-6dec8074ccda | -5.72969 | -42.85579 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8ebe9dd4-1210-3019-8fa8-a106c8850350 | -6.31218 | -43.46181 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c20230ce-42e5-3093-856c-369617dc91bc | -6.11893 | -41.80722 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4ba88498-c379-3ea1-8600-d5d11c13855b | -5.74428 | -42.85175 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 968f62a3-60ad-3c54-8aca-154b4832a063 | -7.70288 | -41.29023 | 2025-09-28 03:36:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README14.md)
