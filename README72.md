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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d8edca3-0153-30e6-9025-7ba3edd08824 | -2.78413 | -54.16936 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f5a506c-105d-317b-9641-16eb2e40b61b | -2.82714 | -54.04795 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd3a342f-dab9-36c6-aa1a-c5bb45982ced | -3.455 | -51.62804 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea67dc47-12d8-3ff4-85af-f0e4b0b6f949 | -3.80858 | -47.80202 | 2024-11-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7fb9b203-36da-3ffa-be7b-023a831c02a5 | -3.03879 | -51.3304 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c7779a4-4747-3d7e-abea-891ec750abe9 | -4.84784 | -50.86156 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a03d24a0-34ed-3ac4-8c53-4220630d4b33 | -3.52248 | -51.39418 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31f09e4b-5d25-3c2c-8b44-8d494bf59aca | -3.1881 | -54.32193 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16d0b788-ca56-3aa9-b6f6-157632730718 | -2.58457 | -54.03456 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a30f3fe7-e638-3722-92a8-59e59628c9a9 | -3.12507 | -54.18324 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5757060d-573d-323f-9148-71f0c4cff140 | -3.66584 | -50.44053 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df2bfe5e-f640-327d-af87-d54b4a933228 | -3.27952 | -50.52341 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4800e23-36bc-36c1-9787-6b38bdbea89c | -2.57132 | -54.07526 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c7ab42b-6b19-3570-abde-c128eddade3c | -3.56212 | -51.36573 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13dc97c4-119e-3013-9af8-b2942cc1e420 | -3.19863 | -54.32 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec58ed01-bf93-3b16-a114-c8f241bbb51c | -3.51415 | -54.68918 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 746aa68b-a954-35b4-af9c-5bc50a0a3241 | -2.41678 | -54.60167 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83953626-64d6-3898-ae78-6b2f7d598329 | -4.39061 | -45.59563 | 2024-11-21 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89c8b321-c3b2-3f81-b93d-837418dd842e | -3.49683 | -50.45031 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f3a404a-ce23-3af7-8944-afb48fc85080 | -3.27523 | -50.21493 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d24c2be-eafe-397a-9c14-2bb203f4bb19 | -3.4196 | -53.28388 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be0d18ea-4baf-3591-b938-4404504685e0 | -2.83315 | -54.00984 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac4ceb78-85f4-3573-83d6-dc3131e68160 | -3.106 | -53.98145 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d160d8d-5ea4-3f51-b088-3928a0b78a03 | -3.41482 | -54.90326 | 2024-11-21 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0bed1a1-c6c3-3445-8a60-36e5c949f57d | -3.19087 | -54.32595 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81e2d97f-959f-3c78-b9be-a7feaf1fbebc | -2.63255 | -54.28833 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad268442-dea8-3032-a9e8-6db409924f3c | -4.08389 | -49.28958 | 2024-11-21 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a309c3b9-49eb-31bc-bf71-8b567c8bd74c | -2.71744 | -53.17025 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c998965-49f8-31c4-84df-73597bb137c9 | -3.77194 | -51.81866 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84867052-9a93-369b-8672-d665e9a5b77c | -2.76067 | -52.10928 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8514af91-80d0-3584-a01c-68f6680ca091 | -3.74608 | -51.60355 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9adea947-23c3-3bb4-9255-38e5f1003085 | -3.73616 | -53.73489 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f65b5af-f823-3983-8c9b-001efdcd4bc4 | -3.4462 | -52.3343 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6005eb06-6fc7-32e2-8ea7-37022d3e1cc9 | -2.61923 | -54.26836 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed59f62b-c4c9-31c5-a874-865ab8de830b | -2.82379 | -54.02612 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0296bb13-a397-3419-abe9-d821d2dad410 | -3.28685 | -53.8264 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70526b05-b908-386f-9b70-bcf3c7cfa8ce | -3.53437 | -54.08762 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 904d6daa-b3fd-3c3c-a6d4-f803afc67247 | -3.91898 | -50.11399 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 619cc822-0063-3114-88c8-7c31b31f1205 | -4.61086 | -49.59442 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce2989d9-a2cb-3359-91f1-7cb39dc2bd53 | -2.91998 | -53.06806 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5788483b-5427-3021-852b-91982daf98fd | -2.7849 | -51.72173 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01d1ccf0-278d-3468-b681-4d417a697f3f | -3.30476 | -51.28954 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 861c4775-8c60-3cf0-8409-8aeb67f4343e | -3.30478 | -50.35997 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20d651ee-122d-399d-adb9-3391f04b3f70 | -3.75925 | -55.57748 | 2024-11-21 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d118930e-61f6-3d7c-933c-b87fd7034bc7 | -3.51787 | -54.17026 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 199a1192-4296-3096-b4e0-6f1eb017e71d | -3.02838 | -54.10764 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0faa251a-2acb-3950-bdc7-3f088b27ff41 | -4.38664 | -47.77315 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba1bb955-3a23-304d-a9c9-21d5a6c7f548 | -2.85743 | -51.2809 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 219b0639-fad0-39da-a9c2-f59ad45fae6c | -3.10704 | -53.73793 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef21da78-11f8-339a-b0a1-0d49c7c98bc2 | -2.58255 | -54.21963 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21add7a3-1c8e-3ede-ab57-15507c06857e | -3.56555 | -52.15665 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 962212de-b265-3776-bd8b-f14ff783b553 | -3.34257 | -54.07561 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efa2b77c-8984-3c6c-9759-e2f5379d82d4 | -2.60119 | -54.05855 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e1adc10-81f5-3f86-9141-b0ecb97e4cc5 | -2.57299 | -54.08622 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a44aef25-4c05-3eba-8a83-486739e592f9 | -7.94808 | -50.0132 | 2024-11-21 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a467eb86-fa6f-3a3a-98de-a1e42d439e1b | -3.80635 | -52.22668 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5abe0eb4-0b61-3a4d-8b2b-90334ccaded7 | -2.39034 | -53.71374 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c699788a-c1df-339a-9cd1-d95b2756b94b | -3.02586 | -51.52604 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 022f460f-8cd8-35dc-a666-1b75a165e7ea | -2.79449 | -54.01799 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98fc4786-c7e8-3ad8-a9aa-80d2f190bbc3 | -3.33769 | -53.30982 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45735f12-07f9-304e-aefc-2fee16940ea0 | -2.62146 | -54.27588 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80f30cc5-37b7-39ea-9a77-85e57cf0c913 | -2.57077 | -54.07874 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5dde86c-4c5d-39f2-85d3-879020c7aee3 | -6.29667 | -45.34029 | 2024-11-21 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08cb2968-a148-36e8-ba95-529d2c1dc9e8 | -3.29129 | -53.8412 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0882f3f1-f155-337c-94bf-4f7c00db1877 | -3.28967 | -53.85153 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 66b07850-d28f-3884-925e-c54453e1c34f | -3.39637 | -54.27266 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ae293a2-0b97-36e5-ba9b-59f0af36efc2 | -3.91215 | -53.82619 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| adcba0ac-e3f7-37e4-9890-9f75a94360f0 | -3.38742 | -54.65191 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1c9d09f-06b1-383d-a5f7-0e4e936b9466 | -3.61209 | -50.62048 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32ffc4db-3529-35ad-9ee7-a05a7079dfc7 | -3.42176 | -49.22794 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e2bf523-96b4-359f-a72c-c653b67adede | -4.40519 | -42.14743 | 2024-11-21 04:55:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 75117811-c24b-3179-bc27-7712207d89cd | -4.96335 | -49.84713 | 2024-11-21 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db29ba6d-eeaf-3447-86e0-bacb22a26a09 | -3.59802 | -51.47484 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9cdc00b-a9f9-3944-854f-d7ae58d05959 | -3.41718 | -49.23211 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98f6bfc1-d148-35d4-94c4-3c731a90f083 | -3.76946 | -50.70024 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d22abbe-9be5-3f18-b538-589dbd00410c | -3.17313 | -53.64271 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5e09eef-dec8-36a2-8287-ac301e2bc302 | -4.76913 | -44.49694 | 2024-11-21 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 277799b9-417e-3dbb-b68d-af298821d094 | -3.31198 | -54.74507 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65d7b4db-1f31-339c-ba5e-78b47bf46b97 | -3.32478 | -53.00069 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91630931-59f2-3ad6-b8a3-7dc3b96bb2ce | -3.31278 | -54.07085 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23ff943b-9b81-3614-be28-82119ed16bb5 | -2.75856 | -54.0298 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c439b27-bbe2-3b00-b551-d9e2f11129be | -3.93109 | -50.03606 | 2024-11-21 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0ae50df-3190-3e72-924d-a2a7abbe6e3f | -3.20086 | -54.32748 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c2bfe02-7d54-393a-ac82-f140a7f2601a | -2.60004 | -54.02274 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dad39d76-0a96-3437-860b-fe6da34ff6bb | -4.20087 | -48.12315 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c255213-7993-30cb-a7c1-1e341c4daf74 | -3.29351 | -53.8486 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 518b895f-ac5a-30d6-ad2e-56b5c28403fb | -3.48514 | -54.69912 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35df907f-a8c6-3fce-9323-7879d5e921b2 | -3.86553 | -51.96625 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b95e11a-86c7-3402-80c6-00dee81dff25 | -3.67109 | -54.27634 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f32c1fd-368d-3f43-bb2a-fb068f7ac0f3 | -4.15959 | -42.01932 | 2024-11-21 04:55:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c0cff06b-ed4a-3bbc-b446-a1318c276723 | -3.7495 | -51.60408 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76adf19d-39a5-32b7-a2b2-132a393b13b8 | -3.0033 | -51.30952 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba4a2a4c-423a-33d5-a71c-270ce4c63f96 | -4.12892 | -49.43321 | 2024-11-21 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 489325f0-245b-32d0-9e7f-a74c3dcf7bab | -3.81654 | -51.35357 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48682fe3-3cf6-3d1d-bbac-5bebe17c0a0c | -3.55053 | -51.4408 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e66269f9-ac38-3d08-bad5-e69111dee55d | -3.40003 | -50.25438 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2098545c-5f16-3821-abce-27ff3a79c107 | -2.56629 | -53.99971 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19d12ba8-a60b-3dae-a104-f6b4d10c8368 | -3.18323 | -53.25362 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95fd3ead-248f-346c-ac71-950a5b5803da | -2.91668 | -53.06755 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 126520c8-0d6d-366c-808c-298bfbe62508 | -3.64241 | -51.4585 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README73.md)
