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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd252f81-b2ed-337d-b689-d19bae73e385 | -11.0585 | -55.381199 | 2025-06-28 00:59:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a413048-267d-3b89-bd39-af5e1fe8fd06 | -9.1019 | -49.4589 | 2025-06-28 00:59:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4e71ec1-df36-3d69-92d8-d40a5ed4ad93 | -12.2646 | -46.7743 | 2025-06-28 00:59:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed68a53b-ec14-36b5-95f4-2f682bd7c7d3 | -12.108 | -54.583401 | 2025-06-28 00:59:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52b5fb13-6408-3214-b735-427b90cbcad2 | -10.0426 | -59.355701 | 2025-06-28 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 319fccc6-f5f7-3a87-a0c3-37f38487b01e | -10.8437 | -53.751701 | 2025-06-28 00:59:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 533c5e67-5165-3d6e-8a70-267456220228 | -11.266 | -52.733799 | 2025-06-28 00:59:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e188445-8582-3001-b148-d565f89b8d46 | -12.6522 | -54.095798 | 2025-06-28 00:59:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b10773c2-9027-32d2-807f-508603978b49 | -11.0325 | -55.358601 | 2025-06-28 00:59:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 961afe0f-c446-35e9-849a-782e0e5fafc6 | -11.0443 | -55.365299 | 2025-06-28 00:59:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29792eab-ce67-3daa-aa80-4e128793c590 | -11.5807 | -52.129101 | 2025-06-28 00:59:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8d8efd3-24a2-3f2b-8d61-dc6b8b57e3af | -14.6905 | -53.376801 | 2025-06-28 00:59:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d568569-b857-3b99-add5-bd69cea15a5a | -9.091 | -59.476299 | 2025-06-28 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7cfaafc0-b420-3f0d-bbc9-29bad95f6399 | -10.8312 | -53.742599 | 2025-06-28 00:59:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5faecdd-5d94-3aab-b581-f0ca0b5bfbf8 | -11.4386 | -54.462601 | 2025-06-28 00:59:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c88321ce-1bba-3cdf-b66b-37338c05632f | -11.0464 | -55.068901 | 2025-06-28 00:59:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44fc2a9d-94b6-315d-9604-91bc8c41897d | -14.531 | -53.826698 | 2025-06-28 00:59:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6232b6e8-c06f-30a7-899f-7eb4395e5228 | -9.7163 | -56.170898 | 2025-06-28 00:59:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b564b0d1-b743-312a-99ab-1957314fcdf0 | -11.8779 | -58.7183 | 2025-06-28 00:59:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| db551c72-9cec-38db-9309-98628a0aa354 | -10.8243 | -53.7565 | 2025-06-28 00:59:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2090c83c-1e43-347b-a0da-ef3b7ea1d798 | -16.2544 | -53.6796 | 2025-06-28 00:59:00 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32729ebf-8fef-3fd9-9f07-0e647d8c82f6 | -9.094 | -59.490101 | 2025-06-28 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e74deca7-9063-3e6e-b9d8-b0555e55e646 | -12.5069 | -58.352299 | 2025-06-28 00:59:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 456ef603-11a9-34fc-b208-be38c6a2a2f9 | -10.8159 | -57.758801 | 2025-06-28 00:59:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16b0d9bc-fdd7-3310-bc82-c2e3b4f41da2 | -10.8465 | -53.763199 | 2025-06-28 00:59:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 566600b1-d8cd-38c8-9c6b-3d6e17291b1b | -10.8368 | -53.765598 | 2025-06-28 00:59:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e616ccab-63af-3dcb-ad39-1310ad030022 | -11.0422 | -55.356201 | 2025-06-28 00:59:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 717b0b3c-5bbb-3fb1-ad10-ae446726128c | -8.5672 | -51.577099 | 2025-06-28 00:59:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6048965-57f2-3d25-873d-9dc840cc3bf5 | -12.2464 | -46.745201 | 2025-06-28 00:59:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 849c51fa-ad75-3f59-8de6-00a097aa6d4e | -9.7106 | -56.1903 | 2025-06-28 00:59:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| addcc2e1-4fa5-30d5-9662-cba98222a217 | -12.1057 | -54.573502 | 2025-06-28 00:59:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c21cdfa-8380-3cd1-9d8d-6abedff1b8f9 | -9.7086 | -56.181801 | 2025-06-28 00:59:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53c70fce-0184-36fe-a771-260beca2de9b | -10.0334 | -54.329498 | 2025-06-28 00:59:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 723baf0b-8d3e-3bd7-a1da-83c561a35b68 | -10.8215 | -53.744999 | 2025-06-28 00:59:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75e1b8d4-6aa6-3b96-ae6e-1d0e199525ea | -9.6989 | -56.1842 | 2025-06-28 00:59:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 803474dc-dfc0-3030-8cf6-7abafed9f52c | -11.8795 | -58.7253 | 2025-06-28 00:59:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7fb17d5f-1f2d-3e89-ad4f-b6b64ebd2e13 | -13.1453 | -56.803001 | 2025-06-28 00:59:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 577679d4-4b55-354d-83e5-8a4249078db4 | -11.881 | -58.7323 | 2025-06-28 00:59:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 391c2820-c755-35c9-acb0-edb3d7a981c9 | -16.252001 | -53.6698 | 2025-06-28 00:59:00 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e79df5dd-109a-3cd6-877e-15db861c46c5 | -7.8951 | -61.460701 | 2025-06-28 00:59:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aea37131-eb64-3bc7-ad8e-bde7a87bdd79 | -9.114 | -49.506199 | 2025-06-28 00:59:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56614861-630a-3ca1-b92d-2834e8d2488f | -11.8826 | -58.7393 | 2025-06-28 00:59:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c5faf7a-5cb4-32d4-bb40-0222df2306e9 | -10.3001 | -57.129398 | 2025-06-28 00:59:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29ce3677-9e5e-376f-b963-b57d804c1d79 | -12.5053 | -58.3452 | 2025-06-28 00:59:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 026d5273-3625-327a-8e69-2f1b8ef51611 | -12.1104 | -54.593201 | 2025-06-28 00:59:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb86112e-26d8-34f8-aea4-c8c2faac9925 | -11.2725 | -52.760101 | 2025-06-28 00:59:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b403b9e-ec98-3f48-a06a-d0f4d895acef | -10.8142 | -57.751499 | 2025-06-28 00:59:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8e6a0eb-3440-3d75-a65d-91ee1fa9f6c3 | -10.2984 | -57.121601 | 2025-06-28 00:59:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4182b6be-06b1-3d52-b552-cf3773def9cd | -11.7833 | -59.311298 | 2025-06-28 00:59:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 100fce3b-0281-3781-9511-002e981916f8 | -10.0524 | -59.3535 | 2025-06-28 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| afe08618-921a-34be-acb9-47950516ff41 | -10.2893 | -56.992901 | 2025-06-28 00:59:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e000e9b-ca88-3128-bba2-6e592b23fd65 | -11.4411 | -54.472801 | 2025-06-28 00:59:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b79fa9bb-d2d7-372f-b7fa-a63fdae07756 | -6.9416 | -42.8834 | 2025-06-28 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 5d358b19-7e69-302f-b15e-d69279b0dab8 | -9.1208 | -49.4743 | 2025-06-28 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 7d12abf0-7014-35bd-871c-7f5fef9d1f07 | -6.8922 | -43.9619 | 2025-06-28 01:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 5b69f145-d181-30a6-a163-1e8cb42df89b | -6.9108 | -43.9834 | 2025-06-28 01:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 98b8ecc4-a846-3db3-94ab-3d16c0f7e526 | -11.2853 | -52.7508 | 2025-06-28 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8f971ac1-4c57-3334-8066-1e8159594264 | -11.2664 | -52.7527 | 2025-06-28 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 191.9 |
| 9ab32729-e3e1-3743-a368-2dd7ec9c5888 | -9.7041 | -56.1843 | 2025-06-28 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| d8c74565-65e3-3d86-b971-e35ddbdd5301 | -9.7228 | -56.183 | 2025-06-28 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| a44673eb-afec-3145-b129-a05748fa5748 | -10.8382 | -53.7648 | 2025-06-28 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1c046aff-f5b4-3571-8128-13e5d0e1f92c | -11.0455 | -55.3773 | 2025-06-28 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 376.7 |
| 7cc52194-3f58-310a-a7e4-9a4607aba639 | -6.911 | -43.9602 | 2025-06-28 01:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 623db3aa-7f7a-395a-9f19-dd33db328723 | -9.1017 | -49.4976 | 2025-06-28 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 949cd952-93bc-3db9-80a1-5e95f7bb08e5 | -11.0644 | -55.3757 | 2025-06-28 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 135.1 |
| fd8bdf9a-fd5f-3afa-8484-5811ead6d793 | -9.102 | -49.4761 | 2025-06-28 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a383d38b-c9fc-3900-b7c7-12a2443b11fd | -9.1205 | -49.4958 | 2025-06-28 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 210763e6-7d41-396d-b733-533e4710fca0 | -11.0453 | -55.3976 | 2025-06-28 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 3f253f99-e215-3b71-b87b-552eb5f23547 | -11.2666 | -52.7318 | 2025-06-28 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| cbb80820-1576-339f-a9b5-0c65c5e010e0 | -11.0266 | -55.3789 | 2025-06-28 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 44da5e3b-75ff-3c1b-abd4-dd67e6d4b15a | -7.2028 | -43.0936 | 2025-06-28 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 82e73ca4-9c5d-368e-afae-825b14053b1c | -7.2031 | -43.0701 | 2025-06-28 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 118.7 |
| eb9fd53d-d4a9-31d5-a940-b57996be699b | -7.2219 | -43.0682 | 2025-06-28 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 158.4 |
| 2b95ce31-3206-3d39-8787-3e190e3ca594 | -10.8385 | -53.7442 | 2025-06-28 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| d44b9be2-3590-3339-855f-a6eadb53f0d8 | -6.892 | -43.9851 | 2025-06-28 01:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 172.9 |
| f65eb32d-f496-3b70-8850-93528e7fc101 | -7.2217 | -43.0917 | 2025-06-28 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.4 |
| 850a6c68-8760-3b55-94f7-469ad72babf5 | -11.0457 | -55.3571 | 2025-06-28 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 6ef069c7-9f80-35e3-98ff-ad30eaf61122 | -13.94976 | -43.25214 | 2025-06-28 01:00:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 37.8 |
| 51475f10-afd3-3312-a2ee-2e2a0bcbd236 | -13.94365 | -54.48796 | 2025-06-28 01:00:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1fd659d2-a587-3a8b-ba8e-9e148ccaa0a1 | -16.25599 | -53.68582 | 2025-06-28 01:00:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ae86a3e2-24b3-31ee-bf15-e42f49b41873 | -16.04397 | -48.4737 | 2025-06-28 01:00:00 | TERRA_M-M | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1ac20a97-c81a-360f-9a17-7c722476059b | -14.53625 | -53.83099 | 2025-06-28 01:00:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 98efa77a-e653-3af9-9f6e-3fb8cb8422ae | -13.94025 | -43.24897 | 2025-06-28 01:00:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 44.4 |
| b1fea145-a182-344e-b654-301f961cb71f | -15.25927 | -51.48124 | 2025-06-28 01:00:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 61383f66-edc8-3e8b-a18d-a650c284b216 | -13.94493 | -54.49763 | 2025-06-28 01:00:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 17750222-e401-32e9-b611-abdc79f8561e | -16.45196 | -49.51758 | 2025-06-28 01:00:00 | TERRA_M-M | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7d9bed59-84c2-37e1-8ff9-10550be24bd5 | -15.2579 | -51.47178 | 2025-06-28 01:00:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1626d0d5-4745-3b05-8304-9cbe7742562a | -16.25472 | -53.67638 | 2025-06-28 01:00:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9b511833-1db0-3a46-8485-21d83477700f | -16.0461 | -48.48732 | 2025-06-28 01:00:00 | TERRA_M-M | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0edb7f08-5357-38e3-99ed-6a349b7b6382 | -13.07254 | -48.84076 | 2025-06-28 01:00:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7ddbf50f-3cfc-3243-9bc5-f61e30b9a659 | -14.69858 | -53.39432 | 2025-06-28 01:00:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e86c560f-3c31-39e7-87e8-0badabb7344e | -14.68847 | -53.38647 | 2025-06-28 01:00:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0f34e16c-171d-3f84-9632-19b0111da382 | -17.15321 | -54.0086 | 2025-06-28 01:00:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 16b2cba6-a6b7-3680-b5b4-312ef715547c | -14.68971 | -53.39561 | 2025-06-28 01:00:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e2a4f577-89ae-3979-a0fc-042dc595d616 | -17.1545 | -54.01859 | 2025-06-28 01:00:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fcfb18b2-2c12-3ac1-b7ff-c1a459a91276 | -14.53751 | -53.84028 | 2025-06-28 01:00:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1c01f848-78d8-354f-b583-b02fe063dd15 | -12.10937 | -54.66738 | 2025-06-28 01:02:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 99a259f6-3fb2-33f4-b300-e40658bc0fe9 | -9.37038 | -47.63087 | 2025-06-28 01:02:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 452b489e-8988-305e-878b-e15ca58b3962 | -9.12243 | -49.47227 | 2025-06-28 01:02:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 38ec3907-bb32-36b8-8fb7-bf35ee4b3c77 | -11.60139 | -55.5488 | 2025-06-28 01:02:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README5.md)
