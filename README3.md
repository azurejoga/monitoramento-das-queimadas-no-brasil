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
| 8fda3217-4a1d-3c22-b1da-430dc71ecb8a | -6.8745 | -43.588799 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 453306c4-500b-3554-85e7-0cb48e5efaba | -4.5927 | -48.785301 | 2025-08-19 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff60cba2-e406-3677-9f68-1a08e77804a3 | -6.624 | -43.881802 | 2025-08-19 00:34:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 200dcf42-3236-3200-b302-0f4325eb2a45 | -13.8689 | -45.549198 | 2025-08-19 00:34:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 61aaf98c-84e7-34a2-ac40-e9884f6b4823 | -6.7448 | -41.543999 | 2025-08-19 00:34:00 | METOP-C | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fad9334d-1f44-3a8e-8bd7-8c1f0515b034 | -6.5508 | -49.5158 | 2025-08-19 00:34:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11feb96b-0c7b-303e-8b2a-a394b301b2e4 | -9.0414 | -50.1744 | 2025-08-19 00:34:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07eaa35a-204a-38db-a4ab-23f89c1a705a | -4.5911 | -43.313599 | 2025-08-19 00:34:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73357103-d277-3c43-b4ea-0b201b25a77b | -14.1748 | -45.306801 | 2025-08-19 00:34:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db128929-6585-320f-881e-0e01bc9627a0 | -7.263 | -50.1702 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cd5f6e9-4d54-3212-a8b8-f326b2fa7925 | -14.5134 | -45.938599 | 2025-08-19 00:34:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12466507-1fed-3a47-9125-d51717186f74 | -10.5295 | -50.365601 | 2025-08-19 00:34:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3693cb52-64c7-35ce-af50-1ae788ab18d3 | -6.6163 | -43.892899 | 2025-08-19 00:34:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25b8a80f-32b4-38fa-bfb6-df410120b62f | -6.9668 | -43.586102 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0c631852-9a6e-302a-8ca9-5379ef644c73 | -9.5794 | -47.4133 | 2025-08-19 00:34:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c28c98e7-b7eb-3cdb-b8b7-6dbb94b0cd4e | -5.9864 | -44.284901 | 2025-08-19 00:34:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edd29378-8f89-3f8a-9242-c10fab2ec83a | -6.6142 | -43.884102 | 2025-08-19 00:34:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cbe4540-5cbb-3eb8-b25c-d2ef81b32a87 | -9.1744 | -40.594299 | 2025-08-19 00:34:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 47ccf122-cd66-3442-8d94-1e6fafe31f66 | -9.8603 | -44.686401 | 2025-08-19 00:34:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 952fdd67-7de8-3720-9299-cfeff66d2f94 | -7.2514 | -50.164398 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b7563e-e38b-3bee-97b0-60b0a5edcdc8 | -11.0459 | -44.588299 | 2025-08-19 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39e58387-0b35-34c5-83fb-6edde07e5a7a | -6.9592 | -43.597401 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 989a0a69-165f-3cea-9e82-8f8e2fd5bb7b | -5.6597 | -43.383999 | 2025-08-19 00:34:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f8ae00b-9be5-3955-b0b8-c2660c6cd89b | -3.2534 | -43.278301 | 2025-08-19 00:34:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5558b5e1-0667-38dd-bfee-b8758143ff5e | -14.9729 | -54.809799 | 2025-08-19 00:34:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b5edecd-0517-3216-92cf-0d2488a4475b | -2.9024 | -48.293499 | 2025-08-19 00:34:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f98d7c1a-1834-31d6-be15-4ea8eda136b8 | -5.5459 | -49.079102 | 2025-08-19 00:34:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40a3383b-231e-342e-819b-29226bb5cf92 | -6.971 | -43.604 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 423db899-ef43-38ce-9d76-a5fda5e6896c | -7.2612 | -50.162201 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3578e102-7fa6-3306-a3d7-0cd30b2089f9 | -6.9319 | -43.6133 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55f44af7-5dee-3d8d-b585-7c4f12176d05 | -15.0252 | -54.820702 | 2025-08-19 00:34:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be3862a3-dd57-3a38-9715-a66aefbb1606 | -12.4278 | -48.705799 | 2025-08-19 00:34:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0b7dca7-92c9-38bb-aa74-6ef2dbe97247 | -8.2363 | -47.854301 | 2025-08-19 00:34:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6bbd24fb-efb0-3890-9498-f4105f51cc49 | -7.2926 | -43.696999 | 2025-08-19 00:34:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa10a803-a06b-304e-b7e7-62b2290241bf | -12.0497 | -44.021999 | 2025-08-19 00:34:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d186baa-6da5-3f33-8beb-e73fb1ff1dd4 | -14.8536 | -48.053799 | 2025-08-19 00:34:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6bb17a81-1873-31b3-8253-1e9a9c28a8fe | -4.6106 | -43.308998 | 2025-08-19 00:34:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6624aad-0faa-34e9-bb6e-b93938646276 | -5.3737 | -46.301701 | 2025-08-19 00:34:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5abcf8b7-1a65-3af8-873d-63ab69d2ebc9 | -6.6261 | -43.890598 | 2025-08-19 00:34:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8271617f-5dac-3c10-a4f1-53d44d455b1d | -7.2206 | -49.610901 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 165d5e7a-8b3d-3920-bfe7-f22969654b9a | -6.9396 | -43.602001 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 97c5b90a-b65f-37cb-846c-6929574b5b88 | -14.5149 | -45.945599 | 2025-08-19 00:34:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 36e503c3-cb44-3602-8204-cfb89a41682d | -12.4376 | -48.703602 | 2025-08-19 00:34:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4ce27d6-a06f-3b55-86c5-5258be085d4d | -5.8749 | -48.123001 | 2025-08-19 00:34:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca07f993-dd6f-3f4f-8115-62b20ba10792 | -6.7575 | -41.553699 | 2025-08-19 00:34:00 | METOP-C | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 53104a32-9f37-303b-b24e-113ecd641c17 | -12.6511 | -45.818699 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c973ef28-b922-39dd-9a98-b108f9cae450 | -8.0887 | -46.663799 | 2025-08-19 00:34:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30f83a9e-bc52-34e6-8407-73d2c0635fbd | -12.6347 | -46.889099 | 2025-08-19 00:34:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 250da216-0cde-3135-8e0a-8a4d63a59795 | -13.8657 | -45.535099 | 2025-08-19 00:34:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e917699d-f50e-302d-bfa8-842f2479d1a3 | -15.0312 | -54.798698 | 2025-08-19 00:34:00 | METOP-C | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 722cf1b4-7acc-3651-83ec-aa783bbe7e72 | -5.5768 | -44.079899 | 2025-08-19 00:34:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d28d3de7-72f7-30a4-bda9-ac08c5fc576d | -3.5858 | -49.4333 | 2025-08-19 00:34:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83afe332-80da-333c-a5a9-cd9b7046a630 | -9.7052 | -51.9664 | 2025-08-19 00:34:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de221950-e4a1-3123-81c3-3d2bf6ec1198 | -14.9788 | -54.7878 | 2025-08-19 00:34:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0b907ea-3058-3e74-8ddf-3d94f2b037ae | -6.9439 | -43.6199 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 169385fb-0131-3d3c-8ad9-9f7b50f76402 | -6.9494 | -43.599701 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 477ecfd0-95e5-3c6a-b293-ad7620b63e91 | -3.8259 | -41.569599 | 2025-08-19 00:34:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef8930b8-484b-318b-9001-ab021a84cdbf | -6.5525 | -49.523201 | 2025-08-19 00:34:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c90722d7-95cb-3110-8637-8ea27572fb3e | -4.4283 | -47.750999 | 2025-08-19 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88f54777-f93c-330c-9d93-bc9652cd75a6 | -6.4566 | -45.454201 | 2025-08-19 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f0c0ff0-2def-38c1-b588-90fa785c0fe1 | -6.946 | -43.628899 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8c70b5f6-d4d0-3476-85dd-e7225d2bf456 | -6.3997 | -44.286598 | 2025-08-19 00:34:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7821e3be-8855-389c-b25b-ec2f9b19c4f3 | -13.2555 | -50.821602 | 2025-08-19 00:34:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c1d4e9b6-cbdd-3c03-afe4-e7722fd5e1fe | -14.8553 | -48.0616 | 2025-08-19 00:34:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db807d68-e4ce-3ec9-997b-06aac566d55b | -13.5862 | -47.000801 | 2025-08-19 00:34:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 29efeb7d-6cfb-31f8-a163-67db0b86c4e5 | -6.9613 | -43.6063 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 092be6d4-1de6-3dcd-a0b3-552f5c6f4ef1 | -12.0461 | -44.006699 | 2025-08-19 00:34:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f862d209-9995-3081-bc40-62be2490768f | -14.8698 | -48.033798 | 2025-08-19 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6963e79a-94d6-3bae-8323-8fdce7eeb185 | -6.9341 | -43.6222 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4afcc18e-ef0d-3b41-97ec-c77045a927e9 | -3.9958 | -42.541801 | 2025-08-19 00:34:00 | METOP-C | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5aab2054-6238-3cc9-bfed-8b191c2a5885 | -3.4743 | -47.684898 | 2025-08-19 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43e5c526-680f-3ec7-a733-fe2a65067ec3 | -9.568 | -47.408501 | 2025-08-19 00:34:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ab1ec22-1f99-3a05-99e3-ca31ee8f9e6c | -5.8847 | -48.1208 | 2025-08-19 00:34:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7a18523-efae-3dd3-9cae-260214018f36 | -4.0157 | -48.0658 | 2025-08-19 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6468a19d-621e-32f5-a550-66e41834e158 | -9.5696 | -47.415501 | 2025-08-19 00:34:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdc01a33-8163-3ae0-8f31-17a4b06104ac | -11.5836 | -44.857201 | 2025-08-19 00:34:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c34c6d44-7747-377f-b203-26b5a7713a53 | -6.9353 | -43.584 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 96a6d15b-3e1d-3104-881c-bc400827fa2c | -3.9877 | -42.5075 | 2025-08-19 00:34:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 714ca6d1-4233-32f0-8ea5-cdaabc12e36e | -10.6022 | -51.183498 | 2025-08-19 00:34:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07b6e973-9337-3b6d-b5a9-43a3c56df86f | -5.784 | -43.6035 | 2025-08-19 00:34:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13e987b7-4bb7-343a-8d19-4a1ac33cb78b | -5.7884 | -43.622002 | 2025-08-19 00:34:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0b135a4-098f-3927-aed4-42833799758d | -11.8168 | -44.2626 | 2025-08-19 00:34:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52be53ce-eab2-3932-b52a-c86e19207068 | -5.8733 | -48.1161 | 2025-08-19 00:34:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62aa538c-0618-3c81-8656-a7d3b1eccef5 | -13.1631 | -54.9338 | 2025-08-19 00:34:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79d1fc6f-83b9-3304-a432-d6da50d79313 | -6.9473 | -43.590698 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b550d981-53d0-3ed3-9a90-5e489c19e30b | -3.4759 | -47.691799 | 2025-08-19 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acd44d5b-2a96-39e1-93a1-51e1007772aa | -15.4069 | -49.564999 | 2025-08-19 00:34:00 | METOP-C | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9623b104-b828-361b-b0eb-498c65370f7b | -9.7075 | -51.9772 | 2025-08-19 00:34:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8886ccb3-af86-3991-8e3a-2a7b4a3ff614 | -7.3133 | -46.299 | 2025-08-19 00:34:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f2c1fd3-888e-38eb-9c08-cdc569c71b23 | -13.2653 | -50.8195 | 2025-08-19 00:34:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 04328800-7efd-3d5c-bac5-50c91d748c35 | -6.454 | -44.561298 | 2025-08-19 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f3b28b3-1079-3a42-8ffa-bcd21dc7fa41 | -14.8668 | -48.067299 | 2025-08-19 00:34:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ce4eb325-4aaa-31d0-b765-ff91e7da7aa8 | -6.8766 | -43.597801 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67751622-bc11-3e8e-b69e-2f757cf0e5f6 | -5.796 | -43.6105 | 2025-08-19 00:34:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7dff985-bafd-3e16-bef9-d9a5e3340eb4 | -10.6001 | -51.173599 | 2025-08-19 00:34:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a397c8c4-fd87-347d-b510-a45d0a939964 | -12.0399 | -44.024399 | 2025-08-19 00:34:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba6ddcad-22cc-3bf3-9baf-ec8ccf9b638b | -11.8588 | -51.569099 | 2025-08-19 00:34:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36189e5d-9e75-3752-919c-bb2db59e53ea | -6.9571 | -43.588402 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df1a2e80-01ab-37e4-88eb-5e89f05c7610 | -5.9932 | -44.139099 | 2025-08-19 00:34:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9add721c-2605-39e5-ad83-b4f25d2eb758 | -5.7982 | -43.619801 | 2025-08-19 00:34:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
