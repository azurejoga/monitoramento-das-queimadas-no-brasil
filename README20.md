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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d511652f-5404-390f-8454-da1306cd0ffc | -3.18155 | -54.08416 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70f4b9b1-6f5e-37b2-b191-b7e9b8b351eb | -3.17462 | -54.07563 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7400f473-3733-36a2-bd31-f58990cd85da | -3.11212 | -50.17905 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbe8a477-8e91-33f2-bd49-8067f53c69c6 | -3.92625 | -45.77258 | 2026-10-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5087cf5b-997e-357a-b3b6-b494deac2298 | -2.88907 | -54.13724 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 996a0bd0-2310-31d1-be02-fedc41447b04 | -2.93685 | -54.09998 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dca0355-344f-3535-bda8-642bb84eaea1 | -1.45402 | -54.64309 | 2026-10-03 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fbaf2be-32cc-3bb4-ad71-66af4411e94e | -1.22516 | -54.53856 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e62d273a-d3cc-3fcb-a6ca-ad43d3745d4c | -3.17113 | -54.09696 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eff979ae-6370-32dd-887e-c531996f8f35 | -3.27985 | -53.83245 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 988e01d0-1bea-3205-a56d-dc50e9c2c102 | -2.22945 | -51.92069 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6f0202d-bf5c-3544-b095-29eeaf9fd75b | -1.59117 | -47.25854 | 2026-10-03 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8c57b14-f40c-3020-89ea-902bf082fa85 | -4.20422 | -47.88816 | 2026-10-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18695000-e0c8-3cbb-8a39-f7279bdafb4f | -3.51193 | -52.72002 | 2026-10-03 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 230becd7-dfcc-36b3-8261-8197598c982d | -3.28275 | -53.83989 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84b0e2e4-af43-34ba-84e9-473cc851b1d1 | -0.91124 | -47.9094 | 2026-10-03 04:38:00 | NOAA-21 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc51c024-3eb6-3b4e-af99-86b66086d5c7 | -2.17291 | -49.76517 | 2026-10-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6e0cd0d-8d8b-3615-937f-f89be806555b | -3.43483 | -50.43727 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98c3195a-3314-3e36-9cc7-5f37adcb332a | -3.10655 | -50.29467 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c59b0b82-a330-3b12-9d9c-fc6a11995f60 | -1.26803 | -54.56168 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| afb276d4-0bb6-3444-90d9-f7f85bcf9315 | -1.33209 | -47.58863 | 2026-10-03 04:38:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d5c9f02c-a98c-31f6-9da9-917b33a9971a | -3.13508 | -53.75294 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a05d394a-f3c2-3fc6-b721-abe12bc8839d | -3.17808 | -54.07994 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e57c0d4-b845-3afc-9cdf-80fa1de9d9e5 | -4.73914 | -43.26715 | 2026-10-03 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| afe2e481-3499-37db-bb65-504c99c6ae2d | -3.18212 | -54.08065 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb9b7680-fffc-35ab-908a-5caf87ffeb6a | -3.71604 | -50.65814 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6974f3d9-d2dc-3afd-a63c-6653cc815d42 | -2.29319 | -48.75816 | 2026-10-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 074cb958-1f5c-359e-a186-b947ec614e0b | -3.21615 | -53.94789 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b57c95a0-4a67-3fed-b576-5835d51d3438 | -4.22735 | -46.44194 | 2026-10-03 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09089fc9-f6a8-39e0-b21e-11a6c4a7939c | 1.78152 | -55.60384 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49f2ac7b-a442-3bd9-82d0-7fc15d837518 | -1.96551 | -48.36995 | 2026-10-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2442485e-a49e-33f5-9eac-99071d6aebb2 | -3.17403 | -54.0792 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa2f994b-4160-3e90-aafa-2eae0ede3c54 | -3.23168 | -54.31339 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc462732-dd02-3125-b8e1-818030ca2fed | -1.68904 | -48.20006 | 2026-10-03 04:38:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38296d91-2c3e-3145-8680-0a9dbcc4a020 | 1.9149 | -55.80738 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9adde65d-4168-386b-ac81-46beb14dc04d | -2.96968 | -54.10239 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25ceee96-bf10-39ef-9278-59a466a986eb | -3.10608 | -50.28368 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78bfff3b-6e98-39a9-8b6a-0ad79dc3ef49 | -2.8879 | -54.11831 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 577e19f9-226c-3f40-adc0-716199d54cbf | -4.73544 | -43.26236 | 2026-10-03 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 372e2101-bd48-3a7f-9bf7-a57c8b3582f4 | -1.08834 | -54.11367 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eac2c8ba-b37d-387a-9bc8-d1133ed37642 | -3.27223 | -50.08851 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53972599-6190-3ad2-9108-4de5e2d9160d | -3.13564 | -53.74952 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22723b61-4925-36b7-8278-f1039a65bf70 | -4.45414 | -47.92333 | 2026-10-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 457320fa-94d0-3f3b-801b-4a2f7fe1884f | -2.58222 | -49.99835 | 2026-10-03 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fdfce65-72c2-3f93-ae9f-a76c7ac44f0f | -1.65668 | -55.21282 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc68d5b4-48f9-33e8-b862-81a28b653df1 | -2.78192 | -48.65556 | 2026-10-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53e51ed0-00c0-329a-a361-eb4738e68b0a | -3.17982 | -54.09474 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9aebfa58-2b84-3bfd-890e-91c4d83aedf7 | -1.99687 | -49.65126 | 2026-10-03 04:38:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 703edc78-26ab-3dd0-ac64-fdc36cb62ddd | -0.40674 | -51.99464 | 2026-10-03 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32541390-dbc5-37e2-9d52-15e93f04faf7 | -3.1373 | -53.73926 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 69cbcd47-615e-32f2-9ffe-3dad16a5d7de | -3.1203 | -53.74359 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 680e898b-375e-3a35-90bc-df81657b8195 | -3.09757 | -51.09974 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0d1ba6e-cbcc-39f5-a327-14fd4ef809f5 | -2.57114 | -54.74153 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 082bbd50-b33b-33c9-9f92-ca6cbf364fe5 | -2.15532 | -53.66306 | 2026-10-03 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f82fc99b-2395-3b25-947e-fb329487df44 | -3.22056 | -54.31102 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe857b20-70a5-3b0c-825e-b5b0c6ab038b | -3.50459 | -53.20081 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3736e5e3-d830-37b6-8a15-25adc7f93c68 | -3.70347 | -50.97831 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68b435cb-0bb4-3c9b-8e65-218e1c69ad66 | -2.89082 | -54.12627 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1736161-131b-3908-b10a-ea61043d6021 | -3.18387 | -54.09547 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fa886483-0f87-3e2f-8c1c-717d556c4bfb | -2.96858 | -53.26693 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3d5745f-2cc6-3507-baed-96506ebb4fd0 | -3.22756 | -54.31276 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5325f3ba-6080-3899-89ac-258c8e865656 | -2.97163 | -53.27248 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4800d6fa-7725-3768-82dd-871d6bdc47cf | -4.06025 | -51.12049 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9dd22ec-dcac-3c45-ad69-635216358908 | 1.78639 | -55.6031 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66af0824-561e-314e-b0ca-3dab1c94d6f7 | -3.29737 | -50.32101 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fe57fbe-a028-30ab-ac82-1b1b834ccae0 | -3.32087 | -51.67537 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ead30744-23cf-38c1-b191-969488209104 | -2.86892 | -50.31982 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b568c811-aa41-3dc6-9e06-096c6e7b41bb | -3.18674 | -54.10341 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9b8c4d0-b130-358e-8c6d-3e83f47cafc2 | 1.90499 | -55.80879 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95c616cb-7fdb-3b4b-a7db-266ab504958d | -4.568 | -46.58697 | 2026-10-03 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| be609f62-8474-3841-ab0a-dbb638e8862e | -2.36328 | -50.34838 | 2026-10-03 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d0ee708-69ef-3e46-ae0a-4fbba248048b | -3.22817 | -50.02351 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cee487f-e393-3d82-b58a-bc46dba4ab8f | -3.21267 | -53.94387 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60e2ee6f-9648-3c0b-8cc8-15bfd036569e | 1.91152 | -55.78494 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7a38f2f-018e-3d51-87a1-d096ba64d126 | -3.12142 | -53.73674 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 96b97c3a-5e1e-34a7-8731-cf59f81dc504 | -4.45024 | -47.92636 | 2026-10-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 08195177-d3a0-3582-af61-03afbb6dbd51 | 1.90742 | -55.79126 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1e7ced0-8574-372a-9821-897fd5c68a75 | -3.70005 | -50.97775 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5523eaa7-f703-37d3-9ef0-d8ce8c14b459 | -3.35541 | -43.37996 | 2026-10-03 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b6c9c78-1ef5-3b3b-82d7-232fba4f5622 | -1.22149 | -54.53374 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b006bb36-3646-3b3a-bcb7-a4acb556a894 | -3.0124 | -53.88986 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9fbcdfc8-296a-3d6a-91a6-d71b66164602 | -3.17171 | -54.09339 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71981247-f814-30c0-9985-1da5d04b8ab3 | -2.10963 | -49.23588 | 2026-10-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 698c49b0-b788-3192-977d-389586162b12 | -3.16592 | -54.07788 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ffa5706-612d-33da-bdc2-b7276c83869b | -2.8955 | -54.14952 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d5576d2-ed1b-3aec-a9c5-5e93c4b08f56 | -1.08431 | -54.1058 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c7b6667-8794-3fed-a32c-36f9aab09ba3 | -3.00382 | -50.47357 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f57a6b05-2e90-3090-b539-9276974057a1 | -3.26638 | -49.51979 | 2026-10-03 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dfd8df2-6010-35c1-b865-0b26f3c11de1 | -2.92811 | -54.10233 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d6eaae5f-61bd-36f6-8313-3c3332fa0d3b | -3.11161 | -50.28451 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43413215-90c6-3d76-a956-bfa884521bde | -2.57157 | -49.11084 | 2026-10-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85643e80-3ebf-3d7a-a502-c65df6ebef08 | -3.55512 | -53.26968 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b57f20c-b552-307f-b489-d91af11a5814 | -3.11946 | -50.27842 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04d2ef16-207f-3bc8-9bc4-19bdbe65060d | -2.89608 | -54.14585 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b7b48b9-a73d-3f10-a988-f280c01b9f1b | -2.88556 | -54.13294 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 410a4e09-26ec-3eec-8cec-52f14ca8c001 | -3.07713 | -51.27176 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5832b20b-34cc-3731-b168-cff3fc423941 | -0.34973 | -51.99466 | 2026-10-03 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f7ce9ea-b2d3-3d92-9f6d-8a380de88b75 | -3.28385 | -53.83301 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b9342db-ac8d-3ad9-a288-9f2831eda0b5 | -3.1578 | -54.07666 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6590be43-423b-336b-8433-184a8e59b27c | -3.24885 | -54.52067 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README21.md)
