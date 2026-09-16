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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e668fb6-090c-339a-9cd9-5169afa3012c | -6.27154 | -55.28138 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3d6e9ede-9e16-3bee-b898-78e1b4e06657 | -9.1043 | -45.73104 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2642ea19-aae0-316d-b2bb-61e18f5bf2f1 | -6.35008 | -62.68631 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3d8eea4c-e160-3f18-8de9-06680f0dedda | -6.33952 | -62.68754 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c7333588-c7d1-3949-ab8d-3bd61f1d41df | -2.86843 | -49.63227 | 2026-09-16 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fee96e7c-8e0b-3107-b44a-24a2fc790086 | -7.06253 | -46.74632 | 2026-09-16 04:57:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62c8a3d1-54f4-3a24-a712-3262232ebf96 | -5.13665 | -55.94087 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2093aab6-951c-3822-a65c-40f663835d7c | -7.26275 | -46.67377 | 2026-09-16 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8968a293-752b-3181-be1e-fa6b7bacd55f | -9.55483 | -45.42031 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a818f26f-51ad-3fcf-856f-e261843c9af5 | -2.91083 | -50.43035 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd41440d-7dbc-3b03-b55f-e27925515f55 | -4.60509 | -55.70734 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9030a3e4-f0fe-33b4-a28a-1ef00529aabb | -6.33976 | -62.68901 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 172276b8-5d8f-31d8-9b56-523f97d4a539 | -5.14464 | -55.93459 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 25c533bb-e707-3092-acd4-3f94cf300d45 | -2.90127 | -50.42039 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 932ced32-9c95-347d-84bc-46d8e05e2c87 | -6.39437 | -44.0592 | 2026-09-16 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25ded6c3-381a-310a-85d6-7cfbeb926d1e | -6.33235 | -60.00224 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1d4a030-1bc8-3c76-adb9-1b24e92bf476 | -4.57129 | -54.91126 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf15ef48-e5d8-302c-83aa-db554857086c | -4.54858 | -54.9256 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0b1f3fe-9c66-3c4c-adc1-9d50ab10254a | -3.06312 | -51.27712 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8289d42b-89bd-3a98-af2a-68a228f84cf2 | -8.84161 | -44.90288 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2b54ff1-4dd8-3882-a3cc-55cfa4294b55 | -5.88425 | -52.08896 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d4d4a80-7689-3a01-a338-5bdbb2b6090e | -2.10412 | -52.0583 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6ad2a673-0e39-3a9d-bc69-edbb0f6f23c2 | -4.44172 | -55.51752 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 821ea2a1-ac57-335c-86b1-4d36dd91269b | -6.2721 | -55.27787 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24c901e2-3a59-38a7-8877-e51c61c853a9 | -2.10131 | -52.05423 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9af5975a-3358-3791-aeb6-9730ce2697c2 | -3.17553 | -61.11271 | 2026-09-16 04:57:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 41f4533e-2c61-3830-b93d-69d5a346f6fc | -3.615 | -49.86974 | 2026-09-16 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41a4f6c0-6c40-3257-8c14-9042fa699167 | -3.12044 | -61.41516 | 2026-09-16 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea6561e0-60e0-34c1-a0b9-da5b34598cf2 | -6.10104 | -53.54343 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d91a4864-e05d-36ff-9196-4d538fd1f1e8 | -7.33909 | -44.48553 | 2026-09-16 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 151311a3-0e33-3a0b-8345-c4e03f030865 | -2.99118 | -54.16153 | 2026-09-16 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7119720-9ace-3626-a3e2-4617d6bae5f9 | -2.89155 | -50.43589 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91e86de3-ebb0-3eb2-8a94-247b98fcb614 | -5.14373 | -47.6016 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07a569ce-8175-3437-9e19-a9f67879c3b7 | -3.3637 | -50.74192 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eafda9d-8cf1-3d05-85f2-76e774910ee1 | -2.55253 | -56.31796 | 2026-09-16 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 631f9152-1d9f-323e-b49e-219368eb739f | -9.49098 | -45.43412 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf65d250-6733-3cc5-9565-8291fd608d34 | -4.16838 | -55.84754 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 969ecb99-437a-3c6e-8343-c0b426c2a9cf | -5.90949 | -52.10381 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7955c29e-c81d-346f-89bb-8eeac95ffb7b | -4.09045 | -54.44017 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 967501dc-f88c-39ee-ba08-d2c900cf2666 | -2.9019 | -50.41624 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e54edd2d-c55d-37fc-a506-7340b437b5c3 | -4.36187 | -47.77981 | 2026-09-16 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 779ab97d-5342-3242-b0c0-ddf0f0078793 | -6.29373 | -55.29206 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9872de04-4adc-3e88-a1d0-ff9c1bb5b2b5 | -5.86016 | -52.03889 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b20af8d8-5f7e-373a-ae68-869ed3c72599 | -4.54913 | -54.92211 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 933c8b4b-062d-3bd6-a106-064aa242dc09 | -3.05685 | -46.92671 | 2026-09-16 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab26159a-a44b-31a0-ae29-166d89f5ece4 | -6.19019 | -44.03378 | 2026-09-16 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6193ed5b-52e5-333f-bc0c-e617ffcdaeef | -6.33523 | -62.68522 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ad2b1524-4f01-33ca-81e7-aaf89d93806d | -4.39457 | -55.44384 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 838e8586-52fc-37ca-bda0-5298e67994e8 | -9.48963 | -45.44449 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 742559f8-69f5-3cf8-acee-16459dd1b100 | -6.33045 | -60.01374 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eec8c11-19e9-3c42-8494-da3be223ab9e | -4.28666 | -48.03626 | 2026-09-16 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef382ef5-0464-3b18-8662-31a2855ae941 | -7.05951 | -59.22902 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34d87c79-f4b5-39f4-b068-4ade1ccb773a | -3.59015 | -58.53717 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a7e0ddb-257c-3fc7-8c66-49c06f4992bc | -5.14521 | -55.93094 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f804ae02-222d-3b0e-8f59-e353443d0a45 | -4.5142 | -54.97062 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eafcbd9-fbf9-370a-b9a5-2e8bab0e14e7 | -8.84593 | -44.89427 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ef6c064-25fe-39bb-93d7-091ffd9d6269 | -6.16314 | -55.71135 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6c89687-c291-3a25-93ef-e341c49c49ec | -5.11195 | -47.60153 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c3bcf54c-94f5-332e-a46f-fc028cd8ecc1 | -6.34905 | -62.69215 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e1776245-7778-3e26-b8d7-fbce3326de7a | -5.10432 | -47.6226 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a753785c-2243-38ba-bcfc-b939a7d1d7cf | -4.73391 | -55.73474 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6da0d6b1-80bd-3c28-bc67-1954501f1c5b | -6.15394 | -57.69894 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d8230c6-27a2-393d-a7d3-81f9ff45bdd0 | -1.95905 | -50.80687 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 424cf78e-3821-38af-9a78-3df4876452e2 | -3.17637 | -61.10763 | 2026-09-16 04:57:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b3613fe0-9f50-35a4-bd8b-d2ad33255ec9 | -2.10241 | -52.0471 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8044d731-142d-3b32-9a81-a8e58f5c738c | -7.15986 | -52.71285 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 477c3890-f50e-3877-8bf4-44eeb6a56763 | -3.55326 | -51.53207 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34cade58-e7e7-3394-a685-15676c577262 | -2.91037 | -50.40904 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69f4a19c-56af-3ead-a829-9f4a1f6fbb4c | -2.90613 | -50.41264 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c701d79-6aaa-3b59-98f9-65b18de63481 | -5.24551 | -59.98455 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c0c2c8c-57ea-3bfc-a667-573358c82db7 | -4.81423 | -42.88982 | 2026-09-16 04:57:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8c6d006d-d3dc-3bd2-93be-768ce8d4d06d | -7.87606 | -54.72842 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db756a4f-8946-3a0f-a6fe-2a7fdcbc82c5 | -4.54143 | -55.61906 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 061a91cb-2eac-32a9-8902-bc5830f45711 | -6.34699 | -62.7038 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3e8fe2f-e8b6-3d75-8ad9-45fdc9bc24e4 | -5.9969 | -52.10468 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d5c78e38-442d-3d48-8cb3-cefa2f60deb7 | -6.43451 | -55.60445 | 2026-09-16 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8895d0a8-775e-36d2-84b8-9b214e97403e | -3.37381 | -52.79846 | 2026-09-16 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0301b19d-011c-3380-ab78-56af2c2aa30a | -2.91146 | -50.4262 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 562619da-9a3c-3e0e-800c-724aa5c8f359 | -3.42612 | -58.23464 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a614967c-4a59-3950-a4c5-c20f44af034c | -2.91868 | -50.42729 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73efc9e4-b544-3fda-b243-eac94aee2784 | -4.52699 | -54.97615 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e642a054-3132-3c0a-9a4e-1fb029aa8358 | -4.46303 | -55.05644 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d164b8c-9ccf-3836-998a-246855493148 | -6.3345 | -62.68668 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 685265c1-6ee1-375a-bd68-cc3869608582 | -9.22692 | -46.70315 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94853e0f-11d0-3b35-bf9b-8263c9ad580d | -3.77464 | -51.87058 | 2026-09-16 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cffc7f6f-27e0-30be-b2a2-7a1a68518429 | -4.56796 | -54.91074 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dabc638d-e814-3dcf-bad2-2070cf40acc6 | -6.34299 | -62.69714 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 176864b0-85fb-3f2d-b6a8-8af2e6205249 | -6.26555 | -43.27892 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb61b226-cca7-3bb4-bb73-b7029b35da8d | -4.51531 | -54.96356 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc44ce7c-5e70-3551-a040-f8a987439550 | -3.81087 | -58.89734 | 2026-09-16 04:57:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 146973c0-7e60-3502-84d5-50cf9ad98d53 | -4.36008 | -47.7815 | 2026-09-16 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| aee676d9-7c0c-325e-b93b-915de691a072 | -5.1418 | -55.93045 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 025666a2-5fe8-3f9e-adf0-7724b6e2deb7 | -6.39318 | -44.06107 | 2026-09-16 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b75a0ac-21d0-3da3-9830-1f66f7419a28 | -5.6483 | -51.09543 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7c6935f-2bf8-32b3-8aa4-2f802241a4a0 | -5.13724 | -55.93721 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3bb8def-f0a5-3b85-a617-f13045b7d0e4 | -7.51304 | -47.56564 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2bbf59c-2555-3d6b-8789-d015e50777b8 | -4.17338 | -48.70986 | 2026-09-16 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 359a22dd-0b99-338b-888f-9c5a3da8da12 | -6.78996 | -48.65763 | 2026-09-16 04:57:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4648eca-31e8-38bd-8924-c7b43b83cc22 | -3.09481 | -51.29341 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60495ae8-72fc-3026-bec0-f6a41ae7fde9 | -6.66373 | -43.65033 | 2026-09-16 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README36.md)
