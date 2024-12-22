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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3e7147b-ff8d-3536-8944-a01b6fe65bbd | -1.25726 | -53.69279 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8913cd4-a5db-38a3-adaa-a21175fdb7e1 | -1.7215 | -52.57839 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 435f6c7e-55dc-3d5d-a9bf-195022e5ab40 | -1.28912 | -53.10134 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cc4c564-3051-363a-94bc-25c4b1e51316 | -2.79866 | -54.18833 | 2024-12-22 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01debe2e-975a-3082-8f60-1f09f3166338 | 0.64555 | -60.30604 | 2024-12-22 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e60b789a-1315-36df-8715-5f72072be942 | -2.63171 | -48.05059 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1417c885-0601-33b5-91ce-2f21473630ac | -2.63396 | -48.03542 | 2024-12-22 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4376bd35-8253-32a7-9365-2c877dbcc7a8 | -2.57709 | -49.45661 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6379556-91f2-350d-baeb-649229bbe641 | -2.22465 | -53.79454 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec9d9584-0a1b-3f57-b008-0b3715e90907 | -2.22846 | -53.79512 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4fde02bc-baee-3188-ac72-63eca21aaf4d | -1.54906 | -54.24622 | 2024-12-22 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4beee9f-3ede-37a1-98dd-19c3f88726c0 | 0.64491 | -60.30196 | 2024-12-22 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f75e0697-91c1-31f9-8cd3-cea9ea50b3d4 | -1.36563 | -53.69234 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 588a1725-8593-3b6c-900d-e4af8fd7b407 | -1.36632 | -53.68794 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8b0ff68-5846-3447-867f-fd4ac542532a | -4.54009 | -45.88457 | 2024-12-22 05:14:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72af0263-7bff-3f36-8195-bf729226b2d4 | -1.36424 | -53.70127 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 728ee167-e26a-392c-86c4-e8a6630ab53f | -3.75961 | -47.20229 | 2024-12-22 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 565f1e99-13b8-38f4-b14a-b52fea90e116 | -1.20783 | -53.3895 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a22df52-1b3a-33a1-944e-d0710df403e7 | -2.45451 | -53.70962 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e72d6970-9c43-3daa-a00c-125e093d96fd | -3.04046 | -52.71486 | 2024-12-22 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ede0a136-f3d8-3d5d-8b34-2fc1234caf3d | -2.50002 | -48.06308 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d5f0d057-d8b3-37f1-94a9-d39f2bd15028 | -3.94785 | -46.41739 | 2024-12-22 05:14:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 48625388-70e7-3a49-b40d-7cb2db6a8662 | -2.68647 | -54.84522 | 2024-12-22 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72ee12e6-f885-33b7-a1ed-ed63050d5312 | -1.36494 | -53.69675 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 40387025-68f8-3880-ae24-fa842c4744ff | -3.60137 | -50.63163 | 2024-12-22 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34716b29-b3d8-3d0e-8710-0dda7cfbe9da | -3.25733 | -48.88894 | 2024-12-22 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3809d4b5-5b1e-3263-9458-bcda8f290291 | -2.93156 | -54.30329 | 2024-12-22 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c7c7f7a-2034-34eb-a319-f418b7f8a4ac | -2.44763 | -51.79271 | 2024-12-22 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a361374-0da4-3d20-89a8-ef87cab5a349 | -2.80397 | -46.7555 | 2024-12-22 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad590ae0-e3ff-360b-873c-02a2e3961de0 | -3.94954 | -46.40559 | 2024-12-22 05:14:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11d86e43-2ff1-3ec9-9bfa-05358f8e10f6 | -3.20872 | -52.86429 | 2024-12-22 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bf7546a-4e37-33d8-90f1-99c2c1e528d7 | -2.66755 | -54.87215 | 2024-12-22 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d0bec6c-0a70-3c86-b884-8946f1c3f55e | -1.37183 | -53.70242 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fd2fc9b0-b392-3d71-b4f6-7e6ca94264c3 | -9.93115 | -59.90473 | 2024-12-22 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc4aeaf9-ce09-3ca8-b756-e01f5fa14391 | -9.92784 | -59.90419 | 2024-12-22 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54a9b049-ea16-3f79-a2e0-a97d4cb515b0 | -12.55607 | -57.75797 | 2024-12-22 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfd6f4fb-e4be-35b9-903c-c66498d24a0e | -9.92839 | -59.9007 | 2024-12-22 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f44a537-c7db-3f68-8c28-ac41b7f284be | -18.00614 | -54.4336 | 2024-12-22 05:18:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39bf009c-a155-3403-b244-1108571515e9 | -2.03731 | -52.11203 | 2024-12-22 06:12:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c7be24a8-6703-35af-a03e-355a66e8ee08 | -1.71647 | -52.5766 | 2024-12-22 06:12:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8c8b047a-701b-3fd7-a90a-d91d538060b8 | -2.4402 | -51.78555 | 2024-12-22 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| a231e9b4-c298-3e48-85cb-c107c5dda266 | -1.71456 | -52.58964 | 2024-12-22 06:12:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cbeb173b-60b5-315e-b4db-9c793acb57f8 | -1.35838 | -53.68929 | 2024-12-22 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 37cca04e-e0ae-3f77-8037-dc005b60815a | -2.03937 | -52.09774 | 2024-12-22 06:12:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| eddad276-10ba-324a-80dd-308791ed4eaf | -1.36809 | -53.69103 | 2024-12-22 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 509c84e1-f318-3c87-845e-e162ac082875 | -2.44334 | -51.77883 | 2024-12-22 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6fb239aa-6e4b-3a5f-9449-78afe24f03b1 | -2.68387 | -54.84134 | 2024-12-22 06:12:00 | AQUA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 35585d4e-28e0-36cf-a21f-707ffda0d5e2 | -1.71839 | -52.56353 | 2024-12-22 06:12:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| db6ad531-9b42-3d70-a6e0-58a63567bf7a | -2.51796 | -54.22049 | 2024-12-22 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e7266a4d-a816-3490-90ad-550f73b3af5f | -1.36654 | -53.7015 | 2024-12-22 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| fb214c73-4889-3a83-8ab0-b47f8639a2fe | -2.76642 | -54.34893 | 2024-12-22 06:12:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 41684760-1423-3c21-9f29-909280fe6c57 | -2.44104 | -51.7942 | 2024-12-22 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| be44805e-3d5b-300d-a983-ed90b792516c | -2.22286 | -53.79124 | 2024-12-22 06:12:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b639b64b-b916-3bfd-a1c0-0de3810d13ea | -2.5736 | -49.4609 | 2024-12-22 06:20:00 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| c22307dc-339c-38f9-a100-fe90d50c8360 | -2.5736 | -49.4609 | 2024-12-22 06:30:00 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 8c917c83-6d33-3522-a055-434324b7660b | -2.5736 | -49.4609 | 2024-12-22 06:40:00 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 83ae8bdd-62d7-3114-8281-8dba61b2c6fd | -2.5736 | -49.4609 | 2024-12-22 07:00:00 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 22b6a3b0-1489-3a90-814b-d43f0787cb31 | -2.5736 | -49.4609 | 2024-12-22 07:10:00 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 87cd1549-1656-3a7e-a6ed-5bf155831d59 | -4.0652 | -44.1169 | 2024-12-22 09:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 30442ffd-8b87-3d5e-bd6d-88b4ff054c81 | -4.0652 | -44.1169 | 2024-12-22 10:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 56b06557-e633-3898-a902-42c42760f389 | -4.0652 | -44.1169 | 2024-12-22 10:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 249.9 |
| bdc55047-18fd-39e6-9e11-7ec84c2aaf86 | -4.0653 | -44.0939 | 2024-12-22 10:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 29eb7f52-71b4-31dc-8050-2f940fe4bb48 | -4.0838 | -44.1159 | 2024-12-22 10:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| f720610d-37b7-3737-8861-6bc404ea53a0 | -4.0653 | -44.0939 | 2024-12-22 10:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 9553f198-8834-33bf-b57a-1da52ddcb973 | -4.0652 | -44.1169 | 2024-12-22 10:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 226.4 |
| 668232ef-8a4a-3c90-8cc7-7c3b55dd35ed | -4.0838 | -44.1159 | 2024-12-22 10:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 450d0502-67c4-33a4-994c-7a14f8b285bc | -4.0653 | -44.0939 | 2024-12-22 10:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 46c63698-85f8-3a22-aab6-74f6d640dd59 | -4.0652 | -44.1169 | 2024-12-22 10:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 413.3 |
| 1572f698-0f1e-3f66-a98a-95c7d27231c8 | -4.0838 | -44.1159 | 2024-12-22 10:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 227975ba-8355-38a4-9b62-ba815b7ff951 | -3.9958 | -46.3316 | 2024-12-22 10:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 376b9826-e58c-3539-a905-a92fd403d9f7 | -3.9958 | -46.3316 | 2024-12-22 10:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 4da80f45-6f41-309c-ae95-97ce7d3798d2 | -4.0652 | -44.1169 | 2024-12-22 10:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 366.1 |
| eea48f2b-c254-353e-813d-2f97e6ff8b5c | -4.0653 | -44.0939 | 2024-12-22 10:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 80a40f0d-0a96-354f-8024-75d91861b806 | -4.0838 | -44.1159 | 2024-12-22 10:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 7f5652d2-9a9b-3225-af9e-f68069ed5c08 | -4.0652 | -44.1169 | 2024-12-22 10:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 7226eae3-4a34-31f8-bf6f-d2492f837ba4 | -4.07 | -44.09 | 2024-12-22 11:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7bc455e-88e4-371e-846b-d92ae687cc05 | -4.1 | -44.09 | 2024-12-22 12:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ac2d929-b809-3c05-baf1-59b1b8a5467c | -4.07 | -44.09 | 2024-12-22 12:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d91e0da-e5a1-34d3-b431-c1d7e696a7bf | -4.08 | -44.13 | 2024-12-22 12:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4da17ecd-467a-3e75-ac2a-416bf22854be | -4.1 | -44.14 | 2024-12-22 12:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff0d3f2d-1227-34ec-8759-3b0cb71c3760 | -4.05004 | -44.13809 | 2024-12-22 12:06:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 98bb0570-4f10-34b3-b28c-9396730ca4c7 | -3.39727 | -41.5097 | 2024-12-22 12:06:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| abc1c9e2-8136-3600-b821-a30cb14aa992 | -4.09937 | -44.10266 | 2024-12-22 12:06:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 5678e355-a626-373b-997f-b0253c314eca | -4.31241 | -43.77192 | 2024-12-22 12:06:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 054584fc-b6a3-321e-95be-27a5d6d1ba0c | -3.4169 | -41.64759 | 2024-12-22 12:06:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 86d24f67-4e40-32f6-986a-2c6153749fd7 | -2.85524 | -42.05225 | 2024-12-22 12:06:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| dc122876-f3ff-33a4-a57c-a7b59b8679e0 | -4.09436 | -44.1351 | 2024-12-22 12:06:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 3d87d00a-54b8-3720-9d86-604b7ec9d3c6 | -5.16623 | -41.1052 | 2024-12-22 12:06:00 | TERRA_M-T | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 68cd08fc-17db-379f-8783-fd1bb214536d | -4.06179 | -44.13985 | 2024-12-22 12:06:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 275538d4-74df-33e2-99a7-c101b8b80fe5 | -3.39887 | -41.49895 | 2024-12-22 12:06:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d01354a1-80ea-3bf7-ac47-4e79237e6086 | -4.08771 | -44.12706 | 2024-12-22 12:06:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 555.8 |
| 8df355db-c548-3a58-a132-4139ad25d769 | -3.41527 | -41.6587 | 2024-12-22 12:06:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 6ba4735d-9712-388d-92c2-62b73468fc97 | -4.09009 | -44.11085 | 2024-12-22 12:06:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 356.8 |
| eb13f9da-577f-385e-9484-591f378c441c | -4.02075 | -44.25206 | 2024-12-22 12:06:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 27a81ea3-5aae-37bc-b710-630969676447 | -4.076 | -44.12508 | 2024-12-22 12:06:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1217.2 |
| f2ceea3c-b25a-3398-80b4-0fecc39187ad | -4.08518 | -44.11689 | 2024-12-22 12:06:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 789.3 |
| 5911c0ae-2341-3e57-a80a-23564f555ab5 | -5.41255 | -36.77562 | 2024-12-22 12:06:00 | TERRA_M-T | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 96e658bc-36d5-325e-846c-fa873587164b | -4.08768 | -44.10083 | 2024-12-22 12:06:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| a4bc4dca-1acf-3da3-97b0-4c51f936b8bf | -5.41112 | -36.78575 | 2024-12-22 12:06:00 | TERRA_M-T | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 9.4 |
| fed1f8ed-5212-332b-9d7f-7ac82b1a97ba | -5.37841 | -39.21554 | 2024-12-22 12:06:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |


[Clique aqui para ver as próximas entradas](README19.md)
