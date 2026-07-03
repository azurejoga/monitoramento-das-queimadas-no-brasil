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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d78db106-58f1-3665-a721-31c4e62655f1 | -3.6725 | -48.9776 | 2026-07-03 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 348550a4-5ac0-3cac-b804-d5a7786e0cc7 | -7.91704 | -47.82328 | 2026-07-03 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b6a5a8f-be79-3035-b60a-4f434be3df17 | -5.79119 | -45.06698 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 91ff7d48-9f54-36c1-9eba-0a30f46a2bc1 | -5.81234 | -45.04365 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e704049b-692c-3bd2-8868-d5a08a408ff7 | -6.93461 | -43.72321 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcca6ecd-bf15-3e52-8822-686294c8c73f | -3.41557 | -41.70283 | 2026-07-03 05:04:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b41a95fb-a6ae-37e1-a6ed-161ef046d767 | -8.38445 | -48.22898 | 2026-07-03 05:04:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46e82596-9ede-3db1-8941-0eea79fa3f27 | -5.80421 | -43.79603 | 2026-07-03 05:04:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce99092d-bd1a-321f-b191-1153c445a057 | -2.51504 | -57.74107 | 2026-07-03 05:04:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90b9c2ed-4c8c-3be7-93fc-18bd9db92d1e | -5.79112 | -45.06476 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ea0de7db-53c6-38e6-a8f5-0c970090d044 | -5.79238 | -45.05851 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e1a1cec4-14ea-3310-b42e-d03d497ba6db | -4.00906 | -48.06408 | 2026-07-03 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5f6d5c42-1c7c-3862-87f2-bc79beb21266 | -5.46906 | -45.42287 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1512f0dc-2216-35df-8f08-202223f9bfbb | -1.78014 | -55.50433 | 2026-07-03 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5591dbe3-5315-3de3-af18-1113395d4679 | -5.79396 | -45.04349 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7897e9ca-a789-3a14-87d2-dabf16569a44 | -5.79451 | -45.03935 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eadad9ce-3ee5-3c69-a8ed-8d49a8127602 | -5.79299 | -45.0542 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 524f59a4-2516-3cc0-994c-36d53638ceba | -3.51557 | -48.03839 | 2026-07-03 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2566289d-c9bb-3e38-adeb-19f936a805bd | -3.41467 | -41.70688 | 2026-07-03 05:04:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 5304b57e-d803-3852-9352-9d0def191b39 | -7.7041 | -55.37625 | 2026-07-03 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c2e94bd-d3d9-3e0f-8ac4-0e36143d0f03 | -3.51096 | -48.03773 | 2026-07-03 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f5ad4771-c764-3010-85f2-db0abce11ed6 | -6.92303 | -43.72102 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 785e5f85-9dee-39d2-87bb-a4d56f0611f5 | -6.92947 | -43.72193 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fd11db21-e10a-3ec4-bed4-9ce28daab69e | -5.79701 | -45.06787 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0aa92c31-bbe9-396e-bd43-65ba10eae004 | -6.92173 | -43.72144 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ea303b91-cbda-352e-a17f-00aa3fd4e295 | -6.91529 | -43.72053 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 69e8888a-2502-3d0f-9627-a6510455f9b4 | -5.80036 | -45.0401 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02a525a2-228f-3cf2-81c1-5d3a7491d2cc | -3.87203 | -42.9779 | 2026-07-03 05:04:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 705b5474-ab0c-3b1b-be4f-80e61c95d29f | -6.92888 | -43.71699 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9be5c22d-129a-37b0-867a-9ddb2045ba09 | -3.42254 | -41.70131 | 2026-07-03 05:04:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ce98169e-5a43-3035-b8c4-8fed5071fee0 | -3.42252 | -41.70377 | 2026-07-03 05:04:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 982c4ac5-69fc-34fd-9c34-6d139f4332b6 | -6.41539 | -51.23106 | 2026-07-03 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3681f16c-4180-3148-809d-1fcc44fd6660 | -7.61439 | -49.54338 | 2026-07-03 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2ddab96-0266-340e-9a8d-076b59aca3e7 | -6.87098 | -56.57094 | 2026-07-03 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a20bda4e-7cf0-3e23-b964-b74befd55a27 | -8.38518 | -48.22349 | 2026-07-03 05:04:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56701c55-caf0-363e-865a-03b32fdbfd5c | -4.00974 | -48.05936 | 2026-07-03 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1df8834b-9bf7-3546-a406-191a2d3acb08 | -5.79329 | -43.6361 | 2026-07-03 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27128266-8c5c-30b7-912b-6662af821019 | -4.29284 | -48.6516 | 2026-07-03 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a8616e3-6126-3ebe-a7c0-6283ecbaaa6b | -4.35125 | -47.76648 | 2026-07-03 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a5a77cb9-6b41-3bec-a75a-971af596d523 | -7.64014 | -50.02824 | 2026-07-03 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 914790fa-937b-36af-8109-0b04fa05dadb | -6.15294 | -52.0799 | 2026-07-03 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92efa20c-64c7-3dbc-97ef-248453f21a7f | -4.88519 | -48.90695 | 2026-07-03 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6789a761-9195-3558-b2c7-e6febceae448 | -5.80676 | -45.03674 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7b8ac429-b637-3d60-9d1d-d4c149c37c60 | -5.79419 | -45.0457 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 07a3265b-604c-359c-b94d-883451a2f59d | -5.78714 | -45.05347 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05bb7ce6-540b-3231-b19a-0f13e4c549c2 | -4.01365 | -48.06504 | 2026-07-03 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| cd589f19-0cba-3cc4-b7d7-27b6083b8e1f | -7.64441 | -50.02886 | 2026-07-03 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb118f99-77b5-3e8a-bdc9-c9b5de6383d9 | -5.80353 | -43.80106 | 2026-07-03 05:04:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d86e8483-10f6-3cf4-a8b5-fe1738c2bc3e | -7.91857 | -48.25128 | 2026-07-03 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e1f1509-d6b8-33b6-a53f-47219cd5ca77 | -5.81152 | -45.04559 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| de67e333-5ffa-3c6d-b7ef-ce3ca1863903 | -5.73123 | -51.71607 | 2026-07-03 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80a53930-3d23-312a-bd42-18f05b820960 | -7.27955 | -44.50386 | 2026-07-03 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b21513b7-8046-39fd-beb1-9f4b4fd8dc76 | -6.42737 | -55.79812 | 2026-07-03 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4a9c736-fead-30fe-8ea7-0be5c0f61488 | -4.88077 | -48.90626 | 2026-07-03 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84918fff-ac93-3066-9601-f495241176bc | -3.87279 | -42.97246 | 2026-07-03 05:04:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b237953-edb0-3da2-8454-9709f2f066be | -5.81291 | -45.03961 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 59e670a3-ddc2-3e90-9cf7-136f20df4e21 | -3.41461 | -41.70932 | 2026-07-03 05:04:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| a1691e2d-b6c9-3a89-a3b4-27410e3cbcc5 | -4.28839 | -48.65084 | 2026-07-03 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85973d03-878f-32c9-8c21-96e4507a82a6 | -5.79056 | -45.06894 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c1237e28-8397-3de2-85f4-9781f8b3cda9 | -5.4696 | -45.41901 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d7508f9-bcad-3274-bdc1-5715df509ed8 | -7.92262 | -48.24799 | 2026-07-03 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa3baeba-3891-34ac-8247-8ca18b4819d9 | -3.42162 | -41.70787 | 2026-07-03 05:04:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f5eb485d-19ec-39eb-ada1-1206d84e7d73 | -5.80706 | -45.03891 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ea7fbb42-2785-3d0e-b1b6-34cf7a65b8de | -5.80567 | -45.04489 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e84ef39b-6b0f-3714-9abd-ce519bcce33f | -7.01685 | -45.43037 | 2026-07-03 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a445e3e0-cf92-3edc-b645-1cc763a356d4 | -5.79981 | -45.04419 | 2026-07-03 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 86a56de7-7c9b-3a09-8db1-8c731046bc4d | -7.92189 | -48.25349 | 2026-07-03 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f7696bc-7cae-3d16-b032-d4fffd8c1fa0 | -6.92746 | -43.72762 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0deaa77e-1ee4-381d-b8c8-03339784f2d7 | -3.4207 | -41.71434 | 2026-07-03 05:04:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f9ff7500-143d-3b21-bed3-3748b3bfa982 | -6.14929 | -52.07913 | 2026-07-03 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b6e7b77-8a00-3213-84e1-60f754d1229e | -7.01738 | -45.42626 | 2026-07-03 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19a1f7d5-85f0-3b50-be1a-a409c578efdb | -6.93016 | -43.71657 | 2026-07-03 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2c90866a-3ada-3c56-a0fa-a018ca6cb78e | -10.30246 | -57.12596 | 2026-07-03 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b9888b7-384c-337c-886b-5c4764b45728 | -11.35083 | -55.42334 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a535cc7-6bb3-3b48-94f3-c7d3f8358324 | -10.5092 | -50.31609 | 2026-07-03 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a98a3af0-6954-31f0-b10f-13346ffc1261 | -11.73897 | -57.81218 | 2026-07-03 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fdf7f99-1165-38c4-9732-4551bc789ba2 | -12.51449 | -48.26485 | 2026-07-03 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d802537-ab71-355a-ace1-ab18f6759a6b | -12.17743 | -57.1285 | 2026-07-03 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c873ce7-a3d3-3577-b881-442d3b5e3213 | -12.75391 | -44.53431 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| c7b92d27-82b4-3009-abea-1cf21c0282de | -11.29336 | -48.93276 | 2026-07-03 05:06:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7655dc5c-f8b8-3f5f-9d4a-b7c900267cbf | -10.90258 | -56.85723 | 2026-07-03 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c25d7cc4-803b-31cd-bf50-6453985a553b | -12.7791 | -59.88187 | 2026-07-03 05:06:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6f2d5d35-46cd-3170-a397-45f5005783a9 | -11.79613 | -56.99837 | 2026-07-03 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ff91c1f-aa1d-3451-b261-ef3bf44cb527 | -12.43246 | -58.41344 | 2026-07-03 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b201a21-070a-313d-93c1-3be2ca0c80e0 | -10.93986 | -43.05285 | 2026-07-03 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 8657d3b5-4977-3efc-a797-3dd7797abcca | -12.74668 | -44.53927 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ddeddba0-2ea5-3aff-97d8-5a54b6f79e96 | -10.94963 | -43.04813 | 2026-07-03 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| d9b9d526-5c92-39bd-9ad5-7d0643a7a2d4 | -11.63009 | -50.36221 | 2026-07-03 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 863bd0cc-48c3-37fa-9f5e-c932bc1941d7 | -11.29822 | -48.93349 | 2026-07-03 05:06:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1465b11d-15e6-3804-8382-f4d6717f8771 | -9.75886 | -47.87804 | 2026-07-03 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c0d59a5-0cf1-330f-93a6-6d694e6ffc72 | -11.4174 | -56.06079 | 2026-07-03 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec23a95f-e6c7-3cc1-b160-d917c42f7e80 | -11.31646 | -54.4741 | 2026-07-03 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9412c816-f7f2-3411-9971-da94362d1817 | -11.35473 | -55.42024 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08b0a9d8-2236-3293-b6ed-852378b115bf | -12.74575 | -44.53772 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 3e33b01d-d80c-3329-84b0-06431d40affe | -10.89983 | -56.85322 | 2026-07-03 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dc07486-1114-3cdb-a663-fab21679f62f | -11.50083 | -54.50418 | 2026-07-03 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36bccb0e-973b-3b27-b7d2-633e9d76f313 | -11.42017 | -56.06486 | 2026-07-03 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48af55fb-9816-35eb-828b-53a351c7abf0 | -11.6449 | -50.38377 | 2026-07-03 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d76b348-628b-3d0e-9976-9dadce54a127 | -12.75354 | -44.52699 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0b863956-11f3-3bc8-beee-cc314738ed34 | -11.85898 | -48.24657 | 2026-07-03 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README16.md)
