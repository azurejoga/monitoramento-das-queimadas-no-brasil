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

## Dados Diários - Página 251

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8e8eafe-447e-3c85-9278-c3151280ad96 | -3.27674 | -44.209 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| d127485b-bd04-3581-af79-9a1bb5681766 | -3.98547 | -42.62415 | 2026-10-08 15:44:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 52abbc7e-edad-3f20-b6c8-379d5119a100 | -2.50711 | -46.04991 | 2026-10-08 15:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ddb94f49-bc16-3787-be6c-7d7779b98cf8 | -4.09134 | -44.12791 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| db22e7b8-fad3-3a0f-8c00-49ce5554c7f5 | -3.9404 | -41.54831 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a7b05aa1-c08e-3d5e-a09d-f80bddbc7a39 | -3.2914 | -42.68421 | 2026-10-08 15:44:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6745bb57-965e-3ef0-be1f-5f41b178f601 | -3.86745 | -43.02458 | 2026-10-08 15:44:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 688b7024-0e4b-313f-afe1-782c5cc86fd6 | -4.43415 | -43.90264 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 740144cf-3cc9-3856-89b8-c064ea251201 | -3.26043 | -41.84692 | 2026-10-08 15:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 221b87b0-5024-3a61-95e7-d814b7e0e6dc | -3.19816 | -42.96692 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 92c96909-85c3-3db0-8393-005e77b71b10 | -3.90956 | -44.38995 | 2026-10-08 15:44:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 2aa3eeae-73fc-3203-9773-c035e5030b95 | -3.43737 | -45.24717 | 2026-10-08 15:44:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f59942a4-eaab-38f9-9858-ab0ba6c29e91 | -4.12885 | -38.71573 | 2026-10-08 15:44:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b9ef8c2f-9a77-3d9e-8981-82ffd3dbd7e7 | -3.29095 | -42.6811 | 2026-10-08 15:44:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 48772fbf-9dbf-3510-b133-28bb905cfd51 | -3.43594 | -39.15844 | 2026-10-08 15:44:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 829f512e-5155-3e5f-908c-49fe34f6f09b | -3.86547 | -43.0229 | 2026-10-08 15:44:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b4412288-cc2e-3e37-b701-e372a3ce795e | -3.26196 | -41.63156 | 2026-10-08 15:44:00 | NOAA-21 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 69be94ac-3f46-3d6b-b148-f749634826fe | -3.02609 | -42.92871 | 2026-10-08 15:44:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 849b6eca-4f34-3ff1-9c85-5ab841fa7bd3 | -3.00998 | -43.10909 | 2026-10-08 15:44:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 33419770-192f-371b-887b-da8507c524ce | -5.09056 | -46.20543 | 2026-10-08 15:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 22844c96-8dc2-3f3b-9c0a-38f3dd7c56a3 | -3.78094 | -41.67003 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5a2c8d36-9b08-323d-ae1e-7c21079a0999 | -3.23833 | -42.58695 | 2026-10-08 15:44:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f4423bf9-8328-30a6-86fc-52727e771b07 | -5.10409 | -46.20501 | 2026-10-08 15:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 4e622e71-5674-323c-ba5b-85cc54c4e48f | -4.08552 | -44.12839 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| cfc7e6d5-27b4-3788-aa50-5b0b9dbfe9d7 | -1.52964 | -47.95548 | 2026-10-08 15:44:00 | NOAA-21 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8b97ad9a-5403-376c-a1c6-d2408a899cd4 | -4.01549 | -41.77149 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 3e43306c-2559-3e8c-9837-49b03ded8c3d | -3.51881 | -44.31583 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a70ee041-1f11-3f61-9779-4feb023c5129 | -3.52381 | -44.31155 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 844cb318-4caf-3706-8749-16432247e670 | -4.08957 | -44.11565 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 4700bf48-2966-3179-a078-0ea06d1a228d | -3.29105 | -42.28868 | 2026-10-08 15:44:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8265a0d0-e61d-35b8-afa4-4ea771cd8273 | -3.94505 | -40.72321 | 2026-10-08 15:44:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 9d027d3e-94cc-3dd8-8bfa-bc441a851feb | -3.77983 | -41.78431 | 2026-10-08 15:44:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| a7b45ded-2c03-3300-9048-86703f74feb4 | -4.51202 | -43.79652 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9681603b-efe4-3724-a6b3-38d5aa444575 | -2.87952 | -45.75158 | 2026-10-08 15:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7aa8de63-7ddd-30bb-ac98-590e134c6819 | -3.19267 | -43.37427 | 2026-10-08 15:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fb751350-03c6-31e0-a092-4e7292dc5ca5 | -5.09657 | -46.19967 | 2026-10-08 15:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| bda9bb4a-80b6-3d69-905b-1a183d945abb | -3.3044 | -43.06724 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ecf55b97-545b-38c0-b1d5-aa284fd459c1 | -1.53181 | -47.95415 | 2026-10-08 15:44:00 | NOAA-21 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| cb968dec-d673-3689-bb0a-497658f848b2 | -4.74071 | -43.31721 | 2026-10-08 15:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdc9101c-32a8-36ea-b82d-da4e1598842b | -3.20864 | -42.96662 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7c1f352f-48d8-324a-9f1c-0d0206ae321b | -3.28785 | -44.24416 | 2026-10-08 15:44:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fc2838a8-ad27-36a7-bfff-f354329aedfa | -4.36547 | -40.41432 | 2026-10-08 15:44:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 41d99b88-157e-350e-b003-221e0ac0a50e | -3.29607 | -42.28786 | 2026-10-08 15:44:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 49a86caf-dbd8-31b4-99ee-f819db0f2310 | -4.04891 | -38.93859 | 2026-10-08 15:44:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 074d5f17-f016-3b05-9691-29802264206a | -4.36483 | -40.40983 | 2026-10-08 15:44:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 0b5034fb-d5ed-3f12-90d2-b219b27830f4 | -3.11 | -41.16669 | 2026-10-08 15:44:00 | NOAA-21 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 83f0829e-8006-3d2e-90de-cfdf67c870e6 | -3.2135 | -42.96148 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6e703bb0-d746-3e7a-86d7-8a74ed491a9a | -3.13837 | -40.07953 | 2026-10-08 15:44:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 75a729db-a72d-3eae-b41f-959afe7e5b4a | -3.29893 | -39.2721 | 2026-10-08 15:44:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d24cfd0b-3dac-30bc-aacc-f1b3896cd282 | -3.90167 | -44.13232 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 212a9a2c-3e20-375b-959e-dff1b6240b9c | -3.20818 | -42.96337 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 9972f29d-e3f7-30cf-b1a9-dc65a6591ace | -3.81519 | -44.60273 | 2026-10-08 15:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| c9a97301-6db6-3aca-83d9-d639e8702422 | -3.30484 | -41.02533 | 2026-10-08 15:44:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8bd1b6fe-aa70-3a2b-8428-a187e7da943a | -3.05332 | -41.77195 | 2026-10-08 15:44:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| af9d07a6-0773-301f-887b-0a9729d24dc6 | -3.99476 | -39.30971 | 2026-10-08 15:44:00 | NOAA-21 | APUIARÉS | CEARÁ | Brasil | 2300903 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3d6c36de-46dc-3b31-83c3-76c4a4e5670e | -3.27777 | -44.20602 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0dc7eb3d-9e53-3d4c-b3ef-2aad2407794a | -3.05742 | -41.77361 | 2026-10-08 15:44:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 51fe3111-81e9-386b-859b-d8e53be84dbb | -4.09537 | -44.11506 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 84854afd-76e0-3a9e-8b04-d140ff30fe5f | -3.91481 | -44.38491 | 2026-10-08 15:44:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| aaad86eb-7ff6-36ab-bcc5-b3385e3d78bf | -2.97746 | -47.34098 | 2026-10-08 15:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f3f7649e-535d-335a-a939-c95618ecb8a2 | -4.35308 | -43.79879 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3205d01f-40cb-314c-843a-732bf85da7a9 | -3.43779 | -45.24897 | 2026-10-08 15:44:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 76371a59-191d-3991-a2c8-75bab6e78379 | -4.09999 | -44.10635 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f6556559-ba20-3b37-8fb7-bc10032b01ef | -4.50887 | -43.79791 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4cbd4850-8965-3845-a246-067faf3164c4 | -4.08781 | -44.10352 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 181.1 |
| c7bc5edf-708b-3d53-9595-4a8f9aef8751 | -3.26124 | -41.85231 | 2026-10-08 15:44:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 9c56b693-d517-381c-a3aa-ef25e95845ce | -4.14449 | -43.20687 | 2026-10-08 15:44:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 940dfadd-272c-3376-aafd-ed21dd677a05 | -4.16956 | -43.34314 | 2026-10-08 15:44:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 513d8b47-0e73-391d-ab27-6573a55dd775 | -3.28975 | -42.68349 | 2026-10-08 15:44:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0e60a390-b980-3f72-a1d8-a5f5816322ef | -3.78503 | -41.66386 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| eaecf185-bc17-3931-b460-b7db5ab6d715 | -3.20725 | -42.95687 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9e7ada6c-7dc6-3024-9fe5-428c53eddec0 | -3.90225 | -44.13632 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f644540b-40d8-391e-af52-7e2253018d66 | -3.05258 | -41.77433 | 2026-10-08 15:44:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b111aaae-952b-3d88-ba77-fa408d1c3da9 | -3.25958 | -42.94661 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 70d8fdea-9d5e-3ee4-b51b-e994327e9c71 | -3.89801 | -41.59693 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| aceef8ec-707c-3573-a5af-7d4569b29fc9 | -3.47656 | -44.39322 | 2026-10-08 15:44:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| e9ec4c23-d0e8-388c-88bf-d4e7f1a1c088 | -4.35761 | -43.79004 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f2387edb-2da4-3bcb-bd65-8e35f55f31b7 | -3.34775 | -42.49506 | 2026-10-08 15:44:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cbda9a2a-787f-3b58-ad22-40685c7d9fe3 | -4.3542 | -43.80661 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f2e15c0c-a212-3bc1-b88b-fb8a7914d145 | -3.19767 | -42.96365 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1cea89d5-4db2-35e0-b6a4-ec0fed448f49 | -4.62648 | -42.75182 | 2026-10-08 15:44:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bff3b6e0-4e5b-3f1f-8c58-23fb60b3ffe2 | -4.13855 | -43.20411 | 2026-10-08 15:44:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1f0fcd71-c8a3-3183-9f69-583f8d91ca58 | -4.36162 | -40.4195 | 2026-10-08 15:44:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 22e1cfaa-4a59-3ac0-bf87-18f622585585 | -3.52403 | -44.31094 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9c995900-a653-31d1-8587-b1ce764799e9 | -4.36419 | -40.40536 | 2026-10-08 15:44:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 13.9 |
| d2745614-707a-3ee0-91ef-344ceab26d9f | -2.87765 | -45.75837 | 2026-10-08 15:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| bf910a5f-5e8e-3a15-a2b7-fc9b03efd3df | -3.00568 | -43.11654 | 2026-10-08 15:44:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 82f5c05b-f167-38ca-b242-9dffb2b97b4c | -3.73268 | -39.53267 | 2026-10-08 15:44:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| eaaee35b-44e3-3d39-893b-8ef987092575 | -2.47431 | -46.01925 | 2026-10-08 15:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f1e1bbdb-1226-31a5-8c44-e1d24471f0b2 | -4.4336 | -43.89869 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 05753375-d258-3412-ab9e-d623ecb0eac4 | -5.09733 | -46.20525 | 2026-10-08 15:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 5aadb9e8-54a3-3f43-bb2b-c05762bd28b5 | -4.08376 | -44.1162 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 5b53a014-2dd6-3dba-9aa6-9f8583813b27 | -5.13206 | -46.02816 | 2026-10-08 15:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| b3b18fd7-ceae-3fc8-96a0-4e6f14437475 | -3.43804 | -45.25188 | 2026-10-08 15:44:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 9f075cba-35e8-360d-8dfb-e50f1e4d7f76 | -4.43511 | -43.88369 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f296d431-a965-38a4-a861-087f0ac67fe7 | -3.36151 | -43.37768 | 2026-10-08 15:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f0227085-4ea3-3921-b4ef-2eb198d6685b | -3.51939 | -44.31993 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| debac247-e736-374b-88ee-7e9250a2c934 | -1.71936 | -47.84379 | 2026-10-08 15:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f8c87339-fc29-3268-8656-3f1592bc9d0d | -3.30303 | -39.27149 | 2026-10-08 15:44:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e0ec97b8-4252-3d51-a497-5f267828c9f3 | -3.50038 | -44.27331 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README252.md)
