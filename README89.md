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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbeed4bf-1526-3d72-b5b0-afae3e09c7f0 | -9.4062 | -60.5326 | 2025-08-27 09:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 23708a88-da4b-3784-9823-1f1dcb019e5e | -9.4064 | -60.5133 | 2025-08-27 09:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4262bbd8-7da7-3d88-98b1-dc179e304eee | -8.948 | -65.9429 | 2025-08-27 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| eeea6d42-4063-3fd2-8ee5-b3195f4bb8fe | -8.9295 | -65.9435 | 2025-08-27 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| d867351e-40cc-315e-bada-fd5e3584c649 | -9.4062 | -60.5326 | 2025-08-27 09:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8168eb13-544c-3ab6-8ca4-94039e1d8190 | -9.4064 | -60.5133 | 2025-08-27 09:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 2c8d05e5-271f-360a-b469-04f5794a4464 | -8.9664 | -65.961 | 2025-08-27 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4600ff09-93ff-3443-962e-4cee1f9d0302 | -8.948 | -65.9429 | 2025-08-27 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 8f70dc84-8017-3afc-8ca3-ea98ce3b86f6 | -8.9479 | -65.9616 | 2025-08-27 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 7e167111-0377-34c5-80f5-7a34b6f1de02 | -8.9479 | -65.9616 | 2025-08-27 09:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 9202e720-de68-3152-8836-18387c1f7e33 | -8.9664 | -65.961 | 2025-08-27 09:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ea04b625-00de-3e0a-ab4c-aa8423dcaa48 | -8.948 | -65.9429 | 2025-08-27 09:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| c02eb211-2ae4-3895-8770-12ccd566b18c | -8.9295 | -65.9435 | 2025-08-27 09:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 45e887ef-95cc-35f6-9394-9b94de64d3c0 | -8.9664 | -65.961 | 2025-08-27 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e9cef0ae-6850-3afc-87da-d56412f08f4a | -8.948 | -65.9429 | 2025-08-27 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 63b8a1cc-71b0-3876-8748-b1a07114e31c | -8.9295 | -65.9435 | 2025-08-27 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 92ab57a0-dae8-36e1-8b50-54681269923b | -8.9479 | -65.9616 | 2025-08-27 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 0ad1a02c-3e9c-37c4-afa6-da101912af27 | -12.784 | -48.1543 | 2025-08-27 10:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| c90a8175-0168-3060-9864-73f9c9df15c7 | -6.4355 | -44.5764 | 2025-08-27 11:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 64ee6297-bebb-3140-bc5f-f104620bb6f6 | -6.4355 | -44.5764 | 2025-08-27 11:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 886e2b0b-3900-34d6-867d-38dc3c8d0142 | -14.1297 | -45.4043 | 2025-08-27 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| ab4d2691-b3f2-30d4-912a-1a009b647b77 | -6.4355 | -44.5764 | 2025-08-27 11:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b731078e-a195-37cd-8fb4-3b29d0db35bf | -14.1297 | -45.4043 | 2025-08-27 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d9b5bb93-f858-35d2-a4b5-b8764e768d86 | -8.9479 | -65.9616 | 2025-08-27 11:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 95f1b2b9-e980-3bcd-8537-f782def5cc73 | -14.1297 | -45.4043 | 2025-08-27 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 81db309d-3fd5-3e64-b4f6-042a8ba7b125 | -13.6102 | -48.1903 | 2025-08-27 11:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 49c879d8-dcf4-3840-9e2c-cd378a4650d8 | -13.6097 | -48.2126 | 2025-08-27 11:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a476617f-fe1b-3e97-a08e-e7134112bf80 | -8.271 | -45.1149 | 2025-08-27 11:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 37f22805-36b4-3612-9a8f-120546a8cba7 | -14.1297 | -45.4043 | 2025-08-27 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c7b41b49-c8e5-3872-aa7d-8a652701a048 | -8.271 | -45.1149 | 2025-08-27 11:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 302c9b43-e76b-31fd-a322-ff3f759b5038 | -6.4355 | -44.5764 | 2025-08-27 11:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e4edc9ba-cbf8-3f4b-a5f4-f275895b4dd8 | -8.271 | -45.1149 | 2025-08-27 11:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 378.4 |
| 430a9e6e-7a8a-3b10-b4c0-e2bd70e652c0 | -8.9479 | -65.9616 | 2025-08-27 11:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 96431bab-0788-3ec7-8727-af8f4bf7aec0 | -14.1297 | -45.4043 | 2025-08-27 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 3d3cc069-4bce-307e-87ea-8fe26899c310 | -13.6097 | -48.2126 | 2025-08-27 11:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 905e3c4a-0f50-3e20-9dcf-3d0349e77dab | -9.4064 | -60.5133 | 2025-08-27 11:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 977a751e-e4ad-3a6b-a2d1-5518a3420e1a | -13.6102 | -48.1903 | 2025-08-27 11:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f719cc1f-2826-3d0e-b188-55a6ace18ece | -4.86284 | -42.64761 | 2025-08-27 11:53:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3265e5ef-930a-3676-b463-379e90994a7e | -4.84732 | -42.68695 | 2025-08-27 11:53:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 16474919-81fc-3c7e-a530-fc6f8d7642a4 | -5.04747 | -43.39893 | 2025-08-27 11:53:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| db5c9686-f586-387f-8b83-d40cffb16f12 | -5.11587 | -43.20641 | 2025-08-27 11:53:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 3af0668e-40f7-33c3-a1aa-e6efd2d781dc | -4.88505 | -37.48405 | 2025-08-27 11:53:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b24ff6d7-090b-33cb-aeb9-a6399a09b344 | -5.43931 | -36.56599 | 2025-08-27 11:53:00 | TERRA_M-M | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 22.0 |
| f3769ace-1077-3c97-8970-cbbabcd4309f | -5.44102 | -36.55322 | 2025-08-27 11:53:00 | TERRA_M-M | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 8d81a9ee-891f-3281-bcdf-23aa8e02db26 | -5.62713 | -42.6022 | 2025-08-27 11:53:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 651d0ce0-1217-3831-9f05-f4408384a4e0 | -4.04777 | -38.91634 | 2025-08-27 11:53:00 | TERRA_M-M | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 85bc25db-e954-34ff-bf27-db05cbb6f6ae | -5.13561 | -43.22642 | 2025-08-27 11:53:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 661e24be-8a9c-34bb-8e92-597926a73aa2 | -5.43382 | -36.5587 | 2025-08-27 11:53:00 | TERRA_M-M | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 5cd4019a-23d5-375f-a397-46d445220e2f | -7.5484 | -36.75205 | 2025-08-27 11:55:00 | TERRA_M-M | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 45.4 |
| defbd16a-12d7-32f2-aa6a-c48dc597956d | -6.05015 | -43.68216 | 2025-08-27 11:55:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2d3d4936-f5a3-3287-b395-3512030d0e84 | -7.17529 | -43.83774 | 2025-08-27 11:55:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dec0a0f4-4b5e-38a3-8415-17be62de9000 | -8.45671 | -43.68811 | 2025-08-27 11:55:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 03b64e12-df7b-3ac8-a4e3-a9640885f47b | -8.08533 | -44.97948 | 2025-08-27 11:55:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 3fdd4dcc-4910-33ba-8b0c-cc7a3c3eb63e | -6.43887 | -44.57221 | 2025-08-27 11:55:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| dc79a3a5-5987-3e31-840b-e6b87a12b815 | -6.60617 | -37.31067 | 2025-08-27 11:55:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ce32ea55-e1ea-306a-89ee-6829467f1386 | -7.65845 | -42.65517 | 2025-08-27 11:55:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| f374c6c3-ebd0-3f9f-b75b-fd3b6e56a35e | -7.64644 | -42.67297 | 2025-08-27 11:55:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| dcf2640f-bf30-33eb-a4b1-ef40011d013c | -6.18086 | -44.04441 | 2025-08-27 11:55:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 67d826d5-505a-3f74-a4a9-ead6be525537 | -6.88198 | -43.60092 | 2025-08-27 11:55:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 456.5 |
| 15f0ba07-4751-3a20-93bf-d854a68fa10f | -8.45986 | -43.66692 | 2025-08-27 11:55:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 645c0d83-c3e0-3e5c-b7a5-192220e80c36 | -7.17309 | -44.87874 | 2025-08-27 11:55:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 85392e6b-37b6-3b78-8efd-9c4d69a30daa | -6.71375 | -43.09968 | 2025-08-27 11:55:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| addd70bd-5795-388d-b1dd-a442c93839e5 | -6.6078 | -37.29897 | 2025-08-27 11:55:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 8882d740-1a23-3c9c-8602-bab9e760d8b9 | -6.12646 | -44.41064 | 2025-08-27 11:55:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| eb74ffb0-1797-34bc-b43a-5e859e912d91 | -7.31619 | -39.85873 | 2025-08-27 11:55:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 67ed6622-4782-3ddc-aefb-efc6f8ff7775 | -6.12909 | -42.94934 | 2025-08-27 11:55:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| a3f30372-e18d-3074-ba6a-e85a04269716 | -8.15107 | -45.04275 | 2025-08-27 11:55:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| da0b7e3d-3c2f-39c4-905f-f3b1de2d8fe4 | -7.59813 | -43.94875 | 2025-08-27 11:55:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c263342b-c3cc-3732-b5d0-c9dbf7778776 | -7.12403 | -43.69979 | 2025-08-27 11:55:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b27b628c-a157-3049-9c9d-12a71786d335 | -6.52255 | -42.9794 | 2025-08-27 11:55:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4bcce0d6-b0ba-37ea-ac51-857e0c65dc43 | -6.35189 | -43.65895 | 2025-08-27 11:55:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 2d0916bc-5490-36c5-abaa-da3817cbfcb0 | -6.34948 | -43.66383 | 2025-08-27 11:55:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 20234daa-799d-3441-9203-e840d939a345 | -6.33962 | -43.66239 | 2025-08-27 11:55:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b2d5303b-21fb-3d23-9045-d6cf7beb7672 | -5.79355 | -43.61476 | 2025-08-27 11:55:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 47653b13-fbd0-3993-8076-df15ba7eaf1a | -7.06588 | -44.3616 | 2025-08-27 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 447784a9-0f62-3bd4-b7e8-dc7f6f776dc3 | -7.19774 | -35.00089 | 2025-08-27 11:55:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 85ecc92c-0af9-394c-8d97-2422161c076e | -7.17503 | -44.86576 | 2025-08-27 11:55:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 10339382-4f10-3519-bf5d-98816efe94bd | -6.61636 | -37.30652 | 2025-08-27 11:55:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 9.0 |
| ef7465d7-3de3-385a-a199-a018339b9e40 | -7.89173 | -44.78873 | 2025-08-27 11:55:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 03f17623-0007-3027-ac0b-f258ccd42938 | -6.87222 | -43.59957 | 2025-08-27 11:55:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 211.0 |
| 4f4c58fc-465f-3ce5-ab5e-c6dccbc9e00d | -8.08327 | -44.99259 | 2025-08-27 11:55:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 405a84cf-c6d5-3577-a8b4-b6c3da0b7c8e | -6.12457 | -43.31153 | 2025-08-27 11:55:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ff6c862a-d71b-361c-a756-0f821448f59f | -6.7878 | -44.30151 | 2025-08-27 11:55:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5a50da1d-62d1-3fe2-bfa9-ae3aec3fbf92 | -7.84814 | -37.79456 | 2025-08-27 11:55:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e181fdfc-1d45-3a15-b021-dcaa2fc37760 | -6.17246 | -44.0313 | 2025-08-27 11:55:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 13acc2f4-dc2f-3a9f-b1dc-eae66d210dad | -6.07478 | -43.99842 | 2025-08-27 11:55:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8d0b7e60-7569-3a8d-9b59-f1c7cf75b0b3 | -7.1736 | -43.84888 | 2025-08-27 11:55:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| df0c0b2a-a2df-3a95-af33-f537538453dc | -7.43548 | -42.03904 | 2025-08-27 11:55:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| b6823b2d-cfa4-3968-b3d5-90cf4e427ace | -6.19279 | -44.16253 | 2025-08-27 11:55:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 36e1cdef-fb78-30da-aa46-7f82b6d8f7f2 | -8.07849 | -44.98501 | 2025-08-27 11:55:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 1249fa41-2dd0-3eb6-9403-1b701e92880e | -8.27906 | -45.12816 | 2025-08-27 11:55:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 788.1 |
| dfa047f7-74ee-3494-ac7d-ac0154d0b73e | -8.45829 | -43.67749 | 2025-08-27 11:55:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f7f5ac3c-b213-3495-a4cf-4ee5110119a4 | -8.39035 | -47.41735 | 2025-08-27 11:55:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 38aa03b1-e91b-3c8e-9c54-b8006e20fe20 | -6.87385 | -43.58872 | 2025-08-27 11:55:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8f0f1fdb-5ac3-301e-a613-814a155610a1 | -8.14914 | -45.05548 | 2025-08-27 11:55:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 71b0de20-7a47-3bb3-974d-94202def70d8 | -7.6344 | -42.69083 | 2025-08-27 11:55:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ecc75da1-5afc-3aea-a94b-4eb92ab8fea9 | -6.09097 | -44.72209 | 2025-08-27 11:55:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 0ff3393d-053e-37d9-88c0-a5aa4954de0d | -7.20162 | -35.00699 | 2025-08-27 11:55:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 34.4 |
| 4fdcaec7-2539-3925-bb2e-faa0b74a1992 | -6.32448 | -42.87606 | 2025-08-27 11:55:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c93e0b9b-5959-34e4-9669-2f4174dda43c | -6.03385 | -44.20145 | 2025-08-27 11:55:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |


[Clique aqui para ver as próximas entradas](README90.md)
