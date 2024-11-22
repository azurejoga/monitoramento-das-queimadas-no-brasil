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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4254fe52-7a3e-3d4d-8c49-316620547c8b | -2.24404 | -49.00294 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8985eb56-019c-37da-8033-0b89ae73286c | -3.3935 | -54.27766 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e70c993b-f029-3327-9119-3197cb123d71 | -4.07124 | -53.72075 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67030a42-ee0b-3e54-aefd-c05157714b11 | -3.17802 | -54.32324 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c1cc3225-b4d6-3430-b7bb-f6616beecfd7 | -2.90521 | -48.32146 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37b0fa16-c8ae-31df-954e-4bccf29e3539 | -1.11738 | -53.39998 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| bb782def-5e67-3f54-8124-190ed6381683 | -1.11796 | -53.39638 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e36d300-e97e-333a-8d54-7ae28c18bcaf | -4.14073 | -54.66397 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 48ab33fd-3ddc-32d8-9c5a-6de995002703 | -0.95305 | -51.64674 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8771657e-a626-3cde-9883-355703436d57 | -3.59795 | -51.30133 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3969eb10-0bc0-3129-b9dd-26e764110368 | -4.97538 | -49.82286 | 2024-11-22 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 298b50b5-93dd-37a5-8d6d-f2295a91a6ad | -2.72233 | -46.09355 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c6156d3-e091-3677-99e6-f099926030c4 | -5.09077 | -45.94048 | 2024-11-22 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 894b259c-e053-3513-acaf-2f730dad2685 | 0.44671 | -50.77348 | 2024-11-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb069f8a-1b74-3a86-8206-db4eb911c6cb | -1.59472 | -50.44128 | 2024-11-22 04:36:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90a60baf-26b4-34ed-ba91-c8147487153f | 0.47032 | -51.34566 | 2024-11-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61110295-8c84-3744-9047-3fc29d5e988d | -1.26853 | -47.88222 | 2024-11-22 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 425bcfc8-c844-3483-96e4-6d71546ec7fc | -2.2505 | -48.42289 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a502c81-d553-3da4-bc3f-0a51d585e8d1 | -3.82381 | -52.26598 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2528fa8-5654-3fab-9019-634d88886e25 | -1.75614 | -52.6669 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 773cbb93-81c0-3b68-8257-4298c4371470 | -4.12568 | -53.97947 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5509eae2-81ce-3c62-8e32-f8568c28aec8 | -0.94135 | -51.64933 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5934a925-7b9a-3d26-a783-35f17a6dcc04 | -1.2561 | -53.36707 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea5ffbc5-fd0f-3037-b326-2d04cddb7054 | -2.84694 | -53.03764 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0103421-f5fa-345b-a2e4-7f6a5397af58 | -3.19084 | -46.55251 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c36b0a36-4425-3093-8907-feee3eb708ba | -1.11273 | -48.35313 | 2024-11-22 04:36:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cd6509d-dda5-3f50-a3ee-2a6e9a5215c4 | -2.71824 | -46.09689 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41dcadf3-c8ac-377a-b08b-a7f5f2a5d0e3 | -4.36474 | -50.8174 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c8deca1-44d1-37e8-9368-4732d853d514 | -2.68255 | -46.16643 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37fbf2d0-bfd1-3e74-be44-0bf8026fdd8e | -1.70948 | -52.48971 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74435a83-60cb-35bb-81f6-8a9cfa3485e1 | -3.18051 | -46.55091 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3fe559e-5228-370c-83f9-3e9c95f55a8b | -3.80673 | -51.99596 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5c0d588-02f1-3b68-ba0d-db8d316101ab | -2.2257 | -46.47281 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5519e0c-0918-39cb-8d4f-a1e82bde88fc | -4.11843 | -46.85101 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d377827-1da3-3efc-9d3a-a86cb22428bd | -0.04133 | -51.23529 | 2024-11-22 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca0eebaf-7b89-3e79-819d-780f1d8024f2 | -3.20763 | -42.69024 | 2024-11-22 04:36:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc228b3d-b39a-3715-b6c9-e74afdc1fb85 | -3.18632 | -51.61382 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 79f451a7-3af4-3096-8bdf-92059db99df1 | -0.80677 | -51.79697 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 14fc7f0b-61e3-3a1b-967d-5012e5ba4132 | -1.26774 | -51.60043 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfb28ab8-7484-3cc9-9233-c954b81f145e | -1.5063 | -53.13186 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff021e4d-518f-3c3c-83f8-899ccbebc0ab | -2.93616 | -48.01542 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abe1a608-6fb6-3a34-82f3-672fd401bda5 | -3.85105 | -52.35452 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3655bef9-5814-305b-bb43-3bcf586410fe | -2.61865 | -54.05256 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b991b7db-cf95-3186-b7b4-234e24b7404c | -4.57444 | -46.59262 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f03f71ab-774a-3f42-bcd6-4800cff57c3c | -2.60882 | -46.19513 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81dac2c9-6e3a-30e2-8ec5-ffb3410bab1b | -1.44302 | -53.39768 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ebeea43b-a02f-3e2e-970c-0c54fa3a5a7f | -0.80812 | -51.7882 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3f9d873c-d63b-351e-be32-17fa83f9defd | -2.26684 | -50.80751 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a52f3f5-a404-3cd6-986d-8f5d235427d6 | -2.73134 | -48.64937 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abe75e08-e064-30ac-91f9-bf9509ea3b99 | -1.19506 | -51.77468 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2829a447-6be1-385a-884b-ecb21a7a98f1 | -1.96183 | -52.99597 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2b3a1591-6967-3699-9722-d4d772ececc7 | -3.59752 | -51.55509 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ffcfddc-489f-3d69-90ff-2c7915d77799 | -2.65895 | -46.14785 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37e93897-f749-3667-a8b9-02cf5fe9fecc | -2.66759 | -46.16095 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4221c55-ae9e-3825-be3f-ba70026263dd | -1.29917 | -52.22008 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9589b683-6fd0-3c67-9f90-4aadf69f21eb | -3.27644 | -53.81691 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| eec89fd9-f314-35ec-95b4-65665f14a13e | -2.43959 | -46.53935 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a8732bd-8b64-3dba-97a4-ffd860fba500 | -1.46721 | -51.96906 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26bc8a12-5027-30ec-bf9a-a07cd77400b0 | -3.51349 | -50.81177 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fd4d492-3c2f-38c7-a9fc-6acb2b61231e | -3.28174 | -53.83577 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e69cca3-c30e-3a50-ae81-1b28d998e81d | -2.0732 | -50.32076 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 626273bd-190f-338a-a7c0-1f2e1349df8f | -1.1331 | -53.40615 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cbe95fe8-2b7f-36dc-b1b0-178eae2440b4 | -1.26865 | -54.21502 | 2024-11-22 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e31b6645-9bc6-32f2-b6b2-205587c30dff | -0.80649 | -50.95778 | 2024-11-22 04:36:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16017e1e-713a-356f-8331-b6af9f32aa4f | -3.11344 | -54.29288 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b6575a5-6432-3300-8e71-e96b97153c64 | -5.24065 | -42.6373 | 2024-11-22 04:36:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c8e932e5-3057-39de-9ee4-a58ee004f081 | -3.27013 | -51.42884 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f6c9ac2-5bf0-3309-a094-f280f8e657c0 | -3.17506 | -54.31493 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 570c371b-67e1-3fae-867c-e19bb6a87230 | -2.76601 | -52.11366 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cd91241-4ac0-338f-8876-272d22cac331 | -3.0975 | -53.74029 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e09953c-8765-3639-8551-9f9f8c6cde16 | -3.53711 | -52.79334 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b58d89b4-543d-3840-8b8b-39af9d0595b9 | -4.22701 | -40.38632 | 2024-11-22 04:36:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 37289f87-6b09-3986-a145-a798703aca6a | -4.99685 | -50.50288 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cb9504b-8486-38c1-866f-1d9af82ccd75 | -2.72932 | -46.0946 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d70deeec-c880-36c6-88eb-e05e12ab1f81 | -1.23421 | -51.78982 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5882766-3c5d-33c9-8b25-677d17de2c0b | -4.06197 | -46.41932 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cef827c7-5821-366a-a927-16d7ef995c7a | -3.81502 | -51.3535 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db4aed86-d72e-3947-a41c-e55addcfac08 | -3.48398 | -54.70104 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f377d388-617a-36ba-a067-acbf9ed84ff9 | -3.50843 | -53.79939 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2e8fbd4-4281-3c19-8edd-9a3894e6868c | -5.62794 | -44.53373 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5c807d3-5a4e-3d96-aa1c-c9608b65355c | -0.94497 | -51.7207 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30ccab60-9019-3e86-8f05-04d497bb5460 | -2.37989 | -47.83649 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f57047fd-4510-32cd-b00a-b7bbe98aa71f | -3.22155 | -54.23937 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 03ffdd9c-8f24-3914-bfe8-25bfaea0eb46 | -2.823 | -54.02204 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efc4fa0c-e652-3ca2-8ebf-b2c08c70b484 | -1.24426 | -51.7457 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29315d82-4853-3008-bc98-1ffa3daea482 | -2.72173 | -46.09742 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64d5e83b-b8b8-30d0-a1bf-98ebeb126651 | -2.92968 | -48.05692 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92617b47-872f-3409-ad4e-eb01aa323b36 | -2.15951 | -50.46267 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 503afb95-159c-3a43-ac1a-f0d21637660f | -5.09221 | -45.93925 | 2024-11-22 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f690dd3-f7e8-37b7-aeaa-149284ea9068 | -2.52654 | -46.38842 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3ea8e7b-ef86-3a11-8f8f-0bd25a969d28 | -3.31143 | -47.01985 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 69f79aca-8dfa-3dec-8c16-c017557cec86 | -2.70137 | -46.09033 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4649dec9-4145-3f52-8ece-7bf21a2d4e35 | -6.36055 | -44.00498 | 2024-11-22 04:36:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad842041-d69f-3900-905d-7cf6cd4a8394 | -3.45996 | -45.91006 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e478e2ec-de21-318f-98bc-fd17df45620f | -4.29834 | -50.15157 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 59b39631-e23f-3fec-99ed-4007f4e9e64b | 0.12385 | -49.93673 | 2024-11-22 04:36:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9de788e-6494-3d86-b6aa-d03786f42a76 | -2.15667 | -50.45841 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a599b508-3a9f-34ae-a357-ee777e3bbd10 | -2.67269 | -46.16098 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dc8e62e-487c-33aa-828b-8d121d1fb5d5 | -1.12203 | -53.39703 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4413b49-5721-364f-991d-4e2993d50e6c | -3.85841 | -52.35567 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README40.md)
