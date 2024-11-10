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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ef3e445-2e55-3c63-b20a-8ef107d98a9f | -1.5347 | -52.2104 | 2024-11-10 04:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| ca94fe86-2d09-3b4f-93ed-bf2bf2257e87 | -3.9669 | -48.1716 | 2024-11-10 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 2221e4ef-22a5-336c-a1bb-0b63d3beb73a | -3.2537 | -50.2849 | 2024-11-10 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| bc977b9b-3911-39d7-a60b-25a4bcf6e489 | -3.2536 | -50.3059 | 2024-11-10 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 8686a0e2-a72c-364d-bfd6-c716439599be | -3.2168 | -50.2861 | 2024-11-10 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| af41cac5-aa40-322d-99f9-f25416327fea | -8.4156 | -44.1344 | 2024-11-10 04:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| e99aad7d-d0ec-3866-9b9b-5f428335da9b | -3.2352 | -50.3065 | 2024-11-10 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 50a93540-073b-3fae-a15a-1902cbc4b31e | -1.2934 | -53.7163 | 2024-11-10 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 04005742-f53b-314c-ade2-1e4eaaca4399 | -17.2933 | -57.4857 | 2024-11-10 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.6 |
| 52853b63-eb74-356b-b7d9-2e47173dd428 | -17.293 | -57.5062 | 2024-11-10 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 8aac6b62-2ca7-3c9c-9b0f-da2929375cca | -2.7587 | -49.3497 | 2024-11-10 04:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c8c99abc-a391-3acf-8bbc-76be1f415609 | -3.967 | -48.15 | 2024-11-10 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a84139b4-027a-33ee-8b8a-a3113173ac60 | -3.1422 | -50.4562 | 2024-11-10 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 202.0 |
| 398cc3bb-3af0-3c79-8235-359051b75b52 | -3.525 | -44.0286 | 2024-11-10 04:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f143e100-7cbc-3a12-a615-9d2cb1a254f9 | -17.6266 | -57.5281 | 2024-11-10 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 223.9 |
| 8cbc5da5-5422-368b-b207-97ae841a1ee8 | -3.2352 | -50.2855 | 2024-11-10 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| a7c875da-35c9-3014-a4f0-4514e044016c | -2.9355 | -51.482 | 2024-11-10 04:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| f332ab7e-e8e0-3b18-a26a-f915d0c6cd15 | -3.1423 | -50.4352 | 2024-11-10 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 385.7 |
| f86aee79-bc3c-3a0e-9832-e029548c5617 | -12.433 | -64.1272 | 2024-11-10 04:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 7e71bf5f-17e6-33b9-a192-aac40333d8d5 | -3.9483 | -48.1724 | 2024-11-10 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| b77e4edb-06ac-313f-bec3-be2887538edb | -3.1239 | -50.4358 | 2024-11-10 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 185.4 |
| cf20ea01-89ce-3d2f-a9cd-f6f0fef7147e | -3.2353 | -50.2645 | 2024-11-10 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| f37f3afa-cb79-305b-8996-7aea23f5a92a | -17.6069 | -57.5304 | 2024-11-10 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 294.3 |
| 94bc9b2a-953a-3e50-8a7d-c1a09da9d3ff | -8.3781 | -44.1154 | 2024-11-10 04:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 4e6c5c6b-0533-380b-8bc5-c3bf7d268b22 | -12.4329 | -64.1462 | 2024-11-10 04:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| cc834269-5ded-3333-bf41-1939e9dc23ad | -3.9668 | -48.1932 | 2024-11-10 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 60363238-9327-332c-8953-7cecf9b75943 | 3.37321 | -51.27478 | 2024-11-10 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 333ac27d-a552-3d68-a534-e2a11f877f43 | 3.73374 | -51.61649 | 2024-11-10 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e02d4d5-c98d-3d23-b557-6f52aae4813c | 3.37261 | -51.27081 | 2024-11-10 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64a5165d-c16a-34e6-bdad-1dd3c36021cc | 3.73261 | -51.61985 | 2024-11-10 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9451ad71-f30d-3a23-858c-14616bfb01da | 3.3746 | -51.27365 | 2024-11-10 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27cc9464-a26a-35a6-a727-255de0779f0e | 3.36828 | -51.2705 | 2024-11-10 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a66e1acb-362a-3587-90d3-04aaba4df308 | 3.732 | -51.61558 | 2024-11-10 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82329560-a97c-3e08-aa58-ae9a40761cac | 3.37403 | -51.26968 | 2024-11-10 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85662e09-db96-3ac5-8eee-0a3113efb269 | -2.72863 | -51.73761 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c56af8e-81ea-38aa-a673-2babcbdaa6ad | -2.39531 | -54.1041 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e29c6ce-14aa-3fca-92be-cab56bf09d99 | -2.14298 | -48.11912 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8edef6b6-8bc2-36e5-9645-e29d6c91cd1d | -6.22671 | -41.67442 | 2024-11-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3d5e5308-f0ff-3c8c-896f-fb28d5f26b7d | -3.54271 | -43.55951 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f34726aa-ef11-38d4-86f8-299c8b046c61 | -2.24374 | -47.97811 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73094b7c-120a-3c05-b3bf-02dc136a9cb8 | -2.65943 | -48.49903 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 484915a5-d00d-3fe9-be23-26a9e780f735 | -4.06664 | -50.01377 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 720cf181-9bc1-3eb9-865d-fb7cfbdabee5 | -2.87642 | -51.30292 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62f783f0-6ff5-351b-938d-0dc98bee7ded | -2.75872 | -49.35521 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5d78612d-45b8-3137-a04c-654b81a94ce3 | -2.68946 | -46.80965 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a96562f-1457-3060-b36c-f65081a645a0 | -3.08343 | -50.42878 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 559caf5b-cbe5-3c42-a57d-ce63f980faa3 | -3.25606 | -48.75051 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39492546-7fbc-371c-bd9d-025c88f46a27 | -3.78102 | -45.18644 | 2024-11-10 04:14:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4d9a5d8e-f43b-3aef-b0b5-e62d96367149 | -2.7975 | -48.28449 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 172b9ce0-0cef-3f03-9586-56b3980e2781 | -3.08155 | -50.5651 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ede4a548-adb1-3b36-bfe9-19c782c00dee | -5.06036 | -45.48878 | 2024-11-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fc8d349-e412-3eea-96da-9d6e0691778e | -2.5674 | -47.34519 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bad17e34-96ad-36d5-af9a-133d88fb8826 | -3.54604 | -43.56002 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 309189f5-5c34-3d6e-93a3-3c826aeffcb2 | -3.4386 | -50.2988 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 487dc234-9df7-3732-8fb4-06ebf276178c | -3.51236 | -44.02934 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 75d4cfa8-c404-37a2-b6e6-2f1935e0dd14 | -2.57598 | -47.34292 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 996da6c4-a38c-3add-bb5e-d7b23e37c4c8 | -2.38986 | -54.09805 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c8ffcc7-f2b6-3511-b2f5-8eb582c5be94 | -4.19631 | -48.54073 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a0c9302-9ebe-3caa-a5a8-54a275744090 | -0.94652 | -52.44349 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5386035-22b8-3e9d-a54e-9f34285aba7e | -4.92913 | -45.36115 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dcad5bd7-58a8-3f86-b151-a9774996eeb8 | -4.09862 | -45.69857 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9df7c82-8ebb-32c8-943d-3a2553f493f4 | -2.24694 | -46.56279 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6748c7c8-e584-3721-9e68-e23c51243598 | -4.17016 | -46.60036 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ce48e0d-83af-3af9-b2ec-c02cbbfa756b | -3.24072 | -50.27815 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fbb9a39-f559-38e8-8d78-add3bd0fd70b | -3.52607 | -49.9997 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c66da12d-7b18-3c22-aea2-37e2cb5b9f9f | -4.10075 | -49.13871 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95505de3-e74b-359e-8177-b761b2441068 | -5.57243 | -43.97952 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e1cf56f-33e4-3d4f-bcf5-04c5f641d9e9 | -4.11382 | -46.90723 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 497012b6-8028-338e-8131-a219ea2bbd02 | -3.6664 | -54.04692 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 511f07bd-e740-34fc-ba93-ac612215680b | -3.10285 | -49.41138 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 52db141f-be9d-3a38-836f-1aac3dec6d4e | -3.11762 | -51.10574 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 692eaf77-04b8-3dd5-9e07-3bc68c6c642b | -5.51349 | -43.79137 | 2024-11-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eadbc1b0-f0fb-35e9-9f28-27733ebd7ed8 | -4.23729 | -48.01945 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 630235da-fdde-3201-992b-b0f25c906b23 | -2.50657 | -47.46101 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84002f32-9f31-33ac-ad64-8c29afe0cf69 | -1.76057 | -48.42106 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79656a2b-18ad-3b5c-9a0c-a63f3e8b4148 | -3.23566 | -50.30119 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3aa3da99-f968-3b1c-a865-af8906208e92 | -3.13741 | -50.45039 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 496b9b6f-6f8b-3ba7-9532-e8f3f173a96d | -3.24349 | -51.23452 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b24ddd5b-e835-3433-850f-5056d2acff79 | -2.59244 | -48.31353 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc22038a-63ee-35de-aefb-5e2b129d09e7 | -2.80789 | -46.64977 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ce78254-52b5-38c5-b1c0-397127fc2966 | -5.72951 | -41.98894 | 2024-11-10 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| da0affa8-0968-3eb1-99f5-1471b0aaf8fc | -1.98519 | -49.01797 | 2024-11-10 04:14:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d10b2948-22cf-3c1a-8243-319fa256f9a1 | -3.37948 | -43.79677 | 2024-11-10 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 454a9570-f425-35d1-b665-a28568116013 | -3.02151 | -50.45535 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ad00853-55b2-3de5-aa9c-befa1587d4d9 | -1.53242 | -52.2051 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7057dcd1-134b-3562-92d6-3bfe5ae56415 | -6.72414 | -40.81879 | 2024-11-10 04:14:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 21c805f4-e7a2-3878-88f3-154aefb47550 | -3.11904 | -45.96847 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85a744a8-d4e9-3365-9bee-3104978a240b | -5.17217 | -47.61163 | 2024-11-10 04:14:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9018c7b2-2aa1-3bab-a0d4-45226e6be8f2 | -3.96525 | -48.12297 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e404a10d-3b7f-386c-96bc-669c9ffa9967 | -2.56847 | -54.73219 | 2024-11-10 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d67c76b1-ab90-31c3-a97f-9c993e1c3659 | -2.76695 | -49.36394 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5be91f14-4b21-3598-b8bd-52ed178fccad | -2.40646 | -46.29594 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0abc5cb-dcd9-3d93-acff-9966f9b9d8f2 | -3.31378 | -44.39183 | 2024-11-10 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 357221c8-3901-33f9-b66b-43144074053d | -3.12366 | -45.23589 | 2024-11-10 04:14:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 083f5639-b061-32d0-bd0e-7dc194b7b98f | -3.22811 | -50.32547 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b145036b-d753-31cc-a6ff-2a14ee12d25d | -1.75018 | -55.03795 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aca9104c-d4bf-3438-be60-af8cade18fd4 | -1.19725 | -51.99557 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebdcd5bf-01a3-3a4e-ae10-c2413d1606f8 | -2.42839 | -45.54818 | 2024-11-10 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4780e48-939a-322f-92de-d608e51dd3c6 | -2.43729 | -45.98546 | 2024-11-10 04:14:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3b7ebeab-7912-3452-ad06-5d98fba9f146 | -4.39581 | -41.90601 | 2024-11-10 04:14:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |


[Clique aqui para ver as próximas entradas](README25.md)
