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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0bc8764-29b1-3bd5-b2db-c0c93c5df31d | -2.76468 | -51.69293 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d620fd7-3837-3669-9a67-d1888a17f2df | -1.31619 | -51.73278 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2aeeb44a-8e12-33b4-819d-cd2a74a3b377 | -3.00917 | -52.02293 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61c1f500-3365-3b76-98ff-6ccb45c5244d | -3.2057 | -53.12756 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3002764d-f78e-327e-b71b-2d493a4f9810 | -1.50633 | -52.56891 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be50adcd-fafc-3a9a-b96c-ffcd85365be1 | -2.23584 | -50.57333 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aadfd4bf-d0e8-30ae-a998-ee12fc133fee | -2.22646 | -50.84985 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da12f3a1-91bc-3999-8e61-e9cdeafb3817 | -1.78406 | -52.74878 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 048e2887-bda5-3a66-8341-29940d72bbbc | -1.75527 | -53.64153 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 765f22ca-87ba-3b63-a1a3-f4602b5a6c0e | -3.12302 | -51.78986 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73b92326-dfba-3cda-a4c2-5f53b08ec058 | -1.48694 | -52.41646 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01b52975-f078-3f0c-a430-c2516731d02e | -4.0889 | -51.11676 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a080771-068f-304d-bee6-e7daf7fd7ab7 | -3.44224 | -52.04459 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0ed406f-e59d-319f-a9e4-0a5c2a3ea885 | -1.1086 | -52.30024 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6b10e98-6497-3116-b5b3-ca8e7176c4c5 | -1.00131 | -51.71579 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15e6567b-cec2-3d1d-abcf-e63efce096b4 | -2.45098 | -53.66542 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 472ed721-2e09-3c1d-bf30-481b5ab1159f | -3.14449 | -53.8381 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8702ac22-d7ff-3aa8-b489-6dcc3006f727 | -2.36369 | -50.42651 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e1b2820-c4c4-376c-bbe4-1ff0ed80ac92 | -3.55546 | -51.44643 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6243104e-b1a3-3b91-a792-5f5d707c430b | -2.37192 | -50.39594 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f6492c2-33f1-34dc-bc57-e6e9004ebb1d | -2.22687 | -50.782 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fbd67b0-298d-33a9-902a-9dae32632d54 | -4.01864 | -47.00069 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 20b2ded6-1f2d-3a99-8a83-438eece69d27 | -4.70119 | -42.39993 | 2024-12-01 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7dc1e9b8-5921-3d51-a34d-eec3d0342177 | -2.58772 | -49.22078 | 2024-12-01 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b6ba26b-6e9a-37c6-9900-b50f058db899 | -2.29499 | -50.68903 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6846754-c555-3bb8-bc21-97c2c295f4f2 | -3.05747 | -53.17184 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdf79060-f050-32fa-89de-8848b03b5844 | -3.48098 | -53.80957 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c46537d7-5994-3815-9e00-225b1bfa6b61 | -3.89821 | -52.1637 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2c8ffa0-3adf-345d-bad5-56d644ffc355 | -3.25349 | -53.85749 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec0ef967-de75-3fc8-84f7-771b437c881d | -2.82515 | -54.07401 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 208a657e-2cd5-360c-88ab-a0c496990c05 | -3.11165 | -53.80558 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1c43bf3d-7e72-33a2-9925-07886b9b56ea | -0.5978 | -51.69962 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3f4a3962-74a8-3af5-bed3-9c13d5b1b9da | -1.72581 | -52.48016 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d84464ca-aace-30a2-9582-c65730c61cba | -4.10084 | -47.81134 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f62ea03-4968-3747-8891-4036b9ed7bf5 | -3.58502 | -50.51222 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21a5b3f4-de99-33ad-959f-ae80fe1ea930 | -2.46751 | -46.56672 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b5d24b3-8165-388d-9dd0-163e62a3079d | -4.77927 | -44.81117 | 2024-12-01 04:44:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 834d1427-4c87-3e70-856a-b99a6fb147b3 | -2.31683 | -53.8511 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb2cf6dd-b381-3c4e-b21e-7f1d81747b85 | -1.63819 | -53.86967 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 382d1b76-b12d-32f4-b696-5747713c5daf | -3.25112 | -53.92072 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d813d0e0-6892-3969-9ed7-215adea9ff0d | -3.75791 | -52.27436 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd8c150a-0115-306d-a463-03f6a8f1c94d | -4.05016 | -46.82314 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51c090c5-9667-3a4f-a968-57363b572f5d | -2.56198 | -46.56791 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16a9280a-8aa4-38b6-a79c-eff8bee7beaf | -3.06121 | -54.04757 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 162f6676-3b73-3d81-8a3a-b8942c96ee7d | -2.49852 | -51.95906 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feaf4a07-0ed0-3824-a584-fc1cf3e7da78 | -2.19322 | -53.77623 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 04646448-f23b-3250-9362-be7283b31740 | -3.48615 | -53.8135 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8abe9d1c-9a57-39e8-a09e-fde74896f954 | -2.59778 | -46.57142 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ad80c8a-263c-35ec-acef-db55aaed79f8 | -1.28435 | -51.6672 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7dd1d59b-b908-3445-9caf-a343057ba0ec | -1.07275 | -53.2178 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4ac308fc-d129-3bfd-81fd-7d5de897441c | -3.31526 | -53.8607 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc4e1c15-83cd-3866-a1f6-4c203a142546 | -2.476 | -54.01196 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 266dccd6-ac33-3104-a816-6aaa43d1069b | -2.90124 | -51.58196 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9899cb98-f2fd-3633-92a7-d5e0976efe32 | -3.25842 | -53.63644 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9869ec36-ae15-337f-8492-d234f1e14eff | -3.95112 | -49.90717 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 441d8e8e-85c6-3b89-9a65-cdd3aa67e48b | -2.65509 | -51.87766 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9371ad4e-978e-33f6-b53c-ae5319a865a9 | -5.10868 | -50.61336 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a1efae8-f10d-3057-8052-d548a3a51818 | -3.09655 | -53.29563 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cabaebde-4d54-32db-857c-03b52e72c954 | -2.78624 | -51.66669 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f7883b0-1fd5-3f6f-8294-9ab233d6fdf8 | -5.53858 | -45.43343 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11226669-4374-3050-abb9-3a59bb5a4d34 | -3.93523 | -46.722 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e93cc3f-8781-38ea-91aa-554d7e49513c | -1.14387 | -51.67233 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e2778b5-0e8d-308b-bbd2-0c1e299b0fe4 | -1.9074 | -52.87322 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cada856-c1b9-3c7f-b628-7e0f210c9c34 | -1.02805 | -53.55252 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5572d96f-e384-3486-af1e-70304065c5da | -1.46147 | -54.3645 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f875d22d-21c5-3a43-b68e-2318236131dc | -1.23511 | -51.80006 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc54dda1-acb4-34f1-b437-109d1a4ce8c2 | -3.05634 | -51.05867 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 71463ec8-e0d2-3e69-9108-c2d1c20d42ce | -4.17636 | -48.62176 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0898b895-3555-33c2-9526-c5c89a8067ef | -1.18683 | -52.12537 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 31074ccf-bd6c-3443-b2c5-59b810375653 | -2.60518 | -46.57259 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a135f5ae-49cd-3c0c-b483-1fe06901be28 | -2.8609 | -53.99616 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad7c3f50-6f27-3bcb-b2ed-3f4f2bf155df | -2.46167 | -46.56797 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 162928b9-3b1a-3362-98e4-d5d3e33376ac | -2.63237 | -54.21868 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d918ff0-266d-3a0e-b17e-d05760f80abb | -1.28588 | -51.72424 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77b995b7-c7af-3a4b-a2c6-cc2e6c70ed43 | -3.46766 | -53.49426 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 365313fe-81ed-3ab0-9b88-ba5cc27ec3b8 | -3.76345 | -50.1759 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f67e868-e564-315d-ba81-5571bd13b8db | -3.85776 | -47.05208 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d797ef41-bec4-30f5-a49e-4b6b39e4ece9 | -1.70032 | -52.64202 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2bfa015-8507-3509-a7a3-c997910a1ea0 | -1.26898 | -55.7599 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e002d711-fe23-3fa1-a174-4ca504abb9e2 | -2.25968 | -50.35737 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72aca80c-b243-35fb-a511-a5b578085b09 | -2.97427 | -53.28978 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e4620e1-47cb-3372-a498-caacf962dd34 | -2.83741 | -54.11812 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffe778b4-9607-362a-8bde-e77e701be3fc | -2.3221 | -50.64701 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f31b876-71b4-319c-bcfa-a7e9993095fe | -2.12024 | -46.55592 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e118ac6-576a-3bb6-a622-7b588a6d248a | -1.72519 | -52.48407 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 691af18d-bc37-3c6e-9303-4e8b4d0c39f5 | -3.25979 | -53.62792 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f33b5b87-b3bf-3018-9dd0-518ef68d0d13 | -3.20232 | -53.42589 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8340f3a-e592-31d9-b872-920d532db687 | -3.02999 | -51.53933 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 064dd362-efe0-37ac-b43f-33415c7f8fdd | -3.259 | -48.77449 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b704f3e-4ee6-3b27-a98e-6e4a36e593af | -3.2248 | -51.72014 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fab95c1-2371-3d7a-8a43-83ff7116a635 | -5.18691 | -43.95391 | 2024-12-01 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b0e7940-bc73-3617-b522-f20bbc65983f | -2.48217 | -54.02371 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23c2d3d2-0043-31c4-883c-374052ddb982 | -2.67833 | -46.60015 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a664be93-8ade-3906-bcd7-7a58a94b57fa | -4.41243 | -50.69851 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36a8a9e6-ac56-3b0d-96cc-633b4fd941cd | -2.85904 | -53.93608 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82b07681-c269-3ba4-8adb-9e4cca62e7c5 | -3.15259 | -53.83498 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 586daf5c-74d0-302e-a64d-be1d48494285 | -3.49281 | -53.81907 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ccf4847-502e-3d8b-95e7-85e1e6b1ba50 | -2.33104 | -50.67686 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b6d9ed6-691d-3fae-8617-9db2938c2e14 | -4.08162 | -50.02692 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ded61f8-1842-3988-8b87-c7534719c73f | -2.81047 | -53.05244 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README53.md)
