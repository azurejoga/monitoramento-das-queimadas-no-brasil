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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b49d2cae-1cd0-3d96-a4ee-dc466221d4d2 | -2.7828 | -55.338902 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dac2f549-d13e-3ee2-a2bf-1ec1295c13f4 | -2.8887 | -53.970501 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d63a89b-fdf9-3c2f-a937-c1b77cd0783d | -1.1085 | -54.114601 | 2024-12-03 00:37:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e11eea73-5af6-3cfe-a689-daee49738d1e | -3.2513 | -53.612598 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99d058e7-e8f2-3e49-9979-dc38e845ac4a | -3.6481 | -52.626701 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0f7ec56-d42e-3d42-ae85-57141ea84489 | -2.4576 | -53.6096 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5896f51-97cb-3673-8ece-de41c7f9f098 | -2.773 | -55.341099 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10d3d29d-ff1e-3e3a-aeb4-a30c0e415fba | -2.0797 | -52.250999 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 759167a0-af24-3818-b9d7-6416d11dd42a | -3.8831 | -50.066399 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee25d2df-ba0a-3cd0-9d41-ff9bb6951754 | -4.4638 | -45.7215 | 2024-12-03 00:37:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 694a5bf4-f7a4-376d-9804-3eda4a31e074 | -2.8868 | -54.146301 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7136e6-bed7-33ee-93a9-8ab2f729cd73 | -3.0307 | -53.409599 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86999684-8651-39d1-9e0a-379d657b22dc | -3.3377 | -46.048698 | 2024-12-03 00:37:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6099b896-c6c8-3376-81d2-9462a79e2778 | -3.1718 | -54.316002 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 437e44a1-a803-31f7-92c5-31e246c7d87d | -3.1159 | -53.973701 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38db063f-af02-3232-bd49-d4a87972dfa8 | -1.9034 | -52.840401 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76fe02b0-c3a4-3509-8be8-327e7cf84afc | -2.7962 | -53.053101 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b96b908-2980-3ddc-9a26-1fc48de8f81e | -1.7541 | -52.7789 | 2024-12-03 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 4b09d56b-df39-342f-9b3f-3c61bb38d5b9 | -2.3396 | -53.8013 | 2024-12-03 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| ba405cd4-f9b1-3cde-97e4-f6bfcf5e9e9a | -2.8196 | -53.0629 | 2024-12-03 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 06eeea6d-bd10-3703-a895-d74b27bfc30d | -2.0455 | -53.9474 | 2024-12-03 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a8c939f8-5213-3e67-9b4b-236678955438 | -4.5589 | -42.9289 | 2024-12-03 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 20bc70b0-fb81-34b0-81ca-fd7adb074890 | -1.0919 | -53.4359 | 2024-12-03 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 69c391fd-832c-3a81-b3d2-f02c929fb907 | -3.259 | -53.6388 | 2024-12-03 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 34c9afec-1777-3e1f-9d87-778972700a77 | -5.8197 | -46.4706 | 2024-12-03 00:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 0e3f50bb-e60a-3b8d-9267-221c44b39dd6 | -5.1181 | -43.1964 | 2024-12-03 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 5b3f7356-05e9-3df0-9ae6-ba9c7627c1d4 | -3.4617 | -41.9983 | 2024-12-03 00:40:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 474d30a5-633f-3217-95e9-c591930bb443 | -5.1367 | -43.2185 | 2024-12-03 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| b1f192bc-9e8d-38f0-8ba2-c77e7be9bdbd | -2.8212 | -52.5741 | 2024-12-03 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8f3b4110-4206-3c18-ae00-8ee73608d3f9 | -4.7485 | -45.1044 | 2024-12-03 00:40:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 07b90c5b-6a70-36cd-b021-262867d61da4 | -2.3645 | -45.7031 | 2024-12-03 00:40:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 141.8 |
| ee73a1d1-4caa-3393-939b-c6985ce7ef71 | -1.0919 | -53.4561 | 2024-12-03 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 276.1 |
| 42532b4d-ab03-3070-9238-f2f57fd46dba | -5.8195 | -46.4929 | 2024-12-03 00:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ad01c678-87af-3e83-bf75-5428051d85ad | -2.0271 | -53.9477 | 2024-12-03 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 9821be9f-a5c5-3116-9c4c-1a8da7793517 | -1.7544 | -52.6363 | 2024-12-03 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 75aadc00-fbd2-348c-a693-e0abebd85b00 | -5.118 | -43.2198 | 2024-12-03 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 6b8cfc2f-357d-3cfb-84eb-8fea19deb90a | -3.0945 | -53.3601 | 2024-12-03 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e5d9a534-0d00-3ca3-b179-1fd56bf132b5 | -2.8396 | -52.5941 | 2024-12-03 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2f2fd6a7-a6f3-3bc6-ac6f-30889984d0a7 | -2.8396 | -52.5736 | 2024-12-03 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 74246e5b-bdbe-318a-ba9f-7aba9707f850 | -1.0735 | -53.4764 | 2024-12-03 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2aa544b5-287c-3eff-881c-2522d6a4eb8e | -3.3421 | -51.2215 | 2024-12-03 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 67733bdb-68f8-38bd-bbb7-52f03cd66da5 | -1.7361 | -52.6366 | 2024-12-03 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 29d80921-ee3b-39cc-811e-7aa8fed25b08 | -1.7725 | -52.799 | 2024-12-03 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8ddcf5ba-a0d6-37d4-a775-68bf8a6e7d59 | -2.8012 | -53.0633 | 2024-12-03 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7110ebca-f598-38dc-9c68-522dcd051d02 | -1.3283 | -54.9964 | 2024-12-03 00:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 4f89ebfe-756a-3725-a19f-c82227e4042a | -2.8013 | -53.043 | 2024-12-03 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 0caa6fbd-731d-3435-b003-3e2162dff9cb | -5.801 | -46.4719 | 2024-12-03 00:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| aaf99b95-4a66-3da9-b392-f0e97cc84e0c | -3.0944 | -53.3804 | 2024-12-03 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| caced7a6-66c3-33c2-8484-e68cea685834 | -3.0761 | -53.3606 | 2024-12-03 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 5ca48e2f-c95d-3498-8d23-06e713e30e56 | -1.0919 | -53.4762 | 2024-12-03 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| aeb83161-6d28-3914-adf0-4cf17786ace9 | -5.0992 | -43.2211 | 2024-12-03 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 32bbbd78-85b8-3fbd-a7c0-010934743a18 | -1.7361 | -52.6162 | 2024-12-03 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| f97d6e73-205c-39ff-baa5-bd4439c12f0b | -3.2591 | -53.6186 | 2024-12-03 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5bcf4759-c41d-3eba-a901-857189530465 | -2.8212 | -52.5945 | 2024-12-03 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a38552e5-ee38-3aec-8fd0-e4657bb6b65e | -1.7541 | -52.7993 | 2024-12-03 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| bcc55d9d-cd6e-3486-b3ab-4196278d5de9 | -1.0735 | -53.4562 | 2024-12-03 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 182.3 |
| 459c51e7-ce2c-373a-a374-5ff388f8997b | -4.5403 | -42.9066 | 2024-12-03 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| bfeb04de-608d-3c12-9046-9f969ae03a64 | -3.2905 | -50.3257 | 2024-12-03 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 32599171-5373-35fd-ae7c-84166007fcea | -3.2775 | -53.6181 | 2024-12-03 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d1917b99-22b0-37c6-8f12-96a3ff1aaa54 | -3.076 | -53.3808 | 2024-12-03 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 8a4ede3c-0b1c-321f-9357-6ee2832d3972 | -4.5402 | -42.93 | 2024-12-03 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| b3364880-820c-3ffa-9fe9-ecc85084cff0 | -2.3459 | -45.7036 | 2024-12-03 00:40:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 142.3 |
| dff9ad90-1fe4-3cb6-845f-7377a56c459d | -5.1365 | -43.2419 | 2024-12-03 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c1b68b10-3a31-35a5-9df3-fdbd3568c047 | -3.0376 | -53.8664 | 2024-12-03 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 5aace007-9b37-3fa5-8441-648ded2e55fa | -3.2774 | -53.6383 | 2024-12-03 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 43caa223-12dc-3744-8b5a-5c5051ff65a4 | -3.0949 | -53.2385 | 2024-12-03 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0a7b0733-9b6b-36fa-83de-cb9d2060f41c | -4.1708 | -48.1842 | 2024-12-03 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| d2779a1d-fe88-3675-816e-b99928ab4e0d | -3.3422 | -51.2007 | 2024-12-03 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 97e9085a-acb9-3755-8c70-e5c2f79d5272 | -3.095 | -53.2183 | 2024-12-03 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 95b5a228-f488-3362-a4be-9dbf1dbaf9b5 | -5.8009 | -46.4941 | 2024-12-03 00:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 03925976-8d75-3751-896f-5bd33599d926 | -2.8197 | -53.0425 | 2024-12-03 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 95ccf8eb-e3bd-3b07-a6f5-11cc5828ce42 | -3.259 | -53.659 | 2024-12-03 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 328020fc-3a93-3637-a892-0cd583e8abc5 | -6.1229 | -43.9578 | 2024-12-03 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 6cf30975-7f78-3028-88f5-ca7ffa76aef0 | -1.0736 | -53.436 | 2024-12-03 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| fc53f829-c95f-33e8-8317-8fd1e48f4d01 | -3.0761 | -53.3606 | 2024-12-03 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| eae60fbe-3576-3e98-99f8-17e8efbd2b13 | -5.1365 | -43.2419 | 2024-12-03 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 037c41c2-b2b3-3f16-aa77-6ec59205c3d8 | -1.0919 | -53.4762 | 2024-12-03 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 3c73fdc4-1cb3-3e88-a923-8bbf930a433f | -3.2591 | -53.6186 | 2024-12-03 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 3f4b92d1-6dec-3324-81b7-88379385b29c | -1.0735 | -53.4562 | 2024-12-03 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 232.8 |
| b4240365-94af-3882-ab8a-8e7982762924 | -2.3396 | -53.8013 | 2024-12-03 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ee01b776-2700-3d76-a79c-14132e4a20e5 | -3.0944 | -53.3804 | 2024-12-03 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 34d5d40b-381d-3c83-a2a5-f68e229e9698 | -3.183 | -54.3448 | 2024-12-03 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e13d7651-b036-3fae-b5b8-4d23f09d6ca3 | -1.7541 | -52.7789 | 2024-12-03 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| aac641b9-7247-3635-939b-7136a9d13684 | -2.3645 | -45.7031 | 2024-12-03 00:50:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 50bee299-e7e4-38b2-910e-e08c731b9397 | -5.801 | -46.4719 | 2024-12-03 00:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| f4092c09-59f3-3fe5-a1be-13a85156ac53 | -2.8196 | -53.0629 | 2024-12-03 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f1d4b8b3-cf57-3fa1-a597-c6b9e956fb6b | -4.5402 | -42.93 | 2024-12-03 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 98308f8a-d863-3e93-831b-faa6979f96e2 | -4.1914 | -51.1914 | 2024-12-03 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 93d2faf5-aca6-3003-8a45-7b562706a07d | -5.1552 | -43.2406 | 2024-12-03 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 2dc8e6d3-49c7-34cd-b178-df6f3abc009d | -9.7355 | -36.4286 | 2024-12-03 00:50:00 | GOES-16 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 90.1 |
| 8c9ccebc-1e57-364e-ab64-24a5f24b926d | -1.736 | -52.657 | 2024-12-03 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b1d6c559-a8ac-33a9-94cd-1286cde4457e | -3.5497 | -50.1699 | 2024-12-03 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 86ec330f-2868-3f61-bf09-aa2cf4d3fec7 | -1.0735 | -53.4764 | 2024-12-03 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0e75cb3d-f9a4-3765-bdb4-0f80d2213ab7 | -2.8197 | -53.0425 | 2024-12-03 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 0844f514-fb37-3150-bb62-12519114e005 | -3.5682 | -50.1693 | 2024-12-03 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 60462113-2652-3374-b7aa-2e95cde94fa4 | -2.8212 | -52.5741 | 2024-12-03 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| caf31712-a5e9-3533-b5de-1aae05b631e5 | -2.8212 | -52.5945 | 2024-12-03 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 132e0b02-239c-3170-83af-1de4ab463059 | -4.1915 | -51.1706 | 2024-12-03 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 378de234-c464-3b8a-9fa9-7a75a719f983 | -3.1134 | -53.2178 | 2024-12-03 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2ff03051-1e92-3b72-909c-23d8017d7251 | -2.8013 | -53.043 | 2024-12-03 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |


[Clique aqui para ver as próximas entradas](README13.md)
