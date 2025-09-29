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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e2d4867-39a3-3ca5-837a-edc9d576cea7 | -13.82429 | -47.96736 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4285aa83-1a0f-3bd8-ad79-1c3c485ec5fb | -9.77497 | -46.19597 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9133559-5834-3c3e-b211-2df99287d95a | -13.81939 | -47.9719 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbf536c0-aca3-3c6b-9303-0e7e1d1d48e0 | -9.10097 | -45.84413 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdda6c22-44bd-3654-8564-cf341c8b631b | -8.05501 | -47.9938 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb1d2f3a-dd9e-3da0-9573-405c50fec9d9 | -11.68846 | -44.30774 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c14d3e8b-bc60-3cdb-8a22-b545eec32439 | -9.1047 | -45.84474 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5fd87e5-9de0-3039-9692-703bf0660671 | -10.81335 | -46.66471 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6af889d-d444-3a8b-b796-f90ec6fc9803 | -11.50637 | -43.54349 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f71304ee-625a-351f-b7cd-b0407ef75a33 | -14.54933 | -48.39983 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d1e93a6f-8d29-3b64-b3b7-2b6e9dff6073 | -9.07068 | -44.99466 | 2025-09-29 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 836d0bcb-e62b-3daf-bbac-3869b7e419aa | -12.53473 | -48.29432 | 2025-09-29 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9bd2bc3-671f-37d4-bdce-c2f6d1f5ab0e | -11.71701 | -44.43427 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70fc11de-f401-3787-b688-fcacd8f478e3 | -14.53887 | -48.4348 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d8e18320-f541-3522-adcd-ae1a146d58e7 | -15.87257 | -46.21526 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa9de9f8-1cf3-33b1-922e-23ab9ddf2680 | -14.05913 | -41.61065 | 2025-09-29 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 57de8755-4ae9-3d74-bab2-2367a58704b2 | -9.79123 | -46.937 | 2025-09-29 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31bc08ef-993d-3153-8d3e-25f979dd2915 | -9.0503 | -46.70444 | 2025-09-29 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dbdb2743-1a27-3d26-8b24-c6e25c4c9e15 | -12.6549 | -51.66777 | 2025-09-29 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4006e29d-1829-34ef-a65d-c2ea4fc17144 | -10.04679 | -50.19646 | 2025-09-29 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 873bb963-9640-3acf-8840-0d9ba748a0fe | -13.5767 | -47.29082 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c17d4cb-a7da-32f1-a7e3-e7fe2d1b02d6 | -15.90835 | -46.20034 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50c28fa5-d016-304b-8278-c0d6d08548ab | -12.65271 | -46.92627 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 74e0bbf3-ade8-3755-9487-f0c864018d5c | -15.86091 | -46.24177 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a14c9c1a-af6c-348b-9436-f285411038e0 | -15.16757 | -50.09065 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85b99104-ccb7-3bc9-92bc-3c1d16a754c6 | -15.79286 | -42.20285 | 2025-09-29 04:08:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c9a669f1-6abc-3e81-aaf5-fce29da98f62 | -11.923 | -48.04062 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfb715bd-6af7-31e3-ba69-7d9332ef8f6b | -10.54307 | -43.63214 | 2025-09-29 04:08:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d32f1e0-2bce-3520-b60a-59b34b96f943 | -12.96283 | -45.17915 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4f89761-8a2f-3894-aef3-b22e6868480d | -11.21257 | -47.75216 | 2025-09-29 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c987fc4a-02a8-35b8-a6bb-f9c28cf4d329 | -9.39829 | -46.24332 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0b331cc-6773-3312-977d-d04f1a3a167e | -12.98361 | -46.26528 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 77dbbcbc-6298-3e23-b465-f88e06b27ecc | -11.69065 | -44.31572 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61a374af-55a0-35a1-a742-2354d0f819b3 | -11.45273 | -51.49781 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b3dcfa2-11e1-3b5e-bac5-1b68f1fa4822 | -12.89835 | -47.09951 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c67186d-afc2-39aa-a354-8f713e41a670 | -13.63006 | -47.33824 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 07815266-b398-34eb-8577-5bebc53f318f | -11.50869 | -44.84885 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 264e0367-15aa-39ec-818c-fd38baa366cb | -10.80622 | -46.68316 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| cbb55731-4979-384a-b0d5-c1e970cce5e3 | -11.80394 | -44.90829 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3edefc6-9f64-31c3-ae1f-765737097ae6 | -13.77919 | -47.86017 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6705a67c-57e2-369c-b770-4f16f0f4cc5a | -13.36123 | -47.30111 | 2025-09-29 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6a99bda-1378-36cc-b0d1-1716b554ecf2 | -14.84328 | -48.37667 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d85145af-686c-3c41-86fa-8eb7d9cb4f68 | -9.28219 | -45.73151 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d8b425c-a269-32c1-a424-5006ff514fba | -14.66863 | -48.16656 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4be70a89-eb09-34b1-a9cf-71d2f9b597bc | -13.40461 | -48.15377 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbf9bf2a-2a80-3b27-9717-78620dd87c79 | -12.69692 | -46.89482 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d9a084d-e293-330c-8b80-d7e864a20140 | -14.93625 | -46.58542 | 2025-09-29 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d0d78d4-c245-38c9-86c3-c56efddfc368 | -13.39251 | -48.15191 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ff1ac859-bc87-3176-b24f-443f5b7b14ac | -15.87127 | -46.83268 | 2025-09-29 04:08:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e8dc530-bb6b-3c77-b507-843ae6dd1c01 | -12.93906 | -46.77235 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 221adf7e-a913-343a-823a-5c591e763515 | -11.45214 | -51.5009 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85596036-df9c-3706-b74b-1a13fab78afc | -15.40234 | -44.98376 | 2025-09-29 04:08:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2750f3a6-d9ba-3d93-a1b2-cc65094331bb | -11.9686 | -48.04006 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7812a0d4-7cb4-3f39-bac8-72bd7188fe24 | -10.03805 | -52.10475 | 2025-09-29 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74ce2275-33ff-329a-b173-db38325e4122 | -14.58725 | -45.0136 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f411ec93-b638-3137-9a57-dad71f1be516 | -12.94952 | -47.18848 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 797e00cd-d966-3208-9567-090eb54588d6 | -11.50913 | -43.54762 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b2ac203-31eb-3aa0-948a-37f4abb70b2e | -15.15794 | -46.40893 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7bd3072-8470-3a56-89a5-5ca957608388 | -15.26453 | -40.61742 | 2025-09-29 04:08:00 | NOAA-20 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c9e77c4a-e38d-3850-ac3e-bd2ca2c76c2b | -14.46836 | -42.17068 | 2025-09-29 04:08:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 75647255-f4f8-37b7-a104-3e44fc696859 | -15.52054 | -47.931 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.0 |
| abf92dd2-c54a-3947-97aa-f41946568359 | -9.31319 | -45.70483 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 184997f2-3ce3-3fff-a25e-f77ad5fc8014 | -8.65671 | -50.08856 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd069f33-095a-3d28-96e7-bab073dc9767 | -15.07387 | -48.33675 | 2025-09-29 04:08:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fd0e968-d35d-33bf-b2e2-454225e27f9a | -9.28145 | -45.7359 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4f07f18-94f3-32ad-aac5-3d9f59f9a98b | -12.85089 | -46.97117 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4e61cf1-c125-3969-9114-22a692c83235 | -11.98192 | -47.1229 | 2025-09-29 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73d49368-8964-3520-8bea-c3cc6393937d | -9.05424 | -46.70502 | 2025-09-29 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c24f4454-f458-31f8-9f15-ed95ac81f47c | -15.41832 | -48.23279 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30cbc081-33f7-3450-9a45-d0a3b511fa6a | -10.00191 | -46.69356 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80df67ae-0b89-3980-8c9c-04cd71567bc5 | -11.98208 | -47.86988 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d23f8201-45e0-37e6-a2c3-70890ffa9102 | -11.37175 | -44.97731 | 2025-09-29 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ba9320e-a1c7-3328-9f83-f799cfd1f9a9 | -14.70235 | -45.20786 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ec575d9-bf16-377b-86ae-592af31fcd4e | -15.87193 | -46.21908 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15300183-b686-33ec-b887-af223d24c909 | -11.72288 | -44.41993 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 057456a6-7b09-3e2d-8e0e-a1990b34cefd | -11.82408 | -51.79301 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ec669d19-999e-3052-9e0a-1243ff114cf5 | -11.62503 | -52.86573 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0319822-355d-32b0-9d79-81f88f80a9d3 | -10.92238 | -45.7195 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb06a07a-b5ab-3ed4-b96c-74c777852768 | -8.71727 | -47.98355 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95e390e4-ba72-3d0e-a3b3-fb35f85b64fc | -11.4579 | -51.49882 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4519801-e1ee-39ad-a222-b133bcf8408e | -8.71596 | -50.04905 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e0c3f21-0de8-351b-8976-cb1425e7730c | -12.96066 | -45.1708 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d9db7f1-aba1-3650-b571-c02df553a957 | -11.62243 | -52.84929 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75b6951c-bda1-320f-afc9-be101c81eee6 | -10.40606 | -48.11604 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e2363d5-38be-3404-b5e3-b2f829b7afd6 | -9.29773 | -45.72942 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 241ce54c-ccc9-3cd3-abb2-07f519a5f84f | -9.63946 | -48.12975 | 2025-09-29 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fedf6f7b-36ba-390b-9310-4d58181cfc3b | -11.92775 | -48.03755 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 773d915e-a467-3457-af83-4ee8cd69c97d | -11.44817 | -44.97785 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3d069143-926f-3fc1-8916-b97a6abe051f | -11.3619 | -45.08064 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4c9b6579-6830-3f73-a6a7-44330bca9967 | -11.80048 | -44.90775 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c79b9892-864f-3827-a1ac-f4486fab8cfa | -14.56431 | -48.24855 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e571f9b-a55b-309d-997c-7e53bd39261c | -8.91265 | -46.085 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4233ea71-0e58-3892-8b54-9b70e405ca44 | -12.80146 | -47.75904 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cdb4209-47f6-3cdf-bcfd-578e73a23153 | -12.28715 | -44.09679 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f82ddf4e-8ce0-3a96-a5e0-5e3c0c39791f | -15.99742 | -47.03317 | 2025-09-29 04:08:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb060800-e6ab-300a-a32e-ff82e08c17c1 | -13.82284 | -47.47936 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99b074f5-8bfe-3f29-8275-5323ee43f841 | -14.72999 | -45.67605 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a608743-c07a-34dd-9a39-90fc289c2316 | -12.97477 | -46.86248 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ead1980-2eba-3b18-b45f-0b0345c5b8fd | -12.89247 | -47.08846 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9694451-a360-3788-b600-8d40bf7152a2 | -12.9462 | -45.17225 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README45.md)
