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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27132292-1b4b-38f5-9643-216b430184f9 | -24.57268 | -53.79404 | 2026-08-16 04:00:00 | NOAA-20 | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3b2dda8e-1bf0-3ea6-a98b-7a35335b361a | -24.57395 | -53.78885 | 2026-08-16 04:00:00 | NOAA-20 | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 31638549-2cb0-3f1f-9a79-a8caf7fbd251 | -6.1108 | -57.7035 | 2026-08-16 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 35723514-8765-30ca-8e74-930bbb12c549 | -8.4275 | -62.676 | 2026-08-16 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| e8d99c6d-b6f8-312b-bdd8-af381cd4467a | -6.8387 | -56.4344 | 2026-08-16 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a9699f94-4e5e-3913-b19a-238054893b7b | -8.96 | -60.5358 | 2026-08-16 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 150.4 |
| d65a4f2f-bf50-3d40-8c4b-b85be47950fc | -6.1107 | -57.723 | 2026-08-16 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 85f5e0d3-e324-3430-ba25-599220b19f94 | -8.9787 | -60.5156 | 2026-08-16 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| b65d9770-2c2f-36cd-becb-251d3f422c56 | -6.6378 | -59.0602 | 2026-08-16 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d5207510-0b2d-3848-90f5-88026ebfb9ee | -8.9415 | -60.5174 | 2026-08-16 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1eb87fcb-b371-3f6c-9c70-64d5f1b39199 | -8.9601 | -60.5165 | 2026-08-16 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 42cf97c4-c394-36f5-8c67-0a6d00e3e165 | -6.1106 | -57.7425 | 2026-08-16 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| d1160ddb-fda9-3414-8957-a8ebf8dc1ac3 | -8.9414 | -60.5367 | 2026-08-16 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 20f60ce9-e3da-3c7f-b93f-5ab12a93621c | -12.7017 | -48.4753 | 2026-08-16 04:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| f4b356f3-ee16-3d86-9d84-6f2b6e16fb7a | -6.7123 | -58.9412 | 2026-08-16 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| e35ee96d-85b9-3cbd-b5bb-03c8d07e8f54 | -6.6377 | -59.0795 | 2026-08-16 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 743783b2-e4f7-38b3-964d-1c731beccae3 | -6.0923 | -57.7238 | 2026-08-16 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 41734925-1104-3e72-8588-ca0c14783bac | -6.82 | -56.4551 | 2026-08-16 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| dc69a420-5255-35b8-a0e7-ea228851cfa6 | -8.9785 | -60.5349 | 2026-08-16 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 76e6898b-cdd8-36c3-a3b9-d9ed9b0ebf6c | -6.6194 | -59.0609 | 2026-08-16 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d67f40f8-a41c-3739-b8e7-3429393f89d7 | -6.6378 | -59.0602 | 2026-08-16 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 9b610403-4af2-3e00-adb8-86e2948a2710 | -6.6194 | -59.0609 | 2026-08-16 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 547c9512-d3e6-3310-83b4-aedc1f35a089 | -8.96 | -60.5358 | 2026-08-16 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 49fe81b4-fdd6-3da6-ae8b-7781224f23bd | -12.7017 | -48.4753 | 2026-08-16 04:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d1605458-1ad4-359e-a23f-e97216412d6e | -6.7123 | -58.9412 | 2026-08-16 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 6e331e05-5ad1-32df-bcf9-94c4d57a9d55 | -8.9601 | -60.5165 | 2026-08-16 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 00f22d29-9853-3420-a233-ae07e4e3d871 | -8.4275 | -62.676 | 2026-08-16 04:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| f8a0bcbe-2498-396d-9490-1af13e04e105 | -8.9787 | -60.5156 | 2026-08-16 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 0b5e1775-ded2-3b8c-9c0f-01c4b0408039 | -6.8387 | -56.4344 | 2026-08-16 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 19e38093-3853-3fc0-aefb-180f00b98fa9 | -6.1108 | -57.7035 | 2026-08-16 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 2b7a01c8-1e2c-3fbc-b2db-9d3ca6fdd1af | -6.6377 | -59.0795 | 2026-08-16 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 1d46bf36-186d-3910-ac4f-a72b382a382f | -8.9414 | -60.5367 | 2026-08-16 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 971d1893-22ef-3c64-addc-f249fabcef15 | -6.82 | -56.4551 | 2026-08-16 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f98e3d78-3480-3361-be76-18e25f954ddd | -8.9415 | -60.5174 | 2026-08-16 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 22be1f31-15f1-3f4c-9a73-0756e5f618d2 | -6.3137 | -43.6178 | 2026-08-16 04:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 1fba690e-c293-3334-871e-151fd51706ea | -12.0282 | -46.4471 | 2026-08-16 04:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| cc4ef40f-fab5-3e22-a471-e40775d71c1a | -8.9785 | -60.5349 | 2026-08-16 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 080362fa-c10c-3348-a6cc-bae2e1d27773 | -6.1107 | -57.723 | 2026-08-16 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 6115a33f-07d1-3b52-8aef-7c823c144f82 | -6.8597 | -58.9738 | 2026-08-16 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8bfbc18c-6e4a-3771-84ac-705d80500e41 | -6.82 | -56.4551 | 2026-08-16 04:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c354e890-e12c-39fe-8eb3-d8d2f2614567 | -6.6193 | -59.0802 | 2026-08-16 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 495b3edd-56d0-3765-844c-70ac2977afe1 | -14.3923 | -51.8867 | 2026-08-16 04:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 2500df18-f301-33e0-b968-7a9e8e703198 | -6.6938 | -58.942 | 2026-08-16 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 05bc1126-00d8-3482-b42f-9b6638e2b2af | -6.6194 | -59.0609 | 2026-08-16 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 26881f8c-dffb-37b3-8474-79cc4830770d | -6.3137 | -43.6178 | 2026-08-16 04:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| d089d598-8f60-3010-a687-15997e777676 | -8.9415 | -60.5174 | 2026-08-16 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1a6c979f-ca20-3a8a-beab-283f3f6117a5 | -8.9785 | -60.5349 | 2026-08-16 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9d98016f-93d5-3a8c-b2ad-00cab3fab2c3 | -8.96 | -60.5358 | 2026-08-16 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| eeafee0f-8f7b-3f94-b122-39f0b66a8cf8 | -8.9601 | -60.5165 | 2026-08-16 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 148.0 |
| cc15020c-7130-346f-906f-0fb4e3dd628d | -6.8387 | -56.4344 | 2026-08-16 04:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 9a12ebcd-073d-374b-95f5-77252e5e5ef7 | -6.7123 | -58.9412 | 2026-08-16 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e1f8e2ee-8f00-3f2f-a3c3-e06b02c41d8c | -8.4275 | -62.676 | 2026-08-16 04:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 2999a25e-528c-3ed2-af7b-dc8e6c4aa8d4 | -8.9787 | -60.5156 | 2026-08-16 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| d4260e15-db15-38f2-a6cd-c8b532b5bbf9 | -4.11047 | -50.99393 | 2026-08-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bebe959c-07b7-3857-aefe-68f8e8ecde4b | -2.59878 | -47.34956 | 2026-08-16 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85afe5a3-3160-393e-ab13-9d0dd021ec5f | -4.10979 | -42.49851 | 2026-08-16 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ee504afb-13b9-368e-b5fa-cb9453b8433d | -4.10913 | -42.50292 | 2026-08-16 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e8a7f7b7-55a6-37ac-be7e-7ff9c86b8d1d | 1.58098 | -55.78366 | 2026-08-16 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cdaeb3e-7a7d-37c9-95d6-c17fdccfbb67 | -1.8044 | -48.06314 | 2026-08-16 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da802225-299f-3f16-87da-5ca379e95114 | -4.09642 | -42.49649 | 2026-08-16 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 432dabee-5076-3852-8b9a-9e2fd841b4b1 | -3.05675 | -46.93121 | 2026-08-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18f5008e-7df7-3349-807d-15ee216d1b4b | -4.33105 | -48.71896 | 2026-08-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3bc42d0-143a-33f7-b93b-3320006acb8a | -2.81592 | -46.71736 | 2026-08-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feeeee39-f62e-3c8d-8a65-c69d33264706 | -3.4981 | -48.03931 | 2026-08-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80dbd17f-b960-390f-a6a6-d4db6c0ec571 | -1.57111 | -47.74737 | 2026-08-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bfcf153-f59a-379a-b973-dd84e736c90c | -4.01424 | -49.46264 | 2026-08-16 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 809c5c9e-1865-30f0-b5d2-f6fe18d4961d | -1.80109 | -48.06263 | 2026-08-16 04:38:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 855d18d0-55f7-3a25-8b6f-9945e2c9fec7 | -3.34924 | -43.51141 | 2026-08-16 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b54e931a-a9d5-37c5-839c-9bf26d6ff9ac | -3.50475 | -48.04034 | 2026-08-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08d00940-e2a9-31a4-8a43-a5acd6caac8b | -3.55834 | -49.20407 | 2026-08-16 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62917dbf-ac38-393f-b477-bb4caed2dfa0 | -4.09512 | -42.50526 | 2026-08-16 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 750f7656-567a-3580-9844-a909a71697f6 | 0.48697 | -60.59435 | 2026-08-16 04:38:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e64e01b8-2e5d-380d-ba8a-e91b1d8d00b2 | -3.50197 | -48.03635 | 2026-08-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2010521-d093-39cb-a8a5-75f2b06b8938 | -2.43404 | -47.03125 | 2026-08-16 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bc52cf03-14fd-3b5c-8979-7422e130fbeb | -1.58976 | -50.44047 | 2026-08-16 04:38:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9d7e8721-6881-31ad-9e31-9b6e8f7819ba | -2.41898 | -48.7221 | 2026-08-16 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75c7caae-a270-3d31-83b3-99012763af80 | -3.96011 | -49.44011 | 2026-08-16 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bea43be4-795f-37ac-8dba-fff4fa78e115 | -3.50142 | -48.03983 | 2026-08-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 288e319e-8591-3386-9805-780bdcb23360 | -2.7687 | -48.57299 | 2026-08-16 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f679ed60-9f59-3f41-bae7-32d7250faa2e | 1.5801 | -55.778 | 2026-08-16 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e260f09a-0130-3408-b5a5-abc9329b3f06 | 0.49362 | -60.59327 | 2026-08-16 04:38:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddb88022-09a2-3f28-b445-3f22b3d8100b | -2.50468 | -48.34914 | 2026-08-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 173ed7e0-0558-3808-8727-8f0f97119997 | -2.76593 | -48.56905 | 2026-08-16 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| da9a4074-ee67-3f68-8fc0-34b118ba0255 | -3.96065 | -49.43666 | 2026-08-16 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| deb1590a-0b4b-351f-94bd-68a20d1d9838 | -5.34259 | -43.17801 | 2026-08-16 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47c3c6b4-5790-39f4-b3b5-72168c476688 | -4.10533 | -42.49783 | 2026-08-16 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 572ec4aa-aaae-3561-9b4f-d8a9024de183 | -3.96342 | -49.44062 | 2026-08-16 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1bcdf387-098c-3d52-b9c1-09b06212fada | -4.27321 | -48.56514 | 2026-08-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1cecc5f7-5003-3e1c-b5d1-ce643be02050 | -4.25217 | -48.54777 | 2026-08-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a35ac740-8d24-300e-b5cf-116b15c282ae | -4.09577 | -42.50087 | 2026-08-16 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 935a63de-29eb-3c2b-b84d-75c902eea7ff | -2.82733 | -46.73429 | 2026-08-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b0060a77-3e38-3c14-99b4-9e7cdb1b7e5c | -4.0137 | -49.46609 | 2026-08-16 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04909456-49d2-3aac-ab02-2ef76d75af82 | -4.10088 | -42.49716 | 2026-08-16 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 54411948-4529-35e7-97ce-3eed883bfe4e | -4.10782 | -42.5117 | 2026-08-16 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 818fadf7-8499-306f-93c8-9dec59aa99f0 | -3.50529 | -48.03688 | 2026-08-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d68e3d8-febd-3ac6-bbba-4a73b79522cb | -2.99727 | -47.74009 | 2026-08-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ece50f6c-16f4-3d01-96ed-b0f981244246 | -2.49826 | -56.05824 | 2026-08-16 04:38:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a3539aa-7947-3d57-a04a-d05c06d084b8 | -2.37464 | -48.3989 | 2026-08-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c15ace8-1d92-36e6-8b42-9c1bfc80ad67 | -1.81085 | -54.87236 | 2026-08-16 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7e1f311-36dc-3705-ae7f-02ebbbfa2211 | -0.83583 | -47.35916 | 2026-08-16 04:38:00 | NOAA-21 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README16.md)
