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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cf2fd16-3717-3f42-b157-6376325a69f9 | -4.82082 | -44.3529 | 2024-10-04 04:32:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 287c99b2-87da-3321-9122-53ea7a04975e | -4.81721 | -44.35236 | 2024-10-04 04:32:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a781554-38b0-38bf-a1ed-35169152036d | -6.3471 | -43.77913 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| becd896a-1803-3982-a988-3c3dc84b7db9 | -6.3263 | -43.74099 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b63be12-e798-3a95-96ab-a2f6258dabc9 | -6.32595 | -43.73825 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c4e8d29-41d3-3483-9885-de9765c170c1 | -6.14489 | -43.81894 | 2024-10-04 04:32:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cddae94-5092-332f-b959-b22aa7b7cfd1 | -6.14421 | -43.82351 | 2024-10-04 04:32:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2816b834-ecff-3987-8515-876f7e98b064 | -6.14112 | -43.81837 | 2024-10-04 04:32:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1adec58-42e5-3f73-9e10-178d09b4cecc | -5.89417 | -43.87336 | 2024-10-04 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9f1e026f-5a1a-3473-b16f-c1207358bcb2 | -5.89351 | -43.87786 | 2024-10-04 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 99ae547b-4887-3e37-a7b0-4edbe5fb421a | -5.89043 | -43.87275 | 2024-10-04 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| efd1ca9f-45cf-3f5a-865a-5382cfa98512 | -5.88976 | -43.87726 | 2024-10-04 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bc39a91d-ad5f-3f31-913a-7484f7b1badd | -5.8416 | -43.88605 | 2024-10-04 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d7bfa76-e529-3506-a0b9-ef10d2e2d01a | -5.83078 | -43.95714 | 2024-10-04 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 269f7d4e-9da7-3fc7-be47-118fa4a5138c | -6.11282 | -44.05809 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c58899fc-37ca-3dfb-9233-c4a41d87c51b | -5.97047 | -44.00626 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fe25046-3a71-3039-b922-996681b4f224 | -5.96741 | -44.00121 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21199b60-dbf0-318f-b66c-5dbdf309bb62 | -5.55981 | -43.7364 | 2024-10-04 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20928080-62bd-3380-b13f-8bba7f697ea5 | -6.40034 | -44.74435 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cbd2ac7f-cba8-3db9-89a9-7ab84aafee3a | -6.3122 | -44.34176 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fa8b253-4ed1-3528-9867-2f866c778a79 | -6.25981 | -44.80521 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a769f236-4f5a-3e6e-8d6d-7a9af11fd818 | -6.25296 | -44.14477 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 134929fb-6c9b-309f-986e-370c85eb4f5a | -6.25229 | -44.14919 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 010791ef-c4bf-3fed-a08c-76c0dd9c66b7 | -6.24993 | -44.13979 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ac62ed4e-3924-311e-bb73-e30d49a79267 | -6.24925 | -44.14423 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 820304dc-436e-3525-b204-ef84780f236e | -6.24858 | -44.14861 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 66ef525a-3cf8-3547-84ad-fa71571c8102 | -6.24792 | -44.15294 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b88a98e0-6871-3831-bba0-a44af443c577 | -6.24622 | -44.13924 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 406b4fba-7793-322f-bbca-d4443fdc15e0 | -6.24554 | -44.14368 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5e282c74-e674-3543-b4e0-b23765bd702e | -6.24252 | -44.13861 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0491b8b-5ffc-3704-8c65-1174e22f2d25 | -6.2078 | -44.14232 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d809cfc-fbca-3d20-b8bc-38c87d6f49fa | -6.20682 | -44.32338 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93b36291-e739-3f11-a0d9-7ab4980c54b8 | -6.20543 | -44.13285 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8e0ad04-8695-390b-adb4-2d1e9670b64c | -6.20411 | -44.14168 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9ca7c45-2185-313a-9454-37498a8fe1bc | -6.20316 | -44.32274 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f109ce95-fbe8-3314-bc97-1184dc16e847 | -6.20173 | -44.13223 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7547fe8d-77d7-3751-9042-61d53b95459f | -6.20108 | -44.13659 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f69ceb4-12e7-31ba-b826-17761f200458 | -6.19672 | -44.14033 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8897998-be38-3950-9c8b-7021e560f7a5 | -6.18691 | -44.12981 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2534462-310a-3e5e-a8f0-66d72ba10e49 | -6.18627 | -44.13412 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63c42977-6939-3e12-90ad-be622e2baa91 | -6.18319 | -44.12933 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7f98709-e8eb-3ebd-a2f0-5edfe42a8b92 | -6.18012 | -44.12449 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de29193d-bc44-303c-a1cf-48c333a6a1f5 | -6.17947 | -44.12885 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f548669-d9ee-315a-b3ae-a9b3f35c6542 | -6.17818 | -44.1375 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8affdf90-5918-38ee-b25d-99b7611c1901 | -6.17755 | -44.14172 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34bc3fe3-3d3e-3f18-bda2-73db1688c334 | -6.17447 | -44.13695 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f862d300-408d-34e1-87d9-4d79392bee58 | -6.17384 | -44.14116 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 241734a7-cfb1-3d42-8b57-88a6219a2ed0 | -6.1695 | -44.14485 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3fa49d8-3d8d-330e-b6aa-ea8585e7312f | -6.16641 | -44.14016 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc6246e8-9d17-377d-b11b-8a11478ac88f | -6.15525 | -44.1387 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc5f4147-436d-3086-ba7a-ed235db2c65c | -6.15347 | -44.14063 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9daaa6e-4fc2-33fe-81e8-5b24808f9915 | -6.15091 | -44.14243 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5b5988c-34ba-33eb-913d-607c7e289765 | -6.15028 | -44.14668 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d76a1065-1c9a-3c17-b916-671b8b6552ad | -6.1491 | -44.14441 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e3cf5e6-346f-3725-9f66-46ffac8dd004 | -6.14845 | -44.14861 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a185314-5b56-3336-919e-d44f051fa585 | -6.14656 | -44.14624 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17219774-9a02-30a4-a46d-63d366c3ce12 | -6.14538 | -44.14391 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32f5b850-8b6e-31ba-bb94-2204cc2c9f33 | -6.14474 | -44.14812 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3779ea37-1618-3dbc-9795-0bd98d4c617d | -6.14233 | -44.13906 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a1b7d1cd-e0e2-349c-b252-40a08e994ce0 | -6.14168 | -44.14333 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5699b4d-090f-3212-991a-780aca1a09a0 | -6.14103 | -44.14756 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3ac3617-0538-3b0e-ab93-b43a786d9904 | -6.13862 | -44.1385 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 83c5b434-a75b-3ad3-8144-8f5fb675a302 | -6.13797 | -44.14275 | 2024-10-04 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78b50b1e-fcfb-37fa-8f46-da3304e8646e | -6.07702 | -44.71576 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6a913ee-912f-3f72-8f38-9df0d0ad8ea8 | -6.06676 | -44.63176 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7dcb9c14-c154-3e70-95e9-7e5c532f7f5b | -6.06613 | -44.63586 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b356849f-486e-37d8-b5a4-f65e91afa532 | -6.06315 | -44.63123 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c6e23765-49a5-34d2-bec9-b0da77c79b42 | -6.06252 | -44.63532 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c88fd008-72be-3743-a8b7-9150665bae4d | -6.00693 | -44.56314 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7078c2cc-7862-38c4-aa2b-0eb93442a75d | -5.82945 | -44.13029 | 2024-10-04 04:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 4c5096f4-1e4e-34ce-a74c-c30c3133f3aa | -5.82751 | -44.12744 | 2024-10-04 04:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 73f5bb43-de0e-3fbf-a7d0-0bf9b7415710 | -5.82684 | -44.13179 | 2024-10-04 04:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 94d88a2f-c446-3438-91f3-68c79928514a | -5.82575 | -44.12975 | 2024-10-04 04:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 471844a7-6af9-33fc-b31e-acfb60b6db18 | -5.82511 | -44.13411 | 2024-10-04 04:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c08174b5-f59f-3a47-83e7-e8fb00b2e23d | -5.82381 | -44.12688 | 2024-10-04 04:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 02d8aa0f-b206-364b-afd1-541275627549 | -5.82314 | -44.13124 | 2024-10-04 04:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 15a55a21-cb6c-3d8f-96d0-de8bb8cc1b86 | -5.82079 | -44.12194 | 2024-10-04 04:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a70df9f3-5328-36c8-a20b-fbfca1b3c8cb | -5.82012 | -44.12632 | 2024-10-04 04:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 153dbc30-624e-3d42-9372-9e62dabe4863 | -5.42637 | -44.83054 | 2024-10-04 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d51d5ae0-58d5-34f8-9f89-7bfacd31d291 | -5.42577 | -44.8345 | 2024-10-04 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 085034be-66c5-3140-acec-27098d3f018a | -5.42282 | -44.82999 | 2024-10-04 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d21fb3d4-56f1-3163-9f4c-41a463b5ace7 | -5.42222 | -44.83396 | 2024-10-04 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5a72680-f5f3-3ded-8947-ff2804cdd86b | -5.31065 | -44.85881 | 2024-10-04 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a03efa5d-6529-37e3-bc8f-3c0d576b7f15 | -7.86788 | -44.80889 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c8245685-050c-34eb-99b8-1055a9b58ee8 | -7.86719 | -44.96027 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44b6129a-5594-3067-b05a-624af94e1d17 | -7.86423 | -44.80835 | 2024-10-04 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 010e2da0-a7cc-38fe-ac75-976e12176055 | -7.86375 | -44.9632 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6e523347-9c2f-36bd-9816-24a8148f4bfe | -7.86292 | -44.96398 | 2024-10-04 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22b4dafe-94b9-3631-b17c-b31c925db95b | -7.85256 | -45.33499 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 517aa4e7-785a-385f-a1d6-0a2bd1f31e02 | -7.85074 | -45.34707 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f8f42722-5fcf-364f-a79d-3fa0bc950b26 | -7.85014 | -45.35109 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4816a48f-9925-36bc-b686-2ae54c3fdd39 | -7.84954 | -45.35511 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f0dfce50-4b60-372e-8b7d-754c6f9c26c5 | -7.84598 | -45.35457 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0671a3f4-53ed-3bb4-9a97-bcaab9fd963d | -7.74673 | -44.05101 | 2024-10-04 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6974f486-d15d-3ee4-9105-9f3bc36dda12 | -7.66404 | -45.22571 | 2024-10-04 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3be6138-c410-3453-a974-316cef8314fa | -6.61251 | -45.03698 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 339b8022-1831-3327-b604-7a465ffd4825 | -6.60895 | -45.03643 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b72260a6-8e4f-3b17-aac1-56cd2d5ccf68 | -6.60061 | -45.04344 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 403a8dce-6066-3292-93e0-edfa84848362 | -6.59706 | -45.04287 | 2024-10-04 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14bf1c6f-b21a-3901-9705-0255c8704b37 | -6.72331 | -44.55098 | 2024-10-04 04:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README97.md)
