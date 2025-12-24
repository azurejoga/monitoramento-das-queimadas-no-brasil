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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 952de459-408b-315b-ab0e-8a5bd2dbc443 | -16.31775 | -53.79488 | 2025-12-24 03:57:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be711d3b-3c02-3d05-a2b7-c74a0edb838b | -15.91224 | -43.72179 | 2025-12-24 03:57:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13eac2de-fa9e-301b-9cd0-7be3c39895aa | -16.58809 | -45.87668 | 2025-12-24 03:57:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e638e000-71ec-3c80-9c26-32757c605438 | -19.68623 | -41.4778 | 2025-12-24 03:57:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3e355915-6160-3f99-9872-6ccb77b641e7 | -17.58245 | -46.66733 | 2025-12-24 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3596424-604f-364a-a34a-e4ed50852806 | -17.42326 | -43.82475 | 2025-12-24 03:57:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20f40c7b-8386-30a3-a230-a791e1c15b72 | -17.57835 | -46.66653 | 2025-12-24 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f17f336-22b6-3b2b-91c7-8e1b61901adb | -19.68291 | -41.47722 | 2025-12-24 03:57:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0e705c29-d171-30a4-a592-9cf4137f893c | -16.58412 | -45.87589 | 2025-12-24 03:57:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5052d35e-7e67-3315-be2d-06c5d50168ae | -15.66829 | -46.32241 | 2025-12-24 03:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e57eaf3-0d56-31bc-b1ba-5cfb71c7fb33 | -16.30987 | -53.79961 | 2025-12-24 03:57:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 385c70c7-d5a2-3272-a476-d25f59ea2901 | -11.84425 | -43.78634 | 2025-12-24 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c94f8f7f-4ec5-3b22-8734-5eade98abbc5 | -12.27996 | -43.53512 | 2025-12-24 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be8c3af1-f45d-3214-aaca-919a89ff976e | -16.30622 | -45.10352 | 2025-12-24 03:57:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb24c9c5-b1ea-3ca9-8736-fda7061b5f62 | -16.30533 | -45.10032 | 2025-12-24 03:57:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 798edb2a-ded2-36fd-b78e-275d6becbee3 | -11.84346 | -43.79102 | 2025-12-24 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bc4748e6-ef5a-3709-93e1-a3dae4343938 | -14.88418 | -43.56094 | 2025-12-24 03:57:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 785b8a8f-c23f-3df7-a748-6dba44e58604 | -15.35833 | -43.16626 | 2025-12-24 03:57:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 04bcda4d-4396-310e-8322-6f3ce85cb1e4 | -12.2852 | -43.52684 | 2025-12-24 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 635e7ce9-4c37-3a17-955e-c4c91792c6f1 | -12.28443 | -43.53132 | 2025-12-24 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c8fd13b-58e5-39a8-8672-2c5d7e16a460 | -16.30242 | -45.10277 | 2025-12-24 03:57:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79c7bf51-8e5a-37ac-9465-fcbf31c4f8aa | -11.84644 | -43.79636 | 2025-12-24 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2fcba7c3-3fd6-3793-9bba-da009f814d27 | -11.84266 | -43.7957 | 2025-12-24 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b0032ce-d631-3285-bba8-2b374d84a163 | -12.2815 | -43.52618 | 2025-12-24 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45b13555-c13e-309e-93e2-cb763b0e729f | -11.81328 | -43.7856 | 2025-12-24 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 692b57cd-ce7d-384e-ab66-eb2d994a5496 | -14.62981 | -44.22281 | 2025-12-24 03:57:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| caf20e7f-36ea-3ff4-ad70-8846c24f35d2 | -13.37569 | -43.20213 | 2025-12-24 03:57:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5b7db47d-fc47-32dd-879d-ee7bb990d33f | -12.10215 | -43.50301 | 2025-12-24 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90a02ecb-8796-387b-b117-000fd5ab8a5e | -14.03333 | -50.53578 | 2025-12-24 03:57:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11524a78-2447-313d-a720-85444d0ef681 | -11.83889 | -43.79503 | 2025-12-24 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 04197c38-ec91-3734-8f8a-bb56e96a03e9 | -11.83214 | -43.78899 | 2025-12-24 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cfb4f40-a15c-3477-ba66-0d720e8287c1 | -16.31644 | -53.80083 | 2025-12-24 03:57:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebb1d9bf-e916-3912-85db-470420afb811 | -16.31473 | -53.80137 | 2025-12-24 03:57:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62d7ae62-3fa5-3792-9476-b3867d6a408c | -15.91581 | -43.72246 | 2025-12-24 03:57:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3234f1d9-014e-3e52-af9c-6eea6da230c5 | -16.31608 | -53.79542 | 2025-12-24 03:57:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6abaa5f5-e613-3c50-a20f-042183682984 | -13.65732 | -43.73112 | 2025-12-24 03:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc790a4c-90c0-38f7-8aaa-f0532561585a | -14.03969 | -50.53322 | 2025-12-24 03:57:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f327b04-429f-37aa-983a-14a22a29a59d | -19.69464 | -47.9695 | 2025-12-24 03:59:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b06df5ae-18e7-3f0c-9540-aa21d05eb1b8 | -23.89917 | -50.17635 | 2025-12-24 03:59:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 76e3e4b5-9480-33f4-8989-e2d4df78ad3f | -22.48565 | -49.90583 | 2025-12-24 03:59:00 | NOAA-20 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c21f1aa3-61e4-31f8-81f8-a231f999c980 | -22.48703 | -49.90349 | 2025-12-24 03:59:00 | NOAA-20 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 535fef8f-f6a5-3bf4-9b75-8af4171a46d0 | -19.52847 | -46.02534 | 2025-12-24 03:59:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4848c000-8c5e-3e01-b26d-acaa199ba076 | -21.57529 | -43.67173 | 2025-12-24 03:59:00 | NOAA-20 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cc6cc660-bc20-3040-ad4f-98efa8a7f265 | -19.91418 | -50.86663 | 2025-12-24 03:59:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| be1585f8-943a-348a-927e-8e44ccb9ce27 | -20.9133 | -48.66857 | 2025-12-24 03:59:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 739b2695-ac6b-374b-8b08-089e11399669 | -22.09447 | -45.30373 | 2025-12-24 03:59:00 | NOAA-20 | OLÍMPIO NORONHA | MINAS GERAIS | Brasil | 3145505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 92d4a565-0a33-33a3-b40c-ab434273ff51 | -19.99145 | -42.26918 | 2025-12-24 03:59:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0eea39ae-0b8f-3c68-994c-25faad6b372f | -21.05231 | -48.42908 | 2025-12-24 03:59:00 | NOAA-20 | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8cdcfca-6e9e-318d-b2e7-da41e98197ac | -23.31076 | -46.11506 | 2025-12-24 03:59:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7da4a71-828e-3bce-ae4e-8e043e9f4513 | -23.45375 | -47.4516 | 2025-12-24 03:59:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6546446f-d190-33b0-a659-cedb4ab160c5 | -20.95958 | -47.18291 | 2025-12-24 03:59:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74e4e37a-e3bb-3e2d-ac9b-cfae4c3be7bc | -21.00281 | -44.90089 | 2025-12-24 03:59:00 | NOAA-20 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ec89e026-c339-3649-bd66-51f267fce37b | -20.62601 | -48.94252 | 2025-12-24 03:59:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7b9ad2bb-c447-3a8d-ae91-ff5e14ef3d03 | -19.90908 | -50.86541 | 2025-12-24 03:59:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f9eb2baf-d776-3e4b-959a-e7df8e1c40a7 | -17.91171 | -54.13049 | 2025-12-24 03:59:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0fcef25-fcc2-3e23-9676-7a0723f4310a | -17.90916 | -54.14163 | 2025-12-24 03:59:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51051d3a-83a3-3e91-9edd-b5f92ba26ea6 | -20.43789 | -48.95505 | 2025-12-24 03:59:00 | NOAA-20 | GUARACI | SÃO PAULO | Brasil | 3517901 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d986ffad-ac7e-3fbd-828d-1f92762e7866 | -17.91044 | -54.13605 | 2025-12-24 03:59:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 459f2fad-7279-30ce-b969-5ee4359c1246 | -21.69936 | -42.35991 | 2025-12-24 03:59:00 | NOAA-20 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d61c1852-e569-3199-939c-9acb256d3064 | -22.93278 | -43.59568 | 2025-12-24 03:59:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1392e22f-56af-338e-b4d3-e7d98e8614fb | -22.49022 | -49.90688 | 2025-12-24 03:59:00 | NOAA-20 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9632254-d7ee-3310-8c45-7f478349cdc4 | -22.9843 | -48.62949 | 2025-12-24 03:59:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c0da1ee-2159-301e-9497-100dc40de70f | -20.99576 | -48.75718 | 2025-12-24 03:59:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cda723ab-410d-32a4-83d0-fff1ac885926 | -19.075 | -46.42126 | 2025-12-24 03:59:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a01ab7ca-3f4b-3e31-80b1-f6e46bccbd58 | -21.49312 | -42.65179 | 2025-12-24 03:59:00 | NOAA-20 | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2c782232-8b18-37c6-8cf5-f9c38ea9bf10 | -20.99485 | -48.7617 | 2025-12-24 03:59:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d93b6aa3-a4f1-3f87-a497-268194a294ad | -20.95562 | -47.18192 | 2025-12-24 03:59:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 103ac32d-a9e3-33ce-9e18-987730b1c53a | -21.05143 | -48.43351 | 2025-12-24 03:59:00 | NOAA-20 | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79824142-2ea8-364b-8ef8-cb0ebfb3c877 | -22.48599 | -49.90864 | 2025-12-24 03:59:00 | NOAA-20 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8af07313-7a1f-36ba-ab71-eeaca766b907 | -22.38795 | -49.89534 | 2025-12-24 03:59:00 | NOAA-20 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1f2d58a2-d023-3508-98be-8488f2593923 | -20.62156 | -48.94144 | 2025-12-24 03:59:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 98830641-0446-3197-84db-c973e7ef450c | -25.51242 | -49.4662 | 2025-12-24 04:01:00 | NOAA-20 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 740aaf0d-475f-39f4-8164-b03d6a4fd189 | -25.25665 | -51.02943 | 2025-12-24 04:01:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ae22b735-c6c0-33a4-835a-f4abb1f6ddc5 | -25.252 | -51.02831 | 2025-12-24 04:01:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 342b619b-918f-34b2-893c-09d5a3fe98e0 | -3.5573 | -41.6357 | 2025-12-24 04:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 18d2163e-8e08-3e7d-9434-9ba5713f5f2b | -3.5573 | -41.6357 | 2025-12-24 04:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 48b9d6af-a70c-3532-b984-30bb2f8b3ed4 | -3.55203 | -41.62983 | 2025-12-24 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 18356da7-b496-3c11-99b7-0cccd88b6eef | -3.5525 | -41.6266 | 2025-12-24 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5b50fe63-49a4-3840-b696-9bddd0268f5e | -3.54775 | -41.62257 | 2025-12-24 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| cb02beb5-6029-355c-827b-7ae0ea28b0ce | -3.54727 | -41.62577 | 2025-12-24 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| cd0f8b0d-50fd-3c09-bf19-9db417cf8fda | -3.54204 | -41.62495 | 2025-12-24 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4c4e5b69-cc1b-33d2-8d5e-0fa305ec5b2c | -3.55774 | -41.62738 | 2025-12-24 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f6149582-bdd8-3f6e-8046-55f29b77322e | -3.55726 | -41.63063 | 2025-12-24 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6436e739-c354-3364-9732-7ca2d2a0833c | -3.54157 | -41.62816 | 2025-12-24 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4dc99ea8-1ae6-38b3-89cf-af4765562fd3 | -3.5468 | -41.62899 | 2025-12-24 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 9e1c5cbe-d265-30a6-a6a2-8ab57c8f73b1 | -3.55822 | -41.62416 | 2025-12-24 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 537e7e91-7566-350d-8c56-5c13b0395a66 | -3.55298 | -41.62339 | 2025-12-24 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5c1d8dc8-72d7-303e-9fa8-761792e4a1b7 | -11.83338 | -43.78814 | 2025-12-24 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30119012-00f9-3488-88f3-385f8eb0f6ae | -11.84789 | -43.79637 | 2025-12-24 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 50994b30-b892-388b-99d4-4c722abb173e | -10.37764 | -47.65984 | 2025-12-24 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 662289aa-c459-3ec1-9b82-057bceefc9bf | -11.84358 | -43.78956 | 2025-12-24 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23d8b8c6-e88d-37b3-aa90-259d9710bf2c | -7.23429 | -43.08983 | 2025-12-24 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d16f6050-7399-3079-bb78-03b98edd5e26 | -11.8428 | -43.79564 | 2025-12-24 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 878577fc-56e2-3d09-8046-3c975ae4feeb | -10.38007 | -47.65671 | 2025-12-24 04:46:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14bb752f-1025-3868-81f7-8c4000876258 | -7.23467 | -43.08735 | 2025-12-24 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f0188c12-7e16-3736-b6e5-cdc51bd97f9f | -7.22969 | -43.08622 | 2025-12-24 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d99fa380-b4d3-3995-8416-d72d5645f4b7 | -7.23011 | -43.0833 | 2025-12-24 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f297ac4d-e14f-319c-852e-95e383cd1521 | -11.84397 | -43.78653 | 2025-12-24 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79ec639e-f970-3140-a3b4-0519f9892c5a | -11.84319 | -43.79259 | 2025-12-24 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e33a9823-5125-36cb-8144-813947ae4207 | -10.71388 | -44.15601 | 2025-12-24 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README4.md)
