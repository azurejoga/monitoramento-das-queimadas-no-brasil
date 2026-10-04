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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c77857b-835f-36ae-9929-78691684d54f | -2.96548 | -54.0787 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc1e3e41-60a3-3fec-9f76-e78184df27f3 | -3.04541 | -54.21526 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 14fa92fd-3f77-3ca6-a7af-442374a9b989 | -3.17927 | -54.07741 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71bcdfbf-711c-3a67-b416-cbcf4c11b849 | -2.88392 | -54.13872 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35609586-5a0a-3910-99ea-760cfba48470 | -3.13491 | -53.74104 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7f7eeac-e6ec-383d-8ccf-ccecc9c8b15c | -2.74421 | -54.59005 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a11ffcc-0645-3d81-b2a9-d3d7bbd2f4bd | -3.47315 | -50.09997 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 97b1af7d-6029-3306-9a84-f13958d2bf76 | -3.50829 | -54.61048 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a27b74ae-000c-385c-8398-801534195c55 | -2.7984 | -54.107 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c474d18-ab36-38dd-afbf-83ab137fadcb | -3.50889 | -54.60665 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 980bfe39-4270-36d6-8bc6-281da8d3c5f5 | -1.49974 | -49.45408 | 2026-10-04 05:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ba162f6-5f65-322f-a3f3-8cd7ac3f7d73 | -3.85031 | -55.80428 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75ea15b4-751f-3bc7-af3f-34a1dfa5604d | -2.92719 | -54.16145 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9042f4ca-8ddc-3993-991c-654b99bc1418 | -2.92462 | -53.94612 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d9185d9-d720-3a41-8f41-c260a157a873 | -4.2804 | -50.28199 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d2a62f32-a4f9-3e23-874b-9cac29f9d28f | -3.18863 | -54.08695 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0d03bb6-59c0-3d20-ac60-c583723c8d6b | -3.0129 | -53.88905 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5152e3e2-aa8e-3195-9c61-5562da16814d | -3.46931 | -50.09471 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ca743ac3-be5b-3fe2-86f8-d9dbf873a0c1 | -4.06142 | -54.31445 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 9d4d3b19-0b93-3cd8-9474-2aea5e03d7be | -3.76477 | -55.54659 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02e725c2-8b3a-3a79-b30b-5ebf722ebcbc | -1.05588 | -53.58603 | 2026-10-04 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46f2254d-3fe0-3215-94d9-8b80bda627d7 | -3.04645 | -54.23143 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 227d184c-4c7a-34ab-8acf-6fb044062bea | -2.82999 | -50.4729 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72150451-4238-3a69-92cb-85bc4074aace | -5.37644 | -56.05807 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93143c5f-2133-3ed1-9f43-bd2d04af9fe7 | -4.54657 | -55.97358 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5f36580-3336-36a2-b0e3-702d9f805add | -2.81141 | -54.09291 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9943fd9e-e28c-3120-9090-efb9b6550ce9 | -2.81952 | -54.11025 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 82bd6499-b3d5-3eff-b153-7c6d653998a1 | -5.78067 | -50.20881 | 2026-10-04 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c7bbb6b-f637-349c-b7e5-67a98278bc7b | -2.92234 | -54.10035 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a221c55c-65c4-3016-b43c-64e49a66fbc4 | -5.63831 | -51.75834 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbd23607-e062-3b91-a3ea-d04bb2a54623 | -2.53328 | -57.55611 | 2026-10-04 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dbc7c90-a845-381d-a807-8c86405d2fe4 | -4.42655 | -55.74756 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31d04fe8-d7c2-3b28-aff9-567dd34d2762 | -4.20331 | -53.46439 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b56efb43-cafd-322b-99d3-71955e85a5e4 | -5.5521 | -45.26203 | 2026-10-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6d2da5a-2f9f-3347-b7dc-21d4912251b9 | -3.1751 | -54.0809 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e984c232-9b07-3507-9be9-059a11be72bc | -2.80789 | -54.09236 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5426d2fe-6ce7-3b40-9a54-400caf660265 | -2.79901 | -54.10307 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb11388e-c8a5-3a66-b00a-b8d9128145dd | -2.57882 | -50.00024 | 2026-10-04 05:16:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 890deda6-0b83-3b98-b594-24b243106727 | -4.19961 | -53.46384 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f8ed0dc-c17e-30e1-8c9e-b9dbada13f87 | -3.81274 | -50.84771 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d27b9dde-46ca-3373-bd7d-5054c5e66cea | -3.84364 | -55.84673 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 55d8c43d-376c-3e81-8080-4bf856e126de | -4.26787 | -46.36752 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1eed5a6f-b9da-3306-97c4-90490e2c5c49 | -2.11068 | -48.99823 | 2026-10-04 05:16:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be55252a-1393-3708-a713-5c4725a874e0 | -1.90984 | -47.01893 | 2026-10-04 05:16:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e35c84df-c280-3d74-a29c-900a90057af2 | -3.11988 | -53.74295 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc7e6ab4-d40f-39b7-9c6b-d3b4a11ecb55 | -3.07915 | -49.54886 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fd474e39-4046-33f6-8dc8-dba747bbacba | -3.73835 | -53.42267 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20dcb866-f7ce-3781-84ef-24e38da22b1c | -2.8117 | -54.13714 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19db152b-a4a4-3ee0-92e1-719ef24f5509 | -2.79488 | -54.10645 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 612f1fcb-f14b-3c69-9a23-69013319fb2f | -3.77006 | -51.85712 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd1cac3d-5c36-3eba-b7a2-e8194fbf64bb | -2.95159 | -54.12091 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07b52c0e-0eee-389e-a3d3-06abb868860a | -3.93958 | -55.83986 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf0733f4-4a47-3e69-9106-daf20e1ebd73 | -3.13126 | -53.75182 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60c53a3e-a834-35cc-96a7-b25847415f29 | -5.6301 | -50.0307 | 2026-10-04 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58f0501c-1ab4-3a9c-9531-101bf2eabb92 | -2.80299 | -54.12379 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 658cf75b-9526-3b1e-9d54-ee75b02cd3ce | -3.31972 | -54.17435 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e92b849b-14ac-35a9-8e0c-8b6cade1e49b | -2.80192 | -54.10754 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0cd3f6a-7bfb-3222-9d6b-d793d8a2744c | -3.18573 | -54.08242 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61f22954-cdf9-3ea4-80a2-f1274f146bf7 | -3.46982 | -50.09597 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f9a85c43-52bf-358f-8209-54c6aeb570bb | -3.4777 | -50.10063 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df051a0a-acaf-32f8-a070-f28b6b63f808 | -5.84099 | -53.82329 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d881341-e50a-3790-99ed-36ff1dee4690 | -3.46478 | -50.09394 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73973fd8-89ae-3133-8c54-865520de3880 | -3.19041 | -54.09882 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7df8156d-3727-3b87-9513-938f2ac7c038 | -3.84595 | -55.96251 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1410604-5b22-3fdf-9eba-a0959370934d | -3.11399 | -53.73362 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 4b19eb09-412d-3ce5-8520-bf3cd9e24753 | -6.7068 | -45.97213 | 2026-10-04 05:16:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 452b10ae-f19c-32f1-9122-36bab3a90437 | -4.44408 | -54.96729 | 2026-10-04 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17ca9223-f5b6-3c97-b4a8-e7bf82503029 | -2.89095 | -54.13979 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0c51eb9-2d86-3d63-8dfc-e6cef6ed8d78 | -3.14033 | -53.74059 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c107b7e4-49e3-3d6c-a5b9-02a9bb039fc2 | -0.36018 | -52.00147 | 2026-10-04 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ed9bc67-8926-3489-a3b2-557d4a88c92d | -4.43692 | -55.23623 | 2026-10-04 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 035feff2-2f6b-3cd6-a816-52b310679a4d | -4.2916 | -50.26944 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f7ddb85a-f074-3332-b1c2-fe40a30c4fe0 | -3.12247 | -53.72651 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c26a33c9-9f73-354e-b6a0-6d9ec3a7fd6a | -4.81549 | -49.2854 | 2026-10-04 05:16:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4af7e192-064b-32af-89c1-b3ab4a1e144f | -2.83375 | -50.47767 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c60e2e3e-d090-35fb-be81-662774affde2 | -2.25535 | -51.93718 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6894057c-087a-38f9-a152-a6caeae079b5 | -4.09614 | -54.32378 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4044411b-65bd-340d-bedd-905095b113b7 | -2.5772 | -51.87572 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d67fb1b0-0454-3ccf-b65b-87ce64f35828 | -2.64558 | -57.98539 | 2026-10-04 05:16:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8a74ff3-0534-345a-a601-a3ecce6c3821 | 1.80158 | -55.55926 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbcee581-64ab-3064-b980-ae730369713a | -3.13032 | -53.7235 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3ac25a46-3b8e-3431-9993-72c7103b51d2 | -3.10975 | -53.73719 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 63112ba5-9fe5-3e72-8938-11138159d55e | -2.48633 | -56.09639 | 2026-10-04 05:16:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86599a12-9479-3d7f-bc16-f0e7b2822e6a | -2.91591 | -54.09531 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4871a293-6790-3456-9159-a94b337a7e15 | -5.63127 | -50.03149 | 2026-10-04 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ff7f155-b070-3409-b8ce-e50715cd87c9 | -3.11528 | -53.7254 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| ced918a0-440e-3d7b-bdea-4c2502a46a40 | -2.52663 | -57.55867 | 2026-10-04 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81a8fa88-9658-36a7-9df3-5b2fbdadf27a | -2.81002 | -54.12487 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82b3c18c-904b-36bc-8aec-6b9e2c8117ef | -3.08537 | -49.53958 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38385c23-18bb-3f79-a01b-02f2dad8f168 | -3.47739 | -55.43317 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62db9398-4c4f-3b76-8c5a-f225aaba5c7e | -3.00344 | -53.87931 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e8e355e-e079-36b8-89ed-cd846e601c9a | -3.16855 | -48.58815 | 2026-10-04 05:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9536774b-a3cf-3211-a6e3-4c59a2af83cc | -3.69967 | -54.19794 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c01d319a-186a-3682-a6d0-f4662b883433 | -3.18218 | -54.08191 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21088add-6409-37e6-b479-37877c316a58 | -1.09897 | -54.11285 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 032561ee-0801-3d83-b62a-a1c48282187a | -3.76266 | -49.55974 | 2026-10-04 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 5a30ac00-937e-3a45-80ca-4ff425306756 | -3.11794 | -53.75527 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1db00393-1fb0-3894-83c0-5c10533a5efc | -2.81125 | -54.11703 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 269ae0b3-cd7a-32cc-a6a7-5b3c78c1711f | -3.57445 | -54.65548 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df047432-5298-359a-9162-a81d93439ff0 | -2.75213 | -51.54717 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README60.md)
