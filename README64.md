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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10cb0228-03fc-30ce-859f-2967e866060a | -3.11453 | -50.29025 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| af2071d8-a8e9-3da8-8ebd-a6701f87b488 | -9.23569 | -45.85419 | 2026-09-30 12:02:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.7 |
| c8b4e899-623e-3561-91ab-a708cf079314 | -4.14811 | -48.89472 | 2026-09-30 12:02:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 587513de-6266-3a71-b829-89b98e58cf68 | -3.10815 | -50.27106 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 63bcc4c5-6ef3-3952-83aa-41c8e61647d2 | -3.55049 | -48.17823 | 2026-09-30 12:02:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8af1e446-868d-302d-9f18-4f2bfad8596a | -8.25774 | -45.44433 | 2026-09-30 12:02:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 8e989e34-961c-3218-92c4-79eac9bafe78 | -3.38266 | -50.93938 | 2026-09-30 12:02:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 5fe60473-b9fd-35db-ae50-b0b36dc38aeb | -7.02121 | -45.29766 | 2026-09-30 12:02:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 4662e2c3-6fbf-3bcd-86e5-f34749de1f62 | -9.37768 | -49.15491 | 2026-09-30 12:02:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 29d2fdba-c78b-33db-88e8-29579b71bada | -3.96705 | -48.1256 | 2026-09-30 12:02:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 58fe900f-f386-3869-ae3d-710d86d97346 | -3.2524 | -50.81044 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6033c3e2-9676-3e5c-9f4c-0feac9229e0a | -2.48365 | -49.33856 | 2026-09-30 12:02:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5111011f-a262-35d5-8198-dc3b1a6bd00e | -7.51181 | -55.0253 | 2026-09-30 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| abaa4eba-3d55-34c3-bad6-805bc89bc60d | -7.51017 | -55.03611 | 2026-09-30 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 93a1f71b-b0e4-31ca-b25a-29e2afaf4867 | -9.85993 | -44.96772 | 2026-09-30 12:02:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 34.4 |
| b60a70cc-f409-3256-97b7-3d9521398e77 | -8.91589 | -44.96223 | 2026-09-30 12:02:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 3123bb57-af7a-30ca-b27e-553ba0902629 | -8.3206 | -54.75164 | 2026-09-30 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5da29b28-2ce3-381f-80b3-facdf77b1c4c | -8.99183 | -51.25076 | 2026-09-30 12:02:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b93e2fde-a44a-30c6-8830-b66fbd0c403b | -9.76818 | -44.8151 | 2026-09-30 12:02:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| cbed88e9-7f59-37d5-ad46-40b8b8447412 | -6.90233 | -43.68988 | 2026-09-30 12:02:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| ed54febd-8fac-3e48-b0b3-ad9c42eaef57 | -4.36473 | -47.77149 | 2026-09-30 12:02:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1359e546-a1da-334b-a1bf-863e0106e084 | -7.482 | -45.78718 | 2026-09-30 12:02:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 9d0f6759-955b-35eb-9944-9627cb71ad3d | -5.86343 | -51.78791 | 2026-09-30 12:02:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| c511e047-7a7c-3656-b78c-cecd13ba5585 | -8.04196 | -54.89437 | 2026-09-30 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1277fec4-2c00-311f-bc43-979c2abd18cc | -3.9622 | -49.04659 | 2026-09-30 12:02:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5ea8c2a5-db9c-3413-900e-05f8ea47a863 | -4.84807 | -50.68276 | 2026-09-30 12:02:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ae84c15d-33ad-3d1a-bb1d-d5fe40ed13f3 | -7.52306 | -44.54566 | 2026-09-30 12:02:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 56b9f195-a234-333a-ac84-c4be9135d649 | -2.34478 | -49.13691 | 2026-09-30 12:02:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 36f261cd-0bad-3505-8010-5b90c84433e1 | -7.00166 | -43.74339 | 2026-09-30 12:02:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 713f1c33-80f3-3884-866e-e9810f564b0e | -3.37616 | -50.84241 | 2026-09-30 12:02:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6bca93ac-7924-3c5b-a296-bc762379b23d | -3.24886 | -50.12143 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 59cb645e-dc7d-3519-a08e-190e3129e3a6 | -8.91884 | -44.93821 | 2026-09-30 12:02:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 9907d0b0-0403-3dc0-a832-78ff6aef7de2 | -8.29839 | -54.70645 | 2026-09-30 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d4db8683-60b5-35e2-b5d8-c92906434fd2 | -3.83854 | -52.26548 | 2026-09-30 12:02:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4d7e1384-b23c-3b22-903b-ee5ededc6971 | -7.53003 | -44.52827 | 2026-09-30 12:02:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 59dc7ad2-a6a4-3e72-82fc-1ea7e4feb020 | -3.0367 | -48.4153 | 2026-09-30 12:02:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 42a1f21f-fc17-31a0-94bd-395e5e6cb345 | -9.8703 | -44.96245 | 2026-09-30 12:02:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| c02a5d77-80dc-32f1-8543-84a6451150ee | -2.36949 | -49.22896 | 2026-09-30 12:02:00 | TERRA_M-T | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d1cda243-d936-3bae-ae92-3e9482bbb65d | -3.29631 | -50.3094 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8590126d-1cab-3dda-9fe2-82d8a0110670 | -3.98413 | -41.5148 | 2026-09-30 12:02:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 41.1 |
| 63280206-2873-3ca5-912b-2a835c2d5057 | -3.51631 | -50.31531 | 2026-09-30 12:02:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 190664ea-9f81-3717-b0ba-fbd2d351c46a | -3.10689 | -50.28004 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 7662f9ae-98e1-3e7e-9374-4e44d4fcc739 | -7.87522 | -54.70773 | 2026-09-30 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4e3c3452-27bc-39ce-a7c2-d9c4fda8cc70 | -3.38142 | -50.94815 | 2026-09-30 12:02:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| bd64e1e0-2583-37a6-9fc2-491b902b36df | -8.25648 | -45.42791 | 2026-09-30 12:02:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 8fe29e29-490d-37bd-acf3-11bcb0e1f39a | -11.7989 | -50.45816 | 2026-09-30 12:04:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3131716d-defe-39b3-b9dd-f68e83460336 | -12.07015 | -46.47076 | 2026-09-30 12:04:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 9cfc38b4-dd14-3891-9be1-7783711143a4 | -14.9113 | -51.87782 | 2026-09-30 12:04:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| da6cff26-0306-345e-ad59-045b3199defa | -9.92715 | -50.15249 | 2026-09-30 12:04:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 70dc6b50-0d8e-3931-aeba-8b638bdf75c1 | -11.83926 | -50.48036 | 2026-09-30 12:04:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d8502c94-9612-3393-abd9-373afed838be | -11.82969 | -50.47908 | 2026-09-30 12:04:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 18259d4a-074a-3b35-99b9-cd345f290d77 | -10.5219 | -45.36413 | 2026-09-30 12:04:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6ae814f4-de09-3377-9115-6381071efbdc | -14.90343 | -51.86662 | 2026-09-30 12:04:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| dfdadd30-86e9-375e-91bb-a931bc11880d | -9.6945 | -58.1153 | 2026-09-30 12:04:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7b538a6b-b60f-3f6d-a14a-65bb7588e5e5 | -12.42163 | -54.10575 | 2026-09-30 12:04:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8697df77-7bd4-3981-8b79-d3ab068dc207 | -12.61859 | -47.23862 | 2026-09-30 12:04:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b06c615f-4547-36d9-8af9-7d9b1bf15ccb | -12.36609 | -46.382 | 2026-09-30 12:04:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 782884d1-f1da-3444-acd8-928d94f62a3a | -11.4398 | -43.43225 | 2026-09-30 12:04:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 8850c6a2-01d9-3aad-a743-49f53c56ae1f | -12.07269 | -46.45007 | 2026-09-30 12:04:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b6a0e739-6d6d-3965-9ab3-889ac476c983 | -12.2245 | -50.26926 | 2026-09-30 12:04:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 6596ec98-ee02-3a19-a676-78fa409b5c61 | -14.50727 | -48.27678 | 2026-09-30 12:04:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a1557cf1-8406-3618-907c-84deb04d1aa4 | -16.09635 | -49.72102 | 2026-09-30 12:04:00 | TERRA_M-T | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3c65d782-b482-3fa0-9d08-e4e86f2c43a9 | -11.20471 | -45.14049 | 2026-09-30 12:04:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 37d234f2-bd52-3cf4-989f-c25507a84fc0 | -10.7421 | -50.50369 | 2026-09-30 12:04:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| abecbbe6-409f-37ef-b098-751640052eb3 | -12.49333 | -49.12119 | 2026-09-30 12:04:00 | TERRA_M-T | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d60ccf0c-7c5e-38e3-80e7-544543ce93a3 | -12.60627 | -47.23714 | 2026-09-30 12:04:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 95523795-6e37-30d7-9cab-5671150a5e65 | -14.90209 | -51.87654 | 2026-09-30 12:04:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 154.8 |
| f56fba06-8ee2-3f56-87fc-8cfb94da32f9 | -14.90076 | -51.88646 | 2026-09-30 12:04:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1b49f097-b25f-3a9a-8af2-04bbb3e976bf | -12.88815 | -44.83098 | 2026-09-30 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 4b12c5cd-df52-39d4-bc25-0b9d97c9dd1e | -11.41621 | -43.42485 | 2026-09-30 12:04:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 5a678daf-f742-3032-90f5-56703a2f9053 | -11.82619 | -50.47266 | 2026-09-30 12:04:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 8281764e-ed04-3d4d-ac06-e128d6db7c6b | -10.2934 | -44.61713 | 2026-09-30 12:04:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 7857cc1b-d411-362c-ba3b-860a94e95706 | -10.51877 | -45.39003 | 2026-09-30 12:04:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| fc958411-b77c-360a-a333-8a48113744c1 | -13.35751 | -46.82113 | 2026-09-30 12:04:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| fc2bdcbc-1033-3266-b144-be744a5e0b97 | -10.52465 | -45.39803 | 2026-09-30 12:04:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 69f18953-5f2b-3e15-8c46-4ce4c4cdbb14 | -11.19798 | -45.16161 | 2026-09-30 12:04:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| af637c74-0606-31e1-ada4-9736230fade3 | -12.6032 | -47.23098 | 2026-09-30 12:04:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| e9efeb83-f967-3a85-a00d-f76f4c13ac93 | -12.89029 | -44.80679 | 2026-09-30 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6d06fc09-41fc-3b81-b19f-720460e6cae0 | -14.32959 | -44.91131 | 2026-09-30 12:04:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 9d88a0c9-5bc0-330c-bd23-6accfaa545a1 | -12.61553 | -47.23244 | 2026-09-30 12:04:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 4b87cd49-205e-3689-b85c-705c6dcb808c | -15.4181 | -50.34753 | 2026-09-30 12:04:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 828079b6-b7b7-3247-89fb-4ce71aa6da63 | -14.33166 | -44.9064 | 2026-09-30 12:04:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| b1ad5170-0be6-3497-9443-98dae12ef4ed | -14.89422 | -51.86534 | 2026-09-30 12:04:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 78df319c-99bc-3826-949d-3ba0a6619dcc | -15.41965 | -50.3355 | 2026-09-30 12:04:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 49f40479-8270-3eb2-80ec-1501f2f66c19 | -14.89554 | -51.85541 | 2026-09-30 12:04:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 2950598f-8603-3d17-8cdd-ecc2be6e9b4a | -12.22111 | -50.27415 | 2026-09-30 12:04:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 7dd08218-1252-3d29-aacb-a84a94dbe6ba | -10.52757 | -45.37221 | 2026-09-30 12:04:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 85788e4a-5468-31e5-abea-de5c15cd2e06 | -14.98567 | -46.57211 | 2026-09-30 12:04:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 99d46823-6a08-3072-b6c1-5f1846a3e2bb | -12.77172 | -47.24546 | 2026-09-30 12:04:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| c642d5ae-81c1-34a3-a700-32af96cababc | -11.18993 | -45.10733 | 2026-09-30 12:04:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 32248513-b116-33cb-bf69-286c6b55a5bb | -11.38699 | -43.46245 | 2026-09-30 12:04:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| c573f970-0fce-30a4-b948-3b21f6577a32 | -10.74009 | -44.41764 | 2026-09-30 12:04:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 2a5d13cf-efe3-31a1-9221-f9bf0d4c798d | -14.40827 | -51.29606 | 2026-09-30 12:04:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6498628c-918b-36e3-a5a0-2699dc29f9d7 | -14.10845 | -46.274 | 2026-09-30 12:04:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 6d3f4f51-21c7-38d8-988a-97fd7d4c1cf2 | -11.20115 | -45.13499 | 2026-09-30 12:04:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 80017b12-6606-3fbd-a248-e4d6b91fab57 | -14.40963 | -51.28565 | 2026-09-30 12:04:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8bccc6a9-452a-35de-8243-25b4a301ce8e | -10.70102 | -50.48177 | 2026-09-30 12:04:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b7234ccc-6a98-3cb7-ac87-adb243906bdc | -12.07048 | -46.45666 | 2026-09-30 12:04:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 434bec6d-e82d-31e4-977a-4b54ba32f864 | -16.09468 | -49.73473 | 2026-09-30 12:04:00 | TERRA_M-T | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e0a4bd5a-51ae-3670-ba37-71b43b7aa6fe | -13.52837 | -49.17118 | 2026-09-30 12:04:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README65.md)
