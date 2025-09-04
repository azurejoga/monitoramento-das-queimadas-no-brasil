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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81e4049b-7699-3aa7-acba-f4707fcbdaf0 | -22.65517 | -43.6884 | 2025-09-04 04:57:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 809f64ff-9ac0-3489-84fb-a140363a2bf1 | -19.21949 | -44.4847 | 2025-09-04 04:57:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 103fdf19-17d4-363c-a270-14c70f79614c | -22.54747 | -43.56092 | 2025-09-04 04:57:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0fc7f2d4-99a4-3e72-badb-bd2e54187fc2 | -18.13952 | -51.79122 | 2025-09-04 04:57:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| da5ee17c-1a84-3b54-8f7c-2a456b38aa3b | -20.09583 | -50.01689 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| de12e80e-033f-3e60-938c-d2979fe27848 | -20.1058 | -50.00852 | 2025-09-04 04:57:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d15263a6-3059-3515-ab87-735794c447b4 | -19.26005 | -46.53513 | 2025-09-04 04:57:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26af7e8d-7e6f-3cc1-aca3-f04214408675 | -19.22239 | -44.48395 | 2025-09-04 04:57:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d06782ad-4652-31bd-bff6-80168af8a336 | -26.09381 | -52.76787 | 2025-09-04 04:59:00 | NPP-375D | ITAPEJARA D'OESTE | PARANÁ | Brasil | 4111209 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 283e48e2-3daa-3331-b93f-e517db10a849 | -26.09765 | -52.76847 | 2025-09-04 04:59:00 | NPP-375D | BOM SUCESSO DO SUL | PARANÁ | Brasil | 4103222 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 345010ed-6244-3ecb-a997-ff03252a9747 | -12.9006 | -56.9488 | 2025-09-04 05:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ecf21bd8-96eb-358e-9b3a-e87390dbd044 | -12.9009 | -56.9287 | 2025-09-04 05:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 6339388b-bf4e-3ba4-90cf-24e2f93ed3f8 | -6.7504 | -58.7268 | 2025-09-04 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 9d7f72d0-785c-31f8-a9a2-60551fc47e03 | -6.7649 | -63.1292 | 2025-09-04 05:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 111ef40d-1c00-33e8-85b3-d26f431dbf5b | -11.6836 | -57.3518 | 2025-09-04 05:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 255981e1-38d3-38bf-a253-4209bb48bd6f | -6.7319 | -58.7276 | 2025-09-04 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 52a4c403-c9be-3495-a3a9-758e25804fc2 | -4.9951 | -56.256 | 2025-09-04 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 1109fb46-7a67-377b-b2a3-28b324493b61 | -6.7503 | -58.7462 | 2025-09-04 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 40591322-dfe8-33d5-beff-c6e12c5a0731 | -12.9006 | -56.9488 | 2025-09-04 05:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 6b1c763f-05d6-34d9-bba8-f91149f43b1e | -11.6836 | -57.3518 | 2025-09-04 05:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| c007f2b3-5e7f-3470-ba0e-4857b9763769 | -6.7319 | -58.7276 | 2025-09-04 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 15719537-b847-3bcf-9bfa-408400a8ef45 | -6.7833 | -63.1286 | 2025-09-04 05:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| fa3cc1c6-031d-3f2c-a6b0-768737c83717 | -6.7503 | -58.7462 | 2025-09-04 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d2a3e3a0-0537-3ed3-9dca-c94b1a2b7055 | -12.9009 | -56.9287 | 2025-09-04 05:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| bf0e30f2-79e4-3e8f-933c-913feff61f01 | -6.7504 | -58.7268 | 2025-09-04 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 448fa432-b49c-355b-90bb-7c88a4e4e10b | -4.9951 | -56.256 | 2025-09-04 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 419d6065-e6e2-3d6c-9f12-32b3618d6a35 | -6.7649 | -63.1292 | 2025-09-04 05:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| f3c8f810-8d95-34d4-9967-48c070b3924a | -3.22817 | -47.12782 | 2025-09-04 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe070d44-bd90-3414-860b-bfa30c8afb1c | -2.96014 | -49.35353 | 2025-09-04 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee83306e-8f3a-3ff8-98eb-fc92bcad4f2b | -2.93243 | -48.82341 | 2025-09-04 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f7ad472-85ab-30ef-81a4-d62b6329425c | -2.95918 | -49.35989 | 2025-09-04 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58c4fd4a-96c3-3e47-9e25-06c8ef702d1b | 1.09005 | -51.31391 | 2025-09-04 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae28cead-cad3-3ac9-9799-a29be46a11b2 | -3.16173 | -49.47623 | 2025-09-04 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdcc2b6a-718c-3a23-9913-937e6daa3c29 | -2.95966 | -49.35672 | 2025-09-04 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98276c01-d587-3736-89f3-56de1dda9c32 | -3.22749 | -47.13238 | 2025-09-04 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c14ce015-6ac2-3c95-af29-f954aab64507 | -2.95871 | -49.36307 | 2025-09-04 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd0da94f-ff63-30bd-a2d6-627dcbfdf044 | -3.16647 | -49.48024 | 2025-09-04 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94c88919-c319-35ac-8213-ec3df187e311 | -2.93786 | -48.82428 | 2025-09-04 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 681e3590-f173-36b9-b816-51c8708eb57a | -3.22215 | -47.12904 | 2025-09-04 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6201fd05-0f16-3b34-81bc-c32e3249f5e1 | -3.22824 | -47.13 | 2025-09-04 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c8640a7-1582-3cbf-8618-598abf552a9e | -2.58515 | -51.92289 | 2025-09-04 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 563a40b7-4795-3ec0-a116-4921cbbc078a | -2.96395 | -49.36389 | 2025-09-04 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40e3601c-4b8b-30f9-9d6d-e1a4c1f51a22 | -3.22139 | -47.13146 | 2025-09-04 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b37d2996-69a0-3054-ba91-c7fb96968d53 | -3.16124 | -49.47948 | 2025-09-04 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c020ba00-7060-3a2d-a605-63d2fd9cfbb5 | -2.78141 | -49.61994 | 2025-09-04 05:14:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dc28e99-b517-3318-a550-40ae820822c1 | -2.95822 | -49.3663 | 2025-09-04 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c63ea1b-9171-3aad-95c3-0c540b080e1a | -3.22209 | -47.12683 | 2025-09-04 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c4501d3-1eef-3790-803c-bed76216387d | -10.44925 | -50.38906 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf51e487-70d2-3ae3-ac63-805cb81ecdd3 | -8.3651 | -52.5475 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4811c497-9777-3ec7-a16d-43a1f027da49 | -7.26634 | -57.55653 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 774a3a53-b5da-3ce8-a4f7-0adf7981564a | -9.61354 | -47.04223 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 229f92ae-92b7-3996-b58a-f980c1a8310b | -6.74788 | -58.72536 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cb4cda36-b402-320d-88fb-31525349d9fc | -5.60853 | -57.36348 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8e2a0fe-976b-3219-98a6-b3b91ebc8c53 | -10.47926 | -53.64103 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe845ad5-cc4a-39f5-b8a4-f7f95f8e477e | -10.46349 | -53.62563 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79f87089-0300-322c-941f-100a92b99031 | -7.71677 | -50.32437 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ceb60593-0c63-3e42-b460-044c8de05df3 | -6.84434 | -59.14885 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84c295db-ac7c-39d2-b7e7-20bd7b4e50c6 | -7.69352 | -50.26443 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45e245b0-1f2c-3d4a-96f9-b207fe4b7f91 | -10.09344 | -54.76297 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 587601ee-83dd-3d84-b78a-12a416d89d4b | -7.69933 | -50.26147 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86431427-15f9-3cf2-b41c-eb922ced1ab9 | -10.09649 | -54.77063 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db3aa443-8671-373f-9863-da80328fe4d9 | -10.94673 | -50.99124 | 2025-09-04 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24126154-03da-328e-86f0-daa5fb984d08 | -6.74016 | -58.73126 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9a197773-9d90-3dd3-aaf7-43d1e7d3ea8b | -8.43698 | -47.3353 | 2025-09-04 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35d2bce6-07c1-3050-89fd-eed69e5ccaca | -7.01768 | -59.66295 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7401354-0ea4-3a85-87ad-fe6f38c145cc | -6.7732 | -63.12933 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| adbcccb8-2f99-33e5-a6c9-37b939e5a567 | -7.25334 | -57.55077 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63bf6a70-6482-3b91-8bdb-a15887791819 | -6.88172 | -59.08384 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e7e0e6f-76b2-3135-8738-d08067ca9e30 | -6.79052 | -58.99495 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52cf7355-227c-38b9-aa58-e3597f9dfc2d | -10.15436 | -46.27417 | 2025-09-04 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ceb77c82-b8fc-35e6-b480-55dfa6cf4d76 | -6.75341 | -58.73334 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47ce5447-9dc9-32c2-932b-5f41ec3ee945 | -10.26815 | -54.26685 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96564457-e471-30a1-ab33-1fd9f62fff23 | -6.87263 | -45.5583 | 2025-09-04 05:16:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f626352b-877e-3699-a360-4bd707f4676b | -8.85686 | -52.01889 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bae36d9a-84e4-3914-a0a4-9863fe654144 | -7.33628 | -59.64661 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd9fa3c8-2b53-3e7a-94de-d7ad0a3711ff | -10.15514 | -46.26785 | 2025-09-04 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7da8efcf-e65c-3e40-8857-e34a08be7b7d | -5.60856 | -45.03065 | 2025-09-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 47c141ea-9001-3df4-a74a-5703c801ebbb | -10.02601 | -46.08893 | 2025-09-04 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd5c0e8e-decd-3998-b747-0c82324b9f1c | -10.52963 | -46.76351 | 2025-09-04 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b61eec1-9675-395f-a562-d5eb960e8e20 | -5.93489 | -51.97421 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e13edebb-2009-331e-bf33-c697c12154e1 | -6.09088 | -55.58995 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20132c45-e201-3b5c-9079-6712f9fb4965 | -6.87481 | -58.93381 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ba05766-3cef-3eaf-bdbc-ec8021f0e40f | -6.74402 | -58.72831 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4c9c4069-9907-39f8-8448-1d487aa93590 | -6.76107 | -63.13201 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 59be25fb-7fbf-3373-aeba-2c9c25bb97a7 | -6.73962 | -58.73472 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| efb66234-6800-3ac5-a2e2-92711c20fc13 | -6.74955 | -58.73628 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 2092aaae-648c-3831-9364-a412a814aa68 | -6.02363 | -46.67775 | 2025-09-04 05:16:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1566dacb-4bf4-37a8-a9a7-fd109fa96404 | -10.48306 | -53.64591 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc08c10c-16cc-3a05-8f9b-38d488faca50 | -9.47317 | -47.60675 | 2025-09-04 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 657e510b-19ee-3579-869d-c6a8be36f23b | -6.87085 | -45.5714 | 2025-09-04 05:16:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 77b6fd8b-3a2e-32d4-a4a9-d31ef327811e | -7.33352 | -59.64259 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 34bbbfb2-8636-3c80-8836-d3a828db1bca | -5.02649 | -56.10971 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66c87ff2-b0b2-3210-b672-2a7dd4537501 | -10.95076 | -51.0018 | 2025-09-04 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05707d4f-f322-341a-b755-00e13e0baecd | -8.531 | -51.32178 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 860fcc03-9179-34dc-86ac-d58df4fd0c1b | -8.53059 | -51.32001 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3de54f72-3339-36ff-8a61-e206ef698732 | -7.97009 | -46.34369 | 2025-09-04 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3e52296-7c2d-3039-8a94-ff7bc28ec539 | -8.36989 | -48.34642 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3ee90a2-2336-37c2-bc95-9fe34ef26086 | -9.25864 | -56.89672 | 2025-09-04 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab76d052-0ed8-3530-bba5-86fee83fdeb6 | -5.61247 | -57.36034 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f68229f7-3b52-31bc-84f3-d684c910f67b | -10.14896 | -46.26017 | 2025-09-04 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README80.md)
