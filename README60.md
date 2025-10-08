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
| 4c2e624a-2ad9-3a69-8265-47e5ba0e1f9d | -1.40702 | -46.7044 | 2025-10-08 04:36:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cc8225b-3571-364c-9276-463e44abfb4a | -3.43959 | -45.59415 | 2025-10-08 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a82eb92-8503-3509-bb52-bf5f9db46d3c | -3.46122 | -44.27168 | 2025-10-08 04:36:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be85c9cc-f23e-3738-8898-f0d505432cfa | -3.11033 | -47.79764 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 48a63892-2a99-3de1-a19b-209d844ae58c | -3.12347 | -48.96457 | 2025-10-08 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c65f19ce-3d07-366d-a7a9-10fb8538c7bd | -2.7837 | -51.79609 | 2025-10-08 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94a607b4-1b31-3fdc-8b22-8fee8a813adc | -1.88821 | -48.3968 | 2025-10-08 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0defc3a2-3050-39ef-9c74-7d4e09ce05f0 | -3.08858 | -51.2512 | 2025-10-08 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff12a981-836a-37d3-b392-b4bc6312c4bd | -3.22408 | -49.36046 | 2025-10-08 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04386a18-5401-3b96-8c38-482be7e6061a | -3.19936 | -51.01455 | 2025-10-08 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f18a40ca-8338-37f7-8395-30e90ef771b5 | -4.20817 | -44.66929 | 2025-10-08 04:36:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb017bad-9a34-365d-bd4f-4d650e1e7e84 | -2.66091 | -47.86903 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69806bc3-8b32-35d8-9c1f-4336b877c4a1 | -2.88531 | -50.72801 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d2e5d9f8-ec17-311b-830e-f53eecf51a83 | -3.43069 | -43.15039 | 2025-10-08 04:36:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 186ff6a9-f1da-3080-b4c0-1bcbd8e17f32 | -3.13639 | -50.44859 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cf3b01f-d138-31d2-aeec-8eba7d33c64f | -2.51813 | -51.93239 | 2025-10-08 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f028c7a-79ef-3bb2-9363-5a170651d45e | -2.88411 | -50.7356 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd201b43-6898-348b-966d-5dc2cedadb05 | -3.14381 | -50.44599 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d57cba5-8f44-3a9f-af6b-5a22ea5aa31e | -3.13698 | -50.4449 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 919d3dc7-0e6b-3d16-a061-9fe9495e2041 | -3.11817 | -48.78379 | 2025-10-08 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f781ffe-3e0e-3579-bae2-a759fe0b1ea1 | -2.4703 | -54.05468 | 2025-10-08 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fae26d5-efe5-3c27-b24a-7d46f564a871 | -0.90082 | -47.54821 | 2025-10-08 04:36:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3680df19-c0dc-31d8-afc6-ccd5a9aef72a | -3.2153 | -47.12842 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40f6b8e3-50e5-3378-baa8-01a1f1c7071a | -2.78851 | -49.61889 | 2025-10-08 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd96a474-ee66-3347-9ac6-50f813547ca1 | -2.7891 | -49.59367 | 2025-10-08 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4073a075-fd2b-3bf0-ad74-284753db9626 | -3.45098 | -45.59171 | 2025-10-08 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fb2dd95-5698-33ef-ad93-b6cbcf55685b | -3.2368 | -46.79026 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be101972-bcbf-3040-bbdd-e408e2b98033 | -1.87178 | -55.16148 | 2025-10-08 04:36:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbe4b332-5ae9-3fc7-a945-1a28015d1430 | -3.09236 | -47.02138 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 039bf14b-637a-3bb4-859a-588e0ab4efce | -3.23964 | -46.79446 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9e4fada-1128-3811-8707-0913d5c8700b | -3.29293 | -50.1477 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f663f1f3-1218-3184-935d-dba56b594545 | -3.44317 | -45.59471 | 2025-10-08 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15e46141-11e1-38f1-87c1-dfb121821261 | -2.88877 | -50.72856 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 265d6fd5-d5d1-3129-999a-408c089cf29e | -2.86226 | -45.45013 | 2025-10-08 04:36:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe5d22b0-06e2-36d7-a9ba-2e8b967f631d | -3.09395 | -50.5828 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdc727b6-5d68-375b-bbc9-106c52c63253 | -0.90413 | -47.54873 | 2025-10-08 04:36:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| faabcf56-04dc-3ec7-9c0e-53cf156a8122 | 1.21219 | -50.68654 | 2025-10-08 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4432185-97fb-34cb-aa8a-d2bd5e0a3337 | -3.09112 | -50.57848 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa680b8f-9ec9-3d06-9900-7b13577902b0 | -3.09292 | -47.01777 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca768c93-8c14-3542-bb67-0243fa7d486a | -2.89509 | -50.73345 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00bdfcc9-a1d6-32c1-a262-9356fe7b4b95 | -3.08708 | -50.58171 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ef3b076-b0ba-31e9-a4a9-d7a498425eb7 | -3.14271 | -50.29895 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7b171b9-e347-3262-93ae-023d0aca0d2a | -3.30136 | -50.16016 | 2025-10-08 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3423078e-8d69-37f7-a193-274bdbe4d5aa | -3.1529 | -50.45499 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edf3a3b6-5fac-3a27-9d7f-dc2772a25968 | -1.41039 | -46.70493 | 2025-10-08 04:36:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b382bf1-afb3-34cc-9278-60e1662aeced | -4.20366 | -44.67339 | 2025-10-08 04:36:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32a3b850-6e2c-35d8-aac8-b17b7340fc5c | -2.83145 | -49.199 | 2025-10-08 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eabda7c9-e54c-3c20-a072-85f60a1aa7a0 | -2.88185 | -50.72747 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4693f64f-8400-35b5-8be4-2a177060d701 | -0.70228 | -47.83752 | 2025-10-08 04:36:00 | NOAA-20 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65b24f12-3627-3a4c-a5d4-9e6b208af25f | -3.08424 | -50.57742 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3eacaed0-3c45-3399-9d4b-a5b53188d840 | -3.08947 | -50.56673 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e03d693a-ada8-32af-ad47-7c6c9eec60a0 | -3.45393 | -45.59636 | 2025-10-08 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07fd687c-ea8a-3ce0-b127-2b21c50daab7 | -2.48061 | -48.36696 | 2025-10-08 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65182cfd-b3c2-3f2f-a774-b2a03ad8f5fe | -2.89163 | -50.7329 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a51faeb7-24b9-3451-8ab5-16ad2dfb68da | -4.05084 | -42.51828 | 2025-10-08 04:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1b6ebd1f-8f44-30f3-ba2b-dbf18947b8d1 | 0.92621 | -51.13531 | 2025-10-08 04:36:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d589a604-14e8-34f7-ba9a-c2c0219f73b6 | -4.0502 | -42.52248 | 2025-10-08 04:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 26941721-9c4a-3e10-baf6-c6304c305b11 | -0.90744 | -47.54924 | 2025-10-08 04:36:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14a52234-d81b-36e3-9802-6db029760b9b | -3.45456 | -45.59225 | 2025-10-08 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 246af921-ac66-3bac-9bf6-23d4f1a90a28 | -3.08828 | -50.5742 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcf57ea7-b63d-3f80-9e3c-a8971ac27696 | -2.29509 | -47.99247 | 2025-10-08 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06e0145a-8b29-3151-a02e-44038645b56f | -1.09511 | -53.68988 | 2025-10-08 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5906350-c787-3518-b9f5-c256d65acf24 | 0.92689 | -51.1396 | 2025-10-08 04:36:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13625fb4-bed3-3d84-8a5c-49c5fc986667 | -4.49471 | -42.86067 | 2025-10-08 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 362662d3-79c4-3c52-9446-68c852f53dcc | -3.22075 | -49.35994 | 2025-10-08 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b1a59d7b-ff78-32bd-850d-dd3c96176df1 | -3.07443 | -51.20427 | 2025-10-08 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 949b810a-1d7c-349e-850c-509c89b3c93e | -3.09574 | -47.0219 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac597aa7-d9e4-35a2-aa47-ce6e670670e0 | -3.45267 | -48.96754 | 2025-10-08 04:36:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f111614c-3051-38d2-a1e5-8b6f812eb8a5 | -3.08505 | -51.25064 | 2025-10-08 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d6ea281-1243-3108-b96b-e925fb53214f | -2.89223 | -50.72911 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65f8cbf0-2c56-3af4-a50f-630191315193 | 0.93152 | -51.12127 | 2025-10-08 04:36:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d96f1009-cc87-3cd9-8ad7-719abe908166 | -4.49901 | -42.86131 | 2025-10-08 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b64bd922-0d7a-304d-bff3-8dc46dfc45bd | -2.88817 | -50.73235 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7e0e3e2b-ae0f-3a26-abe3-490a2f8b7111 | -3.45034 | -45.59581 | 2025-10-08 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffa3dd8a-38a2-34a9-bffa-0768f790d4b8 | -1.41095 | -46.70134 | 2025-10-08 04:36:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6388bb64-ed61-3cf6-bc1a-96ed98be5394 | -3.12093 | -48.78775 | 2025-10-08 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7063b01b-ee2e-304e-96de-6d0d3d904dff | -2.7913 | -49.62295 | 2025-10-08 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9564dd3-b774-36d5-85e6-3e5ac27bafe5 | -3.08081 | -50.57689 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a35b3b9f-96ba-3d47-8772-590cfa9970a4 | -2.14744 | -47.50537 | 2025-10-08 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2597abfa-d427-3b17-ba49-8b1433fbfa7a | -3.1404 | -50.44545 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b60c77b-6c0d-3c92-a096-3fd68a52558c | -3.15573 | -50.45922 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e14aebaa-89f1-3a80-958e-649def9ed460 | -2.48115 | -48.36353 | 2025-10-08 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a23cd59-f8e3-3bf2-9d13-653c59f2570d | -3.07091 | -51.2037 | 2025-10-08 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e2b630c-7a51-3505-8023-6e4b1283a245 | -2.88124 | -50.73126 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fd506c0-befe-3a57-be09-7055f00e7ded | -5.20251 | -37.62822 | 2025-10-08 04:36:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f3a54135-3b49-366a-b711-145d45d9192c | -3.08364 | -50.58117 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80026754-71f9-3c94-b32e-8919ffc6d000 | -3.19874 | -51.01842 | 2025-10-08 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31d0bdda-d03f-3950-9453-2e1425fc610d | -3.11156 | -48.78276 | 2025-10-08 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3869579-1a0f-35ce-9cf5-6c309272a694 | -3.08604 | -50.56619 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7086a244-607c-39bb-bfb4-56a7439fb1ba | -3.08544 | -50.56992 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecc5addf-c1cb-3285-9763-ffd26751415e | -3.25745 | -49.12748 | 2025-10-08 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cf1e579-665f-35ae-b6b0-1c8a227bfa7b | -3.09515 | -50.57529 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4359d38a-b0a6-38b4-8260-5b1d1fd493e4 | -2.78005 | -51.79554 | 2025-10-08 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 343d7338-a711-39ca-a19b-ca54521351e2 | -3.38401 | -50.28013 | 2025-10-08 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a37de081-1fb4-38f0-9e16-ef013816368c | 0.92853 | -51.12614 | 2025-10-08 04:36:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e4576d6b-aa50-3265-a0b8-3c8e85ba280d | -3.11486 | -48.78328 | 2025-10-08 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8af3040a-b93c-3d77-876c-4a8c47f49faf | -3.09171 | -50.57475 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98f981f2-1e18-303f-b4dc-24716f7afef9 | -3.44676 | -45.59526 | 2025-10-08 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09d3a13e-ab95-3290-85ac-c346edc944a3 | -2.14411 | -47.50486 | 2025-10-08 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ce9efb8-525a-3edf-974a-08557403333a | -3.10418 | -47.01215 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |


[Clique aqui para ver as próximas entradas](README61.md)
