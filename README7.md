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
| 3e681b07-c6f2-3c58-857d-e77b7898c350 | -3.0325 | -45.7931 | 2024-11-11 00:50:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e2296469-fd03-38ac-afed-1ee17d6aa731 | -3.5322 | -49.9599 | 2024-11-11 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 14568287-2393-3502-887c-a9c5f1f21cd7 | -3.0295 | -50.9815 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 9e586216-9feb-34d1-9169-133ae387db4f | -3.2427 | -53.0722 | 2024-11-11 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| cdea2618-b2a9-384d-aa1a-3a09fc0a6fe2 | -3.7149 | -54.6504 | 2024-11-11 00:50:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 5e6815fc-4dfa-3a6f-9e75-853399501f4b | -3.2352 | -50.3065 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f8b650ea-9b0e-3847-8639-9df9088394cb | -2.8323 | -49.4325 | 2024-11-11 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 3cd35fe6-e351-31d3-a05b-8f636052cef1 | -2.1891 | -48.36 | 2024-11-11 00:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b94dd037-1d51-3a7d-81d4-6f35c997958e | -3.0138 | -45.8161 | 2024-11-11 00:50:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 170.1 |
| 524fe80e-3b87-3ec3-83cd-200a30bdbe64 | -3.2352 | -50.2855 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 0e74df82-2796-3e93-97de-922e8c8657c4 | -3.2168 | -50.2861 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7963e0cd-75c6-37a6-ad33-f66655a6f04b | -17.5889 | -57.43 | 2024-11-11 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| f0d0a0f6-d5ff-32c1-aba4-b05cde0bf420 | -4.11 | -49.1102 | 2024-11-11 00:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 311b6aa7-10d4-308a-a6c3-5dc9079ea747 | -3.2353 | -50.2645 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| fa236662-c7d1-3673-95aa-858cf6e78839 | -3.2244 | -53.0524 | 2024-11-11 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 43e7b344-2156-3b8a-8cbc-5d167e0d63d2 | -17.2933 | -57.4857 | 2024-11-11 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 155.2 |
| 0886697a-3215-31f4-ab17-47391b7fb096 | -3.5346 | -45.7061 | 2024-11-11 00:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 15704700-c4cd-30b6-8439-6183a106514f | -3.0323 | -45.8377 | 2024-11-11 00:50:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 65272495-c03e-32b8-9788-99732421eed8 | -4.0294 | -46.9484 | 2024-11-11 00:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1a49d360-9560-332e-804d-483912c1914c | -5.8216 | -44.1196 | 2024-11-11 00:50:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3f979245-2f83-3b05-8c30-4deb28d9da92 | -3.051 | -45.8147 | 2024-11-11 00:50:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| b8aafe27-b314-3b83-9cce-2ed97240cb6c | -4.6835 | -46.4074 | 2024-11-11 00:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a8ec95df-0ca4-333d-879f-4e2fdbf3f4fe | -5.9788 | -45.3621 | 2024-11-11 00:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 24937137-e65a-364c-bdb5-e8cd6e2e3bf8 | -17.6086 | -57.4276 | 2024-11-11 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| e9863619-f118-3a2d-a78a-94f80d588d87 | -1.5164 | -52.1491 | 2024-11-11 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ee528ead-d944-3953-81f6-9f67115bd140 | -3.1641 | -54.4854 | 2024-11-11 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 387f3be9-74ea-3e52-ad6b-f41b0a89dca6 | -3.6789 | -50.2074 | 2024-11-11 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 67b5d4cd-75d4-331d-ae69-fbc65d1c6a84 | -2.2075 | -48.3811 | 2024-11-11 00:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 78b35ca3-32c9-33c2-8708-fb2a039e1b70 | -2.2504 | -46.5282 | 2024-11-11 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 3263b8c7-6b88-389a-a633-aaf7d415b6e4 | -3.1097 | -54.2865 | 2024-11-11 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 32745b3b-fb74-30ba-b420-2d99da5feb79 | -3.0137 | -45.8384 | 2024-11-11 00:50:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| d6e0c930-bfe0-3d87-8c1d-217e0a7c5c5f | -3.1458 | -54.4659 | 2024-11-11 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| f566e11e-43a4-3cf1-891f-7ff2a3d2d218 | -2.2504 | -46.5061 | 2024-11-11 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| a642c336-3b3b-3046-963c-f89f4f2de66f | -3.5137 | -49.9606 | 2024-11-11 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b739a271-f5d4-33d7-9e7c-b2b582bcfb77 | -3.2536 | -50.3059 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| a68b14c4-559b-3391-9541-ac161bef3401 | -4.1286 | -49.088 | 2024-11-11 00:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 57c11eda-577d-3437-bb08-ea16c7d2c8c4 | -3.0844 | -51.0839 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 6639bf47-eaf2-334c-b03b-1afe9e2fbfd8 | -3.1423 | -50.4352 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 9bb5a8ab-75d3-3a08-bcb0-ba608d0c0f84 | -3.6217 | -50.587 | 2024-11-11 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 130a41d6-c7ce-33c2-b78a-f22bf8b46b7f | -3.0214 | -53.2404 | 2024-11-11 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| f6a442df-2a3c-3327-88eb-2adb1cacd9ad | -17.313 | -57.4834 | 2024-11-11 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| f400d545-1bc6-3672-b9ae-d1a63245b670 | -3.0296 | -50.9607 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 81aec64d-9308-35a0-be5f-191979b466e1 | -3.6604 | -50.2081 | 2024-11-11 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2fe69615-59a5-3d44-ab10-d30764bf536c | -3.0845 | -51.0631 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4481d108-ebbe-3cdc-8a4e-ec401f762c39 | -3.0111 | -50.982 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 63933602-3624-3cfe-baf8-0aac117a670e | -3.1983 | -50.2867 | 2024-11-11 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 343310d0-7e60-37d9-9f66-8a7a50948b94 | -3.1458 | -54.4859 | 2024-11-11 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| d8124455-3bb3-3acb-bace-b01028c873a0 | -3.6965 | -54.651 | 2024-11-11 00:50:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5d71b555-4c8b-3560-a82d-542b148d1e42 | -2.8508 | -49.432 | 2024-11-11 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 37f33b7c-ac01-346c-9d04-3f6332aa986b | -3.6859 | -45.2502 | 2024-11-11 00:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e683264d-6a80-3e29-bda9-94e856d47bb7 | -2.9792 | -45.2567 | 2024-11-11 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 168c6040-57e5-3227-bf3d-f2de3db68ecf | -2.8508 | -49.4108 | 2024-11-11 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a1c7a3f9-43bb-38ae-82ba-1bfd6708b8a4 | -2.2578 | -53.736301 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0675866-a747-3f22-b9ec-f561f771e7d3 | -2.6948 | -49.843899 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 500f349c-3617-34f5-b83b-5360ec7b60bb | -2.3073 | -50.6679 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3efc200c-7fde-3420-94b9-b76088b9d5ba | -2.425 | -53.882198 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14593cd8-41a4-3f31-a727-a2ce907b57dd | -17.629601 | -57.5313 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cbcecfc9-63a9-3797-926e-05556c854da0 | -1.4621 | -51.4785 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d795e1de-23b0-3506-bd83-8ab23f908fa4 | -2.4664 | -53.973301 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4024478a-fdc9-30cd-8d2c-0fac03c554bc | -2.4311 | -48.7953 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e90f9fb9-1c81-3b30-a6ff-a7b905756d36 | -2.741 | -49.331001 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02912188-edd1-33fc-8bd4-c2a67a97f533 | -2.6678 | -49.282001 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73d6ae20-a3f3-3008-9791-0e46b0022029 | -3.3451 | -51.6814 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5511439c-65b6-388c-8f7f-0abf54614d54 | -3.0234 | -53.251301 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39296a8e-d872-3089-97f9-0491be056c7b | -3.4269 | -54.528599 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dede3592-0416-3962-ab71-1582d96604f7 | -1.1719 | -53.901901 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 859c835b-978b-3663-a1e4-8447b2e6d5ac | -3.184 | -54.320301 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 590257e4-009e-3d58-94fa-a02dbe831d10 | -4.0668 | -43.954601 | 2024-11-11 00:51:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 252e228f-60a9-39eb-9eb5-1c4af6d58c41 | -1.1773 | -52.080101 | 2024-11-11 00:51:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 278bd7a0-9c3f-3600-9360-3d3dcbabbba1 | -4.0997 | -49.0956 | 2024-11-11 00:51:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79370810-4419-3d07-acf9-7e2263a0a044 | -3.2194 | -50.2836 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c5ca761-1460-3bd6-9cd7-065b06748591 | -23.9216 | -54.0383 | 2024-11-11 00:51:00 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b509070-66f4-3df1-a58c-3467a9403f84 | -2.4147 | -53.656101 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16691abb-2b51-3a6e-a379-39cb6d9ab376 | -1.1966 | -53.694302 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b021ee2e-e60d-370a-9be3-0a1f57e7505c | -3.0199 | -50.984699 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b856d277-73cd-382f-90f1-ce9a22aeb676 | -2.9888 | -45.247501 | 2024-11-11 00:51:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58d85855-476b-3514-bcfc-33283373fc94 | -17.6033 | -57.495899 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 37dd2bf3-dc2e-3d12-ad65-28da59b87b1f | -1.4842 | -51.754101 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd71f146-3f5e-3e31-8246-05e38eba3c04 | -2.9104 | -49.349602 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1186cc9-97f9-384f-8a77-aa88c4c4fced | -3.0732 | -49.2066 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d6ebc1e-3302-3889-9265-1a8a26f7cdb0 | -3.5138 | -54.6852 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cc62f72-ebcc-3d8b-b5cf-a8b21f7e1178 | -2.9225 | -49.5798 | 2024-11-11 00:51:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58871f80-49c4-3d72-af8e-68a55af599e0 | -2.9509 | -52.572498 | 2024-11-11 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ba901e0-144b-33b3-a3c7-6f4d0ed37bc8 | -3.7599 | -49.5872 | 2024-11-11 00:51:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9e36bd2-28f4-342e-bc7e-10b69267a636 | -3.3891 | -50.124802 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 355704ba-16b0-381b-babb-1c968c16c191 | -2.6907 | -46.817699 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e28223a6-dc77-3c8d-ab73-3bd94b9bfc04 | -2.9147 | -49.501801 | 2024-11-11 00:51:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55f31c3a-9426-3adf-ba85-c464741a1c66 | -2.7294 | -51.740501 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efa58743-458d-3ffe-831d-1eab1b30687d | -2.19 | -53.258801 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 165450f1-f706-3f28-be2b-d2e881116196 | -2.913 | -49.494202 | 2024-11-11 00:51:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27f353b5-db93-3856-9e9c-0bbaa23cdf82 | -3.0104 | -53.2393 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f27f00d-8469-33a1-bf16-d836f897b7b4 | -1.5153 | -52.204601 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab7b2856-d7f2-3f12-805b-5186d86d8ff8 | -3.6244 | -50.6078 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 497fe7bb-3987-31cb-adf2-55d47616d12b | -2.2332 | -53.673801 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a414146-7412-3b30-b730-029d058fecf0 | -15.3135 | -56.511501 | 2024-11-11 00:51:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 929686ec-4685-3347-ab5a-bd8ceba7d6f3 | -2.4911 | -53.991001 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f276fc17-8354-3fae-b38b-f02f377769ad | -2.7624 | -49.334301 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bec83eec-688c-3d49-b3e7-88c413bd317d | -3.0482 | -49.5434 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27bea334-2696-3635-8d3c-d9377fbb5377 | -2.7616 | -49.375198 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 658040bd-6cec-372d-b707-fed4bf2b235a | -2.1992 | -48.374401 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
