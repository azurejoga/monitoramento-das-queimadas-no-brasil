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
| 769978b8-ad9f-3a99-a5dc-19d3685d56dd | -3.328 | -54.9205 | 2025-01-30 00:00:00 | GOES-16 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ff27fd27-6c8e-33c9-9f8d-55fcb59bb5e6 | -3.328 | -54.9006 | 2025-01-30 00:00:00 | GOES-16 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 59e5c714-e658-353c-8d7d-bcb07c844039 | -3.328 | -54.9205 | 2025-01-30 00:10:00 | GOES-16 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7057cc4d-6251-33f1-a93b-3eba3c44a151 | -3.328 | -54.9006 | 2025-01-30 00:20:00 | GOES-16 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 3f42c1e8-0642-3d86-b78f-304d338e7664 | -3.328 | -54.9205 | 2025-01-30 00:30:00 | GOES-16 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 8dceea4a-0407-31cd-a08d-0d7a8cb3ee13 | -17.8018 | -39.9865 | 2025-01-30 00:40:00 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 72.2 |
| 5e084104-40dc-39c1-bc65-a336332aadeb | -3.328 | -54.9006 | 2025-01-30 00:40:00 | GOES-16 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 71a0c2e9-3be3-3345-afda-e10f3c662141 | -3.328 | -54.9205 | 2025-01-30 00:40:00 | GOES-16 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 94c3406d-cdf1-33b2-8fb9-d3ac13f561f2 | -17.7815 | -39.9921 | 2025-01-30 00:40:00 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 88.3 |
| 1ca58b5e-125c-3da6-a77c-ef2787f937da | -6.9192 | -43.494099 | 2025-01-30 00:40:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6dcfe9d7-aaa5-3f81-ac45-1a14114f4ec2 | -3.3219 | -54.893501 | 2025-01-30 00:40:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00a465be-6a21-327c-a6c4-7105a8499d70 | -3.3137 | -54.902699 | 2025-01-30 00:40:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faf6f274-c748-3702-aa4d-2ede401bc4c3 | -17.775299 | -39.979 | 2025-01-30 00:40:00 | METOP-B | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38507c9e-6c19-3f27-9f87-10657bc6ea68 | -20.283199 | -50.952702 | 2025-01-30 00:40:00 | METOP-B | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0720aa84-61e2-3621-bdc9-576444239c32 | -3.325 | -54.9076 | 2025-01-30 00:40:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dbd7287-f232-3edb-9ee0-a1176cde87a1 | -3.3266 | -54.9146 | 2025-01-30 00:40:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb4eef3a-7086-39a1-821e-f4dc84957bca | -20.286301 | -50.967602 | 2025-01-30 00:40:00 | METOP-B | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ac61d04-6eb9-3fb7-b796-23085bb8abfe | -3.3235 | -54.9006 | 2025-01-30 00:40:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4d38d00-b0a2-381a-ae7b-0a455eb0ccad | -11.2518 | -44.477501 | 2025-01-30 00:40:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 770e3a2e-c5fa-3a20-aa00-a098021088e6 | -20.2847 | -50.960098 | 2025-01-30 00:40:00 | METOP-B | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d7b03d4c-0bd3-380c-bfab-e8cbd31222bc | -17.8026 | -39.9603 | 2025-01-30 00:50:00 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |
| 778eee75-495f-3b21-aeaf-3959a3a06c5e | -17.8018 | -39.9865 | 2025-01-30 00:50:00 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 166.2 |
| e1d70838-cd76-3bb8-acf4-65c73a1353e0 | -17.7815 | -39.9921 | 2025-01-30 00:50:00 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 123.8 |
| 4148bbcf-144a-3928-a475-45083a3e859f | -3.328 | -54.9205 | 2025-01-30 01:00:00 | GOES-16 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 70abce8d-232c-37ff-a608-4311725772bc | -6.9346 | -43.5168 | 2025-01-30 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 0469d833-4f65-34ee-a43b-e8a6bb535469 | -6.9349 | -43.4934 | 2025-01-30 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| d65bb75d-d275-3287-8414-5ff9f59b92eb | -6.93563 | -43.50748 | 2025-01-30 01:02:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| ef43546d-2201-3bbd-8fb8-29afd3e360b9 | -6.93531 | -43.51411 | 2025-01-30 01:02:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| c0becad5-6da9-3731-9922-419dbff7af0b | -3.32184 | -54.92278 | 2025-01-30 01:04:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 99c60c71-38cb-37ee-afbf-93267cd65890 | -3.32551 | -54.91648 | 2025-01-30 01:04:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| cf384dd2-7991-3d12-b5d2-418a405bb4d3 | -3.3269 | -54.92685 | 2025-01-30 01:04:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 28f34249-32b7-39f9-8689-b51b3a243e00 | -3.3204 | -54.91248 | 2025-01-30 01:04:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 9d755bcf-42b2-34f0-ba34-e0e1a9b13a1d | -3.32413 | -54.90619 | 2025-01-30 01:04:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 54bbf627-f2bf-30b2-ae87-d61fa46fe77f | -3.31897 | -54.90223 | 2025-01-30 01:04:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9c34fdd5-985e-3f0d-a29f-928f29ebeb7f | -3.328 | -54.9205 | 2025-01-30 01:10:00 | GOES-16 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 9552e06b-13af-3081-84fe-d32bd1f7394a | -6.9346 | -43.5168 | 2025-01-30 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 195a0b2b-6aea-38d8-9dba-6da0d612df44 | -6.9349 | -43.4934 | 2025-01-30 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 1fa6accc-6aea-3626-8658-a0c184c1a299 | -6.9346 | -43.5168 | 2025-01-30 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e035c779-adbb-3e7d-aaa9-ca49daebf0b7 | -6.9349 | -43.4934 | 2025-01-30 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| d8bdeaab-929a-326f-baa3-4b62db981b70 | -6.9346 | -43.5168 | 2025-01-30 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 36e73e3e-b29d-3807-87ed-921a2d4f31e9 | 2.625 | -61.456902 | 2025-01-30 01:36:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 59f1bccd-6a41-3da8-b86b-35f1b2ba33d0 | -3.3176 | -54.892399 | 2025-01-30 01:36:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a4de9e-4153-3ff3-a18f-0f97c48f4742 | -3.3217 | -54.909801 | 2025-01-30 01:36:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af5702b4-c479-3783-98c9-de8b93442a0b | -6.9537 | -43.4917 | 2025-01-30 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 3d7b83d3-5936-3e3a-af43-64e05bd66c91 | -6.9349 | -43.4934 | 2025-01-30 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| c192a2b4-e559-30ca-898c-df5ae492a443 | -6.9346 | -43.5168 | 2025-01-30 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e2fdeb91-f724-32c3-9a2e-31049dd74c1a | -6.9535 | -43.515 | 2025-01-30 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| e4fdd4f2-57f8-36b6-a633-a6d43900f756 | -6.9346 | -43.5168 | 2025-01-30 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 66d1c228-035d-3d17-bf59-e9d7929ddc11 | -6.9349 | -43.4934 | 2025-01-30 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 0cb85d95-dc62-31fb-8a8e-49a9566977c5 | -6.9537 | -43.4917 | 2025-01-30 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| cd98b9b0-388d-34b0-9ca8-0fd9ac5ad9e1 | -6.9535 | -43.515 | 2025-01-30 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ea37c156-1573-39ee-84d2-99c19b5c5f60 | -6.9537 | -43.4917 | 2025-01-30 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6beacd26-b33f-39a5-8e51-e02acb359739 | -6.9349 | -43.4934 | 2025-01-30 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 9cfd84b6-0816-354b-a2a9-aec2b1991b89 | -6.9346 | -43.5168 | 2025-01-30 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 2d2da1e3-7e6b-3639-987d-a729911ad82b | -6.9346 | -43.5168 | 2025-01-30 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| e8696fb3-9b08-31b1-a079-95829e1ea924 | -6.9349 | -43.4934 | 2025-01-30 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| ad5976dd-84b6-30d4-bbd8-e6ce062879b8 | -6.9349 | -43.4934 | 2025-01-30 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 2814b6e5-bc0a-3efa-8730-4ad12713d88a | -6.9346 | -43.5168 | 2025-01-30 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 7922b6c7-f51b-3774-ad28-4dde046e92a7 | -6.9346 | -43.5168 | 2025-01-30 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 66b8d53d-2679-3cc7-aebd-509ef37c1674 | -6.9349 | -43.4934 | 2025-01-30 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 5062f400-23bc-344a-afbc-2b5b26131400 | -6.9346 | -43.5168 | 2025-01-30 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 223419ab-aae4-3484-86b9-e4d37d1d95b4 | -6.9349 | -43.4934 | 2025-01-30 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| ba70e30a-d94c-3e59-b027-6436aed788e2 | -5.52097 | -37.48603 | 2025-01-30 03:02:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5d209986-dfaf-3053-8b13-896a0924ca7f | -5.52002 | -37.49122 | 2025-01-30 03:02:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1b14897-2fb5-3208-92ac-fd55b25b4e2a | -17.87762 | -40.12064 | 2025-01-30 03:06:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 18fd602d-0b3f-3c22-bfa3-b2c0ad283d5f | -17.87659 | -40.12534 | 2025-01-30 03:06:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b508646b-1bdd-3a62-92bd-a0dd0cf698b2 | -6.9346 | -43.5168 | 2025-01-30 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 080de393-3257-3c8e-a39c-6f88ba4cbf9e | -6.9349 | -43.4934 | 2025-01-30 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 4f67f124-5203-3c8f-9d9b-449fb89ae03c | -6.9346 | -43.5168 | 2025-01-30 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8d2f03bd-0e0a-31f4-8c61-91d7b495f94c | -6.9349 | -43.4934 | 2025-01-30 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 0eb2fcdb-e83e-3ff1-99ca-dd84144baf88 | -6.9349 | -43.4934 | 2025-01-30 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 190.3 |
| aa2d881a-91d1-340f-ad72-c54008c3a7bc | -6.9346 | -43.5168 | 2025-01-30 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 171.2 |
| efad8203-b309-35dd-823b-e8a3e8ba8713 | -6.9535 | -43.515 | 2025-01-30 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| bd6bd226-5d87-359e-b489-596f1c524076 | -6.9537 | -43.4917 | 2025-01-30 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7b71255d-d10f-3c43-9605-de5f897f67b4 | -6.9537 | -43.4917 | 2025-01-30 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| b1e1463f-7447-3874-907e-34453fab7f86 | -6.9158 | -43.5185 | 2025-01-30 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| f7bc21f8-fc8e-370c-af92-b7c8946e53cf | -6.9346 | -43.5168 | 2025-01-30 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 5f748622-56d6-38d0-a5a2-2c39f3d95776 | -6.9535 | -43.515 | 2025-01-30 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| b6579ffd-0957-3bde-98ed-3248946f60d5 | -6.9349 | -43.4934 | 2025-01-30 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 7c44a58e-3c49-3915-bb5c-a9474b64738f | -6.9161 | -43.4952 | 2025-01-30 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c4c5101f-37d9-3652-a2c6-0da69b4ba970 | -6.9346 | -43.5168 | 2025-01-30 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 2b6fcf95-4739-3c01-8643-8242af6b8ed1 | -6.9537 | -43.4917 | 2025-01-30 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| ad0bff93-a108-338e-9e55-692b0311252f | -6.9349 | -43.4934 | 2025-01-30 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 32b6f11c-07bb-3ab3-9a5a-323fa17562c0 | -6.92976 | -43.504 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5f5b8c77-59da-3d9c-9cb8-2968e22bf808 | -6.93259 | -43.51188 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fd5bc0b9-142c-3798-9a2c-f9755c1aac62 | -5.17456 | -39.74975 | 2025-01-30 03:53:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66b4f8da-ceb0-3c7e-81e4-97d0a0083466 | -5.0178 | -41.86727 | 2025-01-30 03:53:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2448084-4ee9-39ed-a6ed-4c148fd86e88 | -5.01909 | -39.71385 | 2025-01-30 03:53:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 07c94fc7-4e49-3da2-890e-915aa0be8f0e | -5.25242 | -40.40402 | 2025-01-30 03:53:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 45b9bae6-1020-3217-a557-f933d5735a7d | -5.0185 | -39.71751 | 2025-01-30 03:53:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e487649-a9fe-3b1c-abdb-dbc4179de295 | -6.9356 | -43.49408 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e359e20-f889-37b4-85cf-6ff69d4c358e | -6.94249 | -43.50248 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 9e965838-4443-3908-b677-0c27ad212e91 | -6.9338 | -43.50472 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b85ed631-a5c2-3f7f-b030-0121067d3fbd | -6.94773 | -43.49604 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad2c87cf-e539-34d8-a376-07c366ba266d | -6.9344 | -43.50116 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 79c539b5-2474-3dc6-a806-97832ed76853 | -6.44486 | -40.00221 | 2025-01-30 03:53:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dd510007-971c-3f2d-a8cf-0a39144cb3fe | -6.93844 | -43.50185 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 4b677cd4-6279-39b2-a096-060b12b5006b | -6.93619 | -43.49057 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33c43bac-ae45-3fbe-afa7-de8ff377b2f4 | -6.46392 | -35.24149 | 2025-01-30 03:53:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 60211d45-7aee-3c90-9aed-f2e55748cd9e | -6.9332 | -43.5083 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |


[Clique aqui para ver as próximas entradas](README2.md)
