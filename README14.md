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
| e408b534-247f-3890-853b-3596e05fc6c2 | -2.00266 | -46.6048 | 2024-11-20 01:24:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 007552ce-fa4f-369a-a8c9-c145ccc01a60 | -3.51497 | -53.79256 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3f0cc341-9de0-3f2c-a8b6-6882c7bbb5bb | -2.61397 | -51.80182 | 2024-11-20 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 586949dc-3ef6-35af-b71e-159bcdc973b7 | -3.19231 | -54.32684 | 2024-11-20 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 6c52085f-e32b-33d5-9e5c-72552efaf1db | -2.53341 | -54.0117 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9c067897-f19d-3a34-991a-537f737505ec | -2.06532 | -53.44029 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2e0c86b0-1570-3200-8e75-67a091c28c17 | -3.13642 | -49.14036 | 2024-11-20 01:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 371d7aba-577c-3093-9ce1-ffb77fbb450c | -3.30741 | -50.36576 | 2024-11-20 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 095f3af8-4d5e-3487-9677-d430e71b9723 | -3.51795 | -53.79679 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ed50bf84-7f46-34e1-ba91-cb02f449ba29 | -2.79677 | -51.79438 | 2024-11-20 01:24:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| eb131682-e839-3c71-afb9-43a4e1713fb7 | -3.01879 | -51.00562 | 2024-11-20 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b4c1ea31-fd42-3873-a9ad-471cd4a77af4 | -3.03437 | -51.53308 | 2024-11-20 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 14ee9b80-36da-3702-8a73-71b010fab392 | -2.74509 | -54.11724 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 875620d7-aa03-3e4f-aef3-96903e971b1b | -2.00317 | -46.59959 | 2024-11-20 01:24:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 551c3103-937b-3b5d-b99f-1dd552844d01 | -3.0548 | -54.41518 | 2024-11-20 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0f825b2b-911a-389d-b644-48b7fd58c176 | -2.35499 | -48.60991 | 2024-11-20 01:24:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 084e70bb-c3f8-3ade-bd32-6b6f83ca368d | -3.09959 | -53.74232 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a2a4fb43-2bfb-3607-8168-a8c8fec07b59 | -3.26818 | -50.63037 | 2024-11-20 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 540b3ec5-251a-3b2b-9ca2-0db4f1439797 | -2.82375 | -54.02315 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 054ac913-8c64-3352-8136-55b4736b771a | -2.59503 | -54.00848 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b877457e-23dc-3e7f-97de-b12404eac117 | -3.42344 | -53.28638 | 2024-11-20 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 59fe55a3-9802-335d-9d18-8c5f883743c7 | -1.90557 | -53.33377 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ae5b094a-19e8-304e-98d6-5ec399e68629 | -3.36397 | -54.09925 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4a251ca3-fb84-320e-bfba-5bdce4ecf785 | -1.93252 | -52.99664 | 2024-11-20 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9af55fd5-53cc-3be3-b55d-1618b2e4ba1d | -1.44683 | -47.12824 | 2024-11-20 01:24:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| c0f0e91e-df78-30ee-bd34-cf6dc9329621 | -3.05332 | -54.40491 | 2024-11-20 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 97ef6f9f-456b-3966-9802-347f0ba7d6d8 | -2.72543 | -49.35645 | 2024-11-20 01:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 087cb8cc-2392-3c1f-9935-6f1470a219d0 | -2.92226 | -53.06958 | 2024-11-20 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 099477e3-b609-3592-a026-6ce895fbbc46 | -2.86512 | -54.48161 | 2024-11-20 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f4091ba1-a16b-3f6c-9b58-58692e5eb468 | -3.0227 | -51.53469 | 2024-11-20 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bfecfdcc-47c1-3119-8e3f-dc9549dab636 | -2.25174 | -53.67697 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 004b769c-a830-33c7-b117-799a0f632656 | -2.74431 | -51.82329 | 2024-11-20 01:24:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 47887e59-61bf-33c6-a267-5545fe6956d0 | -3.18134 | -54.31788 | 2024-11-20 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5a46e6a5-9c13-34aa-9c66-faabe76adbd0 | -4.13528 | -53.60842 | 2024-11-20 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 86ff74b8-fa9a-33ea-8bf9-5bacb2194bcd | -2.06364 | -53.42833 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 5b3abd4d-0321-38e9-a17f-df6773be6551 | -3.45711 | -53.31066 | 2024-11-20 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7326af1b-aaa7-3ade-8f61-8659d702217e | -4.2456 | -53.66389 | 2024-11-20 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d01f6dcf-f2dc-36d9-b742-b7d07f05c395 | -3.28892 | -53.84855 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0e91f0b4-b7f4-30a1-a373-c3ec102ae09d | -2.62545 | -51.80008 | 2024-11-20 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 548e7dbe-5fc7-3718-a297-711b803f899f | -3.01298 | -51.01872 | 2024-11-20 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 489b1f04-dd59-3713-aeea-0c3db29ab0fe | -2.85138 | -54.00817 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| fd702be4-613b-3a0b-9660-724fe74cbad2 | -2.59656 | -54.01933 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 11ee3b5e-d821-3bcf-aae5-8d96775e8155 | -3.45542 | -53.29905 | 2024-11-20 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 72436e63-dd2e-358b-a96f-99cde72576bd | -3.04769 | -54.40153 | 2024-11-20 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c4929f71-5e2b-3904-96c1-05aa464185ef | -6.64129 | -47.34367 | 2024-11-20 01:24:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 27662f52-51d4-38f0-b158-bb986a35e7a9 | -2.31027 | -48.50634 | 2024-11-20 01:24:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| c391b8d3-dfb5-371f-9c53-6c3cee87c516 | -2.72186 | -49.33243 | 2024-11-20 01:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 2473e22d-050b-3c3d-9701-122926db689b | -3.1146 | -53.70609 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3f6d3bca-b1e6-3356-85e0-a831f83e99e3 | -1.71303 | -52.48223 | 2024-11-20 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 60ebb4a1-cf61-368f-aae3-a9da75802f67 | -2.92049 | -53.0571 | 2024-11-20 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| fa2af1db-001c-394c-adde-bbf7653cf2f4 | -3.06279 | -54.40351 | 2024-11-20 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1cbe70dd-7b89-3172-81a1-3dd878d8d18f | -3.1828 | -54.32817 | 2024-11-20 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c58f7a47-d8a8-3592-b2c8-8b4ffaee060c | -2.0534 | -53.42973 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9ad28c2c-a017-34f1-bac4-7f01d89ab06d | -2.27693 | -53.63784 | 2024-11-20 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 5ac021d1-cb90-3c23-a14c-d214ab90421d | -3.51648 | -53.80331 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 323383ce-3605-3359-b5b0-987f69e2b69a | -3.10117 | -53.7534 | 2024-11-20 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6f2d8f1b-c5d4-360b-8dd5-d22d185107a6 | -3.3443 | -53.30362 | 2024-11-20 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e1c25b38-0d0c-3fa6-a588-5070935a3003 | -3.00914 | -51.025 | 2024-11-20 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 0c2cbcbc-5f24-3714-a1d6-b09d75b2551d | -2.30619 | -48.47773 | 2024-11-20 01:24:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ca1e3727-8276-3535-9cbf-06fadf2a61d1 | -3.20326 | -54.33576 | 2024-11-20 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| b2924aab-b810-31fc-97f5-b60ac5cc56f6 | -2.91014 | -53.05877 | 2024-11-20 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| c65ba2d0-3888-3fb9-b3d1-5e5d53d6857f | -2.21936 | -46.47026 | 2024-11-20 01:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 9c951d18-373a-3c08-93c2-f47c1969ef46 | -2.30812 | -48.50128 | 2024-11-20 01:24:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c4054429-3143-3141-b05c-4b67a0ec611e | -2.74649 | -51.83852 | 2024-11-20 01:24:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 67ea56b2-8d90-3679-995b-2cd163bb9782 | -2.71116 | -53.17501 | 2024-11-20 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a42b3639-1bcf-30d1-bda7-537d5d48880a | -1.86352 | -56.40635 | 2024-11-20 01:26:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 85de1440-7c53-365d-9fa3-9c620487e6dd | -1.05448 | -53.09829 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 98c24cde-7b1c-3561-8e76-a2cf5157e870 | -0.78098 | -51.74723 | 2024-11-20 01:26:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1d0a51ff-ca9a-3483-8af2-d71863db8f4a | -0.91519 | -51.78913 | 2024-11-20 01:26:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b1778e04-ae64-3b93-869e-7b9551ba98e4 | -1.13978 | -51.68812 | 2024-11-20 01:26:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| beccd984-b297-37c8-be8e-83e1eda39acb | -1.04365 | -51.74158 | 2024-11-20 01:26:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5603414d-a3ad-31de-840b-b549dbcab25b | -0.30631 | -51.54759 | 2024-11-20 01:26:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0bb7df7b-9dc1-322c-a8f6-134955aba963 | -1.82979 | -55.04812 | 2024-11-20 01:26:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| adf04e8c-7b02-37b4-a547-24878115693c | -1.62896 | -52.61536 | 2024-11-20 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 998fd6a0-0263-3ac4-ac52-a8134884fa51 | -1.20092 | -53.68834 | 2024-11-20 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3e170450-9102-3fb2-a88f-fa2258075640 | -1.12841 | -54.1942 | 2024-11-20 01:26:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1f364aeb-7e7e-3961-a6d7-04f79caecf44 | -1.32245 | -52.40176 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f93bf741-fecf-3630-a60c-47ad66646d90 | -1.13484 | -53.66159 | 2024-11-20 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5da02d70-cd61-33d8-bf1a-60848a418073 | -1.54347 | -52.26187 | 2024-11-20 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c7914459-98b6-3dd4-be3e-b3abe7a7c98f | -1.64979 | -52.68283 | 2024-11-20 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ed23e0fd-73c8-35d1-abfd-974cbfa9325a | 1.53158 | -55.90426 | 2024-11-20 01:26:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0e29b3a2-781a-38ff-88c5-1007a75b4a6f | -1.31336 | -52.41796 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a3af51a0-68b9-33aa-a5a4-b99da2af8832 | -1.60626 | -54.45649 | 2024-11-20 01:26:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e7d2969-bcb7-3381-a148-3700f9dd897c | -1.19873 | -53.68285 | 2024-11-20 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 89330fcd-73e6-3cbe-9af5-b7e2bcb9b6a8 | -1.19769 | -53.66488 | 2024-11-20 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| c0e752da-3acf-35ac-bdc8-3ee7bc12744d | -1.29904 | -52.2391 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bf698d52-6bb9-3f27-b754-c9147e2cbac7 | -1.10528 | -51.74954 | 2024-11-20 01:26:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 15fe48c2-67e4-3c56-a20b-cc9492b16a94 | -1.14676 | -53.52396 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| aaac0775-e21d-3ef3-8995-c3daa0c714e5 | -1.25493 | -51.76607 | 2024-11-20 01:26:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 33ffd7d3-8c44-3c42-a7c7-4122fb725a62 | -1.47934 | -54.44407 | 2024-11-20 01:26:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 34c90e1d-ac5e-3650-a588-3dfd6f2bbfa2 | -1.61159 | -52.41589 | 2024-11-20 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 79da8411-f333-30d6-9fd5-87fa6540414b | -1.79199 | -53.60724 | 2024-11-20 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 57842556-ce01-37e8-8707-a17f78127f89 | -1.25611 | -53.37016 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| d5814568-1ad8-3567-a8e2-6da5557de98f | -1.48082 | -54.45469 | 2024-11-20 01:26:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f0e225b1-9f54-368f-8beb-172cd7086c9d | 0.36498 | -53.8184 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 263504e8-ba06-3046-8ae4-ae2ad765c266 | -1.31125 | -52.40337 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 329a88b8-6ade-3b62-9cfd-40f118cbc45d | -1.64783 | -52.66909 | 2024-11-20 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 60d2a5e1-3d31-315c-b809-24810d955321 | -0.18821 | -51.62459 | 2024-11-20 01:26:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 521c01bc-16f0-30a3-9ad1-045b383fdae9 | -1.24825 | -53.36485 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 56415b28-b0fb-3aee-9f3f-e36aff91b564 | -1.6389 | -52.68441 | 2024-11-20 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |


[Clique aqui para ver as próximas entradas](README15.md)
