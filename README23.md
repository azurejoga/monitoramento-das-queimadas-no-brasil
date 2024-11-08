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
| 2dfb3f53-f1ec-30dc-b8a5-2b55a6f65c49 | -3.37805 | -50.22081 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 34ae9b28-8126-33df-8c8e-a9c7c73ca191 | -1.14917 | -52.00651 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5c9075a4-c1e8-36c6-8112-3587a569eb0f | -5.64728 | -44.24423 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94414897-ece8-367c-b713-78f91cf513fa | -1.14442 | -53.71644 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff130858-08bb-3812-b65a-966809c49b88 | -3.03014 | -51.5271 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fa0f7f47-a80b-3914-988b-886b0c2748df | -2.80629 | -52.94044 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c92907c-4f5f-3bf0-a91f-f2c72334deba | -4.39494 | -49.7696 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 513f484e-214e-3ee5-a97d-4112b9ff37c9 | -2.27101 | -47.99943 | 2024-11-08 04:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee52d108-4f2f-3337-8874-5ef573f8eee3 | -3.91284 | -47.95867 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d38345b8-0ba1-38c7-895c-a2d633f4af7c | -3.01879 | -53.42719 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8beabe87-36e2-3cd8-990a-d712525f71ca | -1.51032 | -51.54247 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e32a665-0dfa-3107-8e39-fe216621ec98 | -4.37011 | -49.1066 | 2024-11-08 04:53:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15b6c206-a373-37ae-a4c9-35b5608b6407 | -1.31275 | -51.65586 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1d39ea1-3918-3735-a271-216ecd55fe5a | -2.27282 | -47.99748 | 2024-11-08 04:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6361ffb0-9358-3dc3-8465-773523faf974 | -4.87048 | -42.94215 | 2024-11-08 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d4cafe9-173f-3ef6-9e83-cc820e328a13 | -2.80798 | -52.95144 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5c1f8404-4317-3f49-9e9f-76717d3baec5 | -3.03564 | -53.27631 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8e0f69e-cd01-38c1-8c52-88a05a002e41 | -4.24104 | -47.87165 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a381cf8-cd35-3d78-8a0a-c5233e903f5e | -9.03265 | -61.99139 | 2024-11-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9637a6fd-5ca4-30f2-b2a2-3e5c12fa278c | -2.14848 | -48.82626 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39bcfbe9-aa06-3e96-9c56-bd4949165948 | -4.68386 | -46.409 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.5 |
| abd45893-8c5b-3dc2-8815-a3b60861bf9e | -3.78973 | -44.02087 | 2024-11-08 04:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1d9295f-c0ad-3c8a-8ab9-fbcb4741813f | -4.78379 | -45.65189 | 2024-11-08 04:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45f8435b-cfa1-35de-b011-1589a685b9b3 | -2.23771 | -53.72757 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99421d8f-77c2-3c63-b7cc-594c0735ec16 | -1.50932 | -52.07336 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 490f489e-5f8d-3c82-939e-ade482820dc5 | -2.21095 | -53.71968 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3dd4b2cc-c624-32a1-959f-a68c6d0e957d | -3.7226 | -41.68739 | 2024-11-08 04:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e845df63-10f1-359f-acb2-83536b928b1a | -1.33254 | -54.60352 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 218d03ce-bce7-3ab5-aeb2-a8564c9d9303 | -2.17354 | -53.66858 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 190db30c-b71b-3059-a9e7-a7085ee9d4f2 | -3.22071 | -50.37944 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1035ce79-93d0-3feb-b19e-c37d887ff8af | -2.8135 | -52.93795 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd4b8204-9c68-325a-ba02-8b1d0066c649 | -2.84593 | -51.96638 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4a33d19-94c6-3dd0-9dee-8b5afa3a6838 | -2.25595 | -53.72284 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7240b196-a12f-3d8f-9568-b2ad89203973 | -4.7729 | -48.6778 | 2024-11-08 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4eff06f4-fb0d-3768-9f95-005ef0a725de | -4.63337 | -42.79134 | 2024-11-08 04:53:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c37db48b-ac70-3159-8f64-4966f1f200da | -2.26029 | -53.71947 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53ba8a98-2dd1-39f7-ac7a-3b701ecd2b9a | -9.80228 | -61.51104 | 2024-11-08 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35bf3455-f365-3514-92f5-beea9f256358 | -2.88748 | -53.97119 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a34a1f9-cc74-36c7-b254-5b372cb30860 | 0.62282 | -59.91561 | 2024-11-08 04:53:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e13e2709-4d5f-361f-b192-5e0f599c50ff | -1.13578 | -53.72659 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c193012-611d-324d-9185-f95f6ca58ece | -3.54478 | -47.37986 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4ebd2d52-b090-332c-89fb-c809136b6894 | -3.05751 | -57.10897 | 2024-11-08 04:53:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5961e5e-65fb-35ce-a04a-f87d684ae741 | -3.71872 | -49.00726 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fdce19b-8069-3ff8-a8da-6be84c59b745 | -2.81059 | -51.8029 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb13f99f-b8dc-3d89-a62e-7acf2f8f87e1 | -3.2504 | -53.36097 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e79d67d0-e455-36c3-bfc9-4e9e0eec90ab | -4.36553 | -47.2236 | 2024-11-08 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a59fa9b6-1e3d-3683-9e38-42f1cac3bc8a | -4.68447 | -46.40491 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3b1c168e-f070-3581-aff2-2c7b7df14140 | -1.43381 | -55.69616 | 2024-11-08 04:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 957593fd-1863-3822-b9ff-196b756f42ef | -2.25994 | -53.71967 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ce4f09e-1909-353f-9769-884c18d97063 | -1.22421 | -46.52718 | 2024-11-08 04:53:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ec24f14-3257-3e67-b72a-e0907d051e49 | -4.57477 | -50.60283 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01f3bc42-ccb9-3a7c-8cf9-2c9cb09d92d8 | -0.97989 | -51.78263 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb6cb8c2-d74c-3d0f-9c6d-8b0239b38bf9 | -0.95843 | -47.88445 | 2024-11-08 04:53:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e4229e3-2c2c-30c7-ae60-dce87726b875 | -2.54937 | -53.99976 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fc2432a1-5578-32af-93a6-32b420df4276 | -4.91804 | -44.04692 | 2024-11-08 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 425f15b9-65c7-343a-854a-45a22a323428 | -1.14851 | -52.50997 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91740cdb-125a-377c-b1d3-6aa453de1c17 | -5.64656 | -44.24427 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a1e49d7-519d-33af-b115-2bfee8ff787c | -3.81038 | -47.79826 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77da4dea-f117-333e-9091-cc357c3bbabe | -2.92409 | -51.04998 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1cd244d-6691-3bc8-a720-b3768f029ad3 | -3.01496 | -53.23318 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53d652b8-338b-3828-8438-3d50f5e95396 | -4.20406 | -48.69862 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 127c3912-c841-33dc-afce-fcd380b56ebb | -4.99501 | -46.82001 | 2024-11-08 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d00087c0-2672-3c2f-aa59-8dcfef80a34d | -1.9757 | -53.13744 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 912bb60e-ea5c-360d-8f83-be836a6c548a | -1.13519 | -53.73035 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4daab721-09c3-328f-aa11-7dbc466b47c1 | -4.12354 | -46.91678 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76329aa3-50cc-35ac-a29c-2c095d26f076 | -2.94957 | -53.2849 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0aed1c55-d8c4-3e19-9443-894e3099bce9 | -2.74122 | -51.89681 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c528591-63f0-397b-b3cd-f1c53b1f530c | -1.87186 | -48.76648 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12972e85-4ccf-3b5b-9c87-86384bdeec5e | -2.18394 | -46.46636 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa08f8ea-5be3-32c9-8c34-137cf0580cc7 | -2.79535 | -53.99925 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2c4b178-2e48-384f-a01c-6f7e836496f4 | -2.4303 | -55.6069 | 2024-11-08 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1874c23-625c-347d-818b-c90b22dd32b8 | -2.28323 | -53.81793 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7628e035-234a-3cb7-8f54-1fa965189368 | -1.38773 | -52.19862 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc725b07-92df-3a78-8e77-4557e331f1b5 | -2.84565 | -51.77316 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dacbff7d-4281-3433-96aa-16e4116b9e07 | -3.95271 | -48.16031 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0c61a53f-1aa5-3cb0-aafc-b8514506af78 | -5.92241 | -44.8697 | 2024-11-08 04:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75d5dd14-f579-3463-ac6f-5630fa3bc975 | -2.85171 | -51.77761 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dcdcdfd-fcd7-331e-b424-13ca1e01bea8 | -9.16291 | -61.53286 | 2024-11-08 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 315f4098-7640-3d24-89fe-37193a3b036b | -4.37324 | -48.17224 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04ffdcd4-6bee-30f7-a44e-a6c5665e279a | -2.25853 | -53.73055 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69673fe6-17df-376a-83e8-1b8433188b3e | -2.25971 | -53.72316 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 835a2196-1b53-3b36-bbbf-30661c17093b | -3.96781 | -48.16273 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ec580d1-6718-3aa1-a649-61777f707bfe | -3.62074 | -50.19292 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e48dc68a-bf7e-35c1-9cfb-4475086a8458 | -2.69524 | -51.69305 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2edf51e8-ce96-3573-abe4-a3dd0b3c2b33 | -3.02301 | -53.87028 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 242a32b3-ba8d-33c0-a33e-319057568810 | -1.35121 | -51.4092 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7db333bc-8d39-3e3c-8f71-88c3e905ae34 | -3.25375 | -53.36151 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 229cb0f5-7d9b-3581-bc0c-eb6917431cf6 | -1.64743 | -47.82668 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03ca4902-c0c7-3c15-a324-c157eb186522 | -3.28305 | -51.52093 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45b9f196-e7fd-33cf-b301-9ae307ffa77f | -3.95579 | -48.16545 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 17aa0d92-d865-343a-adb1-22c92f8370de | -2.81586 | -52.96347 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6b33244-aafa-3031-80f2-6a9209c848c7 | -3.45747 | -52.01668 | 2024-11-08 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc053e10-f289-3763-85a8-6e6d410dd840 | -3.54794 | -47.38559 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f4f2c913-e4f5-3eb2-bbf3-b0ef7b7afb00 | -4.31532 | -49.22486 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31dc9f12-4638-36cb-9adb-8ef3958fcc6a | -2.193 | -53.63396 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2e9f585-d64a-3fec-94d0-25118658a725 | -3.09671 | -53.71268 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e232843b-36a0-334d-8a8d-2a0af432e773 | -3.20374 | -53.85725 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4084cb87-3e51-3edc-9c13-ff58148feb15 | -3.19942 | -53.40053 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ba229b5-9d6c-336a-910f-f7d19c0906f3 | -2.76001 | -53.21506 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19cfca55-7585-3474-8b1e-2e050ea573e5 | -3.04871 | -51.3427 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README24.md)
