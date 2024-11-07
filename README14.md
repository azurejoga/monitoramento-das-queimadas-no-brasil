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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e384147-7c80-32ac-8027-7180c196f8cf | -5.62794 | -43.96112 | 2024-11-07 00:56:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c71741b9-0aa1-328b-8c41-f8982d11557f | -4.48498 | -48.11716 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4c7e7a32-ec5c-39c8-bc65-03b52da4c932 | -5.62565 | -43.94563 | 2024-11-07 00:56:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 20108bb7-648c-35d5-adf2-c2efa5b3c613 | -2.72823 | -51.72253 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 00b9eaee-9a15-3f79-a8b3-076c586dbc52 | -3.33185 | -50.08334 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 49d8481f-5b27-3a56-bb17-4c29c85d0ec2 | -3.53535 | -50.28858 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 91d0e017-c728-34e6-968d-f1c74ac2e895 | -4.09406 | -51.00788 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| e920856a-9b88-3b53-bb6f-06f449a37e3d | -4.41587 | -44.47509 | 2024-11-07 00:56:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c649c67c-0847-3ab8-a298-199beeab1d85 | -7.13697 | -44.83187 | 2024-11-07 00:56:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| df842691-9d29-392f-a46d-372c62311973 | -4.39401 | -49.77007 | 2024-11-07 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 6b176757-75e4-3f50-816a-232f0ddfb700 | -4.34485 | -48.6268 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| a4da870b-5672-3282-b9b3-a9880373e0ac | -8.02108 | -49.62886 | 2024-11-07 00:56:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| acb8715c-fdd7-3a01-a6f7-728db40d1c96 | -5.52324 | -46.54205 | 2024-11-07 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 26d9cc01-16b2-346b-83d2-31d82f41e36b | -3.18799 | -50.57983 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f4e1d3d7-4ae5-327d-8772-2fc7440405cc | -4.95423 | -47.58814 | 2024-11-07 00:56:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e97cfdc1-ed96-3d3f-a2a6-810300c88a03 | -6.69489 | -46.99878 | 2024-11-07 00:56:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7930a202-9b6e-36da-94dc-58777bf4b7c2 | -6.48178 | -44.68539 | 2024-11-07 00:56:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 50aa6b19-9208-39d1-ab49-f35fc7f096fc | -2.40079 | -46.18198 | 2024-11-07 00:56:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b597e9e2-dd51-3ed8-bc07-2222f2056c0e | -3.18926 | -50.58891 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 2d95cdd9-752e-3971-b81b-eafb28e544f4 | -2.55431 | -54.01396 | 2024-11-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4f7d82a6-af41-3c9b-b5bc-26b80e246a12 | -3.66121 | -52.34708 | 2024-11-07 00:56:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0602e5e9-0ec3-33c6-88b7-dba392de1879 | -3.67105 | -52.34579 | 2024-11-07 00:56:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| e716c1bb-2c5c-3c33-8b5b-bee27a5e9777 | -2.659 | -48.56454 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9dadc707-ecbe-355e-bb4a-d62fe4bb2620 | -1.98176 | -47.17591 | 2024-11-07 00:56:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8ff15b4b-a9ae-39ca-9189-f12754f94677 | -4.24926 | -48.53709 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0e6985b4-f939-3ecc-ad27-ea3849dd7b99 | -8.38152 | -49.6385 | 2024-11-07 00:56:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d597666-f926-3ee3-8c0f-c4b20ecf7067 | -7.41008 | -44.81008 | 2024-11-07 00:56:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 764ae7dc-a20f-3f3e-8e95-f3d14952dc94 | -2.67927 | -51.82693 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 63dd5332-62c2-399d-bf84-c3865e05e89e | -8.49898 | -42.10801 | 2024-11-07 00:56:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| a551d009-726f-3656-a6c2-7c27085a69c1 | -2.24564 | -53.66254 | 2024-11-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b72080c1-9ee4-3581-9511-8763c94021e7 | -5.98616 | -45.3623 | 2024-11-07 00:56:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 229.4 |
| aefab289-4716-35ac-833e-d0718e40cce3 | -4.74316 | -44.43187 | 2024-11-07 00:56:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 46f6729f-6f76-3540-83e6-2ca0680fc183 | -2.8138 | -48.55479 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d55fa946-237d-3dc8-a66e-b95273181b1c | -2.73094 | -51.74243 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7a6b3de1-44fa-308f-8205-3e3e74122335 | -4.80644 | -50.83103 | 2024-11-07 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6644efcc-0df7-3f0c-88ce-fbd6988d7e9a | -2.38413 | -48.51044 | 2024-11-07 00:56:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f9c5d78-63d4-360c-b9b1-5be089ce2f04 | -2.4162 | -48.54308 | 2024-11-07 00:56:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4944bc2-2438-3eb3-b045-6c00d1570724 | -2.70749 | -48.64987 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b942ac14-318a-3602-ab13-23a36203e1a3 | -8.68289 | -47.95511 | 2024-11-07 00:56:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c56e8b5f-c1f0-3947-a2ec-6150f2989133 | -2.85067 | -48.68162 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 6ffcf1f4-1a33-37e0-a15e-e7e3d38ad291 | -2.82573 | -52.96368 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c1fde789-58d5-3fc3-bb5c-b31a272c10e8 | -3.72357 | -52.27686 | 2024-11-07 00:56:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2e4e6460-0e59-342c-99f1-07eba03ba796 | -2.19372 | -49.52592 | 2024-11-07 00:56:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 92826987-ba27-3d5e-9b86-6d7ef8f991df | -7.13509 | -44.81916 | 2024-11-07 00:56:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 72ec5fdd-8157-3ee3-b622-12b46b3dd6a2 | -4.67527 | -46.34249 | 2024-11-07 00:56:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 826cbda5-9238-3f1b-81b1-63ac53544488 | -8.31493 | -43.62381 | 2024-11-07 00:56:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e004a866-51ec-3832-ab63-0a77ab1d1735 | -3.24433 | -49.58234 | 2024-11-07 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8ce4e592-bd50-3cde-9444-57ca78773978 | -3.13859 | -49.22665 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d1c0c420-2bfc-30ec-8371-ef099649129f | -2.60678 | -49.24862 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 23a86a16-53a1-39de-acc5-59964806644e | -4.64129 | -49.36536 | 2024-11-07 00:56:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 3afe1d92-29a0-345f-8e7a-40db68b5cf6d | -3.81468 | -48.98302 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 78de06ba-6b88-34a3-98a0-d52088556a65 | -3.29454 | -50.02243 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 04898f51-e075-3aa4-b956-6ffcf04a6382 | -5.70213 | -45.9374 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ca6cd25d-c480-36d0-b6c8-88566d516888 | -5.54457 | -47.06809 | 2024-11-07 00:56:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9f3abf2a-8b2d-3851-91cf-4e48018f3f16 | -3.97592 | -48.1644 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| e045db42-feeb-37f3-801e-16aefdef592b | -1.99136 | -47.17457 | 2024-11-07 00:56:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| db4bfbad-1bab-3d01-8ba8-e0ea13ce71f1 | -2.8461 | -51.77097 | 2024-11-07 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 665d3831-b25d-350f-93e0-828c7f866b75 | -6.54716 | -39.67638 | 2024-11-07 00:56:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 29340069-964d-338b-a305-251fa042a1e4 | -4.3754 | -48.58608 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4552c95b-b95e-349d-93b3-fec17ef9039b | -4.59199 | -48.48211 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f71ea417-514d-3c63-8c27-991e8185591c | -2.72687 | -51.71262 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| b173ed59-99d8-31a7-987e-6883db5881af | -5.1088 | -43.95964 | 2024-11-07 00:56:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 2fb0d10f-73b1-34f3-a871-3d03284e45b1 | -2.14152 | -50.80269 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 58c27b26-a6d4-30b1-971f-531cd7002f08 | -3.04201 | -53.27808 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| a9bef589-9257-3dde-a89b-5234fa3234d1 | -3.04171 | -49.53079 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe365c6f-68a9-3a64-822a-213938ead6d3 | -5.16873 | -44.12393 | 2024-11-07 00:56:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 087decc9-81da-3823-8901-7f6a9ff0f4fc | -3.5247 | -50.35142 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bf7fb25c-b3fe-32c2-9ecd-cd3822d15e3b | -3.44674 | -50.38077 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5e9a9e53-4534-3a6c-af09-d47e8b80dadb | -3.71635 | -49.00293 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e46150ee-3d55-33a3-99f1-215cc13264ab | -4.73127 | -50.88613 | 2024-11-07 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f9fe86a-a0b5-3921-9032-54c4983a60d4 | -2.1883 | -51.74363 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 04a7cd02-b707-319c-9795-0472f5d03bdb | -2.47382 | -49.02055 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d0fd16a-8f54-3131-821e-a53945650af3 | -4.08488 | -51.00911 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 0e1c1491-29ea-3b1f-ab55-a91112f3a6e1 | -2.41691 | -48.93783 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3a40b05-76f3-36d6-abe8-f9b64cc6a51d | -2.81931 | -52.91679 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3db389d0-c8dd-32b6-ad1f-01a658125523 | -2.40811 | -48.87532 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 20f36f2c-8d50-35ce-aa89-2f6b748a6377 | -6.8598 | -47.96712 | 2024-11-07 00:56:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80494c5b-87bf-3552-bf59-df241899c862 | -2.14026 | -50.79361 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 99ec1386-18b5-3860-942f-acab75d86890 | -2.67953 | -48.51535 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d5ceffe-2ca5-332c-a313-f3909eba779d | -3.30176 | -50.13919 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e1712ec-6a68-3edf-9cf1-163d9c5e8b58 | -3.58765 | -50.27207 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6ff3e086-1ca3-3801-9e37-b081de962933 | -2.66027 | -48.57361 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5c949633-a35b-3b82-9fc6-be1bc1f263fc | -3.2166 | -50.38515 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7ef5d9ac-843e-38db-911e-1b6693ca71a0 | -2.94316 | -52.70015 | 2024-11-07 00:56:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 4f53f965-b26a-310e-abb9-39704f74e196 | -2.07477 | -52.04671 | 2024-11-07 00:56:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1fadbfc2-c0c8-3f3f-ab69-afc2bda89c1d | -2.5564 | -54.0073 | 2024-11-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 59ae4fff-969b-3f2c-94cf-6d0d8b1a6ea2 | -5.3703 | -46.25759 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ad53b348-afa0-36a9-821b-1ffb323195f3 | -2.68066 | -51.83701 | 2024-11-07 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 17c2f2a7-e17b-3d10-8eca-a8c79a360039 | -5.32837 | -46.10774 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5c5d2273-d164-3429-a8e8-45fdc7104687 | -2.81258 | -51.80634 | 2024-11-07 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e0f1dac4-2b3b-3222-8bd5-b5998bf47527 | -4.99241 | -46.89581 | 2024-11-07 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 135f8767-1d99-3d87-8f9f-d15008bb1361 | -2.95094 | -53.28476 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d151a8ac-37b1-3b5c-bce0-421189f71578 | -4.0605 | -48.31011 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7718d491-d261-3b70-a1dc-d3c266e53ff9 | -3.74174 | -50.44998 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 656ca0fc-35ee-312d-a91f-be164183f726 | -2.96781 | -54.17068 | 2024-11-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9137bbbc-81e3-34a8-aab4-200c14d292da | -5.85081 | -50.05153 | 2024-11-07 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc240d91-b542-3ba4-8c1f-0d3d30c292f5 | -3.97085 | -48.39366 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a740121b-e3f4-3f55-90f7-c044ee63b088 | -2.84748 | -51.78098 | 2024-11-07 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6e7ed046-b482-3bb1-9f15-0ca1ac7c1714 | -4.27438 | -48.65177 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5f61dd65-efbc-3558-b53f-9d18f97585f2 | -2.87025 | -49.54305 | 2024-11-07 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |


[Clique aqui para ver as próximas entradas](README15.md)
