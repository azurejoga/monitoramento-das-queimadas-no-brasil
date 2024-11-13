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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb47683e-d4a4-396b-96e0-0819d1d083bf | -3.14281 | -45.9818 | 2024-11-13 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbc7b668-ea29-39aa-9627-090e48ef0b8c | -3.30081 | -43.51346 | 2024-11-13 04:04:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6324ed64-96a9-344a-a861-1accf20075a7 | -3.94985 | -48.18011 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 663101f9-c730-3ee9-940d-21909824a2bb | -3.76239 | -50.69847 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6953ff90-9a6b-3c00-8498-de5e2d685c46 | -3.05816 | -50.34438 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a5234b9-ed0a-3f1c-ad71-52c32899d666 | -3.07152 | -50.33199 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9d8a939d-0abd-3a90-ac32-737133d83d47 | -1.77975 | -47.84265 | 2024-11-13 04:04:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 269268c4-0e44-3b65-bba3-a4eac92aeb61 | -2.73858 | -49.18784 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0360152f-9460-3b0a-abfe-582ae225fba3 | -3.25327 | -43.26572 | 2024-11-13 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 11cbb739-db20-369e-8781-11d6142b7761 | -1.96875 | -46.57301 | 2024-11-13 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f583a41d-b443-3bea-a023-6758a6f9e1a9 | -3.3576 | -48.98307 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 425c64c2-d9f2-386d-a685-39525223e133 | -2.66556 | -47.00559 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c07a03a-77d5-39b4-80ca-6a122fc01f99 | -1.34645 | -47.35005 | 2024-11-13 04:04:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 954d5312-6160-304f-936f-f581341c0ed4 | -2.11848 | -50.68536 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb2febdc-691a-3bfd-898b-963183cfcbbf | -3.14802 | -53.24743 | 2024-11-13 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 00302188-83d3-39f5-8326-9a56ad35f2bc | -3.8681 | -41.03552 | 2024-11-13 04:04:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c93249e4-1d6c-3c9d-a861-5c90128f44a6 | -3.35259 | -48.98123 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 16bedc0f-bb60-3e4f-aef5-c7aa00e7cb39 | -3.84576 | -40.72593 | 2024-11-13 04:04:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 250f8c9a-566a-3090-8046-654811bb3186 | -2.66118 | -51.72587 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b43807fb-548e-35e1-8bc0-13cb1afdca2c | -2.11584 | -50.70115 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6b7ce84-83b5-31ce-9637-6a05079f33d8 | -3.87542 | -44.24763 | 2024-11-13 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cda668ea-0a44-312a-bd59-af6c2792d647 | -2.73176 | -45.29227 | 2024-11-13 04:04:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 841d427e-ef4e-30ad-a289-a2dc6ad5495b | -3.93997 | -48.15323 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 569bc196-4658-33b2-80b1-d28be251f2ea | -4.36331 | -44.10957 | 2024-11-13 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff033f06-4e55-358e-a80e-63c3c3511863 | -1.64702 | -52.54055 | 2024-11-13 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 167acf33-0fed-3b39-839c-42e7913d01da | -4.74181 | -44.10411 | 2024-11-13 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20ddf896-8322-3c68-a05f-efc828438870 | -3.76609 | -50.71042 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4864dccc-e681-3e13-b5fd-3b4a1d4f5788 | -2.11013 | -50.70023 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42376cd0-fb1f-3457-9348-56ff50e71456 | -3.85854 | -49.12075 | 2024-11-13 04:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f7aea81-345a-38aa-9b7f-5fff2c4ac84e | -2.98108 | -53.98183 | 2024-11-13 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2fbda90-dd16-3913-bef4-cf8121fc5f29 | -3.34557 | -48.96341 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| a79d1091-dcbb-3c2e-bc6c-c2da8bbb815d | -3.06673 | -50.36069 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 038be784-0dda-3b8a-a3a1-384fbae223a0 | -4.36912 | -44.10757 | 2024-11-13 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8a1866ae-47af-3abd-9de7-07ea695302f1 | -2.31001 | -50.68438 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a17c3955-e737-32c6-a3e5-9861b52af292 | -3.75991 | -50.71313 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c1af784-0a67-3fe1-a8b8-aad3829367b0 | -2.24619 | -53.76227 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e3cc526b-8ce5-3a21-8635-d87b8f48275d | -3.31477 | -40.03791 | 2024-11-13 04:04:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ae5a796-5e16-39b8-a368-b89586a4b3a6 | -0.03578 | -50.78082 | 2024-11-13 04:04:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f15c5d6-a4c8-32ac-bd0b-886f5d507560 | -1.40063 | -51.11035 | 2024-11-13 04:04:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0855e6f-df57-3f45-9299-514c0f0f3138 | -1.84596 | -46.28661 | 2024-11-13 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ae54a6e-64b3-323f-9216-cad35b494b7b | -2.78204 | -50.3027 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b9181db-0948-34d5-966e-31565179f439 | -4.70855 | -42.78502 | 2024-11-13 04:04:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71a593ab-2024-3d9d-a3b5-91f0ffdb489a | -4.34233 | -46.55156 | 2024-11-13 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a04784e3-7e76-3c1e-b333-1fe6bbf3f92c | -3.0121 | -41.12304 | 2024-11-13 04:04:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 12f09f77-10cd-3a22-b64d-bf87bb5447fd | -3.33695 | -48.98288 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2362d46b-87f9-300c-a0b5-28802e9a215b | -4.04426 | -48.10055 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5b624006-30fc-3a4e-9f39-39e36bab0789 | -1.28409 | -52.47921 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2795978-39bb-3f36-b560-5ceb5e1b109c | -4.19731 | -42.33266 | 2024-11-13 04:04:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1742bc25-bb48-3084-b4f5-760387542ee0 | -3.31678 | -47.0213 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e50c8f2d-6bba-39e6-8035-d821d308f83d | -2.36636 | -46.98947 | 2024-11-13 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13e6bdac-b979-346a-93ea-41bccbb225d3 | -2.98338 | -51.35431 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0664f8b2-3fab-30d4-be42-3f1a45349532 | -2.53011 | -46.2076 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b19650a-e922-386d-90bf-7ba38c9e8059 | -3.76425 | -50.68747 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bed08da6-2f18-3f50-a7e9-12dee96a94a4 | -3.33766 | -48.97977 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c147c987-a36b-3863-b2ed-4ef41f9856f9 | -1.86446 | -48.16696 | 2024-11-13 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 089a3514-d6fa-3c59-a43c-0d71253181bf | -3.35758 | -48.98205 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e9613e3f-90c0-37e6-8377-5619f1e29778 | -3.15809 | -50.59362 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e98b308b-1f39-392e-b9b2-6d7acebe70c9 | -2.3921 | -53.73642 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 766cef83-1bd8-3bd2-912d-625d37675c62 | -2.60717 | -48.25103 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65bccb6b-126c-3dfa-96f8-e2377531095a | -1.83073 | -47.80511 | 2024-11-13 04:04:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4839c6b1-ec72-3d14-ac44-f09dd97a7302 | -3.763 | -50.69488 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 09494e0c-76b4-3482-ad74-13991645e02b | -4.4208 | -45.94963 | 2024-11-13 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a881437-edee-3ba6-ab0d-50328acd2b4f | -3.42074 | -51.05733 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5818f2f-539d-30a7-b827-6951a9f2074f | -2.11783 | -50.68923 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad13d9cc-46a2-324f-bb25-9b5dbfd0c1bc | -2.98944 | -51.03508 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| af61563b-f9dc-3fad-b5e1-7b049cec1b93 | -2.99617 | -51.03479 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a448dea5-53eb-39f2-91ea-23c64c8a6bf6 | -2.30306 | -49.08732 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c655c3b8-ca08-31c6-aca7-1b9ba710160d | -2.99453 | -51.04012 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 55a4bb26-5e7b-315b-bd5b-27e340317863 | -2.11655 | -50.68513 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dce5aa44-07e1-3918-984f-b419faa92d80 | -1.28402 | -52.4782 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e97d49bb-a69f-3b76-8886-14e5d723a080 | -2.65514 | -51.72486 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4680ac85-ae86-3d10-ac65-e5ae36a1ee6e | -4.04242 | -48.10295 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a2740782-35f9-37ff-85c8-f6429cae1698 | -2.24757 | -49.32803 | 2024-11-13 04:04:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1baf6d08-8a2e-3fd1-9dbb-35945583cc7c | -2.23927 | -53.76136 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b294bcf0-b06e-37d0-82b5-58b58619e075 | -2.41216 | -48.6383 | 2024-11-13 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fbe035d6-f833-3987-ad53-c5b3022de130 | -3.67017 | -50.7446 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7c290ac-cbc3-3905-ae87-33749bc9a3f5 | -3.62129 | -51.49414 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 864e15e2-debd-3e47-8bf8-f85f83c82905 | -3.34599 | -48.99035 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 744a08e4-8dc7-3a51-ac1c-fbcbd59aff95 | -3.23587 | -50.66883 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a53044f9-f8d4-3089-9a43-c6a20784bb9c | -4.05362 | -48.32225 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d412c99-bf93-357e-9961-af9550e00a08 | -3.26024 | -43.7202 | 2024-11-13 04:04:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b4cbc70-8bec-3e6d-8947-417f4afa69ea | -4.05627 | -42.10303 | 2024-11-13 04:04:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 79691178-de42-338b-83c1-f1d0c1f94f06 | -5.73821 | -35.54693 | 2024-11-13 04:04:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bb73e8fd-3913-3349-8123-aa677d37aebb | -3.52205 | -49.95947 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bd95357-bb2f-3eef-8803-4a747762adf7 | -3.04956 | -50.32839 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8abd92cb-c80e-3d5a-a7a3-fc083ecce1f3 | -4.82204 | -43.69594 | 2024-11-13 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19f6014f-1865-3420-929d-33cc07d97c7f | -2.9841 | -51.3501 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47c4e771-a0b5-33df-9bee-2339ebf64c3b | -2.66271 | -46.8021 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aabba26-72e0-3470-9ea9-beb541cc36ba | -1.39618 | -52.40057 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acda501c-1a6d-3550-9fd4-9279343fda12 | -4.20122 | -42.32962 | 2024-11-13 04:04:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e96572cf-068b-30f7-bca4-853fb78294cc | -3.05995 | -50.33373 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 59c2c149-8558-3f54-8ca3-65306680973c | -3.04408 | -50.32745 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 898e9cb3-d87a-3520-ac4d-c1ad2f964dda | -2.93377 | -48.32228 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b335ddcb-bb41-37ca-82c6-48091bd0c0d6 | -4.58211 | -43.97287 | 2024-11-13 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf34cdb6-61a4-36fb-8694-a67ba6eba352 | -4.67993 | -44.57904 | 2024-11-13 04:04:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| e0374d9f-783b-36e6-af55-ae06009caf3d | -3.10181 | -54.31737 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ac8eec9-1ae5-370d-bfbe-07e1260083c8 | -2.97892 | -51.24399 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2a15cae-bb44-38cf-90bd-ea6935a0d767 | -4.65304 | -45.12841 | 2024-11-13 04:04:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b085abe2-7799-38d6-80de-40b748b8dbb6 | -2.93857 | -48.32307 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f620f949-8418-3986-a3ba-29fa680e9335 | -3.19281 | -50.28265 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README20.md)
