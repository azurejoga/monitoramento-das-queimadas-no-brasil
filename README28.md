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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3da8f323-cee2-3f5a-9b55-b84fd2e4da53 | -9.44807 | -46.70611 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08a640f0-bc66-32c5-8634-c3a2af134efa | -5.73338 | -45.59549 | 2025-09-10 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5ff71dc-672d-3949-a61c-1b5be98ae22f | -7.79122 | -46.06351 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ccb0dc8-8056-3929-9196-926df57ae646 | -6.96861 | -44.79291 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1048884-c5ee-35d7-ae85-83da792566d7 | -5.42358 | -42.80733 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 33c439ca-5bc0-3bc7-9ab5-65e2d6ffd6f3 | -7.77825 | -46.12959 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55631122-754c-352d-9811-53437a6471ef | -8.04602 | -48.67776 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 19.9 |
| ea95f355-d9e1-36fb-8822-98c46439b976 | -6.35651 | -44.06007 | 2025-09-10 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78b9a49d-af94-3c46-869c-bfdff08767e3 | -5.41974 | -42.81026 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 968b06a3-6c85-35b5-9928-766d41569108 | -5.66979 | -43.90467 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79929f12-2e96-3aad-83fd-a6ee7b334b59 | -7.59305 | -49.29156 | 2025-09-10 04:14:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 94785cc7-04ee-3c93-b910-976c48183e33 | -7.86817 | -46.03989 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad77ad82-b3f0-365d-a428-0a6c574247cc | -9.01051 | -46.0551 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b32693b-63a6-33bb-8453-03d034b66499 | -7.19414 | -44.93972 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df4db4b6-39b1-34ed-a0b0-22110b9fdb43 | -8.74854 | -47.09167 | 2025-09-10 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7231468a-5d05-3226-8c1d-118852301169 | -7.52749 | -42.53172 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4ab58385-e5fa-3661-a1ee-67b263fda1d9 | -9.55837 | -48.29251 | 2025-09-10 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04bf676f-ed66-3713-b1dd-0095069f28b4 | -9.08899 | -47.05392 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a46b8fc0-65a3-31d6-b7a1-e67eca30d9c9 | -6.21649 | -43.50058 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d58bc087-7de2-3116-8df6-a4b1cd6a828e | -2.344 | -47.5942 | 2025-09-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c8dc045-4f26-359e-932c-12a4803ba203 | -6.19809 | -43.40233 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ee5569d-bbd5-33fb-ae51-5b4b223d58d0 | -9.06631 | -49.82762 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edbb9aa5-165c-3d17-b3d7-f747197efc6e | -4.88354 | -44.96 | 2025-09-10 04:14:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e96422b-f299-3891-98e8-44662275c977 | -6.293 | -42.20316 | 2025-09-10 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 61371bc9-b794-3fbc-ac04-24704ad56582 | -7.08958 | -44.13755 | 2025-09-10 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20fedec6-a64a-3e7e-9ef5-fcb2bb39eaf5 | -7.7785 | -46.05355 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92915b6a-ca61-3358-be55-ff5a707091a2 | -6.45879 | -43.04123 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec52adae-fe81-3ff6-b6e8-750a4cf18370 | -5.76902 | -45.52945 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8366219c-edfe-3fbc-bfa1-4bc0d9a62a2e | -6.4401 | -44.04825 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b636c18-3860-3c51-9a04-66874d03001b | -6.17492 | -41.0545 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66238609-8b33-39a2-bbfa-65b54436d3b1 | -4.83522 | -45.35373 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d2bd400-0500-35c0-8a9e-0a54f00880ce | -9.03362 | -49.78873 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d3af2de4-64d8-3e0d-b89a-465d0b393923 | -9.52344 | -43.05967 | 2025-09-10 04:14:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2fdf33bd-2ead-35cc-8f8b-0132923138a7 | -6.38331 | -44.45063 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c1b4840-73bd-340a-a559-c06519e55276 | -6.46841 | -41.79341 | 2025-09-10 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 94bc796e-8ef0-3b1c-a66d-3906b2729284 | -8.42789 | -49.11296 | 2025-09-10 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b235d9c-d87f-3454-ada1-72c721788323 | -9.82298 | -46.05311 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb08903f-c2dc-3564-9654-0df27376b952 | -9.60805 | -48.04288 | 2025-09-10 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d49e819a-9ba2-3247-ac68-cfaad24ae64b | -9.21774 | -50.54935 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0bc4801-88bb-3334-a043-bf0ee92dd8bc | -9.06863 | -46.97661 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0625ef20-598b-3aec-a1b8-a48dec32165f | -6.40023 | -43.50182 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0793ce8-f333-3a9f-ac44-ae40d651e551 | -7.86719 | -46.02387 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46f524df-b9d9-3315-a983-ef3e8d6f7d64 | -5.22816 | -43.68428 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63d65881-8d76-38b2-bb68-1297ee486485 | -6.21525 | -45.61815 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19a7c935-f9ce-3cc5-9b67-c8f4fbcf1d84 | -5.85727 | -44.20418 | 2025-09-10 04:14:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ba75351-d2fc-3fe7-a221-12227ca61c7d | -5.66148 | -43.91415 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63a5904e-d1ac-3cc9-85e0-9e51e232b421 | -6.68397 | -44.54962 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ac7aeed-fa61-3edc-a41f-86eb6f94c2fb | -5.67864 | -43.89175 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23f21450-da57-31e0-bbd8-37aaf7ee22b5 | -5.54725 | -45.37683 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89106b1b-6898-38fd-96b0-28a4f4710fb2 | -9.10214 | -46.97461 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2d26930b-22d6-3a0a-8bfd-5f37d5c9282b | -7.68397 | -44.76458 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 662633ea-5ffc-3aee-8de8-dab261cb2429 | -5.98744 | -43.70207 | 2025-09-10 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 875026b4-af5c-3047-afba-1a3f0703cc70 | -8.42866 | -47.27679 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 340289ca-b59b-3dd2-8a83-cfcd2772b581 | -6.25251 | -43.40026 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b8946e5-3b88-348c-97e0-5699de2efda9 | -5.22484 | -43.68377 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 401d7db9-b354-3202-b8f8-8709a1ca8d3d | -5.49125 | -42.6555 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0953c254-1c93-3985-8438-6a9e6717aaeb | -9.14592 | -45.5661 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e989c54e-5465-3373-b42e-927eb6b6e164 | -6.41134 | -45.29045 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ee27f63-9196-3bf0-9c4c-a47b2ace38ca | -4.97602 | -48.93894 | 2025-09-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1b0eb232-42db-35d5-b439-f6cf162fc6e7 | -6.39898 | -42.61724 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| afd9e084-b701-373f-a676-abdc70fbe3e8 | -6.06237 | -43.13752 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ac788022-d95b-3cdd-b8d9-8edc9eb9ef11 | -7.79622 | -46.06415 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04949337-52fe-37df-9cad-40dc37f5582e | -5.63416 | -42.61406 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f545060e-e83f-3669-a56a-3efc090e0a15 | -9.05479 | -45.74133 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2b57967-de73-3953-9dec-21f7dccbff4a | -6.92727 | -45.51086 | 2025-09-10 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58ffaf7d-b3ee-3d64-a2b7-251696bd0c45 | -7.78409 | -46.09425 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f2177a6-29bc-303f-bb27-7ec855844121 | -5.80502 | -44.83918 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deb0536b-7e6e-3633-9065-00bc6f5a5405 | -9.31686 | -46.73096 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 1114f0f7-28c1-370b-a9b6-97331fc5383d | -9.07084 | -46.98548 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 447a37a2-509f-3ffa-8ec7-bf38323893f2 | -4.3274 | -48.39526 | 2025-09-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f64fad1b-4a6a-31a5-b635-23353dba9bee | -3.32912 | -42.86392 | 2025-09-10 04:14:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d9c2269-c5be-3f46-a61d-fcb1d541c59d | -9.09279 | -46.9643 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9973e84a-a389-3aaa-aa3f-3e11d36a098d | -6.40101 | -41.76086 | 2025-09-10 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e86bb859-557d-3d3b-a108-ad50de7deea5 | -5.523 | -44.20909 | 2025-09-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc13e215-14a2-3bc8-bb35-71cbbbd55028 | -5.36858 | -45.96704 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f6ed120-3849-3efe-b188-6f8c884f12b6 | -9.01496 | -49.54574 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66697f0f-9937-3e18-be04-7d91f24f40ea | -7.87005 | -46.02827 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61130593-e60b-30ba-9fbb-977509922ed5 | -5.86556 | -48.16013 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b083fdf-f64a-38d3-8f1d-5c49ba9c1e9d | -6.34048 | -44.07542 | 2025-09-10 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa72061c-fbc2-3194-a33c-f142a44cdc9e | -6.39917 | -41.76086 | 2025-09-10 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 61014074-5bbc-382b-a29e-345c666d54d7 | -9.05919 | -49.81807 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa75a7e5-561f-33bc-a86f-ec4b39f3b604 | -7.42567 | -40.08126 | 2025-09-10 04:14:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 99881fa4-651a-303c-a919-2bcdece857d5 | -6.35595 | -44.06357 | 2025-09-10 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1729a79a-ca18-3187-a345-a5e40f8c5f1f | -6.35872 | -44.06761 | 2025-09-10 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53836695-69ee-3d9a-b4f3-885a7c3f08c5 | -6.24489 | -43.42732 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0df1074c-6e98-3805-83ac-332852c638bb | -5.34259 | -44.81143 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b15a287-6172-37e5-8a98-e20d664de6f9 | -6.85064 | -44.91449 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a373c2fc-8cf9-351f-bf41-1dab8df1d0f4 | -5.67754 | -43.89874 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 801d340f-d58b-37c6-89e3-a82aeff00a46 | -9.6659 | -46.6417 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dd2bf2b-121f-3895-b4a6-9e6c27fe37e8 | -7.68863 | -44.7142 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77ba3bf1-75c6-39ab-ab10-931be90abfeb | -5.56801 | -45.11641 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e1e7855-5858-39ab-b14a-b5b8c080ff4c | -6.09237 | -43.36098 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65e388e5-ff4d-3b72-b38b-3305f10949c1 | -9.07643 | -50.47353 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c372c8b-741c-312c-9924-da16b4cf77e4 | -8.04665 | -48.67408 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ad9fd74-86e9-399a-8255-3cda14ad2c0e | -7.4629 | -44.9348 | 2025-09-10 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5e7af19-bb18-3f95-b14b-7d1760cb6308 | -8.06569 | -48.65922 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17a888c7-b097-3dfe-9476-c193b660719b | -9.15608 | -45.56775 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9784d5cc-7c76-3cd7-a4fe-8a99d9f8aa86 | -6.20546 | -43.29055 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76d4263f-cefa-307e-8de4-1a473808bef6 | -8.3055 | -44.81995 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7ed1bfa-08ff-3029-aa4e-4d05f96f75d5 | -6.65252 | -44.08237 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
