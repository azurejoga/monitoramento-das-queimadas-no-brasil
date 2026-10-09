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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2dcb523-b21e-3873-88b0-0f709fa8749a | -4.49943 | -42.54287 | 2026-10-09 04:25:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 21883688-475b-3807-a5cc-da56f07f8599 | -6.96085 | -45.2793 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b80707b3-d71e-3efe-b4cf-22104453d42e | -7.17935 | -44.28028 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b2d7f28-6a2e-3526-a7e8-f1d7ca99aa8b | -6.14983 | -47.92461 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa02c244-638f-3434-8599-3e070e96bdfa | -3.10191 | -53.95546 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b25f0668-2693-3af0-8c0a-890a8ae0050e | -5.16633 | -44.9424 | 2026-10-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf477101-9047-39f0-839b-2ddef09a61d9 | -5.10164 | -46.21571 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c73ad25-5379-3e24-9c2c-bbfb51d90d50 | -2.8824 | -54.18967 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 62cfcbdd-1809-38e1-9580-4e03426052d9 | -5.69745 | -53.45605 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1533b37-d1cd-33fa-9749-2e86d964a930 | -6.06908 | -44.10645 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47d0dfb8-baf4-3b41-9f5f-c1047aa5467b | -6.70107 | -47.38699 | 2026-10-09 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6e4b569-04fe-3d88-85f7-18a7ae5ee860 | -4.82044 | -45.83722 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa348f60-5a22-3c4e-8d1b-11fda1d0dda4 | -2.74217 | -48.42878 | 2026-10-09 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b7a89389-52db-36a0-83dc-0446902bd235 | -3.27149 | -54.05051 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 655be757-130f-3e6b-ae44-d2bb70a92a70 | -6.96858 | -45.25112 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a2e9244-d8f8-3dac-b2b6-96569323a010 | -3.25155 | -50.40377 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5134ecb7-17aa-3bf1-82b8-982d94043ce0 | -4.07836 | -59.84444 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b1f5223-8b71-3701-962a-6b681731c3e3 | -3.00752 | -54.06285 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e64d82b-a7c3-3700-9ddc-6df235bb2e6b | -4.42906 | -55.16249 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e4162ff-a536-3a27-915d-5d74a979039f | -3.15629 | -50.59209 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4663d19-e851-3e04-8920-6935d5bb5d57 | -1.41804 | -54.62072 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db724728-51aa-32d8-bd94-bf8687c6de77 | -6.46308 | -45.79718 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68cca8e4-b312-3a5e-acb7-4483c0c06314 | -3.43191 | -54.54213 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da064683-3a42-33ad-ae62-5bd0c47927ea | -3.17417 | -50.45849 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e56f029-55e3-369b-97d1-b789e1ecffc5 | -5.7057 | -53.48446 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 596cafea-0cd6-3cdc-8207-5f128733ec1a | -2.57344 | -56.18414 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 238f87b7-d107-35c6-9770-4e8b096dcbd0 | -3.50012 | -49.94007 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2db95947-b55d-3257-881e-228a96673cfd | -3.03499 | -54.0792 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b816894-03bb-324d-9170-26e3eef2c664 | -3.29514 | -54.001 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e9c78ed-b7f7-37ea-9117-41a2a44109ff | -2.94086 | -54.1527 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a1dd1a9-67c0-3651-9498-fd7278681e49 | -3.25626 | -50.39942 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 103152f9-f311-3a1e-9a72-4e3a73f058c7 | -3.10287 | -53.9496 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e9cd9e95-c7d4-3c7c-9836-6ab0a649078c | -5.10494 | -46.21622 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15332327-9525-30c6-8e90-495d5abed0a4 | -2.99614 | -53.84876 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f567e035-cee3-3d07-9b83-afa2c5d1860e | -5.102 | -45.66608 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd14cc3e-446d-3cba-9b8f-bc324e5c6dcb | -3.60501 | -54.67049 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef545bde-c5d6-36d1-a040-7df1775ec708 | -3.49261 | -43.3414 | 2026-10-09 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d1b8ad9-2d9f-3468-a20b-14d1fab53cea | -6.679 | -46.94555 | 2026-10-09 04:25:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67a7788d-65a8-3359-afad-1ffca99f917b | -3.11807 | -54.16681 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 19c97b1d-a7b5-32ff-a01d-2d0c7dc48192 | -2.93008 | -54.12338 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3473190e-9d3e-31b2-a3ec-662984b67927 | -3.21055 | -53.85921 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e1beb18-ab42-3aef-b661-0029c8ddfcc4 | -3.18578 | -50.58619 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ada5797d-3083-3faa-99a1-d4202dcc91c1 | -3.94895 | -49.01075 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 759cfe9c-f56d-3791-8328-2cd666b40b74 | -7.18282 | -44.28078 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cdd0023c-baba-32c5-ad90-e564bd5d1f48 | -3.28258 | -53.83139 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1e6fd55-3386-3e6e-b1bb-de30ac437445 | 0.5046 | -50.77788 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 66503d42-8e2f-3ce6-98c4-465264b85ad5 | -5.70206 | -53.45695 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c4183e9-c8f9-3bbf-864d-87ecc7c35cd5 | -3.03055 | -54.10577 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 500c9b25-9c40-32f7-aa5a-90909fb5616e | -3.09209 | -51.37376 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3749960a-140c-35b9-9037-083ec7dcfb23 | -3.30682 | -54.0237 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c967674-0595-31e4-aa19-c991eef5efd6 | -3.01113 | -51.01897 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b37e2cab-461d-336e-be40-e8ff4478b0bd | -5.99994 | -40.97132 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 77ecf57f-1890-346c-87d3-aca4d66b19dc | -3.26547 | -54.05569 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afbc1be9-29a2-34d2-af2a-78fc0fcb92ed | -2.883 | -54.19796 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e715d40-8c5c-359f-9dc2-7a0a8bb433b5 | -2.84594 | -54.13648 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea88ddd4-9861-3557-a8c9-449b0e7eaa14 | -5.09942 | -46.20833 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31a2d056-4b5a-3682-bc7a-1ebef68a6af1 | -3.89735 | -58.96152 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 349955af-5ca2-3f58-96d8-22ac10b13200 | -5.39746 | -45.91022 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c823992-9e0e-3db4-b941-52969b4274e9 | -5.68489 | -49.0409 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ccfe74-fd97-35b0-ac84-0077d3f457ae | -6.18746 | -44.11229 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 123d34fc-3a42-310c-9d79-13ceb392c6b5 | -5.5615 | -47.49125 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f1861b5-f420-3835-bb14-d3fcba56f45c | -3.17219 | -50.59459 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83263cea-a8cc-3eaf-9ee1-9214a841c442 | -4.28169 | -48.60441 | 2026-10-09 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06434e3b-76c0-34db-be0e-c9249be39574 | -3.74697 | -49.38988 | 2026-10-09 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 952ca518-3dcf-34b0-a680-a4a89c3c0c15 | -5.61729 | -44.83955 | 2026-10-09 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 381d5acd-0858-3e47-9ba0-3737b6824463 | -5.63877 | -45.80262 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e4138df-fa7a-36df-8abc-7795b15ad5fa | -2.47295 | -56.07262 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8f353fb4-dd9c-33f8-902b-3a6b3045c4f5 | -6.05867 | -44.03451 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a644194e-0398-3cf2-b2fc-a9b0a07004ad | -3.56294 | -54.66122 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccb4fe27-2b9f-3b94-b121-c5102493822f | -3.0888 | -53.94155 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd735bef-91fd-3e56-9a38-5a7f18113f06 | -3.12216 | -54.17351 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| d71fe024-8c5d-3b29-b405-ad2abfba513a | -3.53644 | -54.65967 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7cec52e-8031-3ee0-8292-c969091fcd7e | -3.53558 | -59.4072 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ba15e771-14f1-3dbc-8c5d-f5167c9cb7ad | -7.06755 | -44.34641 | 2026-10-09 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab6cb9f9-8030-3ade-9f78-f624b562fa33 | -3.59856 | -54.58216 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dfd25fb8-1e49-3328-881b-38b23b376ceb | -5.70684 | -53.45044 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11c1a3f7-d8c2-37e3-81d5-30a3acab98e9 | -3.59083 | -54.69109 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c7206d2-5755-35a7-9667-5c6b35e97f30 | -3.20593 | -50.56223 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59dc46e4-8f52-3974-a810-c8499bd20a5a | -3.80205 | -50.61147 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| feb9ecd0-5be4-347e-9650-c1ed81accf08 | -5.96066 | -46.37973 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e83320cf-11d8-3cc6-9440-58a5eda4a487 | -3.74171 | -59.44594 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4b00343e-c6c9-3b1d-b721-71dc4b575a2a | -5.41539 | -44.62409 | 2026-10-09 04:25:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5c5b276-760a-34d9-99f9-7d1224c9e775 | -5.96967 | -49.70762 | 2026-10-09 04:25:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c66e63c2-ad53-30a9-813e-19b0e2473b9c | -2.99241 | -53.90257 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d6e1c1f3-e310-393e-8393-097c2c91196d | -4.7464 | -55.67207 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 40df4c25-0bed-3948-8982-58450f8c2a7e | -3.10483 | -53.78273 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 31a4a5c0-c686-35a4-af6d-e95fdbf398a8 | -1.5525 | -54.55899 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19572020-9aa9-30e3-9bc0-0f45f97c267e | -3.56222 | -54.67024 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 366ced7a-ceca-32f3-870d-ca12ea489f9d | -3.82696 | -55.97628 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2bb931d-6a2b-37c6-b640-e671dd93d302 | -3.16821 | -50.59397 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 340dafcc-d263-3501-b402-18ec9269d60b | -3.10959 | -54.19525 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 036e8c13-15a0-3d14-8b24-5e84cac75a60 | -3.30372 | -54.01125 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68463a72-6514-32ae-930e-a2246626645e | -3.89892 | -55.89302 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 000b5b3e-0fba-3a02-8d19-4280c1a9e591 | -6.49857 | -43.95146 | 2026-10-09 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78cdc0c3-aa42-3d5c-9ef0-7ecda6ff53f7 | -5.73305 | -42.07666 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 92003302-0eb8-37bc-ad54-4b18f2caf35e | -3.11658 | -54.17566 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| afbbc812-b1b4-3519-b1ac-7cf49d23d162 | -2.74652 | -54.11633 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a07464f-1b77-311f-ace5-4e73ffa43c34 | -3.01825 | -54.05542 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 231929e5-35c1-3106-afd9-439c3dcaeccf | -3.00448 | -54.11391 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 089101fe-e10d-3487-97eb-aa46b2f08770 | -3.48694 | -50.49242 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README83.md)
