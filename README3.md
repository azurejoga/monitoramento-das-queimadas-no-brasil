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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 729ad4bc-132d-34a9-a72b-13b78e2e37ce | -5.0866 | -44.8115 | 2025-11-07 02:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 01d5ca53-dd37-30fb-8343-08a90e37e80b | -9.4535 | -59.2143 | 2025-11-07 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| bd1cc16f-d42d-339f-a0a3-24aec05b21a2 | -4.2961 | -45.8938 | 2025-11-07 02:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d0c3e4b2-3f0b-30bc-9cb1-d19902627243 | -5.2737 | -47.168 | 2025-11-07 02:30:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 2429483c-90dc-335a-b225-49c45b1dec70 | -5.778 | -40.784 | 2025-11-07 02:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 7cca35d8-818f-3183-b611-c617c3c8e4f6 | -5.7777 | -40.8084 | 2025-11-07 02:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 35.9 |
| 2af4e8b6-9a17-31dc-ae14-06529dc342f6 | -5.7777 | -40.8084 | 2025-11-07 02:40:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 30.2 |
| ea8e5d00-2d6a-33a9-b4c2-e27a8a4f3313 | -5.778 | -40.784 | 2025-11-07 02:40:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 38.9 |
| eb18fbc5-8f0c-3ead-b735-72fbc403ad28 | -4.2961 | -45.8938 | 2025-11-07 02:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 185c92e9-ad41-3b62-b111-834791ab10b4 | -9.4349 | -59.2154 | 2025-11-07 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 1d5af803-0994-300f-a415-f9d5dddc19bf | -9.4535 | -59.2143 | 2025-11-07 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3c4c365b-f64f-3337-830b-6e2b1205b33e | -5.2737 | -47.168 | 2025-11-07 02:40:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 3a686ffa-89eb-353d-9e7f-198eba72b038 | -9.4535 | -59.2143 | 2025-11-07 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 0c60a113-b32e-34e9-80fa-b524e39009a5 | -5.2737 | -47.168 | 2025-11-07 02:50:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 99944c85-e7e4-32f2-a09b-4c2dc82a0791 | -4.2961 | -45.8938 | 2025-11-07 02:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 7fbbd0f5-4b7c-3590-abab-0fbff679cc12 | -9.4349 | -59.2154 | 2025-11-07 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 81778bf0-1b6c-3364-a591-333432e2e4c8 | -4.2961 | -45.8938 | 2025-11-07 03:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ca1d8109-8d93-3bba-b92d-e944b9fb371a | -9.4349 | -59.2154 | 2025-11-07 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 4e7bf4a2-364f-3ea1-917f-47abba897a77 | -5.0868 | -44.7887 | 2025-11-07 03:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 53dbea9f-8ea1-34fd-b33e-7d604bbe443d | -5.0866 | -44.8115 | 2025-11-07 03:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 7b6db98b-b199-3634-b33b-684b223dbd0d | -9.4537 | -59.1949 | 2025-11-07 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 02729312-9d54-3b96-97b3-214a2ab4ffce | -5.2737 | -47.168 | 2025-11-07 03:10:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4fe25e9d-e8a9-3996-9960-4aae817e8b5a | -4.2961 | -45.8938 | 2025-11-07 03:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9160ac15-982f-37fb-a807-0684a3bc6de7 | -7.38839 | -39.63383 | 2025-11-07 03:14:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1a243efa-2699-304a-af7a-3ed2200ef1b8 | -6.51087 | -38.73574 | 2025-11-07 03:14:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8cb75a58-fc9b-3990-b7b4-bc3f2d4d47e5 | -7.14273 | -40.45737 | 2025-11-07 03:14:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9a7e84ae-94a7-3d18-9385-fc5a3a75b068 | -7.14161 | -40.46338 | 2025-11-07 03:14:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b3d89387-82f9-38f0-81c5-9c1cf30d5001 | -6.34089 | -35.15174 | 2025-11-07 03:14:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 420fea4a-4022-345a-a893-bb4e45a173fa | -6.3458 | -35.1526 | 2025-11-07 03:14:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 22493809-e7a7-3d64-a556-f1ed5cf8e631 | -7.38196 | -39.63264 | 2025-11-07 03:14:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8622a7e1-6b06-3885-8515-61337cb2545a | -5.7612 | -40.80226 | 2025-11-07 03:14:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d2cc21dc-111f-309b-a3c8-9116312d43e8 | -7.14255 | -40.46278 | 2025-11-07 03:14:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d151c519-eeed-3f14-8690-8e12dceac694 | -6.50917 | -38.73748 | 2025-11-07 03:14:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| afb408f5-0737-3161-bd64-a93694f01d45 | -5.75409 | -40.80122 | 2025-11-07 03:14:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a078cf13-4268-34a1-99a7-f254c06e99e7 | -6.70383 | -39.9726 | 2025-11-07 03:14:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd49bd88-c3a2-3c1d-b285-d4b5ff2ef697 | -6.34184 | -35.14629 | 2025-11-07 03:14:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6b5d2b41-a948-3f70-8cd3-cb3e90a8ce5e | -6.34674 | -35.14714 | 2025-11-07 03:14:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0cc6a99c-3874-3772-8a54-f53ae8436001 | -7.1869 | -39.67834 | 2025-11-07 03:14:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c50e43b0-38f3-3c73-b937-0f1a0f0b4730 | -6.70274 | -39.97834 | 2025-11-07 03:14:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fb7c64ca-3567-3e8c-a0d6-37eee01d2834 | -6.69929 | -39.97637 | 2025-11-07 03:14:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2eabea27-6891-35b9-a3ab-13a2cb62fadc | -7.18794 | -39.67265 | 2025-11-07 03:14:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 90e4101e-1550-3193-b558-5366a8844152 | -6.69716 | -39.97159 | 2025-11-07 03:14:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ee6ba91d-add0-3865-90bb-3aa74642371e | -9.9924 | -36.0599 | 2025-11-07 03:20:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| cd12bfc0-f321-3166-9dac-7ef61554741a | -5.2737 | -47.168 | 2025-11-07 03:20:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9e68c35f-54fd-34ee-bb99-cceca3c95bab | -9.4535 | -59.2143 | 2025-11-07 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 71d3f29f-d149-3358-a509-33f11d084fb2 | -9.9924 | -36.0599 | 2025-11-07 03:30:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 92.0 |
| 8f5260d2-409b-33d3-97bf-cb099bb42cb2 | -9.4535 | -59.2143 | 2025-11-07 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 7d624783-ac4b-300c-8d14-f130ffe51663 | -5.0868 | -44.7887 | 2025-11-07 03:30:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 4f8200d1-e861-33a1-8a4a-67d5973b05b0 | -4.71384 | -46.43711 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe357aa0-662b-3b62-b700-c34284e674a1 | -3.76578 | -44.01266 | 2025-11-07 03:34:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1cca98eb-ab4f-3224-ac5e-235aeae0f56a | -6.34049 | -35.14991 | 2025-11-07 03:34:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 61695368-fb1f-37de-a901-79fdbfb4fbd2 | -4.48841 | -44.10326 | 2025-11-07 03:34:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd358311-ae6d-3054-9bc8-47c859bff0fe | -5.15279 | -41.24821 | 2025-11-07 03:34:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f521a575-e726-3f79-b92f-f771a79cb34a | -4.45038 | -46.43978 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| c3c4e013-13c0-3f43-b76d-c08cbcedc2b6 | -3.77646 | -43.98669 | 2025-11-07 03:34:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a9b7341-3ee7-3a35-9e95-71e60f36a3ae | -4.29284 | -45.88978 | 2025-11-07 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d32ea344-c574-3f5b-886c-1d02c7a6a056 | -4.29033 | -45.90392 | 2025-11-07 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c624a5e3-3df1-3985-8321-5ec9a2a63e48 | -4.70489 | -46.44718 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e18a0d9-d40e-309b-a150-9f6affdc7dc5 | -4.68731 | -43.40529 | 2025-11-07 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba136036-89d6-3b0f-98c5-971f8157731f | -4.24607 | -45.62932 | 2025-11-07 03:34:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c5c4523-6e14-3c33-9af8-00e27bc99243 | -4.44218 | -46.44561 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 36807e06-bc23-3458-b835-a4e9e06addbc | -3.13479 | -40.99347 | 2025-11-07 03:34:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 79b95066-dca6-3660-b1b3-06faf08fa03a | -4.29171 | -45.89614 | 2025-11-07 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ed8d52be-8a94-3813-aa69-3816d98e4f13 | -4.4892 | -44.09876 | 2025-11-07 03:34:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 310767fa-ddff-3c2a-a105-3b946d7751d8 | -4.46159 | -43.22814 | 2025-11-07 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9208c09f-95de-34c0-be08-035c442cdb85 | -4.68137 | -45.85319 | 2025-11-07 03:34:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 482a4468-675d-3613-898b-6d3c6097d75d | -3.60075 | -43.52283 | 2025-11-07 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fa0468c-e5b2-3d24-a754-a555199f360d | -4.67929 | -45.8467 | 2025-11-07 03:34:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da6056f7-02dc-33d5-bcca-8cbf9cf72635 | -5.1587 | -41.24307 | 2025-11-07 03:34:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3139981-2f5f-344b-bd90-742d1815f248 | -3.82724 | -45.35186 | 2025-11-07 03:34:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ca9387d-bf40-3ea0-8141-7861ac3ad10f | -3.34972 | -40.42768 | 2025-11-07 03:34:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| adec87e9-552c-3496-b77b-37aa31a7b7b3 | -4.4666 | -43.23302 | 2025-11-07 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 824fef7d-8bfd-3c01-8950-420555f91f44 | -4.58729 | -45.99494 | 2025-11-07 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b88b03c-582d-32d5-832c-7ab0b7d9ae1f | -4.24711 | -45.62336 | 2025-11-07 03:34:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ac14b67d-b9af-3be3-be16-81f8df37dd68 | -4.45107 | -46.43769 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ad5ed9df-9738-32f4-a565-19ee3c875e4d | -4.28613 | -45.8886 | 2025-11-07 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7d29dd37-3004-3757-b60a-7c8a49943887 | -3.35011 | -40.42485 | 2025-11-07 03:34:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ded1a9a2-8077-3820-805b-4997f30ac791 | -4.71267 | -46.44354 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1654a90f-66e2-30f7-be54-cf96e6d535ab | -3.76657 | -44.00808 | 2025-11-07 03:34:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9151d2d5-23d8-336b-ba4a-0c6b659b460b | -4.44291 | -46.44355 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f02b44e1-4605-3732-bd6c-7a17bd27daa2 | -4.28491 | -45.89545 | 2025-11-07 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2b4e74f1-bfec-373d-aa07-dde052da75e1 | -4.40035 | -46.44221 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cdc0fd6-e89b-31da-8048-e2e2a76fac4c | -4.46092 | -43.232 | 2025-11-07 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7905dbd0-795d-3577-be74-1530adc3e0dd | -4.4417 | -46.45041 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c169bd3-144b-35d1-8eb7-8b9d43574abf | -4.56576 | -37.96476 | 2025-11-07 03:34:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a598601f-a47b-3f37-b823-83a1977b3758 | -4.86185 | -40.64117 | 2025-11-07 03:34:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 15998037-e578-3924-8e26-01ee63b899b7 | -4.71295 | -46.4417 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53221eb1-f59b-33de-be54-0405417b5d72 | -6.3371 | -35.14936 | 2025-11-07 03:34:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ae9c243e-7cb9-3d77-8181-eb025a3a0c3d | -4.44869 | -46.45119 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e3f699a6-3d86-3611-8ac8-f51d890cfeb0 | -4.98008 | -45.06731 | 2025-11-07 03:34:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc814b07-6e33-34c7-bbcf-2dbd56023d3b | -4.71409 | -46.43516 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c68ed1df-e37f-3edb-ad59-3dbe45b47c56 | -4.71506 | -46.43038 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8268412-530a-3787-b7ae-22f9522eb71c | -3.76967 | -43.99007 | 2025-11-07 03:34:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0febfb19-7d11-3516-be3c-2bf7bff2b370 | -3.13431 | -40.99636 | 2025-11-07 03:34:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9589d8d-a2ef-3092-a6e1-86d134dae00c | -5.16072 | -41.23098 | 2025-11-07 03:34:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 814af08a-e70f-39ce-9dce-2e7de2dca223 | -3.35057 | -40.42243 | 2025-11-07 03:34:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 517d9b75-64ae-3937-9969-5f97f593743a | -3.60143 | -43.5187 | 2025-11-07 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a30bf57-c0c0-3993-af62-80a5da295de7 | -6.3399 | -35.15354 | 2025-11-07 03:34:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3210f451-e2c2-3cf2-a9ef-617c86a4a7bb | -6.34445 | -35.14682 | 2025-11-07 03:34:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 86e56be4-462e-38ee-879d-d247e0fad49f | -2.99902 | -40.23264 | 2025-11-07 03:34:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README4.md)
