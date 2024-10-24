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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d86fdf34-c0b4-337e-8476-e50967e54110 | -15.41535 | -43.08395 | 2024-10-24 03:17:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 76d0837d-5482-31bf-a277-4e6d8db57c1c | -15.86192 | -43.52951 | 2024-10-24 03:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6de04418-3308-3c5f-b8e5-29087cd1f242 | -12.14134 | -43.47631 | 2024-10-24 03:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 212808d6-251e-39b2-a168-11ecccb6e166 | -12.14059 | -43.47882 | 2024-10-24 03:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bd126c4d-3c90-3217-ad85-15d294dc3129 | -12.13496 | -43.47271 | 2024-10-24 03:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 63ac9940-ab07-3be9-8205-32490472ad99 | -12.13412 | -43.47572 | 2024-10-24 03:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8c62e74a-9a44-3d59-994a-eee795d9b756 | -12.13322 | -43.48113 | 2024-10-24 03:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 17399e41-60ea-34a9-82b4-2087f8e222c4 | -11.95332 | -44.16803 | 2024-10-24 03:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c61d77cc-a3cc-30e2-9a18-b6c54fc14af8 | -11.94623 | -44.16637 | 2024-10-24 03:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c532ac45-8b96-34c9-9375-3dccdbd24118 | -13.72931 | -44.28936 | 2024-10-24 03:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba1ccf06-a5cd-3509-b0e5-3c0c35f79786 | -13.51459 | -44.41313 | 2024-10-24 03:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 560e0ce7-b71e-32a5-a59f-0273785332ee | -13.51041 | -44.41214 | 2024-10-24 03:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd2e795a-6487-377d-829f-a53a9aeb5fef | -13.5088 | -44.41955 | 2024-10-24 03:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7286e16a-07c1-31e6-9501-ce26a6c3c946 | -13.50756 | -44.41164 | 2024-10-24 03:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9fdd7eb-a681-3575-a31c-dd41885c54c9 | -13.50591 | -44.41906 | 2024-10-24 03:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a8faa7f-3634-3abc-93b1-63ad5325cd82 | -13.47968 | -44.02652 | 2024-10-24 03:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e07ffd1-cfb0-3138-b940-5a699a6167da | -13.47276 | -44.0252 | 2024-10-24 03:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23f1cebf-2b08-384e-bb5c-2e9f972a2ada | -13.36426 | -43.93052 | 2024-10-24 03:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 728296ee-2134-3a5d-bc92-a8d5b1fdc1cb | -13.35741 | -43.92898 | 2024-10-24 03:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a13b3d4d-5575-34e2-85f1-f33241020d6a | -12.69304 | -43.83697 | 2024-10-24 03:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dc529b69-47ec-3b3c-9590-91e54cfcbba7 | -12.69166 | -43.8435 | 2024-10-24 03:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 539e9f91-108d-3991-9021-dff24f2a081a | -12.69044 | -43.84178 | 2024-10-24 03:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e002a5f4-d311-3de5-9cc5-654bc37de7e2 | -12.69028 | -43.85007 | 2024-10-24 03:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 165f1d2b-0086-3311-bdad-036cf710b5d6 | -12.68902 | -43.84832 | 2024-10-24 03:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ac57900d-61f8-3d9b-870a-773b09e21f9b | -12.68477 | -43.84196 | 2024-10-24 03:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ecc96e63-5f9f-3ad1-8ba1-8626668699a5 | -12.68355 | -43.84026 | 2024-10-24 03:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bc815826-d242-3e66-aecf-e88c4fd203ab | -12.68338 | -43.84855 | 2024-10-24 03:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f13081d1-cccd-388c-8bba-b9426bf641bb | -12.68212 | -43.84684 | 2024-10-24 03:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c32c7877-473f-3a98-9266-84aa79538768 | -14.92285 | -45.11856 | 2024-10-24 03:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 09261491-38bc-30a2-814e-b972844e690b | -14.92124 | -45.12565 | 2024-10-24 03:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d47d5c9a-d1e6-39ea-b423-2042f6b72557 | -14.91415 | -45.1239 | 2024-10-24 03:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c39e3f0e-b8a3-3cfd-a46b-228eb815c9af | -14.9125 | -45.13117 | 2024-10-24 03:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b997748-25fb-3882-81d6-5da5c8d2b17c | -14.91154 | -45.12371 | 2024-10-24 03:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77bbb7cf-197a-34de-9806-582ca72e8815 | -14.90993 | -45.131 | 2024-10-24 03:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca62af42-32d5-338f-bfdc-a37cd6c5f624 | -22.30533 | -41.88107 | 2024-10-24 03:19:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 774d92b3-3872-3484-b67b-f2d23df36402 | -22.3046 | -41.88436 | 2024-10-24 03:19:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3bc50397-9779-3621-8f60-33f85086549c | -22.30372 | -41.88371 | 2024-10-24 03:19:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bb5aed12-9072-3510-a119-53cf41cf5d4c | -21.28982 | -41.74686 | 2024-10-24 03:19:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 144929e7-3c19-350f-9c20-45abfd0ba5bc | -21.28466 | -41.74545 | 2024-10-24 03:19:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d7969021-32ae-334a-a6ba-7d2f61439a84 | -16.01262 | -43.39793 | 2024-10-24 03:19:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ad75e22-3dfc-3be9-9e94-3c29436118dd | -16.01182 | -43.3973 | 2024-10-24 03:19:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e280ec26-610c-310f-8ded-6dec79231398 | -16.00632 | -43.39626 | 2024-10-24 03:19:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0e523370-6dab-37ea-8914-8db215b5fa31 | -16.00553 | -43.3956 | 2024-10-24 03:19:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f4008d81-45b9-3a13-bc16-5d9b566cf2c3 | -15.86246 | -43.52838 | 2024-10-24 03:19:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bce9b09-ce56-348f-8849-e3f04daa1372 | 4.8312 | -60.138 | 2024-10-24 03:24:38 | GOES-16 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 27.5 |
| c45dc7be-4e23-374e-8c83-b25bfc253e7d | -1.5878 | -53.3089 | 2024-10-24 03:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 734d85c5-d731-3cf9-8952-d7e5839ba183 | -1.6062 | -53.3087 | 2024-10-24 03:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| a4d0825a-6034-3e9e-b33a-ccc170ca0b30 | -2.9578 | -50.4198 | 2024-10-24 03:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5e741934-a989-3f56-a56b-3bfd6215c4fc | -3.1422 | -50.4562 | 2024-10-24 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| d83091e4-afa7-3ac4-b2dc-2d6fcfcc330e | -3.1607 | -50.4556 | 2024-10-24 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 803634fd-eb6f-3207-8208-396a7fbbe531 | -3.9396 | -46.4229 | 2024-10-24 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 078fbb06-3697-3ab1-861e-0fe05e56ac34 | -3.9581 | -46.422 | 2024-10-24 03:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1b6f4912-855f-3412-869e-200590c47321 | -10.1969 | -53.8822 | 2024-10-24 03:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 4f0ee879-935f-3db8-b602-21d4467563e0 | -10.1971 | -53.8617 | 2024-10-24 03:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 16ad5505-a725-337d-9461-872a57deb983 | -16.94 | -57.5268 | 2024-10-24 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 6e3a2dee-8ddd-3344-9384-beb40f13b333 | -17.2383 | -57.2462 | 2024-10-24 03:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 04a91b4e-e634-3f2b-88f2-da1994543385 | -17.2579 | -57.2439 | 2024-10-24 03:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 70b635b0-29de-3a7a-99e2-d4779a8f6488 | -19.5681 | -56.6114 | 2024-10-24 03:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 53887938-626d-385d-afc9-6af06990936b | -19.6438 | -56.8521 | 2024-10-24 03:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| 44ec8c66-38b1-3113-95fc-d1458c8eb42a | -19.6442 | -56.8311 | 2024-10-24 03:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.3 |
| e02412dc-07bb-3085-bded-5277c91c188d | -1.5878 | -53.3089 | 2024-10-24 03:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 96851ff1-805e-3170-842f-db9f2aab4932 | -2.9578 | -50.4198 | 2024-10-24 03:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| e7877db4-8631-355d-ae95-3266119d0121 | -3.1101 | -54.1661 | 2024-10-24 03:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 22b18cc7-6829-32c4-ad76-136233d6f6dd | -3.1422 | -50.4562 | 2024-10-24 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 29477fa7-8fd2-3b8d-8b60-95cf87a886e0 | -3.1606 | -50.4766 | 2024-10-24 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 86032cf5-2cea-3f9a-90a6-97b565490ae5 | -3.1607 | -50.4556 | 2024-10-24 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9cdf2b6b-9bc0-3946-b48c-c830f6f715f4 | -3.9396 | -46.4229 | 2024-10-24 03:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 728a4ac0-1bca-3cdb-a639-79cde4fbd5ff | -3.9581 | -46.422 | 2024-10-24 03:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| a8522054-aaf4-3870-ba63-41bd7cffb69a | -4.5698 | -43.9967 | 2024-10-24 03:35:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| be7fcc2e-b5e1-3178-9aff-af7dcd413470 | -10.1969 | -53.8822 | 2024-10-24 03:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 6d265b72-3f6e-327c-8463-6511245bbcde | -10.1971 | -53.8617 | 2024-10-24 03:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 654cd192-a065-3483-996d-15988dbfcc6c | -16.94 | -57.5268 | 2024-10-24 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| cab45c93-d8ac-3d5d-953e-4548c915c542 | -17.2383 | -57.2462 | 2024-10-24 03:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| df0a7b1c-d032-3352-b1b5-bd437f2c3722 | -17.2576 | -57.2644 | 2024-10-24 03:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| b1667c4d-fe0d-3233-bc3f-bba305e4386e | -17.2579 | -57.2439 | 2024-10-24 03:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 55fa2a78-54f3-38e1-a6ff-dd517a8df63b | -18.0837 | -57.3076 | 2024-10-24 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 90af1f4a-02f3-3190-a4c6-5e586c5d386a | -19.5681 | -56.6114 | 2024-10-24 03:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 80bbb072-b0dc-3ed1-829e-aa1696e022a3 | -19.6438 | -56.8521 | 2024-10-24 03:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 910e6880-5655-3e60-8d65-bd14239d142a | -19.7262 | -56.7358 | 2024-10-24 03:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 15a5a09f-0766-3a1b-bcab-e70359452808 | -8.98319 | -35.55657 | 2024-10-24 03:40:00 | NOAA-20 | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5a94964f-df04-3156-a8ce-a7f2a36a451e | -8.72852 | -35.1195 | 2024-10-24 03:40:00 | NOAA-20 | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8223e0ae-942a-3ceb-9329-718444770eff | -8.71093 | -41.16293 | 2024-10-24 03:40:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6887838f-b932-34d4-92ed-17670dbe92ba | -8.70828 | -41.1635 | 2024-10-24 03:40:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f4cc604d-d531-32d9-a282-d6d5b4ee379e | -8.57761 | -35.34604 | 2024-10-24 03:40:00 | NOAA-20 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 13eae1f9-1d00-3463-8b3e-059c03b60be3 | -8.48075 | -40.55292 | 2024-10-24 03:40:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 349f7666-920a-390b-a7d2-da3710aa2372 | -8.48017 | -40.5564 | 2024-10-24 03:40:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6ee9269-eeaa-3ff3-8e96-1ee4dba05665 | -8.4156 | -40.59876 | 2024-10-24 03:40:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 27981640-c7c3-3f61-aa56-ee322b630166 | -8.36209 | -40.29785 | 2024-10-24 03:40:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e89aa1bf-1c1c-31fe-a471-567205196840 | -8.33588 | -40.89325 | 2024-10-24 03:40:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 35cac352-b248-39a5-89ea-d499ebbf1e7e | -8.33525 | -40.89688 | 2024-10-24 03:40:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a68197fc-2aef-3c46-b65d-12c5767ec003 | -7.93117 | -39.91408 | 2024-10-24 03:40:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e1df4a4d-633b-3c67-be6d-7dda0e65bcda | -7.93052 | -44.89677 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25de2765-642e-3aed-a6c2-d3068c5316cc | -7.92515 | -44.89576 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b47574d-cd7e-3ae9-b6da-e710f19adbb6 | -7.92041 | -44.8913 | 2024-10-24 03:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1908c93-b037-365a-861f-fe1a0335f0d7 | -7.84373 | -45.43807 | 2024-10-24 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31b0448e-f184-35ef-9846-e324b2d60d86 | -7.71814 | -35.34861 | 2024-10-24 03:40:00 | NOAA-20 | BUENOS AIRES | PERNAMBUCO | Brasil | 2602704 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ce78cfe9-13dd-393f-93f3-b210474861aa | -7.71704 | -43.77399 | 2024-10-24 03:40:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ef4bf5d5-32c6-37f2-b0f2-f86865118c16 | -7.71681 | -43.77349 | 2024-10-24 03:40:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| da38e9e5-9c92-3f76-b929-1abfe0b71ae0 | -7.66151 | -45.38118 | 2024-10-24 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 733126b0-9f8b-3375-8083-116b2a781867 | -7.66009 | -45.38891 | 2024-10-24 03:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README17.md)
