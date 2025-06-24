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
| 1c1a0a59-a0a2-3a3a-905b-a5d76367beae | -5.97982 | -43.76078 | 2025-06-24 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97c02a02-7a69-3095-b960-41aa95266659 | -5.91764 | -43.47608 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98b8955c-c013-3c45-b2f5-97642c3265cc | -4.66223 | -41.95711 | 2025-06-24 04:23:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d586996f-e8f1-3f0a-a973-124616780a0c | -4.666 | -41.95769 | 2025-06-24 04:23:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 97fba7a4-17d6-3970-b89a-82da6f69a178 | -5.78339 | -43.62465 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e611839a-3101-3d98-b897-a5d29a5360b2 | -5.48919 | -42.14301 | 2025-06-24 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e03636c9-9f7d-38ca-92da-3f046c1d90e9 | -5.91736 | -43.47945 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d46b94cd-29d0-3c81-b721-721ac9bd128b | -4.53596 | -48.0041 | 2025-06-24 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| aebe8815-1fa4-380b-959f-85d309d1fe8e | -5.9201 | -43.46024 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 27c635c5-87ae-3026-8db0-4a82a72d0a23 | -5.92033 | -43.45963 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35a43533-5a2d-3d52-bb59-7ba2958c258d | -5.92089 | -43.47998 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33914522-ddbb-36bf-86f0-4a21ef44f125 | -4.27538 | -48.18631 | 2025-06-24 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d8a2f51-6db7-36d4-a7ec-6a8595c3f5a2 | -5.48542 | -42.14245 | 2025-06-24 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 574604da-025f-364a-b5b5-13060f41b9d3 | -2.44898 | -47.50251 | 2025-06-24 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4036f28-60e0-3a06-a342-cd1595eddf5a | -5.41595 | -47.56916 | 2025-06-24 04:23:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fae32cf-6c0c-37a7-983d-fa91ac68a3b3 | -5.91411 | -43.47554 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f23dfdf-7020-32d3-b32b-554aceadd5e0 | -5.91657 | -43.45967 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dc8ed3d8-d187-340c-adc3-7ed6b34feda4 | -5.20506 | -43.31208 | 2025-06-24 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 93432fdf-19e2-3f3a-8676-c215c347e93d | -4.68768 | -48.8684 | 2025-06-24 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca04c322-b70f-3fa8-a687-3c62311cfd53 | -5.48851 | -42.14758 | 2025-06-24 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c9090f97-305e-3711-8f8c-cbcad764acb9 | -2.44957 | -47.49876 | 2025-06-24 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 177a2044-8357-34d5-b904-25f35daa161f | -5.92148 | -43.47603 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ce537c3a-f81f-34e3-bb82-01f9cf3b3a40 | -5.78575 | -43.60899 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6eb6f5dd-57a6-361c-ba73-1cbb6e03dc2a | -5.78131 | -43.60921 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75631fd3-083c-3d33-810c-c4f8e2386328 | -5.91383 | -43.47892 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ed2cafb4-fa4b-3109-8bd1-64ea94f8315d | -5.64253 | -48.60718 | 2025-06-24 04:23:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb2bec36-2f3d-3cb1-880d-1603401b6051 | -6.00659 | -43.74902 | 2025-06-24 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44bf8d81-cbca-3419-9d82-3bb67e5301b7 | -4.54286 | -48.00514 | 2025-06-24 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ca04e0c-13a7-38aa-8c36-3e62768bf763 | -4.03508 | -48.06269 | 2025-06-24 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac32f228-2727-383d-8ce9-9791f5597ff3 | -5.49228 | -42.14812 | 2025-06-24 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fec60b92-a712-3cdc-9fda-d257d1cf41ab | -4.27599 | -48.18247 | 2025-06-24 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dfd71f44-490c-36f8-86ce-27b0853b5652 | -5.13153 | -45.03118 | 2025-06-24 04:23:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7dda2da9-7fd4-343d-af5d-1fb4e9406f78 | -4.71499 | -42.76342 | 2025-06-24 04:23:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31f27490-ec7e-3fdc-9ef9-f97fbf1baa7b | -5.98189 | -43.76191 | 2025-06-24 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5d53e2c-4b52-3d20-aa82-c5ec57191df2 | -6.14362 | -43.95869 | 2025-06-24 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2d70e2d-66ba-35c2-8962-fa6d7e83d603 | -5.91826 | -43.47213 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88b74e4d-10d9-3ca7-ba77-079355abd872 | -5.0725 | -43.7269 | 2025-06-24 04:23:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 250bcf95-ea1e-351e-be8a-0d31aec3605c | -5.91442 | -43.47496 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e0ba5c2-90ca-3b66-b55c-826fd4e5b294 | -5.91854 | -43.47155 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1aa8d820-a85e-3c5c-b0aa-ec677b5b07a9 | -5.12819 | -45.03068 | 2025-06-24 04:23:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 348f662a-5748-3ffc-9db2-f6eb628dbc37 | -5.78771 | -43.61419 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99e14467-c47b-3803-b23c-ff0127bfdda4 | -3.16516 | -52.45107 | 2025-06-24 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51a67ac7-b9b7-3faf-b430-692c1409b4d9 | -5.78516 | -43.61293 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39886c6f-40af-3b09-a2cb-cfe500f18fb3 | -5.78482 | -43.60975 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0aedba6f-2d22-3ab0-b94c-838a48909f00 | -3.04467 | -49.43504 | 2025-06-24 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad34d278-53b1-3a5d-86ff-1d0cfb5e4a86 | -5.9784 | -43.76138 | 2025-06-24 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bea41e3e-87be-3f16-ad8f-817e5778be1d | -4.53822 | -48.01212 | 2025-06-24 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bb174931-1d33-3dea-9750-eeb22a2d1d81 | -5.78543 | -43.6058 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ccf531d0-21e8-3e47-bb59-1efb6e37dfc4 | -5.97923 | -43.76466 | 2025-06-24 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3be6106d-7cd7-3d25-b808-578b7d22b5e3 | -5.78421 | -43.61367 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 366eccf2-23a7-3fc2-bf43-8e3bafb2cdd7 | -5.9135 | -43.4795 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88c71e9f-8da4-3b74-b98f-3ace44b056b0 | -4.53881 | -48.00837 | 2025-06-24 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c92df742-d5b6-3f4d-ab5e-8a809339431a | -5.07369 | -37.71531 | 2025-06-24 04:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64f49a67-b8ca-3d0e-bb74-fea81dd461ad | -5.44687 | -43.57264 | 2025-06-24 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59ed9e61-6430-3479-b305-d2951dd98952 | -5.44626 | -43.57655 | 2025-06-24 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d90babb2-9d5a-34bc-a626-74dd0652b793 | -4.53941 | -48.00462 | 2025-06-24 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 24031a63-4cf2-308b-9f68-2744ce05f963 | -2.45242 | -47.50306 | 2025-06-24 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9cc3e39d-2443-3e55-a501-64bd9d211f0a | -5.78807 | -43.61737 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10ef63b7-4386-345e-bd54-22978e8110b1 | -5.10317 | -38.29122 | 2025-06-24 04:23:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 773ad11b-bbca-3a39-8978-cab11fc023ee | -2.45183 | -47.50681 | 2025-06-24 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 69c672d8-ba21-32b7-bcdc-95c0017ad5cb | -4.54226 | -48.00889 | 2025-06-24 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 0368a6a3-e507-3573-9a21-92eb6b2e462d | -5.9778 | -43.76526 | 2025-06-24 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06dadf80-0d69-383d-b3b2-e098752f7d54 | -5.78711 | -43.61811 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25e9c43e-a6b4-3916-b8eb-9b1b6849874c | -4.53536 | -48.00785 | 2025-06-24 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a9209ca1-bca4-32f1-9e59-3972cd3b5323 | -5.78457 | -43.61685 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc97df06-bb60-3c99-963b-4df2e318e002 | -5.91795 | -43.4755 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0588940d-2dc2-3b56-afc0-93eeaa5d0a90 | -5.91703 | -43.48003 | 2025-06-24 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5992be59-6915-3bc0-b626-7423430a567c | -6.3397 | -43.74626 | 2025-06-24 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa466374-03a0-3b1e-a514-fc0a2098621b | -5.20566 | -43.30811 | 2025-06-24 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c85b53a4-14be-3c7f-8aa0-348074bf2860 | -9.32011 | -47.78787 | 2025-06-24 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deacf25a-dc2c-35ec-9405-c411383f60fe | -7.45138 | -45.56787 | 2025-06-24 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c90a6147-b51c-3be4-8416-8550b339781a | -11.09968 | -46.64887 | 2025-06-24 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 180579f9-73ea-3fdf-97ed-3c2b3af6fbfa | -12.25193 | -46.68492 | 2025-06-24 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 853ebe14-d14e-3c18-b690-8cb71436d3f7 | -9.67822 | -48.20307 | 2025-06-24 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bac6bae5-fde8-3f85-b4bf-ec85fc4d66d9 | -9.31233 | -47.79383 | 2025-06-24 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| addb996e-1563-3425-8d21-4d7281df6b74 | -13.25611 | -41.33248 | 2025-06-24 04:25:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e53db216-1267-3b21-a014-7cc19a83cca8 | -10.23544 | -44.63949 | 2025-06-24 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c7ba8b3-a800-356f-a940-73663f625130 | -7.20657 | -43.10057 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cfc43771-2c3a-3de1-863b-296eafcc6dc1 | -7.34292 | -45.35153 | 2025-06-24 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ee609d7-515b-39f5-a64b-0063ea35752e | -10.85946 | -53.75633 | 2025-06-24 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eec95176-861b-3003-b609-49fc2c06bec6 | -6.96802 | -42.92454 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ab92c0b-359d-3965-97cb-1876c3f887b3 | -10.5934 | -49.45839 | 2025-06-24 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c4cbd52f-d260-38b0-8e79-2711a45313ed | -8.55401 | -51.55257 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7a8b92a-2da1-3e85-b82d-43ddeebdd670 | -6.2499 | -44.84 | 2025-06-24 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69992054-dfab-309f-af80-c0d43bcbef5e | -12.09067 | -45.75262 | 2025-06-24 04:25:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad5d52a1-2af1-3a73-900c-b01b8c7e99ad | -13.07359 | -48.83809 | 2025-06-24 04:25:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ed3fe94c-f0a7-3f01-bf15-4c79b00d6384 | -9.31622 | -47.79085 | 2025-06-24 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40328f13-f59d-3ab0-9b54-2dcf5078fb42 | -10.50454 | -53.59012 | 2025-06-24 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0d3deaf-f503-3f74-bb8b-120d18cdd0ff | -6.6279 | -44.13091 | 2025-06-24 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 840697a8-8be6-3740-b4ff-8e9d8f739fa4 | -11.9374 | -48.42228 | 2025-06-24 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 303ba66a-3cd3-3782-b256-251de665c7ce | -10.22692 | -48.93011 | 2025-06-24 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9833a288-2c50-3877-82a2-9ae8e85c2e0c | -12.24804 | -46.68796 | 2025-06-24 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfebe9af-d09d-30cc-b182-f3cc827379b0 | -11.24795 | -49.49011 | 2025-06-24 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a65e8edc-b998-3a5e-b08b-cb12c67abcc5 | -8.33806 | -48.52672 | 2025-06-24 04:25:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddd916d9-64b6-33ca-8d76-12a0958f1a7d | -10.58321 | -49.6514 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ab7efb4-4ca6-3cf8-b457-2702c46b3d9b | -8.06715 | -43.11528 | 2025-06-24 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 1fc97cec-c293-3a2d-ade7-62e05d77b89d | -7.20293 | -43.10001 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5c77b5ba-9960-30a0-9116-2457dffbd8cd | -11.27576 | -52.46714 | 2025-06-24 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0edd6d3d-5fe9-3aee-952b-820bbe764af9 | -9.64742 | -48.56504 | 2025-06-24 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e526489b-85fa-3784-aab9-230e110e9177 | -7.31388 | -45.77658 | 2025-06-24 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README12.md)
