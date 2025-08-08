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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04216b9a-5134-356b-af32-b864b17973bf | -12.5341 | -47.0964 | 2025-08-08 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 70a70e61-6198-3875-99ed-790d9778f1df | -7.9106 | -45.3329 | 2025-08-08 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 319.3 |
| 13e376a3-fd62-3521-a4e3-ce1fe41d43f5 | -7.8915 | -45.3575 | 2025-08-08 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 392.8 |
| aed04a91-23e8-38dd-9e42-2b98591e9563 | -7.9295 | -45.3311 | 2025-08-08 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 488d2c4f-5a8b-3107-885c-837701c1876d | -11.7862 | -44.9726 | 2025-08-08 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 267.1 |
| 78d7e11c-04bb-3170-99ce-f2573d70f22e | -7.8918 | -45.3348 | 2025-08-08 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 4008081b-d032-3e20-83f0-b1a0283ca6de | -6.6154 | -45.3354 | 2025-08-08 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1eaff2c3-584d-3d16-96b2-2627e53a6fd0 | -6.2789 | -45.2716 | 2025-08-08 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 8e3af9c7-9a8a-3a1e-a5a4-7a5ef37046ae | -12.0972 | -44.7403 | 2025-08-08 13:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 8de6d2dc-532c-38a1-839a-e68aafb08d55 | -12.5333 | -47.1414 | 2025-08-08 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 89beefbe-835d-37f5-abfd-9b5f742a2152 | -12.5337 | -47.1189 | 2025-08-08 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 159.5 |
| bf7102cb-7446-3934-a503-3f22867b2a3d | -3.2196 | -41.8431 | 2025-08-08 13:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 25d791f7-c77b-3e6c-ab11-cb000e4eac47 | -7.2229 | -44.6455 | 2025-08-08 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| e842d419-4b9f-3a8d-9852-48ad9a25973f | -6.5966 | -45.337 | 2025-08-08 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 8d6e2d9d-57a3-3a84-8fbc-b063098d375f | -12.5718 | -47.1359 | 2025-08-08 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 2ea3fa5a-7400-3ed9-ac04-e112b7ba88f0 | -12.6682 | -48.1926 | 2025-08-08 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 975b4a6d-c4ba-3e4d-80d3-5ffd138fb8ab | -12.5341 | -47.0964 | 2025-08-08 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| f47fdd9a-570d-3416-bb1e-6817e4c17422 | -7.2229 | -44.6455 | 2025-08-08 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| dfa3187e-b130-3498-b923-f7b584557cd8 | -6.6151 | -45.3581 | 2025-08-08 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 5c04e61a-3fd6-3250-8f8b-9c93c851fc83 | -7.9106 | -45.3329 | 2025-08-08 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 188.5 |
| e4f528e2-43a7-32d3-a189-db5cb1077d84 | -7.9295 | -45.3311 | 2025-08-08 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6cf34211-96c9-36f2-b8a8-b0444ffd3a4a | -12.0976 | -44.717 | 2025-08-08 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 5126bc9f-12be-38d2-ae75-5a4220295a62 | -12.5333 | -47.1414 | 2025-08-08 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 153f1b56-ec46-318f-94db-cc08f7f84a9e | -9.9285 | -60.4663 | 2025-08-08 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 02cc49c5-e923-3726-aa1c-1af9970c1bf1 | -12.0972 | -44.7403 | 2025-08-08 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| e2f9ac1f-393e-3172-8f78-0219b0bdb50a | -7.2603 | -44.665 | 2025-08-08 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 02880c32-9180-3060-919b-3ce615efb001 | -12.5337 | -47.1189 | 2025-08-08 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 207.0 |
| 2ead76c5-4b52-37b2-b857-4f01a68a9eea | -3.2196 | -41.8431 | 2025-08-08 14:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| cdc9f30b-88bd-3701-9f4c-3f18cd2527cd | -12.5145 | -47.1217 | 2025-08-08 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 34aef47a-e0f0-314d-9d2c-74ac3be9400f | -6.5966 | -45.337 | 2025-08-08 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| bdd15c82-5825-37bd-8e1e-0ee8e90dcf0f | -7.8918 | -45.3348 | 2025-08-08 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 5f3aff7d-57ec-360b-baa3-dc435233b90d | -7.2417 | -44.6438 | 2025-08-08 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 352af8f8-f646-36f6-af1a-2d71b1171ac2 | -9.7173 | -61.3045 | 2025-08-08 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 8975a80f-c225-3676-907b-fa17dea1dbf6 | -7.8915 | -45.3575 | 2025-08-08 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 148.5 |
| bcc7fbb3-f03a-3b4a-b0dc-53844d613c04 | -8.4897 | -45.7053 | 2025-08-08 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 93a6e37b-f3ba-3aa2-9aef-e735d75b6476 | -12.6682 | -48.1926 | 2025-08-08 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 036c2cd4-2173-3ca2-86cc-963c70ea8d9a | -6.6154 | -45.3354 | 2025-08-08 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| a950310e-c351-38c5-a4b2-13d448d68d42 | -11.762 | -47.4939 | 2025-08-08 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| fd968e10-14f0-3795-85b3-e2a672d0b24d | -7.2227 | -44.6685 | 2025-08-08 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 983a1b51-4517-3e42-ba08-a7ae8c54f5c6 | -6.2789 | -45.2716 | 2025-08-08 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d4259ff5-04ba-3663-a417-1234e24c178a | -11.7862 | -44.9726 | 2025-08-08 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 201a4285-99de-3acf-b4c6-de26c97b8650 | -11.7866 | -44.9494 | 2025-08-08 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 997fa7c5-96a0-3b35-bdb2-3e69657f1b0e | -7.2415 | -44.6667 | 2025-08-08 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 8722d4a7-b166-3447-b3d1-d625f7a53a4a | -6.5966 | -45.337 | 2025-08-08 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 28c43185-fc75-3e42-a8f4-bcf14a08353c | -6.6154 | -45.3354 | 2025-08-08 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 31893447-2613-3627-be16-50d6f62bc74d | -7.5956 | -44.9308 | 2025-08-08 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ff2a944e-98de-3a2c-99df-b440beeca06d | -12.5337 | -47.1189 | 2025-08-08 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 7a8f6ebe-44ce-3f73-8f64-9c680b254553 | -7.2227 | -44.6685 | 2025-08-08 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| e5abaedc-1b8d-3b32-b576-a777cdf9c511 | -11.7862 | -44.9726 | 2025-08-08 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 241.1 |
| 5d6d882f-d4e1-31f5-9cf7-b43bda01506a | -6.6151 | -45.3581 | 2025-08-08 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 123bd6ca-4e5e-35a5-abd0-ba20579376fb | -12.0972 | -44.7403 | 2025-08-08 14:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 1fb0300c-c1d7-3f2a-a4bc-b7e9a8f42e1c | -6.6547 | -43.3321 | 2025-08-08 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 31770923-3965-3e3f-bd82-34e4ef70033e | -6.5978 | -43.3838 | 2025-08-08 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 58.5 |
| e068fd15-5421-3e92-a7bf-6cd25d34f5da | -11.7866 | -44.9494 | 2025-08-08 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| e12bd427-88e4-3720-83e7-b7094d4001a1 | -7.9106 | -45.3329 | 2025-08-08 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 218.5 |
| 14937bfb-972d-3c57-adc4-756bbbafde65 | -7.2417 | -44.6438 | 2025-08-08 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 13805b12-f41c-3a83-b536-37d9de38bb04 | -12.5333 | -47.1414 | 2025-08-08 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| f83783bf-bb5f-3bbb-b11e-9f022e833df2 | -7.9104 | -45.3557 | 2025-08-08 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 392dff04-9db1-3aeb-95c4-d9fffd17bea0 | -12.6682 | -48.1926 | 2025-08-08 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 4335f518-4cc6-3bee-92e3-1eb7408bb9e7 | -9.9285 | -60.4663 | 2025-08-08 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| e706ce5a-823b-3ce4-8b85-6ba1eac10e21 | -12.5341 | -47.0964 | 2025-08-08 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 85fc6fc2-8653-3195-b9cc-6859b5d056fe | -7.8918 | -45.3348 | 2025-08-08 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 43e5db70-df0b-33b1-850c-c357c32a707f | -7.2229 | -44.6455 | 2025-08-08 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 4b618464-a23f-32e7-98e4-68f0e51365ae | -12.0976 | -44.717 | 2025-08-08 14:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 322a6fa3-46d4-30fe-8147-7b9acbb3828e | -7.9295 | -45.3311 | 2025-08-08 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 6973d0cf-8759-39a4-bb01-01ab4902cf7a | -7.7247 | -45.1464 | 2025-08-08 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 7d481649-b1b8-3770-984e-d78d13fbb5aa | -7.577 | -44.9098 | 2025-08-08 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 19dadc3d-7e2d-3c8e-ae6d-8f14897ed8bf | -6.2789 | -45.2716 | 2025-08-08 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 545f3eb3-ee9d-3423-a785-13b29f61368c | -7.2415 | -44.6667 | 2025-08-08 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| d942d0a6-6f5f-3ecf-b4c8-24d164ca4423 | -7.8915 | -45.3575 | 2025-08-08 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 201.2 |
| b4bc8208-28e2-3df5-a4cd-8401637f1301 | -9.9287 | -60.447 | 2025-08-08 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| b1423afc-ea4d-36ab-9bc8-ecb1d3afef0c | -7.2603 | -44.665 | 2025-08-08 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 975c8e4c-8a73-3125-8d51-4e57b356c81b | -6.5962 | -45.3822 | 2025-08-08 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c7a63409-8461-3583-b910-df8e4eae2555 | -9.9285 | -60.4663 | 2025-08-08 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| a91d9b82-9376-3c92-af58-110fd2c2b9f4 | -3.2009 | -41.844 | 2025-08-08 14:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| b52a74a4-c514-3158-9d62-acc0b3eb4838 | -7.9297 | -45.3084 | 2025-08-08 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| f54083e6-b7df-39a7-90c4-a8d67a26dbdf | -11.7866 | -44.9494 | 2025-08-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| b9d98cf9-c1cb-3e81-a87c-7ede63d946e0 | -7.2227 | -44.6685 | 2025-08-08 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 36d1721e-08d2-3296-ba5b-dabf89df76a8 | -6.5966 | -45.337 | 2025-08-08 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 0e98ccec-ab01-36c0-8598-385591fdc084 | -12.5333 | -47.1414 | 2025-08-08 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 86e1531e-1675-31e9-9f00-d834388499d3 | -11.767 | -44.9754 | 2025-08-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 67dbffeb-1fd0-38bf-ba3c-efea810783f6 | -9.9287 | -60.447 | 2025-08-08 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 18b90ee2-7682-304a-905c-2663bf8ce63a | -11.7862 | -44.9726 | 2025-08-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 450214c3-d579-39a5-9850-82624faf7d99 | -12.0976 | -44.717 | 2025-08-08 14:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 798b1a35-b678-32b5-80e1-636078b5eabb | -7.9295 | -45.3311 | 2025-08-08 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 24e260e8-8ed6-3efb-a84a-3379ed380b76 | -6.6149 | -45.3807 | 2025-08-08 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 19f4ee75-081d-353f-ad8b-b4dd9c0798fa | -7.2415 | -44.6667 | 2025-08-08 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 8b8f2910-21e8-3989-93c6-fd77b7b1ad35 | -12.5337 | -47.1189 | 2025-08-08 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 231.8 |
| acbc0b62-686d-304e-9ed8-0ff0b502e475 | -12.5341 | -47.0964 | 2025-08-08 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 213.2 |
| 282f362a-8e48-35cb-b838-4b76ab07bc86 | -7.2229 | -44.6455 | 2025-08-08 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 01cf134e-c403-3941-bb45-d68e30e3c3c2 | -6.6154 | -45.3354 | 2025-08-08 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| debeb5ef-afcc-3858-b4f9-0fbf25ff0ce9 | -7.4076 | -59.9916 | 2025-08-08 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 40746875-b6db-38d7-8bbb-912519f9403d | -6.6151 | -45.3581 | 2025-08-08 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 3162069a-3707-3865-b5d5-d3a00405b698 | -12.0972 | -44.7403 | 2025-08-08 14:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3aec73a0-1779-3027-ae62-57d4bd014d67 | -7.2603 | -44.665 | 2025-08-08 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b9f4f2fd-1f2a-3f69-a565-6b24fd7f1c3a | -7.9106 | -45.3329 | 2025-08-08 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 3989726c-e86a-3b9e-9ede-db19fa0a6f96 | -7.3731 | -44.6546 | 2025-08-08 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 0a030e11-52cd-3141-aa37-3fa5bddee865 | -6.6151 | -45.3581 | 2025-08-08 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 188.7 |
| a440adfb-3ac7-3036-9fcd-4f3ed326e285 | -8.4897 | -45.7053 | 2025-08-08 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 230669b5-ab49-35a8-8f7f-ca0a55810036 | -6.6547 | -43.3321 | 2025-08-08 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 63.4 |


[Clique aqui para ver as próximas entradas](README31.md)
