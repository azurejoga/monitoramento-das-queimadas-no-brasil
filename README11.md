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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96650dd3-78ae-325a-9534-e515540a8484 | -22.55465 | -49.76859 | 2025-08-14 03:34:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f9704db2-94b4-3eeb-abf9-f1090886403d | -22.61832 | -47.39076 | 2025-08-14 03:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ef36f9d3-f09b-338a-bc02-c4fb116cd3b3 | -22.61957 | -47.38742 | 2025-08-14 03:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 69e2e9a3-20a1-3b79-9ba1-4788c0476f35 | -21.1925 | -46.68438 | 2025-08-14 03:34:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e1a649f1-e9fa-3e80-b070-0e9a4febf17b | -24.47544 | -50.65224 | 2025-08-14 03:34:00 | NOAA-20 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e6bbae98-4b31-3a76-9f7a-33c4bcf32c81 | -23.0544 | -48.85545 | 2025-08-14 03:34:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b35e69be-3061-3e43-992e-8246801b8147 | -23.03343 | -50.37883 | 2025-08-14 03:34:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| ede91c61-9c07-3dd4-b6aa-d138eea35571 | -23.02684 | -50.3765 | 2025-08-14 03:34:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| ff3e1521-f13a-3d46-bdf9-a7312b616bbe | -21.93916 | -45.01875 | 2025-08-14 03:34:00 | NOAA-20 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9ba15ca6-0e77-3edb-8419-751c974492d3 | -22.39828 | -45.47131 | 2025-08-14 03:34:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fd602c98-a9cf-31f2-9224-665ea0607e5d | -21.31672 | -48.5654 | 2025-08-14 03:34:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e05e058-d602-3b9d-974e-315a9fa7b7fb | -21.22462 | -42.56846 | 2025-08-14 03:34:00 | NOAA-20 | SANTANA DE CATAGUASES | MINAS GERAIS | Brasil | 3158409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8d72053d-ca57-3184-85b7-bc36eea2178c | -24.47869 | -50.6516 | 2025-08-14 03:34:00 | NOAA-20 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cc789ad9-4283-309c-a93b-f9bbd9471324 | -22.59636 | -46.72795 | 2025-08-14 03:34:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1891bf34-1fac-3c14-920f-9965b031f40b | -21.21839 | -48.80387 | 2025-08-14 03:34:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| baf14b71-2ba4-30de-abab-82c0bc4af8cd | -22.48432 | -44.10505 | 2025-08-14 03:34:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ff29ee1e-989f-3192-9a48-1a27f1f76fbe | -22.85301 | -49.22263 | 2025-08-14 03:34:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c74da772-6bd4-34e9-95fd-9c2267fed8d0 | -23.0575 | -48.85518 | 2025-08-14 03:34:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f89183b-4def-3a31-972b-aace46a30cf5 | -22.66998 | -47.45703 | 2025-08-14 03:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dad4187b-7092-30cb-854e-1758c6af60e1 | -21.70734 | -44.37257 | 2025-08-14 03:34:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a99becbd-ff1e-3380-8619-bd169b06887e | -23.57051 | -47.24351 | 2025-08-14 03:34:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e1056419-4993-3cbb-a7a1-888b14a96b46 | -23.02435 | -50.38069 | 2025-08-14 03:34:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 1954f1ae-4073-3514-beba-e22af604c9c7 | -22.85167 | -49.22817 | 2025-08-14 03:34:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73c099b9-66bb-328e-a30b-a87ae2cc251c | -22.60193 | -46.72923 | 2025-08-14 03:34:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ce336222-8545-3d6f-ad0d-9de1390dc4e8 | -22.62437 | -47.39305 | 2025-08-14 03:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be8cb383-0559-3d34-827d-dbcd0c547a8e | -21.21926 | -48.80081 | 2025-08-14 03:34:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.0 |
| eddabaee-42f3-3c19-a20d-d5d195a8ee27 | -22.60284 | -46.72525 | 2025-08-14 03:34:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| cb0d60b4-0446-3aba-9865-33fda8046136 | -21.21708 | -48.80942 | 2025-08-14 03:34:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 1844c822-c17b-3af9-8c9c-a8f93e4583e3 | -22.16406 | -42.9811 | 2025-08-14 03:34:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 79a9521d-8712-3766-a860-d6f96d2fd5dc | -22.61859 | -47.39169 | 2025-08-14 03:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 77fbd380-e940-35fc-baf2-765aa42cc33a | -23.18632 | -46.58968 | 2025-08-14 03:34:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 42b31d51-5395-363a-9aa9-94f2264b67c5 | -22.55309 | -49.7748 | 2025-08-14 03:34:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9dd03834-9376-3fc2-92ff-83c5a51059a2 | -22.67465 | -47.46325 | 2025-08-14 03:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e524ebb0-20e0-3bab-bc81-e74d5e602245 | -23.54278 | -51.61405 | 2025-08-14 03:34:00 | NOAA-20 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d8df35b3-e75e-3e58-90bb-24599e6de1e3 | -6.0807 | -59.9465 | 2025-08-14 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 179f035d-22a9-3f17-ac30-9e5186e49695 | -6.8955 | -59.1655 | 2025-08-14 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 3d77e772-0cc5-38c2-8450-ac1f8c012f52 | -6.877 | -59.1663 | 2025-08-14 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9865e598-e827-32fd-8291-82ad1f630dbe | -7.6103 | -63.516 | 2025-08-14 03:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 6b84eed8-a0eb-3c43-96d3-8b82e6c5874f | -7.8774 | -61.8253 | 2025-08-14 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7e8b57a4-48e4-38bc-bdfd-5ee96042a5f6 | -9.1336 | -59.6588 | 2025-08-14 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 3576e715-390d-3929-8f6b-c8a36a17a035 | -6.914 | -59.1455 | 2025-08-14 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.0 |
| d2d7b180-ac7e-370e-8655-9ae8ee1c87dc | -6.8771 | -59.147 | 2025-08-14 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| f1ee937b-48a1-3ec8-9aaa-8496c2c64c8a | -6.0991 | -59.9459 | 2025-08-14 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f67e2a49-d0ae-3ec1-9c85-5d98fcea0d55 | -7.8775 | -61.8063 | 2025-08-14 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 7af36652-d3e8-3ecc-a7a2-063a36ff5c7b | -6.8956 | -59.1462 | 2025-08-14 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 97b94248-ee45-3de6-b76f-e574f8f103a0 | -9.1522 | -59.6578 | 2025-08-14 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b0a6963e-5bd5-3cc9-b611-ef29743c9e61 | -16.3153 | -52.9201 | 2025-08-14 03:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| bc31ae4f-f933-3d61-b423-2a0113f8bcfa | -9.1522 | -59.6578 | 2025-08-14 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 52b304fc-406d-3922-bb37-43bc65ef7378 | -6.0807 | -59.9465 | 2025-08-14 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 690aa463-9603-339f-8ab2-b65e244f5196 | -6.914 | -59.1455 | 2025-08-14 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.2 |
| a0ac56b2-7146-300f-b0cf-13bfff03ddd3 | -2.9106 | -48.2971 | 2025-08-14 03:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 691fb8b5-8910-3554-99cf-b717f71e061d | -6.8955 | -59.1655 | 2025-08-14 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 418ab086-7d1f-3341-a1fc-b3746acadbab | -6.877 | -59.1663 | 2025-08-14 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 83a2d761-7975-35fd-8374-2fa467932d37 | -6.8956 | -59.1462 | 2025-08-14 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.1 |
| a17668d6-27c4-3d20-a859-339aae2bd13c | -6.8771 | -59.147 | 2025-08-14 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| a84986c2-98f4-31f6-b05f-974ceb8f0c48 | -6.8956 | -59.1462 | 2025-08-14 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 23676d82-6d67-3188-8144-95532c213a66 | -6.8771 | -59.147 | 2025-08-14 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| fd96508a-914c-30c6-8512-ed63855695bf | -6.8955 | -59.1655 | 2025-08-14 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 220a81a0-4f75-3033-b944-4eabea85cad7 | -6.914 | -59.1455 | 2025-08-14 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 0fc510fe-d1b1-3c42-84fa-02584deee6c0 | -6.0991 | -59.9459 | 2025-08-14 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 08b218d6-e38b-3ccd-a831-5440b646fa05 | -9.1522 | -59.6578 | 2025-08-14 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| bc4dae64-37d0-3304-834d-6d572d31f88a | -6.0807 | -59.9465 | 2025-08-14 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ead16193-5d65-3348-9a1f-8e61c3e8d929 | -7.8774 | -61.8253 | 2025-08-14 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 565ecb42-8d58-314d-a1dc-493b22859922 | -6.877 | -59.1663 | 2025-08-14 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 25fa2456-6c82-3c93-b500-3ccaf02098aa | -2.9106 | -48.2971 | 2025-08-14 04:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 8b5e5a7c-59b2-32d1-a8fd-73699fb7f7b0 | -6.8955 | -59.1655 | 2025-08-14 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| a9bb6cc4-6aea-3cb9-baa0-816e80d24672 | -6.8956 | -59.1462 | 2025-08-14 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 4c27cb4d-882a-3ce9-ad73-ccf740283f7b | -9.1522 | -59.6578 | 2025-08-14 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f75c29b7-a71f-325b-9b08-feaad7b15fd6 | -6.877 | -59.1663 | 2025-08-14 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 8fd63428-eb5f-35b4-93ca-1ab924d9a0c7 | -6.8771 | -59.147 | 2025-08-14 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 8643a6f9-abac-34cc-a738-ca49022443a0 | -6.0807 | -59.9465 | 2025-08-14 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a6242ed1-bc51-3fa7-9ebb-92b855bcc8d7 | -6.914 | -59.1455 | 2025-08-14 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| aa79cc10-e340-3484-ac12-9cce9183182b | -6.9483 | -44.55033 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8932583a-4787-3f7f-97df-28000fde7619 | -5.15542 | -39.50505 | 2025-08-14 04:19:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 22fd7f13-61ed-3ccd-884f-610de3dee266 | -3.82112 | -41.56037 | 2025-08-14 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5f57f2f3-e646-3ed0-82c5-415d030ca982 | -2.9162 | -48.29981 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d68f34d6-a6c3-326b-bbe7-213b86bb531b | -5.68753 | -43.64547 | 2025-08-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a72f6609-0375-30de-a472-a20dd65cb58b | -5.9841 | -44.14659 | 2025-08-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6bbeeab2-5106-3598-9011-ee832c756a43 | -3.89706 | -41.03218 | 2025-08-14 04:19:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc49fa98-8a77-33b5-a396-7acb7d2d9e10 | -6.19069 | -43.31363 | 2025-08-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f90661d6-ebef-306b-907b-f67220c0caa9 | -8.74218 | -44.02803 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36745235-3fac-357e-aa1e-5273f6bd7143 | -6.73153 | -44.28134 | 2025-08-14 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e525c5a7-99fc-3f54-9fe3-7964807240dd | -7.91917 | -45.90588 | 2025-08-14 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e036a8e-361d-3080-b328-b9f06b94627a | -5.75592 | -46.66951 | 2025-08-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c2be30d-024e-3c82-8c37-1fa05c3d28a8 | -5.89265 | -57.74802 | 2025-08-14 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a146a46-e0ff-3d8c-ad22-c093c6d2a09c | -5.78532 | -43.60602 | 2025-08-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6aafd379-e5bc-3e55-ad47-127616a4a7c1 | -6.54145 | -56.19844 | 2025-08-14 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63e31f53-2a5e-3907-b894-f08edde6b88a | -6.91293 | -45.21081 | 2025-08-14 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2f74790-792b-3881-b12a-19b2bc03d863 | -5.50116 | -44.34371 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57a1ea5c-343c-3998-a66c-84afefcd79d3 | -4.06899 | -47.98297 | 2025-08-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6edb703a-28a4-3581-8d53-8380ba2238f9 | -6.45345 | -44.56096 | 2025-08-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cb661dcc-2110-3c51-b1cc-09381084b320 | -4.22771 | -47.21169 | 2025-08-14 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eef024f3-723f-393c-bd5f-8fad99b8764d | -6.45122 | -44.55352 | 2025-08-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bab74213-8116-3abc-b362-666a2b789df2 | -2.29722 | -48.14304 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 949e1fd7-c4ee-3ad1-873e-b36c6e3b5385 | -7.92468 | -46.85417 | 2025-08-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b70c223-608a-3bfc-9f61-6925abf3c3bc | -6.6157 | -43.88647 | 2025-08-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8ea328f3-5b65-3307-911c-c971c4484da1 | -2.47534 | -47.75176 | 2025-08-14 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be1e4b5e-ee6d-3b81-922b-b2e4ef3c3b4a | -8.52763 | -43.32322 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 92ffeaa0-17ad-3588-a7a9-8c321b2a5b46 | -5.7178 | -49.02433 | 2025-08-14 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61f8d895-cb79-3734-9c8b-891b41a64eac | -4.14672 | -46.45367 | 2025-08-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
