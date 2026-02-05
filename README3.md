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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e495d46c-e090-3f25-b0f8-f2a9f6af8d84 | 4.34236 | -60.94199 | 2026-02-05 04:38:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9a8b58cb-99e5-3f62-b29c-cd5e5e89dfc4 | -7.34891 | -47.01313 | 2026-02-05 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a7066e3-aa8b-36f7-b27b-ed0c2f927afa | -8.06861 | -47.11474 | 2026-02-05 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70a0ca9a-1239-3d9e-9871-3c256d329d64 | -5.90548 | -43.84301 | 2026-02-05 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bba6df8-14f9-3012-9a81-cb95886ae9e6 | -4.0065 | -50.32471 | 2026-02-05 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96bb4489-da96-36f6-8087-aa0e56b44bfb | -8.06506 | -47.11424 | 2026-02-05 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eccc0765-ff7a-371c-b19d-f106a11a2536 | -3.26675 | -47.07919 | 2026-02-05 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58813e1b-0fed-347f-83a2-bfcac28b5d09 | -2.9883 | -49.27166 | 2026-02-05 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7a92892-6569-3ad2-9f28-c263f5adc149 | -5.97646 | -43.5622 | 2026-02-05 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6838115a-86cb-3a09-8d37-043885e3d617 | -5.97764 | -43.56016 | 2026-02-05 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c79c3908-d6f9-301e-b776-7157ef869137 | -6.99544 | -50.47553 | 2026-02-05 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff2abe8f-f847-373f-b4d4-174332a0d4aa | -3.42806 | -49.2247 | 2026-02-05 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a102e92-862e-302f-ae95-d8bee1ddb27c | -4.00371 | -50.32066 | 2026-02-05 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba1f7dff-5cda-3ea1-afde-b01a2ffe61df | -4.00315 | -50.32419 | 2026-02-05 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08622462-226a-3fdc-8616-adc4cd13b9dd | -9.70767 | -47.69984 | 2026-02-05 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 80c83289-e9f6-3f0c-824c-1c346e64b0aa | -5.96414 | -43.53342 | 2026-02-05 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b02c3b2-75c3-3638-aa30-cdecf83decfb | -5.87821 | -50.15829 | 2026-02-05 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b953a33f-b495-3b71-b91b-6a089632fdee | -2.70052 | -48.98003 | 2026-02-05 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f773afef-396c-3188-940b-fb75c93cc90b | -2.985 | -49.27115 | 2026-02-05 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d29f306a-b993-3945-a2d4-33a690b9b4e7 | -6.54865 | -44.4521 | 2026-02-05 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23d8dd5f-9ab7-3fd1-8f14-158320e39d6a | -8.06801 | -47.11886 | 2026-02-05 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a812fcf-11a2-3f8a-b85f-bf9b0d8691a4 | -5.8749 | -50.1578 | 2026-02-05 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c54f9e3-b669-3e08-b14d-22239bad950a | -4.82197 | -42.36343 | 2026-02-05 04:40:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 751a4375-2ab5-3992-8d4a-5f1918a9845b | -5.9049 | -43.84692 | 2026-02-05 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cb814c9-b2ed-3b92-bde3-b366e500566d | -5.27909 | -49.87821 | 2026-02-05 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee01d06a-83bf-3a8e-8042-7eccbe81b8e6 | -9.70884 | -47.69868 | 2026-02-05 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 922492c6-da56-386b-965c-07dedb65259c | -3.26392 | -47.07503 | 2026-02-05 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da6b4651-a23c-3671-8e8b-344f70f27ac5 | -3.27521 | -50.98898 | 2026-02-05 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 707c068a-dc61-3f25-b619-3e80411ac9a0 | -5.40075 | -46.41254 | 2026-02-05 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 648e6ba0-b3f8-3760-8fcb-aa495f658fc1 | -3.91747 | -43.52461 | 2026-02-05 04:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6cb6e9e-9e4e-391a-a40c-18e3a812a360 | -4.26043 | -48.8429 | 2026-02-05 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41b2b7c8-88fd-3095-aca1-e6d17a43828a | -6.57249 | -47.90531 | 2026-02-05 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4870d4ed-2c9a-38d3-8a81-71961b6a0cf8 | -7.23657 | -47.37025 | 2026-02-05 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cc44f82-7ee2-31d2-9c3f-f70b9dd4680c | -4.59331 | -48.95508 | 2026-02-05 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb405735-9f68-3143-9aed-aabdff29eefe | -15.18482 | -39.43108 | 2026-02-05 04:42:00 | NOAA-21 | ARATACA | BAHIA | Brasil | 2902252 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| addf301a-0715-356f-991d-7974116dcdf2 | -15.42458 | -41.43228 | 2026-02-05 04:42:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fa19e577-4d8f-36b5-af37-8ff1aa95b318 | -15.425 | -41.42849 | 2026-02-05 04:42:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 02cfa500-050e-335e-a6a7-abf5f1223bd9 | -14.06341 | -39.49663 | 2026-02-05 04:42:00 | NOAA-21 | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e47dce6f-d135-374e-adbd-a8569dfd25ad | -10.79467 | -48.22916 | 2026-02-05 04:42:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 737ca6f5-d8ce-33f9-9f9d-d7d135526e01 | -10.94584 | -45.13719 | 2026-02-05 04:42:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0392d1d8-2287-3be8-bbfc-06602b1b3cc8 | -10.93094 | -45.16356 | 2026-02-05 04:42:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3a3b8324-302f-38f9-a6ad-9ca0b3ec6d66 | -18.74999 | -51.53997 | 2026-02-05 04:44:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a680bac-80f0-3290-8550-f1b0083b5a0b | -20.26077 | -50.65714 | 2026-02-05 04:44:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f338cc17-0c68-39c6-bc88-e5d62e7cd2ed | -20.84252 | -51.73854 | 2026-02-05 04:44:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d4eb3775-f242-3013-8fd3-9abdae66e033 | -16.22465 | -59.52835 | 2026-02-05 04:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdc8c498-6fdc-3abd-81c8-9be2abe2888c | -23.27152 | -51.20774 | 2026-02-05 04:44:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 08d79515-99b7-340b-837a-03f85ffa23d9 | -29.18583 | -54.91297 | 2026-02-05 04:46:00 | NOAA-21 | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 63bd0272-4af5-31f9-be92-070bfc5fd28c | -27.6882 | -48.75187 | 2026-02-05 04:46:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 791f4fbd-6de2-3c53-8b42-adda92658c81 | -29.92756 | -56.18141 | 2026-02-05 04:46:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 7c571ad4-4e9e-3896-8ef4-15d058c57650 | -30.48182 | -56.37466 | 2026-02-05 04:46:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 143bcf32-2efa-34d1-9985-3f1ccab01e97 | 4.38578 | -60.59211 | 2026-02-05 05:08:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ad3c40e-65ce-3234-846f-40bc553e7fa9 | 4.33558 | -60.94935 | 2026-02-05 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 338c8e70-1638-3263-ac13-f13c92381b3f | 3.42595 | -60.74184 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 756e78b4-6da6-3dc8-b15f-c44b77e36cb0 | 3.42986 | -60.7363 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03e0c61d-1b09-3b84-98cf-305289f784c3 | 3.42873 | -60.74314 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d96b9b6-39e9-3d4d-b602-b6c2fe59b3e7 | 3.43126 | -60.72791 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95b4d8dd-e152-3698-be7c-a748d48ba421 | 4.40084 | -60.62984 | 2026-02-05 05:08:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4214355b-5f22-3230-8aa4-2683c0da6b2c | 3.42336 | -60.73897 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b66c0ee8-d6d6-3bb3-a475-9a0cddec0641 | 4.38654 | -60.59735 | 2026-02-05 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a7307ef-affa-39fa-83c0-cfa8cab3fd45 | 3.30963 | -60.90066 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8965b29-c642-376c-8ca7-1bbb3ab44574 | 3.42802 | -60.73829 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e0e0e78a-b44b-3c0d-a0fe-d1fecf0d1534 | 4.34431 | -60.94202 | 2026-02-05 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eee51f3e-35e9-33e7-886c-54068c6ecba8 | 4.34031 | -60.94817 | 2026-02-05 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7561079e-ee1d-3b5a-92c8-9c72bc0983a2 | 4.23029 | -59.8259 | 2026-02-05 05:08:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ecbd94d-df20-3fb8-b88f-1b954061ec3a | 3.42838 | -60.72667 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20bf7b6b-547c-3f99-8f98-7d2ef9339206 | 4.23534 | -59.82934 | 2026-02-05 05:08:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53197518-f943-39a6-b7d7-f21a6851bb80 | 3.30888 | -60.89573 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e6c5532-1e32-3cb5-b712-90c97045377f | 3.42732 | -60.73346 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3911eca-3768-3bb4-8da0-2641896eef63 | 3.4252 | -60.73699 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f5c03ab-89f2-3db8-b08b-884ecf83cb06 | 3.30813 | -60.8908 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cecf01f8-3abf-3628-a495-280b4a7cc310 | 3.43061 | -60.74114 | 2026-02-05 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 246f93eb-bead-3608-994e-e32203c71227 | -3.60101 | -49.44273 | 2026-02-05 05:10:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 179c4c50-7459-323d-8a8d-25a0c5420589 | -2.89599 | -54.20018 | 2026-02-05 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1403a8c9-5f76-3887-93fa-501776048d03 | -4.36982 | -55.77169 | 2026-02-05 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c69e974-e0d2-3bae-b370-772a67344c78 | -4.00748 | -50.32348 | 2026-02-05 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03c22ce7-46a8-3f59-9983-9539468849e2 | -4.40754 | -55.00076 | 2026-02-05 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf0605fc-8e77-38a0-9544-377007526a01 | -5.88108 | -50.15696 | 2026-02-05 05:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f5dfbb9-2f00-392c-8fd2-96c66a050ba4 | -5.87692 | -50.15597 | 2026-02-05 05:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2dbd838-90b7-3a50-bc62-8cf9570456bf | -4.00343 | -50.32283 | 2026-02-05 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc8273d0-a6e3-3e97-8c8e-a8cb7814dcd8 | -2.9879 | -54.21797 | 2026-02-05 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdfe23ac-c308-328b-9c5a-74a274d6abba | -6.77673 | -55.48686 | 2026-02-05 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ff28c2d-580d-35bc-b2ac-cb61ddd0138a | -2.56779 | -54.74407 | 2026-02-05 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e238be2-0b59-37fd-98fc-7e8a2e8d83cc | -2.98589 | -54.21769 | 2026-02-05 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d0164e2-0f36-3648-a49f-8d9084dc07ac | -3.44804 | -54.08703 | 2026-02-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4d6e082-5b9f-3ef5-8ebd-cf0e13f9f655 | -5.88061 | -50.15645 | 2026-02-05 05:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6b40af1-86f9-3688-9564-844bb867db92 | -5.87643 | -50.1555 | 2026-02-05 05:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84a778c9-ba5b-3f28-a563-e8aab1b50c9f | -14.30005 | -59.76707 | 2026-02-05 05:12:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91d63c5d-2129-3235-ab55-af7bebc87db2 | -9.11726 | -62.55043 | 2026-02-05 05:12:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90414e0f-266d-3d4b-99e6-8633358f8bb3 | -29.92682 | -56.17929 | 2026-02-05 05:16:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| c0ee3307-b0b5-3a17-b779-9a3c4ecc2190 | 4.3548 | -60.93385 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83f24a0e-5f00-3037-83a5-e94253bc589d | 4.23274 | -59.83207 | 2026-02-05 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb165ca6-c8fa-3e61-804e-b1c92ea6aed1 | 2.48107 | -60.72466 | 2026-02-05 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3ef1bc0-1918-3b00-b937-146c4dc0e41c | 2.18521 | -61.08982 | 2026-02-05 05:29:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcce9338-96d6-34d1-8839-5870a2cd695a | 3.74229 | -60.64374 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 595bdcd0-2cbc-3624-b4b8-0ff6bd78ee5f | 3.761 | -60.69767 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5552e61e-1b00-38bd-b086-4847183fe81d | 3.5097 | -60.89338 | 2026-02-05 05:29:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc3c78f7-2965-3900-b18e-af3ef2c3e3db | 3.84034 | -60.33781 | 2026-02-05 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 309a45c9-5d85-3787-b62c-f5b62d84e48f | 3.30921 | -60.89277 | 2026-02-05 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27902d4c-0eaf-33d1-8a21-b28f679a362a | 3.82223 | -60.74117 | 2026-02-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c5d0de3-9d34-3fc3-a8d3-c3f71895c3cd | 4.20803 | -60.4072 | 2026-02-05 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README4.md)
