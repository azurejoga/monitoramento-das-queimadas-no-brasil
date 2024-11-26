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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1599418b-54db-3b94-b0ce-529acaf4e0ad | 2.6718 | -60.4304 | 2024-11-26 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 2f0bf57f-bbaf-3091-8b37-3864cd3088d0 | -2.8014 | -53.0227 | 2024-11-26 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 98bb96f6-4542-362b-a4f4-587c0f6ce817 | -3.8506 | -49.1422 | 2024-11-26 00:40:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 3b70dcc7-7adf-3ed0-bb4c-5076604566a1 | -3.5857 | -50.3787 | 2024-11-26 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 310.5 |
| 98794824-6b39-3413-9853-ec1e48928583 | -3.9078 | -42.4256 | 2024-11-26 00:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 435c2f73-8da6-3f0e-84c7-5b131796b6c1 | 2.6901 | -60.4301 | 2024-11-26 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 92.0 |
| e74c483d-4f0a-38ce-9e37-55fd6d7bc600 | -3.9265 | -42.4246 | 2024-11-26 00:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 5c8dce66-e577-3fb7-bdcd-dba6d736f2cb | -1.4951 | -53.8146 | 2024-11-26 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 99b9e301-4015-36d2-87e1-d37d95c15b9e | -3.6041 | -50.3991 | 2024-11-26 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 7a852d2d-597a-3d68-9f6c-f43c311e6b3c | -3.3938 | -44.1722 | 2024-11-26 00:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 30302b6d-327c-392f-9741-7fd8b53bf25d | -3.3752 | -44.173 | 2024-11-26 00:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| d6701a51-e14c-3a7b-b91a-b58a3e95bdf7 | -3.3939 | -44.1492 | 2024-11-26 00:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 88078624-7e2b-32cf-b7af-8d6a19ebc918 | -6.0862 | -48.0339 | 2024-11-26 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 659b1fb0-ef3e-3cdb-be6c-11aa81777db3 | -3.3937 | -44.1951 | 2024-11-26 00:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| c06815f8-bbce-3948-ba6a-b9ada0f639ab | -3.9674 | -48.0851 | 2024-11-26 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 9731f0a1-3a52-38f7-891e-2d949a9074f6 | -4.6733 | -47.9434 | 2024-11-26 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 2d86d0cc-b071-368b-a5c9-aa101d2339e9 | -3.5856 | -50.3997 | 2024-11-26 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 175.9 |
| 878d6c4b-8b91-3ac3-a379-b55e63d06bab | -3.9675 | -48.0634 | 2024-11-26 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 387413de-af5a-3c4b-aade-7580c70345dc | -3.2906 | -50.2837 | 2024-11-26 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2749be35-3bc7-385a-be0d-cbcc5e143098 | -3.287 | -51.1609 | 2024-11-26 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 57bb2953-f659-3087-b0ad-ae80e8042d1c | -3.6042 | -50.3781 | 2024-11-26 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 223.6 |
| 4aca08b9-53bf-33cf-81d2-1a3a611b75ec | -2.8017 | -52.921 | 2024-11-26 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 01d7a515-7c5a-39be-8e26-a84b069a6a41 | -2.8198 | -53.0222 | 2024-11-26 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2a95ba50-92a8-3fad-8ead-1c2647a39124 | -1.4768 | -53.8148 | 2024-11-26 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 95018061-da90-3691-8f96-ad708017d124 | -4.6547 | -47.9444 | 2024-11-26 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 11f6cdff-df4d-32f8-9cad-55e036575321 | -3.9861 | -48.041 | 2024-11-26 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 207121ab-0ce0-3dd2-995c-5cb276258d82 | -2.1965 | -45.9754 | 2024-11-26 00:40:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 37.8 |
| e58381b5-effc-34d9-b503-4a2c796c7ab1 | -3.8691 | -49.1415 | 2024-11-26 00:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 9d371fb8-e0f9-361b-8a67-f4f0a0f321c7 | -3.2224 | -51.601299 | 2024-11-26 00:41:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 825312c5-2a29-36b3-a541-5520bf15392c | -2.4677 | -49.1082 | 2024-11-26 00:41:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c2f56b1-0528-3124-94a3-76c96b1cba1e | -3.1819 | -48.444698 | 2024-11-26 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 788a1e81-392a-3256-84fc-4401217176f4 | -3.5839 | -50.380798 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c7b227d-bb83-325f-806e-553481079d56 | -3.2199 | -50.7742 | 2024-11-26 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11626589-e9bb-3ca0-84a1-9a2870f57961 | -3.9614 | -48.0658 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 615d780c-1320-337f-94c1-bcdaaadfaf24 | -3.4723 | -48.227001 | 2024-11-26 00:41:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af0c4127-4261-3bc5-9c97-1c5913bd8d2e | -3.3832 | -50.088501 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fcfce91-135f-3f8a-b425-e91207a317a8 | -3.7156 | -50.1898 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d96d1603-f843-3dd3-9167-8c96c874d0bd | -3.114 | -45.084499 | 2024-11-26 00:41:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6406ba6a-45b0-305e-ad2d-0ce76bc691cf | -1.9781 | -53.284801 | 2024-11-26 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 352162f2-71c5-326c-be13-38b87d01464f | -2.128 | -45.319199 | 2024-11-26 00:41:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63771c03-f0e4-37a4-bc13-a509c4ec40e6 | 1.9349 | -55.730701 | 2024-11-26 00:41:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28e8919e-a150-30ba-88f7-d8704887dfa3 | -3.9712 | -48.063599 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8dec9ff-5b33-323d-af16-afbabd30f15a | 2.712 | -60.379799 | 2024-11-26 00:41:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1979349d-c951-31ae-ba98-17213e90e32e | -3.5937 | -50.378601 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273a6f05-b682-3a6c-b389-ec3c7f890723 | -3.5364 | -50.3988 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5241fc95-e843-3b06-80a3-006b32a64780 | -3.9582 | -48.051899 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d748b83a-d689-3596-b00a-7fb8be976838 | -3.9746 | -48.0336 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 181e28f6-6447-379c-8aa9-3763d0f350d8 | -2.9798 | -49.5872 | 2024-11-26 00:41:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fbbe377-ea89-3b89-befb-fb5ec6f40ed0 | -3.968 | -48.049702 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ff89026-6784-3155-9efe-fb79acebb1cb | -2.8578 | -45.3554 | 2024-11-26 00:41:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffc077ee-b2f1-3d76-994f-35ffd4aa74a3 | -2.8501 | -45.366699 | 2024-11-26 00:41:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f49a8df-f3fe-3edd-82b7-1b8e6b8e20d7 | -1.8657 | -44.768398 | 2024-11-26 00:41:00 | METOP-C | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 290355a5-dc0c-3514-939a-360db396a7b3 | -3.9794 | -48.054501 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dcd42aa-463f-3a95-b580-75ad834517bb | -2.1886 | -45.978802 | 2024-11-26 00:41:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e056fe0c-81ab-3b40-b862-de37c7378d1b | -3.4864 | -49.6824 | 2024-11-26 00:41:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83bf9fde-9e6b-36dd-bc0b-b1dd07e2472c | -2.2448 | -53.4627 | 2024-11-26 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70e27470-4f17-3382-b411-56a3d41de0cd | -2.8007 | -53.011002 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2131f6ac-3b27-3a3c-9ddf-5e24a23f86b3 | -3.8591 | -49.147499 | 2024-11-26 00:41:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fecfa01b-319e-3bf3-a312-c2b47cf24c05 | -3.4888 | -50.460999 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f71510-dcc2-38dc-8015-442024f1c492 | -3.955 | -48.037998 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19c7e4eb-b28b-35d5-a2f8-d2c8cfe6293a | -1.5921 | -47.455399 | 2024-11-26 00:41:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 939cbc72-c2bc-346b-9238-b90cccb1654e | -3.9728 | -48.070599 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47b8268a-5d0c-3f62-b1c2-a4049d9cec2c | -3.8559 | -49.1339 | 2024-11-26 00:41:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52639676-e431-3618-95a3-2ea949c405df | -1.4698 | -53.808701 | 2024-11-26 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35fdc791-09e1-3690-9a85-01761a3595a5 | -1.5624 | -45.678398 | 2024-11-26 00:41:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ceecce0-1477-3435-966c-bfb7a74084aa | 2.6916 | -60.422401 | 2024-11-26 00:41:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1c189058-a24b-3300-aa6d-0a97bcc4abcf | -2.7966 | -52.902 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7ad628-6a90-3c26-ba74-31c8a7e56e7d | -2.6634 | -52.995201 | 2024-11-26 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 310e7bd6-963e-3c37-af93-67fe859b07d5 | -3.2743 | -50.018299 | 2024-11-26 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97ac7da0-c083-30d3-89fe-b6735cab8fc9 | -3.9662 | -48.0867 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f63af897-89bb-3c79-ae7d-9e7f92c3c752 | -1.5955 | -47.470299 | 2024-11-26 00:41:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b12b854-a135-366e-a069-4068b5d132c9 | -2.7679 | -48.573799 | 2024-11-26 00:41:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e53b9819-e09b-3e6a-8320-926e48be1d2d | -2.7791 | -53.0065 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83fdedc8-7f11-378c-a2a1-3fd65b0c6435 | 2.7023 | -60.377499 | 2024-11-26 00:41:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 120b7956-c876-3726-bcd6-006f89f0f0f4 | -2.848 | -45.357601 | 2024-11-26 00:41:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d5b9553-a1af-3c83-a685-9d47742e826e | -1.4415 | -47.115799 | 2024-11-26 00:41:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 471e401a-6784-341e-86ad-7e160c303c51 | -3.3848 | -50.095402 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eca977d6-9dd9-386c-b2d4-e788d4231328 | -3.9532 | -48.075001 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b54962ef-5d7b-37e1-a540-277570d25d3d | -2.7889 | -53.004299 | 2024-11-26 00:41:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76f6f679-7969-31ac-aca2-a89173a7efe9 | -3.497 | -50.4519 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af6af57d-f818-3728-b9bb-5e152b2824c3 | 2.7067 | -60.402199 | 2024-11-26 00:41:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d7f85867-04bf-304f-9ac7-9be2d3297a20 | -1.8634 | -44.758301 | 2024-11-26 00:41:00 | METOP-C | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3e4f202-16e5-321a-8815-4e248504887c | -1.5481 | -53.791302 | 2024-11-26 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3208dda8-3422-34e8-b2f7-873d13685bad | -3.9696 | -48.056702 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3383827-8cda-387f-af82-c7842cc95325 | -3.2888 | -50.2626 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 883bce6b-099b-30e9-bcf3-24d3a06b4ecf | -2.9291 | -48.0191 | 2024-11-26 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 316265f0-1ac6-382c-a201-d187fdc96e51 | -3.3231 | -50.050999 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cfcf060-7c01-39a2-ae45-fcddb163b75c | -3.9678 | -48.093601 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f3c43a3-1045-36b3-83dc-080ef8f8ce6d | -3.9776 | -48.0914 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86de2152-0fc0-36d2-bb2e-58ac4fa2206f | -3.286 | -51.155201 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42ba8b9f-009b-3865-94e1-691fa110fe77 | -3.446 | -50.0019 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a96ad16-b239-3e16-af06-f55ae346ddc6 | -3.081 | -51.0243 | 2024-11-26 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d54684b3-5d23-3b5a-881b-76870fede59b | -1.4774 | -53.797199 | 2024-11-26 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74a5bc10-c2c6-37ca-84dd-d29c37b58f57 | -3.244 | -45.6847 | 2024-11-26 00:41:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43236716-dd59-3f9a-b890-a141f4cb50f7 | -2.5234 | -45.6012 | 2024-11-26 00:41:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 363323fd-582f-3429-befb-fa51cf617840 | -3.3247 | -50.057899 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5153e8e2-20d3-3ca3-b012-47d60b627261 | -3.9744 | -48.077499 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff9e56fc-ad31-3c02-9729-4ae027584861 | -2.1847 | -45.9617 | 2024-11-26 00:41:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de231d40-1e8a-3eea-938a-a75a459fe70a | -3.9598 | -48.058899 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24c4141d-cc11-312d-b5a4-8ffeaf8452fa | -3.1119 | -45.075199 | 2024-11-26 00:41:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
