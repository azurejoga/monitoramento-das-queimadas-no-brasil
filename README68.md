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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42e2eb86-991f-3fd0-aec7-539cd2adaf6f | -15.8719 | -56.47585 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8a6855b-6a03-31d2-90f4-5eb5b39643c5 | -15.63546 | -50.10656 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9bbd2387-30dc-3bb9-bcea-30ab00c979d4 | -15.6066 | -56.38837 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8bb1d539-440b-3b24-98bd-866d4c905212 | -15.88495 | -56.48178 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e84f4678-f718-306e-bf3f-e15105ae0cf2 | -13.47568 | -57.05883 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a588c48-f535-393e-9146-3e3ce984074b | -11.30761 | -50.57934 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5bac63c1-cb00-3237-aa95-5237577be866 | -15.90369 | -56.21643 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0a531430-fb22-3d4b-a801-08841be4fcc6 | -12.78233 | -46.46024 | 2026-09-01 05:18:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a753b19-f802-374f-8bb7-c25656ed0eb9 | -11.2595 | -50.56808 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c7d073b5-7472-314b-bb78-1f6a9b38382d | -14.70108 | -53.59982 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 362be071-e214-313e-bd93-5a4400cb4d06 | -15.60546 | -56.3959 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27e7f754-a780-3c47-a2ca-2815d04112aa | -11.92306 | -45.09394 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adb82668-70d8-3d09-b48c-74b982739cc6 | -11.93562 | -45.09796 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d6da22a-5a30-3798-8e5a-830c848bd786 | -9.93172 | -60.49035 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cc119b8-1b01-322f-b417-7ccf55f6152a | -11.06647 | -51.5318 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4064eff-cda4-3837-8d07-8a0505ca6a78 | -11.67352 | -47.59412 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a114a6b9-7260-3ffe-b27c-febc735829cb | -15.40391 | -52.72588 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0f060d3-08aa-34ce-9171-c58ace941ca9 | -11.25328 | -50.58057 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2e487a21-1155-3bdb-8bf0-25fb47fa0903 | -15.59992 | -46.58197 | 2026-09-01 05:18:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d68c11ec-8858-3159-9dc4-565a767ceaa8 | -13.47789 | -57.0665 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6b32791-c84c-33f5-8106-19503224af5c | -15.6401 | -56.37454 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50eaa1d4-fa78-3946-9756-916e1909bf11 | -10.51598 | -57.43159 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a83e7417-96f9-3510-a2ff-ce44f42e8430 | -11.18071 | -55.09898 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46c8d50c-21c9-38cc-a378-e373c40feb3a | -14.41142 | -52.49738 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f79f6cd-c6e9-3fe4-806d-c1ca3f1fb5d6 | -11.06532 | -51.52433 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95847f1e-02a9-394f-9366-68648c5bfe08 | -11.26273 | -50.57745 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7e2d2507-2f2b-38c9-8324-741995f9144b | -13.38892 | -51.74539 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 096f690c-ab6c-3bd7-a75d-417b6019a60b | -15.1861 | -46.236 | 2026-09-01 05:18:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b345c42-d1a7-30a2-9b04-6d1e72fadce4 | -15.60886 | -56.39645 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 008a5c13-bbf9-30e2-92cf-36dc22061fc6 | -10.51152 | -57.4381 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45931391-a141-31f3-b166-50ffbddd2354 | -11.66083 | -47.60668 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2e62ba7-f57d-3172-9ab8-ef3a7e8b26d1 | -16.54544 | -49.5709 | 2026-09-01 05:18:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c18a4ad6-4f85-3d4b-956d-b38dbe939aac | -11.47811 | -58.51485 | 2026-09-01 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca952912-78c3-3af2-9ef7-b99e1c0a871a | -14.43999 | -52.50113 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2dd12957-5fe9-33b8-a46f-80e1393508df | -9.06052 | -65.48141 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed29d42e-a10d-3cc7-ae6f-6f91146d4359 | -11.66499 | -47.61757 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 77389026-7829-3eac-bc0c-48d1e8c5f15e | -13.47683 | -57.02978 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 892d1bad-229c-3520-bcb2-99fba7a3bc83 | -11.18926 | -55.11185 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f36fae5-58a6-373d-9244-762407396755 | -15.62476 | -56.38363 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65cf8352-d828-3975-932a-8da6faa26037 | -9.92875 | -60.48515 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16cb9c5e-0ba7-35df-9da5-1a03b5af8516 | -15.62642 | -56.41856 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35ea540f-2d04-3495-99bf-c59f56b3d1ed | -14.38972 | -52.5352 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bee95e5f-f6be-3de4-bf2a-16649cd86700 | -12.24692 | -56.17288 | 2026-09-01 05:18:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c048a095-befd-323d-b575-82136c3bdc88 | -14.50782 | -59.83796 | 2026-09-01 05:18:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3ea02386-b523-322f-8a67-bbdf1fd67848 | -16.47627 | -47.94735 | 2026-09-01 05:18:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1806cb6c-17aa-396c-830a-8c308b86a04e | -14.38874 | -52.54247 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d4869f4-4a1a-3812-80e2-9622e6218d54 | -9.08094 | -65.4886 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f360b105-b253-3e06-bd19-e69d267386d1 | -11.79284 | -47.67419 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d83d4fca-ce23-3209-9361-75e162681191 | -10.74323 | -54.04077 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f919b24b-1deb-372b-b3a4-23f46b4362f1 | -11.4815 | -58.5154 | 2026-09-01 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5ae49da-805a-3fc4-ac2b-04d27206e2ba | -15.6616 | -45.95411 | 2026-09-01 05:18:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf432dba-01d9-3850-a5f2-0e95f845701b | -10.75443 | -54.06337 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 571db87a-23c2-3275-b482-f8fd6bd4b841 | -11.27681 | -50.60609 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53d7389e-3a34-307e-a9de-cbdfa9d0b394 | -8.53923 | -67.15623 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06545a24-58bf-3a09-aeda-4b36b95ea718 | -9.08462 | -65.37961 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 235f4093-0f8f-31a9-abe9-e6a90b093650 | -15.76536 | -56.0973 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| e75c3b31-73cb-3177-a557-fd7343ccc828 | -11.27983 | -50.58432 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9190516-99f3-306d-8834-778d8da1f285 | -9.02335 | -65.44757 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e5631a9-1cd9-33fb-b489-c7a71f1da246 | -9.02713 | -65.39837 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dbcf834-efcf-3942-949a-5f165a64bbab | -10.75679 | -54.07199 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fff0f9e9-58b8-3c22-a0d9-2f5539de64a6 | -11.17327 | -55.10167 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bae1c565-7e7d-38c1-9b52-19e38feb7ae8 | -11.26896 | -50.56497 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3d1310c8-47c1-3a22-9bc2-1a32bf60099c | -15.46105 | -52.79232 | 2026-09-01 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7be63b7-64a2-3c25-bce9-f8e9794c2839 | -11.27279 | -50.56997 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef7f2f64-df90-3027-90ab-0e010bf9e0cb | -11.10734 | -51.54166 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8c56effc-b35a-3266-b0cb-e26e1cfa1a13 | -15.84187 | -47.68656 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c1f5b67-c44a-3488-8953-fb6ffaa9a922 | -14.5866 | -54.11456 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b581159f-60cb-318a-921f-132565fb2ad8 | -14.51096 | -52.2381 | 2026-09-01 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b778754b-b9d5-3bcb-91a2-6e677db948b4 | -10.74731 | -54.0623 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31ec1119-ef76-3570-9057-c2c797d25fe2 | -14.13539 | -52.79903 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d90ba98f-5b65-34ea-904e-7cc22300944a | -15.74555 | -56.41393 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21a93b11-1094-3096-b10f-0a3803a5eaab | -9.31956 | -68.8903 | 2026-09-01 05:18:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3f63f42-e8cd-3409-9053-ac5a97bd00c4 | -13.45771 | -51.8708 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3038415-3852-3e11-9ea0-54102f559db2 | -15.64239 | -50.11094 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b446a46d-6205-36d4-820d-902da9b4c2ed | -9.0286 | -65.44855 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0258ce8c-aab6-33ba-b559-8c35e51762a1 | -15.6513 | -50.09812 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81ce964a-d6c4-3953-8d35-02262fc0e419 | -15.74896 | -56.41447 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b3982cd-48ca-3efb-a693-de8091c2dcbf | -9.59387 | -60.51187 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c6483e1-e1c9-3715-bc79-8cc899f5de00 | -15.48821 | -56.01171 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 224e4988-3a21-3058-9599-c5b4663ce995 | -11.10268 | -51.5448 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| fc280e19-e3de-3587-ae27-ddf82ae770f3 | -15.60078 | -46.57893 | 2026-09-01 05:18:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8511be72-8231-3a40-8759-5df6724dc0da | -15.89348 | -56.42512 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0234e1d5-af34-3a70-8de6-dc2d2587140c | -15.61738 | -56.38628 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01624eb9-c693-3a84-ab19-94c4263cfd40 | -10.74557 | -54.04949 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 803bd2c6-352d-35b0-bc8b-2a2c5b7d7a48 | -14.40578 | -52.47757 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6fa7abc-bbbd-3eb0-a0eb-2e533e941d29 | -11.24982 | -54.00837 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ae74922-2f03-370d-836c-b6c4c79ce7fd | -13.38834 | -51.74952 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2be2fe35-a937-3c3b-aa09-2bcb9a08410b | -14.42268 | -52.50618 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcc31557-1826-3fcd-a8c3-b00bdd20defb | -11.4809 | -58.5191 | 2026-09-01 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03d76c61-cf65-350f-9fce-7050f9485260 | -11.06336 | -51.52367 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0240af1-bfa2-37ac-ba39-80d2414621b1 | -16.04621 | -54.38705 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b164d367-f34c-31ba-984f-6e112020c564 | -15.62874 | -56.38042 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cbd68d4-9a87-358e-8e63-9fde810f9671 | -9.07917 | -65.49828 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2251d77-ab85-3331-acd3-b134119cab5b | -11.52161 | -60.50101 | 2026-09-01 05:18:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b78eb1b9-14bd-37df-8896-40cb22a4550e | -14.27866 | -52.88986 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95fca0d6-c990-3ee8-82ab-10f934187b03 | -15.43398 | -52.68435 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34e3362f-d3ff-3ae2-9124-7f96b8361e02 | -14.66568 | -53.54527 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3871ff6a-0871-3fae-a8b2-2d2f60b50a7b | -14.43948 | -52.50489 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c28b790-c839-36f4-af6e-c3a4e6357556 | -11.23882 | -51.24206 | 2026-09-01 05:18:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04fd971c-a910-339c-8724-62e94c28fa16 | -15.24721 | -53.84338 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README69.md)
