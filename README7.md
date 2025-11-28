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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3ddb89f-aeeb-317f-80b4-bc112253a706 | -5.98729 | -44.60156 | 2025-11-28 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f55010d-5aad-30af-a07e-493c3004a967 | -3.75139 | -46.96311 | 2025-11-28 03:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 94b42dfd-c52a-3b9e-8976-be6a1036cbcc | -2.90338 | -39.97491 | 2025-11-28 03:42:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| be0860c8-ff43-3e48-8fb5-c2563cd6255f | -3.76619 | -47.14143 | 2025-11-28 03:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ba2c563-50c9-3419-91c4-4ed9d8010ed8 | -5.15661 | -38.08321 | 2025-11-28 03:42:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 762450cd-ded8-3d04-8cf1-a378705524c6 | -3.51054 | -43.6824 | 2025-11-28 03:42:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d70fa5e7-4c87-325c-87a3-df6d301858da | -3.75749 | -44.95333 | 2025-11-28 03:42:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b215dd96-3729-3618-a51e-81fe8e41b677 | -2.74801 | -47.13965 | 2025-11-28 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e383d0cc-3d69-35d5-b0a3-fcba674b1fdd | -2.71508 | -45.22534 | 2025-11-28 03:42:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f982466c-fff8-37c6-a745-cb91ff7a71be | -4.94796 | -48.63148 | 2025-11-28 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2dd4cad-91e2-3429-b0cf-531403b579f0 | -3.31973 | -44.16833 | 2025-11-28 03:42:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 80843484-3dec-3c29-ad07-d0f1010b479f | -2.42408 | -45.78776 | 2025-11-28 03:42:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6880946-1a95-310e-b192-86ba21e14edc | -2.70032 | -47.41875 | 2025-11-28 03:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d081ee2e-2551-33d5-bcb7-e9caf2ba89b3 | -5.48426 | -35.52274 | 2025-11-28 03:42:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d3f286c-ec77-3da3-b86a-690b40c559b7 | -3.85803 | -47.04191 | 2025-11-28 03:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c396f64e-3be9-3f02-ac36-ece698afd3a6 | -5.49158 | -36.69452 | 2025-11-28 03:42:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1a412c16-ad08-3609-84e3-084d5d5fc874 | -2.23121 | -47.5092 | 2025-11-28 03:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48f5827f-3b00-3a64-a953-ecea54786d03 | -5.57059 | -45.16895 | 2025-11-28 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce0a6852-68c3-35bd-8dda-c3d2246619b6 | -2.71326 | -45.21822 | 2025-11-28 03:42:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0dd2368f-27a2-3206-b27d-e33b8b492b00 | -7.40757 | -39.11816 | 2025-11-28 03:42:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bb046b48-1e69-3a00-b1ab-9ab893ebb1ad | -3.3197 | -44.16769 | 2025-11-28 03:42:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de999d94-3056-37de-850e-0acd10727591 | -2.70142 | -45.67409 | 2025-11-28 03:42:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4682b656-e68b-3eab-9c71-3279ac7bb5f5 | -6.72783 | -40.82412 | 2025-11-28 03:42:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 528746b8-9960-3ab1-974f-56cb0bd55222 | -3.29694 | -42.42881 | 2025-11-28 03:42:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c6b0690-e520-3ed0-950c-2f94ab8d8e24 | -5.54275 | -39.23822 | 2025-11-28 03:42:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ed255a20-3184-3f1a-9d0f-67e9da28de7c | -2.61716 | -47.36361 | 2025-11-28 03:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c8eeaa10-5c43-302a-b1c2-3d85f37098b1 | -2.70065 | -45.67874 | 2025-11-28 03:42:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b31c2195-15e8-3800-ae14-34af57800b7d | -5.05843 | -40.82065 | 2025-11-28 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| da5b2e28-7ba9-385f-8c3a-8fee1002468a | -4.30041 | -48.60365 | 2025-11-28 03:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f0f61b5-6eae-3b6d-815f-2cfa424944cd | -6.71671 | -40.81431 | 2025-11-28 03:42:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dc1f528b-4008-3deb-8dc0-c8921630d724 | -4.16702 | -43.7519 | 2025-11-28 03:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce58bc3d-d8de-3891-b820-e38af3f2028a | -6.78442 | -38.33771 | 2025-11-28 03:42:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2470eca8-2ed0-326a-b9aa-20a55b5aefe5 | -7.96409 | -35.24672 | 2025-11-28 03:42:00 | NOAA-20 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b63171c1-8b88-3a53-8555-4cd96e1d4bfc | -6.91868 | -38.63135 | 2025-11-28 03:42:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 6.4 |
| ac3aa3f6-a9c0-3ead-bda1-060190eea6ca | -2.90398 | -39.97112 | 2025-11-28 03:42:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c3c5cadb-df0b-3928-9061-5464f434b807 | -4.17175 | -43.75601 | 2025-11-28 03:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 247e4c54-8f20-36bb-9373-c223403bf797 | -4.23503 | -38.03917 | 2025-11-28 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0cd92583-6d52-3ce9-9ae6-55ae96918e78 | -3.32033 | -44.1647 | 2025-11-28 03:42:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7fcf3102-1668-30fe-be78-3a3c6a4a9d9e | -2.90754 | -39.9756 | 2025-11-28 03:42:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c036f668-8757-3621-a871-fb337205927e | -4.23434 | -38.0434 | 2025-11-28 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 80c5d562-ac5f-3fa2-9ce4-f6ee31faca53 | -2.90815 | -39.97181 | 2025-11-28 03:42:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 07625df0-c5c4-3d5c-83a5-9e342f4d77bf | -7.04941 | -35.31782 | 2025-11-28 03:42:00 | NOAA-20 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| efb5e9f2-68e1-3494-9ddc-4d234e4ec7c3 | -5.28894 | -44.96749 | 2025-11-28 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c78579f-3286-3174-9ef4-163c4582b723 | -2.61148 | -47.35593 | 2025-11-28 03:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0891d0ad-99f4-3a98-9954-1ab297c78b15 | -4.9427 | -41.19948 | 2025-11-28 03:42:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fbc39939-5502-3e6d-be9b-747e3a45d143 | -4.25928 | -46.24305 | 2025-11-28 03:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50e59ed6-9197-31c1-9fe2-9c7782dca489 | -5.81454 | -39.21645 | 2025-11-28 03:42:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c216068-e74f-3e51-963b-c22f1739ed1a | -5.35312 | -44.88558 | 2025-11-28 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0590b509-cede-3a97-bbcd-d9e153ce9eb1 | -4.56058 | -40.65541 | 2025-11-28 03:42:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7cd4136b-3611-326e-8e34-c3e3f812ae8f | -2.98784 | -45.42576 | 2025-11-28 03:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bd51310-b90e-3f52-94c0-0c3933a98a8b | -4.17231 | -43.75274 | 2025-11-28 03:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57f107f4-32c6-3996-9b51-3c2bac2c2f36 | -5.75418 | -45.1172 | 2025-11-28 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d741d88-0cb1-3ca9-a43c-f3d68e520752 | -5.84541 | -37.99078 | 2025-11-28 03:42:00 | NOAA-20 | ITAÚ | RIO GRANDE DO NORTE | Brasil | 2404903 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 27514ce1-2e69-3ee6-801f-ced549e0e273 | -3.74487 | -46.96196 | 2025-11-28 03:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bae29b6a-1dcb-310c-9ee7-102406b697a6 | -4.94673 | -48.63831 | 2025-11-28 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1552e8c4-565e-3a27-895d-af0b62efa534 | -3.7579 | -46.96431 | 2025-11-28 03:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 923e59e1-2b8c-33f9-889d-14636acb4da9 | -2.71397 | -45.21387 | 2025-11-28 03:42:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60615435-4e10-3987-b51a-150297bc80a3 | -4.68515 | -44.43036 | 2025-11-28 03:42:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 211dd351-a6ff-30f2-99bf-12f7ff6a2f8e | -6.72302 | -40.82732 | 2025-11-28 03:42:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 04dcf018-f421-3b5e-9e8f-8ab4550bd773 | -6.72717 | -40.828 | 2025-11-28 03:42:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 37cf574c-0e00-3ad5-a7ee-920ee6a6bf62 | -9.39176 | -40.37565 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 96d98977-4984-3028-aac6-1562e2306c15 | -9.3827 | -40.35898 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| fbdea11e-6af1-3803-ab96-9bb17454b516 | -9.95015 | -36.30962 | 2025-11-28 03:44:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f56283c5-854a-35ad-9495-5fc5f3520fdf | -9.56108 | -35.84661 | 2025-11-28 03:44:00 | NOAA-20 | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fbf3de9a-a6b9-38f5-9d90-395f8421de49 | -9.72218 | -36.26894 | 2025-11-28 03:44:00 | NOAA-20 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fe831903-9b80-3821-9b74-4513584afaf2 | -9.38572 | -40.36454 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 716fabaf-b421-3cc4-8537-ee3152da8939 | -9.38621 | -40.38476 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| eabdce57-9d85-376a-b54b-d60b9e4a11f0 | -9.38705 | -40.37988 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 88371791-64d7-3c1c-888f-572970859c04 | -10.0592 | -40.42752 | 2025-11-28 03:44:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6654a643-92aa-323b-8e1e-b1f9976de8b2 | -8.77049 | -40.38112 | 2025-11-28 03:44:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d68358c-4533-30ca-a5fe-b8562e26615d | -9.38016 | -40.37365 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3fe1dfa2-83cc-31d4-b46d-0349a866c3a4 | -9.38234 | -40.38409 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2584d5d6-255c-310f-8580-20cb2caad0ae | -10.14048 | -36.13638 | 2025-11-28 03:44:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b3fa8c73-adee-3303-b962-f251328791bf | -9.39092 | -40.38054 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1c8f0d41-8d26-3a9c-aa9f-02ab38440a94 | -9.38403 | -40.37432 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| c091d869-993c-3565-befe-8d725a2aeeda | -8.37754 | -41.75597 | 2025-11-28 03:44:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| abd3752d-8d73-3a73-a5d4-586af95bb497 | -9.38874 | -40.37009 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 2e4fc8ca-5477-3d80-bb3e-0c32d91bbd11 | -9.38789 | -40.37498 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| a55f1c2b-81c8-32b2-a9a7-4b501f3fb397 | -9.38101 | -40.36876 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b90faea-8dee-32e9-8cba-b93929be6855 | -9.38318 | -40.37921 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5c756ffe-543f-3698-a0c2-67204a5efdbe | -9.72163 | -36.27243 | 2025-11-28 03:44:00 | NOAA-20 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 46eb4b92-86fc-37a9-9527-7f6717dcbef7 | -9.38487 | -40.36943 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 06cd609a-af88-3665-aad9-fc06a5cddc9d | -9.3926 | -40.37076 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| c5e6778b-593d-3fc6-9b49-a6204269a994 | -9.38185 | -40.36388 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7f4eadae-8b95-3273-8e88-17d16142738a | -9.39647 | -40.37143 | 2025-11-28 03:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| d22f4d68-94e2-31ed-aff4-319d942b50e2 | -10.13993 | -36.13987 | 2025-11-28 03:44:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec22b4f2-5a75-3d52-8e10-8556351c8660 | -9.07355 | -41.27357 | 2025-11-28 03:44:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4537d73e-83a2-3e4b-83d8-d9b98983e9f4 | -8.38183 | -41.75674 | 2025-11-28 03:44:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 965ffe72-733f-3dc7-96de-1f0bec46f476 | -19.98309 | -49.99575 | 2025-11-28 03:46:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 2048d047-aaab-38da-88b1-6c2bcc9fbb79 | -16.41545 | -43.12373 | 2025-11-28 03:46:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8f687df-9358-3917-b2d8-3afde3c8227b | -19.98432 | -50.00241 | 2025-11-28 03:46:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 75d159a7-aa9b-3cf7-847d-c68cefc5d1e7 | -19.98202 | -50.00041 | 2025-11-28 03:46:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| bfc75a2f-6766-3313-88b5-ed4a0a047683 | -19.97951 | -49.99617 | 2025-11-28 03:46:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 479bbdb8-db7e-3765-b7b6-a78a96819b4d | -21.7539 | -49.03455 | 2025-11-28 03:46:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ba067106-28e7-3634-af4e-c7eae53bdb2a | -21.74859 | -49.03299 | 2025-11-28 03:46:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e3518390-0c40-35ea-9d2d-5ab04dca46eb | -22.47607 | -49.12608 | 2025-11-28 03:46:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cb1748c-fa3a-3e22-9432-c9547fe0202f | -21.68959 | -47.96026 | 2025-11-28 03:46:00 | NOAA-20 | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 761130d2-56c2-3012-827e-fc823180542a | -22.47159 | -49.12111 | 2025-11-28 03:46:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38deb862-2cc2-32b7-90aa-d8b534062091 | -21.25806 | -50.30184 | 2025-11-28 03:46:00 | NOAA-20 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7252b4d9-395b-356c-8eb7-68ab009ac4bb | -22.47428 | -49.12226 | 2025-11-28 03:46:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README8.md)
