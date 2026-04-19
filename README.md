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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50809175-9523-34cc-9c78-cabc5f4834a8 | -17.49986 | -50.76871 | 2026-04-19 00:54:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 718337ef-cee5-3034-9324-33f7b6520b00 | -23.05128 | -50.04212 | 2026-04-19 00:54:00 | TERRA_M-M | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 89.9 |
| 2efc2a0f-c9ae-32a2-a91d-0595f884485a | -16.43254 | -54.91581 | 2026-04-19 00:54:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9318f285-e4d5-3a9c-b8b9-be4819e6c415 | -23.26967 | -55.18993 | 2026-04-19 00:54:00 | TERRA_M-M | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| f103c318-ae28-33c7-98e6-4f877b62ed2a | -23.26826 | -55.18015 | 2026-04-19 00:54:00 | TERRA_M-M | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| b8c76b37-0ffe-34a5-ba8d-d0a6ca46c747 | -17.5009 | -50.77416 | 2026-04-19 00:54:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6cb6c625-ecdc-3880-81e5-cc0bc4317940 | -23.04791 | -50.02351 | 2026-04-19 00:54:00 | TERRA_M-M | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| d56774f8-1f23-39a4-b3c4-5a4aa14e0013 | -19.0997 | -56.06268 | 2026-04-19 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| b2cf65e3-c585-3607-9a66-783d2ee09040 | -14.92426 | -43.44666 | 2026-04-19 03:32:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 09d8f776-0baf-33e0-8ad0-2860e111db59 | -11.02244 | -38.91959 | 2026-04-19 03:32:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ea4dc842-fc56-3ef7-a3f3-6cfe82071809 | -9.7059 | -37.19927 | 2026-04-19 03:32:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dd66bc6c-578b-3a96-b4d5-139e7587d7f1 | -12.43154 | -39.24069 | 2026-04-19 03:32:00 | NOAA-21 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60952cd7-e5bc-3f34-b388-dd390487d264 | -10.26456 | -37.78067 | 2026-04-19 03:32:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e15df194-2a4e-3779-9b91-f24c18d0743c | -10.26396 | -37.7842 | 2026-04-19 03:32:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e60cc4e9-6d42-387c-8e00-2148e8ff89a2 | -12.82118 | -38.41998 | 2026-04-19 03:32:00 | NOAA-21 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dddeac3c-febd-30d3-bcd3-dadedc7ffb11 | -11.02173 | -38.92366 | 2026-04-19 03:32:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cc92ce48-c835-3719-99a3-87029862c571 | -14.91891 | -43.44558 | 2026-04-19 03:32:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6f4769a4-24df-304a-92ac-076b560c9a15 | -10.26595 | -37.78114 | 2026-04-19 03:32:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50a96751-b650-38a1-9307-6fb22fcc11b4 | -12.19146 | -40.49859 | 2026-04-19 03:32:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eedf4339-12e2-3286-81ec-bf6ffddfe260 | -9.70498 | -37.20185 | 2026-04-19 03:32:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6aa1204e-897b-3ca6-94eb-195b6e62154f | -10.66108 | -40.29802 | 2026-04-19 03:32:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bcfec5ec-a8cd-3d9a-96e6-5edbc453e7f2 | -21.37879 | -41.10804 | 2026-04-19 03:34:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0ffd2d89-414a-36a1-b655-093b8677f73a | -15.30206 | -43.07971 | 2026-04-19 03:34:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b6f32ee-b098-395a-a5ab-bb776799cd0f | -21.04065 | -48.5597 | 2026-04-19 03:34:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e3208928-d04d-3c57-8d56-ef1a5963e987 | -21.04167 | -48.55536 | 2026-04-19 03:34:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d5f82de1-0130-37d4-b1a6-eab3bdf3cf67 | -18.07754 | -46.37413 | 2026-04-19 03:34:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 608f1ac2-6db8-3207-88b1-710bb6f48283 | -18.07872 | -46.37423 | 2026-04-19 03:34:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0dfa744-ae53-3986-bd7c-d06d24c84e40 | -21.03532 | -48.55342 | 2026-04-19 03:34:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 553db45b-a7ae-3e36-b344-9730396210da | -15.30271 | -43.07647 | 2026-04-19 03:34:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7ec7f79e-5719-3a28-9f44-3e1c6fb9fe85 | -21.04203 | -48.55387 | 2026-04-19 03:34:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 15a323cb-298b-3366-b92a-137296229b83 | -20.54359 | -42.41479 | 2026-04-19 03:34:00 | NOAA-21 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 144365d8-e10f-3c27-a01e-cc876be2ad5d | -27.12595 | -51.38478 | 2026-04-19 03:36:00 | NOAA-21 | IBICARÉ | SANTA CATARINA | Brasil | 4206801 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3d679501-b436-3aa3-9e4e-8cd5c0a3ce58 | -7.40546 | -43.20169 | 2026-04-19 04:02:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce4d434b-968d-3d77-9894-5d130137762a | -11.02063 | -38.92191 | 2026-04-19 04:04:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0629bd6b-8771-3728-9591-c7be50179a5b | -11.02397 | -38.92244 | 2026-04-19 04:04:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b4aaca69-0d77-3823-8aa6-39a7bbe5e5ec | -12.43109 | -39.24158 | 2026-04-19 04:04:00 | NPP-375D | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 54f0a24f-2542-38ed-a30d-720f44415dd8 | -11.02119 | -38.91837 | 2026-04-19 04:04:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0cd6bae9-e454-3b61-9a58-6713d64d8141 | -14.9247 | -43.44404 | 2026-04-19 04:04:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa9eb06e-9380-3c06-90fd-9f2f3449193b | -15.4219 | -43.05147 | 2026-04-19 04:04:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6953f3c2-614e-34fd-a547-6bf0d26dd57b | -14.92039 | -43.4476 | 2026-04-19 04:04:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 98fda641-0006-364b-a2b0-ac0a97616e8f | -9.14709 | -40.16483 | 2026-04-19 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 112474ef-5794-3af9-9bc7-971bbe31687c | -10.26295 | -37.78111 | 2026-04-19 04:04:00 | NPP-375D | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 21f0a8a5-a159-39bb-99eb-a5847d23ca1a | -14.92828 | -43.44469 | 2026-04-19 04:04:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3ee3c404-a915-32b0-813e-e148e4aaa58e | -10.47734 | -37.42923 | 2026-04-19 04:04:00 | NPP-375D | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e2faf80-b33a-3d71-9cf4-237cc7d2fc82 | -20.32662 | -47.73303 | 2026-04-19 04:06:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d0baaa9-83e2-3fea-b6d4-a9b107ade910 | -15.7622 | -47.77843 | 2026-04-19 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34b0322d-d4c3-33f7-9517-ed43756cc99d | -17.49947 | -50.76096 | 2026-04-19 04:06:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7151703a-b813-3118-88a6-6dbaacb4b2c2 | -17.50483 | -50.7621 | 2026-04-19 04:06:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7569ede-5759-3e54-b879-40d7e9b3d098 | -18.07764 | -46.37138 | 2026-04-19 04:06:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfbcf180-80d4-3899-8c91-0d9439dd2eb0 | -18.64353 | -45.03048 | 2026-04-19 04:06:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 244ea0ad-7345-3968-b4f5-066d5534e594 | -17.50411 | -50.7655 | 2026-04-19 04:06:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab6cdd3c-718c-3c6b-8ee5-5440dff0d140 | -18.07696 | -46.37506 | 2026-04-19 04:06:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a6f2e21-1a09-3ede-9f9e-bade075c90a8 | -17.5102 | -50.76318 | 2026-04-19 04:06:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c879940-cbc8-3d33-b29e-1ce028101e2a | -20.04087 | -40.74696 | 2026-04-19 04:06:00 | NPP-375D | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8b275083-225e-3dc6-b6bf-22d4e404d99d | -20.54233 | -42.41524 | 2026-04-19 04:06:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c8988a7-3c20-3e2a-987a-1e5cf45d3ea7 | -21.03964 | -48.55728 | 2026-04-19 04:06:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| db02e009-f539-359d-9199-fecb2c44bcd6 | -18.72606 | -40.02032 | 2026-04-19 04:06:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8f2d3470-f3f9-38b8-a9e0-09fd76bd31d4 | -18.22019 | -45.05512 | 2026-04-19 04:06:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd5452ba-3304-3ebd-981c-8d4c96b9e333 | -21.0353 | -48.55625 | 2026-04-19 04:06:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8104eb54-76a0-3295-b698-fc731ad0ff05 | -25.1739 | -49.40059 | 2026-04-19 04:08:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2b4e43d9-7b7f-35a8-b579-a4a3ff0953da | -23.78721 | -52.24488 | 2026-04-19 04:08:00 | NPP-375D | ENGENHEIRO BELTRÃO | PARANÁ | Brasil | 4107504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e1106821-6565-370d-ba7e-0ee61cdc5bae | -25.17479 | -49.39628 | 2026-04-19 04:08:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c2edf1a9-5cb2-36f1-a891-ac89548319d0 | -25.09395 | -49.34606 | 2026-04-19 04:08:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3bc35cfe-68af-376c-a577-0715240d67ff | -23.27276 | -55.18768 | 2026-04-19 04:08:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 754bb15d-85d3-30c0-8f2c-cfe4bab3469d | -23.78185 | -52.24384 | 2026-04-19 04:08:00 | NPP-375D | ENGENHEIRO BELTRÃO | PARANÁ | Brasil | 4107504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c56a4ac9-171b-3b1b-baee-7958d42b71bb | -23.787 | -52.24519 | 2026-04-19 04:08:00 | NPP-375D | ENGENHEIRO BELTRÃO | PARANÁ | Brasil | 4107504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 039a6f95-a68e-3b06-a422-2291c8be7695 | -23.64801 | -48.00155 | 2026-04-19 04:08:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac8342fd-6156-3804-9308-b1a0c8d089d1 | -28.64198 | -49.36914 | 2026-04-19 04:08:00 | NPP-375D | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fabe1099-a0a7-363c-9c78-5a27d5904236 | -23.26665 | -55.18572 | 2026-04-19 04:08:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4ef53484-2bab-30e8-b712-8d0d71e73b1f | -25.08554 | -50.91718 | 2026-04-19 04:08:00 | NPP-375D | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ebc648db-e5b2-3343-8c09-5ca55362c527 | -10.26253 | -37.78138 | 2026-04-19 04:21:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 650cea8c-cd91-3766-9376-ebbcba7bfa41 | -5.35063 | -45.11655 | 2026-04-19 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08c47a75-9132-3f23-a901-4d141f59db24 | -7.40423 | -43.2036 | 2026-04-19 04:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cdc350e2-66b5-361a-8ec3-6e2139a2d92e | -14.92047 | -43.4474 | 2026-04-19 04:23:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c334097-3a8f-3dcb-a81f-6fa631eb6c21 | -13.53861 | -49.91459 | 2026-04-19 04:23:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1359b149-64ae-3793-80c1-9a502a978c7e | -14.33719 | -46.86503 | 2026-04-19 04:23:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c962a702-9ff6-34c1-bfc0-0dce875a5647 | -15.30154 | -43.07763 | 2026-04-19 04:23:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5db7afb6-dc20-3509-812a-56dadfbcbf71 | -13.68168 | -44.29257 | 2026-04-19 04:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fbcef779-af54-3d30-8c6b-9e36f640379a | -15.42073 | -43.0519 | 2026-04-19 04:23:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3e2de029-6d15-3472-9547-38c6c492cd1d | -14.92831 | -43.44423 | 2026-04-19 04:23:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.3 |
| f4917b48-b0d6-3d56-867a-5fe9b581e7a3 | -11.02031 | -38.92142 | 2026-04-19 04:23:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a0952259-09ac-3388-bac4-915d5a5d3c42 | -14.9247 | -43.44368 | 2026-04-19 04:23:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7dec860-7d19-3b0a-92e9-ef06ea3103e0 | -19.09998 | -56.05694 | 2026-04-19 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c5d36a0e-a92f-359a-b52d-a612b4a83b33 | -17.49933 | -50.76348 | 2026-04-19 04:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bd4629a-69e8-31fd-aea8-54d413881926 | -20.62903 | -51.70232 | 2026-04-19 04:25:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fc87034-50e5-3cce-9441-2866468b3750 | -19.3942 | -53.35097 | 2026-04-19 04:25:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bda0466-6e07-3486-b8e5-f15cc12a693a | -18.07665 | -46.37534 | 2026-04-19 04:25:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3882dcb5-b718-308f-9d43-88b4e96c12ab | -17.50698 | -50.76338 | 2026-04-19 04:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3f18729-12e2-3a8b-95ba-30de7130d795 | -17.5037 | -50.75989 | 2026-04-19 04:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e07ca42-1d58-3145-9ba0-e34c09bcf607 | -20.62456 | -51.70608 | 2026-04-19 04:25:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c1c17ee-c172-3dd0-b4fc-f77af3c60078 | -17.50734 | -50.76055 | 2026-04-19 04:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0e2ff6b-e08b-31c0-bdf4-a235411a2da6 | -21.03769 | -48.55645 | 2026-04-19 04:25:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6456ed77-4c1b-3cbd-bada-d8592255b989 | -19.09878 | -56.06266 | 2026-04-19 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 50c527be-af2b-371d-9f92-6b75b223d063 | -17.16754 | -46.83489 | 2026-04-19 04:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d151575-b24e-3eda-a8b6-4fe4fdf8c1bc | -20.32636 | -47.73232 | 2026-04-19 04:25:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84fb05f7-9514-34da-9219-7b81c4cb1f21 | -18.64175 | -45.02955 | 2026-04-19 04:25:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1eabb56-169e-3b22-b177-465640f30296 | -18.07722 | -46.37165 | 2026-04-19 04:25:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20937312-6fd6-34ca-a351-290f15909b9b | -19.09708 | -56.0603 | 2026-04-19 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1949d0c1-8793-3ec3-900f-399cac24e2eb | -17.57693 | -46.97363 | 2026-04-19 04:25:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abe5e2a0-65d5-331c-bbdf-84dcd00a3b5d | -21.03828 | -48.55275 | 2026-04-19 04:25:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |


[Clique aqui para ver as próximas entradas](README2.md)
