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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f88b53f-7ac4-3ae0-8155-dd2cbff8283e | -2.289 | -46.35816 | 2024-12-03 00:15:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| ad222ea8-532c-3f7c-acda-cc07d13d10d5 | -2.33518 | -45.56467 | 2024-12-03 00:15:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| e243c15f-affb-3503-ad56-e98daf0c3d98 | -2.85563 | -45.84177 | 2024-12-03 00:15:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| d6fb1492-aec3-3536-bd5f-f873eeaa81ae | -1.84729 | -46.00967 | 2024-12-03 00:15:00 | TERRA_M-M | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 77210fdf-46e9-3b12-b879-4cf6cda114fc | -2.32249 | -45.56639 | 2024-12-03 00:15:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 51302abd-eb6e-3336-b90e-a7f7d32edaf5 | -2.26818 | -45.46376 | 2024-12-03 00:15:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0f36f2ee-6d6f-3e68-bc23-fb4dabc4c0c8 | -2.66431 | -44.98641 | 2024-12-03 00:15:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 205.7 |
| 08f6ea52-4c21-32b2-af6a-7fda98c2fb23 | -2.96488 | -45.18274 | 2024-12-03 00:15:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 6bc23f08-a892-33c9-8cb8-4c0c3d629e45 | -1.80399 | -46.66087 | 2024-12-03 00:15:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 61cd4fca-1042-32c0-b6b1-d7fcd5024a97 | -2.4948 | -45.5873 | 2024-12-03 00:20:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 632e2cda-0b1c-31c2-96db-99641ed3f7b7 | -2.8013 | -53.043 | 2024-12-03 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 71cbcefb-b25c-3107-a971-01ce7fdde5c5 | -1.0735 | -53.4764 | 2024-12-03 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 8ff0d300-4505-302e-b153-619e1ab9d52e | -4.5589 | -42.9289 | 2024-12-03 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| d1808971-4f83-34f7-a783-dfa52d8db1f3 | -3.5496 | -50.191 | 2024-12-03 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 9b38e7a5-4544-364a-ae4b-e66894828759 | -3.272 | -50.3263 | 2024-12-03 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f2e4d907-618b-3b6e-bbf7-51b0b27f3bbe | -2.8212 | -52.5741 | 2024-12-03 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| b1136f93-0107-38fb-8151-4a4a6c468a81 | -1.7541 | -52.7993 | 2024-12-03 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 5db6daf9-dbc5-38ca-b61f-49c073c01352 | -1.0736 | -53.436 | 2024-12-03 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| e6050f91-7562-3f0f-a409-248debfa14ec | -4.1684 | -48.5937 | 2024-12-03 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 4d94b3fb-c0a6-38fb-8cb0-69e800cc51f9 | -6.1229 | -43.9578 | 2024-12-03 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 95e3226f-fb0f-36d4-9e24-a5a459100050 | -1.0919 | -53.4359 | 2024-12-03 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 45681df6-9e80-3c07-9403-4c7de48b5347 | -2.6644 | -44.9743 | 2024-12-03 00:20:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4b236ce1-b8ca-3ae2-a805-4ecd9e8f08b8 | -1.0735 | -53.4562 | 2024-12-03 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 180.4 |
| b4af596a-b716-3814-a9dd-d16f9ead7a4d | -1.0919 | -53.4561 | 2024-12-03 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 229.6 |
| 699f3dc3-440d-3b8d-8493-5592d019bef9 | -1.7361 | -52.6366 | 2024-12-03 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 3bc394b1-6cf6-3200-8fe7-d378a07eeac3 | -2.3396 | -53.8214 | 2024-12-03 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 1d9a8ead-800c-32c3-8b0f-a84a725769f0 | -3.5497 | -50.1699 | 2024-12-03 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| bbcbed71-6bc4-3390-85bd-ce0594d78dfa | -3.1831 | -54.3247 | 2024-12-03 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 551ab848-7fc7-33ab-a330-92a288837f11 | -12.7147 | -58.2231 | 2024-12-03 00:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| cad7fcd5-4aec-38ce-888d-32f6e58e0ff4 | -4.1915 | -51.1706 | 2024-12-03 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| bab5030a-53c4-3b70-bc84-69b79625513c | -3.259 | -53.659 | 2024-12-03 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| d5e9101b-0dd2-32b1-ae96-ea68b7c772a1 | -3.259 | -53.6388 | 2024-12-03 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| a3351d1d-2eb8-30b3-a959-d82750360ffb | -2.8197 | -53.0425 | 2024-12-03 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f7c56cb5-c69e-3f6d-b8dd-39e654d49123 | -2.8396 | -52.5736 | 2024-12-03 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 149e6547-84a6-3fb6-a098-153dd8d21d87 | -3.2591 | -53.6186 | 2024-12-03 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 30471463-69e9-366e-9669-928b67f9a355 | -3.2905 | -50.3257 | 2024-12-03 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d3a1b8d8-48ec-30f4-b6ac-5580410137e4 | -2.8012 | -53.0633 | 2024-12-03 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 70e6880d-4b57-39bd-b0e3-1c72bb058da7 | -4.1708 | -48.1842 | 2024-12-03 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| ec2397ba-df55-3de5-bfb3-c4c04b560fb0 | -2.8212 | -52.5945 | 2024-12-03 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0601c359-7431-3153-be90-23369ee9a240 | -3.2774 | -53.6383 | 2024-12-03 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| da3e9ef8-af7d-3847-9b9e-ccd6aa8bb690 | -1.0919 | -53.4762 | 2024-12-03 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| e34bdef6-e103-31c0-bbfd-346e67940d99 | -12.7149 | -58.2032 | 2024-12-03 00:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 9e1cdd5e-45e9-3c48-a83b-b315fd1a42ff | -3.3421 | -51.2215 | 2024-12-03 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 6de03f5b-dffe-310c-8897-5ac97e28eb29 | -1.7541 | -52.7789 | 2024-12-03 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 78672cee-c3b0-3331-a8a3-199eed915c5d | -2.3459 | -45.7036 | 2024-12-03 00:20:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 261.2 |
| 2c531752-abb0-308b-8ab9-59afe6af09a0 | -4.5591 | -42.9054 | 2024-12-03 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 62046ae2-81ad-3ab5-9183-eb9f430a333c | -2.8396 | -52.5941 | 2024-12-03 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 9ca6a6ad-735d-3d5a-87f8-35ddac2a1e15 | -1.898 | -46.6249 | 2024-12-03 00:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| e7ca964f-d978-3adc-a26a-8ca4a4d81075 | -2.3644 | -45.7254 | 2024-12-03 00:20:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 2f18aacc-a470-36fb-b31f-76e620487e12 | -2.3458 | -45.7259 | 2024-12-03 00:20:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f8628114-f979-36d5-b1e8-e8e6160d189a | -12.6957 | -58.2247 | 2024-12-03 00:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 302f9483-4537-30f9-8741-8793786b4a6f | -2.3396 | -53.8013 | 2024-12-03 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| ca689a50-baf1-3a2e-9832-1bc73c772830 | -4.7484 | -45.1271 | 2024-12-03 00:20:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f2b7d3fa-206d-3515-abbd-c9ab55acf7ff | -4.7485 | -45.1044 | 2024-12-03 00:20:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 1b34b6f3-4d6f-38e3-ae78-7dcfd3d8d70d | -3.2406 | -53.6595 | 2024-12-03 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8153b516-76d7-3fef-b80a-196de5375667 | -3.0761 | -53.3606 | 2024-12-03 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 0227ac41-50cd-3a2f-91ff-41a6711bb190 | -3.6096 | -45.5908 | 2024-12-03 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| dc96e1ed-2685-33de-b385-d2486c3251f5 | -9.374 | -57.5553 | 2024-12-03 00:20:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a37b8694-b739-305f-a626-e50361108f7a | -1.736 | -52.657 | 2024-12-03 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| ae56808a-ac69-39c6-aa84-d12eaf494aee | -3.0945 | -53.3601 | 2024-12-03 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| b911eecc-142d-3fa8-94b6-e2cb7bf518b0 | -2.3645 | -45.7031 | 2024-12-03 00:20:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 211.8 |
| 51db80bc-98f6-372f-80d9-a1cb397a86ac | -1.7361 | -52.6162 | 2024-12-03 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 81d460f8-ad64-37e3-8665-126b87716e0b | -4.5402 | -42.93 | 2024-12-03 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 151.6 |
| bde3f270-1dfb-3897-b98a-3ee1cd75c384 | -12.6959 | -58.2048 | 2024-12-03 00:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 3fd8ca8f-f0f1-35e5-9070-3008d1447bec | -3.7084 | -51.8301 | 2024-12-03 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| e2962a32-732f-3a3a-9699-fa63585fae8c | -2.2111 | -53.7835 | 2024-12-03 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9ba73e82-3c7c-3637-8bba-c16c68142712 | -9.6537 | -62.4344 | 2024-12-03 00:20:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 061cc861-9c20-37ce-84cf-93a2bdeb6192 | -2.8196 | -53.0629 | 2024-12-03 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 3753f7be-37d5-3ae6-b8db-09eb454fda56 | -4.1706 | -48.2058 | 2024-12-03 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 7171a23b-5620-340c-8326-e0ac6dd2c360 | -4.1914 | -51.1914 | 2024-12-03 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| c6329a04-a326-389a-955c-fa1101fe3766 | -1.7544 | -52.6363 | 2024-12-03 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4eac4a9e-df82-3c6d-a674-e476f64e6eb7 | -3.3422 | -51.2007 | 2024-12-03 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| e87d5573-2582-3cad-9108-92aa0ca76463 | -4.5403 | -42.9066 | 2024-12-03 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 5b7c382a-5d31-3a27-9851-c44adc11c8ec | -3.183 | -54.3448 | 2024-12-03 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 624adef8-9211-32b1-841b-333a89fa7da5 | -3.0944 | -53.3804 | 2024-12-03 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 5f043e6f-bd77-3069-a5ba-f4b4bfdd5f35 | -3.076 | -53.3808 | 2024-12-03 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 52fa9f8d-94dc-33da-ba62-23871e9ae3cb | -3.2775 | -53.6181 | 2024-12-03 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 5a05d33a-395c-3f8f-bda9-3f04f37d6eeb | -3.1134 | -53.2178 | 2024-12-03 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 40222e88-70f5-30f6-8d6e-53eaeab4d9f0 | -3.1831 | -54.3247 | 2024-12-03 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f38e224d-d1db-3a98-a148-c82d5bff1d24 | -2.2111 | -53.7835 | 2024-12-03 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3b77c303-6714-3f31-9073-fbb14ce997c1 | -2.3458 | -45.7259 | 2024-12-03 00:30:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 0e3f635c-ac9d-392b-aeac-2578c3f27870 | -1.0735 | -53.4764 | 2024-12-03 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 06c29f35-5326-3288-9e09-279a6ed604c1 | -4.5402 | -42.93 | 2024-12-03 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 514b8fc7-a539-34eb-a96e-fd730424bf10 | -3.0944 | -53.3804 | 2024-12-03 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 6d5cf896-a643-3fba-99c5-da2d2cfff2d1 | -1.0735 | -53.4562 | 2024-12-03 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 250.9 |
| 3da597d4-16ea-33a3-af14-573e7ab46d5c | -2.4948 | -45.5873 | 2024-12-03 00:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| a69b3a57-2942-3d91-992c-47fe97efa80f | -3.183 | -54.3448 | 2024-12-03 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0ef347ff-43cd-39ca-a4c7-658ad83ad356 | -2.3396 | -53.8013 | 2024-12-03 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 23bb161f-cc62-3947-b8fe-bbdc5abcdc33 | -2.8197 | -53.0425 | 2024-12-03 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 6af46136-f48e-31c9-b993-c4e63e068ad7 | -1.0919 | -53.4561 | 2024-12-03 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 241.2 |
| 92a65f1b-8948-306a-90e8-e548cec430f2 | -2.0455 | -53.9474 | 2024-12-03 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 70840d77-8756-39de-9751-4d10d450be05 | -2.8013 | -53.043 | 2024-12-03 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 8da0ce9a-47e3-3a22-989f-3d55324373f7 | -3.2591 | -53.6186 | 2024-12-03 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| f19357b0-e6f5-31c2-b6bc-246d2b4cd997 | -1.0919 | -53.4762 | 2024-12-03 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9eb1542c-b8b8-3569-8ec1-1d614ffd1ff6 | -5.1181 | -43.1964 | 2024-12-03 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 27401c71-99cb-35ea-9808-05031bca11eb | -3.076 | -53.3808 | 2024-12-03 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| b9257ce9-7e25-3acc-999b-30d2e697c3eb | -3.259 | -53.6388 | 2024-12-03 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 9718d08b-af2e-3aa5-8abc-7f235ac8d8c2 | -1.0919 | -53.4359 | 2024-12-03 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 72ec696c-f6f7-3249-a964-844cc8aa2cd3 | -5.801 | -46.4719 | 2024-12-03 00:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| a1a3f858-38a9-3348-96ab-8c5d24376e9e | -2.8212 | -52.5945 | 2024-12-03 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |


[Clique aqui para ver as próximas entradas](README5.md)
