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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67f45e24-1dc4-3587-86b9-7ecd8365bfc5 | -13.015 | -45.036 | 2025-07-16 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 34284f50-56f3-3e1e-be38-04916cf4559e | -5.5429 | -43.8864 | 2025-07-16 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a6450bfe-10df-3d0e-aa89-3c384abbfbd3 | -7.2154 | -45.3297 | 2025-07-16 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 896b94d5-48b3-3d32-aa4f-c0f3b0eae651 | -7.1834 | -43.1424 | 2025-07-16 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 6179dad3-1f81-3525-85c6-9d8d4bcf0307 | -5.7756 | -45.0826 | 2025-07-16 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 258b45f1-32ac-3ae9-bb67-43bf507bac00 | -20.0805 | -47.6319 | 2025-07-16 00:00:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 65.3 |
| c62837f2-c75d-3f8e-8acf-ba4a1c8fc966 | -13.0146 | -45.0593 | 2025-07-16 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 214.5 |
| 5e04dc8b-ef29-3bb6-ba7d-d6bc082e1a57 | -5.7943 | -45.0813 | 2025-07-16 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| c8fd3e47-27e2-3e85-bea6-4263cf0df000 | -13.0339 | -45.0561 | 2025-07-16 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 447726f9-2636-3268-a26a-a4d1f157dd12 | -7.1837 | -43.1189 | 2025-07-16 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 156.1 |
| e40313dd-87c0-3a96-9beb-5c55fce513c4 | -20.0798 | -47.6553 | 2025-07-16 00:00:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 2121b2a8-f969-397e-8dab-8eaabb0efa5c | -6.7194 | -44.3231 | 2025-07-16 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 5f0eefaf-4e73-3a0c-a93b-8f574463e68c | -7.9374 | -49.6631 | 2025-07-16 00:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 6e67752f-00e1-3b9f-9b05-614e5272a070 | -13.0141 | -45.0826 | 2025-07-16 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 148811ce-80cc-39b9-a5fc-40e042321618 | -7.9377 | -49.6417 | 2025-07-16 00:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c60c1323-33a0-3264-bfd5-ed0f4992989a | -7.2025 | -43.1171 | 2025-07-16 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 23c3aba9-fd14-3230-ad11-a1190676bc44 | -7.9562 | -49.6615 | 2025-07-16 00:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 8c2596cf-460f-35c0-8894-d4a36ec53bc5 | -7.2025 | -43.1171 | 2025-07-16 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 173.5 |
| 52760b2b-fc39-3318-9c02-234cea0ebb2d | -13.0141 | -45.0826 | 2025-07-16 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9d912abc-8db7-35bb-a6b2-a4f0d24cde75 | -7.1837 | -43.1189 | 2025-07-16 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| 5af46a5a-63b7-3829-9c46-ab9b0914ed9a | -13.015 | -45.036 | 2025-07-16 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| c9faaf2c-bea5-3349-bdb5-d03bca7f5a9e | -20.0264 | -47.3879 | 2025-07-16 00:10:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8dfc28fa-885f-380a-b3d6-8c806c460e84 | -6.7194 | -44.3231 | 2025-07-16 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 566bf36a-067c-34f8-a5ca-9f9050f13b41 | -20.0805 | -47.6319 | 2025-07-16 00:10:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 11ac652f-8e2a-38d0-800c-b2da64bdc944 | -7.9374 | -49.6631 | 2025-07-16 00:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1ca3c23f-d727-3f15-bdd0-513b66d85c14 | -5.5241 | -43.8878 | 2025-07-16 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 07a3268d-e8b7-348f-b751-f78169760dc8 | -5.7943 | -45.0813 | 2025-07-16 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 44b73f8e-cd2d-359f-b3e3-9a9bfeca718e | -6.7006 | -44.3247 | 2025-07-16 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| b51440d3-bb17-339a-9933-a1cb26bef217 | -13.0146 | -45.0593 | 2025-07-16 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 265.0 |
| 39a9f633-678d-3722-8999-beb9b5f791dd | -13.0339 | -45.0561 | 2025-07-16 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 83002d1e-afa3-31be-89d1-ca7c21643209 | -5.5429 | -43.8864 | 2025-07-16 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 6b507b34-bcda-3459-8d44-9eb3f839615c | -13.0146 | -45.0593 | 2025-07-16 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 617a5b43-98a9-3d1c-88de-9fee80f75e6b | -7.9564 | -49.6402 | 2025-07-16 00:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| dc40c0bb-bb99-38f5-af19-4bbd1f1cdab3 | -7.9374 | -49.6631 | 2025-07-16 00:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 81b220bf-cdcf-37cb-a239-b3cbfe191a21 | -10.236 | -55.463 | 2025-07-16 00:20:00 | GOES-19 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| c8aaa348-31eb-3e80-b2a8-add93362daf8 | -5.7756 | -45.0826 | 2025-07-16 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| e8ad65f0-3384-3c23-b119-a694ee294a88 | -13.015 | -45.036 | 2025-07-16 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 39b182af-7693-37fe-a1ff-98840a74a69c | -7.2154 | -45.3297 | 2025-07-16 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 0d9cdd07-fa42-357b-9e35-61971d6c882f | -5.7943 | -45.0813 | 2025-07-16 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 79381e41-55e3-399f-a775-ff1cfda4cf04 | -7.1837 | -43.1189 | 2025-07-16 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| 9b88fa38-a41e-3fc8-9500-1968af3f0ec8 | -7.2025 | -43.1171 | 2025-07-16 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 20259a32-6136-3b08-ac1c-520e88391637 | -20.0264 | -47.3879 | 2025-07-16 00:20:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 55.0 |
| d7e19c92-842a-32a4-bcce-af7681452281 | -6.7194 | -44.3231 | 2025-07-16 00:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| c32befdc-6ae0-33e2-96ea-e65b2541cdbf | -13.0339 | -45.0561 | 2025-07-16 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 192.9 |
| fdc646a7-ae59-3023-83ac-c6c0329a3623 | -13.0335 | -45.0794 | 2025-07-16 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| eb650e45-a3ff-38b6-bfa4-6774badb3e24 | -13.0344 | -45.0328 | 2025-07-16 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 82a01d5e-33e9-325f-80b7-7e687e0e95c5 | -7.9562 | -49.6615 | 2025-07-16 00:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| b0f26e21-ae46-3f0e-8387-b5e78ce2426b | -13.161 | -50.7855 | 2025-07-16 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| bb240084-52eb-33a2-9da1-16351b391d1f | -13.0146 | -45.0593 | 2025-07-16 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 257.1 |
| 7fd6d2fc-219e-3303-a29b-c5687ea7c439 | -7.2025 | -43.1171 | 2025-07-16 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| 07b96244-fcc7-3ae8-b34e-a0ae3e3a940b | -7.9562 | -49.6615 | 2025-07-16 00:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c0868f49-3a77-3a1a-8523-caaff5c0991c | -13.0339 | -45.0561 | 2025-07-16 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| b90c0f3d-22e5-3ecb-a654-3c0b1c946637 | -5.5429 | -43.8864 | 2025-07-16 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| fb3ddbbb-5548-31cc-b8d3-014326b1bfd3 | -5.7943 | -45.0813 | 2025-07-16 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 5ff9d5d0-5f34-37f7-947e-39fa143d696f | -7.9377 | -49.6417 | 2025-07-16 00:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 1a37136d-bdcd-3490-9871-1ba7077a0bbc | -5.7756 | -45.0826 | 2025-07-16 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8eff37d0-826a-324a-91fa-f93e51ba1364 | -13.0141 | -45.0826 | 2025-07-16 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 60a874a2-98ef-3f78-9081-25a4eceac891 | -11.9568 | -48.4203 | 2025-07-16 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| e69139e0-14c4-3983-b358-f6418cce0678 | -6.7194 | -44.3231 | 2025-07-16 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| b787f06c-eb2e-3259-ae10-3d1357eb3b8c | -7.9374 | -49.6631 | 2025-07-16 00:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 860a8389-fe92-39f1-bec6-cd817e1c0fab | -7.1837 | -43.1189 | 2025-07-16 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.6 |
| b4fb1286-8f31-33dd-b16a-1662a443c049 | -5.7217 | -44.8366 | 2025-07-16 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 23ef99e2-6d07-3335-9ea9-068d7390bc7f | -6.7199 | -44.321201 | 2025-07-16 00:37:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a11db71-41b9-3327-a577-09f5212bc1d8 | -6.8977 | -52.860699 | 2025-07-16 00:37:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5e0cfd8-23af-3c30-aa83-1a15c1043ff9 | -5.7667 | -45.089298 | 2025-07-16 00:37:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a58810e8-bf38-3d87-8c32-36f38b5a7de9 | -11.4805 | -48.070202 | 2025-07-16 00:37:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53150745-8fd1-38d5-9e3c-616bf426ed15 | -4.2811 | -48.0588 | 2025-07-16 00:37:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f7dab53-878e-3c59-97da-328b4a6da1ac | -10.6411 | -49.4781 | 2025-07-16 00:37:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce099bb9-b938-353e-9569-fe415fb23f00 | -10.2129 | -55.451599 | 2025-07-16 00:37:00 | METOP-C | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32a02ad8-a203-37a5-b822-b2799e0f6c6c | -3.8394 | -47.754299 | 2025-07-16 00:37:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6140a99-72a9-30f3-91c1-a98df63e9a02 | -5.5563 | -46.525299 | 2025-07-16 00:37:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97944a93-714f-30f1-bf8e-1b66e525de7c | -7.1976 | -45.335999 | 2025-07-16 00:37:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e95da3f0-0c01-3998-9ad4-af99bbcc2d77 | -5.5258 | -43.8993 | 2025-07-16 00:37:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 585eef97-1db2-34cd-a092-4980779855b6 | -7.2074 | -45.333698 | 2025-07-16 00:37:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47561b95-8941-340c-8f4c-09ac323d078d | -10.5594 | -49.109299 | 2025-07-16 00:37:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8a012be-cf0c-3f5a-817b-763c6523b364 | -5.6552 | -43.706799 | 2025-07-16 00:37:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59e71b9a-427a-37aa-9fd4-8020db14772c | -6.6251 | -44.5737 | 2025-07-16 00:37:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a5f9957-4614-32de-8baf-5258a5e3b2ac | -6.6229 | -44.5648 | 2025-07-16 00:37:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25ac673e-e99a-35e7-b40c-521f8b95929a | -8.5246 | -47.851601 | 2025-07-16 00:37:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59ee061f-c0fd-32b8-a1e7-c430f1c7aee2 | -8.4982 | -43.297798 | 2025-07-16 00:37:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f044f241-ebe3-3009-93ff-827a24187bf2 | -8.8921 | -47.339401 | 2025-07-16 00:37:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e56ccb6-5e38-3711-b662-a09dfeacf786 | -5.5661 | -46.523102 | 2025-07-16 00:37:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 504ce080-edcf-3f8e-91b1-96cf856567ff | -8.6363 | -47.753799 | 2025-07-16 00:37:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f76017f-37d5-3655-9ca1-744bf2e2e533 | -5.7764 | -45.087002 | 2025-07-16 00:37:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8939422-ed07-3025-9a8d-cec20daec540 | -4.0231 | -48.058498 | 2025-07-16 00:37:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc024794-d732-3bad-abc7-052643a45132 | -7.2055 | -45.3256 | 2025-07-16 00:37:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d54436ff-a246-3c65-930b-37f3438b5f55 | -10.5545 | -49.1334 | 2025-07-16 00:37:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 318eca6b-1a9a-3d51-a68d-565f8e58e1b5 | -8.9019 | -47.337101 | 2025-07-16 00:37:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba97cc1c-f8a7-30db-bf57-a915ac096cf5 | -5.7723 | -45.069698 | 2025-07-16 00:37:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f98d973-0d7a-315c-b69b-18a3c2797169 | -6.5609 | -51.107601 | 2025-07-16 00:37:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abb2acbe-bab9-3c17-83d4-a421be1d611a | -7.9336 | -49.655701 | 2025-07-16 00:37:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ced0763a-64f6-36da-b0ed-5d0267773149 | -8.9035 | -47.344101 | 2025-07-16 00:37:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67642ee6-8710-3f8e-af04-41bc1f34a863 | -10.8794 | -49.207199 | 2025-07-16 00:37:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| caf088c3-a6e4-30a8-b708-f14540d10f53 | -6.7004 | -44.325802 | 2025-07-16 00:37:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d1c6e59-e6f6-38fb-8afb-e04c7bea0ddd | -10.3063 | -49.9179 | 2025-07-16 00:37:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c0765af-a7e2-3520-b808-74f3e7df73c9 | -5.7646 | -45.0807 | 2025-07-16 00:37:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| daf6ceb3-10ef-3aac-bd9e-17bc0e63c901 | -10.6309 | -44.480202 | 2025-07-16 00:37:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fd197808-ba92-31a3-b5a9-de943c89ab48 | -9.8387 | -47.872101 | 2025-07-16 00:37:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96fc7bcb-b930-3d49-a1e9-cfe708428f8e | -11.1702 | -48.616699 | 2025-07-16 00:37:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ac0ad2f-9b1a-3975-8d3c-637dec44d56e | -11.4639 | -47.311199 | 2025-07-16 00:37:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
