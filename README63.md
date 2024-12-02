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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8efcfbbc-d052-3a37-8fcf-37d0b44e7735 | -3.23071 | -53.62629 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83824297-334b-3c02-98a0-4e9fc69bb485 | -1.64019 | -53.86518 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9ddf944-004c-3edd-8821-b1370025a46c | -3.78215 | -52.03939 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 41804dac-f258-3728-8bb0-25b289f839da | -2.89003 | -54.16063 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 29155566-1f43-34d4-92e0-3267430c9b07 | -2.54641 | -53.40879 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d10102aa-fd8c-3eb5-ab6e-876ef65c805c | -3.93272 | -46.91721 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77d11537-dfaa-3943-a2b8-661b3895ccd7 | -3.95904 | -46.01443 | 2024-12-02 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 825c480c-0b97-3d3a-90b9-a1b7e61013ec | -2.42017 | -54.02261 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d8e2d25-3c1a-3a7e-b618-978ac27aa856 | -4.00207 | -46.65083 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 825107a3-6dac-38f7-bd46-6caf4fec6200 | -2.15957 | -49.75907 | 2024-12-02 04:48:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62bbe937-3bc6-316b-9648-d0f9fabbd427 | -1.96064 | -48.3926 | 2024-12-02 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73484043-872e-30c0-a8c1-0d88cf13f7e8 | -3.46849 | -50.26683 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 729cb499-689a-3d5b-97dd-d3d93ac34a05 | -3.7677 | -52.19572 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7174d72d-cdcb-3a2e-917f-b9411f28d1d3 | -3.956 | -49.99141 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbab3014-500a-3adf-8b59-0fbc28bd0026 | -4.52201 | -50.67778 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aee1bf70-ee9e-36f7-b92b-59b532cde05d | -3.66202 | -50.19529 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15abc345-9f4e-3f1f-8c6b-e0c211b867cb | -2.47906 | -46.57595 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f2deec1-8b49-3747-9a23-13fe27a8e2a7 | -1.4538 | -55.2231 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| aaabeb6a-fc03-3630-b07c-4961c4e47abf | -3.06402 | -54.0527 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36c7c369-111e-39c7-8d46-1dcc803d03da | -2.88947 | -54.00718 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee9d80be-2f83-3b71-a764-4fd27b58a055 | -2.87108 | -51.82904 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 041a55d4-1e09-349e-adf3-233b4b995091 | -3.85386 | -46.53503 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a89fda78-fe4e-3d05-a6a2-120d7391fcfe | -2.73015 | -54.10018 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38977a1f-a3fd-3ef4-9275-a1f36faff0eb | -1.90577 | -51.0969 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2435c0a7-8bf3-33c9-80c6-e12dc6e30ae4 | -4.6679 | -46.87171 | 2024-12-02 04:48:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28624b40-e737-3e21-b7ca-93a2dbfdc20a | -1.90927 | -52.86646 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f6a91ba-d19c-3989-866b-258b286c89a8 | -2.90379 | -51.46858 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ba7ef9dc-1d9e-31f8-95b8-14fde0802d47 | -1.28152 | -51.65374 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd4c68e6-a1df-3265-9841-a6d7b26e7456 | -3.30432 | -50.03702 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43ea1319-d131-3cb7-a7f7-b4c2376bd6e2 | -3.24763 | -53.65152 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72e72f21-ce85-3ad2-bcb1-ccc427990b13 | -3.25563 | -53.64524 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce820eb9-d27f-38f4-8f9e-02e8130bd964 | -3.55169 | -51.45309 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fba516f-4e65-338d-923b-4b4fcce4dd3a | -0.94728 | -51.66129 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83c6b1d7-6316-3b8a-abfe-441335364d4d | -1.2506 | -54.53897 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 32f9a8d4-961c-36bf-9d71-1b7237986dec | -0.45684 | -52.03461 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b9462b0-21d8-3afe-858f-4686ac8c4436 | -2.53982 | -46.10136 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 341dfe65-4edf-3a4c-9cb5-ee194656ade6 | -3.26421 | -53.6353 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d23a775d-7b16-3364-8945-c8799d1899c3 | -2.96335 | -53.89865 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6711ac60-858b-3c2a-9024-f0db6f48b037 | -3.21606 | -54.18198 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5701fa5-69e5-37bc-a7ac-1d265347a9b8 | -3.70364 | -50.60691 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8046551e-38cf-36d3-b51c-ebe622d1bf6e | -2.85601 | -54.06062 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b8b8d1a-f7c9-31fa-af52-bc61275f752a | -3.97958 | -49.90722 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| db65f5ee-b3db-389e-9092-e20646db5681 | -3.50063 | -50.32724 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 681cc730-e5a2-341f-96fd-a4ac0e3a3623 | -3.08546 | -54.11877 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7b173a5-aba2-3cd2-a4be-66256dce2723 | -2.3199 | -50.64334 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41875dc3-36c1-3275-9ed3-34a35c18fb3a | -3.74363 | -52.26252 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 417f8242-e14f-3488-bbda-dca19f180fa0 | -1.47848 | -47.34251 | 2024-12-02 04:48:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 799a9462-3a05-34c0-a870-93063656d3df | -2.8328 | -54.03772 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d029961e-8b05-38cd-8d38-9e55d7cdea44 | -3.07035 | -53.68549 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b47d2fe-4681-3ffc-841e-588611f5c667 | -3.04576 | -49.37378 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 567c3b88-6214-327a-840a-f5de73761144 | -3.69751 | -47.11726 | 2024-12-02 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 253d8ea7-69db-35e0-b76b-215ee9c5e417 | -2.86459 | -54.00719 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67521893-8c17-30d8-8026-55ed65b04985 | -3.22598 | -53.83059 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00082f54-94fc-305d-96b9-29d68460e4e7 | -3.65451 | -51.12142 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1caa83a0-ddb5-3038-8a1e-9df730de0149 | -1.32765 | -51.42531 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1aecf6a6-cc3a-303b-a3e8-b7148becda42 | -4.63066 | -45.46356 | 2024-12-02 04:48:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3141e943-b47e-3a89-896f-de71eacaa030 | -3.86561 | -52.39458 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76d3ad88-41dc-34df-b19c-682e3021b4dd | -3.65173 | -51.11743 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6b4bfeb-a72b-3439-ba59-ddc3e36c6ae2 | -4.11385 | -39.99176 | 2024-12-02 04:48:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a469b651-bbeb-37c4-b8ec-605d3a30747b | -3.89804 | -50.29841 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6aac0784-784b-340b-85b5-9c7e2aa49146 | -0.76733 | -52.45997 | 2024-12-02 04:48:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e639e8f-e931-311c-8257-0d4041b59214 | -2.58652 | -53.9959 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bd6690f-ae85-3c8b-be75-67185a84c02d | -3.54005 | -54.08325 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e705b356-f20b-3a82-9cfc-1d99cdc2b7c6 | -3.66597 | -50.19218 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3f4520c-bbb8-321b-a00f-e6c9ffa6c5d0 | -2.85497 | -54.11159 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e09db072-ed11-3c6f-ac6b-23c9d5614eef | -4.20538 | -50.68368 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 798dc97a-103e-39d6-9891-045d8ea0422c | -3.9605 | -52.1799 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14c90f82-a8d7-3b03-9a70-418c0ca6c783 | -3.27535 | -53.41307 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7281395-6df8-3434-8390-266dc6d36393 | -2.56117 | -53.40363 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e5c4e507-c61e-3203-8fef-97503de3fd12 | -2.8002 | -53.97394 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb36d74e-9ad0-3874-8724-9f72f4e50542 | -3.72199 | -51.08193 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccdad00b-ddda-3dd8-bc4c-fc6b6961d7e3 | -3.29803 | -52.07267 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39cacee9-dd95-39b3-8215-9cb7bcc5f08a | -3.28328 | -54.12972 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddb0f010-cc9c-3ba0-a843-cdd8e636dab0 | -3.22238 | -53.63297 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fed277d1-d06f-35c2-8403-c79d8b1f4b4b | -2.89959 | -53.96595 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd2cf93a-be0c-30ae-9d01-87b17871b5f1 | -3.53742 | -50.18088 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04cfe3ed-63b1-34e8-bea1-ef8ee4f93854 | -3.05676 | -51.05682 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14dba740-627a-30bb-875b-3ae416122dae | -2.47885 | -46.57201 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbd2d5d1-4f1d-32c7-a4d3-37ff499da26a | -1.99895 | -50.65387 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3951cda1-121f-3404-84df-72a068cc6f79 | -3.26021 | -53.63842 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78757f1b-7b44-37cb-aa5f-3836cf1297a5 | -1.46486 | -54.48885 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cfbd46d-b0a7-3307-a841-1da210ac3cee | -3.19756 | -48.57443 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0d8e693-8204-3e02-bd5f-2367d03dba54 | -3.11773 | -53.80632 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 298ed2aa-ab51-360b-9e30-68dac1f23979 | -3.7073 | -50.26192 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf2e3110-2961-3dd3-aea4-e4e180ac4f4b | -3.2494 | -53.6405 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5886adb-e9a5-36bc-a405-67652713c1c9 | -3.96381 | -52.18042 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41eb0470-89e0-3884-8cf4-c8756ab1d514 | -3.55432 | -46.02679 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f971096b-9284-3771-ac14-4b32e3d4cfe2 | -2.25071 | -53.63554 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d8a6cfa-3167-3db8-9f25-e162b0042759 | -2.59801 | -54.0134 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8afabe9e-def9-3b1b-8aa0-2a0d48e01df6 | -3.49217 | -50.24826 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51bbe150-e088-3025-ad6e-cd34c93a01ff | -1.57252 | -51.18613 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 772c94dd-2070-3cd2-8c78-4e1083e0e08c | -2.59114 | -54.22197 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c385c646-7840-3e26-933f-1bc107f84a3d | -4.06332 | -49.05705 | 2024-12-02 04:48:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 58440e93-f3e7-3623-8689-250a8f99990b | -2.61013 | -54.0822 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59db1953-ce8b-3f88-849a-29bb31d4c0b6 | -1.44117 | -55.23026 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0bf17b1-4e32-336f-a7f0-62392a82b521 | -1.38628 | -55.18932 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fb6c84f2-c26c-3c60-a73a-6b8c52a58caa | -4.05374 | -48.96056 | 2024-12-02 04:48:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bb10e8b4-a480-3e21-a9b3-52627da83e43 | -3.16947 | -53.63601 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a50847c5-000b-311f-97a0-b3b67e0595f0 | -3.21319 | -54.17758 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 431068d3-341c-3aa8-9848-d3c66202e060 | 1.21211 | -56.00961 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README64.md)
