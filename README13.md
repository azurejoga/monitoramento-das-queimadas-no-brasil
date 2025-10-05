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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17d74cb7-9458-30ef-96e0-22283e866ebb | -6.25998 | -45.34882 | 2025-10-05 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b546992b-8398-3d2c-85b0-6a1a96747502 | -6.46055 | -44.59321 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 15f0ee9a-8885-3e9b-811c-72e4600ea782 | -5.01525 | -47.21563 | 2025-10-05 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f925adcf-9b80-3fc6-bb15-1953eba613ff | -4.06632 | -45.22472 | 2025-10-05 00:35:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4ea38ecb-bbca-38cb-a316-64609c97feaa | -4.13642 | -47.65041 | 2025-10-05 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 74b5a7ea-76fc-30e1-9cc4-2f594f02efff | -7.45488 | -47.1781 | 2025-10-05 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b1aba99c-f8b1-3b04-aa33-12844d87ef64 | -7.8568 | -48.19524 | 2025-10-05 00:35:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 29f266e6-daa1-3c2a-bff2-7b3f28bdd47e | -5.9873 | -44.35664 | 2025-10-05 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| bcb0f4fd-db52-3d2a-abdf-0a89a24bc67b | -7.02312 | -42.79321 | 2025-10-05 00:35:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 0d3aa08c-9e4b-34f9-a4bf-a38cb12e907a | -5.88517 | -42.90956 | 2025-10-05 00:35:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| e7d65b4e-4aa5-3310-8af2-cbafbd8cce2a | -7.78066 | -49.83814 | 2025-10-05 00:35:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 55973e40-688e-3769-8aa2-eabfe9ca7120 | -3.09193 | -47.02538 | 2025-10-05 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 33d7091a-539f-30ff-a975-377512602a31 | -5.84023 | -42.87518 | 2025-10-05 00:35:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| c281a7c3-db63-33e6-9fa2-9fef7194eb4d | -3.38969 | -50.14242 | 2025-10-05 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b5b0e175-f84a-39dc-8bef-863f885ba9e0 | -6.26188 | -45.36186 | 2025-10-05 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f6c89e8f-f79a-303d-a3ce-5bee87e14e70 | -5.50349 | -45.6532 | 2025-10-05 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ead9f8b4-4806-30cc-9042-67309234ebcd | -5.82526 | -45.81446 | 2025-10-05 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 693351a4-9fc8-34e7-8726-4e470bdb0cc6 | -2.10557 | -47.49908 | 2025-10-05 00:35:00 | TERRA_M-M | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1435d3b0-54c8-3895-8165-7e1c93ac5bf7 | -8.18621 | -47.00134 | 2025-10-05 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 71038b0e-4c5a-33a7-8754-593e1c58fd5c | -6.39724 | -43.07468 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 3caf07cc-a83b-337d-8c4e-cfefe8a0e458 | -6.4418 | -44.16233 | 2025-10-05 00:35:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 7890086e-bb26-3e40-86c3-c79d6d84dab1 | -6.40683 | -43.05351 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 364.2 |
| f6dd4b48-5d5c-39ff-bb64-26756cd5fcca | -3.81209 | -51.0724 | 2025-10-05 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c6129d71-87d9-3466-932d-5227bd369cac | -7.78715 | -44.53661 | 2025-10-05 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 5930b496-cd4f-30cb-9e78-292fab25ac48 | -4.32003 | -48.09258 | 2025-10-05 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 843f1320-95f5-3dab-a448-8df7113085ad | -8.41642 | -46.80793 | 2025-10-05 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| ac8b48bc-44de-356c-8663-a7691bda4431 | -5.53926 | -51.44296 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 20d29da5-5dc9-3574-a512-781f35ff4e05 | -5.92481 | -43.33969 | 2025-10-05 00:35:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 6eddb7d7-6af1-39cf-9e56-26bbc855af9f | -6.72174 | -46.06047 | 2025-10-05 00:35:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f3153296-be89-3bdd-8fd8-99713249a960 | -6.24752 | -45.33719 | 2025-10-05 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 61657034-d938-3cd4-9e6b-69cb2dbcffb8 | 3.86964 | -51.80386 | 2025-10-05 00:37:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 131a4f7c-4707-3dda-80ee-fe607989e7b9 | -11.8775 | -56.8969 | 2025-10-05 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| c786695a-378f-302f-948e-9ed9860eb26e | -11.8225 | -45.0827 | 2025-10-05 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 9d4ea440-6eed-3a3f-a633-44d2e229ef6b | -2.6883 | -48.3899 | 2025-10-05 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 3fbaf8e7-ef32-3799-b750-4188cf298383 | -4.4445 | -43.2397 | 2025-10-05 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 2cf51d49-94bd-3db3-8acf-78c5b467aebc | -4.3197 | -48.0908 | 2025-10-05 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1f7abf35-ab06-3b7a-afeb-526bbfc1e686 | -6.3946 | -43.0505 | 2025-10-05 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| a7d612a9-1552-3f90-bd13-c08752de5c25 | -10.4054 | -45.3931 | 2025-10-05 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 34e062ca-d426-35e5-b5af-93aa68bbcb63 | -12.4669 | -45.5155 | 2025-10-05 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 250.7 |
| 1468d085-2862-308d-afe3-dd962fb9b672 | -5.655 | -43.9013 | 2025-10-05 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| c8f6bea5-c567-3b0d-a5fa-616a48702a4d | -6.4134 | -43.0489 | 2025-10-05 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| ec3259c9-bf02-3e58-8520-d26ad76a3c5a | -8.4354 | -70.1117 | 2025-10-05 00:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a85a1da1-5e35-33fb-9ea1-cfa9cdc50442 | -12.4472 | -45.5415 | 2025-10-05 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c78103cd-8447-3f02-899f-ea635dc72a64 | -14.3353 | -47.6755 | 2025-10-05 00:40:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d313d338-d858-373d-b217-93c5a429d1f1 | -4.4446 | -43.2164 | 2025-10-05 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 3619af18-db22-32fa-bad9-f26f431c0432 | -5.9226 | -43.3236 | 2025-10-05 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 69036c93-2049-3850-bb80-cdeee60ddfba | -4.6318 | -43.1816 | 2025-10-05 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 223.8 |
| 525091e9-91e0-3f1f-8da5-47edc5d5fd83 | -11.7712 | -44.7432 | 2025-10-05 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 12705aae-9359-3853-aab1-ec470b967afb | -11.823 | -45.0596 | 2025-10-05 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| d26b02b4-be4f-3ee6-a4ab-b07d97c04259 | -10.5863 | -54.36 | 2025-10-05 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 2f14fe2f-34b9-36e1-8912-e529768e8515 | -5.6361 | -43.9258 | 2025-10-05 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 374a7de0-9a97-33f7-861f-2eb4827e6066 | -5.6548 | -43.9244 | 2025-10-05 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e76dd1a7-c0c1-3522-8213-18e43cd5c5d3 | -4.6504 | -43.2038 | 2025-10-05 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| ff8eb295-dad6-33d4-957e-42e46e01f875 | -7.1699 | -46.0771 | 2025-10-05 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 496758ce-3417-3b62-b15d-c1ded416cb51 | -12.4476 | -45.5185 | 2025-10-05 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 80990090-c544-3817-9b1a-b56751f5d8dd | -14.9157 | -46.8541 | 2025-10-05 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 3efbc3fa-293e-3b3c-b20c-d1d7c61795ff | -5.6363 | -43.9027 | 2025-10-05 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 6c849ea7-b110-3ab7-9e44-18007779a2ff | -6.3943 | -43.074 | 2025-10-05 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 44dd8a7e-22c8-3d90-9a57-b7ef4f2f1797 | -14.9352 | -46.8507 | 2025-10-05 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4d57d060-53af-3bbc-8d44-14356811788b | -4.6317 | -43.205 | 2025-10-05 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 5242b178-f07f-32c4-9c3e-4640cd8b9b6c | -11.8588 | -56.8785 | 2025-10-05 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 41614910-a7dd-3250-af13-4ac771ad18be | -13.1585 | -50.9359 | 2025-10-05 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 15324cf9-1a81-37bb-88c5-94cb9dd7f2a1 | -15.9084 | -48.8254 | 2025-10-05 00:40:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 983d70c2-8dd2-3b38-9cf0-39fdb9268256 | -21.08 | -49.0699 | 2025-10-05 00:40:00 | GOES-19 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.4 |
| 40203422-3347-38fa-bd24-a420f1883b75 | -13.1393 | -50.9383 | 2025-10-05 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 78a5b7ed-43df-30f3-9a95-e60248ef27b8 | -10.6052 | -54.3584 | 2025-10-05 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8c29c3be-6b88-3d91-a3a6-9f984d2fb212 | -13.1589 | -50.9144 | 2025-10-05 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b8912274-d341-3088-8e14-6ee354ef91fe | -13.1397 | -50.9169 | 2025-10-05 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 266.3 |
| c0dfb27b-e241-3793-92ac-de4ba0c95bae | -6.4396 | -44.1627 | 2025-10-05 00:40:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 0b585a38-848d-3f6b-a606-d473500820b4 | -12.4673 | -45.4925 | 2025-10-05 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 3609663c-6bd1-3977-ace5-0cea6410dc7a | -4.6505 | -43.1805 | 2025-10-05 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 229.7 |
| 89e96349-ae65-38d3-ae0f-3414539a0790 | -11.8777 | -56.8769 | 2025-10-05 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 7412c192-4810-3454-a547-e521cfa3b795 | -21.0793 | -49.0931 | 2025-10-05 00:40:00 | GOES-19 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.6 |
| 5e78f1a9-a5e4-333f-8c67-795b538fbfce | -15.928 | -48.822 | 2025-10-05 00:40:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d24fb0d4-69e6-3dc2-9d43-b7efd544c31e | -12.895 | -47.3134 | 2025-10-05 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 3e6bcd5c-30bd-355e-b1bf-4ea49bf80c9f | -6.4398 | -44.1396 | 2025-10-05 00:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5c62e0b8-253a-39c8-b99b-bc4788295495 | -8.4353 | -70.13 | 2025-10-05 00:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5b1feb62-dc86-3d2e-8cff-5c42631acd9d | -13.14 | -50.8954 | 2025-10-05 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 5ec564a6-772e-3466-b01a-2eb3f61731db | -10.8379 | -57.1781 | 2025-10-05 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| be735ac3-e65a-3e08-b998-45748bffda86 | -15.3597 | -47.9779 | 2025-10-05 00:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 2b883e48-fa04-3d63-99f8-19ee8632207b | -8.5956 | -46.2798 | 2025-10-05 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d764935a-a485-3685-97e6-cb5adff0a96c | -6.4131 | -43.0724 | 2025-10-05 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| bb8825c5-4813-3455-a75a-085005501198 | -13.1161 | -43.847 | 2025-10-05 00:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 2b384e96-c73a-3006-895a-f34a6070cea1 | -12.4665 | -45.5386 | 2025-10-05 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| e631206a-962c-3783-baf5-9a9d133102bd | -7.7301 | -46.3185 | 2025-10-05 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| e7d032a2-2a64-3721-9201-ed71323ef8b1 | -5.066 | -40.475 | 2025-10-05 00:50:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 74fa5bd1-82f9-39b4-ae8c-0a5b86468835 | -11.8418 | -45.0799 | 2025-10-05 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| ccc2521e-2b4b-36b5-b743-ff47f56af853 | -22.9821 | -52.7352 | 2025-10-05 00:50:00 | GOES-19 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 51.3 |
| 7e9ed8c9-1479-3f94-8375-cd73e74d91a8 | -6.4131 | -43.0724 | 2025-10-05 00:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 26ca84de-f995-370c-9f29-439fb6438da9 | -4.6504 | -43.2038 | 2025-10-05 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| a5c9e655-66aa-3ba7-88f0-a97d4b225ae4 | -12.3914 | -51.094 | 2025-10-05 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a936096b-939f-3dfb-976c-fd20230c9a75 | -5.6548 | -43.9244 | 2025-10-05 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 19978286-75cd-339b-b37c-bf84c8da05b1 | -2.6883 | -48.3899 | 2025-10-05 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b5928384-5f2b-33ee-8b38-d26831db3367 | -6.3946 | -43.0505 | 2025-10-05 00:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 55769288-2ea4-33b3-a1a8-b01f52eee1d4 | -15.9084 | -48.8254 | 2025-10-05 00:50:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 4cab31e0-2b03-33c3-938f-5a9e22aa3364 | -4.6507 | -43.1571 | 2025-10-05 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 5cb1b538-6c78-3fa5-852a-a3bab8210e8c | -5.655 | -43.9013 | 2025-10-05 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| ea45a928-9f45-35f6-b6e2-9cbd63033cb3 | -5.4909 | -43.4032 | 2025-10-05 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 349907d9-1257-3b6a-9e8b-adab0cb66993 | -6.4396 | -44.1627 | 2025-10-05 00:50:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 890ac4c9-7acf-3380-8fed-830d6820a570 | -11.8225 | -45.0827 | 2025-10-05 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |


[Clique aqui para ver as próximas entradas](README14.md)
