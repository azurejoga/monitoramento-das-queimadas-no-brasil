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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f73fb9b-d278-355f-b1ac-cd910b1e0a94 | -5.13904 | -60.38799 | 2024-11-21 04:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 24229e71-37e6-37dc-8dae-4553b3464f8d | -3.5242 | -53.80753 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61d1d1f8-71a5-35a1-963d-8e71318daf5e | -3.1809 | -50.38873 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30bb7f1b-e63a-3636-bf58-aa78b0f0b93e | -3.14066 | -52.98286 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 329baa39-ec60-3b93-9dd3-822d7969e9d2 | -3.28421 | -50.00967 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2da8108b-9002-36a0-a1d1-41caeacbeff7 | -2.58956 | -54.04605 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bd964ee-ff99-3c26-a5ff-60df72aa405e | -4.63788 | -49.54543 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 744cb387-d837-365c-8f7d-fdf44c74ac15 | -3.56843 | -54.68715 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c50e6857-83fc-3ee3-abfe-79f0bedf0bfd | -3.3567 | -53.40428 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ba2556a-bbff-33ef-a159-3a5d2c773b3c | -4.03632 | -46.2238 | 2024-11-21 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e5d420b-770e-360c-9f96-88817047f5e7 | -3.03948 | -49.4674 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad5f0aa6-736a-313a-af16-90e83e654a9a | -3.47203 | -50.49239 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cefbdb81-fc3a-3885-b28b-2ea6d7ea72ac | -3.94817 | -51.22882 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 340a4f3f-1af0-3ef2-a419-9db965a58585 | -3.283 | -53.82933 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e8170c75-97f5-3244-985f-65e23877c18f | -2.58501 | -51.72077 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecc80e43-ed3c-3cbd-ad18-5367b2e97f24 | -3.53982 | -50.52786 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ee885f13-3781-3905-a204-d6198cd40fea | -2.28797 | -53.63071 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83980056-9101-3595-bcf4-3944cd7b033e | -3.75333 | -52.32405 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df055565-66e3-3301-87e8-e52a6b119f03 | -3.50747 | -54.51505 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4496cdc-c6e9-3926-8e02-f9ad27787877 | -3.05141 | -54.41129 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab56ef2e-d162-3c1c-82eb-fd99fec33211 | -4.96025 | -49.84194 | 2024-11-21 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63550902-2abe-312c-b84f-bc0e9841a2ce | -5.119 | -46.17813 | 2024-11-21 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd5acded-9aae-3cfc-a4ad-3470648992e9 | -3.10211 | -53.74773 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63f21328-767c-3e54-879b-9e1274335f54 | -3.04966 | -54.52985 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5fbbb9c-5ef9-3eaa-bac9-f90a1bb67e76 | -6.8207 | -46.78194 | 2024-11-21 04:55:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d1644690-f855-38b2-a0f4-645aeb5f3b33 | -2.72963 | -51.74285 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abcc923f-f2e2-3707-97dd-30e35b6992f1 | -2.78626 | -54.06998 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70f0cb17-8ea6-3844-bf4b-585b8b4885ac | -3.03876 | -49.47199 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e66e7b9-d967-3636-9df8-7cc001331c8b | -2.60607 | -51.79385 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 183177a6-4334-35dd-99f4-1f49423d0bfe | -2.5464 | -53.99625 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f57a5cc-4cf8-39dc-aa5b-202130fec797 | -5.27666 | -45.45093 | 2024-11-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5acfab0a-e85e-3c91-9155-cb97d380cd2c | -3.52063 | -54.17425 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| adc79016-ae7b-381a-8d3f-54d0a2637c07 | -3.51261 | -53.79512 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c953f7ba-1ad6-3985-917e-3790be75f032 | -2.5796 | -54.04449 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f986ad9b-4f31-3f14-b9a5-e7bca7616c98 | -4.85141 | -50.8621 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffca7ca7-cad8-3a91-8adf-dab79bac6ccf | -2.62201 | -54.27238 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4c0126c-8184-376e-ae53-294b5858a937 | -3.79345 | -50.27061 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bea2ab7d-535a-3729-b504-d7b45f95e3da | -2.79559 | -54.01107 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2adbc6f3-6d45-3332-8445-9c12eb149bca | -4.34242 | -46.13788 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ceb3b09-d287-3ee4-bd9f-c61368ba1c1d | -3.80917 | -47.79811 | 2024-11-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4529ad48-0e80-30d3-8e35-66eeb87e7cd7 | -3.75736 | -52.40804 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 970b2969-9485-31e7-b5e8-968405192ff8 | -2.7653 | -54.07346 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 392deaee-1f45-3038-a650-b9be0e55f2dd | -3.1053 | -53.70595 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e05017d-828d-3bf1-8cfd-b1a1d9062711 | -3.23277 | -53.06756 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9185fb46-4090-3c02-8720-37187252e909 | -3.02927 | -51.52658 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05d0f737-f7b1-322d-8482-34dc8d26906b | -3.75791 | -52.40453 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84b693f0-debd-3462-8793-52fc30ecc8da | -2.73609 | -54.12941 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f706b1f1-9f81-369f-a6ad-ac182670eb7a | -3.10596 | -53.74481 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67636c6c-d2df-3db2-b3cf-86b3cbd0becc | -2.8957 | -53.05019 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddc6c1d4-8b8b-39db-94f2-9f0d50fe6386 | -3.3579 | -50.18454 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a454699c-3bc5-3d08-8ac4-8702d38633bb | -2.82434 | -54.02266 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d8bdbae-4634-37f2-80e2-1b96ef100087 | -4.1781 | -53.58237 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da853c8e-588c-3678-840d-640098c3d5e3 | -3.70908 | -51.84258 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ab448b8-d31f-3d67-8221-7f98437d81a7 | -3.6951 | -51.27716 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbca0344-20c6-374e-a1ea-d214306135ed | -2.60451 | -54.05906 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dae831bd-4ad9-3c90-b71d-b830d928e51b | -8.36304 | -49.48469 | 2024-11-21 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b042cbc5-a8d5-36aa-bae2-a2f58a674051 | -3.51098 | -53.80544 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 390e82b2-bfff-38e2-a09a-786686b620c6 | -2.56855 | -54.07126 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c422ef18-f6f8-30c3-ad4e-e0343f076015 | -2.81946 | -51.79647 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a41f4adb-adb0-30c1-966b-4b53f2e00e49 | -3.47244 | -54.54191 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07bb7235-7a5e-3fc6-959f-3ee981a4198d | -3.95165 | -51.22937 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc22cbe5-a294-3c35-aa78-1bdf04243555 | -4.0907 | -51.07891 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8ab8fac-0d11-3628-be9b-0d0226cbfaaf | -3.81307 | -51.35309 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f4f344c-991c-38c8-8b90-d342eaec9ca2 | -3.31996 | -54.08974 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bdc575e-0704-35f5-8f66-fc66e80fbe57 | -2.52984 | -54.01507 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca85ce7a-1372-3fa7-86ea-d7e9893d9867 | -5.94103 | -46.19753 | 2024-11-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baa4fe41-6d37-3e86-a08a-039f6f57e3ba | -4.06698 | -50.9059 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fe01c5f-265c-3edc-a8fa-65d52a985d50 | -3.272 | -53.83467 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 258af7a5-3e65-30d9-b652-5ec343e53c86 | -3.90885 | -53.82568 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3296b948-95e1-3c97-a5bb-7719bdfb141a | -3.10433 | -53.75513 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f18c6007-86ed-32fb-9bff-24394f6994c1 | -3.28772 | -50.54119 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c703bdc0-3206-320e-89b9-7bbbe2472b8c | -10.69987 | -48.80912 | 2024-11-21 04:55:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 868dd1a6-4b73-346c-8288-f999c9baf309 | -3.04529 | -54.40677 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2107be24-358b-3e2c-87cf-69232ce14742 | -2.82984 | -54.00932 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b353f47-a1e3-3c2a-99c8-3c3778c3448e | -5.66682 | -47.33467 | 2024-11-21 04:55:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c716a90-4757-36dc-b611-4a0addacb79c | -2.78829 | -51.72225 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 730d3531-5599-3489-9ae3-78a0dabe8b24 | -2.28866 | -56.32747 | 2024-11-21 04:55:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac0588b3-9fa2-3cb0-9a07-2a7e688e9c10 | -3.28744 | -53.84412 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 799c69df-46ac-3a66-ad96-bb9ddf36af21 | -3.19475 | -54.32297 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 060db1b0-3e01-3fd1-9ed0-07ac23041f07 | -2.91391 | -53.0636 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 739bb444-2a66-36d1-b795-dfa5c1c96add | -3.182 | -54.31742 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3bb62935-5157-3e58-946f-c2eed707baee | -2.73496 | -54.11498 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fc36f65-a078-33bd-a493-bf2e30d77bb8 | -3.51471 | -54.68565 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b3336d60-9225-382d-b441-f119e6c25d53 | -2.83592 | -54.01382 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5cc36668-83b1-35fd-aacb-7faa5aab2909 | -2.58107 | -51.72385 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 372c50c7-77a4-3a15-bd5f-e8288929065c | -5.9418 | -46.19211 | 2024-11-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 978439f5-6afa-3ec2-bdc8-a7a68afaaacf | -3.5434 | -50.52841 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aa9865d1-2ce4-3a5c-9899-6641e73c04a7 | -2.93481 | -54.41824 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1948e19-4b11-392a-8d1a-a1f5362d3e5d | -3.53825 | -50.44392 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0aeeb798-92f2-32da-b974-f5164998021f | -3.80208 | -51.148 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06d8fb85-ab1a-3067-a871-af5b50ce89dc | -3.98875 | -49.9216 | 2024-11-21 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1723542d-457a-35e5-8f33-66d2dbc61af7 | -2.78681 | -54.06651 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28c8696d-e78c-3de6-a3d0-ef1a86e8f806 | -3.57798 | -52.29694 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 946ca6d6-34fa-3e5d-852d-b88040318287 | -3.39507 | -51.20198 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b80343f1-f527-3f7f-a26e-78f6ad45b3cd | -2.85241 | -53.97385 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec951e4a-ac8c-3f52-af72-6c4fb6e3ef96 | -2.77446 | -53.97195 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96cbd1ab-fe92-3fc2-b045-deff05ff412f | -5.42859 | -45.3418 | 2024-11-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d58c07b3-927b-37c2-9171-48878c344ad6 | -3.49387 | -50.44563 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83ff1bff-bc85-31fa-aa2a-f8aa125a5550 | -4.33911 | -50.42243 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ac8db4d-fabb-37e1-8de8-cb27317fa91a | -2.61007 | -54.53733 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README71.md)
