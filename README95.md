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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b91fece-2547-30ee-92a7-45d37783a132 | -2.92501 | -54.12255 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9d531e2-7fdb-39da-9e06-ce1b440b5726 | -4.53497 | -49.66817 | 2026-10-09 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15087244-993e-3232-950f-635958ff6bce | -3.10271 | -53.76491 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 121d2a2e-6a59-35a7-9a99-238dc3db22b9 | -3.54379 | -59.4016 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fc73206e-e507-363d-ba39-5ccc77e4a290 | -4.58309 | -54.95147 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45f30804-79ed-36bd-8a5a-4299d6828bb0 | -1.10311 | -54.17563 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 65e87f96-8845-3786-9279-8501ccced1df | -3.12313 | -54.16771 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dedbd67c-0226-3901-9516-a678ee6169f3 | -3.17701 | -54.74622 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9dced49-559e-3245-9b85-57c187409c90 | -5.996 | -40.94042 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 29787d29-b36f-3825-a0cb-801930bde70b | -3.19569 | -50.55014 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fb332e8-b83a-3ed4-9a22-33eeeaad5493 | -3.10383 | -53.94378 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b0332a87-b8a8-38fc-b952-126415cdbf80 | -3.08429 | -53.9378 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8eedbd8-5356-3a67-9008-cf85bd978be0 | -2.09284 | -50.4096 | 2026-10-09 04:25:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 009aeb93-b294-3047-95c9-22e28d7fbe6f | -2.77462 | -54.07172 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 298582ac-499f-3d7e-a646-a8ca8c565dbe | -3.59856 | -54.58215 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41f49049-9fb6-3061-998a-fb189d002f1b | -2.89155 | -54.16646 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b23bf8ed-279f-3e84-877b-fe51f33c6a2e | -4.22229 | -59.54574 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08f1ab9c-ea3a-3abe-909d-6845d037e40d | -3.00597 | -53.91363 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 98105086-59da-3f99-a5ed-e18d073efca4 | -2.98322 | -54.11675 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22b8c952-aacc-3381-b41b-0576a0a21af0 | -2.82255 | -57.13741 | 2026-10-09 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4405d8b3-4f16-3e46-911a-be6af66d23d1 | -2.90071 | -54.02353 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94d057b4-b8a1-338a-876a-d043d0f406c5 | -3.08458 | -54.30321 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7046892d-d107-371a-8ce2-1a711a685f90 | -3.58874 | -54.57729 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0abe0adc-60f8-3979-b09f-7ca220b2a2e7 | -2.50581 | -56.1615 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 802a8b38-d746-32c6-b622-23f8a73ce262 | -6.14703 | -47.92047 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| feb567c1-5532-34cc-9173-19cca5963e8d | -2.07745 | -46.57597 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c8c16b6-28fc-3103-9298-418020ceac29 | -3.271 | -54.05341 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0de6d44-b9bf-3293-89b3-f95d0025a253 | -2.56946 | -56.17626 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20c519b8-ad80-3046-9365-48d045a5fd7e | -3.17348 | -52.15906 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 029e75e9-ecc9-3b67-90e6-68613762902d | -3.08454 | -53.96741 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bad023c7-2459-367e-a2f0-61725596efdf | -3.10617 | -53.92949 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00047c55-cc51-3a82-a702-14db1dd1772f | -3.65597 | -54.52456 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3fb401f1-97b8-3485-82ce-9412d4af38cb | -1.77634 | -55.02191 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 171119c5-22bf-347f-b66c-581016f59cc1 | -3.22019 | -53.8936 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ca3cf68-3ad4-3fbd-bfe7-c60e2c6ed9c1 | -3.29969 | -54.00454 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa4630ea-8cd6-3e8f-b73a-2f6caac55faf | -3.11475 | -53.78407 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ed1d3268-dabc-3012-83ec-d956ab5a52b3 | -5.39416 | -45.9097 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89fdba83-8c51-357e-9264-eec7ecf2317c | -4.40769 | -43.11757 | 2026-10-09 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 715f2ee2-549d-3288-a680-8a21c3f933cb | -3.93913 | -55.71512 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 841083e8-5445-3911-b5b0-4aebfb491ff4 | -3.10893 | -54.19007 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 50334e07-ab24-3e92-9dd7-3c2a399fbb2d | -6.45789 | -46.02715 | 2026-10-09 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 995a338b-7a26-31eb-94df-747d7b765a1f | -3.17442 | -50.58088 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8deb6143-2e4f-36b2-8619-9a6887ba6993 | -3.90199 | -55.89682 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 205abd54-033d-34d2-a211-5dc09d3669cf | -3.53593 | -54.66278 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 229fab2d-abc5-3e2e-9f55-f0d341f0b644 | -3.867 | -55.99796 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7cecfbc3-dc1a-3e67-a3c8-64fcde268b32 | -3.18859 | -50.54381 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1ecb7555-29f0-30a8-8a91-d4a8483c3791 | -3.01124 | -54.0663 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cec5a0f-6d22-319f-a00f-7546ad6b10b8 | -4.74221 | -55.66373 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 032b9de2-1452-3f84-9447-9a53d73f9f3f | -2.84036 | -54.13868 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85305009-de08-34a4-a924-b1e153dee110 | -3.52535 | -59.35066 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b44478e6-77ba-3ce6-8d6d-1083acce9c25 | -3.35479 | -50.41286 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e6ea8c4d-98dd-31cc-b0b5-7175c3b4ac8b | -2.37894 | -48.22521 | 2026-10-09 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e59afc0-ff02-389c-9f36-c17a90a2764a | -3.55324 | -54.69135 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3fc5ea78-9298-3f7b-969a-6558857f38ec | -2.3408 | -48.86426 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9104908d-022d-3262-b3d1-887e523c1a83 | -5.0909 | -46.13311 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2160a8d9-f7fd-32e7-b0c8-218d81604c53 | -6.01539 | -40.98087 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 478c0067-aeff-3a0e-91fd-3f916f2290db | -4.08175 | -44.12071 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27af0551-e31d-3e58-8d9f-42ab42f08e09 | -2.54665 | -58.03824 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 969222ee-8cb2-3c91-9adc-2ec3f9685ae4 | -3.01826 | -54.05541 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0250e22-edb5-3efd-8dcb-69ccf2ffd602 | -2.47097 | -56.08492 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 692a74e1-9728-394c-9970-8730f81df57b | -6.00711 | -40.97988 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 692a8f76-c589-3ab6-86ed-e558f8d217e6 | -3.25939 | -50.405 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03f2fdab-f68f-346a-8dd7-216334c2d9a9 | -2.99743 | -54.06125 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93805e23-b7f1-32a4-be31-436c7ab8a28d | -3.89985 | -58.95666 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cf71d865-44a0-3fb3-82bb-471d7d6dae24 | -3.99173 | -59.35936 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b0324478-9298-3a01-b36f-2fe59ba60f26 | -3.45419 | -45.26015 | 2026-10-09 04:25:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45eac461-cb54-3b3a-9fab-1dad5bd33195 | -1.10363 | -54.1724 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd79643d-6ec3-3457-b84f-22c11474af24 | -1.26458 | -54.68278 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b8e7b0e-e63e-3080-9ef0-d2c4addb1cd5 | -4.46379 | -55.40017 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 412476d4-8b00-3a71-8bf4-34d629f5eb84 | -3.20558 | -53.85848 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d46e071c-d6eb-31d8-918f-bbbbe09c00f1 | -3.01336 | -54.09101 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20ddd40c-f721-3f6d-a7d8-46b9056ef8c5 | -3.35087 | -50.41225 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9a3e5dd2-acc6-3441-89fa-2db443553fa1 | 0.50885 | -50.77721 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 508db4bd-05a7-338a-861b-42de34003d66 | -3.10191 | -53.95545 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09b95ead-71a8-3989-9258-abde98e7d5c3 | -2.75766 | -54.112 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b710ac9-9f24-3f3a-b7ac-8d2806691a81 | -2.97306 | -54.11528 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52900998-eb15-354b-bfff-562d17d76cd6 | -3.25982 | -54.02785 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aca7e3a5-9475-3a6f-9534-c5511b681d23 | -3.31078 | -53.69353 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb63b301-f18f-3dce-99d9-96ea86ec7d80 | -3.25527 | -54.02423 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75a1ff30-7d5e-360d-a5ee-e4ced973cac7 | -3.17575 | -50.45141 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b5c1ba4-a0e1-3ead-b449-466e61ca3174 | -3.54627 | -55.52501 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94b3ec49-8501-34c4-a41b-248508d51993 | -2.33325 | -48.87049 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 494d6a19-f68b-34d0-9202-5c3d96966746 | 1.69293 | -55.61085 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4da8ba6-9d9f-3944-9792-42edb44ecbc8 | -2.97939 | -54.07654 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b2316c8-56c5-3525-94de-a1eafc24770b | -3.57133 | -54.67544 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c541f65-8ff8-3711-90a0-4a37952a67b9 | -3.8206 | -47.48144 | 2026-10-09 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab4c5d45-998c-315b-a2f1-12497924b974 | -4.54808 | -54.96795 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff51cd90-6037-388a-9a07-437c011e5cee | -2.93634 | -54.05455 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67867fc7-ab14-3950-8591-e37f9ce5c286 | -1.52791 | -56.12347 | 2026-10-09 04:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 411dc400-bf50-3675-aab5-697f7cdf570b | -3.89956 | -55.88913 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1924683d-a164-3dfb-85ae-5f595ae55896 | -2.69853 | -49.37288 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 543b45b6-3828-3205-ba5b-42407c62a7e9 | -3.26127 | -54.01915 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c22452f9-c2d7-337c-9a13-6e63f9e59dff | -5.09899 | -56.19525 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2df1d4a2-4d66-3424-b88e-be85071cb6b2 | -3.15583 | -57.68133 | 2026-10-09 04:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80c420f1-062f-3959-b132-b58102898039 | -5.7031 | -49.08789 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef748181-79dc-3c92-ba9d-cfca99bee891 | -5.28429 | -47.91055 | 2026-10-09 04:25:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da5d152a-46d7-3ba8-ac31-e33f2747f065 | -3.74284 | -59.44922 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b9d70006-6297-3c2b-bfc7-3e8bbb746f3d | -3.57574 | -54.68524 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a338e88e-2e9a-3a7e-bdc5-da525f27b42c | -3.02092 | -54.04396 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8027606a-c4ee-3662-87cb-a2f590e688a9 | -4.11283 | -54.62885 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README96.md)
