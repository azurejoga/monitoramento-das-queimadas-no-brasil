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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36e830df-5b7a-3f9f-a68b-a8ea430c9a84 | -4.6768 | -48.77407 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2ceeccd-6d62-31c8-844a-dea2eef90860 | -5.72833 | -41.98706 | 2024-11-10 04:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6795f4e8-74b7-3a76-8424-02ecbd6cd598 | -2.93185 | -49.36294 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 059c71ac-11c4-3167-a837-3001e80eeeb3 | -4.12541 | -46.11123 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72285d17-e1e1-36cd-8147-f6862356eac5 | -8.37977 | -44.14111 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8576a685-395a-3152-8ac8-40996a744a52 | -2.97861 | -50.30199 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0451870d-df3a-32d4-a0a4-79cdc7fae388 | -2.671 | -49.26117 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2db32ac2-278d-3d7a-abbe-c51b9d7f7705 | -4.11032 | -48.49793 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e16370e9-0643-3caa-ad3c-0c2c4e9f8ca7 | -3.29941 | -50.01799 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ac052a7-1c68-32d1-ab7f-fdef6067bed1 | -1.64408 | -54.44079 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abfc5724-d0d0-306e-9e67-d69252134eab | -2.92518 | -49.36189 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93bb0961-d3ca-3b0a-8406-b9ef890cdd57 | -2.83255 | -49.4588 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79e76c54-f84d-3314-aadf-4dec951d102e | -2.87134 | -50.40655 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c2dadcd7-6261-337e-abee-3e37675cb0fb | -5.63672 | -46.97333 | 2024-11-10 04:38:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57f2c866-65a8-32e7-9210-a9cdeb8fd306 | -3.08326 | -49.55849 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33777e12-1d8d-3bd5-9424-c98cd094c694 | -1.76483 | -53.75342 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 257c1fea-5f4f-3a88-a0e2-288bf28b5429 | -4.24151 | -43.82768 | 2024-11-10 04:38:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f85b6826-5dfc-3de4-9b8b-c58ba88c09e7 | -3.44134 | -50.09483 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 458da8ea-cd66-394c-b6b1-0dcb79736108 | -7.30866 | -55.30798 | 2024-11-10 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcc39f3e-4aed-35f9-8907-4026dc577522 | -8.39688 | -44.11184 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af024fbe-96f2-3e7d-8fa3-ef41fd5ecfbd | -3.97763 | -48.17917 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5c38f32-013e-3952-8931-93087ed6aac1 | -3.04294 | -49.54183 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ccc176fa-6791-3429-a76d-17607cf42019 | -3.95983 | -48.16216 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 366bb697-abf3-3723-b5e9-e10f6ea2f522 | -1.40469 | -55.45042 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03d2ee4c-b235-38e0-a0b2-24d523182db9 | -3.25943 | -48.74634 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 92e75dd5-c838-3200-a586-4042aac2eea9 | -3.96014 | -46.99173 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c89a9b8a-28d5-356f-b410-330f51eb56c0 | -3.24225 | -46.48885 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8433305a-f5da-3191-8688-5f57f6221dba | -4.13143 | -48.23873 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 252144f9-9fdb-3675-8988-20d3225a3c5a | -3.24917 | -46.48991 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21488718-7e02-3004-950a-c23cad39d692 | -2.95496 | -50.47206 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07bff9b5-b480-3798-a8d4-ea25ac7b30d4 | -1.75209 | -55.0379 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0df1c0d5-4ba6-375b-a1cd-a8ce4dc0fe14 | -2.19647 | -51.87472 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5a001772-bd7f-3f9f-98f4-d26462b5a25a | -3.21568 | -50.30521 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f9a1467-e5e3-353b-a0a8-3d95cb1aa3cc | -5.57039 | -43.97207 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 622768da-e8dd-32c0-aaf7-10825092fe61 | -3.9758 | -48.12548 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f4e43c8-b605-3a57-9526-7f122e927515 | -2.06665 | -51.40364 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65db943d-e960-3c44-80d6-49652c42c77d | -5.30738 | -46.23074 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28f3928e-6dbd-324e-ad10-aa75363498c5 | -3.14179 | -48.56933 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eab50e83-96dd-3116-aa1a-bdc5059e7f7e | -3.09046 | -50.23752 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d039fbfb-dc48-3f36-b658-9aa2ba8bf7cc | -2.87821 | -51.31537 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 592297d2-0e81-3ad6-8865-d053ca84fac2 | -2.08089 | -54.68291 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae85dea0-4e97-3877-9204-f3ae66eefc53 | -3.1391 | -49.12051 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f2ee750-529b-3ad4-9050-d2e0e8c0112a | -3.20381 | -46.49446 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c805dad8-1ef5-3189-aef5-7758bcb04763 | -3.44845 | -50.18092 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2ad932a-5045-30f8-81b9-ba204ef118d7 | -3.22938 | -50.2849 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2e0d89ed-6cf5-37c9-b8e4-94d07107fe5a | -2.88301 | -51.6664 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3663eb3-49ff-3324-b859-b552f443109a | -3.11259 | -51.29357 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc6fbf4b-c629-3658-9efc-c89ad2fce7d3 | -3.02515 | -48.08442 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da69c56b-7d22-31e0-ace3-b6701e368b7f | -8.3823 | -44.1534 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 595f9be0-2ac5-3254-a90e-99ab3513a785 | -3.02686 | -50.35091 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13a3eda9-eb34-3c65-8aec-552771f7b5e7 | -4.32092 | -49.76401 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fcbe137c-0218-3e6a-9098-212a7b1881cb | -3.03093 | -51.53228 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73cee997-1b0d-361e-bdbb-36dd4e5d7c66 | -2.8069 | -49.86806 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adf7a906-b159-3148-a12b-309e4cb60413 | -2.65258 | -48.55958 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 991942b7-74a6-379d-90cf-865c1f76ad22 | -2.94116 | -51.395 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca990f13-ae00-3fe6-a77b-17fc093ac79c | -2.68116 | -48.50756 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55fcb5dc-a189-3ec0-b19c-574d216a2cb6 | -4.36317 | -47.22859 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9257263-2416-3f68-9a33-59c9caefae34 | -2.55621 | -50.63404 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5616244c-6733-3c7b-b4f6-4965b0fbe26a | -4.05917 | -49.21186 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 83020f8f-2a75-36e5-8b06-daaac8fc1d39 | -8.37667 | -44.13271 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c294200f-a569-3d48-97bf-40c7a719495f | -3.2742 | -50.3552 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 765bfc4a-12ea-3622-9a09-305f53c9f563 | -2.84071 | -49.82945 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90835b57-2583-38df-9f41-d703e9df2983 | -2.92474 | -49.49461 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81c74a51-f8b6-3d2f-a091-bd0b16da3865 | -2.92992 | -51.4885 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91f321b0-f390-3266-9922-81098661f75a | -2.25799 | -50.53519 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bedeac17-0bf5-367e-be9b-00f148f4f42e | -3.61712 | -48.9227 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac083ec7-e6c3-3c4d-9f30-aaefd07f4280 | -4.21045 | -48.68007 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b79d265-03cf-38c0-b401-a8eb6b2d37c6 | -3.37051 | -49.92629 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14077479-c14a-3d61-a8d1-aadfa375b45b | -2.93606 | -52.7783 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 0966b956-0b2f-3024-a1b5-0f95f7450e6c | -2.5842 | -49.18333 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edb37b6a-90d3-34de-a4e1-e2998cd77504 | -3.25117 | -48.75565 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7eee550-18d1-32c1-a7f2-ae6fdd0cb9b5 | -2.13725 | -50.802 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a30794d7-6ed8-348c-8c52-f5e777cf320a | -2.91749 | -49.49707 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fe873a5-c6e1-3872-80df-3c386de404d6 | -4.11534 | -48.50933 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79b1cbdf-9957-348c-a45a-bb8ee7ff9a4e | -8.39463 | -44.12744 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a1f3ff5-8d1f-3e6c-9528-91b2b259635f | -3.92108 | -46.40912 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82bc8e39-1aad-3b75-8145-669dbe955745 | -4.72334 | -48.77485 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1d65107a-b360-359f-98cd-485490ee067f | -4.49419 | -48.49101 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd3a3cbf-05c3-35ef-a24b-e85d0d10d207 | -3.10024 | -53.32866 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 37e4d042-df1c-3c71-b047-e73789e50480 | -2.28297 | -50.67807 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 12221dfe-39a1-3351-bad5-fabffc9d6955 | -3.11632 | -50.14099 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03e8dff5-3484-33e5-b4a2-f3813594a439 | -2.9095 | -49.2451 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40be225d-e109-3c8d-bec7-a3e2f66c28e3 | -2.41888 | -53.66486 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7570bfa0-364d-38d9-8d19-9a6464a02371 | -3.24783 | -51.59784 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30f2be65-f9ea-3b25-8d3a-c46a33ca1969 | -5.73527 | -47.17692 | 2024-11-10 04:38:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 6ccd668e-341a-3cab-920b-f7ad3ae41bef | -3.42534 | -50.3261 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b7ed728-e984-37c7-ae92-4903243b6308 | -3.02734 | -51.53171 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de3b40ca-03f6-3ad6-b3fe-194f6244d8d8 | -3.12196 | -50.14929 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aac829c6-dbb0-306e-8870-aa3f57b5fbc7 | -3.26854 | -46.31783 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca91258e-4c60-3d2b-87bd-e432a33c2e87 | -3.1184 | -44.99266 | 2024-11-10 04:38:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1afbbe48-b120-3405-81c0-afca84f42ab7 | -4.31762 | -45.64262 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce201952-5db9-367f-bdd6-634681a384f3 | -3.35677 | -50.05618 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b56cd082-3f3f-35cf-8c4a-4533d14c39a1 | -4.08842 | -48.51234 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f44dc7bb-467b-3262-ada1-68c19c4ba6b7 | -3.95862 | -49.43793 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 422ee931-b51e-35aa-987e-abd17fe6c06b | -8.39828 | -44.13198 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca7185b3-3980-3e7e-9de0-dcbfa418f0a8 | -5.31494 | -47.68736 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 72039b8e-7921-3fd3-ac64-19c5943d209a | -4.30515 | -48.61387 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30454ba4-776b-3984-b25a-d18c952381c0 | -3.37206 | -57.24107 | 2024-11-10 04:38:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08eb6e2e-daf0-3df4-bc53-04aad92a6761 | -2.56463 | -50.68203 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 50936a7b-9d08-321e-b8be-2e4329b35763 | -2.8995 | -49.24354 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README106.md)
