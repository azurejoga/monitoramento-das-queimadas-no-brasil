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
| 27a1864e-d176-30e1-9f35-bddec738cf76 | -10.883 | -54.7624 | 2025-06-12 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a34ccbaa-491d-38b5-97f3-adf775a09133 | -11.9874 | -57.2076 | 2025-06-12 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| aeb00e8d-b8ca-3952-89e0-5f816da92f5e | -13.2796 | -57.0952 | 2025-06-12 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 455055c1-25da-33fe-b0d9-0d6cec18b8c7 | -20.5625 | -50.0948 | 2025-06-12 00:40:00 | GOES-19 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.8 |
| f680d36f-928c-3c77-a852-9dda287f1a24 | -13.8864 | -54.6519 | 2025-06-12 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| bdc91596-1092-39c0-8a4c-fb50f27846a0 | -10.8832 | -54.742 | 2025-06-12 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| f249b04c-ae77-322e-bad4-0a63a7c79d1d | -11.9278 | -57.4717 | 2025-06-12 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 6038e883-5dfc-36f2-9339-4aff48cc701f | -13.2986 | -57.0935 | 2025-06-12 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 8452fd15-ecdd-3027-b22f-73032325aa82 | -13.8867 | -54.6312 | 2025-06-12 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b4871788-5b1b-3123-8687-bdd931a155ac | -12.0063 | -57.2061 | 2025-06-12 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 7b905687-4d50-38ad-9ffd-f30229ec72d6 | -12.2403 | -44.168701 | 2025-06-12 00:44:00 | METOP-C | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1bb6eb8-8e05-39c8-a7ff-24917064f67c | -20.5581 | -50.1077 | 2025-06-12 00:44:00 | METOP-C | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ce7b7ad5-7e75-3473-9bf8-656ddf14d9d3 | -7.2419 | -43.110901 | 2025-06-12 00:44:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e28d9158-9328-33d5-8a93-d823908fbbf0 | -11.5861 | -47.444199 | 2025-06-12 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7be1c34f-b5c7-3570-9072-992bfd54b210 | -9.4092 | -48.430698 | 2025-06-12 00:44:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb29a255-bc98-3bb5-b390-dbf32cfcb107 | -7.1975 | -47.429699 | 2025-06-12 00:44:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5adfc52b-67c9-374e-bb80-62e017657e97 | -11.8669 | -52.252899 | 2025-06-12 00:44:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64b932e3-0287-31f8-98c8-a0dac640cd57 | -7.4566 | -45.5033 | 2025-06-12 00:44:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8634b889-12bd-3451-845b-564639ea47d3 | -13.9009 | -54.668201 | 2025-06-12 00:44:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51a6d1e4-c5f8-3f8a-9009-a780a5fd6ef3 | -9.8607 | -47.881001 | 2025-06-12 00:44:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8421a2ea-813b-3daf-ba82-e8866f2b20a9 | -7.4489 | -45.514301 | 2025-06-12 00:44:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa72d366-b02f-3955-8255-a77788e0af86 | -20.4524 | -46.402302 | 2025-06-12 00:44:00 | METOP-C | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0ff9c916-8847-3c7b-bbf5-53fd9a63c539 | -11.9117 | -57.464401 | 2025-06-12 00:44:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0903c7a-92d9-3e7b-a751-8d16bed02eac | -12.7729 | -44.4048 | 2025-06-12 00:44:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82a95a29-39cb-388f-9aea-063ee6f6f537 | -15.3857 | -47.885399 | 2025-06-12 00:44:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 58968d35-dbef-336a-831c-1c834e74fede | -8.9647 | -47.976799 | 2025-06-12 00:44:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c949a54f-97ac-3250-ab8d-1389aacd27bc | -10.1404 | -47.438202 | 2025-06-12 00:44:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6da88662-6e1e-36ff-bd8b-d3e8e9365739 | -4.6266 | -47.422298 | 2025-06-12 00:44:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 23f830f4-e073-3464-a0d0-9fd54024f9ab | -13.2959 | -57.068699 | 2025-06-12 00:44:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f00a144-49d8-3a23-a456-073b43f287c7 | -5.0713 | -43.7216 | 2025-06-12 00:44:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5442d7dc-c352-3967-8cf9-891e1d75b57e | -7.2516 | -43.108601 | 2025-06-12 00:44:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 16b2fef3-e7f2-37eb-ae7e-947d26a67093 | -11.5716 | -51.304401 | 2025-06-12 00:44:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9488a7c-39a0-3079-bc41-7396f8304bbc | -15.3873 | -47.892502 | 2025-06-12 00:44:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7fa58d38-75c4-3bc6-a175-ab78f4babfb7 | -14.4768 | -48.613701 | 2025-06-12 00:44:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f51d9de0-0d52-314d-8fd6-b393c2ae4df4 | -7.2009 | -47.444302 | 2025-06-12 00:44:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8d2ed16-574b-3cca-aac3-3c4add510285 | -13.899 | -48.745602 | 2025-06-12 00:44:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 90cde550-690d-36bb-bd53-74fbb2d0a97f | -11.9214 | -57.462502 | 2025-06-12 00:44:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7949df7-33ea-35eb-99ff-be4ec1ed565e | -8.0473 | -49.646999 | 2025-06-12 00:44:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cc182ea-4e1a-3d2d-8ac3-13423b1b80b1 | -12.706 | -58.0359 | 2025-06-12 00:44:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a7327d5e-197b-3487-9abd-a3e34f198574 | -10.6952 | -49.515701 | 2025-06-12 00:44:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f44dc18-55bc-3999-9259-698664cd822b | -20.5679 | -50.105598 | 2025-06-12 00:44:00 | METOP-C | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| afd05b6b-00fa-32f8-bc5b-cf27677bd123 | -10.7034 | -49.506401 | 2025-06-12 00:44:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b5bae11-991f-3287-bd47-53e7b6936d73 | -11.5763 | -47.4464 | 2025-06-12 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c19a350-7cb8-3f6f-b4db-bb4c8365125d | -5.652 | -43.6091 | 2025-06-12 00:44:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2804a385-ec2f-3539-bef0-e2106b39af7e | -12.2381 | -44.159599 | 2025-06-12 00:44:00 | METOP-C | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43839c53-1c44-3989-87b6-9d3d33ea9dae | -11.7697 | -54.3783 | 2025-06-12 00:44:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44a38950-9a3b-3edb-a37b-e096df7f62db | -12.7708 | -44.396099 | 2025-06-12 00:44:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1846644-b930-3bd7-ab96-fefece37a88e | -5.6491 | -43.597099 | 2025-06-12 00:44:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33791619-77c7-3946-821a-e621481e0c38 | -13.8953 | -54.639801 | 2025-06-12 00:44:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64ff77c0-0fba-379e-bc13-b7bc37daa41f | -13.8855 | -54.6418 | 2025-06-12 00:44:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d2c3956-ba2f-3aea-883d-dc31e8ea9d2c | -12.7015 | -58.012699 | 2025-06-12 00:44:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e1b35ca-68f7-3f34-9df7-f4f56c1c61ca | -19.5809 | -49.112 | 2025-06-12 00:44:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f0b6d4ac-a8b2-323f-a3fa-49893a8e7873 | -8.0489 | -49.6539 | 2025-06-12 00:44:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb65590-6fb4-3442-a6d1-bfeca9f67e06 | -20.5562 | -50.098202 | 2025-06-12 00:44:00 | METOP-C | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3f9ef7bc-3327-3b91-92c4-3eccc8a68a14 | -11.5733 | -51.312698 | 2025-06-12 00:44:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c04e94f-5fcd-3dea-8d09-afb114b2e07a | -10.6632 | -49.418701 | 2025-06-12 00:44:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38702277-d619-3de2-a16d-ff0d44570611 | -5.9236 | -43.454399 | 2025-06-12 00:44:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27d1d947-4e03-3545-9258-4c6e4d97d1e1 | -14.1775 | -45.487301 | 2025-06-12 00:44:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f838901e-b333-3f6b-a073-c7ed366d6c64 | -12.2136 | -49.636101 | 2025-06-12 00:44:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b6d0989-f8ac-35fb-8c2a-73157c0ab725 | -7.4685 | -45.509701 | 2025-06-12 00:44:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 741060c1-70de-34e1-ba28-287ba260b7fa | -10.2459 | -52.238998 | 2025-06-12 00:44:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 300c336d-12dc-330a-88b8-220f65ca7db7 | -11.5731 | -47.4324 | 2025-06-12 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6ba149e-2434-349f-818b-d3c64dce6340 | -14.1891 | -45.492599 | 2025-06-12 00:44:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 000b77eb-6a8a-3514-871b-af82f0118bd8 | -7.4608 | -45.520802 | 2025-06-12 00:44:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6688a8e1-ddef-3168-b1cb-5d10042ff660 | -10.6968 | -49.5228 | 2025-06-12 00:44:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53350f42-67b4-39b0-ba68-367ebbaea582 | -11.8508 | -43.799599 | 2025-06-12 00:44:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b2cc962-1e45-3a1b-9018-0dd7c570920b | -9.2373 | -57.5243 | 2025-06-12 00:44:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8451e5-8f02-3825-9328-c31acd7beda7 | -8.9728 | -47.967602 | 2025-06-12 00:44:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 914ceea3-8b30-346c-9db0-ed005f56409e | -10.8715 | -54.319698 | 2025-06-12 00:44:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51ccf5f9-beed-37fe-9cb8-2bbf052651f6 | -12.8305 | -47.3834 | 2025-06-12 00:44:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6177801e-403e-3042-b3a8-3240e1d4da22 | -11.9157 | -57.485001 | 2025-06-12 00:44:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1567618b-e1fa-3896-bc0e-a81365539803 | -7.4726 | -45.527199 | 2025-06-12 00:44:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70509790-5207-3d2d-99a2-c60950b8c36e | -8.9744 | -47.974602 | 2025-06-12 00:44:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b3f1693-4e70-3e26-b09f-5425a0c3909e | -13.8981 | -54.653999 | 2025-06-12 00:44:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 26ef8cc9-d9c2-391e-97f7-2e2cd36cafc7 | -14.1909 | -45.500198 | 2025-06-12 00:44:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2fb9c183-47ef-3d6f-bcc1-a526d6159649 | -12.775 | -44.413502 | 2025-06-12 00:44:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f881cf6-ae02-3740-af47-02bab04108c6 | -13.2765 | -57.072399 | 2025-06-12 00:44:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab27d0a8-aa99-3b00-a0e8-8fbf24812a47 | -13.8883 | -54.655998 | 2025-06-12 00:44:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e68759c-0819-38ea-ac4d-7f5d1d71e569 | -20.4541 | -46.409698 | 2025-06-12 00:44:00 | METOP-C | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5aa2fb61-47fd-3a10-8432-b7f513124e91 | -12.8289 | -47.3764 | 2025-06-12 00:44:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 439adf9b-e5b6-3723-aa0b-e9197c789d4c | -5.9266 | -43.466702 | 2025-06-12 00:44:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bef6950e-5c46-3158-8a9e-0de4a8a9ea11 | -7.2449 | -43.123199 | 2025-06-12 00:44:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f24cc2ac-6c75-3824-8cbb-23701114f612 | -10.6566 | -49.435001 | 2025-06-12 00:44:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c8b08a5-827b-3ab5-8cae-f4ee31cf03ac | -13.2823 | -57.050301 | 2025-06-12 00:44:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 399e1e06-5f8f-388c-b40f-00fbb3afc900 | -10.7066 | -49.520599 | 2025-06-12 00:44:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b38c4b9-58f0-308d-9316-a138e93e146a | -13.2901 | -57.091 | 2025-06-12 00:44:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 358a92a7-7b43-3c77-8a57-1ef5e9b53427 | -6.951 | -42.8064 | 2025-06-12 00:44:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 57f8ca44-57e7-373c-9aef-1ded8b257527 | -11.981 | -57.199402 | 2025-06-12 00:44:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e28411a-05ff-370d-ac94-f80a97998cfc | -7.2546 | -43.120899 | 2025-06-12 00:44:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c9259e9-ab29-3ec6-a44a-382fa67dfbb0 | -20.6078 | -48.880699 | 2025-06-12 00:44:00 | METOP-C | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 25470d51-e84d-367e-aff2-2302602ca7b8 | -20.559999 | -50.117298 | 2025-06-12 00:44:00 | METOP-C | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 04968593-86bf-30c2-9190-1d40012c99e4 | -11.9945 | -57.2174 | 2025-06-12 00:44:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04f7bb2e-9a2d-3b82-96f9-d6b60981231c | -4.6248 | -47.4147 | 2025-06-12 00:44:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b0796a15-23f8-3fb9-9899-2eb8761e8b88 | -5.0742 | -43.7337 | 2025-06-12 00:44:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45fe3cb9-6a98-3e3b-8e6b-48b6bdd3c221 | -15.3842 | -47.878201 | 2025-06-12 00:44:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3840eb7b-0dbc-3ddf-a588-5d9721a71527 | -10.8764 | -54.735699 | 2025-06-12 00:44:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adce33d8-c81a-3dd8-80ec-ce691d4d9fcc | -10.8915 | -54.759499 | 2025-06-12 00:44:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80e9ea9a-49e8-3519-b00b-daf44cd5fd7e | -10.6468 | -49.437199 | 2025-06-12 00:44:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19984112-1522-3893-8495-59854c5c354a | -10.6603 | -49.360001 | 2025-06-12 00:44:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bf77047-fc10-361f-bfcf-a45aecaaf945 | -12.2152 | -49.643398 | 2025-06-12 00:44:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
