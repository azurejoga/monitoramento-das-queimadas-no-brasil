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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0073abea-8176-3ea2-9460-8986ff027607 | -5.13294 | -42.88026 | 2026-10-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65fd6c83-6e9f-3b0f-a17d-163530d3431f | -3.55904 | -54.69766 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3269c0c9-604b-3efd-a106-a05de4ee7e68 | -5.95381 | -40.92347 | 2026-10-10 04:08:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| acdb3b8e-71f6-321d-a34c-92fa54b01824 | -6.77347 | -48.66312 | 2026-10-10 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ddf3f2a1-a771-3a58-9ebf-77d805298672 | -7.03198 | -47.67461 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd40647c-d724-392a-8c9e-9c7df7562fe1 | -3.4752 | -46.07341 | 2026-10-10 04:08:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f01b4bb-dd28-3823-ade7-174a4d5570f4 | -5.7111 | -41.65188 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 37e3dc05-582a-3234-94eb-d8acf2e8bfa4 | -3.20419 | -53.85947 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81977532-8d7e-3774-bcfa-7a1d697b291a | -3.80382 | -49.94221 | 2026-10-10 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2745f42-8030-3974-ac94-63db2726bc81 | -8.98055 | -45.89324 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72bf3c1c-1aa1-3615-a0f5-0c66639d1e66 | -5.09283 | -46.22437 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63563199-09a4-3c7a-9088-6bce9206b758 | -3.30817 | -54.0118 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 849d1c3b-ac56-3eaf-8f75-4bd5289fa79b | -5.62446 | -43.65148 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f6e3200-4fed-3dc9-b9cb-74e0f911382b | -9.32464 | -46.47567 | 2026-10-10 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b07f5392-83d3-35a6-a4cc-7325b0e49fe5 | -6.08689 | -53.50174 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d570127-a6fb-3504-8711-f4c81e50f6ab | -4.0958 | -54.01715 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e4140bd1-ae44-37e2-8ef6-6c8d0ab6a8d0 | -7.2104 | -44.3408 | 2026-10-10 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25c12ef6-726e-3452-8fad-6c2c731c521b | -10.28282 | -43.9503 | 2026-10-10 04:08:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fda21cb2-9bba-3f98-b48b-cbd0de8dc753 | -7.49761 | -54.99729 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f11c55ca-6d41-3dc6-a686-13e28f0c5b5b | -3.35006 | -50.42273 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7af50bb-fbf1-31f6-af16-b7793c473f2a | -5.04136 | -49.35259 | 2026-10-10 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 32c984d8-d7af-3986-83b4-990f630371ab | -5.74271 | -45.07634 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adb2efe3-9a75-328e-89f5-dad7fa7a9a5b | -1.11217 | -54.166 | 2026-10-10 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 10eb9226-6858-3b5e-89c1-30439d16dfb9 | -5.14694 | -45.767 | 2026-10-10 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3802ae6-e6b7-31c3-b647-a02c3f86266e | -3.34698 | -50.40817 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 464be048-215d-325c-8c6d-ded9aca3325a | -6.47752 | -55.07228 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f15df668-7568-3433-aa35-a26a53b332eb | -5.71007 | -53.48088 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d84ac785-8852-3769-9f34-68319d384e85 | -6.22744 | -43.85705 | 2026-10-10 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c165ec78-bd8b-388a-a7e9-96109d924461 | -2.39542 | -51.29134 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53da2df6-d517-32d3-8b86-802f3ad950b3 | -8.36025 | -48.14815 | 2026-10-10 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5f97165-b8dc-3664-a9ac-3edc60e0be93 | -3.34388 | -50.41413 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3549b32-19d3-3ac7-8b36-774dc965c384 | -7.09769 | -41.75106 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| be840a34-2511-38f0-a907-022e7484ca9a | -3.17414 | -50.58747 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 590e6dea-71b0-31e7-84a7-000d0867c5a3 | -7.21933 | -55.07574 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a0f8ae05-e4ff-33e6-885c-9cde9bd4417a | -6.46682 | -55.50962 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ecb11080-75b4-3243-8cfe-53909a9247d6 | -3.53448 | -54.74298 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4ea6100c-ab48-3219-a2b4-3294dbf356a3 | -5.72045 | -53.49561 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03b0cb27-8fa4-3849-9551-d3d76d607451 | -5.46092 | -44.78158 | 2026-10-10 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc4d3a92-71de-3894-a620-7176a18685e7 | -3.10567 | -50.3165 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56190398-04f3-3b9e-955b-dfa778ef685e | -6.76813 | -48.66699 | 2026-10-10 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d1832344-2f01-399f-aeeb-509a05e4b990 | -3.89103 | -52.19833 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d8af4648-d6eb-3549-b555-e9e562815c73 | -3.21882 | -49.43837 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1c055d7-ebdb-36c2-8bc8-449eba218ae7 | -8.17533 | -54.71369 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa7b943f-f207-3c38-a7ba-8761e1e8f67c | -8.22371 | -46.38646 | 2026-10-10 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 85caaf5a-db36-3da4-844e-23cabba6917a | -6.69742 | -40.46588 | 2026-10-10 04:08:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c072feb6-cdd9-374b-a03c-02668a54d6b1 | -5.6984 | -49.05317 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7c00a06-de2d-3e2a-bf2c-26a11119a174 | -3.98351 | -54.4594 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bf2734b1-4e5f-3bc9-8098-97160a5f71e6 | -8.37465 | -46.90968 | 2026-10-10 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6550fd63-b8b2-3b86-aa31-aec4212c0d45 | -7.22801 | -55.14024 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f1b7854a-a01f-3909-a4ab-e9abf19e18f2 | -7.33353 | -43.99229 | 2026-10-10 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc8940a0-5e24-3ca5-a16c-41d81f7981d7 | -7.00229 | -47.72215 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1cb758d-9997-3881-aa7d-6a21cf08ccec | -6.98938 | -47.6954 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5ec67f9-d3f7-3a3b-9a64-4e018ecb9093 | -3.50178 | -54.61196 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 80f99f75-b803-3ead-b727-3fc5efb3c2c2 | -4.40294 | -49.77666 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3a531561-2b85-30a8-a9eb-3ac15c117c90 | -6.81857 | -39.55128 | 2026-10-10 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 98ad527f-af97-3ae5-b366-6b1f5dc4bf96 | -3.26393 | -54.18563 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 34ba3e51-b492-3fdc-a923-12c34f0d4996 | -7.05435 | -40.95543 | 2026-10-10 04:08:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e25e8daa-f54b-3ed0-aaee-19456dd2e413 | -7.90112 | -54.71301 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f462b189-d9d3-3416-aefb-16fcfa417f30 | -5.86903 | -37.27721 | 2026-10-10 04:08:00 | NOAA-21 | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4dcda4fd-610a-3508-9624-e4d0f04538bb | -5.88722 | -43.41096 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5557f2b7-2c9a-31a7-969f-582b742f15d2 | -3.04315 | -53.89354 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ec386533-bf2d-3fa8-9b77-3bbce58ee772 | -3.79086 | -50.79847 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f1d0298-1cd3-3dbd-afad-557a8a263499 | -3.19216 | -50.54636 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96bc56bc-59c7-3fb9-887a-ddd1ba61f71a | -3.5828 | -54.71608 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2abb0398-f306-3082-9f21-c1af9b93ae87 | -4.60773 | -49.20947 | 2026-10-10 04:08:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a42fbca2-8ee3-37f1-962b-013690d2df4c | -8.15202 | -49.43941 | 2026-10-10 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 76e07d92-e124-3bb4-9b33-7bd79c9be384 | -3.25714 | -54.18409 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8eeac0d7-070b-376f-a788-914c494209da | -2.07365 | -48.14801 | 2026-10-10 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bbaa666-5976-36c6-87b6-8aeaa0de17cd | -3.208 | -50.55256 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 417aacaf-687b-3db4-906a-c054d9711b92 | -6.06156 | -44.66381 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db796f4b-f02b-3ea7-ba09-d599d48e6247 | -7.92079 | -54.71704 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| afa02d2f-8822-3070-b63b-fd9b66e0d1e7 | -9.21464 | -45.65535 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d25db4d-ada3-3895-b9f6-ff01a6ca5309 | -7.22476 | -55.07617 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b493d0a5-af12-3acb-9592-e78b639a6786 | -3.27525 | -50.3924 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df5c48fa-a9dd-3ebd-a4c9-3278d5ad90fa | -3.28111 | -54.69627 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0d53fe44-b7a1-357f-a77e-103b878e03b8 | -6.07295 | -44.66141 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f8861ed-6b29-3055-9b5a-ca5ef9d27302 | -3.54488 | -54.7378 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f661403a-d535-3427-b940-c03c37f1e9a8 | -4.1289 | -46.86666 | 2026-10-10 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9fadec16-1af0-3483-a302-b70984654c58 | -3.1051 | -50.31993 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0dd3ba4a-fd76-3251-a9f8-cc243799fdab | -7.57452 | -45.65308 | 2026-10-10 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21304ca1-7a3f-3aef-ae18-f41ab3c43d0c | -7.90435 | -54.73193 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be08acde-e2fd-3f4a-b946-6b6dab72b649 | -8.26115 | -46.41496 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 984636c4-7f31-3e6e-bc5a-62a7319e29ea | -3.58004 | -54.70171 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a2e52dc5-3cea-3ba7-8f9c-f1ae0cd77b6a | -3.01611 | -51.01656 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c65804ef-7d07-3ef6-a374-c6ad8cc5a5b5 | -9.00782 | -44.37481 | 2026-10-10 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e33e284d-717a-31fe-9f63-fd97ba11ab68 | -7.23026 | -44.17425 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5a6b3f79-f012-3ddb-b597-499c5fc01cfb | -5.71394 | -53.47983 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d3749836-2962-31d1-9b56-828d10033e52 | -5.53356 | -43.05728 | 2026-10-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2cadd4f0-1633-394d-ad02-ca4c270fc0fb | -2.99158 | -53.91022 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13510b6f-ecc4-394a-b7b6-564cc7aa6166 | -3.26695 | -54.69421 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e036bcf4-686f-38ca-af5f-b3a361b0800b | -3.47175 | -46.0693 | 2026-10-10 04:08:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6c5130b-131c-38c6-879e-b65d61214762 | -7.09991 | -41.75848 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 81288ab6-d078-3592-a219-d5339e223457 | -2.39338 | -51.30374 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d0a944d-6d63-395b-b176-7afb2337d051 | -3.24611 | -54.03645 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c27c4f30-651b-3250-b771-d179eec51e98 | -8.53624 | -47.35524 | 2026-10-10 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d38ff0d-65d3-3900-b6ed-a2c1afc8579f | -5.79722 | -53.80778 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1454e3a6-7b89-3ad1-9354-8cfa54eae7ac | -6.33619 | -46.02776 | 2026-10-10 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fdd749c-e871-36be-beec-1f9108ad3a78 | -5.08817 | -46.20301 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 153600ce-9e2f-30c5-91fb-49df0b22b8ca | -2.57777 | -48.25531 | 2026-10-10 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 751d6ca8-dab9-3cef-b724-09dd2378ee41 | -6.98872 | -47.69935 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README37.md)
