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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6aa9d2da-851b-3fc2-baec-bf8d85938f49 | -4.6049 | -44.3161 | 2024-10-30 02:05:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 3b05c823-2673-398e-8fab-abbd8be6d480 | -5.2308 | -47.9349 | 2024-10-30 02:05:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| fdb51cab-be51-3aae-ba23-963f03d79f59 | -5.2306 | -47.9566 | 2024-10-30 02:05:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| b72efe04-e5c6-31a9-951f-088aab5993f6 | -5.212 | -47.9577 | 2024-10-30 02:05:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8d50bffe-806e-3ad0-883f-26770cd1772d | -6.0933 | -47.203 | 2024-10-30 02:05:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 94e4901d-abc9-3cfa-b6f5-555a82b29414 | -6.0746 | -47.2043 | 2024-10-30 02:05:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 5e08ce88-7739-3d83-87cb-7ab07529f4ae | -5.9788 | -45.3621 | 2024-10-30 02:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 5c6e850d-2e60-3393-88ed-87e15d636c10 | -6.8592 | -59.0511 | 2024-10-30 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| befe05af-5438-34c1-9d43-2de87da68753 | -6.8408 | -59.0519 | 2024-10-30 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d3825c9f-6bc8-3cc1-9d04-835f32967f18 | -19.61632 | -56.70845 | 2024-10-30 02:06:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 9c9cbdf7-5da9-31d5-9631-f055f0761472 | -19.60293 | -56.71129 | 2024-10-30 02:06:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 14ae93a8-dcd0-3b5c-aeaf-8b9ac2ecbfd9 | -19.58195 | -56.72222 | 2024-10-30 02:06:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 09613861-3f82-35d7-a586-942dc269ab18 | -19.57614 | -56.71694 | 2024-10-30 02:06:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.9 |
| db086ec5-76f0-3ca1-9796-ccb6317ae64d | -19.50234 | -56.59247 | 2024-10-30 02:06:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.4 |
| 7f6e950a-267d-3b78-b3ca-440034ea11fd | -18.25246 | -55.99522 | 2024-10-30 02:06:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.9 |
| 44057572-46b2-32e4-9b48-eabb1c5038f1 | -10.3437 | -49.6321 | 2024-10-30 02:06:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 07085c3d-9a12-3a7f-95e5-88c376547585 | -10.3434 | -49.6536 | 2024-10-30 02:06:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 150.3 |
| c72f3c2b-c787-3307-8b2e-e405f5198094 | -10.3245 | -49.6556 | 2024-10-30 02:06:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 664418d3-10ae-3e99-8f86-ef3ddf0fef25 | -10.7171 | -44.9391 | 2024-10-30 02:06:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| a9b200d5-c49c-32e4-b3fe-835a4afafc45 | -10.7175 | -44.916 | 2024-10-30 02:06:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 727fded9-3975-3c41-ba3a-f700f63f48c5 | -19.5862 | -56.7136 | 2024-10-30 02:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.3 |
| deda79f6-ab69-321a-8cd6-1d282d90e397 | -19.5866 | -56.6926 | 2024-10-30 02:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 6f200f01-04a6-39bb-a47e-b77c0d905b6f | -19.6063 | -56.7108 | 2024-10-30 02:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 153.5 |
| 33b1a5bd-d01d-3d62-9329-5040079bd8fa | -19.6067 | -56.6898 | 2024-10-30 02:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| b8792515-66f8-361d-a0f3-83045181b26d | -19.6264 | -56.7079 | 2024-10-30 02:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 115.6 |
| b21d6ae9-c5a8-3a98-86fa-726b538c55de | -9.49444 | -64.44518 | 2024-10-30 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3cd2eb88-9b6c-34c2-bfa4-27cc489f7c73 | -10.69096 | -64.99996 | 2024-10-30 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 7fc6216a-192b-3d87-a6b0-6ac702d147e5 | -11.90922 | -63.67392 | 2024-10-30 02:09:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f49eecc4-b51b-3ba1-93a5-6421219dd797 | -11.9818 | -64.04058 | 2024-10-30 02:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2289a7f2-afab-3441-9d0c-c852cd69ee6d | -12.02788 | -64.04755 | 2024-10-30 02:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 088c014c-35e6-3c21-9f54-41636de76b85 | -12.33264 | -63.98186 | 2024-10-30 02:09:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2a628532-d80a-3a43-b7aa-8ee5dd5cee0f | -8.85662 | -64.23564 | 2024-10-30 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e9f3014c-610f-3c50-8df7-8abde22c5a0d | -8.85811 | -64.24584 | 2024-10-30 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 67dd9954-67ca-3435-ae95-5f148abaaee9 | -9.01213 | -64.3655 | 2024-10-30 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cfee8521-4544-3b76-bf59-22548e59ed67 | -9.37782 | -64.45497 | 2024-10-30 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c5d46342-52ed-36c3-9528-f3e75ee293b3 | -9.493 | -64.43536 | 2024-10-30 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d6438b8-0ce6-39b4-b2b4-09a97f735c9b | -9.55601 | -63.14296 | 2024-10-30 02:09:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 48e86b97-e0d1-3b35-9b3e-e171ba038e0e | -9.5543 | -63.13132 | 2024-10-30 02:09:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3cb18c31-3240-30a7-8011-4c2b7c69e110 | -9.5412 | -66.64923 | 2024-10-30 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| efe98280-e66e-3e99-ab77-2f7844a4871e | -9.54078 | -64.43822 | 2024-10-30 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 19c0c4c3-edbe-3f3a-a880-f2e16fa55a1e | -9.51301 | -65.59729 | 2024-10-30 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 52834e59-9565-3cf3-bb28-ace6f69d8a46 | -0.76991 | -62.89479 | 2024-10-30 02:11:00 | TERRA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ec2c5caf-65ae-3df0-8ab8-b21ae29a70bd | -2.3906 | -48.955 | 2024-10-30 02:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 48edca8f-f19b-3aba-8312-3a026a88fe5e | -2.3906 | -48.9337 | 2024-10-30 02:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 58ced8e8-7f66-34ff-b7b9-41f3bd3c1f5e | -2.833 | -49.2413 | 2024-10-30 02:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 2d202fc0-d07a-3ca4-ad07-7cdad8da5774 | -2.8331 | -49.22 | 2024-10-30 02:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| b8687007-9235-39d2-b1d2-8331cd93023f | -2.8515 | -49.2408 | 2024-10-30 02:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 2855f4cd-6752-3746-8adb-3e914edac919 | -3.0734 | -54.167 | 2024-10-30 02:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 3bfa817b-6ab9-31a2-bc56-d1228460b6a4 | -3.1094 | -45.2293 | 2024-10-30 02:15:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9039ec91-4915-3f37-b69a-bca25e3caef8 | -3.1601 | -50.6021 | 2024-10-30 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| c34f0fb4-8f2a-396b-8a50-04fdeedc3f28 | -3.1602 | -50.5812 | 2024-10-30 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| fbfaef8b-74a1-320b-a724-419fef4de967 | -3.1786 | -50.6016 | 2024-10-30 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| d4e5bfb8-fd36-3b32-841a-8302b148bfd9 | -3.1787 | -50.5807 | 2024-10-30 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 5f9b3da9-e45d-3194-8432-df6988b97292 | -3.234 | -50.5789 | 2024-10-30 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 3ae02e7e-0679-3837-a300-aa5dda8a0006 | -3.2534 | -50.3689 | 2024-10-30 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e0d67014-54f1-3ecd-b9f2-a48196bfa9b8 | -3.2535 | -50.3479 | 2024-10-30 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 6e6ba9d0-d285-3632-aa49-0b41efbfab04 | -3.2719 | -50.3473 | 2024-10-30 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 60b75564-afc6-38ba-bf02-053faf7eca9d | -3.5631 | -47.3847 | 2024-10-30 02:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 224.0 |
| c6854513-4425-3a0b-9f87-419141b6f226 | -3.5632 | -47.3629 | 2024-10-30 02:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| c97d644d-989f-3492-9ee4-d5b4c450ab91 | -3.5817 | -47.384 | 2024-10-30 02:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 280.1 |
| 7c6813da-71da-3937-8b8b-16313b1f1e59 | -3.5818 | -47.3621 | 2024-10-30 02:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| c0d1090e-d50c-3151-937a-8e7a75deafca | -3.8037 | -51.1644 | 2024-10-30 02:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| fe0e04f0-d2d4-3fbc-8643-ef7c4830de2f | -3.9326 | -41.4957 | 2024-10-30 02:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 964c882f-d918-3b82-9600-78d79a109191 | -3.8845 | -49.7568 | 2024-10-30 02:15:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| ddf57d32-f519-38fb-8566-f81dba674c53 | -3.8846 | -49.7356 | 2024-10-30 02:15:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 61659001-aa7b-353a-b4d0-8ba0597bb330 | -4.0681 | -50.024 | 2024-10-30 02:15:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| bb484d15-8ea3-3433-ab42-ad0a3c461f6f | -4.0682 | -50.0029 | 2024-10-30 02:15:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 5845f8e6-2cba-34da-997c-23e6bdcbb9fe | -4.2563 | -43.4368 | 2024-10-30 02:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 446469fd-03b0-32a1-aa33-aa1d3595b60a | -4.2748 | -43.4589 | 2024-10-30 02:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e07348d2-8d81-30de-a556-c2a2f2013e12 | -4.2749 | -43.4357 | 2024-10-30 02:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| fcad6194-b277-3279-899e-385ea3120c7c | -4.2496 | -50.6677 | 2024-10-30 02:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 17bdd62c-df3b-369e-b959-a3d0bcaa6667 | -4.2681 | -50.6669 | 2024-10-30 02:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1f73ba22-3175-38c3-b3be-47bf8da63bd7 | -4.6049 | -44.3161 | 2024-10-30 02:15:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 280.9 |
| 2e675205-293d-3fe0-a98b-b18b84179a86 | -4.5862 | -44.3172 | 2024-10-30 02:15:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 45d0d0a9-4187-3d40-877c-b15c56231c05 | -4.5864 | -44.2943 | 2024-10-30 02:15:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| dbb8d3c8-27b5-34d1-8019-27104ccbd4db | -4.6051 | -44.2932 | 2024-10-30 02:15:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 400.4 |
| 0e93f6da-0d91-3eb1-839b-0b5bf09f8b88 | -5.2308 | -47.9349 | 2024-10-30 02:15:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 219b0456-de2c-38d5-b7c8-32d782c272b5 | -5.2306 | -47.9566 | 2024-10-30 02:15:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| f6259df0-ec24-36d6-9895-2018574b9011 | -5.212 | -47.9577 | 2024-10-30 02:15:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 83af7511-355a-3028-9b6e-de736b477174 | -5.9788 | -45.3621 | 2024-10-30 02:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 019b0e1b-4dc3-3cd6-8606-5e16ab33b4ce | -6.8593 | -59.0318 | 2024-10-30 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 72ec4ce7-1664-3293-9085-45e35ca158a9 | -6.8592 | -59.0511 | 2024-10-30 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 6894288b-6321-3d8c-b6b1-80bb28863fb2 | -6.8408 | -59.0519 | 2024-10-30 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a0d30b01-d6f2-37c8-9f1a-dbf496f266a5 | -10.3437 | -49.6321 | 2024-10-30 02:16:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 1852cf9a-39f9-32ee-bff9-02a7a1603f40 | -10.3434 | -49.6536 | 2024-10-30 02:16:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 6b4e5a65-02dd-342e-b60d-ee46c10a1982 | -10.3245 | -49.6556 | 2024-10-30 02:16:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 36becacf-00ff-3880-ada5-aadbc5f906b7 | -10.7175 | -44.916 | 2024-10-30 02:16:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| f4bdc544-31d1-3cb0-bf01-1b6804d83781 | -12.899 | -45.0549 | 2024-10-30 02:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| dbb1941b-aa38-347c-a4df-55c1943c2918 | -19.5862 | -56.7136 | 2024-10-30 02:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 86036e33-c211-355f-b8d4-03c761bfc0c8 | -19.6063 | -56.7108 | 2024-10-30 02:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 9e34c3fc-9b93-32b8-b81d-e843d399e11d | -19.6067 | -56.6898 | 2024-10-30 02:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 12988ee6-8b73-3096-9282-b9c5c3415746 | -19.6264 | -56.7079 | 2024-10-30 02:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 7fe32a29-1d14-388c-814b-a98cc68bd44b | -19.6268 | -56.6869 | 2024-10-30 02:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 6e2065dd-b675-3c6d-b37f-42a71df80c71 | -2.833 | -49.2413 | 2024-10-30 02:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 7f787a03-3b58-3324-b7cf-f1ae1a26f583 | -2.8331 | -49.22 | 2024-10-30 02:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 8b9b670a-aeb6-3292-951c-aba266a029f1 | -2.8515 | -49.2408 | 2024-10-30 02:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 1b4b51ba-cc9c-32fe-b870-2e42b120ba74 | -3.2719 | -50.3473 | 2024-10-30 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 6aba702d-be8e-3be9-9aa3-6ffd31893594 | -3.16 | -50.6231 | 2024-10-30 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| d7958bbf-253f-348f-b6f6-0a2f56067a85 | -3.1601 | -50.6021 | 2024-10-30 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| df10dcde-0318-37d8-9547-1d6e7f8fe4ec | -3.1602 | -50.5812 | 2024-10-30 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |


[Clique aqui para ver as próximas entradas](README24.md)
