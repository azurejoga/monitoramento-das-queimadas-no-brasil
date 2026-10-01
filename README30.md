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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 128ea336-85c1-3e2e-b99e-57c4ed8c9c7a | -11.62934 | -41.83151 | 2026-10-01 04:14:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 87423eb0-dfeb-3a98-9f3e-f8d8bc77f5fb | -4.29232 | -50.7973 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a1114aeb-7f3b-3ad4-90bc-9b7ee1ab4d24 | -11.45774 | -43.43907 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9d79103-5c6a-3127-a4e5-8994e75394ed | -11.68231 | -43.49998 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0c4f8b1-e42e-3110-8734-d80ea779467f | -4.28164 | -50.78557 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 253.0 |
| deff25a8-8234-39d0-87c6-d9fed81228c3 | -4.30697 | -50.75064 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d1dddf2-a020-3d42-a530-a79cf6a6519d | -8.84652 | -49.70116 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3581bff4-b48f-3455-8d20-c8c1ba9cb0a1 | -9.20693 | -45.80404 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fda81688-3d59-38de-807d-2acbd051596c | -4.28093 | -50.76449 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 316.9 |
| 2f882663-4e4d-35d9-a9c1-a350da298888 | -8.96422 | -44.17886 | 2026-10-01 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e450314-74df-3113-8b46-e41afb261b64 | -11.43872 | -43.42366 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c25e2867-ed4d-3c5c-9d18-7001526fc9a9 | -4.28509 | -50.81477 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 53052dfc-47f2-3674-973d-ad7a5e3818f0 | -11.33043 | -50.97119 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53c2f381-f501-390b-984f-b76542669a13 | -11.41018 | -51.02615 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9916394b-79c9-35a0-ab63-f0cf9c43fda5 | -4.30726 | -50.78496 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 18489795-0f4b-3d3d-9975-ff433b726c36 | -9.06643 | -49.86792 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30f6ec22-90ac-308c-a552-48f8c722ef82 | -4.28314 | -50.7415 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f14dbcf5-b04d-3d47-b948-315788859219 | -8.63269 | -45.29481 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5802747-3ac4-354e-aa08-cf7d9f3678c7 | -4.63826 | -50.61981 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6a1d3a2f-163c-3a66-8a76-6f580711e44d | -7.61249 | -44.55145 | 2026-10-01 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a29c68ae-0488-30ed-bcf3-a44c8b3791fc | -11.43265 | -43.50343 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4754de99-b632-3698-b77d-ef986f383e0c | -11.41774 | -43.42006 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3c06be7-8d88-3e27-9d45-f8831aa88b71 | -5.81008 | -46.21574 | 2026-10-01 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03733c29-2e7a-3d54-8505-b83bee2b38f9 | -11.41338 | -43.40319 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b0935b90-fd6c-31cc-b99a-bd7536a55aa5 | -11.38679 | -43.36691 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ce81c4e-48c2-37c4-96f7-d10db9f0caea | -4.2955 | -50.74356 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7317acf-8b64-3e0a-826f-76acf9b57e22 | -11.51795 | -47.17537 | 2026-10-01 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b325ba3f-95b0-3841-9eca-9202141039a9 | -4.30108 | -50.78387 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| afb875a3-7ab4-3d34-a837-0f5c7f3e796b | -4.29376 | -50.75333 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| de45ce04-0bb0-32b7-994c-e8d5ae654857 | -11.29284 | -50.96885 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0be32eaf-4375-3682-a8ee-408ff74623d0 | -4.28784 | -50.78662 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 253.0 |
| ef4a86c6-703b-34ce-8aaf-bf7dc179ceee | -8.84933 | -50.50866 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25f02489-8f63-3df8-b4d8-f4b58ace540d | -4.28719 | -50.82619 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d738143a-abe7-352b-a75d-21e4c77a70da | -8.38906 | -46.28804 | 2026-10-01 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71fa7433-c80e-3ddd-8934-da2633bffa55 | -4.27112 | -50.82174 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e487a43-c3ba-390f-805f-b12a1edab1dd | -6.08238 | -53.30904 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b15a775-6250-3739-8814-13b8a7c0750c | -4.26779 | -50.82737 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ca367dc-a5e3-3d3f-8669-ddca9f3ddba2 | -10.90952 | -43.84415 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c338b351-ac4a-3b49-893d-2a438cd98abe | -11.25565 | -43.52657 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52c29ac2-20ea-3d20-bba3-0b7c896e8b60 | -5.75007 | -45.15864 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| db697bab-ae63-31eb-9814-e5da7d4dde3d | -8.79348 | -48.00381 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81f0b2df-8edb-3031-9b82-d69ddfad08ce | -5.22313 | -46.02243 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5edc9271-d2a9-3639-ae29-91c356c0a73a | -11.83874 | -44.7486 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e8c48e5-1a37-3f4b-89a4-3c329edfc17b | -11.66312 | -41.84469 | 2026-10-01 04:14:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eac4d3ea-bd52-3acf-b2c8-b4c103eebf2f | -8.79827 | -48.00465 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69f1ba33-84d6-3e3a-8736-dea71e4d54e3 | -8.63667 | -45.29566 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c1c2b78-ebac-3260-a9ad-37987262039b | -4.6277 | -50.60867 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dba61234-3ad5-3758-913a-0b2260c84e5a | -7.84542 | -45.82631 | 2026-10-01 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47e82a20-5984-30e6-a9b3-cbc2677e7c52 | -10.84134 | -48.69341 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5761fa89-4189-309d-b722-6e12bdd11bc2 | -11.39544 | -51.02345 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1129e9f9-0f89-3929-be84-0fed5cbb7932 | -4.27193 | -50.76855 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4ca4bb5e-6bed-352b-88ed-88c7186ee882 | -11.41286 | -51.02313 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11c76c7c-6e09-3150-aac7-45d4579c9ab8 | -7.41398 | -42.61338 | 2026-10-01 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 01e58e6a-8a1a-390c-afac-6aa00c113f53 | -11.19018 | -45.11622 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1cba5b1-01c8-3981-9c6a-773a12b3d2ec | -4.26609 | -50.77677 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 9be1ffff-6c36-3596-958e-b5670c359359 | -4.25604 | -50.78604 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 28e3e821-c644-3599-b77b-402ea37bf9ac | -11.45099 | -43.45809 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ac03800-18a5-3bd3-b589-c38eb7fc3480 | -8.62583 | -45.38352 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9d73438-e422-384f-90a4-9d2c5dda5898 | -4.24627 | -50.74411 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 85cc8843-6dca-3ef6-b50e-2e1f5936f0cc | -4.30167 | -50.74465 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 753d88c4-a8ce-39b4-b0de-011002c3f44b | -10.56201 | -50.04845 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b68e55e6-7f96-3180-8bd7-53db2d3c7edb | -10.50924 | -45.38127 | 2026-10-01 04:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 580683e6-3754-3e45-97c2-f532a733e813 | -4.27906 | -50.80006 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 81ee278b-2132-3f3a-b549-eb1ad20b37fe | -11.11482 | -44.5925 | 2026-10-01 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81d5a35e-a558-3158-be42-8015745d25cb | -7.72091 | -49.5439 | 2026-10-01 04:14:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acda7de2-9432-3e2d-83eb-cca8f6196bae | -11.46979 | -43.45325 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 233432c1-39e7-3a78-90f5-4a3158b944d1 | -10.84969 | -48.70244 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 028f818d-94b3-37d4-8ae9-428a52b8e781 | -11.40462 | -51.02502 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b282ba2-799d-3cc4-8f4b-2cf40b7171f2 | -10.56264 | -50.0451 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a396a26d-6b21-3880-ad03-e18decb4f4e6 | -11.40656 | -43.48683 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e08099da-c15a-3e93-bbc0-568c25dd1a30 | -5.74817 | -45.17004 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8893e184-3ae6-34bb-8def-4cb804141e26 | -5.14482 | -47.60429 | 2026-10-01 04:14:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8668322-eb03-3043-b70d-55102882724d | -4.25082 | -50.75451 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 290935c4-c71d-321a-a4d1-455749340525 | -11.21488 | -45.15485 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e14f9437-ccbb-319f-948e-c37163b3f979 | -8.01711 | -42.89408 | 2026-10-01 04:14:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a9d33e10-8ea7-386e-98ae-ebba63acc467 | -11.46059 | -43.4436 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 35ad34f1-f19a-3242-a881-f8598bab4a62 | -4.26077 | -50.84476 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6c28a1e-c51f-3b97-97ae-83d6353b9c9a | -5.1783 | -46.19246 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c82ef8f2-8e5a-3aa3-b6c5-7030b6904a99 | -11.43807 | -43.42758 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 420a6700-ad9e-3bba-88f6-f969dccb93a7 | -11.44222 | -43.42426 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f6dbe813-e507-30cc-9e6c-6d60bc5e144d | -11.19301 | -45.18971 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2edeb25d-2620-38e2-a78b-6d244123f0f3 | -7.60872 | -44.55286 | 2026-10-01 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a3ce10e-b459-33e4-87da-1ea1b4256f7d | -7.50652 | -45.83405 | 2026-10-01 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fd3c7551-09fd-3b49-9070-60d59b089a5a | -8.13343 | -43.49203 | 2026-10-01 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90dab922-e805-3f84-921e-99f286b07413 | -6.33122 | -51.1265 | 2026-10-01 04:14:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caca2672-1f28-3403-a413-e954c1d88ec6 | -11.68581 | -43.5006 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7089a1e-fedf-3d51-b432-73cbf5ad6ce0 | -11.60439 | -43.53519 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d957865-51f7-3a03-ae24-375c121a4c18 | -8.62021 | -45.36788 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4eb01a9f-006f-352c-8a76-1afd5636101b | -10.56074 | -50.05514 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b0f9be9-d61b-34cd-bdd2-67be57066b2e | -10.76204 | -44.82172 | 2026-10-01 04:14:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c12e71b6-3354-3a96-b390-469382898891 | -8.6136 | -49.46758 | 2026-10-01 04:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6875e4fe-971f-3455-8ae3-7409f7c5061d | -11.46214 | -43.45598 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37148260-ee5f-3aba-b168-be105d5be354 | -8.63146 | -45.32619 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b7297f5-9956-3f37-be6a-19622475e604 | -11.20367 | -45.19643 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e75d42bb-6ea9-3853-a7c3-07194a6b64b7 | -10.56137 | -50.05179 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53a26938-1e42-3078-8474-58ba9f50daed | -8.21441 | -45.48123 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95a4660c-e3c3-3998-9c6b-5476bb1484f5 | -4.28428 | -50.8195 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| afa16e7b-38bd-3c6b-9257-cacf204bb3fc | -11.46629 | -43.45265 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51ba9533-1733-3045-9d17-817725948f68 | -4.25867 | -50.81983 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58630ef6-4fa4-3a6c-a7bb-0592e3a60209 | -10.25004 | -44.58199 | 2026-10-01 04:14:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README31.md)
