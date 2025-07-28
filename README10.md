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
| 7d8c96ce-79fc-39ce-af63-a6ac51499148 | -6.02398 | -44.06119 | 2025-07-28 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76909d0f-77f1-3fef-91be-26d87100325d | -12.68532 | -47.0312 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86d965e9-5669-3ec4-bee1-ca1ccbffae08 | -7.65817 | -44.80283 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| da7e5cf2-852d-3a59-8d45-5bbeeba68809 | -7.11066 | -44.88777 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7f4c98a-fc67-33a8-9241-39ce92be5fbe | -7.12356 | -43.34808 | 2025-07-28 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5ac55b66-d4a8-3d20-86f5-1b068399e69f | -6.248 | -44.06676 | 2025-07-28 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c71985a-b3b8-3695-bf82-1c7aeebd53a1 | -7.07743 | -44.90523 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47757e0c-f607-3db6-8039-8711a50ea46c | -6.25854 | -44.96462 | 2025-07-28 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e25cc3c3-8478-3b0e-9c71-ca24f6b4e507 | -7.29253 | -43.42262 | 2025-07-28 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3500820d-be9f-33ae-a238-b2b00ed75566 | -7.69748 | -46.05005 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 012f4991-20d0-3ca6-83b7-1b975b8cc40b | -7.24721 | -45.39387 | 2025-07-28 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2ab30535-b49a-3d79-ad2c-6f4a25dfbe7f | -7.0775 | -49.95568 | 2025-07-28 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2154262d-1a5a-3d4e-89d8-7bbf85647457 | -10.04064 | -59.10186 | 2025-07-28 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8423be2a-e5a7-3f9c-9b1c-edadeea5bfb6 | -6.91906 | -44.24792 | 2025-07-28 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a5c2d8e-a33c-3153-b5f9-a55eb39ee8fa | -7.24627 | -45.39108 | 2025-07-28 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cff0eba7-c61b-3c47-8f9e-9573511b9552 | -7.07874 | -44.92402 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ec219f57-a6d7-363e-bbd8-3eb1d126f032 | -10.03951 | -59.10796 | 2025-07-28 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56198c99-63b8-34ae-8a7d-059d7c7214dd | -7.82188 | -44.58927 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51799829-998a-33bf-b5a2-d3412cb5ffbf | -7.02379 | -42.11022 | 2025-07-28 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 72eca7cf-45a3-3b2c-ae99-29069e5cdf54 | -8.30958 | -55.10159 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15119734-d2fd-3f1d-9f22-9476194e8fa0 | -6.41728 | -41.14101 | 2025-07-28 04:40:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9e6c7846-647b-3fab-bc60-3cbed29a3656 | -7.80567 | -50.77535 | 2025-07-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cbfefc3-ec28-37e8-a26a-0165ff26f655 | -11.96707 | -46.69739 | 2025-07-28 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcf16be0-5287-3b90-8ba1-b87540d35897 | -7.14873 | -48.20579 | 2025-07-28 04:40:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50149e85-d428-3615-becb-cdbe66e8a381 | -7.58044 | -45.38258 | 2025-07-28 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 745c24d8-8868-3b93-8265-f9bcf397ed09 | -5.88604 | -50.5881 | 2025-07-28 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01c690c5-60d1-3e20-8b79-90e5c8dbcc1e | -10.25623 | -55.0014 | 2025-07-28 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74e8e4d8-1f4c-3f72-b4c4-25e63e8c4a7d | -12.66786 | -46.99041 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3ac1a76-3aa6-3002-8b0b-ae90816c4f7b | -13.11897 | -47.37768 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89caf05e-19b0-3f0f-b155-9565c6b61fba | -10.31727 | -54.15447 | 2025-07-28 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 567902fa-d272-37ca-9d01-1864ea7e9d36 | -9.12802 | -45.86441 | 2025-07-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02930f8a-4926-37aa-89ca-87ff4470b51f | -12.74686 | -44.74339 | 2025-07-28 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 482954bd-97ef-3b69-88a3-b7c074d4b6fe | -6.25327 | -44.05984 | 2025-07-28 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f95b0d54-4734-3e91-b050-ba334ce7e159 | -7.34418 | -44.70296 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecf12eeb-49bf-374a-8bfc-866b57b6f836 | -7.09871 | -44.92642 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d230616d-a449-3084-b212-43ac5654db16 | -7.08243 | -44.89891 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 916cda63-6451-3962-b84d-d9d2d5a6ca59 | -7.09964 | -44.94749 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5d6815a-8257-321a-877c-c91922b0ffde | -7.07692 | -44.90871 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62577c26-25e5-3907-969f-e9ff32ee43ee | -7.39438 | -44.67337 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d437aae1-c389-37f5-b813-8181a7e2793d | -10.8484 | -46.68022 | 2025-07-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d42721b8-0b67-37ee-977c-3f5af21fe244 | -7.14197 | -48.20477 | 2025-07-28 04:40:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcc03a4f-f5db-3dca-b23a-556e61d6721f | -7.10211 | -44.9582 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb4ec0ce-2433-3d33-8d21-7bb7a0e1acee | -7.97887 | -49.95739 | 2025-07-28 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 258ca661-daec-37b7-a349-aba1da597282 | -7.90964 | -43.10262 | 2025-07-28 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2f1b60bb-37e9-3a0a-a52d-64a0f0f42c52 | -7.24168 | -45.39534 | 2025-07-28 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eb7c1a2e-c3bf-387d-bafc-8da233a2069f | -12.66717 | -46.99539 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0ac2c6d-1c3c-31d6-ac27-9386f541c962 | -6.49231 | -56.1986 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4925b899-4bc3-3c24-9e76-9f2ca8aaa579 | -6.4002 | -53.353 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68a5e2d4-1431-3cbf-b271-96b8b2011134 | -6.825 | -44.14973 | 2025-07-28 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a360d25-5fa8-3f7e-9b4a-61944d0abd06 | -11.34725 | -51.24675 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e674bb3-1b71-30a5-bf97-eb9cc9eddd30 | -6.50345 | -56.2141 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f645e438-bcb8-3d84-b253-d786a9507b92 | -7.10876 | -44.91352 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3638b855-e998-3b69-b5c3-d4a342759fcb | -7.92384 | -43.10782 | 2025-07-28 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dabddd8e-45c3-30da-98dd-704e263b40fd | -10.85215 | -46.68083 | 2025-07-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5afc05f2-16e9-38d2-8f3e-797c5221e459 | -7.211 | -44.16596 | 2025-07-28 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3aa7acf7-f756-3dd1-a2cf-d928b481cee5 | -5.63728 | -46.67727 | 2025-07-28 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f53f6f60-a4f0-3312-ac63-a6b41f68b5d4 | -7.6627 | -44.80009 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b4551ce-f0d6-3ecd-8d92-02fe462a0ac0 | -10.51754 | -42.55788 | 2025-07-28 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6eab3443-2769-399a-bfb6-34bcf8bf89ae | -7.29693 | -43.4233 | 2025-07-28 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9b4ae84-152b-31c3-9c5a-278362e940ac | -10.31284 | -54.15831 | 2025-07-28 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ee0f8a25-8279-3053-8baf-d9fed3559e3d | -6.49602 | -56.20378 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 17d1376d-506a-313d-a528-b2aaf1772f8e | -6.44324 | -53.34623 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb86417d-1876-304f-b95d-39e6d3fe5903 | -7.91148 | -43.09628 | 2025-07-28 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 899c423f-053f-3809-affd-fa52bb17b39a | -7.07983 | -43.8772 | 2025-07-28 04:40:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae67c1d3-c211-3b3e-a9f3-6d812c5884b3 | -6.89984 | -52.86848 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76e2c9cb-fc27-3a30-b3fe-60ec06046996 | -7.35186 | -44.36255 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d6ad4e4-d42d-381b-b2a2-02317a0de6c9 | -12.66336 | -47.02295 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21a4330b-d96d-398d-8f53-6e3f971b9b63 | -7.3523 | -44.73664 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c066c0d-b76f-3377-b67c-e7ff08e832ac | -7.696 | -46.04259 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e58f156-7783-3fef-8a26-39f9a5ecaa97 | -6.40392 | -53.35359 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 89306291-2e5f-3854-bacf-692322457116 | -6.14358 | -44.34874 | 2025-07-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93d6e196-9e97-3536-b65c-f8198447fbf0 | -7.07613 | -43.87254 | 2025-07-28 04:40:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 053684ea-e4bc-32d2-a945-3fe51e903e65 | -10.51827 | -42.55228 | 2025-07-28 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 13a1e2c1-014b-3d20-a8bc-ca783d3b68dc | -6.39947 | -53.35746 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf80e6c7-dbbf-3cde-a9e4-a596f7e54dbd | -7.34013 | -44.70239 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34c8e21a-4a0f-31aa-8ca7-71025b7bd836 | -6.17947 | -58.0733 | 2025-07-28 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9253d4f5-4dbb-3aed-b8b9-ef3b0e09d35f | -7.09484 | -44.9525 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1e398da6-9e1b-3939-88cf-f71f6f72eb33 | -7.09564 | -44.94711 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 204e395f-3820-3a0e-a6ef-45fa9c6b5ca4 | -7.66755 | -44.80088 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb28e58d-0b4d-3cfe-9dbf-f00ec1571d09 | -7.24555 | -45.3959 | 2025-07-28 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8ba1589a-8c54-3c23-ae1b-fadaa827df5e | -13.07495 | -47.36679 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b07179fb-395f-33d4-aa0a-e5b8f76e05f9 | -8.49992 | -47.49813 | 2025-07-28 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4837816b-b42f-3736-995f-f33b38a72875 | -7.38393 | -43.44271 | 2025-07-28 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df54de4c-25b9-34ba-9aa2-f00f4b57e093 | -7.10925 | -44.92648 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2e9decc6-67cf-3d67-a116-713e4fdf342e | -6.47724 | -41.62244 | 2025-07-28 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a5aaddf-9feb-3c4d-90ea-b0a26990d3e8 | -7.10901 | -44.88451 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11b1cca6-f38a-3a20-9d70-1c8c10f99001 | -6.40764 | -53.35416 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9292a9da-19bd-394b-8b9f-8a356611364d | -6.01464 | -44.06701 | 2025-07-28 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7fea39b-2444-3192-9d92-ca84689e7767 | -7.09795 | -44.93153 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81cc4884-5695-3168-b3be-b931240e2f64 | -6.93261 | -44.24211 | 2025-07-28 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 291c2157-34ec-395e-80dd-988eacc7b899 | -6.21265 | -43.74858 | 2025-07-28 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a93609b7-55aa-3b98-bd3c-17e3763424dd | -7.66301 | -44.80382 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9348a397-8c49-3b87-85f4-c79da38884fb | -7.15152 | -44.36954 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44896af7-11bb-32e9-be77-99c909de02bf | -6.2565 | -42.83704 | 2025-07-28 04:40:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 878944a4-e872-39a4-8b73-2a87ee2cf4e6 | -7.66624 | -44.80413 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24b5e7b8-ee3f-31e4-8277-8efca54f710f | -7.08672 | -44.925 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a77f5579-7b13-373d-96bd-c3fb3422e4af | -6.15182 | -43.8118 | 2025-07-28 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4564bb1-c1dd-3995-bbeb-adf17b9f79a9 | -12.69289 | -47.0321 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54d078d0-073a-3f21-b9a7-5618ef3c2152 | -6.447 | -53.3587 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26a24fa3-c2e3-31d8-b6d4-727116fa4c14 | -6.92684 | -44.25277 | 2025-07-28 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
