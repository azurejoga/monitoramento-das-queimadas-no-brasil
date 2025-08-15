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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48560455-ed41-3869-9f98-c938696554c9 | -7.53264 | -61.33044 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 145.4 |
| c97ead12-112b-37d7-8974-cbc4c5c6d0c6 | -9.34574 | -62.58937 | 2025-08-15 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 27.1 |
| d19710d8-3a77-30c5-bc1f-38c11111c8f6 | -6.90673 | -59.64132 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e3aa5c0-0da3-3c51-8758-fb3fe40de808 | -7.15383 | -59.63856 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 02c14b59-d2a0-30e0-af58-008594c448bc | -7.33129 | -60.61697 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 511bfaea-b842-336f-98cb-47a9e6c7967a | -7.61344 | -63.5273 | 2025-08-15 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b1f43df6-8d9f-391c-b2e9-827e7f19d5c1 | -6.68775 | -58.83446 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| af0f0eca-255c-32ee-bb71-4c110317c2ba | -6.94329 | -59.52537 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4fdf0845-9c06-3077-9fe9-201cc741f20d | -6.10085 | -59.93919 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6d879d4b-3a71-3a92-b65e-83e40c1c8248 | -7.34031 | -60.61566 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 389ddef7-a3d5-3d86-a9a1-fa4827c8d692 | -7.11812 | -59.62908 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| dd8d5d46-9bd6-37ef-8726-340a436e8fa1 | -6.48439 | -62.94347 | 2025-08-15 01:28:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 89fbb112-6f8c-3493-9d03-a506f5c5436b | -9.02037 | -61.22143 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9ed4224b-a5e9-3c05-ab00-88d606ccd004 | -7.87762 | -61.82453 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 45305c4b-dc7a-3df4-ab76-c18e156c3d60 | -7.24155 | -57.66874 | 2025-08-15 01:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 47c20949-565f-35f4-b9c8-cd044ebd7644 | -7.60169 | -63.50938 | 2025-08-15 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 91156867-e4e2-3e20-9730-cb9f0300ffb9 | -7.32228 | -60.61829 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 6888210c-a167-31c3-9d82-a5a191bd11b7 | -8.04846 | -61.5979 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 9bcb2b9b-6fab-3a15-ae9c-344ce3c8149b | -7.08194 | -59.21338 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2dd6859b-a3f2-3d34-adda-3d02dffa7987 | -6.08352 | -59.95186 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 167.6 |
| a57c8ab5-875b-3343-8ed5-38cb99afb001 | -6.70598 | -58.81995 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 97d9f69a-d7e6-318c-be38-709a6d118f59 | -7.0916 | -59.21195 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| e9d923e5-894a-36d2-b23a-ae72f0e06196 | -7.0851 | -59.23481 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ae609ddc-850b-32c3-9740-8f680524199f | -6.628 | -60.00385 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| df259c7c-0e76-39fb-ab65-c180d995ca2b | -7.56277 | -61.41699 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| e1bdf066-1ea4-3768-9af6-03e2762c6e1a | -9.16481 | -59.65094 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 59328d9b-5349-3d7e-8bc9-2dec5141cfd4 | -7.53124 | -61.3852 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7fa26228-89e7-357b-8e67-0b89bb895902 | -8.56492 | -63.91011 | 2025-08-15 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 59ad5828-aae4-32a4-a4ce-91bd718582d9 | -7.53388 | -61.33936 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| cb832ed9-6884-39e2-9475-4d5b34d79de2 | -6.93002 | -59.53323 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| fad1147e-b2fc-348e-b1fb-5c247aefa603 | -5.457 | -60.14707 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 4dc1dddd-6893-3e7e-9c6b-846b6ad1ca8d | -8.10452 | -61.19633 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| aa8e2f98-b224-3530-963f-9b65fb26926b | -9.15983 | -59.66749 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| a612ed32-18cc-397f-aeac-686a85e539ad | -5.93507 | -59.93463 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0712b4a7-4aac-32cb-8970-3eccd4cc099c | -6.99979 | -59.97914 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 39b61c29-2959-3f2f-b2d4-96e34b87103b | -9.16623 | -59.66068 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| c209458c-66c1-373e-8b8f-b38bc24387ad | -6.0692 | -59.95992 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| eed110cf-0499-3a40-aa0b-8a05971cf777 | -7.52113 | -61.37756 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 710e8451-c921-32cb-8d91-4c132a1f366a | -8.92262 | -60.72866 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e58f3d73-cbb2-33e6-afcc-b86fc785c577 | -7.24263 | -59.99123 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1334d0b8-4a8d-32f3-9f4c-f6004754273d | -6.71594 | -58.81842 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| a64f0db7-dcf6-3c9f-954f-bec860b6a18d | -9.54278 | -63.5851 | 2025-08-15 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 05cc9d5f-0a93-3b80-ba6a-250e3a58758a | -5.4503 | -60.14425 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| b2e80203-7738-3936-b520-dd0b3afff91b | -7.45931 | -60.41524 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bcd893b9-6b41-3cfb-bc9e-9216e355eebc | -7.09293 | -60.03548 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7ef0c9d7-233c-3913-b359-7a3725913579 | -7.961 | -61.76104 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 043adb8b-7616-39d3-9ea8-c944025efa4a | -6.08063 | -59.93189 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d9e0fda1-04d4-375b-8276-8b57a4210872 | -6.92198 | -59.54492 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a83b6867-6b87-3288-b212-51e9bd4fed40 | -7.96223 | -61.76991 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fd5a24b3-c27a-34a3-bf19-3a55e681b5f7 | -6.63367 | -59.99713 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 821d8468-3e8b-314f-ac70-639e9883d353 | -6.48315 | -62.93443 | 2025-08-15 01:28:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| e1bbb18e-3c40-3fc7-b801-e2d660a41d9d | -6.70764 | -58.83142 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| e55fa106-f035-3f55-b6ee-1cb590558b7e | -9.54145 | -63.575 | 2025-08-15 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 7d45d6e9-8cbf-3fb3-baec-63bf3276ea9a | -7.52502 | -61.34063 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 72814ac0-9102-31da-b09e-3b91a97d48bf | -6.71759 | -58.8299 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 14c8ac6e-48e7-327e-85e1-b32be1018f86 | -7.3326 | -60.62621 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c70ddd86-b73f-3a12-b279-0b27b6646a6c | -8.10327 | -61.18739 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.5 |
| e75a09f7-d0b9-3d8b-b9cf-afe3d09e98c8 | -8.55547 | -63.91141 | 2025-08-15 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a9509038-fa16-33db-a232-2cdbbb56a994 | -6.63512 | -60.00708 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2cdc43e5-d8e4-3a14-80df-38915339a5f1 | -6.66617 | -58.82598 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 76ab33d6-6033-3b02-8bf7-3d8d8b112993 | -7.52377 | -61.33171 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| da43d188-c109-39be-9bde-7706a828116c | -7.80215 | -61.34629 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 35744587-9111-3d20-80de-c97b2a777fd5 | -6.69603 | -58.82148 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 418f6a37-a753-36f7-a547-1b07b7863b93 | -7.60298 | -63.51897 | 2025-08-15 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 89a76aab-4293-3405-a2e0-ad2630b6354f | -7.30424 | -60.62091 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| d7e39a52-7459-322a-a416-f737e660966a | -9.16906 | -59.68011 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 8ffb0c4b-ab18-32a8-829d-344e734f9e5d | -7.4233 | -60.03198 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3cb33af4-d21a-3be6-ba72-88bcfc77f91f | -6.72917 | -58.8398 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| cf997d04-1e14-3368-a4a4-9b12d0558039 | -6.66448 | -58.81452 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 410c1076-afd4-3270-bcc3-54b55e18ac52 | -7.31456 | -60.6288 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 5844a967-e494-352e-b1d6-ef3af4488a5c | -6.99393 | -59.98592 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ad2ceddb-864f-36f2-ad58-89316437172a | -7.95977 | -61.75217 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 814aeac7-2191-39c7-a224-4d79107554cc | -7.95216 | -61.76231 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f5ec8304-f93c-3611-a204-4c1ceb02d258 | -5.92567 | -59.93602 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0a93c045-731b-3730-ae92-ffe98169f6e1 | -8.90091 | -60.5741 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72d84bdf-43ae-3db0-b49d-ebf8aaaad3e1 | -9.16397 | -59.69664 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c7a79cb1-dd91-3618-bdc1-48fc9b385976 | -7.54361 | -63.4847 | 2025-08-15 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b7f0c7ab-8ecd-3c66-adde-8c8d5def6d94 | -6.72754 | -58.8284 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| fd07bd9a-aa82-3be0-b153-02067c1292eb | -9.15845 | -59.65777 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 981a9c08-27ca-3111-93a7-365c5c87c50a | -7.06989 | -59.22104 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 39b4ba87-66aa-384d-85e9-c919fcd0169c | -7.34161 | -60.6249 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| da893c73-00c3-3b4a-8b27-1bc4754025eb | -5.45556 | -60.13712 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 5b190e09-681d-39b4-8aa2-9534b70bd84f | -6.11024 | -59.93785 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 504cc3dc-f44e-39da-b509-ac7b9ed94e17 | -7.12755 | -59.62769 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| acbb2ede-d65a-3436-b875-07ac372d556e | -6.90527 | -59.63113 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e518324b-1d6f-3273-8b1c-de71f112114b | -7.96361 | -63.46428 | 2025-08-15 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 56970bb4-e095-3c4d-940e-7e2d6edae2ec | -6.92051 | -59.53457 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 017038e3-7ee5-36ff-91c8-1b64f53bef5c | -8.55822 | -63.85913 | 2025-08-15 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 224e1973-a4c8-33b0-bcc4-8eba27eea7b3 | -6.08497 | -59.96189 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 695724a8-dee8-3cc6-bbc9-8ce4eae7be0f | -6.94758 | -59.99284 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7b17162a-167c-3a54-8ef0-18dd4daef47a | -9.63523 | -63.09363 | 2025-08-15 01:28:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8cfdb249-c9f7-342b-a7b7-44a1436a5746 | -9.16121 | -59.67722 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6805809a-f1e9-30fd-b4c3-f63607c6086f | -9.15476 | -59.69799 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3479aad8-368b-3f8e-9baa-ad53f11aa9ba | -8.11214 | -61.18611 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4ad8392a-2c79-3328-928d-b24a8c0431bf | -7.01564 | -59.8256 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 59452214-23f2-3c17-9eb7-94ec8a09907d | -9.16259 | -59.68695 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 51fb1283-06af-3a80-8e65-022c2c8274f5 | -9.34449 | -62.58014 | 2025-08-15 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dd72280c-65b2-38a6-bbda-bb7246501aaf | -6.94898 | -60.00262 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 6e3bbd46-7688-33e6-a46c-2aed3b8f8234 | -8.10201 | -61.17845 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 546d0bc3-16d1-3267-99c6-b2b8957e2399 | -5.4489 | -60.13428 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |


[Clique aqui para ver as próximas entradas](README12.md)
