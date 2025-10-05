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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe18bd81-ad7f-3471-98f2-3364d781b0a2 | -16.01728 | -50.9568 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e375bdc5-1740-383d-8a9e-c0ebba3405d1 | -19.83718 | -46.51852 | 2025-10-05 04:49:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6e7906a-858a-3e6e-97cf-6aef17320f0b | -17.95833 | -57.5687 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bc40f7d5-dd8d-3281-83f5-51f06a001b47 | -14.45068 | -46.10038 | 2025-10-05 04:49:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6525592-2fab-33fe-9ce2-607570180932 | -14.01131 | -48.20476 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 183bdaea-5f88-37ae-b144-d5352155b75d | -15.55361 | -49.27671 | 2025-10-05 04:49:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca5086ea-60a8-362b-bca0-6f99e09040dd | -14.65624 | -48.34781 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb3d4aa1-3d91-3b68-891a-35bdce63f2ec | -17.96766 | -57.58064 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 08335076-85de-3cb8-890e-1001d772634d | -20.77619 | -49.38519 | 2025-10-05 04:51:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb1cd463-1bad-38d0-b1db-a336a576e4d6 | -23.43751 | -45.4719 | 2025-10-05 04:51:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 14a1f3b7-e8a4-3567-84e4-799a28cbafdf | -22.368 | -46.8835 | 2025-10-05 04:51:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c66b3383-4602-36c2-95e0-8dab6e06411f | -21.82127 | -47.38869 | 2025-10-05 04:51:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ca0b4923-55ad-3a66-aecd-2e985b8130b7 | -21.16737 | -44.27249 | 2025-10-05 04:51:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 09433388-9415-30fa-9e91-a2724ffe57b0 | -20.7341 | -49.61936 | 2025-10-05 04:51:00 | NOAA-21 | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5bf90900-5380-3e43-bb81-b25a6c58bbb3 | -22.15643 | -50.02135 | 2025-10-05 04:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0c165883-1ded-39b6-bfa1-36486b757bd4 | -22.10541 | -46.96814 | 2025-10-05 04:51:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1661c9a0-9c6a-3fc4-af7e-aef6f0e33b49 | -22.1007 | -46.96753 | 2025-10-05 04:51:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ead92ccc-b27a-3727-8c14-610c12b5d950 | -23.57008 | -45.97433 | 2025-10-05 04:51:00 | NOAA-21 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 58d1582e-29f6-39c6-9776-614c721b235e | -20.3251 | -47.73267 | 2025-10-05 04:51:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 924ebed1-6bd6-3567-afaa-899188f2e559 | -23.44248 | -45.47569 | 2025-10-05 04:51:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0b2db26e-64bd-38fd-8269-99778570c979 | -22.10012 | -46.97283 | 2025-10-05 04:51:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 947effbb-f5ea-3761-8221-4f4989206993 | -21.82533 | -47.39381 | 2025-10-05 04:51:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c0b5c419-17a2-3f87-8724-9d1e21d6eab0 | -21.58076 | -48.36082 | 2025-10-05 04:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd9f4532-7289-3702-a3fd-9010d6aa403f | -22.48168 | -46.81534 | 2025-10-05 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e43c4b5-93e5-33da-8829-1dcf2300b60a | -23.43717 | -45.47543 | 2025-10-05 04:51:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| acd0b759-7ccf-341d-8fba-558b3001e7cc | -21.93226 | -46.59479 | 2025-10-05 04:51:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6df4f0bc-b411-3e13-ac82-6d593fc91ebc | -23.02052 | -46.24952 | 2025-10-05 04:51:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cdaa6ea5-230c-312b-8a1b-7f8159b5e0ae | -20.55897 | -54.65749 | 2025-10-05 04:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08cecb8c-ee28-3d80-a6a7-bd1327ed15c9 | -20.51489 | -43.92573 | 2025-10-05 04:51:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 22a802b8-0a15-3c18-ba0d-5884583b1129 | -23.44199 | -45.47426 | 2025-10-05 04:51:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 122ae554-872f-365c-b97b-ec1ce1c6dde2 | -22.28687 | -46.72811 | 2025-10-05 04:51:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 129ff162-c32e-3644-b7f7-6ffe103af6ef | -23.39059 | -46.80156 | 2025-10-05 04:51:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5b732f3b-7182-3907-b4d4-37f2fb248b98 | -20.32564 | -47.7342 | 2025-10-05 04:51:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa570b01-f62a-3abf-b537-b47ee8d682f3 | -21.68482 | -48.4253 | 2025-10-05 04:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 75.3 |
| a930d563-7048-3e93-ab11-55e6c14846ac | -22.92773 | -45.07894 | 2025-10-05 04:51:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 848a8a2d-13e5-3469-91e2-1131630653e8 | -21.58125 | -48.35662 | 2025-10-05 04:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17a6c0fb-5cc3-334b-91c8-26e7fe5b28d2 | -20.80309 | -51.65574 | 2025-10-05 04:51:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7ce715cc-1008-3368-8dc3-b5c60f6470fd | -22.10483 | -46.97347 | 2025-10-05 04:51:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be5d1600-47d7-3f70-a731-96ea18810a31 | -22.37178 | -50.02365 | 2025-10-05 04:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4e685014-652f-35af-a4cf-96b83ec7d19d | -23.57038 | -45.97115 | 2025-10-05 04:51:00 | NOAA-21 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 665759c0-416f-304b-8ad8-b99d371bd458 | -21.82584 | -47.38924 | 2025-10-05 04:51:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| d9d4419f-4073-3c2f-8e62-6b85e45d3843 | -21.68959 | -48.42156 | 2025-10-05 04:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7391ed2e-e9e3-32fd-9af3-616d6403af18 | -21.82481 | -47.39847 | 2025-10-05 04:51:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 58d23977-5a12-32ee-9a64-13cae4305b85 | -23.44281 | -45.4723 | 2025-10-05 04:51:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5f8e146a-bf05-3c77-bfe4-09c68bdd7e1c | -20.77892 | -49.3863 | 2025-10-05 04:51:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dae1a8a-e184-379e-8cbf-96dda870f68d | -20.72988 | -49.61784 | 2025-10-05 04:51:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2fb14f3b-8fdf-3f07-bf72-301b34536fe4 | -20.50925 | -43.92526 | 2025-10-05 04:51:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1e944c60-eeba-34c2-bb4f-a035a64f0c52 | -22.36859 | -46.8779 | 2025-10-05 04:51:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e57dc3f4-f884-3116-9ebd-107c37347b89 | -21.82937 | -47.39908 | 2025-10-05 04:51:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 95b7c02a-24a4-3986-b441-40ace2d06c53 | -21.69333 | -48.42661 | 2025-10-05 04:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 62125b63-a8cc-3896-9d96-232a33754e74 | -22.49954 | -46.03461 | 2025-10-05 04:51:00 | NOAA-21 | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| de1fbd21-8c11-3529-af36-d11027cfceb7 | 4.34769 | -59.78105 | 2025-10-05 05:10:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a736bda-1d15-348d-949e-03ab34c559f8 | -3.81196 | -51.29332 | 2025-10-05 05:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 109c8f18-d315-317c-b3b0-945e55457839 | -3.78525 | -43.58422 | 2025-10-05 05:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b602b2d2-ce5f-31ba-828a-996ec44a11ae | -2.68916 | -48.38994 | 2025-10-05 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 59e6cfad-3583-3c1d-9f2d-4d64358b45f7 | -0.90974 | -47.55085 | 2025-10-05 05:12:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75096381-2e28-3718-afee-8c7fb15aabd9 | -3.84136 | -44.55294 | 2025-10-05 05:12:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd454a20-a5b1-3bbb-9868-016da02efb14 | -2.693 | -54.76606 | 2025-10-05 05:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b7c3435-1fd8-3ca7-98e6-925b3f5a0a04 | -2.60481 | -49.40417 | 2025-10-05 05:12:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 584843d0-dc4d-3e86-bcad-b0da4a2bb7b9 | -2.89837 | -50.73013 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51b18eda-26e0-328f-9e09-85f42a24a990 | -4.63753 | -43.18534 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0e78ed5b-65ec-3e61-bb7f-a5c64a639204 | -4.31879 | -48.09206 | 2025-10-05 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e19a953d-e7ee-3187-b0a2-81355d1c48ed | -2.69243 | -54.76974 | 2025-10-05 05:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53aa468b-31b7-3c93-b618-77ed617cd4b7 | -4.4439 | -43.23835 | 2025-10-05 05:12:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 422df042-5b2e-3b58-9fb0-4473b78bd38b | -4.64472 | -43.18636 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a96aa223-1dac-375a-bc12-31e25e6be865 | -4.314 | -48.08812 | 2025-10-05 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54987029-39ca-3fa0-9c1a-8e9618ddc824 | -3.81456 | -51.07558 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3e31bfd3-02d9-3c0a-9e8a-4f3d3cb24881 | -3.60878 | -51.04226 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df538cb4-c2bd-3c07-9e3e-d1e1ea4c213a | 1.00082 | -51.26863 | 2025-10-05 05:12:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b25905b0-9ea2-3b53-92d8-9bf2120acc26 | -4.63874 | -43.18829 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| c8622cbc-3245-314e-8404-1828eb4a5894 | -4.63056 | -43.19431 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6a63edd3-2197-3aee-b9c6-6eacca227ed7 | -3.80932 | -51.7702 | 2025-10-05 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 078154a6-a39a-3cd9-b836-dff729fccfdd | -1.75134 | -54.14309 | 2025-10-05 05:12:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f43ef11-860b-3ffb-9b50-69178d56821d | -2.89715 | -50.73817 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bbbd7f3-a3a9-3634-9288-a1b5c5e4efb3 | -4.27148 | -46.74065 | 2025-10-05 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dfa1e61-7eb2-3bac-b6fc-dd0a8ec862cf | -3.77143 | -51.94046 | 2025-10-05 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bbd5ba3-52ba-3ccc-a8b9-9a8614fc8321 | -0.90503 | -47.54689 | 2025-10-05 05:12:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a99ad6f-308e-3d74-84d3-55cf6b0d4087 | -2.89929 | -48.07519 | 2025-10-05 05:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 645d5d92-3aa7-3c6d-ab4c-f2a92f0b1a2f | -4.63033 | -43.1843 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ae53d561-927a-343d-a490-decc6fa3b7ec | -2.88978 | -50.7288 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be0774ba-b848-3b4d-bc4f-2296af6b5d20 | -2.1442 | -53.63736 | 2025-10-05 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cf1f181-02a3-30f9-ae6b-a38efd0c238e | -2.6095 | -49.40485 | 2025-10-05 05:12:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f52abe5-e573-31c7-ab8c-ad6c6a7b3545 | -3.09098 | -47.79199 | 2025-10-05 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb75a34d-bed3-3257-bbee-02a08f6bb379 | -3.81557 | -51.29778 | 2025-10-05 05:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e866dbe-5b62-3ddc-ab1e-ec1f93f58c0d | -3.39676 | -50.27447 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa94cb2e-ccba-3793-bc9d-c8999662c18c | -3.81029 | -51.07506 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6bc27a22-cc05-333c-89dd-9c24f2ce9189 | -3.61301 | -51.04303 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d972452-1931-3a9f-8d16-248c3385df8e | -2.90267 | -50.73079 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9216f1e9-d401-3d91-86f7-687da9238bcb | -4.31927 | -48.08885 | 2025-10-05 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fd4cfcd6-3197-392f-9ca5-4749c55410c6 | -2.10933 | -52.76786 | 2025-10-05 05:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 219f8ecb-331a-317a-a0a8-c7e6ae42f231 | -3.60937 | -51.0383 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43526168-6f6b-3ca5-bee1-dfa97861dc4c | -4.63155 | -43.18722 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dd58534c-ab11-3f54-8c57-6d3ded3e7857 | -2.52001 | -51.93398 | 2025-10-05 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22ce3ca9-66c5-3012-8eb6-87a09749cf1c | -4.2709 | -46.7446 | 2025-10-05 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e1754736-c0b8-3233-8fbd-52b991bade86 | -4.26979 | -46.75222 | 2025-10-05 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 682d7afb-30ad-3563-a614-69c980d0bdbe | -2.89776 | -50.73415 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c357daba-1e63-310f-89e3-272d28af5441 | -2.14777 | -53.63795 | 2025-10-05 05:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e37cb8a5-40b1-3c99-81bc-6ccdd726f8c0 | -4.45206 | -43.23236 | 2025-10-05 05:12:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e80e8ac3-6dd9-334b-ae91-56f06547bfa6 | -3.81616 | -51.29394 | 2025-10-05 05:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 747b7bbf-0a03-3a22-89fd-0d564cac4901 | -4.25295 | -48.5662 | 2025-10-05 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README116.md)
