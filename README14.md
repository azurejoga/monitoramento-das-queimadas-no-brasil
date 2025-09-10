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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e54d9f1-287a-352b-81c4-33e37e65875f | -20.0198 | -47.6225 | 2025-09-10 03:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 633688e2-7bfa-3aa6-85bc-5bfe6721981f | -5.5892 | -45.0278 | 2025-09-10 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b8217fba-611d-3bf5-8bee-dedcbc3c63bb | -6.2595 | -43.4129 | 2025-09-10 03:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| daae79ad-a1c1-37b6-b2f7-7764af7c6fb2 | -8.0414 | -48.6873 | 2025-09-10 03:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 182.9 |
| e6f16c93-ea25-32f4-924b-259423d177c9 | -6.8521 | -47.9143 | 2025-09-10 03:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 2cff63d8-bf6a-3214-b7bd-aff0cf278c5f | -8.0604 | -48.664 | 2025-09-10 03:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 777f3ac0-5ed8-3531-8c7b-374c8c7c4913 | -8.0602 | -48.6856 | 2025-09-10 03:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 91.8 |
| ea421cc5-91b8-35c0-b77c-15d6684a87d9 | -11.4657 | -43.6195 | 2025-09-10 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| dcd947cb-c358-3f50-bcef-6d8b95df05b4 | -20.0198 | -47.6225 | 2025-09-10 03:10:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 3ef8a1f8-7d63-3ea5-a213-dc4d1c3b0033 | -6.8519 | -47.9361 | 2025-09-10 03:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 55bd065d-4e58-38a0-85d5-19deac9c6bc7 | -8.0416 | -48.6656 | 2025-09-10 03:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 108.1 |
| f1616edc-33c4-3680-9218-0fa02707579c | -8.0416 | -48.6656 | 2025-09-10 03:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 86.7 |
| f9d8dc91-b0fb-36f8-8acf-649060cf1a33 | -6.8519 | -47.9361 | 2025-09-10 03:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 05f6155a-74e1-3d06-8b38-8d61f24045d0 | -18.0418 | -47.1277 | 2025-09-10 03:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 1e17b4b9-5e53-3ea4-b7cc-034adee910ca | -11.4657 | -43.6195 | 2025-09-10 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| bf32446f-14ce-39f7-9216-48e555422153 | -6.8521 | -47.9143 | 2025-09-10 03:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 51a837b9-d479-3143-905a-138c538facb6 | -8.0602 | -48.6856 | 2025-09-10 03:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 201.4 |
| 2733ebe1-2e9d-3d30-909f-d15135113c56 | -20.4756 | -43.9435 | 2025-09-10 03:20:00 | GOES-19 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 157.6 |
| 2e979752-585e-3aeb-b5c7-0b56e1eb7077 | -8.0604 | -48.664 | 2025-09-10 03:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 344028f5-577b-3210-8443-a89163575f0b | -8.0414 | -48.6873 | 2025-09-10 03:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 005c59a1-513c-3533-b006-9cc09c7b0dc5 | -5.67188 | -43.34646 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 328bded3-f4ff-370d-80e5-8b01ade8e530 | -5.67858 | -43.35584 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86245954-ef24-3836-a56f-e9bd6245bd1a | -3.96627 | -43.23959 | 2025-09-10 03:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0eef4483-8b47-3875-a079-132a2becd283 | -6.19104 | -43.50666 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fd8cdae1-1cd2-3890-8102-23bf915ca16b | -5.66767 | -43.90496 | 2025-09-10 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e33ee57-223e-3036-8255-27f7080bc31d | -6.25009 | -43.41615 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| df930ca8-47ee-35f6-9669-ceb099c614c8 | -5.67177 | -43.35465 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41fb5dbc-7e52-3036-80bb-7c01485344e0 | -6.18873 | -41.05175 | 2025-09-10 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 45ca248a-c255-3273-a706-d982f4abd267 | -6.2079 | -43.37 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6331d28a-638d-3dc6-834d-147e8c78f941 | -6.17035 | -41.05292 | 2025-09-10 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c79ee8b-d5e8-312b-80ee-350304d4b525 | -5.66375 | -43.35992 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 84b077ad-8557-3dcb-9a9f-d33dc5fb431d | -6.48026 | -41.75484 | 2025-09-10 03:21:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c1849875-44f4-3a39-be5a-0f3bdced49ad | -6.44186 | -44.06405 | 2025-09-10 03:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 89b00ee7-3241-3062-b2c2-2ab06604d6d3 | -7.54813 | -44.65922 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 87cd7955-55d1-3f11-bcf3-a05d2630f908 | -6.20968 | -43.37062 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb3b24f7-3eea-3b1c-b649-1c1f2d0fa0bc | -5.67987 | -43.34109 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b1df706-ab53-3040-a9af-40f39836ded3 | -6.06062 | -43.13684 | 2025-09-10 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b53abd98-fec8-3f3f-870c-539b375a9314 | -5.79302 | -43.89346 | 2025-09-10 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94d5410e-1379-3339-b677-cf7f3d6d03a3 | -5.64397 | -43.92902 | 2025-09-10 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 61cd14c0-ce9c-342a-9ce6-d2d5c37b2829 | -4.54434 | -43.30108 | 2025-09-10 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecf79858-7aa1-3546-b643-b9052560a772 | -6.25228 | -43.40435 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 417df7b7-bd4d-3543-83b6-e0b94cc7b952 | -7.55101 | -44.66467 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 91612503-cc39-3b36-85d6-0e4ac0635d1a | -7.94016 | -44.85706 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b064e44e-1bea-3bd9-b55f-24d99a0b025d | -4.5495 | -37.78775 | 2025-09-10 03:21:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fcd8798e-2786-31a6-a2d7-dcfba9f896bf | -6.21468 | -43.37111 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3d8fa4a-60ad-3f3e-bc23-aa29e1c22096 | -6.39852 | -43.50193 | 2025-09-10 03:21:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09fae7d8-27a2-3505-9706-df7cf4e0c192 | -4.09694 | -41.58009 | 2025-09-10 03:21:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 95e52747-a607-39ff-9f0a-1c8a7271e177 | -5.67649 | -43.35986 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b98bb079-3c1e-3706-8c48-c0cde4add6a0 | -6.05221 | -43.12789 | 2025-09-10 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3d75324b-3b14-3bab-a099-9df52fdeedf1 | -6.20378 | -43.50865 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22a75426-47a9-3bb6-b6ab-5a81ec970343 | -5.67406 | -43.34242 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b12b074-9793-3b41-a5ae-c7596a0bf96b | -5.53424 | -42.66067 | 2025-09-10 03:21:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c5f8586b-dfb2-3724-9354-a261593b7c4e | -6.05324 | -43.12214 | 2025-09-10 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 23cb4bb2-69b1-3ae1-867b-3b768bf6373f | -6.17547 | -41.05821 | 2025-09-10 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c770a594-c246-3dd4-adb5-7e39e519c93b | -6.55821 | -43.15167 | 2025-09-10 03:21:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ace0cd6-cbbf-39d3-9632-db9822fe13af | -5.68666 | -43.34233 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bbb85e6-cfff-3f3d-bf4e-f36e758ab8c2 | -6.24549 | -43.40328 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6858eebc-565d-3ca8-a5e3-5b7e13b781b7 | -7.25842 | -44.46692 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cab2818-344c-363f-a43d-453df9615cab | -4.09068 | -41.57897 | 2025-09-10 03:21:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 967523b8-c86e-3acf-a7f2-7a9b134608e8 | -7.93537 | -44.85833 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 67c1ca06-a4e3-3d0e-9abf-794f8c3914b5 | -6.56478 | -43.15316 | 2025-09-10 03:21:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74e80a82-e4b6-314c-b956-b749aae4e480 | -6.18286 | -41.05071 | 2025-09-10 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e13ebea1-33fa-3772-b890-4b3ddf10d3e6 | -7.93282 | -44.85668 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d1eaf3c2-c5cd-3a7f-9220-67112baff8c0 | -5.6774 | -43.36212 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f17cafb-81fe-34c3-9b02-2b58b1f1d446 | -5.63827 | -43.92047 | 2025-09-10 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 15108898-f0bf-39bb-a5a2-474586db7365 | -6.31298 | -43.41638 | 2025-09-10 03:21:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7c34556-7959-37e1-b12d-7df1bbe43e12 | -6.19693 | -43.50761 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26c7b4ca-07a3-3eb9-bf58-a156a9afb626 | -6.56127 | -43.14964 | 2025-09-10 03:21:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eef4953c-ff73-3dbd-85f7-746039dac24b | -5.67972 | -43.3497 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22c0b987-0c12-3dbe-8c8d-de873b244035 | -4.09345 | -41.57898 | 2025-09-10 03:21:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d25402ad-1ff9-337b-9c76-078492ca71a0 | -6.25678 | -43.4178 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| ff96849c-bcf2-31c5-9a17-e254b734c11b | -5.6762 | -43.3686 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5db8c5b-d002-34b7-83c3-99ca3baf52e2 | -7.41973 | -40.08234 | 2025-09-10 03:21:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f5f7b8f-49ee-3452-aae1-146525ce23e3 | -7.55223 | -44.65832 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d615e387-9cc7-3d06-8ebc-92a40a532300 | -3.96516 | -43.24592 | 2025-09-10 03:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca6f0136-2c71-3c83-bef0-54f04aaae18e | -6.47937 | -41.7598 | 2025-09-10 03:21:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0544ac3-919a-36fa-b420-e7babbf812e1 | -5.68089 | -43.34343 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 187fc754-6016-33fa-af89-6b64dcdb445e | -4.09261 | -41.58394 | 2025-09-10 03:21:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8712f512-d4ea-3ad1-b846-4d16198d767e | -6.17085 | -43.38164 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0a1bc04-3e10-384b-a208-a86b7faa83b9 | -5.64519 | -43.92238 | 2025-09-10 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a8e3322-86fe-3407-b51f-4a5d163d2f62 | -6.17623 | -41.05396 | 2025-09-10 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2754187d-b061-3306-ab8d-c0894c350985 | -5.67534 | -43.36625 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1fddf2c1-2d73-3444-9b89-23f95cd78cf8 | -6.19785 | -43.50785 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4bb74080-e8cc-30e8-91ec-3e0e18cd4a54 | -5.663 | -43.90438 | 2025-09-10 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1aba3d6e-b7c9-3181-b217-ad5c656c1719 | -6.44301 | -44.05798 | 2025-09-10 03:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6d5ce619-cbf2-30f5-93db-dec9538d0e89 | -5.66502 | -43.34554 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f5f5dbf-910f-3c9f-9f9c-d377befe0af4 | -6.17112 | -41.04859 | 2025-09-10 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a05c3ed4-37b3-3bc1-ad29-7630c0ed2012 | -6.2512 | -43.41015 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d5b778dd-0522-35c5-b02d-60b27d43bbcb | -6.1949 | -41.04215 | 2025-09-10 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 673ec5d3-e56f-39b7-bf33-19c123686ca4 | -5.93212 | -42.78642 | 2025-09-10 03:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 465710c9-a709-35dd-99e5-86ed646c1f53 | -6.2444 | -43.40915 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 855b2caa-938c-3e30-b301-7292fedb9b7a | -5.67761 | -43.35363 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 21e6e5cf-6c29-31fc-88aa-329ed530e5b6 | -6.31559 | -43.4132 | 2025-09-10 03:21:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b8885c9-aae3-3a70-99da-9ef3ea51c0a9 | -6.25902 | -43.40571 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3aad13e5-efdf-353b-a20b-a92cf5d01fb4 | -7.54506 | -44.65722 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5c082968-ab85-3cfe-968f-e92e6c99f319 | -5.67079 | -43.35249 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5dcce49e-41d3-3dd5-9c79-ff86d9acaef3 | -7.75308 | -34.89949 | 2025-09-10 03:21:00 | NOAA-20 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4c98793f-93ac-376c-9d4a-783c957d8499 | -7.42036 | -40.07883 | 2025-09-10 03:21:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 60c1106a-c982-3628-9632-1b911f0ddb25 | -6.19012 | -43.50636 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fb98c045-f41c-32e5-ba60-5cf9b55b4929 | -6.25565 | -43.42392 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |


[Clique aqui para ver as próximas entradas](README15.md)
