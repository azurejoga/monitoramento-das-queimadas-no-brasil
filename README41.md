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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dca0bc00-ebdf-3dab-94b9-953513ed89cb | 1.04568 | -54.64638 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c2dc092-040e-3cb1-85ab-26b10fcaecb7 | -2.82635 | -46.65793 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52f6f701-61a3-33e7-8d00-140966c6a6c6 | -3.40564 | -50.31214 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5f57294-6525-3fbe-9053-5d941555169c | -4.24306 | -46.55173 | 2024-11-14 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63b40f13-7f1d-3ca2-8ecf-58b5710b53ce | -2.83749 | -56.78712 | 2024-11-14 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0626f766-da22-363e-8a58-5e356411553d | -2.164 | -50.65279 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6600adf3-6090-36d0-98f4-23ae01a3989b | -1.3835 | -51.56662 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba605c88-00b3-3777-a0c9-f1df973957e7 | -2.93355 | -54.45903 | 2024-11-14 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f55f9f9-085a-392e-8419-6c6f34cfa3cf | -1.21114 | -51.77652 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b5f0228-37bd-3040-a1b1-d6676071097f | -3.22239 | -50.58961 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ffec99b-25b9-341a-a3e6-1619894de972 | -4.03068 | -44.68145 | 2024-11-14 05:01:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf3b3667-2180-359e-a5e6-aa27aa04400f | -1.38874 | -51.12006 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b4f8a15-d947-3a72-b4a5-a639a418d35f | -3.23537 | -50.66806 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8925e55a-d3dd-3c11-9b53-8318b17e8d3a | -4.13116 | -51.0733 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a3a8ed8-277f-30ec-9441-3e74bbe2b87e | -3.88879 | -46.09365 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b910ee58-04a7-3d28-9866-b9c419a39e23 | -0.41256 | -51.57521 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f44032e-ea04-33a3-a529-1a9e3b8a3f90 | -2.69536 | -51.87482 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64b34ef5-a550-3198-b572-686d6e7f03be | -2.69895 | -51.87537 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2c1afe1-2039-306a-b8e5-e51ea059db4a | -2.67404 | -46.98941 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d374d11-7162-3343-b1aa-8a0b1d77fe7a | -2.37054 | -46.49789 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e61b038-d15e-31e1-a142-0a9a92b4de09 | -3.78267 | -46.05413 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d8fe5a3-d8c3-366f-8ecd-5137a46b442a | -1.55785 | -51.86268 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e091fc39-8674-30ba-8eb9-196daa9007a3 | -0.33899 | -52.02637 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48cbcaf4-5da6-3474-9088-e1e69fb51155 | -1.24582 | -51.75694 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c166359d-01ce-3a1a-80ba-705c37cc752c | -1.27093 | -52.17261 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7afd95e-6931-361a-9dbe-0cf4dd3666f6 | -3.05221 | -45.5233 | 2024-11-14 05:01:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b3d3cb2-910d-3b7f-a253-a430d7449b8f | -1.39241 | -51.12062 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a35f3997-c7fd-321e-9b95-18fc01efbeb9 | -0.80618 | -51.48487 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 709f6c5a-c0e7-34cd-b269-e31a75d53158 | -1.79756 | -52.17516 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b4e50ce-db8b-352f-a7db-413564c32f4b | -3.80459 | -44.85798 | 2024-11-14 05:01:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1becb3c6-be19-33af-b745-afbcda67da81 | -3.49167 | -50.84237 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f8c296b-7a7f-3224-8ca3-98eb1e98055c | -3.484 | -50.84117 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c323ca63-573a-35f9-a63c-9fed9bff9b62 | -1.38418 | -52.07481 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f03bca2-7423-3cb7-8e4f-7133c3395435 | -1.35353 | -53.08563 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a592631-5842-3190-b366-a76a50a54048 | -2.78321 | -50.29902 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d007ecfb-67d1-3df5-afcb-7077697b2a3d | -2.83689 | -56.79083 | 2024-11-14 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dceae0c-ef86-3d2f-aed1-3245e70048b2 | -1.79695 | -52.17904 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fd93b35-329a-3be0-9576-e2ca95145e77 | 1.07504 | -59.2429 | 2024-11-14 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4fe5b79-bae6-308d-87f1-cfb5bb0ad268 | -1.46286 | -53.5029 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0a60d71-cb03-3c4c-926b-1b27876ccc66 | -1.55846 | -51.85872 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3706d4f-20b3-3762-8219-46196e3b05db | -1.21051 | -51.78049 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dfea8a1-c0ba-370b-b213-5d73413574e5 | -1.61077 | -52.24179 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f837a742-f7e3-36fa-b094-070b9fcfdb9c | -1.55553 | -51.85421 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 096085cd-dd58-38d4-abaa-f46f63e5bded | -0.2036 | -51.50364 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d752277-24d5-3426-8096-4feee7fd4ffd | -1.22263 | -51.74979 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b58da4c-da30-31fb-a507-ab06058326f7 | -1.17698 | -53.74867 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1c3c892-db80-37cb-bd54-4add8343c1ec | -3.46849 | -50.31321 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3df777b1-336c-31f2-8176-a3c16c86ff82 | -2.6485 | -46.16998 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eceb2305-f4af-3869-ac21-9ae18f6c214c | -1.63918 | -53.26887 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5630c24b-cd3f-3156-8477-2dbf50052716 | -2.902 | -51.79455 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95648fdf-5477-31a9-a519-4938f5adadaa | -1.25401 | -51.77452 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a564524-9854-3db3-92e3-ef5063e9bb98 | -2.66352 | -51.72293 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6891207-d89a-33bd-bb05-c404e6ec5a03 | 2.26263 | -55.92429 | 2024-11-14 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 889aacb9-f810-3abb-b8c2-b5fa002c38b5 | -0.90107 | -51.75219 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 973da719-7899-3d25-9b41-ba9347bb38d6 | -2.12324 | -50.68916 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb4daa83-d02a-306f-9a11-ce9cdb2e4b0c | -4.35299 | -49.68235 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a3602067-22c2-34ab-b651-3cd0f7518c86 | 0.846 | -50.2081 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cb2cdb8-7fc7-3696-8562-8f6fcbcc7264 | -3.16763 | -50.45158 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccefa6ef-cf0b-3f09-8d35-57266453f913 | -3.40833 | -50.30914 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 494c9132-2fee-3228-9bfe-785f0451a393 | 1.07035 | -59.23986 | 2024-11-14 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e5a6a47-474b-3926-b334-da35fe7912fb | -3.16363 | -50.45421 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58316635-b6ef-355c-af71-2db9b1acdc1b | -2.89258 | -51.68702 | 2024-11-14 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9583b3e9-e0cf-3761-a952-2ac87d323853 | 0.11932 | -51.33931 | 2024-11-14 05:01:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf718025-fb31-3824-8697-bb1f22c31563 | -2.99929 | -51.45619 | 2024-11-14 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89d65de2-d6c7-36bd-8db7-6b7a84b15ccd | -2.20586 | -53.75074 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1952518-b15b-3b8b-bc0b-876d1e1876cb | -2.83808 | -56.78341 | 2024-11-14 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d42177cd-c538-3c72-9810-16d8912b39bb | -2.15097 | -50.90999 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18de633b-6659-39c8-b770-a6f42cb0f68d | 1.07561 | -59.24659 | 2024-11-14 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3a87047-99fd-375b-bcf4-96393ca1cc12 | -3.80977 | -47.80287 | 2024-11-14 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d3b941cd-2b73-3a4c-ab30-bd009c0c9795 | -1.25046 | -51.77397 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77df1626-2541-3062-a29d-0001f4aac341 | -4.94222 | -44.95868 | 2024-11-14 05:01:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bfc8fd1c-1d73-3c88-97b7-9d1e9611f575 | -2.20696 | -53.74373 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df04b171-0643-3b78-9e11-d0ae8e66c215 | -2.22089 | -50.85613 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8de326c3-74d8-3afc-ac87-c827002b636c | -2.12704 | -50.68973 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47ee17cc-9183-3421-9be7-cd41001aed18 | -4.59402 | -47.03925 | 2024-11-14 05:01:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 972e1910-c297-3a0e-abb2-e72f346d6dd5 | -2.37172 | -46.49725 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd751e87-83c4-3978-b28b-f57e1abc0c99 | -0.19392 | -51.50365 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82f10aa0-0caf-3aeb-9e95-3628c4521c89 | -0.41904 | -51.58029 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bc2ab16-76b3-3c7e-8e66-e560edb40852 | -2.63591 | -49.52528 | 2024-11-14 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2651caa9-daa9-30de-aaef-3434a016157d | -4.15516 | -46.24209 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 008e9dbd-97b2-397e-b1ad-d95f6be8c96a | -0.19265 | -51.55086 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a54458c-e4a8-3f84-a6b4-e2ce839df361 | -4.43035 | -49.68229 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 747be84b-35cf-3487-a793-d97370af366c | -2.67017 | -46.81323 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e1cc57f-d6af-338e-9b14-497dfcfc1ef1 | -1.64255 | -53.26938 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0cf13e63-e2df-32db-901c-bac36f63f186 | -1.35464 | -53.08563 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a580a954-ba9b-3191-b5fa-2ded9701f1f8 | -3.95409 | -46.41217 | 2024-11-14 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07c5111c-de34-3da0-bc2f-5268b6b59ce9 | -2.15656 | -53.64945 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 476cba8b-a5aa-3803-b1f4-4b619eef7ad2 | -3.05106 | -45.52973 | 2024-11-14 05:01:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8544db66-74be-327a-bd0c-51f3ed90af44 | -3.4096 | -50.31274 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f834d7be-7faa-3996-b809-cd5c2a78ebab | -1.33691 | -51.40524 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e4a25f4-b696-32e7-98d3-15f310d8fa11 | -2.69958 | -51.8713 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fc5e448-18b0-3d57-96aa-d7083350e7b9 | -2.71731 | -51.71002 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac6b8371-b751-32b1-8b54-fb207d4e8553 | -3.23369 | -50.66994 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d2a0b13-e2a5-32c1-8ed4-b432a7e8996f | -3.49311 | -50.83297 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19021c8c-323a-3f9f-8633-204af92d1f6e | -2.64178 | -46.17185 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddda3778-0a0a-3ffe-84c8-178c46811e08 | -3.6744 | -50.16121 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 742ae0d9-cec7-33f7-9cd6-6d8abcb6b794 | -0.01663 | -51.14254 | 2024-11-14 05:01:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c69e425-a74c-3eec-b2a3-bb8dfb8d6590 | -2.28874 | -53.80272 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ceac773-a379-39ff-966f-5bb1b67dae1c | -2.70967 | -47.7285 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73c8cd59-faa9-3f35-ad6e-0181bd248ba8 | -0.93707 | -51.72836 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README42.md)
