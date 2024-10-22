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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 002034a1-1f1e-32c1-b6a8-f69df31ab9a4 | -2.7403 | -49.329 | 2024-10-22 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 4468a90a-c156-3221-9379-7f1a1ddae64a | -2.7404 | -49.3077 | 2024-10-22 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 88875a52-22b7-3867-abcd-3668cd5f871d | -2.7588 | -49.3285 | 2024-10-22 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 227.5 |
| 80b63111-cedd-364c-b03e-7ff31a6c669f | -2.7589 | -49.3072 | 2024-10-22 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 183.8 |
| 8158e8a9-729b-327b-ba88-7f0e58555a44 | -2.7773 | -49.3279 | 2024-10-22 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 5477e298-cfc5-3d46-b8b1-b1cd4d307249 | -2.7773 | -49.3067 | 2024-10-22 05:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 1140b35c-5df7-314a-91bb-ab20a2597dd1 | -3.35573 | -68.12612 | 2024-10-22 05:57:00 | NOAA-20 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 128f8532-198d-3930-aaf0-0d975d8b318b | -8.95709 | -65.92178 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6076fb4d-52e4-3ab8-a22e-c58516c5bcf6 | -8.95636 | -65.92686 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed781809-15bb-3e56-ac2a-47b30d768459 | -8.95314 | -65.92119 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a0450d4-db7b-3e0e-8135-7190e151f122 | -8.95242 | -65.92628 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10d9ea40-eea3-306e-bdae-728f0535a6c0 | -9.37075 | -66.48832 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d28274b-eff8-3308-8b5b-2d7555d003ab | -9.19476 | -66.07866 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee163f99-6659-390c-9490-5fece03ea934 | -9.19402 | -66.08372 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a99848ea-e9e4-367b-acec-5537cc707ea3 | -8.96279 | -65.93817 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7511ae34-7a24-3a9c-bfb1-a0584d433c30 | -8.96103 | -65.92236 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7097f4e0-f82a-3f5a-9294-a68cc1fc7792 | -8.9603 | -65.92745 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e2dede37-b5d8-3b54-b4ca-fec74e509435 | -8.95958 | -65.93253 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1c7d35c-b446-3c9c-bc4f-981ef4bbcccb | -8.95885 | -65.9376 | 2024-10-22 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e385ae3-3456-38db-bf97-ff35eae41f73 | -7.82282 | -61.37247 | 2024-10-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d75f4ff0-b1f0-3563-a96a-52b26e81aeff | -7.82237 | -61.37574 | 2024-10-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1400ef8a-0fc2-32d5-a203-2736c816a2f2 | -7.81709 | -61.37498 | 2024-10-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 836202a6-2486-3fcc-88fb-28503696d05a | -7.81664 | -61.37824 | 2024-10-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9f09d32-65f0-3035-92c0-50d8761f707d | -7.80202 | -61.56421 | 2024-10-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eaf90e0-fae7-3e15-8f10-ca37269c8de8 | -7.8016 | -61.56738 | 2024-10-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fcfdfe8-76fb-30d5-b510-b57393fd068e | -7.80153 | -61.56371 | 2024-10-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39b5d051-848b-32c7-ab5b-8adec68d499b | -7.80109 | -61.56688 | 2024-10-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee202d43-66e5-36f6-9ff9-5f0675679936 | -16.08955 | -60.12851 | 2024-10-22 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2edf1ac-e5de-356a-8c14-758686300acf | -16.0837 | -60.12249 | 2024-10-22 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 239e35fd-3b4c-3da8-be1b-e281e4c4395e | -16.08318 | -60.12782 | 2024-10-22 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18a271cf-c49a-3483-befe-336f24b589b0 | -8.01202 | -37.16276 | 2024-10-22 12:29:00 | TERRA_M-T | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 37.7 |
| bf7faf91-cde8-3d0d-b16e-ede9fcf85fc8 | -7.59183 | -37.68039 | 2024-10-22 12:29:00 | TERRA_M-T | SOLIDÃO | PERNAMBUCO | Brasil | 2614402 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 20077c2c-1317-3c3d-be67-2383d5ad0594 | -7.19436 | -38.11501 | 2024-10-22 12:29:00 | TERRA_M-T | IGARACY | PARAÍBA | Brasil | 2502607 | 25 | 33 | nan | nan | nan | Caatinga | 25.9 |
| e8e1cac3-7f13-3276-8441-8065b0642394 | -6.90402 | -38.56631 | 2024-10-22 12:29:00 | TERRA_M-T | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 84855fa2-2c87-34f1-82db-6fe846e43040 | -8.87173 | -38.77087 | 2024-10-22 12:29:00 | TERRA_M-T | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 47.3 |
| fae15737-674f-35a8-baed-ab5415062ac7 | -11.82701 | -39.1776 | 2024-10-22 12:29:00 | TERRA_M-T | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 39.0 |
| cf7cecec-1ae6-31ac-9b5d-0dda19d537e9 | -7.96425 | -39.8225 | 2024-10-22 12:29:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 8d63867c-9b0a-3fd0-951b-6044a12f79a0 | -6.85431 | -39.03432 | 2024-10-22 12:29:00 | TERRA_M-T | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 918fd299-fcc5-3575-92cd-b7cafdf8100d | -6.85241 | -39.04875 | 2024-10-22 12:29:00 | TERRA_M-T | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 1d25c123-455d-3c0c-ac71-f241d0e27850 | -8.83453 | -40.41454 | 2024-10-22 12:29:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 385437ed-218f-39b1-b49d-c7a06ecd380b | -8.81146 | -40.27146 | 2024-10-22 12:29:00 | TERRA_M-T | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 12.3 |
| c197cb0a-59b2-3f2a-957c-33dfe4cd4895 | -6.08385 | -40.43601 | 2024-10-22 12:29:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 44712dc6-319a-3939-94db-d658ab1a756b | -6.08227 | -40.44723 | 2024-10-22 12:29:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 18.5 |
| f8f77f71-4272-3e89-a9b0-0188267eb6e8 | -7.32942 | -42.16511 | 2024-10-22 12:29:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 9efd406e-8264-3e14-957e-6d5f65c6010b | -7.32809 | -42.17465 | 2024-10-22 12:29:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| d500b4eb-41f2-372f-96e2-fab4fcdc9059 | -6.93602 | -41.43412 | 2024-10-22 12:29:00 | TERRA_M-T | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 91ac07f1-0faa-3ecf-88ee-c98bd2189196 | -4.07368 | -42.89281 | 2024-10-22 12:29:00 | TERRA_M-T | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 239ac2cd-2b1f-34e1-a8b7-6e32ee059685 | -6.84601 | -41.48818 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 77637b7d-d47b-3c2b-a0ac-36bb0095d95f | -6.82069 | -41.66739 | 2024-10-22 12:29:00 | TERRA_M-T | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 983244d5-5793-37e4-a79e-be42562f4d73 | -9.86634 | -42.3361 | 2024-10-22 12:29:00 | TERRA_M-T | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| de28a74b-09e5-3ca1-b294-247560fb9d3b | -10.53697 | -42.39668 | 2024-10-22 12:29:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| da71f28d-9dbb-37a5-84d7-48ffc8ba5a3e | -11.25083 | -41.72591 | 2024-10-22 12:29:00 | TERRA_M-T | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| ac75dc9d-5ead-36dc-8316-a61e76d1cfc2 | -3.58138 | -41.8321 | 2024-10-22 12:29:00 | TERRA_M-T | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 91d03a95-dd52-3df6-a5ae-fe0c48385c70 | -3.38589 | -42.42213 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 13.2 |
| ea5c6c09-8b3e-3d87-8ede-c3a74a8fad95 | -2.90299 | -41.93479 | 2024-10-22 12:29:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 26c3369c-53eb-3d68-b015-1569f84608e2 | -3.50258 | -42.64052 | 2024-10-22 12:29:00 | TERRA_M-T | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 34d5bba0-cdac-30df-82c7-ac2901b0c820 | -3.40913 | -42.71146 | 2024-10-22 12:29:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 65f0535d-ce59-33ea-bd31-14427c2d4196 | -3.38461 | -42.43099 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 9a6bc224-f63d-32e8-aec4-2cd45e9e6450 | -3.30329 | -42.61829 | 2024-10-22 12:29:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 589cf1b1-ef11-3499-b66a-a7ba7f17bcb1 | -3.15067 | -42.83623 | 2024-10-22 12:29:00 | TERRA_M-T | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 6d0fbce4-215c-378f-8238-c808d49dc43d | -3.1494 | -42.84503 | 2024-10-22 12:29:00 | TERRA_M-T | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 93b62788-4257-3b8e-9f2d-9bce77f8c5ac | -4.62774 | -42.38161 | 2024-10-22 12:29:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 583bfa83-350d-3a1f-af42-3559c48b44e9 | -4.62646 | -42.3906 | 2024-10-22 12:29:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 902f576b-fa1a-3634-83c5-618da55b5bf2 | -4.09952 | -42.46258 | 2024-10-22 12:29:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| ff4b3ca6-5477-3db2-b612-25e39a5566b5 | -4.9229 | -43.20914 | 2024-10-22 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c90c15ca-f975-3412-8e7d-03776768b3c2 | -4.17161 | -42.99091 | 2024-10-22 12:29:00 | TERRA_M-T | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8318cac0-2913-39d2-b252-8c30f78d212a | -4.12886 | -42.96092 | 2024-10-22 12:29:00 | TERRA_M-T | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 53216780-2f71-3b7a-b089-7571ce51be85 | -4.07241 | -42.90163 | 2024-10-22 12:29:00 | TERRA_M-T | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b22efa89-0334-3d8b-b904-4dba458dbff0 | -3.59442 | -42.8308 | 2024-10-22 12:29:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 36ed64f4-6245-3cbf-9cd2-d88b066a89a8 | -5.43715 | -43.22857 | 2024-10-22 12:29:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4a1b13f5-e8b6-3524-899b-bbe1966cf68e | -5.40456 | -43.19095 | 2024-10-22 12:29:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| e31de11d-d8c8-345a-aaa7-87a6ee863c64 | -5.29125 | -43.02422 | 2024-10-22 12:29:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 30318927-664b-3529-9ee4-00afc4f6c48d | -5.23189 | -43.17231 | 2024-10-22 12:29:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 203.3 |
| f18fc938-60c6-3f92-ba62-57e62ab76535 | -5.23061 | -43.18115 | 2024-10-22 12:29:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 214.3 |
| be528f88-6bd3-3ef1-b491-b35e3a8054a4 | -5.22934 | -43.18999 | 2024-10-22 12:29:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| faf40c47-7683-3737-be96-955c609e9caf | -5.22303 | -43.17107 | 2024-10-22 12:29:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| dac8dd53-6744-356b-b786-95445ba822dd | -5.22175 | -43.17991 | 2024-10-22 12:29:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 17e8385c-81fc-3127-8750-22df6f0acf37 | -5.17326 | -42.87758 | 2024-10-22 12:29:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| faa263f3-c7f9-3c65-837e-8aa1de9cdb33 | -5.17198 | -42.88646 | 2024-10-22 12:29:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 58fbd01e-9d73-362a-873d-6850dca7c3d6 | -5.1631 | -42.88522 | 2024-10-22 12:29:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c40f0817-55e9-326d-afc9-78b653feb6d0 | -5.09443 | -43.11052 | 2024-10-22 12:29:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b8c220b9-990e-3f90-a102-5a36b92c29c5 | -6.42405 | -42.63972 | 2024-10-22 12:29:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 21cbec5e-e8fe-3ae3-a8ac-264389ddc56b | -6.42275 | -42.64875 | 2024-10-22 12:29:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d0d9b489-1ef7-3c80-b978-48e95f46fb88 | -6.30056 | -43.43347 | 2024-10-22 12:29:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| be4a7a05-5184-3a50-b0c1-58b860067695 | -6.29928 | -43.44232 | 2024-10-22 12:29:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3e11136d-7c1b-30af-9432-e597fc688a55 | -6.20103 | -43.422 | 2024-10-22 12:29:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5125edb8-f525-3d46-a5c6-3779e6173d19 | -6.19976 | -43.43084 | 2024-10-22 12:29:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 071c6b2f-eb5a-3b7b-a7d7-243e5814afd8 | -6.1909 | -43.4296 | 2024-10-22 12:29:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 768edf3d-3674-3987-afe0-f118107b49fc | -7.56783 | -43.79628 | 2024-10-22 12:29:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3f212641-a3f2-36e8-811b-d1267334a518 | -7.32991 | -43.20203 | 2024-10-22 12:29:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| f6efcc7c-5212-3425-8872-84f9b8115e00 | -7.24062 | -43.57106 | 2024-10-22 12:29:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 645d87b9-e232-380d-828e-f40c634304fd | -7.13283 | -42.51744 | 2024-10-22 12:29:00 | TERRA_M-T | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 3912be2d-a8aa-3021-a6b6-c155abd38028 | -7.06559 | -43.44331 | 2024-10-22 12:29:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| c113d590-ca26-389a-b5f3-4e8b17dba2c3 | -7.06432 | -43.45219 | 2024-10-22 12:29:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 4f3d9640-3432-330e-a430-77ccb69f247d | -6.98381 | -42.39933 | 2024-10-22 12:29:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 5af5ed37-ede3-3827-866e-61564e6895f2 | -6.93017 | -42.7754 | 2024-10-22 12:29:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 70512d4d-86ed-3468-a769-72eff371560c | -6.70605 | -43.05294 | 2024-10-22 12:29:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 11d434cf-7b5a-3cea-a279-8042c4657afd | -6.66154 | -43.04672 | 2024-10-22 12:29:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 75125e4c-b4b1-350a-8a8a-2c7b25573470 | -6.66026 | -43.05566 | 2024-10-22 12:29:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 2b41cbff-c8eb-39fd-a42c-d0b441a58ec1 | -9.607 | -42.93483 | 2024-10-22 12:29:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |


[Clique aqui para ver as próximas entradas](README34.md)
