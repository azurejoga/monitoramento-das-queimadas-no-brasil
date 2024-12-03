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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d98bb695-50fb-325b-bebd-1732ed7bf17f | -3.55482 | -50.17876 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9fa9b3cd-5412-3da6-b006-5a746420cd21 | -3.26409 | -50.21186 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a778a20-56af-34b4-ae54-1b9c0ea5455a | -4.07215 | -46.67989 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01e6e2db-6d89-3169-a169-74770432d742 | -5.79402 | -46.48153 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 41245c44-c790-3374-8668-a1edd8d04340 | -1.72971 | -52.6179 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a98bc75d-d009-3622-a981-0f34d81367b8 | -2.33064 | -53.92678 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 98898044-330d-32fd-860a-c63050fc0e31 | -1.75097 | -52.80293 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32d87561-991e-3810-bb55-98d677147539 | -3.67102 | -53.80614 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5e65723-752d-3dcd-ac15-e514d652433b | -5.16822 | -44.80712 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d07c4bd1-f641-3385-91ed-a116d77f986c | -2.8082 | -53.04037 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78aae3c6-6a2c-3be4-8e7a-a542f06c4c03 | -3.38586 | -51.14528 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47eff2c3-238c-394d-99d6-815c8b6f8995 | -2.75564 | -46.10927 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e26554f1-f99d-349c-8dd3-ca52e0131377 | -1.88245 | -53.30032 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20037217-35e5-3cd5-951d-ed46cdba0a0f | -2.46454 | -46.53482 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 277af952-6b94-34d8-b156-ee26020cf1e2 | -2.44019 | -51.78642 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4ae324f-0147-3c86-9424-e295b270267a | -6.18975 | -43.41309 | 2024-12-03 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b4428e4a-a2f7-36e0-85a3-dcc6d325e58b | -4.15758 | -43.06453 | 2024-12-03 04:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dc14f4a-b623-36d9-a6b4-36e487bf6d3b | -3.64886 | -51.12383 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 703c8bbf-dd8c-36db-aab4-5d1409a23a6e | -3.69907 | -51.82677 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 65dba3fb-485d-3b1b-92d5-42553bbf22f4 | -4.19313 | -51.18637 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a3c53b18-1014-3cce-a206-294ea552f493 | -2.67088 | -46.281 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4480ca2-6f22-3897-a25d-2cfa44397642 | -4.31811 | -48.09473 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc449eb4-2ff8-38a5-a340-a7ca5c446a55 | -5.79512 | -46.47445 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84ff2eed-b0f1-3df5-a69a-7cbc0f794d2c | -3.99196 | -48.15814 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ad85d78-9d70-3731-a716-fac772a4f3bc | -4.01468 | -49.95741 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5c76d74-6985-38f3-9bb6-d80548268d7e | -3.41901 | -54.02505 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81b1caf4-6e6c-351b-a3f4-5ed7ac074944 | -3.21611 | -54.23818 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 866795a6-e9ee-3506-8f81-3ece2308fc56 | -4.16705 | -48.1925 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a0507abb-59a7-3fbd-966a-1ade15f031c8 | -4.05761 | -46.81566 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86b0ba19-770b-3a9c-9af3-104041c08662 | -3.12746 | -45.98763 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5665b62-3384-386b-9d45-d9c7d6e3fa76 | -2.57879 | -46.54206 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90eff64a-8b76-32b6-a003-c823702d3c3f | -2.58942 | -47.03691 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43ab3c69-9b9c-3543-8c36-09d4965b8436 | -2.45954 | -46.52346 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3b508a6-8e43-3e1b-a1e9-8983d010ad58 | -2.68119 | -46.60418 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53d6c841-e820-3de1-9eb7-b412e0ad0fbe | -3.09355 | -53.25534 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5951a2c-1a32-3e74-b0b7-233e1a07c811 | -4.03835 | -46.83034 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30d0ac6b-f28b-3ef7-991a-2054a0a22083 | -1.1762 | -53.42561 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 295f09db-2ca9-385c-9650-8d82668adfda | -2.7271 | -54.17513 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df83d204-e42c-36c0-9698-ee12e9d85e56 | -2.6283 | -46.27051 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a017d912-9371-3da7-b82b-ae11c2c396a0 | -2.63128 | -46.12177 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95baee71-b022-3561-871e-88bebdeaf82a | -4.04232 | -46.86981 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a085dbe-f852-3039-9b83-5276e024fc78 | -3.8612 | -50.89481 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72b5223f-1f72-325c-a92b-b7c3f93230ff | -2.30086 | -47.27339 | 2024-12-03 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54686b9a-5a82-322f-aeb5-76b4f74a3357 | -4.04196 | -46.93682 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e813d651-bc8f-3188-a672-e7e319af60bb | -2.61171 | -46.26796 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d4af072-abfb-38ee-bf88-2c203de75e27 | -1.73576 | -52.6354 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d301af24-cbb1-339a-9861-01f9cc614ff8 | -3.97055 | -46.65697 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d610f10e-12fe-3e98-9b51-0eea11e11284 | -2.15198 | -50.69487 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a2a5db4-da7d-3d1e-9333-326fc7b1d30c | -4.07714 | -46.69131 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2c35a4e-4824-3a31-a65d-3038813572c7 | -4.11634 | -48.53572 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9eeb59c-98c2-39cd-9da9-002e4799e57f | -5.81185 | -46.47709 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a5c49d3d-7908-3260-88d4-75eea222caef | -2.45271 | -53.81125 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9abaf51e-e381-37a3-93a8-7c9429b54f91 | -4.30471 | -48.24323 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf855841-13b0-34a7-bb98-ceb2c0f2099f | -3.28172 | -51.0693 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a1fe5ab2-72d2-3c3a-a23f-eb6c5bf5071e | -3.46771 | -51.64481 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73ddcb0f-24b8-34e1-90f2-5f4cefa6726a | -2.33099 | -53.8085 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f96707a-a9af-35f8-b6f6-5f6ea4dc5c0a | -2.80619 | -53.05277 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7061a0c3-b6b1-3a10-b666-3f903aaac00c | -3.02372 | -51.53344 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6262f740-5fe1-3bd1-9757-7fa8b5fa9acf | -4.43615 | -48.69592 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ac198c5-babc-31ac-8f95-6a0f340b0fb1 | -3.98485 | -46.63076 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a71c1e70-bf01-38ed-8cb8-caf023327d82 | -2.66763 | -46.12772 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8730d8b-3506-31dd-84b6-1dea0a3d065d | -3.94328 | -49.95065 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c729cc1c-e42b-32fe-b3bc-a29057296d0f | -3.94138 | -46.88578 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e0d6fe5-8b39-3638-8c96-10adaf32a4cb | -3.41356 | -53.22919 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4540e8f4-bf31-39dc-a83c-3ffba7344afb | -4.00174 | -46.93407 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47862a3e-ce47-3413-a643-7f2faef2b9e2 | -5.27673 | -47.79122 | 2024-12-03 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 380da1aa-4f9c-3187-8f3f-e7624445ee32 | -2.89693 | -51.79655 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5144179f-c65e-32af-bd90-9646a9c244cf | -5.69908 | -45.04891 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 152cdaf2-6516-3c69-91fc-5180d9cb7353 | -3.50232 | -50.05798 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ac039169-1ef7-3413-8d47-96ce6244e749 | -3.29385 | -53.6637 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| bd8a6df7-f88d-39ba-bcb3-9646a64e9143 | -2.6409 | -46.58031 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f9cf384-d884-3869-946e-eebc93b38563 | -1.92836 | -53.44609 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 950ef4aa-ab46-3321-8985-119486261c38 | -2.81919 | -53.05489 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 049a67a6-2576-3412-a3b2-a709bf13349a | -3.10045 | -54.01865 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 553a1abc-2e81-3b9d-9302-e93ddcf5db86 | -3.95513 | -48.82399 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6eb27fdf-72c9-3c6f-a821-ff427870452b | -3.83557 | -49.00396 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15984cf6-24b7-3ddc-bfd4-3a43a091452b | -2.9881 | -53.90063 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89834abd-22ae-34a1-a749-7ba5fd4e0d8e | -3.33543 | -53.20909 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 174cfc82-7396-3be6-9ca6-7c746a60c102 | -3.25431 | -53.652 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fecc91d4-06d8-371c-ba33-1be85609140e | -6.77545 | -46.27607 | 2024-12-03 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76091978-fb8f-3269-bcce-44fe507e6d35 | -3.96119 | -49.88435 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e95d7824-992b-33da-87de-741124a9fb2f | -3.02644 | -47.79891 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dc99d25-ef04-3fb6-95f3-c33158589b2d | -2.67957 | -46.6145 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e37c4531-0479-3aa6-a9f7-20f6660b46fe | -2.73103 | -46.24419 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b41d3938-677e-3703-bcdc-16c12556b008 | -3.0691 | -50.99282 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e61795c4-0430-3c21-832d-5b20c189e7bd | -4.1313 | -46.1279 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9153e108-b137-3b06-b448-9bb7e1c9322a | -2.98191 | -53.9097 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3686c5be-9326-31e6-b7c9-f26b2a3bbc75 | -2.83132 | -46.85978 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2658fd6-86d8-33c6-9460-ada997d82173 | -4.1197 | -48.53625 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20c6c3a7-eceb-3e03-a2f5-af6bb6a87f5a | -3.54053 | -51.49767 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b6e03de-63ad-3571-ad31-fd2f4cfc0343 | -2.62687 | -46.1282 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d02c05d3-8176-3cbe-b3e8-99881da2ef4c | -4.18559 | -51.1852 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 02d795bf-9e1c-3b62-8ccb-fc6e5b330c9c | -5.81464 | -46.48113 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 411d0d7c-6b70-325f-bc43-8e84e7378432 | -2.54576 | -53.40913 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d849c87-2c55-3f17-803f-c1d9e7b73cbe | -3.24825 | -53.63283 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e210732-5316-3b6e-8e45-97e9aecec3d2 | -2.30469 | -47.03428 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8ba796a-8769-3e0c-973c-27e3b47e1a44 | -3.28623 | -51.06533 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e53ed12b-d8e0-3aa4-83a4-0437ac1d2dc7 | -2.82909 | -46.85239 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4edf008-94ad-3cdf-84fc-34855bc32e74 | -3.65092 | -52.62561 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 206ba8f7-f674-3e7d-bce3-ae444a05567c | -3.84972 | -46.51722 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README37.md)
