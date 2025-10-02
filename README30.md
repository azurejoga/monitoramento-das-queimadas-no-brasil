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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61fdb728-3610-3721-9e85-cde33ad17a54 | -8.70253 | -47.86631 | 2025-10-02 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18b179e9-9d81-39ea-a1c2-f88421bf2eda | -10.2139 | -50.27604 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8417adef-188e-397d-9f64-2fcdb0d4dd8c | -7.78835 | -42.50403 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 421df845-f262-3847-b4a9-4bf0d74b6808 | -12.82283 | -47.02922 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65a46558-abfb-3411-a0a4-33d306d01bf2 | -11.14321 | -43.37993 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fdda5849-4ef4-30ab-bd29-bf266b349d8f | -10.81998 | -46.62788 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b5450ac8-8621-3cc5-8c88-e938d2f3f2f6 | -6.9638 | -45.32203 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b34c95b-c775-333f-bf1d-0e63abd34b4e | -11.18276 | -47.19002 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56dad725-01b3-3f9b-b8e6-a1c6e45ee98b | -12.07453 | -47.83556 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa1b17f9-8f6b-374f-bbd7-0ae54e3233d2 | -9.92976 | -50.49213 | 2025-10-02 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5aeb6530-501a-3939-884e-fc23ba31258a | -10.26681 | -50.33599 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 509c1136-d791-331b-b43f-c8f85bae23a5 | -9.45122 | -45.47452 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecc20df8-ed44-34e9-aec1-bd719809b48e | -8.66576 | -47.69278 | 2025-10-02 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ac82867-736f-3769-b1ef-c1c41cc1a5ca | -6.35511 | -43.29581 | 2025-10-02 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d0fd98e4-aadb-3d4f-8e6f-cfb624674eb7 | -11.54548 | -45.06284 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 127744e8-ed7b-32ec-b18b-4cb95f807e48 | -8.38069 | -41.85662 | 2025-10-02 04:02:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1d1e261-874d-332d-8ab0-4d1e5b65754d | -9.42681 | -47.36246 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8b743b9-3674-385f-833a-8a92131d8e66 | -6.32491 | -43.04006 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 12c3e62f-d824-3cd7-ad50-eb11371640a5 | -9.45372 | -50.90078 | 2025-10-02 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 647af9b6-1455-3ef7-81d0-9f76faa0d2e6 | -10.23592 | -50.32305 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 1d0c32e9-941b-3bbb-acf4-78ebbfcbf096 | -9.94964 | -43.70001 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3476700-4422-3c2d-9edd-17dfb98e21ff | -7.30886 | -42.88169 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01aaacf7-1293-35ac-8b4b-923216194f45 | -10.93491 | -48.58239 | 2025-10-02 04:02:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91629323-2ad7-3b71-ac7b-70ac8c1f9cc6 | -11.0008 | -46.59612 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| ab6b5d59-851a-3847-baaa-8b60683cf023 | -11.59526 | -45.05085 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48058885-1b00-3889-9587-ffc0a16cb9b9 | -11.48399 | -45.10779 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27df60aa-1e34-3f61-9030-a5ae39d8cd45 | -11.5801 | -47.66113 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8771ade-49f8-3483-ba3e-10b59954ad44 | -11.3613 | -48.33722 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6be0b909-6c53-3d7c-b851-017a866f5ec3 | -8.51327 | -47.80509 | 2025-10-02 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7d347d8-6ea0-31ae-8354-f57534bd7eb7 | -12.81938 | -47.02472 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6138f4d-76df-3613-a6b7-2db5049654de | -9.43206 | -47.35871 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74da3ff1-4943-3572-926a-fdb7f1877231 | -10.81775 | -46.59188 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41fc2026-2ba3-3fec-98c9-f6f9f1e7527b | -8.88866 | -46.59797 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec3b1b66-8f92-3f51-9ba7-b26a896226f5 | -12.8077 | -47.01867 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 97ae20eb-3ae8-303b-9af8-ab79df8a073b | -7.40013 | -39.69671 | 2025-10-02 04:02:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c4c86d41-0a80-3818-8c29-07fbcc206b8f | -12.83905 | -46.86697 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6253b79-1bc6-3cf3-a83b-9bb7fd01e9d0 | -11.07862 | -47.80528 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 03e087f2-2c7a-3613-960b-df721432838d | -11.811 | -45.00709 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 571da5d4-bc60-3729-9caf-4436a9f0b3d9 | -9.93472 | -43.76905 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 0cd5c3ee-588a-339f-92cb-cda3e5cce64f | -9.33112 | -45.67744 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77a420a5-98b4-3777-9b3d-6c64fc0dd759 | -12.89495 | -46.90453 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06d24c62-62d4-350e-a470-db02d89f0f7d | -12.86945 | -47.00579 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 337d0f59-c1c4-3183-b2d4-4edb6277eb91 | -11.81547 | -45.00311 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3c0254b-f90e-3b83-a0da-e315dc7b2a38 | -7.7834 | -42.53442 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6004ea56-099f-339a-97a4-55bf8cecfbc2 | -11.81333 | -44.90219 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0de08d51-5fc8-3008-abd0-69759c2848bb | -9.93941 | -43.74032 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 97dac674-cf86-36aa-8e9e-b3bc6ddd29aa | -11.14628 | -47.19641 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6b7d31b-82a6-32a4-a3d2-2c4c58047f94 | -10.18155 | -50.2416 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 708e1f64-5ce6-320e-b931-2f190320028b | -11.67218 | -47.49953 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f835dd68-e458-34b7-a19c-be7d4916e697 | -7.78366 | -42.51108 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1d496c58-b6d3-314b-8441-e0a1f51eabb7 | -9.38371 | -45.82999 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53b9e56a-72a0-3a9f-b366-d5346c8910d6 | -11.20047 | -47.18969 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fdf9f0f2-740d-3276-8d8f-af1865b44eb1 | -5.84114 | -45.75401 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9ac3b0c-e78e-39bf-885a-48c014cb0f25 | -7.30404 | -42.88909 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 742d78b4-caf8-373b-879f-af8ea774e0f6 | -7.77185 | -45.71101 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2645128-a89a-3504-90ca-e59bfe0ae398 | -11.79696 | -44.9999 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e20621bb-6e4e-3b9b-b542-4d252d8b291e | -10.22633 | -48.2136 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f048596-da69-3eeb-83f6-25972b24638b | -11.87499 | -49.91175 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84c27c6c-441a-3e5e-afea-aaeb3de3d88b | -10.8358 | -46.61075 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| aa88c6dd-6d75-3789-9944-63316dabc1f9 | -12.86878 | -47.0096 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26659b28-27f2-3923-a292-452228e0dbdd | -11.47322 | -45.00459 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03f1047a-07e6-3aad-9e92-07d694b28c34 | -7.77244 | -42.53653 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| f485fc9d-3963-352d-8a68-5713863d5f18 | -12.85646 | -46.93518 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c2e359c-9647-30f7-a080-950ccbf497d7 | -12.6398 | -46.95236 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| afe29d18-6389-35f9-861b-c074fb09eb61 | -10.44771 | -48.08486 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c00da72c-0af9-374a-a998-6f0f0cd7a525 | -11.26244 | -47.81368 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d01365ff-ef74-3844-8764-c615e259b6c1 | -10.20383 | -50.27058 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ca9d71c3-e600-3552-a021-564bbb06cb58 | -11.80077 | -44.97715 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c75e7ae7-f030-354b-a169-71b0db842221 | -12.11896 | -43.43397 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24d6814e-1b37-38b5-876d-e2d4164d5abf | -7.42065 | -42.88662 | 2025-10-02 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50279819-efef-3244-83f6-edfe99a1f599 | -10.24194 | -50.3206 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 3ee4135b-30a7-339b-ac80-2ad6f93da21c | -6.22948 | -45.33421 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22d1776c-1b04-3536-b7aa-8fe58cd37f00 | -11.13224 | -43.3819 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51a5a3b3-99dd-3310-95dd-0b3840d81632 | -11.86983 | -45.01075 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed15cf51-678d-3b20-8f81-92d270b1e56f | -8.90445 | -46.66051 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bf9a240-4fff-383e-ac9f-e1c0d30be1f4 | -6.88032 | -39.27657 | 2025-10-02 04:02:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4ff157a7-b19a-3eb6-a639-f08a691ef864 | -8.55736 | -44.64972 | 2025-10-02 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bb6e06b8-b899-39be-9d8c-de5ed1bc66cc | -12.41163 | -47.50091 | 2025-10-02 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1a805c27-81ad-35a9-8f69-082581b78076 | -11.46512 | -44.96173 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c085669a-69d8-31c9-90ff-0f854ebfceb0 | -10.81582 | -46.62716 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9b4b2aa-9cb8-3d13-9f62-fda0ba1c5c8e | -7.05032 | -43.31201 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3d1af726-fc02-36f1-83a2-f83560c88e56 | -6.48229 | -44.28934 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1d51af0-3acc-3b6e-a138-72ee5b5bb801 | -12.71306 | -46.89096 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 301076a2-f6f6-39d6-96b8-6a88a823347c | -10.22192 | -50.3383 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39c9a088-489b-38ae-80dd-0d40cb5f680c | -11.58855 | -47.63961 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4931a6a2-9a1c-324b-a563-97a358bb2b5d | -10.83379 | -46.62226 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c23f470c-da47-3f64-a4a8-e67e51b3e8b7 | -10.81988 | -46.60406 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3376dc0e-2ab1-391f-81bb-166f0663baf6 | -6.23417 | -45.33141 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 35cf922c-4833-3dc2-aa3d-b24ed99690f2 | -9.94719 | -43.67042 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41f2ead4-e4ee-3735-b84c-1483aab555c7 | -10.48734 | -49.36982 | 2025-10-02 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a0ac10e-8efa-3ab7-8d3e-f8e54e1efcfa | -8.8252 | -44.79046 | 2025-10-02 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dae41e3d-db31-38ec-8909-f121fe157c0c | -11.81494 | -45.01962 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17343aee-3900-39d4-91a4-c26ba427adfc | -10.26532 | -50.31428 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c8130c9-7948-36e4-bd9a-6e1ed1c6e575 | -12.11802 | -43.41828 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a990b84a-3846-37c5-bdb8-9a487b2a9c28 | -11.81886 | -44.99697 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2887ad9d-eef1-30ac-bcc2-86b3dbfcc3d6 | -12.11208 | -43.43293 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2f1b67d-d5d5-3b78-bcab-50c5a54ac3f5 | -6.28643 | -44.0659 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e26eb1a3-16ae-39c9-8895-c171eceadb00 | -7.01022 | -44.5037 | 2025-10-02 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31f8816a-0427-38a2-a885-a567801da730 | -9.42235 | -47.36166 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c32cd84-1d88-3ea4-8710-dd2b0b1422e5 | -9.94319 | -43.76193 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |


[Clique aqui para ver as próximas entradas](README31.md)
