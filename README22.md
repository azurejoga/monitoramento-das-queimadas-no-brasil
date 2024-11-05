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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d678bbac-b5d4-3a3b-a137-4d51c1a4c30c | -0.68356 | -51.67214 | 2024-11-05 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a53b8361-1d55-3e80-b965-9811895606b9 | -2.27596 | -46.83422 | 2024-11-05 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9a5b7f9-08ca-320c-b125-c12ba0da2b6e | -2.27152 | -46.83355 | 2024-11-05 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c06f1c9-ada8-37b3-98d8-9449ede4bf46 | 0.26351 | -51.32711 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 831c9809-2703-390b-91c6-fef87e71b511 | -0.68131 | -51.66454 | 2024-11-05 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4ae85de-6f48-3dde-af0d-b560c522a9f2 | -2.2722 | -46.8292 | 2024-11-05 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4660480-ac7f-3f2a-9b5a-5e2ae7b4633c | -0.73996 | -51.70621 | 2024-11-05 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 050f9130-ad6f-37cc-80bb-16a27785d43f | -1.22383 | -51.75905 | 2024-11-05 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6f3b57d-c1e4-349e-88a2-ba28bd4290eb | 1.40165 | -50.72093 | 2024-11-05 04:53:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef37c094-7275-37c6-a822-8381a7ad316c | -1.32703 | -52.5331 | 2024-11-05 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73ae5f74-6205-3245-bd5a-f4c574540d75 | 0.47994 | -50.27921 | 2024-11-05 04:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff2b3765-0c08-3a27-8189-e671a45c9154 | 0.20139 | -51.07505 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 487ae620-14cc-30a3-8f37-8d2a5f89f9e3 | 0.04428 | -49.55529 | 2024-11-05 04:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2def73b0-67ef-3197-ae1f-7e95310fe6e1 | -1.64282 | -50.4355 | 2024-11-05 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7524b3d4-3629-3de2-b2fd-fd00d7e17ce9 | 1.78748 | -50.43311 | 2024-11-05 04:53:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af75667d-05d3-3790-9ac8-d76848b3c694 | -0.68076 | -51.66808 | 2024-11-05 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48c1ba90-6302-39b8-baac-445f688ea346 | -1.03931 | -47.79149 | 2024-11-05 04:53:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79f7cbbc-fbd8-30fc-b806-9a8982a5d64d | 1.77723 | -50.43471 | 2024-11-05 04:53:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 779de74b-b176-341c-812b-5acc18af764d | -1.22047 | -51.75853 | 2024-11-05 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28e98325-58f3-316c-8b5b-0d48637d476e | 0.07051 | -51.10986 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55168689-a15c-3ebb-bbfe-f9e32a12390d | -1.32426 | -52.52914 | 2024-11-05 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95b13d8d-da23-31c3-8b4a-2308ab6fab20 | 0.24904 | -51.33615 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efad2587-6d0f-3ae5-98b1-7aa2d32bbfe5 | 0.17687 | -51.4456 | 2024-11-05 04:53:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4f9299c-cb32-3de1-badd-0e7c6d9ad15c | -0.13603 | -51.26728 | 2024-11-05 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74a18eb6-b416-3bd1-82dc-808b8dd986b0 | -2.23137 | -46.67836 | 2024-11-05 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a4a1c35-a20f-3c93-a067-0e50b8930a7c | 0.93417 | -52.00044 | 2024-11-05 04:53:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8979827e-1cbf-3917-bd0f-c29591fc499a | -2.27664 | -46.82988 | 2024-11-05 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8f0e524-842c-3814-9293-fc6910eeca92 | 0.20817 | -51.074 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a35f618-c98b-33e4-bd53-a909fe63c975 | 0.18667 | -51.00295 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e00d58bc-468a-3e0d-b351-4cf396143d1d | 0.18245 | -51.43748 | 2024-11-05 04:53:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba8e30d0-838a-3ed2-9f71-5d3b67724d71 | -1.32757 | -52.52965 | 2024-11-05 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47c3e7ed-818f-370a-9f01-297d1f8dd9c6 | 0.19292 | -51.06523 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abb8c9bb-399e-3ab8-8483-a729d51d9965 | 0.04363 | -49.55113 | 2024-11-05 04:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9668aab0-b4ec-354b-abb1-90b41f92c365 | 1.78807 | -50.43681 | 2024-11-05 04:53:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b344947-59b1-3b4d-a1b1-5ae213b1e4bc | 0.04855 | -49.5589 | 2024-11-05 04:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6acea10a-68d2-3556-a816-fc1ec5ccc4f1 | 0.18727 | -51.05125 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75dee2ac-2909-3c84-9812-4f2e99a1fae2 | 0.20196 | -51.07868 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11566e73-7032-39fc-9aef-96996678a06e | 0.19631 | -51.06471 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8307c016-d5a5-3505-9053-487053ed6e9b | 3.49981 | -51.26514 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 381d8d04-ae21-3155-be58-f3086c96fb33 | 3.5695 | -51.81561 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95ec5022-7f46-3d72-abca-6982f9cca308 | 3.52656 | -51.26117 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 369fc1d4-8a6f-3a9b-a6d2-b11557430f6f | 3.57004 | -51.81904 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1bcb8b4c-ab6f-36fa-bfc2-4540d52f63dd | 3.40692 | -51.32234 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49d34a48-d8d6-3095-b24c-2538f9dec7f8 | 3.52711 | -51.26464 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 688619a8-1d56-33f0-863e-315cf3e19119 | 2.77584 | -51.07141 | 2024-11-05 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72bede35-0ba9-39b8-ad05-30aaf7565577 | 3.52215 | -51.25476 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e195599-a841-3c35-856d-fd2a22d4b4e5 | 3.52546 | -51.25424 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d0ccbd7-0d82-3386-9e81-345d372b1426 | 3.52601 | -51.25771 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e02e78b-67d6-3eac-8c92-8f61820088bd | 2.73544 | -51.37455 | 2024-11-05 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dede18a3-9564-371a-923d-4b2e26865d97 | 2.69012 | -51.36737 | 2024-11-05 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 718f096e-9357-3570-9c1d-c5d63d3ca049 | 3.50834 | -51.25336 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44e4b4fd-0903-3ab6-acef-fa03336b2fb2 | 3.62376 | -51.29567 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fb57372-8011-306f-bf6c-af9a212822d8 | 3.34295 | -51.28263 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2eb2c630-1631-3fe2-ac96-4262c9381989 | 3.40747 | -51.32581 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bde02b0e-8d8d-35f0-baa1-677b60a8461a | 3.51497 | -51.25233 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2390cdbd-5b21-339b-9bb6-2dfbe14d139a | 3.51552 | -51.25579 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b73d3cb4-35a3-3c5b-a9b5-9664ec5ce831 | 3.4047 | -51.32979 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c65daeeb-7c30-31f0-8b28-a281e86d9ce7 | 3.50203 | -51.25769 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c4d19f4-d0cb-3603-b4a6-f35d48fae042 | 3.5728 | -51.81509 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9d71223-cd0b-3e2a-bdf0-5b62c91770aa | 3.51166 | -51.25284 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcc64861-f226-3531-884c-39f35d2c8e9e | 3.5048 | -51.2537 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94a3adc6-b668-3f90-b793-8e3c5352b808 | 3.49927 | -51.26167 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 26d0990d-8cae-31b9-8271-cda5c4957dc5 | 3.62982 | -51.31245 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ebb0bbe-e53e-3203-adb9-31fcb2704ded | 3.51883 | -51.25527 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2876d4a-b382-3897-bd33-3c14a83a65f7 | 3.49872 | -51.25821 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8805224-9999-37ba-8bfe-7a9185d0e7b3 | 3.51828 | -51.25181 | 2024-11-05 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7401fac-180a-3190-9389-0ad5beb7c945 | -4.60401 | -48.92791 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1467a369-10b7-3cbe-b35f-41ecdae05e7e | -3.99587 | -49.93944 | 2024-11-05 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16995830-11cf-31bd-8fe9-214e6e53a7b5 | -2.12179 | -50.65837 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55c1ad41-73ff-3a80-9a83-ae12797e3c53 | -3.10728 | -50.30048 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4339dbcd-669f-3d5f-99ca-37cd9210858a | -3.55386 | -47.39396 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5d397fbe-59da-32ac-867e-5b1a1e008043 | -2.87736 | -51.31379 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00ee4b49-2a18-370d-800c-ffbb95c19652 | -2.46274 | -48.49061 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1628cec4-a842-356b-8570-065dc068511d | -2.23864 | -50.70298 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8f78a34-c410-3cc4-a350-8d7002907b08 | -2.77902 | -52.87263 | 2024-11-05 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb16a756-23b7-3bba-a79d-62063eedb892 | -6.0984 | -43.96503 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 96a2ab97-d020-3edb-8ee3-b3e02ac8da61 | -3.4467 | -50.13709 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 673ccf45-9181-3828-b630-a5ac4002f59f | -3.04596 | -51.06662 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f811a4d5-2e8d-35ca-ac64-b3d39e8418d8 | -3.04283 | -53.27007 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d627ae3-976f-374e-b295-39c1b88c74e0 | -2.18075 | -48.85495 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c42a6263-5f9f-3bfd-978a-b1d08f7ef279 | -3.04006 | -53.26612 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 344a6d25-5781-380e-9bc5-7e14ac32b8e8 | -2.61668 | -51.72281 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6315ddc1-a12e-3e85-b0a9-cefc4fe999fe | -3.44759 | -51.65699 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb57bfcc-f08e-3129-96fc-2dffa72de225 | -2.91655 | -49.34881 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f4e7b06-9deb-3c71-9f7d-93c6647a84bb | -2.88197 | -51.30683 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9111da77-13f6-3ee5-aa01-810d3f2a6bba | -2.8706 | -49.39573 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b38b557-5a05-3a27-a00f-fcd197d0d60c | -4.36452 | -47.89449 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a03603b9-051b-3eef-8aa2-5527aecb4a62 | -3.03622 | -53.20208 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9066a0fb-874c-3637-b0ba-6ddc88ebc655 | -3.48062 | -50.38233 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70515da3-97db-3cf3-9e50-9e0f4578e270 | -3.0406 | -53.26269 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dc305f4-7693-353d-80e9-d288ba862e7b | -2.81561 | -52.94186 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c641779-132c-32ee-89b2-734050bd2b5f | -4.88798 | -46.72038 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28b25d41-34a0-3f79-96f3-9b837b8d4917 | -2.17224 | -48.85863 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f2495e09-893e-39f7-9fc6-f9defc869662 | -6.51939 | -45.93443 | 2024-11-05 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca10dcbc-22f0-3514-a15a-0b869020d82b | -3.08259 | -54.50355 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ad1a951-b8bd-3359-8334-e08e9cdcbc2e | -2.92165 | -48.05637 | 2024-11-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0ba4275-df75-35ec-acaa-3238ed8a594b | -1.38504 | -55.42767 | 2024-11-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30fa8cd3-ff47-32d5-a92c-7be18f178378 | -3.93902 | -45.56967 | 2024-11-05 04:55:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7d6d7440-0310-3363-a726-15ebc9f66860 | -3.85255 | -52.13618 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31678556-3418-3a98-96b7-b1b44826a2e7 | -2.91767 | -48.60206 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
