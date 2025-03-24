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
| dae206f8-10ef-3cba-b8c0-52af87b5cd68 | 4.7001 | -60.9026 | 2025-03-24 00:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a5686200-298f-3ef5-9a27-efefcb0edd51 | -12.09922 | -43.86859 | 2025-03-24 00:03:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5a489654-be53-3679-93ac-992ac1617c9d | -15.51662 | -42.6059 | 2025-03-24 00:03:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 80833641-6e4b-3185-8207-455b6ffd4525 | -12.10693 | -43.85984 | 2025-03-24 00:03:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bd5ff58a-b4c3-34c8-85f6-a03ca5d08c06 | -2.94975 | -39.90575 | 2025-03-24 00:05:00 | TERRA_M-M | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 60fb202e-ecd2-35e9-988e-57807ca92d9e | -6.84744 | -34.93357 | 2025-03-24 00:05:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 5ed8855c-055a-31f0-9180-05a50606b27d | 4.7001 | -60.9026 | 2025-03-24 00:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 7fc71ce3-1d35-3d7d-9626-2470514b68be | 4.6818 | -60.903 | 2025-03-24 00:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 7ae5b88d-d514-357b-ba6a-e3bd59ad0b4d | 4.0575 | -61.5605 | 2025-03-24 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e8d554aa-c6bf-395d-a973-88a1420bba9e | 4.0758 | -61.5602 | 2025-03-24 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 948f67f7-e5ad-36f8-b9cf-a8865e706658 | 4.7001 | -60.9026 | 2025-03-24 00:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f9f75810-edd8-3ca3-ad99-2b85bfde0111 | 4.094 | -61.5598 | 2025-03-24 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 105.3 |
| e30713ad-470d-3868-a782-09a794845088 | 4.0757 | -61.579 | 2025-03-24 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 92.8 |
| b78940b9-5043-3800-8275-36f899ebbe5c | 4.0941 | -61.5409 | 2025-03-24 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0ede8914-7a31-3c68-b254-e16a72799225 | 4.6818 | -60.903 | 2025-03-24 00:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 63bc86a3-79b1-3b2d-b897-28e4d06d1db9 | 4.0758 | -61.5602 | 2025-03-24 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 9deaf208-e174-3389-81b9-473c9eb0d61f | 4.7001 | -60.9026 | 2025-03-24 00:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8b4c84b5-3692-3176-ad46-de97485d1ed7 | 4.094 | -61.5598 | 2025-03-24 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 796b0a18-8fcf-3d9b-8028-a7f6e136dd2c | 4.0575 | -61.5605 | 2025-03-24 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 5e1550ad-6da7-3cd8-ad1c-cb041ebccf5d | 4.6818 | -60.903 | 2025-03-24 00:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 95b0846b-04f5-3e3e-93b7-9fa3e6f375dd | 4.0941 | -61.5409 | 2025-03-24 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c319a97c-e42c-3016-8f41-83d3e1ebee62 | 4.0757 | -61.579 | 2025-03-24 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 141fe9ac-7fd4-350c-8fbc-28e9e1231732 | 4.0757 | -61.579 | 2025-03-24 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 18ca1f69-ec53-3138-a1ec-0f4902c36e30 | 4.0574 | -61.5794 | 2025-03-24 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e1ffadc8-3593-38e8-b197-c61a68f46512 | 4.094 | -61.5598 | 2025-03-24 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 0a7b8e0f-0ab3-3eaf-a939-547e478098d5 | 4.0575 | -61.5605 | 2025-03-24 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 17fa1fed-a584-34e7-9260-ba7bb3ac72fb | 4.0758 | -61.5602 | 2025-03-24 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 140.9 |
| c9a47c7f-b9eb-3c43-9d34-5359e4dbb9c4 | 4.7001 | -60.9026 | 2025-03-24 00:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 47.6 |
| f0478936-e1db-3b55-a110-c54cd75abfef | 4.0758 | -61.5602 | 2025-03-24 01:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 2c7945dd-2ac2-377e-828c-3fc542b62d4c | 4.0757 | -61.579 | 2025-03-24 01:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 51c23fe6-ffb5-3670-8f3c-d87eebf298e1 | 4.0575 | -61.5605 | 2025-03-24 01:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| afa42ca0-d4f3-3755-8189-ea332e1fec89 | 4.094 | -61.5598 | 2025-03-24 01:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 49c37666-f433-33b3-b71a-084d2f0f083b | 4.094 | -61.5598 | 2025-03-24 01:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 8abde853-2870-3e03-99a9-5df65f3853d2 | 4.0758 | -61.5602 | 2025-03-24 01:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 121.9 |
| d7ba4cd7-e43a-354e-b7bb-1302e36c146a | 4.0757 | -61.579 | 2025-03-24 01:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 2cf1bc2f-52e2-3c32-9d6b-e4e0efeca893 | 4.0575 | -61.5605 | 2025-03-24 01:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| edbd665a-c7ac-3c1c-9906-a5814488a7cc | 4.0758 | -61.5602 | 2025-03-24 01:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 4f88057b-1151-3835-8ff2-72ed7f671e71 | 4.0575 | -61.5605 | 2025-03-24 01:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 47.3 |
| e1cf92d7-235d-3836-a7ce-de71f9925bc8 | 4.0757 | -61.579 | 2025-03-24 01:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8cf615a8-7c2a-3f14-a39b-09bd3d68e6d9 | 4.094 | -61.5598 | 2025-03-24 01:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 2ca923e6-85bd-3efb-a3e4-cfafeb800a16 | 4.0757 | -61.579 | 2025-03-24 01:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f21a8b80-71a5-39ac-b344-26f7b6895f4f | 4.0575 | -61.5605 | 2025-03-24 01:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 8f718416-0697-3781-88e2-ed5c79cf358e | 4.0758 | -61.5602 | 2025-03-24 01:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 125.0 |
| c3db01e5-f5ef-3444-a7a5-24d56c75c536 | 4.094 | -61.5598 | 2025-03-24 01:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d5662719-a048-37b6-a9ed-7bf24b3f7714 | 4.0757 | -61.579 | 2025-03-24 01:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 851b35be-0983-33c6-a52e-0924afbb6735 | 4.0758 | -61.5602 | 2025-03-24 01:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 122.3 |
| a042757d-c536-35d2-9c6b-44d78b9072ca | 4.094 | -61.5598 | 2025-03-24 01:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| b4bc65dc-1709-307e-b7c3-305bb07343dc | 4.0575 | -61.5605 | 2025-03-24 01:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b32b690a-2aff-3c61-9fcd-b30789758143 | 2.14826 | -60.59427 | 2025-03-24 01:43:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d9caf15d-b0dc-32ee-b30d-4f2621877de8 | 1.38404 | -60.79753 | 2025-03-24 01:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c4b810d5-d579-3aff-b673-d8e985c4c767 | 1.3824 | -60.80929 | 2025-03-24 01:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a95ef732-7c36-386d-aef7-64987a8c91f1 | 2.08564 | -60.22613 | 2025-03-24 01:43:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c6f5adf2-6f7e-3018-88fb-a18255d84874 | 1.94006 | -60.61649 | 2025-03-24 01:43:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f2ca56b7-73b5-3485-80b4-691d77294d12 | 2.82941 | -60.43724 | 2025-03-24 01:43:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f038690a-2533-3008-a206-24c7f3cf6c69 | 3.30863 | -60.09768 | 2025-03-24 01:43:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8301f9c7-9af8-375b-8354-36ea92f865d3 | 1.5709 | -60.70211 | 2025-03-24 01:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b147c910-3482-363a-ae88-1af21f6224a5 | 4.07849 | -61.56275 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 93.8 |
| cc74cc60-27b4-37c7-963a-2e25cd8bde53 | 4.06698 | -61.57275 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a2c327f6-d345-3d63-bb2f-d2f0c18c146f | 4.09852 | -61.56543 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 89424326-5924-3502-8609-be41e7162c1a | 4.09004 | -61.55264 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 9c674c88-8271-39dc-8b08-08dd12d28983 | 4.0885 | -61.5641 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 3a6f873c-8b5d-377b-a293-40b1859f253f | 4.07697 | -61.57418 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d077487b-001f-377d-9132-8ab0028985e9 | 4.06849 | -61.56132 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b02b9610-c11f-3b3f-bcd4-84499578a487 | 4.04753 | -61.56409 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 3b641ff0-f95b-30f3-aa54-6f7eedfbec9c | 4.05911 | -61.55402 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2272a07b-5bbc-301d-adff-29daf2b1e4bf | 4.04911 | -61.55265 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ca5e989d-8580-32be-897f-a831b4dcc8a1 | 4.10007 | -61.55395 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 6605fa0a-377e-3f2b-850c-9b101bb64135 | 4.05849 | -61.5599 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 77448af8-0553-3f31-b215-94469dd7ee70 | 4.08696 | -61.57556 | 2025-03-24 01:45:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9517d791-c436-33d5-9b23-0dfd91ef0fcb | 4.0758 | -61.5602 | 2025-03-24 01:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 56b70a80-3f9d-30ee-8425-024adc6aa003 | 4.094 | -61.5598 | 2025-03-24 01:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f1ecb20e-094b-3e81-a768-f2605451be17 | 4.0757 | -61.579 | 2025-03-24 01:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 534dd912-cec7-30a3-909f-b70f7daf6faa | 4.0575 | -61.5605 | 2025-03-24 01:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c71e6736-9cdc-355f-b024-b7cf5052cfea | 4.0941 | -61.5409 | 2025-03-24 01:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 1bc0627c-8a71-3f7f-86a2-28fde50bd283 | 4.094 | -61.5598 | 2025-03-24 02:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| db8487af-3f0f-37e5-97d6-93016884fa07 | 4.0575 | -61.5605 | 2025-03-24 02:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e666c5da-6be2-3183-a05a-032704096f40 | 4.0758 | -61.5602 | 2025-03-24 02:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 083c5a9c-d9b9-3ac9-bd83-f5a05ad1c5d7 | 4.0757 | -61.579 | 2025-03-24 02:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 86f206aa-57a1-31c1-8e6d-fdba58fc9863 | 4.094 | -61.5598 | 2025-03-24 02:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 61324028-ee5a-3b48-a6ec-f0093814687a | 4.0758 | -61.5602 | 2025-03-24 02:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 86782cfe-0075-36e3-ae26-39944ceb7d80 | 4.0758 | -61.5602 | 2025-03-24 02:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 59ba542c-7348-3b33-b876-78199fb9655a | 4.094 | -61.5598 | 2025-03-24 02:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 3dd57f47-3713-334e-9e6d-5993e5fe1848 | 4.0758 | -61.5602 | 2025-03-24 02:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 5b27b1c0-fbe8-3b2a-b1a5-7ee617287aef | -7.02666 | -34.92081 | 2025-03-24 02:45:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| ef673118-8981-351b-96e7-dc4686baf25d | -7.02814 | -34.913 | 2025-03-24 02:45:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8ec13e2e-e088-3e99-8a29-1ae0b6a108a0 | 4.0758 | -61.5602 | 2025-03-24 02:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ae686f3b-ed61-37d0-a70f-011cf84abc26 | 4.0758 | -61.5602 | 2025-03-24 03:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8e9124fb-c0f6-3924-a6ac-173229788ea9 | 4.094 | -61.5598 | 2025-03-24 03:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 784174cd-0d80-38f9-9968-718a37f9792c | -7.0233 | -34.91169 | 2025-03-24 03:08:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2e0d5746-160c-322f-9d08-6df153e2215b | -8.38977 | -35.02812 | 2025-03-24 03:08:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8a368723-dce1-3269-8520-86cac4bb8696 | -7.02239 | -34.91315 | 2025-03-24 03:08:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 66c670f2-8d50-3a9e-a96f-7c971d55bef6 | -7.02722 | -34.91383 | 2025-03-24 03:08:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 4deb4b10-eb6c-358f-8fde-1964395f6822 | -6.04002 | -35.31313 | 2025-03-24 03:08:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f2f0e99b-6c05-36d5-91fa-5f7cb49da7f9 | -5.51942 | -37.48563 | 2025-03-24 03:08:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 51dcfbe5-10b5-3e57-bcb3-2d15e6fa5f35 | -7.0211 | -34.9115 | 2025-03-24 03:10:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 79.2 |
| 97f50ac8-c98a-3101-be0e-d90998586d9b | 4.0758 | -61.5602 | 2025-03-24 03:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0af5e6f7-b4bd-3423-8dc0-0972428e6dee | 4.0758 | -61.5602 | 2025-03-24 03:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 69e5ec93-3152-3f8a-8c94-53f7e7950527 | 4.0758 | -61.5602 | 2025-03-24 03:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b31890ce-7369-3515-8b74-19bbad807b24 | -5.23399 | -39.44181 | 2025-03-24 04:00:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3a7a3f15-5217-33f0-b82f-b5d7c907a6cd | -2.95371 | -39.90561 | 2025-03-24 04:00:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
