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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be4a5708-11e2-3230-aa86-1b8f7c7bc7a8 | -3.38213 | -47.47716 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1edef7fd-9b77-3ce3-9908-49a9dc5a7e15 | -2.66329 | -47.3973 | 2025-07-17 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 406c87d3-3566-3e37-a6c8-57636da56c4d | -3.38115 | -47.48391 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 020294e9-18b3-3957-94b8-ad54cf1f66d0 | -3.40561 | -47.50463 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 71723205-961f-3510-a81c-32cfa837a3be | -2.44018 | -47.33144 | 2025-07-17 05:10:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af7a7391-a5ee-3039-ac59-014a17e86352 | -3.38555 | -47.49142 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b9d61891-ba64-3cd7-a246-a9d4a8f89cc9 | -2.58622 | -51.92021 | 2025-07-17 05:10:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c68ba7bf-1147-3a62-aeff-37e1458c9252 | -3.38066 | -47.48726 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7d07368e-5749-3f28-914e-c2fd4b4c57a7 | -1.60574 | -54.52679 | 2025-07-17 05:10:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4660341b-623d-381e-8554-f237b71d24fa | -3.38363 | -47.46688 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 905e9ab1-3101-320e-afb8-05241c06f818 | -2.91504 | -48.24121 | 2025-07-17 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f8cda2c5-7aa1-31d5-abb1-4de75df4d798 | -3.39484 | -47.50312 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 700eb872-745c-37f0-af7b-2218256d638c | -3.38752 | -47.47798 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 46671d6e-052e-323d-bf60-a15ec2c18f7b | -2.47791 | -47.20873 | 2025-07-17 05:10:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4601de3-430a-3a92-96e8-8f8f4dc3544f | -3.41054 | -47.50854 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fee6deee-0bbc-3f78-929b-eac642c98e82 | -3.38653 | -47.48474 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7b2c3eb7-3f09-3be4-a9c2-f9bde8084725 | -3.38604 | -47.4881 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e61816f6-43b4-37dd-8ee0-dbac36d2f262 | -3.39143 | -47.48886 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2df703c-6a8a-3eed-a849-7b9f74c2773e | -3.02214 | -49.42677 | 2025-07-17 05:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93d26b6d-3045-3af7-b66e-bb8d5f34c0b7 | -3.41101 | -47.50531 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27455a83-4f09-3533-bb02-6f64392d63c2 | -3.04481 | -49.43526 | 2025-07-17 05:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ffc323f-43c7-328d-afda-4a157330be95 | -3.02682 | -49.4275 | 2025-07-17 05:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6ffa6f3-cd56-3a3d-b19a-304d09fb3fe6 | -2.91459 | -48.24414 | 2025-07-17 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d33095bf-7a80-3b94-8ca8-9a510534ffe7 | -2.90997 | -48.24041 | 2025-07-17 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa2aaf5d-e0c4-33ca-b46a-0a5cf9d6a3cc | -2.6628 | -47.4006 | 2025-07-17 05:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcb3b7c0-61ff-392d-b656-e5734e04e40c | -3.04088 | -49.42965 | 2025-07-17 05:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 17c7efb8-7044-3c5c-abd1-bd221c21adc1 | -2.58544 | -51.92516 | 2025-07-17 05:10:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d39f8e4-2a97-3721-bd35-824bc94400ab | -3.39533 | -47.49977 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d470894-a556-3b3e-a949-bc4892f2ef68 | -3.38164 | -47.48054 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 58fb1247-20a5-310d-abfb-26d43aa3577d | -2.91414 | -48.24708 | 2025-07-17 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35d4096c-a5f5-3bde-a795-4c70c6ba24e5 | -3.38702 | -47.48137 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b7702d4d-8525-363b-b4c7-79cf3c720466 | -3.39094 | -47.49223 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e696a5e3-7216-3117-8462-e5537ae99e5d | -3.38312 | -47.47034 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57f7791d-8018-3970-9ecb-dba30ab3a997 | -2.4407 | -47.32811 | 2025-07-17 05:10:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a1d04dc-2d5c-339b-ad87-b2b293f4ad06 | -2.58553 | -51.9218 | 2025-07-17 05:10:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e67659d1-0d16-3a5b-9999-34a67461fffe | -3.39192 | -47.48549 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3821186e-baf5-3031-96f5-630a2f18b138 | -3.40022 | -47.5039 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b8bdbe23-d6f0-3a0a-8ce3-ea1c862213a2 | -3.03238 | -47.86209 | 2025-07-17 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0000d71c-6c09-324e-bdd0-0ce0caaaecb5 | -6.73276 | -44.33014 | 2025-07-17 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b37f9e32-0fe8-36e8-a580-775ed323787b | -6.84418 | -44.76527 | 2025-07-17 05:12:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa28388d-436e-327b-af72-33d7da566643 | -7.15522 | -46.09283 | 2025-07-17 05:12:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f00630aa-8251-386a-a6ff-ac870594c65f | -8.88556 | -50.15621 | 2025-07-17 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 619008f1-e213-37de-a539-0dde4fe7e6ac | -5.78757 | -45.0874 | 2025-07-17 05:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63928309-0a82-3ba8-a195-e9dd073de1d2 | -6.85087 | -44.76645 | 2025-07-17 05:12:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29bbd203-7cb2-34e0-9dbf-3af78f09712d | -8.03723 | -49.88715 | 2025-07-17 05:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02234ff6-9643-3744-863e-863cff12180d | -5.53163 | -43.88564 | 2025-07-17 05:12:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f41cb756-6c27-31d4-b43b-e3247f9440b1 | -4.37054 | -55.77299 | 2025-07-17 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88bb836f-319a-396f-8cea-e44d9f2c2901 | -5.79186 | -45.10427 | 2025-07-17 05:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6ac1a908-0b9e-3811-936f-38b429a0b7d1 | -6.43516 | -45.3181 | 2025-07-17 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6693098-5bf5-3dd1-b7c6-3597c5b78059 | -6.71898 | -44.32827 | 2025-07-17 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 20abedf7-3595-3dc9-95d3-d1e93e37b9d2 | -6.71296 | -44.32077 | 2025-07-17 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d3e2589a-b1ed-390c-8eef-1f145d59bdc5 | -9.312 | -44.84567 | 2025-07-17 05:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa9f8bdf-5b5c-3874-b8d5-2153dafc2add | -9.41697 | -48.41175 | 2025-07-17 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5c112c3-60d7-31a7-ae9f-f199c8c06aa8 | -6.43538 | -45.31838 | 2025-07-17 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27c18b30-a58d-3252-80dd-f8582ea96165 | -5.66579 | -43.72277 | 2025-07-17 05:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 9b394e86-cb84-3323-90a6-302cb3ac09ec | -4.30117 | -48.09947 | 2025-07-17 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a294fadf-a168-3bf0-981c-96194cf27314 | -3.54546 | -53.57361 | 2025-07-17 05:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9727f1eb-1774-3d4f-a557-75eeba29d596 | -7.20484 | -45.33091 | 2025-07-17 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ef8265a-c110-32b1-bc86-073d028ba440 | -9.41769 | -48.41323 | 2025-07-17 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf04fbaa-3f43-3f84-a5b8-0c7629ca5266 | -4.1092 | -48.20753 | 2025-07-17 05:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b98517f6-42c8-3938-bea6-ba5a11bd43e9 | -6.70608 | -44.31975 | 2025-07-17 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9183adce-4ea1-33b9-9f37-43fec49aa707 | -7.88509 | -55.3722 | 2025-07-17 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5952dc5-7a61-38a0-b210-53377048ca2d | -4.10962 | -48.20456 | 2025-07-17 05:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf854917-1099-3807-9620-0f25c6b692c3 | -6.71989 | -44.32137 | 2025-07-17 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| afb18bd7-eafe-31d4-9eff-c6c00c9fd1a3 | -6.62725 | -56.28416 | 2025-07-17 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38b73cdd-fc8d-306c-b27b-381b97f7b11c | -6.14307 | -47.31361 | 2025-07-17 05:12:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b51a6932-b30f-3fd6-9951-157dd114968b | -5.6597 | -43.71477 | 2025-07-17 05:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 6a01b91c-078a-308e-b301-3adca1499c78 | -9.41217 | -48.41251 | 2025-07-17 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 723db411-b30e-360c-82e1-730600d2ed4c | -5.96919 | -52.20361 | 2025-07-17 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4974d3f-df31-39c0-87a9-d76fa4b684ca | -7.8822 | -55.36781 | 2025-07-17 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c6be6ba-7e47-3bcd-9c3b-8bf0559f3d34 | -8.71108 | -50.05039 | 2025-07-17 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47f77470-9034-3b87-be03-3e350988230d | -3.84522 | -47.75178 | 2025-07-17 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58c90819-becf-3f7f-9d3d-83af85bf0b95 | -4.80508 | -43.22447 | 2025-07-17 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 956714cf-ce6f-3bf3-a6d2-0e254dae7b0a | -7.34569 | -44.19791 | 2025-07-17 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d92aa0e6-8c33-39ca-8a13-d0ba4d84c94e | -5.65877 | -43.72158 | 2025-07-17 05:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| af08aabb-029e-3835-9c43-d31754b28487 | -4.30071 | -48.10263 | 2025-07-17 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9f692f30-0ea1-3f1e-9039-99cb4e7fe198 | -6.6278 | -56.28061 | 2025-07-17 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d67bd6a-bca7-3fb3-8d83-74fd82045408 | -7.25386 | -56.2743 | 2025-07-17 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7777591c-929b-3aa6-8b6b-db0711d408d9 | -9.4105 | -48.41846 | 2025-07-17 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0be7dbdd-8737-378f-8781-19925eedd6c9 | -9.41603 | -48.41916 | 2025-07-17 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33f67a0d-e272-3dac-8058-69f124b03669 | -9.24679 | -48.559 | 2025-07-17 05:12:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8e84ec93-20d5-3a4f-b0a3-85e05e8800b6 | -9.24583 | -48.56627 | 2025-07-17 05:12:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| feba1d49-0de3-3761-8b27-1109dcddd285 | -5.7984 | -45.10488 | 2025-07-17 05:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 304855ce-1ecb-3199-8ffb-b6a8524e54b6 | -6.71209 | -44.32737 | 2025-07-17 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9e8fa603-d026-3414-a334-5a88a5f8b9e6 | -6.13737 | -47.31297 | 2025-07-17 05:12:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92a488fc-73f5-32ef-8798-58d20216d843 | -3.54909 | -53.57415 | 2025-07-17 05:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5363a3f-9763-3ddf-8d30-ce26bc853e47 | -8.53968 | -47.84867 | 2025-07-17 05:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bcec2be-3f85-388b-98e5-b70fa8732dd1 | -3.74289 | -54.26241 | 2025-07-17 05:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86eebedf-8fb3-33a1-a6f7-d2badeed1a37 | -9.4165 | -48.41546 | 2025-07-17 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09757caa-c8a6-30a1-bf00-90a3d917647e | -7.2114 | -45.33158 | 2025-07-17 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31d2fa47-6440-30a0-9942-6c0e38449833 | -6.42965 | -45.31216 | 2025-07-17 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ebc3c649-0450-3763-ab5c-1dd25161777e | -6.26958 | -57.40086 | 2025-07-17 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4dd9578-e3ae-3872-8006-b93aff8b75bc | -3.74219 | -54.26319 | 2025-07-17 05:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dfb3bcd-c4c3-37ba-b9af-16cbfd2a7872 | -6.7319 | -44.33662 | 2025-07-17 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 612fb961-d740-3b72-9f8f-4b5dd83e6968 | -7.50824 | -55.01096 | 2025-07-17 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f880986f-8ee7-302d-bc0b-e5621c28db23 | -4.10853 | -48.20779 | 2025-07-17 05:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 908af224-97b1-36cc-9c9c-31bc77b9bd53 | -8.04212 | -49.88786 | 2025-07-17 05:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88d5fe6f-e3dd-31c0-9b0e-8c81155ab100 | -7.35145 | -44.19804 | 2025-07-17 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08ce436b-6b50-3e92-baa8-93a5d84028b9 | -6.13791 | -47.30914 | 2025-07-17 05:12:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82f55f8e-8ebe-390c-a65f-5d94f46cfaa9 | -6.14361 | -47.30978 | 2025-07-17 05:12:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README27.md)
