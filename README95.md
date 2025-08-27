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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f0359f0-2298-34b5-82f3-b66c8faa1744 | -13.6097 | -48.2126 | 2025-08-27 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 3c86a8de-2acc-3528-b2e7-54ca48da23a5 | -9.4062 | -60.5326 | 2025-08-27 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 55cbd93d-4a17-3c08-8877-5519cec6caba | -12.7067 | -48.1873 | 2025-08-27 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 0dde8f7c-8c65-39d0-b5da-d13e0bb6a820 | -11.1583 | -44.7859 | 2025-08-27 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 3a19ca7a-9f3a-3684-90e9-d334a4664e43 | -13.5004 | -46.8609 | 2025-08-27 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 861ad85c-9011-340b-87ca-946dba74621e | -6.8774 | -43.5919 | 2025-08-27 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 306.1 |
| 29a47a47-f3a7-351c-b240-fcb46acb31fd | -13.4032 | -46.8987 | 2025-08-27 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| f2589b99-93a7-3e02-9e5b-0c523873799e | -9.1009 | -49.5621 | 2025-08-27 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| af16f30a-a888-3d8f-98f7-404360ea9827 | -15.6171 | -52.7207 | 2025-08-27 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| bd14e7e9-a28d-3517-88ca-3a751341a763 | -9.2092 | -59.4997 | 2025-08-27 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0d73a425-0073-37ec-83cf-9374419149d5 | -13.3843 | -46.879 | 2025-08-27 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| aa817e90-3308-3958-bf80-613db0ece878 | -8.2707 | -45.1377 | 2025-08-27 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 136.9 |
| c507b7c6-d8dc-36a6-be7a-1a73be5077dc | -13.6102 | -48.1903 | 2025-08-27 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| da8f3201-03a2-3627-9a94-7ea42a018053 | -9.0819 | -49.5853 | 2025-08-27 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 13aca166-4245-3421-804f-0ce5aeb3cfdc | -13.067 | -46.3382 | 2025-08-27 13:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 6e999682-903a-3a6e-aba9-180f040ea349 | -12.9068 | -44.658 | 2025-08-27 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 5ece05de-72ef-371b-8e6b-c9c572919f97 | -6.8873 | -44.4234 | 2025-08-27 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 35d8e6fd-a726-3ebd-98de-2c70720587c8 | -6.8772 | -43.6152 | 2025-08-27 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 283.0 |
| deb1eeb0-765c-3931-b623-0275e7533a8d | -10.4879 | -51.5953 | 2025-08-27 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e9a312ae-3c79-3345-82ac-62997fd2c6d2 | -10.6825 | -47.1412 | 2025-08-27 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 9460e545-243f-3388-b92c-ba812d2c68b9 | -6.8413 | -58.9552 | 2025-08-27 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| f61335b9-823c-3a40-a437-23f95a949c09 | -8.2519 | -45.1396 | 2025-08-27 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 604749d7-5d47-3c21-9e6d-eb697770b75e | -7.6411 | -42.6955 | 2025-08-27 13:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 205.9 |
| 6f70d235-0ab6-34be-86aa-f5110d45cdcc | -12.7447 | -48.2041 | 2025-08-27 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a3e98b67-e89b-3c24-9985-4ce71be8fa62 | -8.8839 | -60.7891 | 2025-08-27 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 0a590b5a-fe95-3c6f-a76b-f20d6c457c85 | -9.1007 | -49.5835 | 2025-08-27 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 189f4162-031e-3418-9905-3b6c40b2a90d | -13.4036 | -46.876 | 2025-08-27 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 214e000a-0bf2-350a-a9a5-575373296df6 | -8.271 | -45.1149 | 2025-08-27 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.0 |
| c1e09a25-36e4-3b6a-98a3-e5e3ed5b53cc | -12.9266 | -44.6314 | 2025-08-27 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 8f6f6e35-5cec-3e9e-8099-7abf1d113955 | -8.8842 | -60.7507 | 2025-08-27 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 205.5 |
| 9840a021-69dc-3005-bb00-e24fa4eeeae4 | -11.5694 | -47.6081 | 2025-08-27 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 68972adf-9c1e-3702-bb0e-c471d9c43860 | -9.4064 | -60.5133 | 2025-08-27 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| d851f7bd-10f5-359f-864d-840c74918b8b | -14.3344 | -53.0372 | 2025-08-27 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| a106791c-9f29-3dff-ab5b-d3b2a962e34b | -17.8471 | -47.7428 | 2025-08-27 13:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 177c4253-050e-3e62-8a53-989fd57c4c8d | -12.7263 | -48.1624 | 2025-08-27 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| f89dfc1f-cdbd-3a24-8d8f-a04c7f5a5a30 | -12.804 | -48.1072 | 2025-08-27 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 841e29ce-3f3b-3e97-bf4e-528b02314121 | -6.4357 | -44.5535 | 2025-08-27 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 686dea65-5931-3beb-9718-598fbe980c40 | -9.0821 | -49.5638 | 2025-08-27 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b775260f-a37b-3ed1-9a24-5787f17efe43 | -8.4596 | -43.6645 | 2025-08-27 13:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 177.0 |
| f7b4c562-a40b-38b5-aae9-751d3bcd682a | -10.6825 | -47.1412 | 2025-08-27 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d77b9999-3bf8-320b-8af5-17d99edae211 | -9.418 | -48.2756 | 2025-08-27 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| feabdd54-5023-328f-8288-d325b3e581d8 | -8.2519 | -45.1396 | 2025-08-27 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 9fc6b5cc-99ed-39fe-a234-7a695dea8a78 | -9.1715 | -59.5599 | 2025-08-27 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| fe3f92de-6af1-386f-b7f2-43123dc3defe | -9.4062 | -60.5326 | 2025-08-27 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| ac0a8b27-bd22-38b3-aa7a-5a0cf9e2f19d | -9.0819 | -49.5853 | 2025-08-27 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| b6101940-f009-3c3f-a9e0-47ab3b81c8a7 | -13.0674 | -46.3153 | 2025-08-27 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 26582f93-c300-3778-93c1-961ffc94b45e | -8.4593 | -43.6879 | 2025-08-27 13:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 181.4 |
| c084f888-46c6-3483-84c8-59c8307de1d9 | -15.6171 | -52.7207 | 2025-08-27 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| b5c75d76-b6ba-3c69-964a-bb6150a0bf02 | -7.6414 | -42.6718 | 2025-08-27 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 171.5 |
| b0b5f767-d0a5-3487-bf8f-a1cf964299fb | -7.5487 | -36.7602 | 2025-08-27 13:50:00 | GOES-19 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 114.2 |
| 551d1f90-46fc-36c2-94e0-d9eed6345f06 | -12.784 | -48.1543 | 2025-08-27 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b6e5b427-f155-3a93-b010-925accbbea4f | -9.0816 | -49.6068 | 2025-08-27 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| e2265319-883d-36bc-9f03-50d19dedd7ee | -9.6574 | -64.9845 | 2025-08-27 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c23fe17b-ec7c-31eb-bf01-e27fe32d2cb4 | -15.6362 | -52.7393 | 2025-08-27 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 4a02510c-fd76-314f-b73d-094a4cecff20 | -11.8307 | -46.8131 | 2025-08-27 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| aed3aeb1-65db-3670-8d7a-c076065446b7 | -8.2707 | -45.1377 | 2025-08-27 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 610e6e42-4c32-3aac-92cf-794924c2a321 | -11.9208 | -47.1375 | 2025-08-27 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b58716e0-cd18-3823-bdb4-6ea0af6775c6 | -11.1583 | -44.7859 | 2025-08-27 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c8fe570d-3f0a-39d9-b4f9-f6c075e73050 | -6.1783 | -44.0457 | 2025-08-27 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 2807d070-9be4-3368-be58-28332b8f8a62 | -13.067 | -46.3382 | 2025-08-27 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 298a903c-c384-33e3-abeb-ecd6a04c1ec2 | -12.8036 | -48.1294 | 2025-08-27 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a10ee278-cc43-3468-a4e6-71fec0ed94dc | -11.5722 | -46.2844 | 2025-08-27 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 12f4f96a-12f3-3dda-be49-51508f04440e | -6.8772 | -43.6152 | 2025-08-27 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 03db0de3-cd41-323c-b8d3-05a3ed46b3db | -12.9072 | -44.6346 | 2025-08-27 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| fb04b7e2-5266-3f3c-a5da-4ddb73b97fa0 | -14.3678 | -53.3481 | 2025-08-27 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 28fc2d63-7866-394c-89a9-d972ca9e22a2 | -12.9068 | -44.658 | 2025-08-27 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| edd70a51-4899-3e64-9bfe-a3f625fc9731 | -6.8774 | -43.5919 | 2025-08-27 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 313.9 |
| e1dd1d1a-32ab-349c-8330-32835cedff70 | -9.1007 | -49.5835 | 2025-08-27 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| bbbfcb11-463f-3754-9157-fbcbcefd9080 | -9.1004 | -49.605 | 2025-08-27 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 51062560-0d9e-3a56-935a-afc122a1f2c6 | -9.4064 | -60.5133 | 2025-08-27 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 86abe04b-2c75-31be-9af4-b751092831c6 | -13.3838 | -46.9017 | 2025-08-27 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 5823316b-f16d-35f8-b4fb-30a07ba2eac9 | -13.5193 | -46.8805 | 2025-08-27 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0af7cca4-1f4a-3be0-bdad-b5299f43d66f | -13.4027 | -46.9214 | 2025-08-27 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e0e61a7f-3796-31c0-a72d-15e41edc9450 | -11.3338 | -43.4979 | 2025-08-27 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 09329653-1ed8-3890-b902-e31d4525a4d1 | -12.7259 | -48.1846 | 2025-08-27 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 549252f1-67d7-3c8d-af00-2a1e76450687 | -13.6291 | -48.2097 | 2025-08-27 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 22d11e60-4ace-33a5-9b8f-6d6cce8678a3 | -9.8286 | -64.2824 | 2025-08-27 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| fd5c067c-f4ff-3b75-b989-eb01983e6e6d | -7.6411 | -42.6955 | 2025-08-27 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 179.7 |
| 1e10f71d-3a6d-3863-89c7-fed72de3c6bc | -12.7067 | -48.1873 | 2025-08-27 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 5caf0b9d-02b9-3574-b6ad-4850d1868e0f | -7.7741 | -51.0512 | 2025-08-27 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 0a3d256f-775d-32a2-bd86-9722abe6a6e2 | -10.2742 | -64.5096 | 2025-08-27 13:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 2495f20c-0fda-314d-b7e9-e7eac8011b82 | -13.5904 | -48.2154 | 2025-08-27 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 81c8ec94-1f5d-3aa4-ac90-cff9e35c4d60 | -11.5694 | -47.6081 | 2025-08-27 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 819a9738-4d46-3279-a8ac-208943cb0f8e | -9.2092 | -59.4997 | 2025-08-27 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 0a3220dc-3c5a-36fc-a7ff-5830ce0d9bd5 | -6.4355 | -44.5764 | 2025-08-27 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 496b864c-4329-32fb-8a34-bed127538c62 | -8.8855 | -47.1861 | 2025-08-27 13:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ca5257e8-1754-38d1-b82a-644e0ad0c806 | -8.271 | -45.1149 | 2025-08-27 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 8aa2a603-60b6-30e5-aa99-34eceef39391 | -7.5673 | -47.4851 | 2025-08-27 13:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 4af07d00-f89e-3d49-99cf-74763b4c8b02 | -9.4183 | -48.2537 | 2025-08-27 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 67ce3bf0-b724-34e5-9597-2e9e26f89b27 | -13.4032 | -46.8987 | 2025-08-27 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 5649a252-08d4-3c67-ab9d-69b58914bb67 | -12.9266 | -44.6314 | 2025-08-27 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| c9f6f2e6-bd56-3e39-bb86-fb1041589daf | -11.3146 | -43.5008 | 2025-08-27 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 67cfa7ec-45d7-3015-a966-0a545afdf10e | -6.4543 | -44.5749 | 2025-08-27 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 138.9 |
| c92b8746-dbbc-3e3a-b680-b3c88b679228 | -6.8875 | -44.4004 | 2025-08-27 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 16405e98-7f4b-3029-a014-5d993617f637 | -7.6603 | -42.6698 | 2025-08-27 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| a73cc05b-58da-33e8-8b66-57c4900490ee | -12.7643 | -48.1792 | 2025-08-27 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| c65a2861-e437-3364-b9d2-9f2fa10aba4a | -13.6097 | -48.2126 | 2025-08-27 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 150.7 |
| a9962764-63ff-3ee3-b2bb-d19814f744c3 | -13.3843 | -46.879 | 2025-08-27 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ddbaf204-c3eb-3f37-a60c-79d4b72b1b1d | -13.4036 | -46.876 | 2025-08-27 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ce268598-2d64-32a0-b4b5-1c038b54e3a8 | -6.62 | -53.3373 | 2025-08-27 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 262.0 |


[Clique aqui para ver as próximas entradas](README96.md)
