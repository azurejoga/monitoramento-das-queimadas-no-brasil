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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a454fd1-802d-3149-9f8e-6184313b4782 | -13.7764 | -47.5617 | 2025-10-03 02:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e4bd3027-618a-352e-a2a1-29d5239c0546 | -7.7746 | -42.5865 | 2025-10-03 02:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 117.9 |
| 162840d5-596d-3d25-8995-6ab2b23ffb3f | -13.1345 | -47.882 | 2025-10-03 02:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 4d1fb593-8211-3ba0-84fe-6c1443c3f312 | -9.062 | -46.6565 | 2025-10-03 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| da228735-90b2-3db6-880c-32fda32acbc4 | -13.9771 | -48.1793 | 2025-10-03 02:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f033e920-ffb6-3d64-bfb9-8218f91568dd | -6.3444 | -44.3086 | 2025-10-03 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 12a9c718-549d-35c5-b60f-d1398a31af0e | -18.2167 | -53.3607 | 2025-10-03 02:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 63.9 |
| eb2d7572-378b-3fb4-b62e-03cf20003130 | -6.0605 | -44.6061 | 2025-10-03 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 65a05689-7088-3748-937f-2be47e7930aa | -11.144 | -43.4082 | 2025-10-03 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 3f8630af-8a47-3083-b58f-c1e70421d6cb | -7.756 | -42.5648 | 2025-10-03 02:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| a0148717-3b7c-3f8c-a090-0ab8025383cc | -6.0416 | -44.6304 | 2025-10-03 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 812ce1e9-a2e9-3991-8fec-8c8a3ecc648e | -6.0418 | -44.6076 | 2025-10-03 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e93ef753-98fe-3d97-aca0-493112f56895 | -5.3568 | -43.761 | 2025-10-03 02:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 49465f03-83f3-338f-b1ac-f9ddc45bbb52 | -9.9182 | -43.7212 | 2025-10-03 02:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 3a0fd212-9d2f-3f3f-8696-c72484dbef34 | -9.9175 | -50.4881 | 2025-10-03 02:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 4031316b-33a4-3f54-8bb0-bcef60461a7d | -8.6138 | -54.976 | 2025-10-03 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| d34b4183-0ec8-351b-991b-0ebcbe92fe28 | -12.6135 | -46.9499 | 2025-10-03 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1b537889-2528-3606-8c14-0bc9e12c3a0e | -12.6131 | -46.9725 | 2025-10-03 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 7391338c-2e04-3137-8c0b-db4c44253f76 | -14.9342 | -46.8965 | 2025-10-03 02:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 96d078b4-ecae-3ee5-be62-f63748783ebc | -13.1345 | -47.882 | 2025-10-03 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 6a91ea61-e4ad-32ee-98e8-cedb20c0c4a2 | -18.2167 | -53.3607 | 2025-10-03 02:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 75bbc64d-e1cf-3be4-9b36-411c5346f23f | -6.0603 | -44.629 | 2025-10-03 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 7f41c6a0-2769-3737-aa6e-a3cf8b363f4c | -5.3568 | -43.761 | 2025-10-03 02:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 71cb85fd-a744-3427-9f71-dcdf1141ac29 | -6.0416 | -44.6304 | 2025-10-03 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| c645a3ca-bfc1-3961-ba1a-85caa90f5a68 | -9.9182 | -43.7212 | 2025-10-03 02:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 52e2389a-8838-3da4-bce5-cbdf0c4ae4bf | -10.6024 | -48.7157 | 2025-10-03 02:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| b0bda931-ff6c-3687-88ea-3f0261ca94e1 | -13.1152 | -47.8848 | 2025-10-03 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c12ffcab-6fe8-3433-805a-0415477be6cf | -6.0418 | -44.6076 | 2025-10-03 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 76b2a5ae-4f05-3bf3-baca-d90da3255293 | -12.6323 | -46.9697 | 2025-10-03 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| cf17276c-3005-3977-a9e9-1c05db6212f3 | -14.9342 | -46.8965 | 2025-10-03 02:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| aa8fb3ae-7c40-323e-98b2-02095d4c755c | -13.776 | -47.5843 | 2025-10-03 02:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9f27fc30-749c-3f4d-8464-82558da01500 | -5.338 | -43.7623 | 2025-10-03 02:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ca217dbd-299f-3e40-b150-cd931a4a173f | -7.7746 | -42.5865 | 2025-10-03 02:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 933362a3-2d81-38e7-b092-53ffef69cc2e | -7.7496 | -46.2496 | 2025-10-03 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| c68481e9-b74a-3a0d-8aae-07b6fc5ea405 | -8.6138 | -54.976 | 2025-10-03 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 7a1a8d2c-3d15-3378-a5ba-90a50b626a11 | -12.6135 | -46.9499 | 2025-10-03 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 97b77a58-f612-37db-b6cc-5759dcd3e8a1 | -13.7764 | -47.5617 | 2025-10-03 02:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 62a146f0-1e2c-339f-9df2-b84c239ff6d8 | -12.6131 | -46.9725 | 2025-10-03 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| bd21c40a-4563-3334-a7f9-2debb9d20866 | -9.9172 | -50.5094 | 2025-10-03 02:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| e7477c86-a079-35e3-abf5-1a8f89380bf8 | -12.6131 | -46.9725 | 2025-10-03 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 8084821b-7f70-35e3-999c-6e222e6e30df | -18.2167 | -53.3607 | 2025-10-03 03:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 57.8 |
| ac971686-29da-301a-bf43-53cb59a9e49d | -6.0418 | -44.6076 | 2025-10-03 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 64861010-4869-3d8f-94f8-89162d0c3965 | -7.7684 | -46.2479 | 2025-10-03 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 26fdaef4-f635-3576-aba7-7d422ed4f206 | -14.9538 | -46.8931 | 2025-10-03 03:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| eefd37fb-aed5-317d-b7ff-856e0f8cb907 | -7.7494 | -46.272 | 2025-10-03 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 166215f7-c704-3870-8bfc-510c92eabd98 | -7.756 | -42.5648 | 2025-10-03 03:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 052ce463-7a4c-3ea1-b6b2-dff124fd09cb | -13.7764 | -47.5617 | 2025-10-03 03:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 6f2f1734-a8b4-32f8-8514-d5ca6ab24f44 | -7.7499 | -46.2272 | 2025-10-03 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f47b0035-07b8-3d32-b750-836f6670c27c | -8.6138 | -54.976 | 2025-10-03 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 6829f86c-99f8-352c-b3de-6b0f0adb026b | -13.7769 | -47.5392 | 2025-10-03 03:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 750ea425-42d5-3689-9de2-ab4ddae3ba93 | -7.7746 | -42.5865 | 2025-10-03 03:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| be92991f-b10f-3818-8efc-26baaf84b8dc | -13.776 | -47.5843 | 2025-10-03 03:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 308ce915-dc4e-3a98-a92c-d46b357c2548 | -6.0416 | -44.6304 | 2025-10-03 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 5bbe6eda-1a2a-362a-b9c6-72fb06314e50 | -13.1345 | -47.882 | 2025-10-03 03:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 5a15e0df-94f3-3861-ae02-70afa8c44434 | -7.7496 | -46.2496 | 2025-10-03 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 214.7 |
| dc4a9747-8b07-3c3b-a2e8-8f44ec7ee73d | -14.9342 | -46.8965 | 2025-10-03 03:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| cad4c9f3-303a-3020-b066-4fbff5fb79b9 | -9.9182 | -43.7212 | 2025-10-03 03:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| eac2c08a-ec20-3167-80fa-a35cebdad5a2 | -12.6319 | -46.9923 | 2025-10-03 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| fb8d6298-7de3-3115-9961-7c8b280adba7 | -6.0603 | -44.629 | 2025-10-03 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2935e000-2a6d-3d74-af9e-2ceb6b641891 | -12.6323 | -46.9697 | 2025-10-03 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| f19ec385-de45-3d0c-9294-146067193834 | -6.0605 | -44.6061 | 2025-10-03 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 66cf58a3-6d08-3082-a499-a8e72d090cc3 | -4.669 | -45.8066 | 2025-10-03 03:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 766.2 |
| d099b95f-395d-3661-af63-5a8762ab9783 | -13.7666 | -48.0777 | 2025-10-03 03:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 0bba7245-cf90-3aac-a74c-6ebf32610d12 | -6.0416 | -44.6304 | 2025-10-03 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2640a188-04ec-3261-959e-af3d60e41618 | -4.6504 | -45.8077 | 2025-10-03 03:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 355.2 |
| 3e31e741-63f6-3541-9ded-036553131f71 | -14.8855 | -48.3035 | 2025-10-03 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6bc9075a-cb2c-3dd2-bb50-9ed6213f9042 | -13.776 | -47.5843 | 2025-10-03 03:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 194.1 |
| c5b929a1-460e-37ec-acaf-de3598effa6b | -8.798 | -46.6616 | 2025-10-03 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| c8aa4d0e-55bb-3295-930d-33e35bd09fb5 | -11.9163 | -46.2817 | 2025-10-03 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| cbb6d4fa-66bd-3bdf-b52e-255456c2e2e3 | -4.6505 | -45.7853 | 2025-10-03 03:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 313.7 |
| 5a937653-66e0-3b5e-9059-e4c84245b7b2 | -13.9771 | -48.1793 | 2025-10-03 03:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f03082ea-5a75-3bce-9b38-a07dd2a75a6f | -12.6323 | -46.9697 | 2025-10-03 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 32a91046-9b5c-37ab-9509-275291e712bf | -4.6878 | -45.7832 | 2025-10-03 03:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0147da0c-cdc3-3b03-9ba7-bc2bd67ad06a | -13.1345 | -47.882 | 2025-10-03 03:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 7e2b6101-3406-3cd9-bfc9-80f316ce77e6 | -8.8168 | -46.6597 | 2025-10-03 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| e570f08e-dafc-374f-ba31-ce84d3a8200c | -12.6131 | -46.9725 | 2025-10-03 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 282e3752-7d1d-3ee3-8f7e-a423d5ed5e6d | -7.7499 | -46.2272 | 2025-10-03 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 9e8f5e28-a67f-3c66-91a1-bdc91ec920a4 | -7.7494 | -46.272 | 2025-10-03 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 187.7 |
| 4532514c-3e32-363e-882d-a324aa002825 | -6.0418 | -44.6076 | 2025-10-03 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5dc46eb6-b689-3f64-87f8-3d85c06aaacd | -12.6127 | -46.9951 | 2025-10-03 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| fbb5b924-e67a-31e9-8988-4bce7afd8e1c | -13.7764 | -47.5617 | 2025-10-03 03:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 127.2 |
| e3e89f58-34df-3698-b900-902317848bc4 | -10.8026 | -46.7462 | 2025-10-03 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| cdd2ea10-fd77-3905-a735-ecbfaf0f2f6d | -4.6692 | -45.7842 | 2025-10-03 03:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 637.3 |
| 050c4931-a90e-324f-b369-2749d540ae36 | -13.9775 | -48.157 | 2025-10-03 03:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| a0e1a2de-ac64-329d-9be0-06e834c8fcf4 | -18.2167 | -53.3607 | 2025-10-03 03:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2debb456-e046-3633-bdb5-bcf02603993b | -13.7566 | -47.5873 | 2025-10-03 03:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 60c82a20-fae7-363b-a1cc-b3275862b5f6 | -7.7682 | -46.2703 | 2025-10-03 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0838cbe6-f59f-3d60-8caf-c59603b32d53 | -10.8216 | -46.7438 | 2025-10-03 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 95f89079-3776-3104-ae11-a8eee69f88be | -14.9342 | -46.8965 | 2025-10-03 03:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 07f51f04-6396-37da-924b-819dcf0f5d3a | -6.0603 | -44.629 | 2025-10-03 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3f740c5a-53fd-385c-808c-788bf9fb2089 | -7.7684 | -46.2479 | 2025-10-03 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 198f12b8-6ef3-36d6-8748-4abd6673150d | -8.7977 | -46.684 | 2025-10-03 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 5a1acd0f-94b0-384b-bff7-be5dee7e3b59 | -7.7749 | -42.5628 | 2025-10-03 03:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 7cc16b41-581d-3de7-8ce0-462575fd1e78 | -7.7746 | -42.5865 | 2025-10-03 03:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 115.3 |
| e93c43ee-c4a0-35ae-8d22-9763d739a67f | -12.6135 | -46.9499 | 2025-10-03 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 4bb419c3-7d2d-3cdb-9a16-c8ddb3f69b16 | -8.8165 | -46.682 | 2025-10-03 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| f7657b5c-2bf0-3251-9a00-cdb6a1f5de93 | -4.6877 | -45.8056 | 2025-10-03 03:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 24c466ef-a962-3305-8325-a2e7045081a8 | -8.6138 | -54.976 | 2025-10-03 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| b1ca1364-a033-3cbb-b482-c224a0848c22 | -7.7496 | -46.2496 | 2025-10-03 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 510.9 |
| 4b75e84d-d240-38da-a836-f58b42921df7 | -13.9775 | -48.157 | 2025-10-03 03:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |


[Clique aqui para ver as próximas entradas](README15.md)
