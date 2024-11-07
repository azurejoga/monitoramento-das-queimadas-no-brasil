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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a62d51b-2ed1-39ba-bb29-4d9b5c982172 | -1.33886 | -54.2128 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a818e25-e83d-3a95-8659-1cfd67066d64 | -3.65676 | -51.2433 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f3e33ab-d585-32d4-b2c8-81e3be6237b7 | -2.40137 | -53.63226 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20fc0b8a-6fd0-37a7-8d7e-561374ae2048 | -2.9733 | -53.8699 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ad49eef-e025-3f36-9183-5941b9931239 | -3.0546 | -51.07094 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00eb69ca-3079-35ba-b02f-5a5db969e5f5 | -2.75379 | -53.22279 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1357a869-2ff6-3493-84db-d0fb4832ca08 | -4.38613 | -50.83865 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b83e560e-d6a6-3c7c-a3c5-a75d021fea84 | -1.22803 | -54.54282 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2cd4478-d4ed-3d45-babc-8a062d737ec4 | -2.7998 | -51.4942 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23265eac-fdf9-39eb-a923-b62e6a793d84 | -3.45035 | -51.11241 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7aa5042-88c4-347e-a1b5-f14f6a7a712f | -1.4404 | -52.82397 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb4edcf4-4bb9-39e8-bfe2-acbbb1007ca3 | -2.99519 | -51.05939 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb5535c3-aac7-3595-bd56-2a634f637457 | -1.13741 | -54.2205 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1048b3c-ea1c-315e-9cc8-49efd7a67675 | -4.25842 | -50.69607 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b8c64d6-7f80-314b-b799-ff21e5615c2c | -1.14595 | -53.73551 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 430ebc45-3c5b-3d97-aa93-2ff27d2ec530 | -3.11813 | -51.11096 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63e0fb00-1bdf-36a5-951e-954c1c7d6f58 | -2.97037 | -53.86535 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51e302c0-4d20-3cae-8d7f-b87a3e2e8fea | -2.23532 | -53.6741 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a85478aa-9cba-3b3e-834f-b87f32e03994 | -2.01077 | -53.30068 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 902d5492-d7a3-3cdc-ae15-5bf19a53d0c6 | -3.45528 | -50.36998 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6ec0bf8-ffa6-3447-b6f0-cb68236b489b | -2.27797 | -53.79781 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cc87724-e070-3c63-a468-f07c97f02f08 | -2.85365 | -48.6735 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 53f17065-47a1-325c-bc3b-928b0fd53073 | -2.81247 | -52.93832 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26effcd6-b20d-3c73-94d0-ac105791eeed | -2.91551 | -51.04715 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e2c6f20-5738-34e2-8b23-8c566040504a | -0.40754 | -51.56249 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ae67ab08-d5ba-3baf-ac6f-2d9c5b8af59e | -1.52686 | -52.22153 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| ebf0f254-30db-38e3-b644-3f756fed9aec | -2.81756 | -52.92997 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38196582-ab8b-3fd3-84d0-0a102ca42c2c | -3.01363 | -53.43575 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4081d358-b633-3cb8-88fc-e39da9da6f51 | -2.93521 | -54.1187 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 442cd671-b0e1-31b4-8c12-69c6ab7e1e17 | -2.43511 | -53.6698 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b83df910-3947-3df2-be05-29d0edfd45bd | -2.87781 | -51.31253 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f9a7a55-fdff-3c92-a87e-4c5481be34f1 | -4.66752 | -46.33342 | 2024-11-07 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ab18b4d-a066-39ec-b228-ee3a222b5d4a | -2.04889 | -53.27911 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b094854-430d-3cdb-8e8e-f4597bd4a90a | -3.77565 | -51.40108 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4828720b-0fbd-31e2-9a19-8bd24728e1ac | -3.01426 | -53.43157 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cb87dca-a403-3be4-9921-04d4784e3b59 | -3.24593 | -49.58133 | 2024-11-07 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb856ba4-3410-3e80-9228-3a1d9f6d5a7a | -5.02505 | -46.84226 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 07775c71-ad99-31c6-83f1-e650bfe1141a | -3.01 | -53.43522 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09c385fe-798e-3772-abac-e0145e12ec2f | -1.11276 | -47.28491 | 2024-11-07 05:10:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39bd0e42-8e50-30ee-ab0c-cb09bb530580 | -1.22124 | -54.54178 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb6d7b51-8c9d-32a9-a658-cd0d68a8d48c | -3.18916 | -50.58324 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78624ada-d5b4-393a-acc5-65fca9152647 | -3.18852 | -50.58744 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cddd2caa-c9ad-3b4d-95f1-0b35136128dd | -2.91608 | -51.04328 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 778e611e-707c-3132-9fb1-84bf5c93e7a8 | -2.88497 | -51.31274 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a165561-c5dd-39f5-abd5-64e4fe268dac | -4.34504 | -46.77738 | 2024-11-07 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80533d64-f32c-3ce3-ba07-bf2116f9a860 | -2.75809 | -53.21915 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1312f109-dc37-30e1-b2cd-811a9e473b3b | -1.18655 | -53.89971 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eea8e1d7-bbea-304e-9520-cf17b99562fb | 0.26114 | -51.31281 | 2024-11-07 05:10:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee59d312-2569-35b8-bd0b-d0c078440fba | -4.34631 | -48.62732 | 2024-11-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1edb8a6d-9986-3a3e-9d89-d38e5164a55c | -1.3268 | -54.60736 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c4be886-dfb6-3f47-bef2-bde95d578116 | -3.05384 | -51.04713 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 035bab87-17f5-390a-b9b8-ad7ff604e514 | -2.40557 | -53.62874 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f606fdf-9ad3-3d3e-87f1-857bff077e7c | -2.15557 | -53.6507 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66c24598-ab83-3845-a08d-8071bc178750 | -2.84872 | -48.67276 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e6c8ad42-0096-3556-a1b0-5f8ae09c5a1c | -1.11226 | -47.28287 | 2024-11-07 05:10:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fc45bf3-8fbc-313e-a9ef-f29fac0ef695 | -2.85447 | -48.66792 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1960b7e7-ad6b-372b-a3b8-a6be0395e09e | -2.23825 | -53.67867 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 321e3c48-d448-392b-9052-2d84da6b58e4 | -1.43193 | -54.2457 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8cd4323-0ea0-387c-9e56-f2f004dbc0b3 | -3.39571 | -53.68409 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b26e2d07-d72a-3a0d-b033-521755a7e2d0 | -3.24769 | -49.5806 | 2024-11-07 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b6df3f7-697a-3fdc-89f2-3e9deb7a58e7 | -2.06087 | -48.13894 | 2024-11-07 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e40c994-5b2d-3e7f-a5bd-9c84af9c543e | -3.24695 | -49.58544 | 2024-11-07 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f47db22-434f-3649-95db-499d521599d2 | -5.03027 | -46.84143 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6b0c6df7-726f-389e-a257-2d7f4bda9beb | -2.1765 | -53.70303 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57f2ac69-0d01-39c0-afae-6a9f81d82395 | -1.33357 | -54.60852 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7d6a318-01a6-311e-8203-1608ae5970fa | -2.96114 | -52.91196 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ad52784-4b68-32d0-a5fb-4fcd0ca8b533 | -2.82291 | -52.9446 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f677cc0-67b1-3dfe-a388-ea09efec27f1 | 4.34001 | -59.8397 | 2024-11-07 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a017189-ff2c-3841-b12a-1bf3ff3be7c9 | -2.66433 | -49.87107 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 383c2a7b-9975-34ec-a09b-e9a1f6e61c76 | -2.82195 | -52.92616 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4e9fe0d-8241-3768-b5b1-a0186e2e4e46 | -1.22463 | -54.5423 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15711c54-0647-37dd-8674-82c7c793a005 | -2.21025 | -53.71939 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5303335-3d72-3d1f-a4ac-9652b46b7711 | -1.19752 | -53.70373 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1143964-560b-3c22-b671-284b23d20e4e | -3.08333 | -53.88511 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1cbdf108-7e4c-363c-bb6a-7c71207fb4b7 | -2.8077 | -51.80762 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a4f3b2d-d8c5-356e-8649-af5702a678d1 | -2.88835 | -53.32028 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d60943aa-21e8-3984-b4fc-b5aa7119e821 | -1.12602 | -53.60816 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f13865eb-d45e-39de-966c-b730dc7ec058 | -2.93461 | -54.12259 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e981659-08a8-3675-84ab-bee1f1cc3b01 | -3.17997 | -57.06038 | 2024-11-07 05:10:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b5130e7-f537-36b3-a158-fe809fd3f75e | -2.24366 | -53.66715 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 71ed38b6-04c8-3e84-b9b1-01b6fcf2b402 | -3.45049 | -50.37601 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0841da6d-4bd2-30be-baea-7499fa1d536a | -3.5858 | -50.22761 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fb917ecc-cf54-3ec2-a050-a5752b5882b8 | -2.84328 | -52.91136 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0334f4c-ace0-3642-95fa-f46fa12672ca | -3.02025 | -53.44095 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 359626c1-d4bc-3b7f-be4f-b40fbc1c89fc | -1.84392 | -52.35046 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd58ab5c-ed27-3d70-8eb3-0b8e9f52e03e | -2.94068 | -51.05099 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bbf9b4e-d167-3e33-a2ad-4f7705f246bd | -3.51692 | -52.89808 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16892a2d-9ccc-3d51-82ce-7ffe567d5d4a | -1.15446 | -53.65732 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed61034d-044a-3034-a711-8ae14f2ef590 | -3.1736 | -50.59791 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7e46c86-466f-3f16-bccb-be6e52410155 | -1.39074 | -52.19839 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef2fd0e1-4055-3af2-a4d7-12009d5767c2 | -2.30097 | -53.78915 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4182f272-7383-332b-b41b-6ecbf1102d65 | -5.02449 | -46.84637 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91d006d0-c829-3585-bc35-e15802fd8307 | -1.13375 | -53.72176 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e23b62dd-a7c1-3484-ba06-f7b03aebb383 | -2.61625 | -51.30357 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0a31c0b3-7038-34f9-9734-9b51f6406b4f | -3.12118 | -51.11268 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9c2a812-caf1-3110-b37f-9e9df29746aa | -3.44732 | -50.0941 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a98cffc-9f27-3b1d-a564-0d524da0ff90 | -1.11523 | -53.60316 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e88ae7b-3dba-3c75-a33d-b3e5d655acf8 | -1.06264 | -53.66348 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aee4bb94-6dc1-3055-9a5a-45cac80d2f13 | -2.84282 | -51.34862 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adf7e27f-1cee-3d0b-b7ff-41fe3c9d0776 | -1.41722 | -54.50113 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README44.md)
