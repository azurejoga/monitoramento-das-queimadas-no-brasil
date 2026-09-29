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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0679e74f-8489-3e68-9146-cd2f0d05c490 | -15.83191 | -42.55842 | 2026-09-29 11:25:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| a5ade766-10e8-3375-9fce-5f8d72f3f0d0 | -12.68848 | -45.00732 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8bc68bcf-198d-353c-afba-2c87af09b2c5 | -14.11258 | -46.28716 | 2026-09-29 11:25:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 46.3 |
| bbed0f8d-7244-36e8-8a47-bbc7b8b63087 | -15.24636 | -43.26944 | 2026-09-29 11:25:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 18.3 |
| c2d9c888-adda-31b0-887a-ab38875b5abc | -15.38726 | -47.91906 | 2026-09-29 11:25:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ba11d462-f557-3599-820c-18f3dab0b65f | -12.68704 | -45.0169 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6afb02d1-4fb0-32ee-9f44-e586008d4a56 | -15.97116 | -41.65899 | 2026-09-29 11:25:00 | TERRA_M-M | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| b666901d-c9b1-36d1-8af7-e945d81a1f39 | -15.1782 | -46.12781 | 2026-09-29 11:25:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| eb8850ef-dac1-3c76-accf-c13eb8864c83 | -13.378 | -44.02494 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e32ac362-be80-35de-87aa-7c130a82bd47 | -13.66014 | -42.07532 | 2026-09-29 11:25:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| ceae13b9-16f1-37df-829f-6f959d49229c | -16.0583 | -43.26314 | 2026-09-29 11:25:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 87a2f09d-e072-302c-9c2d-d39e18c8834c | -12.00209 | -50.92611 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 38.5 |
| e1073040-043c-311a-b64b-7e3416d28ab8 | -19.23363 | -46.43535 | 2026-09-29 11:28:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 28.7 |
| aab9cb6c-4fff-3bc7-b1f8-17a82670fac9 | -18.41291 | -46.05915 | 2026-09-29 11:28:00 | TERRA_M-M | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 18875fa6-b372-3f82-941a-8e75561d7d12 | -19.23219 | -47.23407 | 2026-09-29 11:28:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 22.6 |
| a95a58bc-a2d4-358b-8195-ae0732efc3f0 | -21.24347 | -44.32686 | 2026-09-29 11:28:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| ed350efe-5a8a-31f0-9ed7-56c2f6f14edd | -20.34584 | -42.3392 | 2026-09-29 11:28:00 | TERRA_M-M | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 35e8266a-7433-3884-9fca-ea5e69c2b2ba | -20.5413 | -44.21629 | 2026-09-29 11:28:00 | TERRA_M-M | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| 134431bb-6431-3708-a69d-3cac515f0880 | -18.88469 | -43.80291 | 2026-09-29 11:28:00 | TERRA_M-M | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8cd69354-4d99-36d9-9066-35dcdee7f44d | -18.93182 | -47.19696 | 2026-09-29 11:28:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 57.6 |
| ba8ee9ad-d740-3259-a5e5-1afef26839ec | -19.53531 | -42.93047 | 2026-09-29 11:28:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 0e034f2b-1ab7-37b5-8ea9-985d0c50b3df | -17.02394 | -45.90171 | 2026-09-29 11:28:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b1ee6e21-5cf3-3104-86ee-095aea0ec171 | -19.24122 | -46.44655 | 2026-09-29 11:28:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 489678e4-70bd-348f-a204-c9c5e25d25a4 | -17.5037 | -45.47199 | 2026-09-29 11:28:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 219.3 |
| 0a8725cb-5a87-3aaa-8faa-cf5159226ed7 | -20.5426 | -44.20671 | 2026-09-29 11:28:00 | TERRA_M-M | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 1957d99b-005c-32e0-b696-0ab7eed92279 | -19.54456 | -42.93174 | 2026-09-29 11:28:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| bec0d228-3fb8-3ac6-80b9-b1a1d8784665 | -17.29597 | -42.4795 | 2026-09-29 11:28:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 680de390-00d9-3d1c-acf6-efe36324187c | -19.23215 | -46.44511 | 2026-09-29 11:28:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 8367bdf2-41ba-3f3c-8102-8cf7ec9671a5 | -18.09997 | -44.54453 | 2026-09-29 11:28:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83b7ea82-6881-3f0a-9f96-834c6e05a870 | -16.0919 | -49.72858 | 2026-09-29 11:28:00 | TERRA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 38e8e07d-dc2d-31cd-a030-583903178d12 | -19.05844 | -44.66822 | 2026-09-29 11:28:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eed2feed-33fd-3b89-a46e-ca8a6228b980 | -18.93347 | -47.18642 | 2026-09-29 11:28:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 30d91b32-b0d3-3a86-8b43-343085586050 | -20.16278 | -42.33506 | 2026-09-29 11:28:00 | TERRA_M-M | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 8a5d5e67-a6b6-3f48-918b-280695863962 | -21.22282 | -45.13478 | 2026-09-29 11:28:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 065a80f7-8e64-3cf3-9d1d-cbefa270a492 | -19.33913 | -46.70977 | 2026-09-29 11:28:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0e639ffb-7b7a-3923-9866-e6884d4f666a | -19.24269 | -46.43683 | 2026-09-29 11:28:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c4bebd00-89c5-315f-972a-cd45317e90a0 | -18.10062 | -44.39746 | 2026-09-29 11:28:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| a44f754d-2614-3737-b69b-98ab8d2cf32c | -19.33759 | -46.71975 | 2026-09-29 11:28:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 31.6 |
| f13d1753-1ef3-306d-97f7-c769930f8970 | -17.5051 | -45.46261 | 2026-09-29 11:28:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 69.9 |
| d6b2f877-d5a9-315f-990c-dd9b06d950fc | -20.34727 | -42.32784 | 2026-09-29 11:28:00 | TERRA_M-M | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 9b35a849-c86f-3cc8-b9fb-ffa622eaac6e | -16.98833 | -41.94671 | 2026-09-29 11:28:00 | TERRA_M-M | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f18d7439-eddf-39fb-81d9-12390a93623e | -11.4307 | -43.4358 | 2026-09-29 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6f2fca41-b214-389b-98b3-64cf2180cd20 | -9.0463 | -45.0083 | 2026-09-29 11:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| d0dd16cc-3908-3b63-bc6d-b11c8aaf2633 | -11.4302 | -43.4596 | 2026-09-29 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| c213b3b0-acef-30c3-8e85-6da8d18c9bad | -8.9823 | -44.1633 | 2026-09-29 11:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 5f6061fe-bdf8-33ea-8f94-4f87c2effb59 | -11.1907 | -45.1274 | 2026-09-29 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f68b1b1e-3476-349c-befd-b82966ea61be | -10.3707 | -61.2513 | 2026-09-29 11:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| bbc9d339-c809-3be1-b85d-67d310c6e1a5 | -12.761 | -47.2881 | 2026-09-29 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| cb86c301-fddf-30aa-b1f7-eaa79e6e7ada | -11.1771 | -44.8064 | 2026-09-29 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 479308cb-9c4d-3f49-b03c-4e9da11cd403 | -12.7421 | -47.2684 | 2026-09-29 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5b209faa-eaaa-3cae-9250-a9b3e5767816 | -11.1775 | -44.7832 | 2026-09-29 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 896a78c6-37ae-3ad8-a7d9-8e584ec6e308 | -12.7421 | -47.2684 | 2026-09-29 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 76438751-4c5b-3c9e-8533-3b4a411e45a8 | -12.7036 | -47.274 | 2026-09-29 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 4c038453-c5bd-36b5-b583-6eb65204bab8 | -8.9633 | -44.1655 | 2026-09-29 11:40:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| d2ac84d4-f6b7-38c7-8e85-c4a9ca925a3d | -12.012 | -50.9891 | 2026-09-29 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 581deb93-f4ec-3456-ac91-5de0b8e5b717 | -11.1771 | -44.8064 | 2026-09-29 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| c0d33b5c-4cd4-34e2-8544-4de97a372374 | -12.0311 | -50.9869 | 2026-09-29 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 177.5 |
| c795aa9b-f563-3233-a3b7-1b2dd26da25d | -12.7614 | -47.2656 | 2026-09-29 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d1834c0c-7e3c-328c-8725-b40a9c20b541 | -11.1907 | -45.1274 | 2026-09-29 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 1893bd0f-d6aa-32e4-9bfa-8cbc0dc6a0a1 | -11.1775 | -44.7832 | 2026-09-29 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 60220c16-da79-31fb-b1d9-2f28e1988ffd | -12.7417 | -47.2909 | 2026-09-29 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4e54e703-89ea-3353-9fc0-fb937c17a590 | -12.761 | -47.2881 | 2026-09-29 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| fa09839f-0db6-3f63-ac3d-7279448f9680 | -11.4302 | -43.4596 | 2026-09-29 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 30064038-748b-3112-869e-ac2bd7913820 | -11.1775 | -44.7832 | 2026-09-29 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| b41f011f-e6b2-3ec4-8133-57ae277faa1b | -11.1903 | -45.1505 | 2026-09-29 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8308bc60-6ff9-391d-9cb0-da9a5a2aa70b | -11.1771 | -44.8064 | 2026-09-29 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 1bf4f84b-6cc0-3917-b5c7-b29193e3eee1 | -12.0129 | -50.9251 | 2026-09-29 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| daf3fca6-1b23-3f54-8e22-53a6208ec3a8 | -12.7421 | -47.2684 | 2026-09-29 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| c8a317b0-d172-3d95-be32-cad5cb7caf85 | -12.0311 | -50.9869 | 2026-09-29 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| e4b46643-c2df-3d17-9090-c689feba41d5 | -12.761 | -47.2881 | 2026-09-29 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 2a951447-3188-3068-a7b0-71188a839407 | -12.7614 | -47.2656 | 2026-09-29 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 610e9d08-3ece-33ea-8432-6815e503de99 | -8.9823 | -44.1633 | 2026-09-29 11:50:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 27b93fc8-d3ae-378a-aa83-2d4a5597f11f | -8.9633 | -44.1655 | 2026-09-29 11:50:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| eb5f4a66-b924-337c-8008-2c00cb36d01e | -11.1907 | -45.1274 | 2026-09-29 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 39b3b69b-206b-32ec-ad68-343692ee9fea | -10.2147 | -46.706 | 2026-09-29 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 819c95c3-e007-3db5-aa3d-1b5dbb9f0b61 | -12.761 | -47.2881 | 2026-09-29 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 339bd4cd-9657-3b11-abfc-d00f9bf79f02 | -10.2843 | -44.6274 | 2026-09-29 12:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 942714a8-cb1a-35e9-b40d-3c1b57b5e745 | -12.7417 | -47.2909 | 2026-09-29 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| f079282a-20aa-30e4-8201-282cf8b022ba | -11.1907 | -45.1274 | 2026-09-29 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 18b7d132-71aa-33ef-9c24-90090bce897c | -11.1903 | -45.1505 | 2026-09-29 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 7332d1a6-e112-360f-bc3a-dd421a541efe | -8.6451 | -45.3489 | 2026-09-29 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 182c3179-ee42-3103-a99b-39d36983e0b1 | -12.0126 | -50.9464 | 2026-09-29 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| d6588936-7a0d-37a1-8f2a-6c8fd4546dff | -11.4307 | -43.4358 | 2026-09-29 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| bf14defd-c788-3841-84c0-2be9464bfadd | -14.4644 | -47.0447 | 2026-09-29 12:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| e828329a-e9c7-3129-9878-a6da70aaa291 | -8.9633 | -44.1655 | 2026-09-29 12:00:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| c0940733-a5ee-3d5a-adba-027d07ef7be0 | -8.9823 | -44.1633 | 2026-09-29 12:00:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| c8e8ac16-603f-3791-8e45-d70c9dd0ccfe | -11.3962 | -45.3973 | 2026-09-29 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 58748a88-5856-3f30-85ca-73cf64b118cd | -11.1775 | -44.7832 | 2026-09-29 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 0700964f-fad8-3030-b02a-e70af8965e0e | -12.0317 | -50.9442 | 2026-09-29 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| c3896e87-77e3-3d50-bd51-1f3b30e89fb2 | -12.7421 | -47.2684 | 2026-09-29 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 208.0 |
| c2c3eecc-9c92-303a-879b-6589d58aa7b1 | -11.1771 | -44.8064 | 2026-09-29 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 49ecf896-fc0d-3fa0-bad8-c08a242bb602 | -12.7614 | -47.2656 | 2026-09-29 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| b79caf2e-3988-3ab7-9a0c-5dfcc92c13ca | -10.3894 | -61.2502 | 2026-09-29 12:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 274.2 |
| 1bad3b6e-83d1-3e51-a634-aeb130894fc1 | -12.0311 | -50.9869 | 2026-09-29 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.0 |
| a24cd277-484c-382e-b286-aee864540ad3 | -11.9936 | -50.9486 | 2026-09-29 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 48f685e5-0baf-38bf-bf7e-8335e9ba0353 | -11.4302 | -43.4596 | 2026-09-29 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 7abb1c15-5984-3888-8bc3-c8bdf7065423 | -12.7417 | -47.2909 | 2026-09-29 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 66bfa9ec-ca55-38ee-9ac4-4cb0f3199c3c | -11.1903 | -45.1505 | 2026-09-29 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f6d9bc3f-7e65-345b-ae44-ff920d1704d6 | -11.4302 | -43.4596 | 2026-09-29 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| a477f04d-b6f0-3037-8fdd-f09504ee782d | -11.1907 | -45.1274 | 2026-09-29 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.8 |


[Clique aqui para ver as próximas entradas](README74.md)
