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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c700fd9f-dc12-3ead-a773-c8641b765dfd | -2.74459 | -46.19431 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 684558d2-dfda-3c57-ba87-e13dfa503685 | -3.03334 | -40.10565 | 2024-12-27 04:33:00 | AQUA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 32.1 |
| f9967369-a249-3fee-8866-717a53ab6740 | -3.58126 | -51.05063 | 2024-12-27 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd76ce21-1f48-30f7-9554-8eba490a966e | -4.42593 | -46.55787 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 751a5917-b826-37ee-a626-52444fc94c51 | -4.25608 | -47.58381 | 2024-12-27 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48a277d5-afbd-36e6-b768-74b025146f18 | -4.56369 | -44.12694 | 2024-12-27 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2a8d050-6efa-3cda-9005-28cf133dffbe | -4.3971 | -47.77185 | 2024-12-27 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1793bcf3-3c4f-348f-85f1-0fec5a0c4055 | -5.24497 | -41.39702 | 2024-12-27 04:33:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 927ebbd0-6fb9-394c-88c6-420ada1e098a | -4.52597 | -45.88908 | 2024-12-27 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26476b85-a3f2-34ad-ae93-80287d64294c | -5.64595 | -43.70721 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4999c56d-a8c0-3416-b159-da72e54e8918 | -3.09122 | -53.71868 | 2024-12-27 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cba796b6-1fa3-3b41-971d-b876751e6b3c | -5.31518 | -46.0531 | 2024-12-27 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 416b3f26-b936-377e-a0ef-2db9b766a0a7 | -4.39764 | -47.76841 | 2024-12-27 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dacf1f70-e778-381b-9342-0c21886515e2 | -4.4315 | -46.56592 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a507d881-1771-36d1-abbb-9da9cf8e9331 | -5.87913 | -43.88246 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d32449c0-5032-316d-a47e-5bee74c2e44c | -6.09155 | -43.69885 | 2024-12-27 04:33:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cf52312-2faa-3fb7-8349-6d247c104878 | -4.55571 | -44.13012 | 2024-12-27 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae452a51-c328-3a91-ac11-d4104de4c8a8 | -10.15003 | -42.43652 | 2024-12-27 04:33:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dad2bf78-b247-303e-8e71-dae52135d888 | -4.25278 | -47.5833 | 2024-12-27 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44291732-f98b-3b5a-8a5b-2bf358b1bd71 | -5.90532 | -43.48895 | 2024-12-27 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 42b7dd82-ecad-38b2-8cd7-9bc15b1f44b4 | -5.59583 | -46.53156 | 2024-12-27 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b787a88b-26d2-3c4c-ba8d-551774d30500 | -11.96144 | -41.32801 | 2024-12-27 04:33:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 08e0090c-5b9b-3c0f-9eee-a6d24d6dd022 | -5.77777 | -46.5845 | 2024-12-27 04:33:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c8b331a-f9da-36c8-8ebb-8e5dfe32e262 | -5.65356 | -43.7084 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a20eccf-5859-3d14-b9a4-96e9ae7dc5db | -5.64833 | -43.71719 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4b060fc-9f0f-3438-83d1-706dea8ac023 | -4.40215 | -45.98615 | 2024-12-27 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a17f2823-111b-3e98-b4fb-a7f7f748617d | -5.64363 | -43.71906 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b50b3f00-1919-3d0d-b86f-57fa692b14cd | -5.96503 | -44.28989 | 2024-12-27 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95dcd8b7-7776-32fc-9238-856c5395443c | -2.97421 | -54.6193 | 2024-12-27 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22491cf7-6bd4-31e8-b58f-6e3479687b6e | -5.64186 | -43.70438 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e411d4de-4efc-3524-975c-c0c468f4a5bf | -5.90408 | -43.48717 | 2024-12-27 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b523006-0b3b-3e75-82c4-55591aef28e4 | -5.35975 | -39.34382 | 2024-12-27 04:33:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 49552dce-89a1-3182-8fbe-efe77967283a | -5.40392 | -46.47666 | 2024-12-27 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 502ae3c8-a992-332b-b100-cdc52688ce17 | -3.57756 | -51.05007 | 2024-12-27 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6250841d-ea07-32f0-bb8f-44c76ba78679 | -2.97337 | -54.62437 | 2024-12-27 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0380809d-aa37-3b6d-8695-545b2df562ee | -5.6526 | -43.71091 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c722dc5-dd3d-3589-80a5-17b226bba198 | -5.13522 | -43.23748 | 2024-12-27 04:33:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 56b4994a-b261-3720-b444-7d1b207a9533 | -12.33565 | -43.44431 | 2024-12-27 04:33:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 293df844-bd0b-3ade-b53a-12abbcd24514 | -10.14935 | -42.44245 | 2024-12-27 04:33:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8a3ce52a-2959-3af5-94ef-e67f4ca9199e | -5.22941 | -44.72547 | 2024-12-27 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7404644-3499-3fee-8d30-c666d10af387 | -5.63622 | -43.72006 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a07a6608-e3d0-3130-b6b3-33e19561726e | -5.31501 | -45.45308 | 2024-12-27 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aff9d2ae-9cac-3ec5-bd84-d528d067e9ef | -10.12686 | -36.45783 | 2024-12-27 04:33:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 62ed945c-4041-30e5-9af3-e25b3ae26569 | -4.18983 | -47.98582 | 2024-12-27 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c054d118-c730-3b1f-be1c-76c58cd6d7f0 | -10.43419 | -44.8875 | 2024-12-27 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c042969-f501-3151-b52e-612618a0f6cc | -5.64948 | -43.70557 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7abda778-b1a1-3260-b84c-db962c2c04d0 | -5.90848 | -43.4944 | 2024-12-27 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 219e23c1-4334-30be-8ff9-1b940c08c405 | -5.64215 | -43.70661 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 46ece40a-9cdd-324f-9048-f751b849bf9a | -5.64976 | -43.70781 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1856e89a-0614-38c5-b455-eaebd6a54cd5 | -5.31463 | -46.05674 | 2024-12-27 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e33a376d-7734-396e-9c2b-0ced07dc2cf0 | -11.98809 | -42.2841 | 2024-12-27 04:33:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2cfa80e2-4bd3-3c9c-b198-3392ae5da545 | -5.90988 | -43.48477 | 2024-12-27 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 52bb6923-73c6-34d8-8f75-939d859bd856 | -4.58183 | -46.14208 | 2024-12-27 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d35095e4-ffd5-3e14-8444-625e4315176a | -5.64002 | -43.72065 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26ae3f41-caa7-3f19-83f7-e51ad2939296 | -4.06973 | -47.0789 | 2024-12-27 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fab7b32-66f5-31d2-934e-7063d67afb6e | -6.03164 | -39.76891 | 2024-12-27 04:33:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f5733887-7546-3edb-a607-aff15b8dcc1c | -5.90462 | -43.49377 | 2024-12-27 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d1200dd1-b4dc-3c40-b449-066d3a3c5f4a | -5.63932 | -43.72526 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9559619-f8ab-3cb7-b619-009ace7e5ab8 | -11.01099 | -41.99966 | 2024-12-27 04:33:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a7afee1d-a5b2-38ab-8bea-d431b9ad229e | -5.9254 | -43.77976 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d8f8cb8-2b31-302e-9ed4-f9015bd007f1 | -4.32337 | -46.34033 | 2024-12-27 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea8b20e8-3feb-3544-bb3d-c1b1cb6d073e | -10.14996 | -42.4381 | 2024-12-27 04:33:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 337c9953-2b15-36fc-82e3-ae16ba69f2ca | -4.4215 | -46.56439 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 65aafba1-b70c-3bbb-93fb-4aef695f1c1d | -5.22301 | -41.27208 | 2024-12-27 04:33:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2938b3c2-5e09-3d3c-b3e2-1daeb6b5f9b1 | -5.24556 | -41.39288 | 2024-12-27 04:33:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1a2f6337-a5a3-3f95-8daa-83f40bcc63cb | -5.64073 | -43.71597 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 02c5d522-bf3d-3915-beba-eb94470073f4 | -10.14946 | -42.44088 | 2024-12-27 04:33:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3f852338-d6b9-35d1-9056-6a8574bad5a7 | -4.07643 | -47.10112 | 2024-12-27 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4f03a03-9323-3270-aa43-db0f0cd5d483 | -5.1345 | -43.24233 | 2024-12-27 04:33:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5c38812d-2b59-3614-835c-ca6fa6cfd8db | -5.64904 | -43.71253 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 954fbe8b-35c7-31e9-9ddf-84187f2ee172 | -4.71397 | -43.43353 | 2024-12-27 04:33:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08f03bc4-b54c-33b4-98af-8c9bf8d40f83 | -5.64879 | -43.71031 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ef80b638-2f7a-3dd0-982c-db706360788e | -12.76088 | -38.48293 | 2024-12-27 04:33:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d285a381-51de-3a22-bdcc-ac328a6ec1f5 | -4.42817 | -46.56541 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5f1cac53-e9ae-3486-b789-c8a6fc615915 | -4.55506 | -44.13442 | 2024-12-27 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbce1844-c3dc-3fbf-9250-e8c3361e993e | -4.40272 | -45.98249 | 2024-12-27 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f901b1ce-a448-31bb-897b-13ab49063bad | -5.91059 | -43.47992 | 2024-12-27 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c9180b9-8a83-3801-9bc7-6b8485f93cb0 | -4.25724 | -45.99689 | 2024-12-27 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 82d05e00-499d-3a87-a92b-b047600c4060 | -4.5779 | -46.14518 | 2024-12-27 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9494b44f-1e4a-393d-b254-24d7003ba4ca | -6.87628 | -47.24628 | 2024-12-27 04:33:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3269986f-b0db-3a78-a881-79cfb296a2c9 | -4.42538 | -46.56138 | 2024-12-27 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 53d5e6ee-dc96-35a1-b126-bb737e143586 | -5.371 | -44.84567 | 2024-12-27 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96aed371-8f7e-3de2-a6ce-f8e8016513a8 | -4.5852 | -46.1426 | 2024-12-27 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcac3457-8c6c-36c6-b4a6-ac59aa80af73 | -4.08689 | -47.09922 | 2024-12-27 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce4828a5-27be-356a-86a7-f4ba105d10d6 | -5.63552 | -43.72468 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8492dce-f5ed-354e-a1ca-638c2bd4fb99 | -5.90602 | -43.4841 | 2024-12-27 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| a913fdca-4382-30da-ac4c-fea07fa18ed6 | -5.64382 | -43.72124 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4e6c34a1-96c7-31af-8939-1a72fdc575a6 | -5.47815 | -39.66586 | 2024-12-27 04:33:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0d69fc89-376c-3564-b3b2-2a6c88d440f2 | -4.9814 | -42.59332 | 2024-12-27 04:33:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4697c284-42e5-3373-89ed-4dac4bd3afea | -5.64499 | -43.7097 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 877df000-ad72-3f59-90b9-67a9d1f18997 | -4.39434 | -47.76789 | 2024-12-27 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc9de423-05b5-35ed-9369-b0d98afc62bb | -5.90918 | -43.4896 | 2024-12-27 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 59adfead-1beb-3baa-9a56-9fce2baefc61 | -5.94879 | -44.44753 | 2024-12-27 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 06c3bea6-5389-3aa3-befe-67157216b9ff | -4.7178 | -43.43409 | 2024-12-27 04:33:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf3205c5-1bbb-326f-b9d5-71010f3620f9 | -5.9292 | -43.78037 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6790bd42-7ecf-327e-9343-bf57a8dab38a | -5.92991 | -43.77565 | 2024-12-27 04:33:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc97ccbb-f54d-311c-84b7-d185dadf58e6 | -10.43041 | -44.88694 | 2024-12-27 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92258ca1-171c-391e-83ef-c089306ecfec | -5.21654 | -44.90652 | 2024-12-27 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73c30a02-ebcd-360d-bc77-f687bf738ba3 | -5.90482 | -43.48233 | 2024-12-27 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19f421f8-834b-3eba-8288-d2b3bdad3cf5 | -6.52087 | -46.07859 | 2024-12-27 04:33:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README12.md)
