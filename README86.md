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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c871f06-d438-3a6f-aeaa-2b5d74c7b2ae | -3.3765 | -54.11215 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89e22b00-cf91-3a9c-875f-deb2a7031882 | -3.376 | -54.11507 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0dac95a9-8352-3f53-898a-0e017a2f1d26 | -3.37551 | -54.11796 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bd258d8-3787-3a80-8259-ea88f1fd1ab1 | -3.37543 | -54.09989 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 687af639-aea3-3e12-bc2f-547d701be3c0 | -3.37501 | -54.12085 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcd6057a-0f42-3822-b801-2c2b08e60e84 | -3.37495 | -54.10281 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a9cb73b-d132-3f62-8bbc-02da43853de4 | -3.37446 | -54.10581 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f6675d0-d9db-3bd9-b575-50ef2fdfa6c4 | -3.37396 | -54.1089 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcf553f5-7b04-344a-b5de-5b583ae421ec | -3.37345 | -54.11197 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c583b9e6-bd4d-3e64-be84-7844b6bd3326 | -3.37297 | -54.11491 | 2024-10-03 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a6e5c26-2fc0-395f-aab3-a3cc4734bfd3 | -2.95175 | -53.70329 | 2024-10-03 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d44cd8a9-494d-37c2-b79b-3be49b5b7554 | -2.95127 | -53.70618 | 2024-10-03 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73225783-1d4b-3fb9-b2bd-2158a52c5025 | -2.94722 | -53.69963 | 2024-10-03 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dac241a-c5cf-3b2a-ac3b-a722b3653941 | -3.66707 | -54.37015 | 2024-10-03 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2daedd1c-f398-335b-be55-fcdb0d4d1e7f | -3.66557 | -54.3705 | 2024-10-03 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 959c7e01-4a19-3b5a-b37f-77d997b9ebce | -3.65939 | -54.31118 | 2024-10-03 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0361f664-f02b-36f2-aef4-5545c3036338 | -3.6589 | -54.31417 | 2024-10-03 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83165af0-0ca1-3452-a336-4e4e92e02210 | -4.0949 | -48.4894 | 2024-10-03 04:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| dbc7bc57-a132-3791-bc8c-0460c89a991a | -4.095 | -48.4679 | 2024-10-03 04:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 19f99655-773f-37ca-9fd5-0b8c95d9c63e | -9.0515 | -67.871 | 2024-10-03 04:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 8acaf85c-6139-3f0b-9cf8-b706420634c4 | -9.0516 | -67.8525 | 2024-10-03 04:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 627ac0df-8335-3dc5-a062-52bc06e5ae0a | -10.9384 | -46.5717 | 2024-10-03 04:26:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 69cbaf39-fdba-3670-8b63-230e64d8b38b | -10.9381 | -46.5942 | 2024-10-03 04:26:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 63f08d58-cb1d-3ad2-a743-43acf97fa0f1 | -10.8942 | -63.8971 | 2024-10-03 04:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 22bca684-be84-324a-9d0f-8e56c3eead2c | -11.6932 | -64.9785 | 2024-10-03 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 141bb51e-57a0-3b0d-a5f3-96065cd73107 | -11.6744 | -64.9793 | 2024-10-03 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8fcdec9c-b504-333b-b528-3d29467171d8 | -12.4227 | -62.9999 | 2024-10-03 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 960f2f58-273d-331c-b5a9-b9661e253709 | -12.4228 | -62.9807 | 2024-10-03 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 115.0 |
| dfb0ad2e-601e-3138-8e06-59b228dab548 | -12.404 | -62.9817 | 2024-10-03 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 184.5 |
| ba45f4c6-4304-3200-94de-b7ca6da6b578 | -12.4038 | -63.0009 | 2024-10-03 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 190.2 |
| 37479620-e7fb-3a2c-a5cd-c6c426530cc9 | -12.3851 | -62.9828 | 2024-10-03 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 9468e664-c0f1-3a1b-875e-831bc6f522a6 | -12.6486 | -63.1022 | 2024-10-03 04:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| d1dab7c3-ea01-3ba4-9e05-ecd343c14178 | -13.0402 | -51.1432 | 2024-10-03 04:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 3b3259ce-54fa-32a1-908d-886555e05d7e | -12.8999 | -62.4527 | 2024-10-03 04:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 9aa6f826-0a00-3668-88af-e1a744444b48 | -12.8998 | -62.472 | 2024-10-03 04:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 0c73d358-9d49-3fe9-ad9e-7699c75d1009 | -12.8996 | -62.4913 | 2024-10-03 04:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 3231e67c-5d32-3b48-9774-f8262326f55f | -13.0406 | -51.1218 | 2024-10-03 04:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 8a3b41fd-c057-32b7-bb88-6e890896bcb0 | -12.881 | -62.4538 | 2024-10-03 04:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 55c24a93-d3a0-3d0e-92e2-45064caed50a | -12.9741 | -62.6409 | 2024-10-03 04:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 2c968491-433b-3324-a06b-638ee78e43b9 | -13.0975 | -51.1575 | 2024-10-03 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 711831ce-90ba-30b0-9f75-05310f1b485d | -13.0594 | -51.1409 | 2024-10-03 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a1a4f18a-89b4-3fee-a09e-6f0f8a4429a1 | -13.0783 | -51.1599 | 2024-10-03 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 132.2 |
| f4b9e64a-a6fc-3026-b9d8-e80edfcabc49 | -13.5198 | -51.1252 | 2024-10-03 04:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 0e4d10ff-23c3-3889-b41f-f674b7813561 | -13.5195 | -51.1467 | 2024-10-03 04:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| a138a471-5ce5-3a81-82de-3f544b0ca02d | -13.5387 | -51.1442 | 2024-10-03 04:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| c620abd6-e2f9-3ce2-9400-f9948d640806 | -16.5585 | -58.2204 | 2024-10-03 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 200.1 |
| 91372cf8-75e8-36dd-9a83-a3b635389168 | -16.5783 | -58.198 | 2024-10-03 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 02897613-59ad-3eef-a0bf-88bf06d915b3 | -16.578 | -58.2183 | 2024-10-03 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| ae025f6f-46f5-3d4d-85c3-2c570ba37a41 | -16.5588 | -58.2001 | 2024-10-03 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 186.7 |
| 66f376e5-35cc-3365-82bd-008750effe1c | -16.539 | -58.2225 | 2024-10-03 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 27196ca2-6c12-33ad-8048-33bd9a1daf5b | -16.5393 | -58.2022 | 2024-10-03 04:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.7 |
| 7fd67916-144e-3c33-b5df-b352099056d3 | -19.0344 | -43.1944 | 2024-10-03 04:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.3 |
| 94081b22-550e-35d6-bd42-b4e8425b0877 | -11.27876 | -43.39314 | 2024-10-03 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f018ddc7-b13d-3821-99d2-35af3e2b0f04 | -11.27809 | -43.39774 | 2024-10-03 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| efa20bb8-c9c1-3a42-b9a0-f67aba1fdcfd | -11.275 | -43.39258 | 2024-10-03 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e967917c-c300-39e8-9d3c-dbb04de7a85e | -9.15238 | -43.15795 | 2024-10-03 04:27:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5806c629-a061-363c-99e3-d94bcc5a5e7e | -12.34991 | -38.06652 | 2024-10-03 04:27:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fb6d09c6-49cc-3876-9622-921b89382cd8 | -12.34447 | -38.06584 | 2024-10-03 04:27:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| daf74c78-aff1-309a-a1ba-2a81a66f0559 | -12.34404 | -38.0694 | 2024-10-03 04:27:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 418b7332-20a9-3584-a159-e8045b959324 | -15.67723 | -39.21688 | 2024-10-03 04:27:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9c36ad12-89a9-39cb-9879-b535647a7797 | -9.15054 | -43.16 | 2024-10-03 04:27:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 203d59b6-78d0-32f9-b56a-aa5a0d5da1b9 | -11.27433 | -43.39718 | 2024-10-03 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90d44312-5790-3839-85a1-70555e6161cf | -9.01869 | -40.26331 | 2024-10-03 04:27:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 212445fe-7a61-32ad-9bad-4124037d8f9a | -14.20833 | -42.01735 | 2024-10-03 04:27:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b561bde-942c-3410-a762-2ab398347faa | -14.20048 | -42.07802 | 2024-10-03 04:27:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 12837046-05f7-3dcd-b4bc-0d59eaa6ae77 | -15.0796 | -41.93737 | 2024-10-03 04:27:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a5f5f08e-f398-332e-968a-8c0e0d666280 | -15.51539 | -42.23926 | 2024-10-03 04:27:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bd4b09c-4aa3-30a1-b25a-c4c6e5bb56cf | -15.43989 | -41.14309 | 2024-10-03 04:27:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4c4655ee-7cf0-3595-912c-1f1e37b99d31 | -15.43927 | -41.14802 | 2024-10-03 04:27:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9a8557a3-9d14-3aff-8897-b3db1c3b3a91 | -11.26923 | -43.40583 | 2024-10-03 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78baf683-7909-3511-b452-8e78984708b4 | -8.43922 | -41.92879 | 2024-10-03 04:27:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 44d7acfe-2251-3237-951b-54ca3a2bc5cd | -8.43849 | -41.93386 | 2024-10-03 04:27:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05f0ebec-ba72-30d0-98ce-fc1172585b2a | -8.43376 | -41.93858 | 2024-10-03 04:27:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d6bb7ad6-3796-350b-b5c8-43a2b5633e09 | -8.43302 | -41.94364 | 2024-10-03 04:27:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8a0d8944-e23b-35b0-93f8-50bd0040ae48 | -8.42977 | -41.93824 | 2024-10-03 04:27:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 785f5724-6fdc-3dff-9599-bc5a2743ade7 | -8.42905 | -41.94324 | 2024-10-03 04:27:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 76984026-00ae-3679-9b8c-a532d68f0685 | -8.37608 | -41.86106 | 2024-10-03 04:27:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 34cd232b-dfa8-384d-8c9b-3306800130b5 | -10.23694 | -42.3869 | 2024-10-03 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6cb739fd-6821-3cde-be91-563c3f827bc0 | -14.341 | -42.34989 | 2024-10-03 04:27:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1458fdd5-77ed-33d7-81de-12d63d8c7131 | -14.75855 | -42.42104 | 2024-10-03 04:27:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ca5ad8bd-35c0-3483-bfa3-497f2ee68f39 | -15.23769 | -43.33704 | 2024-10-03 04:27:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f0a9c1b3-58cd-346e-bb7b-089f3da05817 | -15.23372 | -43.33645 | 2024-10-03 04:27:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7f188d67-7fc8-3f1c-9526-6b5f10cd9459 | -9.19407 | -58.18674 | 2024-10-03 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b995806-1037-3e03-98e3-35c5e9f1ea8f | -9.1932 | -58.19132 | 2024-10-03 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 270eecd3-cabc-315a-a749-0a00a313810f | -9.18801 | -58.18573 | 2024-10-03 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60a877f2-5c07-3651-8673-8d9424853d8f | -9.16823 | -59.36921 | 2024-10-03 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a1ac15f-f8aa-394c-9afe-66a6c4bc461d | -9.16717 | -59.37463 | 2024-10-03 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b800c5fa-23b8-3e36-996c-7c899b485760 | -9.1661 | -59.38011 | 2024-10-03 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23e3b41c-6033-32e2-8f51-311c23f20c47 | -9.16502 | -59.38563 | 2024-10-03 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4eed4b29-53e0-337e-a53f-5ae3013b6b94 | -9.16066 | -59.37348 | 2024-10-03 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfb4f4af-4f4d-3461-90d3-4b8feca3d8f0 | -9.02555 | -58.89574 | 2024-10-03 04:27:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85fb1f20-debe-3e96-9323-f2c2897df0fe | -10.7221 | -58.52405 | 2024-10-03 04:27:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4f9a13c-4bec-3b92-818a-d903a03e1dfb | -10.70463 | -58.54924 | 2024-10-03 04:27:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b5b0c14-dec4-3881-b01a-a04abc06661e | -10.70371 | -58.55384 | 2024-10-03 04:27:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cb848e2-1fae-315e-a735-7e11b97f899d | -10.70279 | -58.5585 | 2024-10-03 04:27:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad40224c-fb6c-3a6e-a39e-1d234b29dfc3 | -10.70186 | -58.5632 | 2024-10-03 04:27:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6e842a7-fd1c-36cf-8efb-a9fa96a32f8d | -10.70094 | -58.56784 | 2024-10-03 04:27:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 159bd971-1ea6-341d-bd34-15aff277010a | -10.69841 | -58.54066 | 2024-10-03 04:27:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02d9c1fe-f0e0-3925-a0c5-cbf6d4afa8c6 | -10.69438 | -58.53788 | 2024-10-03 04:27:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d1566cf-b079-37c9-a022-8a1d48719aec | -10.69351 | -58.54222 | 2024-10-03 04:27:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README87.md)
