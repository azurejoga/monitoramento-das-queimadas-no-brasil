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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc24efc5-cec5-30af-b5e3-5b2a16e4d6df | -6.40857 | -51.70736 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a544a27-f86e-3b34-9778-e50bd246ad75 | -7.29478 | -45.36203 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 92c5bd0b-07aa-34a7-af4c-fb499d0c0ce8 | -5.0121 | -56.13342 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e232c4d-9b62-3e83-a86d-20f40a9b391b | -5.69134 | -53.74006 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e1443bb-3d66-309f-a415-b56b2cb5207d | -3.13041 | -61.18456 | 2026-08-25 05:10:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cb09dc0-378c-3baf-9f39-69cdb95f9585 | -6.18149 | -53.48498 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26d7e083-010d-34d9-8c21-b1d20b003fd3 | -5.78686 | -57.60412 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1be4e092-0ee5-3484-8a31-18a01096e069 | -3.55131 | -54.49706 | 2026-08-25 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e697075e-2741-396f-a814-907dbcbc9ac9 | -6.21509 | -55.48807 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d5db4a2-3dcd-38dd-954d-081523bcd8a7 | -6.33001 | -54.75032 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0de42a7-b082-3e3b-8af5-15ae8ecfae0d | -6.3512 | -54.75357 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5349f714-f15f-3545-b525-abae39080ad0 | -6.33588 | -54.75937 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1eec45c-ac94-3187-8122-2fb96fb231e4 | -6.33294 | -54.75484 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa65c4fa-0756-310d-adf4-d8a0bddea61f | -7.26325 | -45.85798 | 2026-08-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 26ff8f88-f25d-305d-a895-9ec0e14103d9 | -4.9307 | -55.77599 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdce2ef2-67a2-37f6-972f-8f1d70b45857 | -6.34767 | -54.75302 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2423b8dc-027a-3ac4-8343-d60ec97ce966 | -3.59354 | -54.8391 | 2026-08-25 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d49d1850-8d09-3b5c-b277-c587b213ba36 | -7.2872 | -45.36536 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1c1def6b-e899-3fb5-a991-d8a20ba4aed7 | -5.91736 | -43.64065 | 2026-08-25 05:10:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ab532b9d-e0ac-39b6-bd4e-438ac20c50e5 | -6.33354 | -54.75086 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 750105ac-77b5-3125-b6dd-68ff516f92ee | -6.17528 | -53.47471 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 960d1053-4de1-3db6-96e5-ee5eb1952cd8 | -7.29404 | -45.36759 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| db803740-1bcb-3fdd-8b99-d164a021e3d0 | -5.78619 | -57.56511 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3416aeb3-846f-322d-bdf7-fcd5fe25c06a | -7.27442 | -45.36494 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 80c1230b-1c38-39c7-84d4-9224e2b132a9 | -6.18128 | -55.4333 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4f2512d4-527b-34c3-a86a-3199a73ca7eb | -3.09553 | -61.19662 | 2026-08-25 05:10:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c5575ed-75a7-3835-9edb-33b8326c475c | -3.53879 | -48.18423 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| ba8e707e-ac9c-3717-87ee-13f37c91fd48 | -5.79294 | -57.60857 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 218270cd-f62a-3a85-ab3e-d87478462a2f | -6.18593 | -53.48095 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4c16c4ea-8b03-3844-9d54-a3fee4d39110 | -6.32881 | -54.75829 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a7485f2-6045-3932-a5b6-efa175c6b676 | -5.76168 | -48.67601 | 2026-08-25 05:10:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c325ac3a-02d2-3ccc-867f-bbfd98a50a00 | -6.22991 | -55.48286 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 259551e4-1fef-3e5e-8e49-5695e50e80b0 | -6.33528 | -54.76336 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c292af0-eb3e-3cd2-bad0-86d1a53641d7 | -6.17084 | -53.47872 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b905054f-efe3-3723-ad93-65d565669c4c | -5.95738 | -53.58673 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21a0a2f4-b5f1-366f-ab00-f7128c116410 | -6.17151 | -53.47415 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d0ddd9b-cd62-3ad3-844a-345b12a708fa | -2.89362 | -48.80323 | 2026-08-25 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e71475d1-2716-3dd4-9fb5-2c63f72192ff | -5.87414 | -57.56824 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4d71e6e-36bd-3d5c-b531-2312f1edf691 | -5.95804 | -53.58228 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a9d6403-d70b-3421-a16d-97cb34655bc4 | -7.25265 | -45.37872 | 2026-08-25 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4c71f964-a2d9-3103-b214-5aecc84759b3 | -3.54016 | -48.17492 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2785a7b3-b3fd-3ef7-ab47-403d9e9baf70 | -7.28103 | -44.0758 | 2026-08-25 05:10:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 027436a8-73b0-3932-8360-2e40508c7f56 | -3.59526 | -54.0436 | 2026-08-25 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf996ec0-0a95-3b0c-88ee-41a1cd7390d8 | -5.78234 | -57.56805 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8ce3a70-997f-371a-9b60-d570e46955f2 | -7.2599 | -45.37418 | 2026-08-25 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 400d4376-07fb-3dab-a3d0-f2ffd9ab71ea | -7.2639 | -49.86881 | 2026-08-25 05:12:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b8d5561-3806-3b46-a26f-f4be3f6f27b4 | -6.14155 | -57.76992 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f74761c-b903-34eb-bac8-65bb8a79aa58 | -6.13499 | -57.85749 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c46407e-fb38-3a43-a9f2-6d3831faa522 | -6.80747 | -59.58613 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0506911c-5b51-3e5f-82e4-edd7741f15e1 | -6.86314 | -59.41191 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 778dda44-442c-350d-bc1a-94fc6c769509 | -11.9737 | -45.89891 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a01308f3-138e-331c-93c1-b1343ae3189f | -8.62509 | -54.7393 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a994cd11-584a-3ad3-bc5b-0958ecc8175f | -6.80852 | -59.60162 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec2d0b09-7e73-3b3c-8786-ead588779672 | -9.57435 | -49.23526 | 2026-08-25 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 447380b0-374a-3b1d-bd64-54bf7d5928ef | -6.15118 | -57.94881 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90b4978e-a724-3ef9-a756-18a5d7b56032 | -7.29634 | -60.67849 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db183510-2b61-381f-91d9-674a5ff1ff3c | -6.14619 | -57.93736 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e7736e0-3b47-3b8e-b7ab-f22933e5d05b | -8.55068 | -55.28945 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d31d512-9eeb-30d8-a708-92476a0e6b50 | -7.38412 | -55.17617 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ee37f765-5d41-36c0-8d13-4eecfdb53ccf | -10.05434 | -48.45668 | 2026-08-25 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7864a5a2-fc70-3c84-9d8c-38a343b11110 | -6.21946 | -55.92396 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bc96908-c67f-39f1-bdb2-9d812eb7512c | -8.60149 | -54.74873 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 218cebda-f226-382e-a7d1-0cbe1a58d8de | -6.74899 | -59.66528 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce96e796-f901-3599-9398-9dd1a2cf9b14 | -7.00105 | -59.2571 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 2809bf80-68d4-3934-9a49-3787f4a2baee | -12.74163 | -46.473 | 2026-08-25 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9f42306-2488-39ee-92ec-d2e6ee2441a4 | -7.2115 | -60.61452 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 83df70da-30d6-3fc3-982c-bed78dde67b6 | -7.21796 | -60.6197 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ec47b88-a627-3cc0-85bb-5a0d04bfddfd | -6.93801 | -52.77838 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a5a4bb3-24fa-36f4-80b4-170a2fa04a7d | -6.79762 | -59.60377 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c8fdc53-ba17-33f7-a110-d7c8a94dd70c | -11.97975 | -45.90577 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ab3c57d7-2225-3b26-9ad5-1bb9072373c7 | -6.98749 | -59.24723 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 13624179-42bd-3b83-99cd-e3b7df8eca35 | -6.70138 | -55.5867 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c1ddade-eee7-351a-9c9d-7f87154a2709 | -9.03515 | -50.81968 | 2026-08-25 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8ee9be33-df19-3d24-9630-4ef7e3d0596a | -7.44387 | -59.77866 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d33d0bb-e97a-3066-a590-19215316c8e5 | -12.74221 | -46.47318 | 2026-08-25 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f7afcc0-f233-3fed-831f-6b89b31209fd | -6.13994 | -57.84762 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ebea853-ae3e-3346-9415-b4145ce22298 | -9.15915 | -59.40158 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98097718-9a4d-3feb-9120-425a841814b6 | -8.60273 | -54.74027 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 653cbc37-c180-3386-ac98-37961890fdfd | -6.16063 | -57.73741 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c36f58b2-d745-3cea-867c-493e3541cbcc | -6.79394 | -59.80441 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5649cbc-958e-3a74-9481-eddeea6fd811 | -6.54203 | -58.31837 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66d70aeb-364a-31cb-85ec-06bac9def2e2 | -13.36026 | -48.21398 | 2026-08-25 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c21039ba-700e-31a9-97a3-c0b258a645d8 | -7.04533 | -56.34747 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99064369-10a8-3aba-a81a-0e613a45f4a6 | -6.81996 | -58.64734 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8230f7b4-4d53-3aa6-b11c-f5bebf5a05ef | -11.98579 | -45.91265 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 833974ec-bb28-33f1-8b56-8247c21d27a0 | -10.79758 | -50.92823 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3d302873-17e9-35b1-9824-43d0b19a510f | -6.7962 | -59.81253 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15e41352-8f25-34fc-aadf-4adef3739c8e | -6.99312 | -59.25556 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b36d80d5-7476-35db-94d5-014b2d5b8387 | -5.90546 | -57.71463 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4e23abb-070d-3b81-93b9-944b89c6587a | -12.7057 | -48.41547 | 2026-08-25 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b5bfd6bf-27a3-3b30-b4bc-54867f8fcbc9 | -10.64472 | -57.20518 | 2026-08-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33bc67d9-7eda-3ed0-8328-d54e9865aec8 | -6.85574 | -59.41452 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4884662-19cd-37af-9fc2-d6e84ddb7f36 | -6.14797 | -57.70718 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1e32a32-5b70-32c9-91c0-b6cac72548db | -7.51831 | -55.58451 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39204ab4-5259-388e-941c-320fa73e2f82 | -6.82823 | -59.67368 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59278a33-37c3-3990-8d6f-380874cd3ed8 | -8.07308 | -44.64991 | 2026-08-25 05:12:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 15a023b4-9fbc-3907-b9fb-2a0c38db9501 | -9.20043 | -59.57478 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da1b2c9a-0076-39ca-8f34-27bfe39a221d | -6.02232 | -57.79368 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4ce4d86-8b20-3ddb-be6a-82aa5894e90e | -7.02796 | -56.61758 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67035c69-9372-3439-b8bf-659c87bcc1b7 | -9.96933 | -48.32563 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README47.md)
