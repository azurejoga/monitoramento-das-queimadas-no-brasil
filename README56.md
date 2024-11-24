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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1f2fbb3-c458-32fc-8c88-42f7d6a97416 | -0.98304 | -51.72068 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 401718f6-8d7b-3c37-a3a8-a2d0dca45f7a | -3.24926 | -53.28502 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b023e9b2-6f11-3037-998d-24290234acc2 | -2.74157 | -49.11938 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5ab68c32-5d57-352c-a504-9dd06cecf421 | -2.55045 | -54.05253 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 476dfb1e-b2aa-3ba4-8e3c-a0f2010dd317 | -1.13073 | -53.70473 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 633d9282-373b-36e3-8f78-645ef56f9d4e | -5.55095 | -45.33171 | 2024-11-24 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c646813c-057f-3cf6-ac5b-91a5f4033c36 | -2.06066 | -50.17403 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7636aa3-75f7-3124-9870-f676027444f8 | -2.37756 | -49.84775 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d548a2d-f15d-3cfd-9270-011e4d51920b | -2.44989 | -49.08631 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 82415e04-e581-332f-9fdb-a1c2b0432e22 | -2.50804 | -51.95637 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d9ec52e-fac8-30d4-8e8a-ebd443f39dbf | -3.29054 | -49.91042 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6554ed09-0f4e-3995-9db8-278412520780 | -2.44803 | -49.09837 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 31dd6f03-e6f4-375f-bd6c-30491605a723 | -2.22751 | -50.56767 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 097b559b-8363-37d9-83c9-0e429ded6763 | -4.10015 | -51.0766 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 819d0fd3-18ee-3044-a85b-545bca2d2a46 | -1.61873 | -55.13815 | 2024-11-24 04:53:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff897d7f-98cc-3498-9a54-093198f3807c | -2.93241 | -46.69582 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e276e1ee-fb17-3397-a501-e5df225c97eb | -1.52812 | -51.56345 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63340427-da78-3751-a378-1dcca06dc7f8 | -4.00456 | -54.33656 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 693f2979-39e3-32ae-938f-cdde7c1eacb8 | -2.7471 | -54.07426 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0b9129e-bab7-3a29-bcca-1bb263e72b50 | -4.11617 | -49.43841 | 2024-11-24 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0426a40c-8e4a-34b8-90ea-9a8aab517c92 | -2.17149 | -50.90587 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27a75de3-1b34-3399-aedf-e153f1c5ee60 | -3.03231 | -54.06849 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d727e94b-e284-3fb9-a301-fb07b746011e | -3.96113 | -51.11648 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| beb51a87-5faf-3e5a-a4b0-69765c9c7ba2 | -2.10198 | -50.1319 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22e42762-9e55-3ea0-864a-e9c62f43b839 | -3.71028 | -53.75125 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fd0ca21-c037-3a02-afc8-7ba6c6b3c069 | -3.83815 | -46.01469 | 2024-11-24 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcfa8671-28d9-39c3-86fd-f5c3db7bda4e | -3.23031 | -53.92537 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f6844dd-41ea-3b81-80e6-ca2080221e73 | -5.10538 | -43.14001 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a3c1c44-dcb7-36e9-987e-93950e214f6d | -2.37089 | -53.6548 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f81b74cf-8da8-3ff1-8f21-371a975aabd4 | -2.1608 | -50.49574 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33292e27-677c-310f-8dd9-a7e021410e9a | -2.62788 | -53.98394 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a1da0c6-078a-35fd-8ce5-cf59358933fa | -1.61743 | -53.30485 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d830a6f-f425-3242-b0e9-0ad36a7e6f1c | -1.77265 | -52.72086 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3bebb65-c72f-3fc1-a8a8-1bf32195d850 | -4.08983 | -46.10707 | 2024-11-24 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2603aac4-319a-3a33-a45e-faeedb8ae735 | -1.39676 | -54.49587 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76e34b58-b5c9-38f8-bbe9-094cdf330833 | -3.1768 | -57.04196 | 2024-11-24 04:53:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3fb5ba4-c8bd-3ac7-b887-d2f4e8e8aac6 | -2.56646 | -54.06264 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2c012eb-a7b9-3f83-b9da-aabdb08a3e52 | -2.14972 | -50.71538 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 228fa51c-6d30-33f4-910d-aec5cc9d35d2 | -1.32924 | -51.85919 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a296b70-fc86-3fd2-957a-463471c878bb | -4.53524 | -42.90197 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d765fbc7-ace3-330c-9c4e-adddd926f4cc | -4.76173 | -44.39594 | 2024-11-24 04:53:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 561c2d3c-14fb-35a9-952f-681c6216ff21 | -2.01681 | -51.17801 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dc2461b-c7d5-36d2-92b4-0c059dbfda7c | -3.30212 | -50.36134 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ac95ee6-b4d6-382d-b829-ded585f870f3 | -0.97091 | -51.71179 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f3a9f0c-ff40-3cac-9616-7264b567b1f0 | -3.2846 | -50.04075 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa218f7b-8ca7-3afc-bdb5-23d32e8d620e | -3.60692 | -47.50967 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0af79007-1b59-3fa9-b168-016ef9002ee8 | -1.61237 | -54.41603 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b3a21a62-0b71-3f82-b171-648ac9ba0582 | -0.25863 | -51.63562 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c62865a-5de5-3e99-9dac-fdff363c5b2c | -10.49881 | -51.74883 | 2024-11-24 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7300577f-73eb-38f0-9351-1b33dd004729 | -1.50355 | -51.17569 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8151a60c-1604-3b5c-8c58-96ea000aad7c | -2.2495 | -48.9999 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29c02b2f-9f34-3531-974e-99f8a564cc99 | -4.81562 | -49.83971 | 2024-11-24 04:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f4bebb8-88fe-3875-aa85-ab7a545fae89 | -2.70138 | -51.87022 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30cf34f9-1abc-3dce-ac6c-37324701f59a | -1.18598 | -51.97067 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 651efa87-45f2-3c1b-8180-773532c495a2 | -2.68889 | -46.27597 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a3baa4a-ae8c-3d34-bab3-e69908ba7a7c | -2.58137 | -49.21994 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58d74a78-74b3-3b91-afe7-b1b49763a71c | -2.37672 | -50.32959 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d951b86-70bd-3f15-b410-084fed93487c | -3.28691 | -53.83722 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 133a8011-c8e3-3bc0-b316-4455cdfea753 | -3.05833 | -53.21942 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15c6d364-b3a1-3fe4-8277-155bb071114f | -2.81187 | -54.01949 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5e11665-aa3f-3d7b-b343-17e663db8ba0 | -3.25036 | -53.27795 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1030e45-2cac-31ba-8914-70b95573437d | -3.52234 | -53.79162 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f562b5a-d3ea-3bf6-9742-3acca012c7eb | -0.80973 | -51.59167 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdf7856c-ab74-34f1-871d-545536a7f04c | -2.61791 | -46.20093 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62b915c8-4de0-3816-b4ec-1f58618f4af8 | -2.85135 | -53.99184 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f84b052-6c88-3b74-ada8-14e49e0a7a70 | -3.2888 | -53.685 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb06c17f-1a29-3783-977c-cc915dcae299 | -1.21821 | -53.68412 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 946fe176-070a-3e0c-ad16-001572608056 | -0.96126 | -51.64364 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b047dddd-2eae-3d73-8547-1a7626ef95c0 | -1.73275 | -52.73617 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6298f55-f1ee-3c1e-8cc6-83928038caaa | -3.51608 | -53.80924 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 73188c1a-ec75-3630-b277-458ec0a1a5e0 | -3.06168 | -53.21993 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c49e85cc-b3fe-3f2e-8196-422629f7805e | -3.19542 | -54.32749 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8ac9bd1-bf7a-3278-8d2c-186b07373b33 | -3.94413 | -45.99823 | 2024-11-24 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d423f5c5-8af5-3e9a-bd80-a77c4023a35f | -2.22923 | -46.10965 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 69ff6abc-8d43-36d0-8d18-0817590d9850 | -2.21642 | -48.85734 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c146592-62f8-3d9e-99a7-8a87529cbb9c | -1.31209 | -51.74772 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa0bfb8e-fcdf-30ed-9030-66751004d848 | -2.67237 | -46.15656 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abd552a7-5284-3c6f-9e41-4074bd07f7e6 | -0.94949 | -51.71903 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8a266cc-0252-31ef-8971-d02dd4733abc | -3.28517 | -53.84814 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f5405bf-9cb3-3f74-99db-0526c9ec922d | -2.46672 | -50.38426 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88ed20c7-6a65-398a-8a7a-f6c0db7708dd | -3.31101 | -50.02944 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 153a3b3c-2d45-3ec7-8162-bd8b05755c57 | -0.34517 | -51.55767 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8eb5b46d-a6e8-31b9-97ed-6005b77b6bff | -1.7701 | -53.61106 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d77600d-d55f-3eb9-997a-c974acad23ad | -1.23562 | -51.73948 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 237352a6-ed04-35c4-ac41-6fc3c9bd1ffb | -2.7348 | -54.12982 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab7343ec-a8f8-3aba-a17c-0f2240409af2 | -2.1998 | -49.55102 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bec83d04-da3f-3b97-bb6a-f7f89bb197cb | -3.01251 | -51.4463 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8dffd05e-2a31-3b2d-b8cf-acc6d3919b2e | -2.77262 | -48.64494 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62f80879-2de7-3e29-9a6e-e85725ba744d | -2.81907 | -52.85945 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c22c66a0-3b60-31a8-a5e2-04552ccdd142 | -2.22692 | -50.8533 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d57f514b-54a0-33db-8ba5-bfa00da087b4 | -4.51636 | -45.72588 | 2024-11-24 04:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e1c1854-e9b2-3779-a399-a0d194c857d6 | -3.22038 | -53.38205 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ac86846-888d-3f1a-8cb8-b5f292c19430 | -2.14986 | -50.91329 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87ea441e-b887-36c2-be27-190f33c150f8 | -2.14287 | -50.50029 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b5b777c-1d5e-38ae-bc23-fdd07e4fe3ef | -2.26614 | -50.7765 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c1df6f8-25fe-3e7b-a7d5-4c20c53e0598 | -3.47138 | -50.01075 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d81cccd4-e9d4-3e6e-be9d-38937cf0292c | -6.35337 | -47.30443 | 2024-11-24 04:53:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac1030f5-80d4-3bc6-8279-2941d4c79d2e | -2.28266 | -53.63406 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94111004-0761-3a7e-aa61-0d02963ec65c | -2.26388 | -46.87025 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd103686-fd08-3d3e-8550-ec17ff99aa5a | -2.15684 | -50.4549 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README57.md)
