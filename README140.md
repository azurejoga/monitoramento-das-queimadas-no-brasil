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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d7d5c93-1c8d-32cf-8132-f46f201f09c5 | -7.69358 | -46.15789 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e59bc2d-7415-3430-8313-9059b67afa10 | -7.69354 | -46.1591 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0291a48-e2af-388e-a9d9-13842d02e4fc | -7.69234 | -46.16757 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ace0535-aeca-3cd8-bed3-425df42b55bf | -7.69206 | -46.16922 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74a9c1d6-baaa-3dae-a203-feabed27aa78 | -7.69194 | -46.17038 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe480509-f192-3333-8458-911c89078796 | -7.68773 | -46.164 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51e646e1-7fe3-3569-8691-e339beb4a2b2 | -7.68733 | -46.16679 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4cecc45-02ef-3ed8-ae57-f1bfdceb3446 | -7.68273 | -46.16317 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cfe46ae2-2b62-37d2-8ba1-2b508d39b10b | -7.68232 | -46.16605 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f31542df-a8a4-3a38-b41e-d2e4815ef59a | -7.33164 | -46.71 | 2024-10-04 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8be59b36-d7c9-338a-932f-11249b41b4b4 | -8.63463 | -46.52032 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddbe6b5b-d3ed-33bb-a469-7be1ad2d25c2 | -8.58903 | -46.51478 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c10fc2b6-f503-33ff-9b68-f391a7b3262d | -8.58822 | -46.52065 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8a0ad0e6-368d-3971-b38d-23cecc00940b | -8.41993 | -46.85248 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a52538e-6df1-36e0-9d10-50c5c5a6d3e3 | -9.02836 | -46.59173 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1793044c-2a31-35bd-ab4e-01707f8bf780 | -9.02758 | -46.59196 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db8554c9-fa88-34a3-872b-a3f1989a043a | -9.02341 | -46.59089 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2d5428f-8821-3b25-ae76-94e74af80ab4 | -8.62968 | -46.51949 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c45cf792-f526-3be4-a88e-4abe93d9140f | -8.59402 | -46.51528 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 502d0f9c-732e-3a0a-859d-404b78259d58 | -8.58325 | -46.52006 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 547f0218-9c21-3e44-a430-7cfa0e628bd7 | -8.58246 | -46.52576 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d2d29a3-7c1d-3131-ab57-52d74872c5a2 | -9.84007 | -46.77464 | 2024-10-04 04:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d705d12a-c41c-325d-9c10-553e5e8273cd | -9.83321 | -46.75047 | 2024-10-04 04:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 84dc87d7-55d8-38f2-a414-be6dce3011a2 | -9.83242 | -46.75636 | 2024-10-04 04:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bdd23b3c-3fde-3a26-9c8d-6b1dfdeba0c8 | -10.7293 | -46.16395 | 2024-10-04 04:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06e43851-3932-352e-a5ea-63bf3689dc8e | -10.72489 | -46.15671 | 2024-10-04 04:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 406dc6a9-40b0-381b-b85c-4b8efd03f752 | -10.72447 | -46.16005 | 2024-10-04 04:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f6f2220-13bf-38da-b65d-3ed2ac9bc207 | -10.85584 | -46.33947 | 2024-10-04 04:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adb67379-38a2-3a60-ade8-5323e5b91783 | -10.85023 | -46.342 | 2024-10-04 04:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d72f9da-2509-377f-ad85-09372c66d3f3 | -10.86103 | -46.34012 | 2024-10-04 04:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aed5b53-7b48-32e2-b271-44a5dd573df5 | -10.85063 | -46.33892 | 2024-10-04 04:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de152607-dfee-3476-b861-17d857ecbade | -10.84542 | -46.33839 | 2024-10-04 04:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbd31c69-f42c-3461-b5e6-89ba44895080 | -10.84022 | -46.33783 | 2024-10-04 04:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a24cef82-f67d-3c0d-8a6c-a15cba257bd3 | -3.3178 | -46.99181 | 2024-10-04 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07cf9d01-4c35-33a2-9fe6-02a12b672a2e | -3.31336 | -46.99118 | 2024-10-04 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f2734e4-2abf-3400-bf58-46df461dac44 | -4.69366 | -46.75373 | 2024-10-04 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fa3b597-ea4e-3001-9e21-46cb1b262f3a | -4.69295 | -46.75845 | 2024-10-04 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebc70d10-670f-32de-8fd6-eb9b51dbf642 | -4.68908 | -46.75289 | 2024-10-04 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d8a6a85-8b08-3df0-b060-8351f512dc55 | -4.34164 | -47.30062 | 2024-10-04 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e86d233e-5e48-302e-a91a-f2dd960479c1 | -4.13276 | -46.71165 | 2024-10-04 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8979225f-8c69-380b-871a-8044f7f33ad6 | -5.60112 | -47.95905 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 348e008f-02d5-3eca-be3d-3db9288a8377 | -5.60051 | -47.96309 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f6e005f-9856-3a8a-8ad4-a7d82bdbbeef | -5.3115 | -47.2702 | 2024-10-04 04:55:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 098cf821-e037-30db-b52c-5aec938a1973 | -5.30766 | -47.26506 | 2024-10-04 04:55:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d08fbe93-f4b2-3e8b-9773-67ebf3d67c82 | -5.29044 | -47.32124 | 2024-10-04 04:55:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6812b71f-7443-3de9-aecf-6bbc8ab5d628 | -5.28596 | -47.32069 | 2024-10-04 04:55:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50b08fd3-c5d8-3d18-be29-1f2972404d96 | -7.39185 | -47.2879 | 2024-10-04 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe664aed-0e59-3744-b293-7b079bc177e6 | -7.38722 | -47.28728 | 2024-10-04 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a13254f-2301-3094-946e-1c1383aa6191 | -7.18391 | -47.8306 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b08587da-ac0a-3050-9979-55ffc1b918e4 | -7.1795 | -47.82974 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4922223c-43b0-34de-9688-84f704b61bdd | -7.17886 | -47.83426 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2e2fdbf-e3f7-36ad-bb0c-06a2a54b1c84 | -7.17822 | -47.83876 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e0a3be3-9135-3aa5-9cc3-0027f0497021 | -7.12 | -47.9034 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00ebc432-06b0-341c-b912-f3a9027eab36 | -7.11936 | -47.90771 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a9c5395-521c-3c65-8628-295061d8ce4e | -7.11607 | -47.86845 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aac3533e-8dab-36c0-99ae-c5bf66f9a30a | -7.11545 | -47.87271 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32c7c180-3675-3830-ae35-fb5c31f55746 | -7.11223 | -47.86381 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0aeebb41-3d36-3244-bd21-82add7a96fb9 | -7.11163 | -47.86798 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 809c6900-6ba4-39b3-badd-88302c3c5001 | -7.10471 | -47.85341 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0125af5a-24f9-339e-9eca-1bfd1bed807c | -7.1041 | -47.85761 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf8d55aa-3dd9-3794-9d8e-d73deab3024e | -7.09967 | -47.85701 | 2024-10-04 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07f6410d-0250-3147-acad-a9a58271770d | -6.93893 | -47.68596 | 2024-10-04 04:55:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35779608-062e-3a28-94c2-ed7afbb5c2b7 | -6.89354 | -47.23695 | 2024-10-04 04:55:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27869e3f-38f0-3651-946f-8641c26a7e2f | -6.88948 | -47.23482 | 2024-10-04 04:55:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 54d41c00-7f29-31eb-8e5e-9cdc439d3268 | -6.88878 | -47.23961 | 2024-10-04 04:55:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d5eecffc-9428-3cf5-bd30-a4b4bd366d37 | -6.72649 | -46.95816 | 2024-10-04 04:55:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a35dd716-3fa8-3935-b7f9-f182a7ef4fd4 | -6.72433 | -46.95525 | 2024-10-04 04:55:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5fbcf64-9742-3817-8188-d2b0a3107ba5 | -6.72182 | -46.95742 | 2024-10-04 04:55:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b030f2fc-c804-3989-94c7-e42314087733 | -6.5164 | -47.82101 | 2024-10-04 04:55:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d933df84-11d4-3221-9c02-d1e6a7ba6311 | -6.51198 | -47.82056 | 2024-10-04 04:55:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e71cc4f8-a5de-3275-8926-c149db97d16c | -8.53696 | -47.16762 | 2024-10-04 04:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| eb692276-6391-3f62-bc42-a61901d1964e | -8.52283 | -47.2329 | 2024-10-04 04:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c887fcc-fe21-372e-9820-849a10b1922d | -8.51947 | -47.23291 | 2024-10-04 04:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9c7b3124-13f9-3081-83b7-95f5b3308dbd | -8.51812 | -47.23222 | 2024-10-04 04:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f8866e77-8268-3824-ba78-0d82173c901b | -8.50934 | -47.30826 | 2024-10-04 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86dadaa4-ab27-36b4-90cb-f6788919a5f5 | -8.50866 | -47.31332 | 2024-10-04 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d0a9781-b632-3d1b-a346-42fe0d873283 | -8.50396 | -47.31272 | 2024-10-04 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1aeb7490-db4f-31f0-b61f-9d13836ef13b | -8.502 | -47.31191 | 2024-10-04 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e82550b-4751-32dc-a90f-fd2b61dcae04 | -8.43887 | -47.10716 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b99a1ce-af84-31fc-8448-b1bfee30569d | -8.43829 | -47.10467 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3383555c-129d-32d8-b950-2d15d7f49434 | -8.43757 | -47.10971 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 824f8e1e-6c33-319b-a0c3-f779634577ca | -8.43684 | -47.1148 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c13f8cd-0fed-3542-94ca-262384593fd6 | -8.42803 | -47.1157 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 75b27ce0-9c5c-3383-85e7-36836fe5a952 | -8.35738 | -47.53493 | 2024-10-04 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fd5551b-9154-3bfb-b717-fe6cb57404ff | -8.89055 | -48.26617 | 2024-10-04 04:55:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d8d49f2-e2ca-3bb9-8710-2c3bca290207 | -8.88993 | -48.27053 | 2024-10-04 04:55:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d392716b-cad5-3665-a29a-ecfe60ba9e57 | -8.82661 | -48.30521 | 2024-10-04 04:55:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45ebda63-ccc7-3777-ace4-5ef44073f47a | -8.58614 | -47.13324 | 2024-10-04 04:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b6a0e186-44cf-3b65-9332-c9c661eddc62 | -8.55728 | -47.64566 | 2024-10-04 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4eb8e27-8dcd-35b4-bd79-0b958309e395 | -8.5114 | -47.31309 | 2024-10-04 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ccf2b0a-03cb-31f8-91ad-bc7a21d08854 | -8.50671 | -47.31247 | 2024-10-04 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76b9c8ee-1ad1-32bf-9b9b-e8cde31f708e | -8.43412 | -47.10641 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b05b5e2-6995-3286-8c6d-f189d78a9f32 | -8.43345 | -47.11143 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53d9decb-d3de-3653-bcad-8df9717237a3 | -8.43283 | -47.10894 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20a7bda7-fcec-3864-a2b1-b2c3acc44e06 | -8.43276 | -47.11652 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5b2da6c-2ff9-37c6-b418-f744197f432f | -8.43212 | -47.11396 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f595908a-349e-366a-84ee-cc14e193b820 | -8.4314 | -47.11903 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3c0fee5a-6bd2-3265-9ef6-e01b19c9fe22 | -8.42666 | -47.11825 | 2024-10-04 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e5e362c-a552-3bab-be46-8398d8a93753 | -8.36217 | -47.53759 | 2024-10-04 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0314f615-195f-3bb3-9855-7ef60e9f21bb | -8.362 | -47.53549 | 2024-10-04 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README141.md)
