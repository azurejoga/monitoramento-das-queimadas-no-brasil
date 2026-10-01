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
| ce048916-a9bf-319e-a916-1abb69af9977 | -5.82191 | -47.80627 | 2026-10-01 04:32:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77e8c730-90da-3db5-bfaa-fb1c9b2c4eb0 | -3.57089 | -54.3229 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5942fe61-684b-3f02-bfc7-607760ba261a | -5.43934 | -43.74054 | 2026-10-01 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05cda217-8746-3d6f-bf67-483082b3dc90 | -6.73856 | -44.14056 | 2026-10-01 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28a608c5-2d85-3714-a4c5-bbc461a140f9 | -3.29551 | -53.85543 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| acd0c400-8a12-31a1-8e2b-c71307fca5db | -3.9592 | -49.05621 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 922dc424-0c6e-3d4d-8685-4f658d26cf2c | -3.28868 | -53.86591 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| a82c0fbd-7179-3e06-894c-b41259cf64a6 | -4.29896 | -50.77686 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 374b8b8c-7e5c-37a4-89ba-ee1de957c969 | -4.05691 | -51.10511 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 308ada71-7681-3127-8d03-b99d1b2fad15 | -5.18475 | -48.2599 | 2026-10-01 04:32:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ee393fb-edc3-3f15-b724-4a1b7af53cb9 | -2.29929 | -48.75668 | 2026-10-01 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15b4a3d6-6426-3f50-9735-9717054d4625 | -5.11039 | -56.0103 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5d8f652-1864-3af4-b590-5a7dd0fa31fd | -4.6304 | -50.62082 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7fcfcf61-c5d3-369e-8afa-c0f28f852619 | -5.60345 | -46.25323 | 2026-10-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4013bfe-f5ff-369e-b0da-81c2f994dd51 | -4.26635 | -50.77682 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 584a8a9e-0e1f-3664-8581-54d558527f0b | -5.17815 | -46.19293 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 999506ed-46a4-39c3-8602-88acacf92eb4 | -5.14334 | -47.60299 | 2026-10-01 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df4bf788-4edc-3b41-9b93-c39a7ce7d495 | -4.06041 | -51.10926 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2c3b853-62d3-3896-9ef1-37d7ca0685a6 | -3.28464 | -53.85944 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 14151b6e-b010-37c8-83fa-1413a8260717 | -5.11865 | -56.01941 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa22d1a8-4fa6-32d2-95bd-744452b3577d | -3.35683 | -50.46972 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5eff0140-39e4-3b8f-97b4-93bc8e77e48c | -3.00855 | -53.88338 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cb093eb-04c1-3e8b-900c-c82349522794 | -3.16744 | -54.09697 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 745303a5-f6ad-3371-9614-f8de85fa7a63 | -4.14485 | -48.91106 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 243e762f-53ec-3c77-b079-3341333eec87 | -3.26735 | -50.70337 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c564fbe-fe7a-3a8f-9e3b-46db2cf47f5f | -2.97407 | -51.04715 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77114915-fe56-378b-b30f-d676b9de5110 | -3.30004 | -45.93088 | 2026-10-01 04:32:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ad79aa6-5f4f-38bb-b355-bff748505860 | -4.29129 | -50.74941 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bd771792-1001-3a6b-80fa-fba912ddbf85 | -3.97871 | -51.92007 | 2026-10-01 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e5d411c-905e-3518-b575-249f786a7993 | -5.64123 | -43.72204 | 2026-10-01 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9410ebee-8e4f-382f-9251-62dd901e4ca0 | -2.97819 | -51.04782 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7d674591-19ef-3f24-b91c-d948a8ec02ad | -0.44362 | -52.01158 | 2026-10-01 04:32:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1b75831-fd15-3f1d-a8cc-e9e22c232ffc | -2.90526 | -51.31121 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30b3a9ec-d6af-361f-9d0c-09daa9fc9a36 | -5.44284 | -43.7411 | 2026-10-01 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58ac92ca-7a7e-3608-94ac-71d6056fb73a | -3.60821 | -48.91488 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b627d119-e25e-3d54-b6e0-51543148ef7e | -4.31399 | -50.78461 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c6d1ba67-46ed-391d-ba64-a90ca16aa7e6 | -4.24775 | -50.75105 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 71fc64c8-712f-3000-bfae-2ae370654dc5 | -4.62893 | -50.60557 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e6c54f33-e277-3e12-90a4-d5b5a318bfde | -2.90946 | -51.31191 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13ba84ee-f6e8-33b7-80ef-605445dbe764 | -3.01854 | -53.88508 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3d4e79e-65e6-31e4-889b-9dcc78e62634 | -2.97886 | -51.01765 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af1bc3cb-4010-3e87-a191-42772727c435 | -6.0103 | -49.55572 | 2026-10-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 48b88d74-1cbf-342d-87c6-70dc8d55e8c1 | -2.27326 | -48.7568 | 2026-10-01 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e06ada14-5e23-3100-98e8-ee877f8272e7 | -3.17264 | -54.10522 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2d3cffab-1fc0-38d3-87e8-fa53f121f353 | -3.10519 | -50.2639 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf65eb07-4049-36da-a1e8-cdcfd07fc42b | -3.1649 | -54.08887 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 642f471c-1a8e-3d3f-8c2a-3ba73e0a61c8 | -4.25635 | -50.7735 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0029e554-85db-31aa-9a29-227dffc37e41 | -3.29343 | -45.92984 | 2026-10-01 04:32:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fa364cb-881a-3872-bd42-5def914b9d09 | -6.19508 | -44.85753 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdfc228d-4085-3c0b-805b-1822c5dd7d31 | -4.04432 | -54.23069 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9f48019-4408-3786-8503-c2f4ca5b4d48 | -4.30064 | -50.76672 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4ac69f2c-d9ee-374b-9649-66ac0858c688 | -4.85663 | -45.84184 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0995896b-0105-3c41-ad10-6719221e81a6 | -3.10438 | -50.26887 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45470964-134c-337d-acab-12a0c6fd237f | -4.15176 | -48.89131 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0877fb36-acc5-3a43-a463-c00ab1c9a22a | -2.72054 | -49.78804 | 2026-10-01 04:32:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21d8f589-fa3b-326b-95fc-6c0445b43e9d | -4.26185 | -50.79003 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c84ada5-17eb-34d3-a3fd-570b77347488 | -2.9059 | -51.30736 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6e5f3ff-fe2f-3780-8bad-9de5571208b8 | -4.26774 | -50.79285 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 34152775-1157-356e-b255-b6e85ddf3154 | -5.74721 | -45.16648 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 36576071-6d17-3c91-aa8b-2cf376ea8d60 | -1.46488 | -48.91922 | 2026-10-01 04:32:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5922ce2f-efd8-3d69-ab9a-1b7a3da6c394 | -4.25868 | -50.78434 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8026a627-83f8-3cfa-a7c1-b5c1741b1f44 | -6.01683 | -49.56112 | 2026-10-01 04:32:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9da00469-b603-3782-aeaa-89307cccfdf8 | -4.26266 | -50.78499 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 257c1f7f-e48c-37c2-a978-03c85e96c96b | -4.26663 | -50.78568 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 9b330aa8-de2e-3b2b-8bd5-251478817ce1 | -2.22056 | -46.07465 | 2026-10-01 04:32:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78948645-ca72-3688-93af-09361e54fced | -1.63262 | -55.12808 | 2026-10-01 04:32:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8acbd5f-1f0e-364d-88c7-72417d9888f7 | -4.26355 | -50.74495 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e8039db9-f66c-354e-a4b6-2b27c7e1c20e | -5.75891 | -45.15741 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4efd841-c63d-318e-89c9-d71d079de36f | -4.2777 | -50.7577 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| c1ddcedc-0097-338b-9d08-8429e0239551 | -5.42957 | -43.45346 | 2026-10-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e46e04b8-80cc-376f-b808-fc7846e5cd6e | -2.98941 | -51.03071 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| abb2019e-3caa-3310-9d12-cf449717e3c5 | -3.87232 | -50.43922 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9943e205-c8aa-31d2-b969-8df230a7acaa | -3.09958 | -50.29855 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0a3cce51-34ad-3955-935f-ba49a92533ae | -4.30833 | -50.79419 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9b37a63-f9b5-363e-bde3-a6e655032366 | -3.24976 | -50.81244 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35bb1548-bc3d-36d7-98de-0bb23284f93c | -4.26859 | -50.78777 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9913189c-ff2d-3ddb-a76f-c6ef4544c318 | -2.90883 | -51.31575 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f30dfbe9-5f01-3109-9492-66b2d7f4e69c | -6.17449 | -44.91416 | 2026-10-01 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fb9e049-1de2-3656-bdf2-b7ca165144eb | -4.26977 | -50.7564 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 0bfd6a0e-6f02-3f3e-b1aa-34e13db86897 | -3.57104 | -51.47858 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b031558f-a9b6-3b49-98d2-1c0addde2f86 | -3.38082 | -50.95506 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 707ab0ea-064e-3812-9bdf-fcd790cb8dff | -3.00903 | -53.88053 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 742450d3-d0fd-3e34-8d7c-73308762b8b6 | -5.10147 | -45.66752 | 2026-10-01 04:32:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95b40432-6882-3098-886f-7f79323fa69e | -5.93677 | -51.79788 | 2026-10-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47025bbf-4276-3677-ae56-95da06615aef | -3.08874 | -50.26632 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbf94143-ef85-39ff-be60-8f43121faa33 | -4.26363 | -50.75354 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e80c75e9-b19e-385f-bb51-933602d1885d | -4.3117 | -50.77375 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e52580d8-1b98-3902-a11e-7973cc6b51de | -3.16079 | -54.08223 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 64c73c1c-a1ae-3c38-bd14-49779874c756 | -4.30377 | -50.77243 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ed1328f0-0d83-3bf8-bbe8-c17f57fda920 | -3.12083 | -50.26644 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59ed98df-960b-37de-85ef-a7b61d3b7aef | -5.12553 | -56.01299 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 460d13e9-cfd4-3f0b-a2f4-1bd739cc3931 | -2.98411 | -51.03738 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c24ce8e1-592e-3148-8d6a-36b41c13621a | -4.30436 | -50.79355 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20e19aa7-9ccb-38e5-982c-3a792e0edac5 | -3.22491 | -54.31704 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb5d5375-e797-3725-94c6-b77c144e4cca | -3.27136 | -50.704 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8591c667-9d65-3e41-ba4a-d90625fefc7f | -4.26066 | -50.78639 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9291fff1-ae35-3572-af93-024de2b1a0ef | -3.68333 | -45.41953 | 2026-10-01 04:32:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b25d913-7c4a-343e-99ec-8c12453cd67c | -3.06938 | -54.38155 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6b2adcc-697c-3c4b-8e0f-c881bc201efd | -6.70896 | -45.98509 | 2026-10-01 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb96bcd3-da77-3b25-a059-8332f68ae39b | -4.29017 | -50.78068 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |


[Clique aqui para ver as próximas entradas](README47.md)
