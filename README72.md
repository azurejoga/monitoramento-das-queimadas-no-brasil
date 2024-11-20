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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ef7f27c-9e8c-345d-a6e5-8d18c0a72afb | -2.82174 | -54.01781 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8fcaa9e-fd8c-3048-87a9-4139779dc265 | -0.83112 | -52.83623 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 258258c4-6b3f-349b-bbea-820ade3dbfd4 | -2.85548 | -53.9752 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88b6fa38-fdbe-3d82-af72-7e5a949aaee5 | -1.24712 | -51.75208 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44e532de-a6fb-3283-aa6e-68dd30fe7020 | -1.19085 | -51.97725 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb4d05e3-5493-3eeb-a7a9-cfef05851fd1 | -1.15114 | -53.51193 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7eb3079e-4302-3c01-8244-8f40fb059925 | -1.62233 | -52.59047 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d8b54dac-74d9-3ea2-be5f-fbbe918911e6 | -2.471 | -54.7514 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6010a24f-c360-382c-83be-f0231b8bd53b | -4.38428 | -47.77299 | 2024-11-20 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e55d9c6-c44e-339b-8c1d-2840f8d63b46 | -3.87949 | -46.06641 | 2024-11-20 05:14:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de997986-6b66-35a2-be8c-fea6702ee369 | -2.82571 | -54.09425 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d3693508-3866-3042-828a-7e9ebeb129d0 | -3.04924 | -54.40125 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49f30031-03f6-3a97-af25-eb1723d705f9 | -3.18585 | -54.31929 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b6fa280-a416-330a-a183-b144a60df6d4 | -3.04855 | -54.40573 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5904b65b-679e-3734-910a-7cfb95a5666e | -3.31769 | -54.09298 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3699697c-c235-3b55-9e36-a6a47a60a770 | -1.06081 | -52.39793 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c604ead0-1aba-3390-aec8-f9a2dfdebad4 | -3.41646 | -54.90347 | 2024-11-20 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eae59bb5-a79c-361e-9ddb-3fbb24b6cca2 | -2.20052 | -53.66017 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c61fb4f-f532-3600-a9a6-a7076017886b | -3.88052 | -46.06409 | 2024-11-20 05:14:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97d1648d-104d-3ac5-a63a-d646921b7ff9 | -2.95045 | -53.71632 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c0a3742-cda8-3e84-a436-cb6ef47a8015 | -2.02895 | -45.7951 | 2024-11-20 05:14:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 184785b9-8223-3527-896f-8813316bc0c7 | -1.64525 | -52.68302 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba93deee-66c8-37d5-8400-f3e062e554c6 | -1.09808 | -51.74481 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abe3cecb-cf9b-357e-bafd-78c7dc4bc8e5 | -1.25067 | -53.36773 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db2cf22a-6956-3c19-b7dd-33d47f4b60dc | -2.30123 | -48.49664 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5fe9e4a-2050-3656-809c-d3edaa3af9b8 | -2.74269 | -51.83197 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 13fb8b14-b32f-3886-b990-d64944cdce0f | -2.25898 | -48.81246 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc949dfd-325f-3353-9b1a-1609198d493f | -1.38541 | -51.55568 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56414d39-9e79-3901-bfed-eaab9b2f994b | -1.47686 | -53.48447 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e7b691a-407a-3e7f-afc6-d6454a131658 | -1.13666 | -51.68198 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fcb666b-5687-399b-8aa3-e5259f19ab3a | -1.90619 | -53.3344 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 43cb6c90-bf2b-31cb-99b4-bf43034a7d46 | -2.69473 | -51.87934 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecfece4c-c68d-3799-8a48-eb0eb82e3b4d | -3.58335 | -53.72413 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c215c95c-4c6f-364e-ba34-db1cdb0f6af0 | -2.89202 | -48.27979 | 2024-11-20 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a948c82-0907-33cb-b935-913618eae2f9 | -2.95148 | -48.33109 | 2024-11-20 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94bd71ce-1a00-3195-9136-88f09e839ee5 | -2.99829 | -45.43949 | 2024-11-20 05:14:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bbbe0d1-e434-3a23-a28a-268f5544bf0f | -3.38269 | -53.27231 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3a64221-d904-3a02-a422-cee4fc941ce2 | -3.80576 | -47.8072 | 2024-11-20 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e6b8cb41-74e2-34dd-8dae-51eaacd589c9 | -0.48643 | -52.08061 | 2024-11-20 05:14:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c280598e-df46-31a7-9667-8b1869e304fe | -0.90459 | -51.72875 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49012815-cf79-37a4-94d9-b577d93642bb | -2.91911 | -53.0618 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2fe56344-8a3c-34b5-8794-42d5de0de7db | -1.37413 | -52.08012 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdd9d673-7c16-3509-862c-a20b516a6706 | -2.62472 | -54.26742 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce824656-a6e3-3746-8e27-0ef58610ca6a | -1.63656 | -52.68538 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 319def60-55af-325c-b4f2-7e1d0aac46ce | -4.1074 | -51.04873 | 2024-11-20 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0edd15fa-42e8-3da7-85ff-002b4f9ae149 | -1.60087 | -54.45304 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3181d25-5a80-36b1-8b43-5a7f31881878 | -1.32347 | -52.39994 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| e6883f30-0c3c-3873-8024-67f59349dd63 | -3.20051 | -54.32872 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d1670174-7a69-362a-9681-9013e669a73b | -3.08598 | -54.67027 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1d78865-d216-362c-b77b-d4a383ac9110 | -3.06345 | -54.40808 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13fc248b-e845-3f1a-96a5-13c2ae4f4418 | -1.86237 | -47.81995 | 2024-11-20 05:14:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb5831e9-0eb7-34d0-a1f7-61f4a9fa6732 | -3.1964 | -54.32557 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71fb8ebb-519b-3ff6-9100-a1030fc6a0d0 | -1.7202 | -53.26598 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd7511d3-fe02-3171-a87f-e6b180ca6d9d | -1.52324 | -55.48962 | 2024-11-20 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6234f055-6bc5-38ed-9a41-091d01315506 | -2.03541 | -45.79624 | 2024-11-20 05:14:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71c4e383-153d-3a14-9929-0bc40f35ab15 | -2.46201 | -53.94286 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f5cb3f8-693a-3c3d-ac6c-462ea94087c5 | -1.86178 | -47.82387 | 2024-11-20 05:14:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59752284-6997-3aa5-9113-1c3ed7d9f4d5 | -1.4593 | -52.67395 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 357487b7-81be-3acb-86df-68e5a26920c8 | -1.04953 | -51.74566 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6de12b9a-03f0-3435-ac66-5d2cf32ac186 | -1.48163 | -54.44929 | 2024-11-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed844dfb-93a2-3f2e-9408-c0527dc17a3f | -1.51709 | -51.15818 | 2024-11-20 05:14:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a366809b-d7f1-338f-aafd-9780536ff1d6 | -1.23563 | -52.0242 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40b9b825-5220-3ee8-a7d7-3c213e06a5b8 | -3.34287 | -53.30889 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d88a00d5-8042-3236-9a38-c09659c0f096 | -2.61725 | -45.90031 | 2024-11-20 05:14:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2c3e7189-e8d1-3273-bf25-01428bdb033c | -3.48187 | -50.31297 | 2024-11-20 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0afd693-a433-3600-909e-f576299623c1 | -1.2936 | -52.23789 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc9167af-f923-3ca6-adb5-a8f3a91fb4b4 | -1.14405 | -51.69151 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddb8ac58-158c-3844-ad14-dfb6ace4d472 | -0.33604 | -51.74562 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6824d3bf-f8b1-379c-ab50-d88d591d498d | -1.59605 | -47.14403 | 2024-11-20 05:14:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67f47527-9c20-38e8-aa14-035a4b858803 | -3.28682 | -54.11636 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89371df9-cef3-3771-bdeb-b46b07d6c9a5 | -1.9344 | -52.99481 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70df73b7-04cf-398f-b18d-cf59dbbc4e83 | -3.88311 | -52.2364 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb8d30f6-cdb1-37ec-962c-85f029c89df1 | -2.92666 | -53.06649 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| d6c02232-1ac2-3095-9ecb-a6b210a991fc | -0.7755 | -51.75078 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d394553-fe33-3ffe-a873-dcec93cd096c | -3.53297 | -54.63303 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b526cc6d-c0e4-33e6-b8aa-ca9e86e0587d | -2.79812 | -51.7925 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 813a9c9d-44ac-3309-9190-54ad05e2cbb6 | -2.30672 | -48.49744 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ac90f47-9d17-3246-b3d6-2efce91689e4 | -3.51531 | -53.80424 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d407841c-5454-36a8-9a4d-2f40e920d305 | -4.44643 | -46.5955 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 290c0a50-97a9-3681-807a-92440a64a0b1 | -3.19676 | -54.3281 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b75a8c2-22ba-3cc6-905d-e5a2621c3705 | -2.2178 | -48.77422 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a593b22e-5fb2-3779-ac09-c51e26b5d0f4 | -1.63711 | -52.68177 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f60b7159-43b6-3f2e-8faa-fd120221e82e | -2.56932 | -54.07536 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eaa27cdc-5cfa-31ee-8c54-b0eed02647d7 | -2.22087 | -46.47882 | 2024-11-20 05:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e856047c-bed9-3e2e-8df7-4c6e4531f72d | -4.07833 | -50.04212 | 2024-11-20 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b8ea487-d118-3b2b-ab6a-65faf4e28e36 | -3.05599 | -54.40695 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db54b32c-d032-315c-b6f6-7204ef85cfa0 | -3.10377 | -53.10729 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f947a59e-b226-34fe-8d76-666975e75e48 | -1.64173 | -52.67879 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a576559-bb96-3798-941e-5782a7d0a23a | -2.54123 | -54.27953 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e34d504-2c4a-3ed3-9408-0f6fd9d1bcdb | -2.57169 | -54.08498 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67ce210b-2759-3eba-b9e3-717f21621d86 | -1.44681 | -54.50606 | 2024-11-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2863e0c-6ce2-374d-aa1f-cd4c06b4eff5 | -2.21625 | -46.48124 | 2024-11-20 05:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d214f16f-3ae6-37c6-a419-1ed35706aa60 | -3.11037 | -54.28519 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c343b87-b832-38d0-bad7-e7327ed33f02 | -1.24643 | -51.78529 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b40183d4-5bd5-32fc-ac30-2544df830443 | -2.20842 | -53.71016 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcb4e7db-4eb0-36ff-930d-61e5573cb106 | -1.63666 | -52.62994 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7ef949b-c3bd-3af4-810d-a0ff52e0d94b | -2.59374 | -54.01839 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 338d6d49-c1c0-3ab4-9b9b-8d5a8e668e67 | -4.44719 | -46.59027 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 4d181745-8235-3c6f-8ab0-339539c0a05e | -1.62904 | -52.62506 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 247e33c8-bb1e-367f-addb-a1933614db88 | -1.20971 | -51.75178 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README73.md)
