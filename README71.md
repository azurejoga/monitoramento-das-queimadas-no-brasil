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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3225e4a-ecde-3157-8510-f959d14059b7 | -12.28759 | -47.10942 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ae46e9e-56c6-3f0a-94fa-767df7ad1f54 | -11.0247 | -54.13409 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 236bdbcb-5c36-3965-84f5-04a63fcbddc6 | -7.05823 | -47.5316 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3696688c-d073-39f8-8dc2-e7e995d6fb7c | -9.26497 | -48.20587 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c31c1d0d-cdcb-39a0-b9e1-21f48e1ec6ae | -12.02256 | -51.47029 | 2026-09-20 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cf1af81-6bed-3f79-8d7f-3c76f3b16d4f | -9.83123 | -46.43649 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4712a954-473e-3d57-8a69-73d37f3152b0 | -9.02463 | -48.7816 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59007a1f-55c6-3f3e-8799-95d2aed5ea33 | -11.85606 | -47.668 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dc71ccbe-7ed4-342b-bf69-bc43d7d36a8e | -9.31811 | -48.49344 | 2026-09-20 04:40:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69991ebd-02d1-3a88-8b7b-16e901b9e3fc | -8.17736 | -54.75219 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5693dfe-9f85-3318-beb2-abbc4e989b27 | -8.61335 | -54.58805 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49df96c9-b93d-3561-a958-aa2a85171924 | -7.08608 | -44.7304 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3853aaa0-1c1e-3fe2-8714-930d07643743 | -11.48233 | -47.77985 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ea994c6-94f0-33c6-bb4f-52ed93969f26 | -6.39162 | -54.88883 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4135f285-4250-398d-91bc-d42a067c2e3c | -8.17595 | -54.73447 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f808033d-de9c-3e9d-83ad-b10146476447 | -10.29846 | -45.42318 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a990e157-a3f3-3b7b-9b33-ab48879accd9 | -7.18043 | -47.89997 | 2026-09-20 04:40:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c173e5d3-dcc2-3ad6-8fe1-4b238bf40306 | -9.8266 | -46.44356 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4884cfc7-bd2d-343b-bec2-9631877bf9f7 | -9.57555 | -55.10735 | 2026-09-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef050eb5-ba32-3553-870f-d3f46f82da79 | -8.73619 | -52.36373 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 972cb314-85bc-37d1-8da4-b7eeed06b750 | -10.67478 | -50.70428 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12d41781-d624-3a8d-a1c7-17be9648c242 | -9.02794 | -48.71795 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af5592a8-0c3f-324b-9c64-827936328030 | -11.42767 | -45.4091 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d1b0ce6-ec75-3eb7-b047-5cab6769b624 | -6.66555 | -50.8956 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b29450aa-d5b8-33f7-adac-b44fbd7ed098 | -10.83993 | -50.93698 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4a34c59b-15d5-3760-bc5e-f399ba399c7c | -8.47678 | -44.50772 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9bd380a-2383-3fc7-a8ca-14125c14db31 | -7.80203 | -44.93789 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86e5104e-f156-3ba2-8461-753024d56877 | -11.85324 | -47.66376 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 09c3a6ba-8092-3d3e-b39c-849bcd3caf4e | -11.09107 | -48.29341 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| adc810c7-33a0-31c3-8ebd-3398a0f58485 | -9.02186 | -48.75622 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3bba0e2-f52f-39b9-b092-53de8e24b1b1 | -9.70598 | -45.87189 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8a92918-d2d9-3cee-862d-399764376ee1 | -10.36793 | -50.45096 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 12a454a3-5be4-3943-8833-9bdd00a9bb76 | -13.20801 | -51.74627 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cd60dcf-60d9-367b-ad28-04df1902c3f8 | -11.97638 | -44.99753 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6856a94f-6419-3887-8266-41c9433c4622 | -9.79277 | -45.075 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 051e5166-c49c-3655-b019-368a7b816f12 | -12.02129 | -51.47796 | 2026-09-20 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b303f7a-9155-3405-a648-f601d0c05063 | -7.562 | -45.38393 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7ca5525-2c32-3fac-aa18-e29178f36484 | -5.84295 | -53.53765 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3781697-d11a-3105-acb0-d517fec1023a | -6.77231 | -47.86035 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 106c66e8-49f2-3040-a61b-1af47007f02d | -7.59335 | -46.97331 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0ab3e9c-a246-313b-87dc-c4cdea93f6d2 | -8.7723 | -48.70216 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3ac2710-bfa6-39a3-b805-ecc5e46b9a4c | -11.60724 | -47.04837 | 2026-09-20 04:40:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4019ccf1-57c1-3116-adbc-f6dba536744d | -7.21433 | -44.18494 | 2026-09-20 04:40:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5a4ab8b-0b3a-30ef-aaaf-1c4a8c6d3c6d | -10.9248 | -53.96557 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3612617d-d9ea-323c-9425-dcec461351bb | -13.60827 | -46.92702 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a26add9c-7a17-3398-958f-8d0b73cf7ff1 | -11.42179 | -51.46964 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16e31f82-bb31-3798-b2d6-98ac6e8dfd3c | -12.75684 | -46.14304 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8f70eee-43f5-3fd9-a0e2-af2ebe4e60e7 | -8.38778 | -45.63326 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dbd6a90c-c487-3234-98e5-f9ad740c8d4e | -9.02738 | -48.72143 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9380b10a-4ac4-355b-b4e1-f9be5b91509a | -13.95702 | -47.84169 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb05f472-b1ff-306f-a923-32efb09c31dd | -11.46018 | -47.64494 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abea79a4-4290-3fda-a7e9-2907b2135235 | -11.39156 | -51.38221 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74f75024-51bf-34e3-95d1-b3e0e0d11b22 | -11.48118 | -45.36343 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8345f435-2c1a-30bd-a89c-94218952fd95 | -11.38679 | -51.43283 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1382ce3c-336f-3dff-9bb7-f0f221a4880f | -7.62682 | -45.42996 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d01d2a58-44e1-3202-a24c-6d7d60372715 | -7.62373 | -45.45035 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4da7b43-55f3-39fc-912b-1b47442f4c58 | -7.74259 | -46.71069 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e80ef2c4-b938-3bed-84a6-0d24f0486f96 | -6.09733 | -57.68588 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1655eb13-bfc6-3adf-9330-48f9f004971a | -12.74619 | -46.19006 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff7e34f7-cd41-3eda-ae71-086b3b2361b6 | -5.83616 | -53.55212 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b25bd234-161c-332b-9761-9c41fa9b398d | -10.49136 | -46.27288 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07d04618-1456-30a3-a0ca-b5f5cf626641 | -13.02929 | -46.91059 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95814cba-e21b-335d-b511-e99105becce4 | -10.60192 | -46.52427 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1537f5b-da43-3e38-babc-15eabf370125 | -10.19258 | -44.15046 | 2026-09-20 04:40:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 234e7bb4-10bf-3513-92f7-f5bf691d810d | -10.41396 | -48.90954 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9108b089-ebf3-3922-8810-af8097a1e1f2 | -10.66765 | -47.42993 | 2026-09-20 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54a50bb6-8fa3-3c31-ae9f-c366cbcefafd | -9.79471 | -45.06155 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79fa42e0-483f-38d5-8ff9-a3df76099ac0 | -9.21296 | -46.22238 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c27ab42-22e4-31e4-bfd9-422e147039ec | -8.77178 | -45.86439 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd21a6ab-9e1b-3a33-b64a-42b618565337 | -9.04835 | -48.71765 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20e64f36-2b0f-3ff9-8d79-310347982c68 | -11.8345 | -46.85955 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d816840d-7aed-3191-a559-170f56383767 | -9.8341 | -46.44111 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 28aabef7-aff5-30c0-8cfa-0b90cc39f385 | -9.79099 | -45.06097 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a288471b-d63e-3d21-9d66-1606b5faf0a6 | -9.02407 | -48.7423 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7631529a-f5f3-3d2b-84d7-3346427f9857 | -11.85018 | -46.87409 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f365bab4-a0bd-3853-b119-bda7e743c9e4 | -6.0886 | -56.47011 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed2555f4-5cfd-3ffb-8610-2cdfac1feffb | -9.68874 | -49.28303 | 2026-09-20 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa084dde-253f-320c-8399-f4f7a0b9a94f | -11.32276 | -44.17855 | 2026-09-20 04:40:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c3a0afb-8a03-36f2-bec9-40ce5b2871a1 | -14.10897 | -45.60767 | 2026-09-20 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a3c818c6-7538-36f3-9470-20f66263c4fb | -9.35366 | -46.38684 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3cbf3109-483b-3d4f-850e-a6f10e41e6dd | -10.77543 | -46.16078 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95ae4fa3-956f-316b-a13f-946d41f3b282 | -11.05116 | -54.17963 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e0dca1d2-8159-39ef-9dd7-9b1dde67cbe2 | -11.02182 | -48.30427 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 812a6372-c9ba-3642-91a6-f6e3b87407eb | -8.72202 | -52.35688 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08d34874-a1e4-3aad-9b3a-c02a8a5d8e55 | -12.2887 | -47.12551 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1632c7ea-17ac-3abb-a15e-9c2eba53f18b | -13.23836 | -51.75537 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dba89ea-b06a-37e9-8d89-7673d861672e | -11.24102 | -48.37916 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f70c8d48-e4b6-3696-b3ba-693d84a6ee0e | -11.73689 | -54.55589 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff285f61-9bd1-3f04-a210-b738a99e288a | -11.08052 | -48.31734 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3bec154-2e0c-3ad9-9e86-4467e876f9f0 | -6.90427 | -48.78409 | 2026-09-20 04:40:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5df5f15-03df-3d67-8d11-cae647889463 | -5.89383 | -53.64491 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40787ddc-8289-305b-b9cd-a578331b1ffb | -5.85132 | -53.53897 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae58e7b0-4d75-3fcc-bd85-39d3b989d54d | -10.37145 | -48.36018 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4b589e5-8474-3c76-b70e-8a258a693726 | -11.36895 | -51.3902 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d4e59a5-9def-3d84-aca0-633eda4df89e | -9.05166 | -48.71818 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c4d9065a-c57b-3e49-8bb6-ced497cfa418 | -8.05609 | -46.26584 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c71892f3-8b04-345e-87e3-c8ebbc892794 | -12.75391 | -46.21321 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bb7684ee-bbb4-313b-9499-7473e4ebd89e | -12.77003 | -52.85562 | 2026-09-20 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dcf3aee-07de-3649-8009-152b8e54cd0d | -8.41596 | -45.87479 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d02f3e97-2f0c-31ca-b5c1-96bb5554fb88 | -7.01433 | -45.25195 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README72.md)
