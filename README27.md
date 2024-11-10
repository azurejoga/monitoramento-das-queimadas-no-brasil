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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00350fd2-b585-360f-9f3f-730409750b37 | -4.57459 | -45.69025 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee03331f-132d-39da-a1db-9361eac80bdd | -2.61471 | -46.16311 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d288340e-c48a-3bc0-b2bf-cd1d28b14b7e | -2.59306 | -48.28962 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05f4ca4c-eafb-3483-843f-b448e450c84f | -1.52373 | -52.20345 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3d9c2780-a52c-3d14-a07f-1482609f6dce | -2.87998 | -51.47551 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 4a1632fb-de01-3950-bca8-86729cc9c641 | -4.95589 | -42.98438 | 2024-11-10 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcf074aa-400a-37a3-937f-be4d48100097 | -3.10972 | -50.20636 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c626c21f-5806-3808-a046-d81cff0c50d0 | -5.24323 | -46.24423 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d53b7137-7d35-3960-a940-ff008e9537b5 | -5.52397 | -45.40148 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5bbfdd31-b4b1-380a-8d69-910a3ba534b0 | -3.89413 | -49.98115 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c94398ee-16a2-3b4f-a243-e9a3b7f3e4ea | -5.16494 | -50.67829 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09d6a10d-c216-3bcc-a4d4-1719d994856e | -1.52308 | -52.20731 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ef84d26-1775-3991-a379-0b2d5fe04bd4 | -2.68326 | -46.79883 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3e999a6-a677-3b64-875f-73d4f5351ee3 | -3.68709 | -45.81792 | 2024-11-10 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5349c381-1d5c-3ef0-bec7-414c2bcadb45 | -3.84126 | -44.1246 | 2024-11-10 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93354145-b527-3fa6-8df2-5092a9e5f98c | -2.88358 | -49.22917 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95c6bd76-8ebc-3776-b308-8043c6c564ff | -2.20772 | -48.36388 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6496a390-b643-3de7-9490-549797917e1d | -4.12635 | -43.59051 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46a4b77e-e76c-311e-b104-448cae569fa5 | -5.30516 | -46.22833 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1882a68-5527-33bc-a3cc-ef6aa7f2e2da | -2.56985 | -45.55251 | 2024-11-10 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2432eafd-93d2-33a1-a68b-0e124f50fbbe | -2.39838 | -48.49833 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09648a31-a52e-3655-ad3d-5cae1515f4e7 | -4.0635 | -48.31696 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcf0b955-8f5f-32bf-9a3b-0cd260799175 | -2.24888 | -53.66979 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0b04af8e-4957-39b5-b0fd-ab931f2dc3e5 | -4.57587 | -45.40758 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bd4763e-f4da-3da3-89b8-c1787ecd0464 | -4.85477 | -46.98188 | 2024-11-10 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 9a95ca64-afa4-3599-ab6e-f64fa0a142a9 | -6.70195 | -40.45575 | 2024-11-10 04:14:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fcc8b4dc-71da-3316-ac90-6ced440505e6 | -5.54767 | -47.5033 | 2024-11-10 04:14:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 263aa3ef-22a7-3526-948a-fad2ab70eb55 | -3.08788 | -51.12646 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2426759f-2c57-3105-811d-9e699702acf0 | -3.11172 | -45.96733 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d09aac13-c347-36a4-ae43-bd08ce98b4d1 | -3.55416 | -49.9855 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66dd64f1-bd65-3ebd-9103-4e2e60d7891b | -5.05647 | -44.27429 | 2024-11-10 04:14:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c49000c-7f8a-3231-9ef2-4465fd02f4e2 | -3.57953 | -50.27978 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d67c87a2-343b-3f9d-8ff7-6f1fc904e5fb | 1.11629 | -50.8863 | 2024-11-10 04:14:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6150b39e-81a9-3483-a990-8f8520c4b578 | -4.64039 | -46.02616 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f978d68-63b4-35d6-9d4c-4b023552cefe | -2.08719 | -48.82953 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e964b7b7-31ab-32ee-9f1d-edf993563a84 | -3.24853 | -46.49218 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 905bfa98-afce-39b8-a570-e38f4206b543 | -3.43376 | -50.29805 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| c024028b-f2b2-3849-90ee-3e85cafac746 | -3.35775 | -50.13169 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1ccb62b4-9c75-3c88-a14b-e8c9746c1295 | -3.28205 | -53.67353 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f545795-c0ee-3bb6-b424-41a40155901a | -1.53304 | -52.20122 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 242e69f6-cbdf-35d7-a498-5f3e45f13bb2 | -3.11714 | -51.10875 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1eea306-6308-35c0-b960-c073086e65f0 | -5.88177 | -44.34615 | 2024-11-10 04:14:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8fbd1b7-9946-35cc-8824-90664fe2e717 | -3.19404 | -48.65615 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bc6da81-58fa-3202-b019-eaace656c2ba | -3.25305 | -48.74145 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b3bc1e6-748a-3bb3-9caa-bea9e3c2bbd1 | -4.09776 | -49.13095 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d36d19b5-61e4-3078-8374-634d28badd4d | -3.23956 | -50.31626 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 00f5acb7-b53a-3eb5-8526-49b10860a61e | -4.24216 | -43.82736 | 2024-11-10 04:14:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f293e19-05d2-3e3a-ae05-ae3e7b4a403a | -2.89118 | -48.29423 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4fd17b0-3163-36d4-9571-b3947e296fdf | -6.51583 | -41.43822 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa33fe6c-4d66-3d41-8a8c-0117dd902771 | -5.60991 | -45.92946 | 2024-11-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10d13695-c95a-3e60-9477-cbbc08762e5f | -5.13465 | -48.25216 | 2024-11-10 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9124a364-9fb3-33f4-b83c-d6141353d2f1 | -1.40036 | -52.3603 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3878cacb-9bb2-34a1-ab15-2b2a96545b47 | -2.42833 | -46.30397 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 79385dc1-c20e-392d-8239-c062f0f85657 | -3.7912 | -47.46876 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a333fa8-762f-355a-8e73-67674f6eed76 | -5.41044 | -46.41621 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbed7486-e11b-3d01-9c5a-1d49d7e85679 | -3.79202 | -47.46364 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b45221af-eb30-3114-9a0a-93fd2821263f | -4.09044 | -49.11921 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 27b0079f-f661-35e0-af60-91a14d78a16b | -5.23967 | -46.66254 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7497cbb1-eeaa-3292-8087-2b0c2e7e664f | -2.3969 | -46.77592 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d00b4d7f-6a8a-3095-a902-effddac18f68 | -2.09486 | -50.21867 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47f09f18-80a6-3037-b603-e5b98aa95d73 | -2.57028 | -47.35278 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6141c697-ada1-350d-b487-03bdcd912eb9 | -3.54217 | -43.563 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60d0ea2f-282b-3176-883d-a8d9c7583b17 | -3.82019 | -49.86037 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca694d52-2d68-3ccb-887b-b8bf2528a1a1 | -3.96063 | -46.69966 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53c6a5dd-36a0-333a-a42a-c8124ae2d104 | -2.68007 | -51.81841 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 11a1a677-9706-30bc-b556-e69c3b6dce45 | -2.18361 | -46.57477 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| e60881d4-0290-382d-897d-f39021824fd3 | -4.09987 | -48.97759 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 72f3fe9e-42da-37a8-9ed0-1780491c7d12 | -3.96313 | -48.18777 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d43a79a5-c365-3f17-8bee-52b1614655b5 | -5.97216 | -45.36573 | 2024-11-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| d2715924-8df4-387a-9d41-14f10fe9b768 | -2.59901 | -48.19668 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cd84bf8e-589e-3ad9-a853-447c8c112bdf | -3.24499 | -50.27544 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a97284c4-2bed-31f8-9afa-eeb2a00beaf4 | -2.65301 | -51.88236 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b0000422-8f7e-3cde-94cd-bde1f141b64a | -2.1953 | -49.53228 | 2024-11-10 04:14:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3b48002-7f1a-3932-b536-db79201d4beb | -1.40043 | -52.36948 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e31686a1-25c7-3860-a61d-bc96e7cd881f | -4.10733 | -49.12645 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4032076e-617e-3a78-a229-4f86859e1bc6 | -2.69462 | -51.69342 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4dfab14-b875-3cbe-9ac4-b8bd42326731 | -3.94857 | -48.14702 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 299a5509-277e-306d-becd-14400f95b6ff | -2.50661 | -46.27695 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e29dbc5-1465-3b19-bede-357462cf8629 | -2.93147 | -48.31195 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b34060ee-1dcd-34ff-995b-92599523f0ea | -2.80978 | -52.54213 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a62a586f-5277-3b64-8d7d-72a48e7cc516 | -4.51642 | -43.98623 | 2024-11-10 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d134b5e4-368e-3d69-b93a-612f45cf975c | -1.71723 | -52.46663 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15734046-4f95-319c-81b7-b2049f03391b | -1.87697 | -48.45501 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d5bc04bb-a6ef-3fc4-ad9e-d4cd2bf8edbe | -3.20467 | -50.63449 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 19593ff9-666a-34c1-a0b9-6f4105c35391 | -3.34605 | -50.3573 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 182aefbd-54b1-3d45-8ab1-47722c4c0f32 | -2.42566 | -51.95759 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 56f5fddd-2795-3f7f-afc9-afd6b4be72f6 | -2.37315 | -48.57153 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd4fad10-db5e-3e9e-a3e0-b1988534730a | -2.15925 | -46.67878 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a66ed4e9-41f7-3368-8f9f-c49cafa280ca | -2.46239 | -46.33279 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a605d6a6-7e9a-3572-ad68-54b01f8f46fc | -2.63579 | -46.7634 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4d800aeb-7cc7-33ec-a5cc-a844b4f4ce5c | -3.52591 | -50.53292 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff95fe9e-cca3-3d14-bcab-7ddd641414b4 | -3.15942 | -51.12336 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc241930-3be4-32f6-b10a-af8e6c73a00f | -3.29761 | -42.29776 | 2024-11-10 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23db554d-83c4-342f-ad6e-a9bddeceb976 | -2.61771 | -51.30042 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 717d471f-06a2-3f43-8dd9-0600253fca0d | -2.29669 | -46.74713 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ef14427-be27-33b0-bfb0-f32ce67fd3df | -2.92007 | -49.4935 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7dad36bc-6150-358f-b89b-eb0644406990 | -3.28673 | -53.26167 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4c05c8b5-8587-387d-9b01-7017e8eb18fd | -3.22268 | -50.67958 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e3828119-e321-359a-9e41-1fa730ad3874 | -2.10593 | -46.47764 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33584251-9119-3db1-b08c-32fd1b0e72e7 | -2.36477 | -48.84808 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README28.md)
