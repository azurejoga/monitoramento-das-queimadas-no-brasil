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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76c69c1a-f291-3bfd-8e18-bed9fb628aa0 | -3.0851 | -54.26913 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44150947-277c-36cd-ba53-3580a59444c2 | -4.58357 | -54.9486 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a49e886-b44c-3573-9493-c55ddff88283 | -3.1903 | -50.58341 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4eda007d-091e-35e3-a20b-3a2bc76f9c83 | -3.50392 | -49.94065 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 795bf3a7-fadc-3136-923d-75a9c4f4d61b | -4.66466 | -49.2311 | 2026-10-09 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8122f9c3-2967-324b-b286-fcc348482615 | -3.02092 | -54.04397 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcb884b9-6bcd-3752-a73f-e68a7ea29b07 | -2.39999 | -51.30681 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b3e45f3-64ea-3e63-9712-3a22a101d80a | -2.83577 | -54.13484 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b28fa06c-4e8a-3b5b-81c0-a23a21333fab | -5.34724 | -45.73292 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fced438a-956c-3f1e-8543-24c39dfd9cbf | -3.57052 | -54.68437 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 732be8b4-8b9a-34fc-bfdf-38ad34e59ec1 | -3.4361 | -56.93802 | 2026-10-09 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f420d881-9a36-3eeb-a51e-f579a4e131da | -4.80175 | -56.14667 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 48e73ab7-b104-32e1-bc63-a680346436a3 | -6.96229 | -43.85181 | 2026-10-09 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fd5ea86-a98e-32db-b4cb-6683582d0ae4 | -3.29497 | -51.56966 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59d759cf-a4d4-3696-9641-5f638186846a | -7.40632 | -35.1936 | 2026-10-09 04:25:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 9b4245cf-d8a5-3a9f-9524-ffeb7ae1c28f | -3.72675 | -54.2224 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 769a8f89-4d9e-3b90-b5d2-2650aac001f6 | -2.47548 | -56.09401 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e16e340-2390-3558-b69d-2679deeed611 | -2.74554 | -54.12232 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea658fd1-16bc-38f8-943d-da36e19b881a | -3.32699 | -50.17919 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24a8070c-53fa-310f-ab26-11cdbe15233e | -5.98185 | -41.37558 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7f6d979c-191e-3c73-8dd2-3b2496e5c431 | -3.85695 | -51.11002 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03e1d2e1-c316-3298-96b3-11faefc9d8ac | -2.91794 | -54.13369 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfea33d9-2636-3f48-8cf1-a85b422af4e3 | -3.19965 | -50.55077 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 653bbc09-eb38-3808-a3d7-212b7d99d82b | -5.33506 | -50.98633 | 2026-10-09 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7899e785-e0ff-350b-a9a4-a4228f64ba33 | -2.50418 | -56.06356 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 02c3739d-3f13-3c5c-81c3-09a7c40d4c3f | -3.5768 | -54.67899 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d26a9533-a7a8-3f15-977e-894aed7ac7a5 | -5.30705 | -45.72612 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91525e84-4aaf-3a53-9684-d32f6e847f5d | -3.19882 | -50.55586 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3f40d24-2c16-38bd-9657-588b6d2fa188 | -3.26881 | -50.39631 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 491aeff7-b0bd-3545-acd3-f9c5d8657379 | -2.49697 | -56.07092 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 583a6fb1-f3e7-3075-9ada-7f0f5b8d7dcd | -3.10523 | -53.93521 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 42aaf24a-dafb-30be-bf47-3c8bd0819243 | -3.00325 | -54.11352 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60367583-f06f-3d10-8be8-265a099d93a6 | -3.25577 | -54.02131 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 825819d8-9299-312e-8f92-1fdd7e214755 | -3.11903 | -54.1611 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdf0b48c-4f1c-375d-854e-b58a89bf4e84 | -3.08434 | -58.09409 | 2026-10-09 04:25:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a63ed47d-9cc1-3f1b-a078-a3cadf11a16a | -2.77462 | -54.07173 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 978ce47d-22eb-3d30-9b01-62bb6234ec90 | -6.91203 | -45.46453 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21e7b173-c205-35cb-abd2-365a5438c83c | -3.31736 | -39.82014 | 2026-10-09 04:25:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e727a9e-6014-366a-8b6c-adf0a03a33f9 | -4.664 | -49.23525 | 2026-10-09 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ae61913-2583-3502-8e16-6d88f6e82c6d | -6.88782 | -45.90958 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ace941d9-af39-3380-8034-1bd2e4b9aa17 | -4.4083 | -50.79498 | 2026-10-09 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ddfffad-f666-385a-a868-115aabbff2b7 | -2.88493 | -54.18597 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 28d56a58-6387-3a17-8784-fa5900fdf985 | -3.78319 | -58.5834 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5e42b007-2fb4-319f-bc65-5f82003032d6 | -3.53511 | -59.57536 | 2026-10-09 04:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 053378f3-ce9c-34a3-90bf-747c6d1608d8 | -3.38621 | -50.21648 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3fb4487-088a-368d-ac13-ed775c39fb4c | -4.58309 | -54.95148 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a13ffb0-b464-3a9c-b437-5cc985c60e4a | -3.28968 | -54.00296 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6871b53-6eb3-3240-875f-fc719163dcd4 | -2.18996 | -48.2494 | 2026-10-09 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 304785ff-3c2a-3fb2-bb1e-4b0529483660 | -7.06662 | -40.95428 | 2026-10-09 04:25:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dfce3f2d-7d23-31b5-89fd-be317379fbd2 | -2.36457 | -48.88396 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8565da44-4579-3900-8afa-ad6435216a94 | -3.44699 | -59.5538 | 2026-10-09 04:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 32918a4e-64cc-33c4-a937-777202182b45 | -3.09594 | -53.96056 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b797ff2c-4309-36b7-92d9-459ee4fd7e09 | -5.53337 | -47.19468 | 2026-10-09 04:25:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 734206ce-fe97-3fd7-a517-e574f2e5aafd | -2.78524 | -54.07042 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c72bd9d-b975-35f1-8beb-f4cd01b2ffc8 | -2.92781 | -54.20002 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5017bc12-f0c6-37eb-a699-655ce6cc5797 | -7.20757 | -44.27173 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88886e7c-518d-3f7a-ac69-ce6cf8df1f19 | -3.09738 | -53.95178 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58e1cc65-508d-3bc0-a138-e7cd2d6180d5 | 0.98587 | -49.95472 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37964db0-edbe-35df-b6b5-00f2962386b8 | -1.82652 | -54.99343 | 2026-10-09 04:25:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7128179-1cd8-34f6-b76f-483a8dc19560 | -4.994 | -45.59562 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e236652-65a1-3c42-ae58-e88e638c90ac | -3.47176 | -44.2923 | 2026-10-09 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59eca14a-5215-3d93-a979-40b7498dee77 | -5.71343 | -53.49495 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb1c10a5-0821-3c7c-a325-8cd613906c3c | -2.82968 | -54.14009 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25d8542a-77b7-389c-b786-0e49618f4f7b | -6.00766 | -40.97615 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 1c711ba4-e883-3e3a-883c-b9791718e040 | -5.70744 | -41.75982 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 07f220a6-de27-39bb-a54d-a81ade23321d | -3.93913 | -55.71915 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 509de986-3cc6-382b-86b1-8309d77a0a9e | -5.48665 | -45.2267 | 2026-10-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 650cc112-c785-3cff-9dac-ddba0be82ad6 | -4.11335 | -54.62569 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8d33626-cd59-34c7-85a2-a2157ce75a08 | -4.5522 | -54.9754 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0211820e-8aa1-39bd-a8a7-02296692c78c | -3.2603 | -54.02494 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9057705-29cd-3dc6-9ec8-82a5ac2e1760 | -5.09175 | -46.21418 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8380fb4-05b9-31a3-bb3c-3b3b340b9236 | -2.84741 | -54.12752 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a00aafd-bca3-3b66-a98a-6fe5dc051cb4 | -2.49766 | -56.06682 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 476d1bc9-b357-368c-8b56-079a85013504 | -2.98901 | -54.08113 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6496dd58-e043-34e4-9c1b-be937167929a | -6.88677 | -43.70212 | 2026-10-09 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ab82a81-a08f-39d0-be4d-1e59a207e9e7 | -5.24168 | -48.39782 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b0f72b6-2b3b-3459-b04e-7f44aa85c308 | -2.99551 | -54.07306 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eac07d8f-a59b-383c-bbb5-5f3c7b9389f3 | -3.30284 | -53.69608 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae95fdbe-de82-3505-97f3-57a6875bc35f | -6.0093 | -40.96498 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| ae03cff5-f92b-3795-87e6-4a4636f4620d | -3.30058 | -49.13198 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e569ac55-67c8-3b18-86fe-67d53906614b | -5.7098 | -53.46078 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a5ce898-c6e5-314b-9fa6-364701b2b0c1 | -2.88754 | -54.0729 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa4a064e-b981-3e9b-8f58-732f56397c68 | 1.35727 | -50.83329 | 2026-10-09 04:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f404eee5-f0fe-3625-8afc-f1d46aa9eec6 | -3.26079 | -54.02204 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c72863b4-bcff-3b36-8fdc-24634cde39ac | -3.31403 | -54.04246 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3fd0f82-45b4-3e64-a191-af145696f36a | -4.11283 | -54.62886 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a207df8a-cb6a-3285-9148-041c8ca988fd | -3.5484 | -54.68466 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfe1c756-6b91-3fec-8fe6-e10fb0527e62 | -3.02078 | -54.07704 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1c22e320-5ae9-3f4a-a2ac-5a422aa111ac | -2.98322 | -54.11676 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e57d01fd-6b57-36c4-b9a7-35ede48a38c3 | -5.61742 | -44.37772 | 2026-10-09 04:25:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30e83cb0-4724-31e8-9f18-d4f4d54a43dd | -3.27004 | -54.05921 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 792939d6-376f-3f52-b22f-407c169e44fa | -3.08204 | -54.28716 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2006f4f8-c2cd-3411-8633-069f9799e7aa | -3.08196 | -54.30178 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d60a82f-b602-32bb-9e24-6d6a31d806d4 | -3.00775 | -54.08691 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df05022b-8e3d-38a0-b73c-ae65e1dbce6a | -3.10072 | -53.93145 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f9b1d6c5-1385-3205-a052-d7be32435c96 | -7.18906 | -44.27676 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87ad31c8-445e-3a68-9237-f07c84a0c8bc | 0.50157 | -50.78649 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5273afc8-516c-3e0a-90c9-72ae8dadd287 | -4.05932 | -49.10612 | 2026-10-09 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cf598e6-b0c9-3c5f-9ecf-d8a519d9f10c | -5.94626 | -45.37666 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c92a850-5039-33fe-ab0f-5f7a276498fd | -3.2867 | -51.54007 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README93.md)
