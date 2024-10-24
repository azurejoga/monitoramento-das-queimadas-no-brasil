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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f83fab5-84fa-3f8e-9581-ba64eef14182 | -10.60135 | -44.2593 | 2024-10-24 04:44:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 94a8f2ae-8f1f-3f47-8aab-923c08c1a548 | -3.7029 | -41.68739 | 2024-10-24 04:44:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 35dffa53-58d8-3cb3-ae5c-9ba2224e8820 | -3.70543 | -41.67124 | 2024-10-24 04:44:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 229d8b8e-a873-3213-8273-d91a9be8131f | -4.56328 | -43.98737 | 2024-10-24 04:44:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 89f4d70d-1d9d-3bd3-b704-00cd06604fe4 | -4.56719 | -43.99569 | 2024-10-24 04:44:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 37f4a2e9-db02-3e2c-9808-d047ae9d5dd0 | -6.50833 | -35.25471 | 2024-10-24 04:44:00 | AQUA_M-M | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 466bd13e-b15e-3a6d-a82c-d2ce677724ae | -6.73022 | -40.48263 | 2024-10-24 04:44:00 | AQUA_M-M | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 0f8a6e0c-b538-386a-b875-c33aecc44449 | -7.30079 | -39.141 | 2024-10-24 04:44:00 | AQUA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 89da78ce-e6e7-3742-9d27-5b7204f23149 | -1.5878 | -53.3089 | 2024-10-24 04:45:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| af6fd5ac-169b-3824-a137-4058c82bc478 | -2.9578 | -50.4198 | 2024-10-24 04:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 672a1375-d156-3531-8eee-7ec8af5e377a | -3.1607 | -50.4556 | 2024-10-24 04:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 8bc1dba4-de07-3db8-bab1-7b81e9266550 | -3.9396 | -46.4229 | 2024-10-24 04:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 108.3 |
| a42d6f97-f4e5-392d-92f8-69d10b295199 | -10.9268 | -47.81021 | 2024-10-24 04:46:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 7b6d4488-5ccd-3ade-a8f7-43d44bd554b7 | -11.02312 | -48.26538 | 2024-10-24 04:46:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 08787a78-afc9-3a70-897d-1f80b78255d6 | -11.81452 | -47.07076 | 2024-10-24 04:46:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 07cb4b69-2b49-3b9e-92ca-240dd54e29f0 | -11.61936 | -44.91801 | 2024-10-24 04:46:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 66a5dc62-9649-32f6-92df-d0a8d6d2cd5e | -12.13687 | -43.47255 | 2024-10-24 04:46:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| bd4c6bb8-c078-30dd-93cc-c41c4158208c | -12.67604 | -43.83996 | 2024-10-24 04:46:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 74b14099-5de2-3d11-b23f-09113d20ba82 | -12.68778 | -43.84201 | 2024-10-24 04:46:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| ad12c8e0-7fb1-33fd-bc61-1e7cce7790cb | -14.92216 | -45.11093 | 2024-10-24 04:46:00 | AQUA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c0b89f73-5959-3a5e-ad3b-fc8e2dc72367 | -16.00749 | -43.3886 | 2024-10-24 04:46:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 40b2de2b-b0ee-32f1-ad3e-dfb2a54af939 | -16.9792 | -57.5223 | 2024-10-24 04:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 2d06a959-ab10-3fd3-a564-0c4129659240 | -16.9596 | -57.5245 | 2024-10-24 04:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.6 |
| 668d1e94-32e7-364e-9aa4-c5fb1af2d765 | -16.94 | -57.5268 | 2024-10-24 04:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| e6b18575-782d-3ab1-9cf4-68bdefdd9aee | -16.9599 | -57.5041 | 2024-10-24 04:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| e48915c9-1b9d-3e5d-8f22-29a3f9fc7b09 | -17.2383 | -57.2462 | 2024-10-24 04:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 48a4f9eb-9a5c-332c-a661-5c4e96051127 | -17.2579 | -57.2439 | 2024-10-24 04:46:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 0d33c034-e3d9-3c33-bff6-bd5eeedccf15 | -19.6442 | -56.8311 | 2024-10-24 04:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 51.9 |
| bf8541b4-7e2c-3dbc-88fa-a1e37eec33fd | -19.6438 | -56.8521 | 2024-10-24 04:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 07ddda89-2f29-3634-a4f3-08ca02626bf5 | -19.5681 | -56.6114 | 2024-10-24 04:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.2 |
| c509d4bf-421a-3d0a-b3e7-1b0305cbba01 | 1.79865 | -50.47442 | 2024-10-24 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 924c9b87-a7f0-32d0-8cd7-3fa1c1306c76 | 2.63543 | -50.88027 | 2024-10-24 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b46d1eef-3afb-3bbc-ada4-bbd9b090ed27 | 2.63264 | -50.88434 | 2024-10-24 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d17cc7dd-1ea9-3499-86d8-c645d2fd9040 | 2.63207 | -50.8808 | 2024-10-24 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3210bcd-e328-32ce-8b4f-9ab661424740 | 1.81527 | -50.47184 | 2024-10-24 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6331da07-a1fa-340e-9305-6f4473bbf8cf | 1.81468 | -50.46817 | 2024-10-24 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| befd98e8-6b91-3d5b-b831-87ec9cb4d906 | 1.81186 | -50.47237 | 2024-10-24 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7de5b953-df27-3ff0-b2b8-996d0a369bee | 1.81127 | -50.4687 | 2024-10-24 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 328ed5de-0341-3067-a950-76974061c28a | 1.79531 | -50.51999 | 2024-10-24 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78691a3e-c017-330e-ab75-d57c1e267a29 | 1.79523 | -50.47496 | 2024-10-24 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f29478c-18e7-3bf8-b5a5-3558beb625a3 | 1.79239 | -50.47916 | 2024-10-24 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0bc2410-0e8b-3855-9361-dac7cc8e5a61 | 1.79182 | -50.47549 | 2024-10-24 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23def1d5-ab95-3db1-8a24-0058df161995 | 1.78898 | -50.47969 | 2024-10-24 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea9fa5bb-5a2a-3340-9dc3-a145e5b9e4f8 | 1.33734 | -51.13986 | 2024-10-24 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f4e59fa-45e6-3b35-bc6e-e3171c6bf51c | 3.51941 | -51.45778 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e24e16fc-0d6a-3e60-a2af-ffe1478600dd | 3.51886 | -51.45433 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e59fae5-26bb-3f42-a8df-6b17b14f87c4 | 3.51831 | -51.45087 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f6e4e0b-7891-30d5-a6d3-327a392627d9 | 3.48764 | -51.25684 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05401c90-300c-3524-9cd3-285476dd799b | 3.48431 | -51.25736 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 753d732c-d644-36f9-98d3-5a9ff62a901b | 3.48098 | -51.25788 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07a528a7-e9cb-328b-bb77-5688f0bdb5d9 | 3.47931 | -51.26882 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d32eead8-862f-3a63-af1d-01c9e8c4c67d | 3.47876 | -51.26535 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55ed5a8d-4f88-3f19-ab8c-46ae3c5a3cf7 | 3.47821 | -51.26188 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e834fc8b-3447-38c5-ae00-5c7916e4009c | 3.42092 | -51.28136 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 789e8cdd-4ce9-31db-99ad-68c47719a65d | 3.335 | -51.31676 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22794890-8cd3-37cb-9d88-b16402a0fd3a | 3.33446 | -51.31329 | 2024-10-24 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65e88054-e35f-3ad5-947f-d71720e12553 | 2.80422 | -50.93755 | 2024-10-24 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9ae2341-ea5b-3f20-abda-e0141c043993 | 2.80366 | -50.93402 | 2024-10-24 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6176c0a4-4176-3b7a-9c14-245ca98c9ae8 | 2.80087 | -50.93807 | 2024-10-24 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84f3bb05-997d-3ffe-a606-06dae1253a06 | 2.50012 | -51.0024 | 2024-10-24 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4e8301f-4ee9-3336-ab63-d87a37eea5c2 | 0.99286 | -51.29782 | 2024-10-24 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0dcf29eb-54bc-34a1-980f-dbf7908a6424 | 4.82976 | -60.14432 | 2024-10-24 04:53:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fff35837-d8db-3d27-a67f-49f4f86f0a2e | 4.82479 | -60.14645 | 2024-10-24 04:53:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bed59058-f5d2-37b5-8db2-ba2a59029ee8 | 4.82431 | -60.1431 | 2024-10-24 04:53:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835a79c4-da17-3f90-aed0-1b54e65a7aa0 | 4.81933 | -60.14515 | 2024-10-24 04:53:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b068de5c-91a5-3e4e-aace-398fbc09e471 | -1.94505 | -46.54737 | 2024-10-24 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c680c1fa-1363-36b3-85a9-82cb82b9ee4b | -1.943 | -46.5447 | 2024-10-24 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78807d2c-6ae8-35b0-9695-f280ebb33e8b | -3.31935 | -47.01513 | 2024-10-24 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 401a20b7-d1df-36cd-bd7a-5becdc803c68 | -2.93779 | -46.78621 | 2024-10-24 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4698fe7-44bd-3a72-b8dd-cd92aa6583b1 | -2.93711 | -46.79065 | 2024-10-24 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a343fbb7-ff90-32fd-a954-75e1a11927bc | -2.54024 | -47.22016 | 2024-10-24 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f0f6618-43f8-35aa-bf88-abaa14d2adb1 | -2.53961 | -47.22428 | 2024-10-24 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 933fc503-0df7-30c5-a149-c84a0e0afe46 | -4.75103 | -47.56437 | 2024-10-24 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 45c1efd8-91f9-399f-9072-da868c047198 | -4.43967 | -47.76895 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddfc7cb1-bc0d-3b1e-9f6a-eadad01df2bf | -4.33891 | -47.59322 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 365e0a03-4cd8-3898-8975-e4102e8798c4 | -4.33455 | -47.59274 | 2024-10-24 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16c0ca97-3b6c-39c5-9f36-b2ec4b7af850 | -4.99436 | -46.48186 | 2024-10-24 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85a715e2-290f-34ca-a2b0-bd9e36fc9030 | -4.99366 | -46.48665 | 2024-10-24 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58555696-323b-3ab0-82d0-0762ebd44269 | -4.82339 | -46.85403 | 2024-10-24 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84f501f5-2a27-3357-854c-04c361cec4db | -4.77228 | -46.4027 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39e239dc-a0e6-3069-8a25-91c12f8d82b1 | -4.76755 | -46.40191 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 856d8e61-4ccb-346f-b7a4-3b71e943ea08 | -4.76685 | -46.40681 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 53cad355-1b37-3767-b0ee-56934a32b11a | -4.76678 | -46.40027 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8974a7e1-893a-317c-9062-a00cc6297434 | -4.76605 | -46.40511 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 36b038da-6204-3dc1-be54-f6389ac9c89c | -4.7653 | -46.41006 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 99d915c9-bdbb-3c11-bbbf-07c4a9a4eb23 | -4.76283 | -46.40111 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 83f530ef-89ec-31d9-ad9b-3db1d0437ba3 | -4.76212 | -46.40602 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| ac174d0a-03e2-3478-a4d5-4a9e96bf8784 | -4.76132 | -46.40436 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ad9c719f-c124-39d6-ac76-59897ba27d24 | -4.76057 | -46.40929 | 2024-10-24 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e1048177-8d0f-3050-8c7b-1797476a9237 | -4.75673 | -46.64258 | 2024-10-24 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f34ab128-74a1-345b-a07c-c367a3d7489d | -4.75205 | -46.64199 | 2024-10-24 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a024a4f5-2b52-336e-a1b4-a4cecf6897f3 | -4.75136 | -46.64676 | 2024-10-24 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0dd6eb73-3db5-3be8-873f-3e94d7d70316 | -4.75088 | -46.61723 | 2024-10-24 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a038d394-cbf1-3fae-9d06-19ef46450e99 | -4.74828 | -46.60227 | 2024-10-24 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 319b90f7-4498-319e-931e-c20a79efdd57 | -4.74619 | -46.61669 | 2024-10-24 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 78621160-c6da-3610-8deb-8101e01df205 | -4.74361 | -46.60155 | 2024-10-24 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cbb5a9e-ceb6-3b25-ba5a-225e153ced93 | -4.66272 | -46.58228 | 2024-10-24 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94e8e1ca-2d4e-3572-85a7-d03d24c26bc3 | -3.80709 | -47.49565 | 2024-10-24 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56a52a17-69e1-3cb2-90e3-cb82172b4ae8 | -3.80647 | -47.49976 | 2024-10-24 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67d214c2-f6e2-3087-b5cc-46fbab9577b2 | -3.80585 | -47.50385 | 2024-10-24 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README61.md)
