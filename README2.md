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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fde0b83f-f51b-3f09-972d-f8ed93fd289e | -29.81609 | -51.45601 | 2025-02-10 04:21:00 | NPP-375D | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| a404aa4b-f5d0-3dfb-840d-1726ecdcec9d | -23.98504 | -48.91835 | 2025-02-10 04:21:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a9687af-9065-3e7c-806a-674046fc0c0c | -29.63992 | -55.57794 | 2025-02-10 04:23:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| be6c4e86-9799-38fd-a344-6c7f99708d5a | -29.64115 | -55.5811 | 2025-02-10 04:23:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 8cff6857-c3cf-335d-b35e-c27375225494 | -29.64207 | -55.57663 | 2025-02-10 04:23:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| e2148d21-faaf-36ea-af66-074e14c16892 | -6.53023 | -43.57037 | 2025-02-10 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bafac7aa-0c9f-358e-a2db-4330b8cea639 | -6.98119 | -42.99818 | 2025-02-10 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 79368e1f-a77a-34dd-90ae-9134a63d1e77 | -6.98182 | -42.99371 | 2025-02-10 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 110872c6-ce5f-30c2-a305-a5dfda9d04e2 | -19.7308 | -54.83609 | 2025-02-10 04:40:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f8287b0-caee-3650-8138-dc19d2241f8b | -20.76211 | -46.7682 | 2025-02-10 04:40:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f969efec-5922-3a6f-820b-d60cf448a863 | -19.73424 | -54.83677 | 2025-02-10 04:40:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b33370ec-2618-31d8-849a-772b32aeceb7 | -20.91124 | -56.53372 | 2025-02-10 04:42:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2faf0699-7d7f-3fe7-8ff3-54ce83d40093 | -21.35855 | -48.5739 | 2025-02-10 04:42:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 45cb6510-dda5-3e05-85b1-09d01f6f674a | -23.34017 | -46.77177 | 2025-02-10 04:42:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 05247c2d-8343-3681-9fc6-fd14e54aff82 | -21.47326 | -51.37426 | 2025-02-10 04:42:00 | NOAA-20 | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 74fee569-4785-3293-b65a-09702773c54c | -23.34009 | -46.77294 | 2025-02-10 04:42:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3e22e91e-b205-372b-ab45-adf7015ab134 | -21.49092 | -56.23186 | 2025-02-10 04:42:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 24c320ae-0933-3873-92cd-162266d1db15 | -20.90758 | -56.53304 | 2025-02-10 04:42:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1a2eae4-e819-3131-a2d2-d7e22da1a961 | -23.40473 | -46.55463 | 2025-02-10 04:42:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5ce85563-e24c-311c-bbdb-fcb979d4a611 | -21.47044 | -51.36983 | 2025-02-10 04:42:00 | NOAA-20 | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c6dd7df0-18af-3a81-956d-11d26a3fc0f1 | -21.47383 | -51.37041 | 2025-02-10 04:42:00 | NOAA-20 | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a671b160-d04a-3b35-a588-97671f8da886 | -22.67624 | -42.85306 | 2025-02-10 04:42:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 813832ee-39dd-3e3b-a54b-3735574b64f9 | -20.99446 | -51.79348 | 2025-02-10 04:42:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 19cac6a9-955b-3e6b-b812-01493cbdd941 | -20.56101 | -55.56243 | 2025-02-10 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e3b32b6-2f90-31b0-8526-1241e8f4361b | -29.6407 | -55.57595 | 2025-02-10 04:44:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 7e79b7f5-4602-342c-b5e5-62cbe0a08532 | -29.64007 | -55.57992 | 2025-02-10 04:44:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 98b28250-4fc7-3759-bb35-fad4d08ad855 | -30.33836 | -54.26539 | 2025-02-10 04:44:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| b881e69c-6155-3342-bd4f-413f344e8041 | -26.78379 | -51.2779 | 2025-02-10 04:44:00 | NOAA-20 | MACIEIRA | SANTA CATARINA | Brasil | 4210050 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aff0680c-8928-3431-9539-6569097120ce | -28.58825 | -49.44288 | 2025-02-10 04:44:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b58d31ad-970c-35fe-8aec-2437b2a94784 | -27.79624 | -50.38322 | 2025-02-10 04:44:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ee2db789-803d-394d-a16b-2879c121a8d7 | -16.46412 | -58.16897 | 2025-02-10 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9c4347e9-fdef-3321-b8aa-02a58b2f762e | -20.90792 | -56.53369 | 2025-02-10 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b58cd09c-87bd-3b34-b462-0b2bf8c5bc6d | -20.91334 | -56.53115 | 2025-02-10 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e8ba678-52a9-312d-8ce0-e013d6af3716 | -20.91301 | -56.53451 | 2025-02-10 05:33:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0a58b82-ef18-32c0-891d-f0f781336b26 | -12.05 | -45.12 | 2025-02-10 12:00:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0d16d83-664f-3eb7-a0aa-5fd79a5d51db | -12.05 | -45.07 | 2025-02-10 12:00:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba2ee950-3052-3314-8b93-9afff4d8125f | -8.34979 | -45.18869 | 2025-02-10 12:31:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| ee7dfcf1-a59b-33f3-8dbe-9128be154c61 | -11.68113 | -46.45354 | 2025-02-10 12:31:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 5827f14f-8609-3fec-b6b8-eb9ce2596372 | -11.57205 | -44.85806 | 2025-02-10 12:31:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 5f9a410d-d1ff-3af8-abf0-17e739e90c35 | -11.58147 | -44.85936 | 2025-02-10 12:31:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9fb20462-6032-3a37-a7b0-d921274a155d | -9.17892 | -44.7249 | 2025-02-10 12:31:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3e9c1931-3287-3589-bf24-7ba6bbf722c2 | -9.51591 | -44.74562 | 2025-02-10 12:31:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9fcc92f8-02a0-3992-bf1c-ec865895a706 | -11.68242 | -46.44447 | 2025-02-10 12:31:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2b96cde1-f281-38f0-adf0-55721bc8f2f2 | -8.35109 | -45.17945 | 2025-02-10 12:31:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 887c96fb-d288-3d11-9441-2fb2c6cee25f | -11.58006 | -44.86958 | 2025-02-10 12:31:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 9bc5f28b-8793-3812-a5ce-6c098a2f6e37 | -8.27553 | -42.14153 | 2025-02-10 12:31:00 | TERRA_M-T | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 0a185eed-9fe8-3faa-b210-4f950098b5cc | -11.57065 | -44.86829 | 2025-02-10 12:31:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 4ed9180c-9508-34e0-8869-eb5eda47fc74 | -12.49107 | -43.78908 | 2025-02-10 12:33:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3752179d-95e9-3517-8337-1034ece6e987 | -12.59825 | -45.07381 | 2025-02-10 12:33:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 0edddcd3-a686-383f-8eed-8254dca89d91 | -15.0335 | -43.13796 | 2025-02-10 12:33:00 | TERRA_M-T | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 14.8 |
| efffabcf-9859-37dd-80c6-c600023e0de7 | -12.59962 | -45.06361 | 2025-02-10 12:33:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| df76507d-e215-3961-9667-c2e9946bca12 | -12.44907 | -44.41895 | 2025-02-10 12:33:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| deba6b20-2b3c-3b88-bb93-8c06a3746316 | -21.86956 | -49.73796 | 2025-02-10 12:36:00 | TERRA_M-T | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 99310c36-b3c1-3b57-b787-2f8b7e272730 | -27.1112 | -50.83347 | 2025-02-10 12:38:00 | TERRA_M-T | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 5ab126fc-58cc-3fc4-ab4c-3dc15c497c17 | -22.80007 | -46.28122 | 2025-02-10 12:38:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0bc38e4b-ebe2-3b07-a1ab-13ae9d094ac8 | -22.83514 | -46.32954 | 2025-02-10 12:38:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 5cf66cfc-2a46-3641-936f-3f60a6bc9b1e | -26.18456 | -51.60467 | 2025-02-10 12:38:00 | TERRA_M-T | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f4741ae4-b9fa-3faa-8daa-2a336110a69f | -25.59092 | -51.98597 | 2025-02-10 12:38:00 | TERRA_M-T | CANDÓI | PARANÁ | Brasil | 4104428 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 387f3b62-adb0-393a-b432-23e5cd98a1ba | -23.11682 | -47.00999 | 2025-02-10 12:38:00 | TERRA_M-T | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 3cf21059-e819-390e-a0bd-9d26a8605be7 | -29.89067 | -51.93172 | 2025-02-10 12:40:00 | TERRA_M-T | GENERAL CÂMARA | RIO GRANDE DO SUL | Brasil | 4308805 | 43 | 33 | nan | nan | nan | Pampa | 5.2 |


