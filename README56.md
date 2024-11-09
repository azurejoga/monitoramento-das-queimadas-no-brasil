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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6f102bf-f806-305a-a733-aa611b05cda5 | -3.9545 | -48.99581 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d892dc3-fadd-3a97-ae3a-0918af693773 | -5.71981 | -42.71312 | 2024-11-09 04:33:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 609c2ae1-792e-35ea-96cc-226845e081f7 | -3.26521 | -46.31647 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2dd6d5c-0cc2-3dd1-acef-0bf3423efa57 | -4.20313 | -48.54605 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 9bb2f5e9-9b61-37c8-a7dd-243435677107 | -5.13574 | -50.6093 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0943854-dc68-363e-87b5-a5f5bce0297f | -3.78206 | -46.49307 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67ea8273-7582-3d57-a52b-8147ede550ee | -4.35246 | -46.82759 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97af2ef6-55f0-3f81-b1c9-495f229a953d | -3.01264 | -53.43453 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74d8df61-2666-3a3b-b212-c502b6fb8af7 | -5.20784 | -46.10799 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e4cc068-eca4-387d-ab91-d0a4b51a09d5 | -3.28179 | -49.6291 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a223fe77-1864-322e-b8e6-0bc5eefeda62 | -3.62524 | -54.10675 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d34d2ba-3d4a-3a31-8fe4-80f38c9e3d83 | -4.22146 | -48.5381 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7250b3b-b7a1-33ac-b549-fa4896bb1d78 | -3.09336 | -50.24592 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4e7a7d39-913c-3678-b6c6-7ea57ff0795a | -4.14261 | -46.90826 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08bee963-73e9-3b7a-a2f3-0c776a98a97a | -3.25609 | -50.18307 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 97c09623-4a47-355c-8c08-66e25f7f6120 | -4.08116 | -48.32613 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08bcd654-73dd-343c-b1ba-5f12bcb0615a | -3.14153 | -52.97095 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 714b1d9b-0d47-34e4-9dbb-3e2677caf4e4 | -4.23601 | -47.55421 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb7effde-d35f-32e0-865b-7f4fc49153f1 | -3.85148 | -51.24261 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fe58f02-b5ed-3b7f-b03b-c0e3e50263be | -4.72385 | -46.75701 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1cb883e-a36d-34a3-a90f-e578e4979709 | -4.89364 | -48.61134 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8179edce-dcb2-3e91-a548-76b4a300c3df | -3.92804 | -48.3268 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a000fdc8-c4a7-300d-8236-e0b457c3e90c | -4.53463 | -50.35425 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19a8b690-d9c9-3f1f-8244-0bd06d6ea766 | -4.85922 | -45.74886 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e5fd8c9-5af0-3921-bd27-fa774c54f658 | -2.30896 | -53.98149 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7741c9f6-9dfe-3e66-81f4-f10cdbca3f11 | -2.43717 | -53.66232 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f4f89c7-4c8a-3d4c-a30e-a01a86849811 | -2.83565 | -52.9034 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40fa8109-e088-3d96-928a-9435be919a78 | -3.06585 | -53.90399 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42426f2c-bc2f-31be-8727-19af68ad8ece | -2.86823 | -50.40663 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 79a7d211-a5ef-313f-a81a-447001aad187 | -4.5193 | -45.67915 | 2024-11-09 04:33:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 180278a5-058a-3731-ba11-2ba003c05da2 | -3.14947 | -48.58023 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f58ccd8-a96f-3e0d-a744-d441e380b46e | -3.47914 | -50.37888 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1419c5b7-fc26-34af-9441-ab07b768be43 | -2.88475 | -49.38524 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 517d53d5-d9c5-37bd-a4fd-4c527edf9138 | -3.82374 | -49.85667 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| e6846e4b-0c12-37e7-8805-625eed6eca33 | -11.08424 | -43.34627 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| cefeab8e-5724-373b-b997-40f9a4652a9f | -4.72241 | -48.31659 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2178915-0822-39c4-b22f-85210b0b5c89 | -2.38465 | -53.74356 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e2c4c27-c209-3b49-9cc1-3aae30dfabbf | -4.13707 | -46.90031 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 095181c7-948e-3904-b384-c7a06632a226 | -3.23829 | -50.27166 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 809558fd-ff95-3779-bf1d-91747a7cdeeb | -3.98315 | -49.98835 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b927e823-1c3b-38aa-8556-f807bb5cbb50 | -2.86213 | -50.31779 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f4a8c0f0-6cc0-3032-abe0-4a65e504b9d6 | -3.02522 | -48.11715 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c95b232b-fe90-3f1b-af05-b5e5b9bdd215 | -3.83585 | -50.05025 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99e5d15b-df5d-32b1-be7b-fb7a344c6760 | -3.95309 | -48.16659 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bea9eaeb-c4ae-3518-badb-4b70ac985715 | -2.58628 | -54.01075 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85cf9941-bd87-3e64-a6c9-44323db8ae0a | -3.44435 | -45.99023 | 2024-11-09 04:33:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 567f4328-3aa1-3819-a6fe-2c7964608466 | -3.23436 | -46.53635 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54863df7-6cb4-3898-8c95-6eee363b3f75 | -3.17526 | -53.85334 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7fa371de-1272-3f5a-b5ef-e88f8585cd4d | -3.25035 | -50.45053 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 182c9fb4-3a90-33c8-8805-588db46063ee | -3.40652 | -50.01318 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f32eabe2-8f03-3f5d-8b56-bc14a8ecc606 | -4.06317 | -50.0121 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fda4e113-94b8-31c4-a3d7-4d0f910e47ce | -3.7504 | -52.09311 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eacb0927-6274-3631-9b0e-0e14841eecd5 | -3.27038 | -52.74032 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4df49442-b9c1-30fe-b1c3-44f524f44fe8 | -3.24471 | -46.49173 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 424736ca-4437-3241-9b99-2f6b78599ec9 | -4.58857 | -37.80598 | 2024-11-09 04:33:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 380fbeb8-1c83-36e3-8f5c-eb20ec7ffcb8 | -4.39547 | -47.64589 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ea865db-7a3a-36ab-aae7-0297707c1af2 | -3.24687 | -46.47785 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f35e226e-371b-3708-b310-70eeb314243d | -2.93698 | -52.53516 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d754d87-6a85-35e0-895c-67ee03f4cbef | -4.71726 | -46.44685 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54d91837-dd21-3066-b704-434a1cf98d88 | -3.83484 | -50.03394 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 332018cd-cf66-3a28-83ef-34b7d17e815c | -2.87011 | -50.32618 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3e61491-f29c-34ff-9945-66d93bf2a89e | -4.11524 | -48.49989 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 78d1224a-6988-3320-b49c-a3530cf96faa | -3.60085 | -47.35239 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fecae388-da9a-34c5-af61-fc83249fab85 | -3.40767 | -46.05695 | 2024-11-09 04:33:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21db0de8-4375-338b-b3d6-81fec1cbe1c9 | -4.30574 | -46.27103 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 78888b5d-f747-3507-b4b5-8fd2fccf3795 | -2.25136 | -53.66929 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6af38d85-cff2-3641-b641-18ab64308be6 | -3.27452 | -52.74098 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2356d421-8628-31b0-b3f5-714982fe5886 | -3.53024 | -50.32718 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47ab21ba-ecd7-3f90-92a9-93fc3e365983 | -4.00569 | -49.02225 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5ad9300-01e1-346e-a3b2-ea033dcce989 | -4.34382 | -49.7718 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20987df5-b729-3699-92a8-b6cb5fde7152 | -3.12106 | -50.14227 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1ff58490-546d-3330-8d80-5eef44a324c2 | -2.90335 | -51.47034 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 164feb72-1c63-31b5-958e-0a491224ff52 | -5.65426 | -42.7322 | 2024-11-09 04:33:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 415540c3-6126-364e-b6cb-c957cc1e98f4 | -3.11595 | -51.10673 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95892f50-dc74-39af-b5b8-1fa6efbfc908 | -3.65464 | -50.14042 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f51801b9-1d5d-3f2d-af60-e29da042382e | -2.97107 | -49.34869 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ce4ccc5-bac8-3732-9f05-bc4c92f6ea66 | -3.98044 | -46.41948 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7036c0c8-f1e3-3bf4-b5fa-17e25dd18495 | -2.58749 | -51.92101 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a99a29b-b1db-3239-b59d-2a263fbc7a81 | -2.8891 | -48.28976 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6d3d34a3-a5e6-3942-a7d0-c59383a8e394 | -3.67058 | -54.23451 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ca080c7d-efc0-31bc-aca1-343a0706600e | -3.63358 | -50.18216 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| eb82af96-6326-3993-abf9-431e5e3b02cc | -4.70643 | -46.3837 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 058927a8-f036-31d2-90c2-8db726b8b099 | -3.45953 | -50.18056 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 925287aa-f50c-3ec1-9d57-bf8f5e93f7e2 | -4.12643 | -46.8597 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfbd2ca6-bcd7-3a75-9469-253b51683f5a | -4.1139 | -46.89672 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2a67f0b-150b-39cd-bdbb-e1165dc038ae | -2.86509 | -50.32245 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82798a37-091f-3457-9e98-fc6487e2677e | -2.65238 | -49.89664 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| effc977e-3ee9-3e6e-82d2-c11037ff7b1e | -3.9754 | -46.40788 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 849c9066-035a-3dc1-a0f3-b5016e96f402 | -3.9824 | -48.15344 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d60471f-fadf-3402-b3a0-7a48311f5dbf | -5.11349 | -47.14108 | 2024-11-09 04:33:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9ea8c3ad-411b-3432-a0e0-46ec6cd3beeb | -6.23157 | -47.2766 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c76a51eb-bb78-3919-8d01-bf978183145a | -2.67193 | -49.88748 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32b12a67-8a57-39ec-8b3e-ee2378612ccb | -3.02839 | -48.03207 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 202d7ee1-a012-35ef-8de1-a0766938757c | -4.39711 | -50.97565 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86235281-2ec9-3f5a-9fc6-b47a57030451 | -3.95983 | -46.70572 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4374ed2-3220-3da8-bbd4-fb6d815507a9 | -5.20002 | -47.45918 | 2024-11-09 04:33:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73098a23-2ed4-39d6-b62b-9f0e09da13ca | -4.20586 | -50.62122 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 69e03805-df66-36ce-80f8-2ede72141643 | -2.84234 | -52.54707 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2fd313d-9191-3b3b-b754-44eca9254cf1 | -3.65235 | -50.13192 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49b048ec-08b8-37bb-9a69-96022044826c | -2.97647 | -50.29522 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README57.md)
