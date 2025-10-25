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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc24bda8-e646-3dc7-8f47-ae31867ee17e | -9.32253 | -45.19092 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c18f590-1285-3c63-b7fe-81f782576170 | -13.4096 | -47.96216 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 674d0bf9-9294-3e7a-a4c0-689038258cd1 | -14.86674 | -48.08532 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b8635cd4-c9fa-3f53-a250-2bfb73377db2 | -11.14508 | -44.93695 | 2025-10-25 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4689defe-b355-361f-8803-aa409bab6d5e | -9.9246 | -47.99942 | 2025-10-25 04:00:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccea2aa9-1618-30e2-96af-26cc447a6de4 | -12.8445 | -48.64933 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 002fe92c-9504-306e-b50d-aa396ee31da2 | -13.91618 | -48.40688 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 694a2ed6-5511-32e4-a0b0-2861f4c3ccc5 | -13.04545 | -47.2101 | 2025-10-25 04:00:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 57eecdbb-db58-3938-a67d-c75b2561c2c3 | -12.94401 | -48.50452 | 2025-10-25 04:00:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33a9777a-bfe3-325f-aee6-6c02532d5f2d | -12.22423 | -46.50692 | 2025-10-25 04:00:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 681f68db-ef85-3dfb-abc6-07f17b044333 | -9.24433 | -45.58891 | 2025-10-25 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55cf129c-21a9-3b23-af1a-e4ae6456b910 | -10.65976 | -44.71712 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4ad7d70-10c0-3f2a-9519-ad9d81787009 | -10.92985 | -50.42037 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95345220-3732-31f5-97dc-6390f57288bf | -13.45268 | -48.59868 | 2025-10-25 04:00:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8e88e49-b4c7-30e4-afab-700d25e81cff | -10.87558 | -48.04108 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9be22f6-f390-3bde-bc6a-3e550db2a6de | -12.22383 | -43.30669 | 2025-10-25 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87487852-39dd-3b59-a4d4-53f50057fd3c | -14.19866 | -47.306 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd88b8a5-497a-37fa-afa9-eac57524adf1 | -10.84642 | -48.96751 | 2025-10-25 04:00:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43a5d831-f31d-366c-8d93-7853ce387c0e | -9.98652 | -44.16036 | 2025-10-25 04:00:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a29bff60-a668-3bfd-9702-3c9ae560573d | -12.08472 | -46.42544 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a4288ffa-b23c-3e5f-b2a1-c488447d515b | -9.09019 | -47.82132 | 2025-10-25 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca0749ce-e245-3bee-aad3-d686c7a94ac8 | -10.59472 | -45.20924 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74714ed4-e1b2-378e-b291-f4eb4a55d9ea | -9.57448 | -49.68224 | 2025-10-25 04:00:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cbca2b2-49ff-3966-afbf-16fb4e6a22dc | -13.91837 | -48.39539 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15e7225d-d1a0-373c-8670-a56cc81de236 | -10.4082 | -44.7469 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f0863af-e4a7-3513-84f9-e58e3a64f5a2 | -13.90795 | -48.42305 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 501ab1be-5249-3cfb-886b-c7f663100181 | -13.317 | -42.41712 | 2025-10-25 04:00:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 4e6dde74-51db-3aa4-949e-e616571736ab | -10.88447 | -48.03469 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39d66f98-1c91-34f1-a8ab-5663600debbb | -11.84646 | -49.85933 | 2025-10-25 04:00:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fe94a1d-540f-3093-b0f4-75559f25fe5e | -15.53058 | -45.70187 | 2025-10-25 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 921310b0-a6d6-33af-ad6b-af74a2c857e6 | -8.71863 | -49.60421 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c834f1b4-5f69-3a7d-8868-2cab1c3356d4 | -13.29985 | -47.45407 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbeacc6f-3a97-3829-aea5-19471c2829e0 | -12.46571 | -44.53335 | 2025-10-25 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c05c79d4-8bfb-3bc9-83ab-a943fea55959 | -11.57442 | -49.53908 | 2025-10-25 04:00:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c1508d8-a39a-370b-a1c4-388c9cba8ebf | -14.93283 | -48.12712 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a3972b3-cbcc-3b0d-a73e-458a6be253bc | -10.61913 | -52.18431 | 2025-10-25 04:00:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efd090d5-281d-35b6-9b53-d7a803228ef8 | -14.46485 | -47.92403 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd29822f-2c60-37fc-9353-a3a4daff53c8 | -13.94417 | -43.81732 | 2025-10-25 04:00:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 321330f4-e180-3af4-85d9-54e396bd22ce | -10.86422 | -48.04539 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68ab09b3-5b47-38ec-bf87-e3506744a37e | -9.32181 | -45.19507 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36af0c13-6f46-321c-bc68-d3582e8875d8 | -9.71468 | -45.42186 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cd3dfad-8197-3bd4-9c15-96b414fcf64b | -10.2547 | -47.99713 | 2025-10-25 04:00:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cda9ef0-cfbb-3d17-86a4-a5b92575c177 | -10.64573 | -45.23426 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fc0c3e3-a5ed-3e17-acac-2eb918934b10 | -12.11692 | -46.7086 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 54aafdef-51cf-39c0-b7e3-4542d2980fbd | -12.05081 | -46.40818 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da38078c-54b6-3620-83c5-42d72b9c1eea | -12.94519 | -48.4985 | 2025-10-25 04:00:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 33eb081a-59b6-3c34-bf4a-e33338536b9e | -9.99787 | -47.5926 | 2025-10-25 04:00:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aee52934-ea14-310d-b65a-df4977b2bcd7 | -12.70168 | -46.33513 | 2025-10-25 04:00:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b55a800a-5016-3831-bfb5-7ee8e4f67be3 | -12.64182 | -44.3022 | 2025-10-25 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0838024a-7673-3609-843d-1fdbce07ce89 | -8.71785 | -49.60838 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0b744411-546c-3d4e-9e37-7c2cb51e2bfb | -9.23984 | -45.58834 | 2025-10-25 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8f1243b-64db-3d7d-9bbd-de2d7ad20751 | -9.30214 | -45.17986 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da703256-6441-35c5-9157-92d0c4ed36d6 | -12.38456 | -49.9495 | 2025-10-25 04:00:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b732d004-7d47-383c-848e-7662f9d20c40 | -14.17746 | -47.31765 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c059739-1242-311c-b312-8899cc8dc391 | -14.7213 | -46.61415 | 2025-10-25 04:00:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b6d9493-6110-37ed-af6c-6dfae86e78c8 | -14.92815 | -48.12571 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9524050f-557d-3f7c-8bc1-4ae1f170d10d | -12.1528 | -48.01952 | 2025-10-25 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab756c51-5fd2-3ca1-bdcf-0b5d0281aec4 | -13.20776 | -44.10572 | 2025-10-25 04:00:00 | NPP-375D | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce7fdd7f-3ece-308d-831d-0bd3f43757fd | -10.80214 | -49.65512 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd455a7d-edc0-348c-87a0-50097f2bef1d | -11.50612 | -44.00636 | 2025-10-25 04:00:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5be68d41-49c6-349e-8622-bf510ee4bff0 | -13.31632 | -42.4211 | 2025-10-25 04:00:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 60f881e4-b5e8-3da0-abcc-052d4cd04001 | -14.58598 | -44.13291 | 2025-10-25 04:00:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ce8ea24-4452-3f52-a344-62c043ab3ae1 | -12.83744 | -43.81199 | 2025-10-25 04:00:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a05ad174-d17a-3586-8eb6-6952beba9205 | -14.87537 | -48.09546 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47a014a9-f1f4-3815-a3cf-c28890c08160 | -14.81137 | -48.4427 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e573f98-308b-3c39-b03f-d032f392ecd9 | -12.04569 | -46.41076 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4a9e9ae-6920-3896-a785-eb57bf116f9d | -14.4646 | -47.92694 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d1012b6-362d-38de-bc31-b47f38dcbf34 | -9.99616 | -47.09629 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db28ae25-ee17-3b3e-881f-a527ba5c3edf | -8.86468 | -48.29178 | 2025-10-25 04:00:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12d071a4-a106-395f-ae74-d98fd03abf3d | -10.89485 | -48.0357 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49338514-b4ba-3941-9f23-78a195dae48b | -13.91731 | -48.40094 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7e52b05f-9837-3185-9ffe-e08b0d1042ca | -10.88132 | -45.08025 | 2025-10-25 04:00:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62643dfd-8422-3618-a9e0-405ccb21a019 | -14.87051 | -48.09502 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 21d63deb-ef96-3e8e-b083-970e357efcf1 | -14.27344 | -47.3334 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdf11163-bb72-3126-8a6b-f6410e714d04 | -15.58478 | -43.21674 | 2025-10-25 04:00:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b9ad8d20-e4b4-35ec-88a9-a754d4a8e2f6 | -14.89004 | -47.86185 | 2025-10-25 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3086c277-e2aa-3182-987e-1213d283fe79 | -12.06228 | -46.39631 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4220772e-d7be-3923-8424-a29495add74c | -13.88146 | -48.40045 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94507b0e-41f9-3d98-9647-f1b1c4946f45 | -9.32392 | -45.18292 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27a83a83-b476-30e2-9c55-ca3b97387bbf | -13.0408 | -47.20924 | 2025-10-25 04:00:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e617e6a0-bab9-3575-a97f-e430ae8a751a | -12.34776 | -40.2774 | 2025-10-25 04:00:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b6d75e36-0908-3cbb-b1b4-8ed0d86fa018 | -14.86454 | -48.0965 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 4b6eb223-e0c2-334d-80ec-6cde00bcf852 | -12.63795 | -44.30143 | 2025-10-25 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d82184be-07f5-3f4c-883e-b5c9a4a6686b | -13.20691 | -44.11049 | 2025-10-25 04:00:00 | NPP-375D | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f679f70-b976-3425-aab3-8e27931ae361 | -14.56483 | -49.83923 | 2025-10-25 04:00:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f34ab79-0ee4-39f3-a556-e9cb4741866e | -10.86873 | -48.04961 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 065533eb-34dd-3266-8e7e-84b7add576a7 | -13.90312 | -48.42139 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 0f489e30-b3cf-3569-a195-cc03f4f88dae | -13.33247 | -47.93248 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86fede94-131e-3da1-8d7c-7c984999fad4 | -13.64642 | -44.23361 | 2025-10-25 04:00:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19c6dfe8-5b13-3f07-8f24-76d296c539fe | -12.83175 | -48.63282 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64636cfa-aa44-3545-b179-94d1f68c1e16 | -8.54798 | -50.04752 | 2025-10-25 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be7dc9a6-d62c-30e2-ae9d-8ae6cbdf84e9 | -14.8715 | -48.08627 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c615c7d5-9ad4-3420-a30b-b7c47a3f8907 | -13.01847 | -47.22566 | 2025-10-25 04:00:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfff8643-170c-3b9a-9d50-10d020981a17 | -14.47316 | -47.93376 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1da6c20d-8584-33bc-89b5-3ec1127e10e2 | -10.86283 | -48.05297 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b8b8fb2-164e-3513-9752-d88f73ae258c | -9.2406 | -45.58395 | 2025-10-25 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a21a0225-3640-3c74-bece-daf4bc3ae3d5 | -9.19439 | -46.34856 | 2025-10-25 04:00:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e16391df-4054-32de-9fae-12c26c8b84d1 | -12.12706 | -46.73039 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdf8b995-e3b4-3c97-a1b5-c6555573017f | -10.41433 | -44.73635 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ffa8ea8-7504-313e-b4cc-826c93953afe | -12.06042 | -46.40636 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README21.md)
