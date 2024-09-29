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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4de8256-8f04-39e6-9d8b-78f4c11a9419 | -10.0499 | -65.07 | 2024-09-29 02:28:17 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 367a06a2-d1b6-3098-9859-acd02a9c08c3 | -9.0422 | -67.817299 | 2024-09-29 02:28:44 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d22ef5f8-a9f5-3a5a-a55b-90fccb0a7370 | -7.686 | -67.040497 | 2024-09-29 02:29:03 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5ce09ac-73b4-326e-bfda-787cfdc67fd1 | -8.0317 | -70.576897 | 2024-09-29 02:29:11 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3297928b-e65b-3738-b376-f24c7bbc7eb4 | -6.6559 | -69.952698 | 2024-09-29 02:29:31 | METOP-C | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c86f7175-d4a3-3136-bbc4-f61e063e0a25 | -6.6419 | -69.937103 | 2024-09-29 02:29:31 | METOP-C | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 550d3106-6394-3c41-88c2-48c0c369556d | -6.644 | -69.946098 | 2024-09-29 02:29:31 | METOP-C | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16ca5af1-3c15-35ef-9cb1-804596f51d3e | -6.6461 | -69.955002 | 2024-09-29 02:29:31 | METOP-C | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f50cd3b1-cac2-3236-a404-8bfdef13d6f0 | -6.6483 | -69.963997 | 2024-09-29 02:29:31 | METOP-C | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b97010fc-9874-3e11-95f9-0b4b17ffd7ae | -10.06179 | -65.06378 | 2024-09-29 02:43:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 9589c048-f249-3c1c-b9e4-d06ca2c4637c | -10.078 | -65.06085 | 2024-09-29 02:43:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 39935bca-4df9-39d3-bf1a-821099a572fe | -10.07132 | -65.06721 | 2024-09-29 02:43:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 116.2 |
| e404e415-b2a5-38fc-b545-524abd146a11 | -11.59147 | -63.89997 | 2024-09-29 02:43:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 95cc52ab-59d6-3054-b82d-10b817ee1d34 | -11.59334 | -63.89249 | 2024-09-29 02:43:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 32.9 |
| cf334bc9-1ed8-3b55-9c88-6a7713394153 | -9.65512 | -68.5677 | 2024-09-29 02:43:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6429c8d6-bc50-3a26-adac-b222c5965e87 | -9.06544 | -67.82583 | 2024-09-29 02:43:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ef2bebb9-5d20-393f-9946-75d21ec7ea48 | -9.06014 | -67.82107 | 2024-09-29 02:43:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 7a4f68d0-856f-3936-8d22-11e9a4a1f3bd | -6.6651 | -69.96506 | 2024-09-29 02:45:00 | TERRA_M-M | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| d21867ac-be20-3ea7-b6a2-643a42e57f19 | -6.66259 | -69.94859 | 2024-09-29 02:45:00 | TERRA_M-M | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 4c93f901-e5d0-3235-ba9b-b21c1dac4a5c | -8.04741 | -70.5787 | 2024-09-29 02:45:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f4fb68cc-a17f-34ff-bfd5-03b148a1b284 | -7.71049 | -67.0565 | 2024-09-29 02:45:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ba850f2f-9a3a-3004-895d-e485d4e3e88a | -14.58 | -45.79 | 2024-09-29 03:03:59 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db5a5f83-fa61-39b1-9c57-205d315c2232 | -7.56225 | -38.33917 | 2024-09-29 03:08:00 | NOAA-20 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 81240f2b-6900-3b82-ad4e-995f0274d636 | -7.55927 | -38.33777 | 2024-09-29 03:08:00 | NOAA-20 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 01a3a2e0-fe47-35b0-be52-8b858adc584f | -5.19888 | -35.61419 | 2024-09-29 03:08:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| afcf6b5b-8783-3b14-9f3b-a073dca9a4ec | -5.0705 | -37.72538 | 2024-09-29 03:08:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b2b567e-0965-39a5-a693-f6a316ba122f | -5.06974 | -37.72981 | 2024-09-29 03:08:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3bbe263e-4be2-336e-afd2-b2fa226c5ac7 | -8.95759 | -40.58191 | 2024-09-29 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6b37de52-f0fd-35df-b3f3-b78ed64bdeff | -13.89882 | -41.66691 | 2024-09-29 03:10:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3e8cfb0e-9ac5-3e64-9d2f-cd2a07d2ac3e | -13.89787 | -41.66442 | 2024-09-29 03:10:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ebdf22bc-3fb3-387d-8bcb-cb1dedff92c1 | -13.89234 | -41.6653 | 2024-09-29 03:10:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 58873fe3-dbff-3bc8-a5d6-2819f87e630e | -13.89139 | -41.66284 | 2024-09-29 03:10:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f1d24475-0dd0-3448-9cad-466c81bbb177 | -13.35667 | -42.06807 | 2024-09-29 03:10:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df30ec37-2a07-3b8c-a8e8-20746a853790 | -13.35498 | -42.07612 | 2024-09-29 03:10:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d6b971e7-0d1f-3885-b378-da56782d9de1 | -13.35179 | -42.06669 | 2024-09-29 03:10:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8feea02a-096a-3335-b055-7a35fd97734a | -13.35005 | -42.06608 | 2024-09-29 03:10:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8cfd9133-ddc6-39ad-b263-217cc8f3d124 | -13.34333 | -42.07316 | 2024-09-29 03:10:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9acbaa80-b72a-3632-a044-f0b6c00874d6 | -13.34167 | -42.07243 | 2024-09-29 03:10:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 06bcc76d-af6d-3a97-b167-a9de4c48be2f | -13.19745 | -42.24543 | 2024-09-29 03:10:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| f01248b6-19ce-3276-a19b-025dc8fde99b | -13.19668 | -42.25196 | 2024-09-29 03:10:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 7cad1e9a-c412-3cf2-8051-8f9539a95fa9 | -13.19583 | -42.25306 | 2024-09-29 03:10:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 2609a009-1836-365d-a676-327ac327f53c | -18.0927 | -43.97073 | 2024-09-29 03:13:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8491fb2c-0d56-3c48-8f3b-34469ef3c5d6 | -18.09214 | -43.97016 | 2024-09-29 03:13:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d54168ac-a936-3a37-b23b-02e5cb1b1e17 | -18.09117 | -43.97726 | 2024-09-29 03:13:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b7e7bb1-ab0e-3af3-9d8f-6a2edcb1a736 | -18.09059 | -43.97659 | 2024-09-29 03:13:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1158e38-2ea9-3174-ab10-6b6dd5c93dcf | -18.05575 | -44.39729 | 2024-09-29 03:13:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e801c09-aae7-3571-bdae-5507cfb93b05 | -18.05414 | -44.40401 | 2024-09-29 03:13:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f49a59f-65ce-3608-a0be-9294eaa3a488 | -18.04877 | -44.39539 | 2024-09-29 03:13:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9df46c32-3edb-3ba0-818f-5bbb22927134 | -18.04722 | -44.40184 | 2024-09-29 03:13:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cc70881-770f-3296-afc5-c5b8a3b2dd4e | -17.76996 | -43.3146 | 2024-09-29 03:13:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 800265fc-9cf8-35af-92c8-4ab094fce71e | -17.76723 | -43.32637 | 2024-09-29 03:13:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4dd07fe-07e1-313c-aae7-eb221fc8bc82 | -17.76204 | -43.31842 | 2024-09-29 03:13:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fbbe8313-a02d-34b9-9a9c-b23f820fd962 | -17.76065 | -43.32438 | 2024-09-29 03:13:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c77e03a3-b601-3268-805d-b266419aaeb9 | -17.75916 | -43.33079 | 2024-09-29 03:13:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3f78f147-7d93-3bed-ab5a-851a78f13773 | -17.62853 | -43.26379 | 2024-09-29 03:13:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1947de59-d3e6-3585-9340-17a41a7445d4 | -17.62611 | -43.25552 | 2024-09-29 03:13:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97bd5477-5d8e-329c-a682-319ef6a42453 | -17.62433 | -43.26313 | 2024-09-29 03:13:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9da07efd-a30e-371d-83f1-53d1b04786fd | -17.62191 | -43.26201 | 2024-09-29 03:13:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d571855-e8b1-3b14-a4eb-78cd245ad53c | -17.61786 | -43.26072 | 2024-09-29 03:13:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1538919a-f626-3b60-9ae1-7275e6512532 | -19.93817 | -40.74892 | 2024-09-29 03:13:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e233a8c7-c678-3dd8-ac51-590e5fa0bef7 | -19.93496 | -40.7435 | 2024-09-29 03:13:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4f08a7d6-87ca-345c-b90c-bf02a1f6656a | -19.93412 | -40.74738 | 2024-09-29 03:13:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 36d243db-a9d9-35bd-b773-113436ce7d31 | -19.9334 | -40.74427 | 2024-09-29 03:13:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b8d5f065-8ae5-3360-927b-b2deb2ff14a3 | -19.93333 | -40.75108 | 2024-09-29 03:13:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 76189b24-949a-3c4a-aaa5-ec3b9616dd1d | -19.93255 | -40.74805 | 2024-09-29 03:13:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f242a2b2-a482-3afa-993f-7e7333b4581d | -19.40572 | -42.98664 | 2024-09-29 03:13:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2491dfda-fe26-3421-9499-64dbc8a0c23c | -18.94982 | -42.09244 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fafca7fd-6dbc-3b16-bee4-37aa194d4d86 | -18.94366 | -42.09132 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 46a485b2-6cf3-3f9a-bded-a6baca9a839e | -18.94038 | -42.10591 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4a7d1554-211d-3843-b369-1b7d48301205 | -18.93931 | -42.11066 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 09fda431-8842-3cf2-a462-df59265821be | -18.93754 | -42.08998 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4763d90b-6fab-3d5a-9ca0-c6bee3837865 | -18.93646 | -42.0948 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 28a86de5-93f5-398c-a100-61f44f490a32 | -18.93427 | -42.10449 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 506ef828-10c0-3913-9ba1-94cd39ff16d6 | -18.80383 | -41.91789 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fa4f69e7-6926-3777-9f8c-e198be4e2692 | -18.79901 | -41.90961 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 720bc3f9-e507-3001-8312-dfab743357e2 | -18.79897 | -41.91129 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a20794ac-d2ec-3ac7-bb87-f483bfc5e61f | -18.79794 | -41.91442 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b487041c-357e-3d05-bdd3-3e68c57068ef | -18.79412 | -41.90463 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| aa99de81-d3f4-3264-a4c9-a1a5c915cb21 | -18.79303 | -41.90789 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3806d53f-0627-34da-af47-488f8d2a43f5 | -18.79297 | -41.90966 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4d655f59-a646-3330-ae34-0920cd52fe2d | -18.7919 | -41.91298 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 86ccdccf-50e0-3bcd-93fa-381b198efe9e | -18.79185 | -41.91456 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5bdd9196-ecb1-3259-9dff-d51873274d0b | -18.79089 | -41.91754 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a7d70a70-e89b-321c-a9f2-0a06989ec549 | -18.79081 | -41.91909 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5061b719-e07c-3e0a-a8b0-9f099c0e4c65 | -18.78985 | -41.92222 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 07aa8eed-725f-3e1f-8f09-85da72304fc5 | -18.78482 | -41.91621 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6d358518-fd99-3ed9-bf20-a52e30c1557f | -18.78476 | -41.91769 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 92af6b5a-e55a-34db-8ec7-f5f9f5a89a36 | -18.78384 | -41.92062 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| cd23329e-3430-3434-8ca0-ecc5c3cbbffb | -18.78371 | -41.92225 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 06f8eb39-bd8c-3640-b923-4eacf4cef121 | -18.78275 | -41.92552 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d1faa4b1-5698-3d15-8dd2-3331b8548736 | -18.78257 | -41.92723 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5ee8b1cb-caac-3acd-95d4-d91b88834ae0 | -18.78165 | -41.93049 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 22ffd86f-3877-371e-a316-e20aa27989b4 | -18.78144 | -41.93215 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e7cc87e8-3acd-33dc-b3e9-af9006255a7e | -18.78056 | -41.93539 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2bbeda8f-592f-38f5-afa6-c609650866e5 | -18.77571 | -41.92854 | 2024-09-29 03:13:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9b06b015-f319-3238-95fa-01c114eca155 | -18.54687 | -41.34895 | 2024-09-29 03:13:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 26538265-5835-3fc9-93a1-c7a4d04133c6 | -18.54113 | -41.34691 | 2024-09-29 03:13:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9bfe7fba-22bb-392c-a003-a9d75a0e45bd | -18.36306 | -42.76878 | 2024-09-29 03:13:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b80f0e32-1b55-3c78-85c4-e9a899cf0718 | -18.36175 | -42.77455 | 2024-09-29 03:13:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0e149390-469e-32c1-b933-4b169e3a8911 | -18.35146 | -42.76054 | 2024-09-29 03:13:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |


[Clique aqui para ver as próximas entradas](README19.md)
