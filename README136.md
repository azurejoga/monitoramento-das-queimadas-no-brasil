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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0933f187-db10-3a7d-a56d-13f5a4c90a5f | -16.81498 | -57.37811 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 86b71663-a17d-35b3-9091-33d5e609fd1c | -16.81457 | -57.38205 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 57dbd0dc-c889-3831-8151-1b58fc2844b2 | -16.81416 | -57.38599 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 27e7b843-6b11-3955-86aa-28173c69b5f0 | -16.81374 | -57.38993 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| a4844d81-9846-3d00-a5a3-09bc4d626df2 | -16.81333 | -57.39388 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 271c1073-2465-379d-ad23-21cbdfd7c2f4 | -16.81292 | -57.39781 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8992c8e1-1282-32dc-a41f-78dbfc62f0a1 | -16.81251 | -57.40174 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c30cdc31-4961-365a-a1e8-7e482d8f9197 | -16.81165 | -57.37794 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7a9e4e35-4649-3bb8-87a8-d4a7344cd107 | -16.81121 | -57.38188 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cae9d6de-32ea-3ac2-8cee-502e2b192b0d | -16.81077 | -57.38582 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 57503d8d-1668-389f-a1cf-0017ffdecb9b | -16.81033 | -57.38976 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 39f6c941-81aa-3914-9388-cc58c858c000 | -16.80989 | -57.39369 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 741f55d2-6095-3db4-b6fe-5241833cfdbb | -16.80946 | -57.39761 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 65906ec1-ac2a-3816-b919-95e06d4e3dd3 | -16.80902 | -57.40154 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| bd360ac1-02e8-391e-ba91-ca1f1c096b70 | -16.80858 | -57.40546 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6792e05a-2a11-305f-810b-86637b07a903 | -16.80687 | -57.40108 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 065f0b02-6ebd-3af8-99bf-7566fbaefdd5 | -16.80646 | -57.40501 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 79a9774b-a4e9-3317-9443-ec267318712c | -16.80294 | -57.40482 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a7f7a46a-015f-3759-9f90-bbe0eeb8ee87 | -16.80123 | -57.40042 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 967127f2-d9bc-3646-801d-7eb0ea355cd4 | -16.80083 | -57.40435 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f0cad796-af00-318d-82ca-a47f5e219f4e | -17.0084 | -56.69811 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0e97feaa-8384-356e-bdfd-29d9ab204755 | -17.00795 | -56.70251 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1287f9db-f7f6-3e9d-916d-8b43676d22c3 | -17.00249 | -56.69746 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bb9c532e-27d2-3002-ab42-6e1c04babb53 | -17.00204 | -56.70185 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c06dbbb3-f7a0-3b74-9182-d4a31c2b8a08 | -17.0016 | -56.70624 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d892d0fe-f6f9-31a6-9686-15ab51deef60 | -17.00115 | -56.71065 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b2d17289-befe-30ea-aac0-831ba0177dbf | -17.0007 | -56.71505 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2fcb5817-81af-354e-b73b-e643cff71c66 | -17.00026 | -56.71944 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d6c8a7ff-bb22-3487-9797-ee58ec1ce019 | -16.99981 | -56.72384 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 413ad77c-332e-36eb-bb55-3c9f6fdafab2 | -16.99936 | -56.72823 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b2e1c504-1cf3-31ed-bf2f-bb0a36cd2b06 | -16.99658 | -56.69677 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 032f8eb3-c884-3a06-94b9-90bc92151354 | -16.9957 | -56.70555 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fdd81d7f-b2dd-311d-aa52-4bff2ed4eea2 | -16.9948 | -56.71437 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| da8664c3-775c-318a-b38b-cb087610828b | -16.99436 | -56.71878 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 88d62944-7245-325f-b2eb-65ddb7b78a09 | -16.99391 | -56.72317 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c573e60f-e942-35a5-afd3-aea8bd2eec3f | -16.99347 | -56.72755 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 63ca9486-5b49-3b57-b2d6-85e5d935e70f | -16.99302 | -56.73194 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 83be2386-c642-38ea-9739-5908efcc268c | -16.99286 | -56.69409 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9cfd15d7-3f5b-37ab-8440-e64d936b70da | -16.99191 | -56.70288 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0c1bfdf6-edc5-3948-890a-9eb0aa69b0a7 | -16.99144 | -56.70728 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a7f02147-9a80-3a89-895b-d50e5e24813f | -16.99049 | -56.71608 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b1afaf2e-ce08-3f16-852e-45680ec68df5 | -16.98979 | -56.70489 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| b602cc5b-f289-3ec8-a2b7-c7ca963b624b | -16.98935 | -56.7093 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| df92eb57-74ce-3262-be6c-ad1a1dfb9ac2 | -16.98506 | -56.71103 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dc30acca-662a-3745-9f8c-0ecace238a60 | -16.8653 | -56.71536 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 61642c04-1307-34d6-89cf-dee2e73e1f26 | -16.86486 | -56.71974 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 51f72ac8-6ea7-3c58-a806-5eda989523f7 | -16.86063 | -56.71589 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| be176df2-246b-37eb-95db-c4db393717c2 | -16.85941 | -56.7147 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 886fe5d6-9b7b-30d9-a6e4-67b19dcb50aa | -16.85474 | -56.71523 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7cb61360-6607-3fe6-bb84-5d71f512b8a2 | -16.93154 | -57.70287 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 497f8c0b-5089-3d64-bdae-db23fe734464 | -16.93113 | -57.70665 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ec62f847-07ab-3338-b1eb-562481d1527d | -16.92682 | -57.69468 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fdb7251d-90cf-3283-a7a6-b9a0ed6fe8ce | -16.92641 | -57.69845 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 36a547d6-6a18-3200-a58b-c29fe79a32e3 | -16.926 | -57.70223 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 778c75e9-d43c-35e1-a34f-06171e39b1ec | -16.92169 | -57.69027 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 001af15d-572a-35a4-80a8-4e9793732bca | -16.92128 | -57.69403 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3ef0de5e-830c-3f4c-8d53-f43edc2ee4ff | -16.91615 | -57.68961 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 25625651-2053-398f-8e8e-67da6fc15487 | -16.91574 | -57.69339 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3ddf95a0-7b72-385f-93ca-96f1fbb42cce | -16.83568 | -57.45202 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e1e84a7e-f24e-3290-9885-7401c01958db | -16.83526 | -57.45593 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 17a1e606-00e6-3359-90f0-df3f35a02b98 | -16.83047 | -57.44747 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 863a1216-19c3-3db4-abf1-531c804c1f1f | -16.82485 | -57.44683 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ee5d102d-3621-3574-ac1a-cb9fc59c71a8 | -16.82444 | -57.45073 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| aa999ee1-e596-38fc-b80b-61c4b6774c39 | -16.82212 | -57.41877 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a7d4688b-ca67-33c6-86d1-37bb7f1280c4 | -16.82171 | -57.42269 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| c25e9567-6f7f-35be-89da-b8b673c8974b | -16.82129 | -57.42661 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| c4470d04-811a-3722-9393-98510e850122 | -16.82088 | -57.43053 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 8a4af091-a642-3818-bb20-15f5d6dbeba8 | -16.82047 | -57.43445 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| e3f95c8d-7c24-3313-a364-f6e2aeed4414 | -16.81964 | -57.44227 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| fa37a65c-1763-3046-890b-6f3c5d78a363 | -16.81923 | -57.44618 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 136c8edb-15e9-3478-88aa-f51dfb7291ce | -16.81882 | -57.45008 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 42139e7c-02d8-3beb-b386-145ef03eb065 | -16.81732 | -57.41027 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bead9084-6106-32d7-9e3a-b70eee956351 | -16.8169 | -57.41418 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bd861625-76cf-3c27-ae9b-3b34bcf2d635 | -16.81649 | -57.41811 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e99cd920-1071-3989-ba8c-17a2efe6b217 | -16.81608 | -57.42203 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 51f0d0d7-a8b4-37fa-8265-283f44ad7f5f | -16.81567 | -57.42595 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| a6611cda-cc2a-336a-9d08-27f3e6195d7b | -16.81525 | -57.42986 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 015782e8-cf73-3791-b55f-6e216dbd2477 | -16.81484 | -57.43379 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 5b56ea2e-58a2-3897-bf03-5f8be7281857 | -16.81443 | -57.4377 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 77e564d8-5a91-3ed5-9c4d-b9b5ff45d3fc | -16.81402 | -57.44161 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f3cd177a-e638-343f-9648-781232eee51d | -18.71602 | -57.29889 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8ab3e91a-fcdc-31f5-b127-892236200523 | -16.81361 | -57.4455 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 35890a22-5885-3641-a03d-0d6b13b5e3e8 | -16.81127 | -57.41352 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a82e5752-5ba1-3b78-bca5-e549dee19a14 | -16.81086 | -57.41745 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d496c890-158a-3728-9fa2-09fc03dcc6c1 | -16.81045 | -57.42137 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 60f8a064-4e99-3543-9d60-9631d1fc1d92 | -16.81004 | -57.42529 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 63084e7b-6611-3d63-a65b-d10b9a7b5399 | -16.80963 | -57.42921 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 837128ea-9b0e-3994-8908-3f7ca32ccc15 | -16.80922 | -57.43312 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 4e4edc1a-7faa-3300-ae74-086938be2b55 | -16.80881 | -57.43704 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.5 |
| 8f28bae5-8787-3334-8c7c-559fb676e120 | -16.8084 | -57.44095 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.5 |
| ece7fb82-9479-3bd1-9c73-90dbb4ff3ef6 | -16.80799 | -57.44484 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 63e616df-c651-3c54-8857-0b16739d8035 | -16.80639 | -57.42505 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d10ac545-b647-38dc-8e78-3df4fa8b4351 | -16.80595 | -57.42895 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 27eab4fa-8f94-36f2-a69a-c13805bd77bf | -16.80551 | -57.43286 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a78aa3c9-c198-3c5d-8090-4fed7a6de537 | -16.80508 | -57.43678 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 82ef57e6-ea9d-3931-9657-835ade4f1711 | -17.02341 | -56.84108 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 3d27806c-478f-3dde-9843-a24d59d1933d | -17.01801 | -56.83609 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| c4e1c570-c3ad-316e-b234-16d66b62c24d | -17.01756 | -56.84041 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| d788e2dc-ddd6-3649-83c8-29376d3e64e5 | -17.0117 | -56.83973 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 154597ee-e328-34ba-bdcc-78fccc4170b6 | -17.00629 | -56.83472 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |


[Clique aqui para ver as próximas entradas](README137.md)
