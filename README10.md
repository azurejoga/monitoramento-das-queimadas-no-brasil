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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 557e024a-658c-3de7-8625-1f1bce7edb08 | -3.92913 | -46.9376 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc96afcd-7708-3467-a558-60bb82f1aa63 | -2.12922 | -50.70407 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88352743-0579-317f-82f4-6a543df1661e | -0.62467 | -49.61982 | 2024-12-23 04:31:00 | NPP-375D | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3784d61-2337-3ca6-90a7-7e7734fc0155 | -4.01089 | -46.80798 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bc29ef3-5d6a-36e0-9d5d-84e5e4bb0d0d | -3.10195 | -54.55184 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 87217997-17d3-3b4e-b095-8238b0d367f0 | -5.45009 | -44.8073 | 2024-12-23 04:31:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60349c70-7bb4-3b04-9628-de986df81aee | -2.73015 | -46.19076 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 868f53e4-1e67-3255-997a-7eb9179aab49 | -2.65188 | -46.11049 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3ffc077-f87f-3ff0-bd7d-a87c0a1824c5 | -4.18145 | -43.63454 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4471cf94-1d96-3936-bf8f-1c8f7bd700af | -3.92342 | -46.88695 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d887811-9bc9-3419-9b4d-742d1ce950b7 | -4.03087 | -50.05952 | 2024-12-23 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92df2740-3924-3e6c-8ca2-0ec21d953cce | -2.86361 | -48.70263 | 2024-12-23 04:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca287145-7dd7-33ba-8ea1-4fc0aa62486f | -3.87935 | -47.02237 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee8b6d4e-c31b-362a-90d9-e054324d1261 | -2.79433 | -46.75734 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2889751-7d41-3c91-8496-1548a8be9349 | -6.94046 | -43.53537 | 2024-12-23 04:31:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b2d478e9-d01f-3075-8767-6f450a31158d | -2.42635 | -48.59766 | 2024-12-23 04:31:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0ec4877-fa8c-3cf1-89f0-c3f34834929f | -3.29437 | -49.47841 | 2024-12-23 04:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e4e749a-00a1-3a2c-947a-e25024d7ea59 | -3.0933 | -46.55839 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3faf2864-5867-3c16-a5a3-0cc721a9ad77 | -4.0399 | -46.79168 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc9d078b-1659-3f70-9d8d-9274f5280dc1 | -4.00911 | -46.33694 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c463ee5-4f58-35a0-a4c5-6120064bc4c4 | -2.39144 | -47.07964 | 2024-12-23 04:31:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5054eebd-b71e-312b-b606-1ee736defd69 | -4.0855 | -46.80587 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9bb0edf-ed16-3894-b8cf-5321120fefa4 | -2.40468 | -53.74078 | 2024-12-23 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e748dcad-fd1e-3821-97f8-d9082aaf2823 | -2.4449 | -51.79493 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e9b4749-bfdc-3ce2-8887-d35c873d3073 | -6.00534 | -45.42003 | 2024-12-23 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c339c2cb-0cdf-304b-9956-114089d0c184 | -1.63184 | -45.84446 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c96afb6-6ced-36ff-a88c-bfe311327e87 | -3.9169 | -46.92863 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f446b8c-a18b-3b07-8cfe-ab05a8620a44 | -3.90712 | -46.99105 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b348053-7042-3e6c-ac7d-5ac8f2f226b7 | -4.08666 | -46.82028 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bef3a2ae-7464-30d2-8465-14f42fead52e | -2.81966 | -48.2519 | 2024-12-23 04:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0327401b-b86e-3b15-8097-1f2702fd9f01 | -2.79488 | -46.75388 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a660ee5c-54e8-3520-b410-9bd13fba61eb | -4.04343 | -47.03062 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bdd0d7a-588a-3d02-9857-56aa85c5c977 | -4.01193 | -47.05766 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 447bc34a-7b60-36e6-a851-bb1b3bffce13 | -4.53151 | -46.35928 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff51a115-9bfa-3226-91f8-502a59cecc84 | -1.62848 | -45.84394 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15b33cd1-c99b-3112-9a23-db22fe31ec25 | -3.10206 | -54.55313 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf774297-89a5-34b2-83ce-1b1b34c0918d | -3.83436 | -46.68444 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64fe6a99-e13e-3468-a085-5951b2318f92 | -3.80087 | -46.85384 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0748b3e9-4dc2-3991-a85a-52701e658ec6 | -2.48458 | -47.13366 | 2024-12-23 04:31:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f06dbeb8-b7fe-362b-ad93-54e13b2148c5 | -3.98221 | -46.6857 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fa82b80-716d-3634-8626-f914f0e84a3b | -3.79831 | -46.71811 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8a1ca31-f81e-30ba-8667-f287d39677ed | -4.10387 | -46.8194 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ee8e6f8-9aa0-372d-adb8-26b434f96190 | -3.92294 | -46.9118 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc5b515f-f740-30fa-8d6e-19f719a0dcec | -3.83624 | -41.55949 | 2024-12-23 04:31:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 454a0360-4f1a-3570-98a6-168bff8c45c5 | -4.03128 | -47.04292 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f732f5d0-c385-3175-9dfe-ed8490adf234 | -1.26197 | -54.14533 | 2024-12-23 04:31:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 907fe924-90c6-394f-8665-cf1e069b761e | -3.91744 | -46.92516 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16f2fdc9-eb93-3617-afa2-3c04307d88e1 | -1.6352 | -45.84498 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b85c0d73-7e7f-3518-975d-a1792884b9c4 | -4.77798 | -46.39729 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96b2ac1d-2428-3177-9247-8ee5c5138753 | -4.22785 | -48.71249 | 2024-12-23 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e27ae11-0667-3919-848e-1dff30c09e2e | -2.12548 | -50.7035 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7860b942-4b00-36e0-8f58-00c491d8cc6d | -2.65133 | -46.11401 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4c9f8e3-7408-32bb-bdef-8692a796dfc1 | -2.6258 | -48.63935 | 2024-12-23 04:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 89281246-3129-3054-b766-a32c734d446a | -3.25042 | -48.07045 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7fbe940-b3c4-3681-bf75-8fc0154e69cf | -3.97772 | -46.67068 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b338d17-034b-39e0-8e9d-f392afcccba3 | -2.9903 | -51.43861 | 2024-12-23 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3343d2d8-da7a-3179-8015-f1527687aff2 | -3.93279 | -46.35447 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7be9e28-eb86-326d-badf-69b822e9100d | -3.99073 | -46.95791 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e776fc4c-7bd7-3b7f-9c24-905e37034137 | -3.92736 | -46.90538 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dec8e50e-8576-3e6e-9afa-adcacd5a0437 | -2.38074 | -47.42814 | 2024-12-23 04:31:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62da0495-a6ba-3e11-8c25-8ac0c4d3cf2d | -3.90441 | -47.00837 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69e0d3c6-47b5-3464-b3b5-4b47dfd20f83 | -3.00848 | -48.12273 | 2024-12-23 04:31:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4dfb23a-6b93-372a-8daa-23401211d392 | -3.91432 | -46.98862 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e07d19d-ae94-35bd-a510-8ed7dfc88d0f | -3.79918 | -46.84291 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b25bb1bb-0d3f-3351-a421-1ef767425d39 | -3.9489 | -46.87671 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90978fd4-29bc-32ab-83b1-566c27497f99 | -7.39114 | -35.26757 | 2024-12-23 04:31:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| cc4e5771-9445-3bee-b1ba-2551986ecef2 | -4.0536 | -47.09606 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 524ca745-5cc7-3165-aeed-431861d64793 | -2.64152 | -46.97419 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae4c6684-95db-3279-91c8-a5dbc2e2e3e7 | -2.64682 | -46.09888 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f0ab1b1-0842-3f85-b9f4-de6e592d7472 | -3.91656 | -46.99606 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bf6e937-d1d5-37ae-962c-4fa11b6e6055 | -1.63129 | -45.84798 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ef83646-3869-3650-9998-d3a45bd770fb | -4.01804 | -47.06214 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90f70ed1-b92f-3682-be78-a86b62fe00c1 | -3.91044 | -46.36551 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e600bbe-7e2c-3ca4-80c0-ab8d4a0a8649 | -3.79699 | -46.85679 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84652f6a-d530-3c3a-8f1e-244be9beed00 | -0.21335 | -51.60112 | 2024-12-23 04:31:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 675a3f8b-b956-343f-89b9-6dda320d1b0d | -2.71904 | -46.18573 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf2ac0b5-a1c3-37be-acc9-22c7dd35f7f3 | -3.97567 | -46.92352 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e205faa-94d1-3f87-a617-46dea822f4f7 | -3.9134 | -46.89272 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89aaea63-6646-3903-88c4-f73b16212319 | -3.90392 | -46.64871 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c3737a4-39c2-3886-9d96-7ac13b9c5d52 | -3.98103 | -46.04478 | 2024-12-23 04:31:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71db8017-7c6f-3526-8e94-d96365dd39f5 | -3.19225 | -52.88884 | 2024-12-23 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17c1add9-fd8b-3774-84c0-5182afd5daeb | -1.63464 | -45.8485 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2352c543-4258-3659-aba0-77a87a05baaf | -2.95409 | -45.73742 | 2024-12-23 04:31:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a3e82bb-0e49-36c5-a04f-73f4f8d73f56 | -5.60429 | -46.804 | 2024-12-23 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9dcc915-8cb4-343d-aaf6-e8d9ad6bb985 | -7.84511 | -35.22266 | 2024-12-23 04:31:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 18678684-c3c4-3bb0-95fa-b94bf68a5d00 | -3.91099 | -46.98811 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c845aa3d-1c70-3eaf-b2b7-6b93c404a60e | -3.91764 | -46.98913 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71059f64-ef42-365a-bf3f-c14c35581197 | -3.83825 | -46.68147 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d50631e-c869-3e26-beff-9d7908a1c9dd | -2.27389 | -45.75855 | 2024-12-23 04:31:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 74f0a676-5bec-3596-9e80-32c8ac2255d2 | -1.37717 | -55.13654 | 2024-12-23 04:31:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3275361e-9982-3e80-8c37-b9321f663a08 | -4.78025 | -46.40488 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b93a0b34-8b48-32eb-bb30-b38b005a655a | -4.01945 | -46.90546 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bae1ab59-2563-34f1-afd5-0742d654e8d3 | -3.09341 | -54.60415 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2088974-4ff8-3e77-a51f-f5b59361ab5b | -3.83769 | -46.68496 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f75bc657-3426-3da5-bfb0-b43ca26897c5 | -5.45307 | -44.81192 | 2024-12-23 04:31:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aed95ad2-f018-3b5d-a563-a1194dcc76fa | -2.94054 | -45.73531 | 2024-12-23 04:31:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2ac79c6-6bfa-3fdd-920f-d4ba0faa38fa | -3.09275 | -46.56187 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcdf05df-cf12-3f71-abd2-d36c0510422c | -3.97438 | -46.67015 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78052259-209d-3c12-8905-5c797f4c5c02 | -3.90603 | -46.99799 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4073296a-c502-3fcf-b3c0-e1f5a7967997 | -3.87096 | -42.25595 | 2024-12-23 04:31:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README11.md)
