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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5256d2da-dd76-3a1c-ad86-5bad426e9a84 | -11.2034 | -54.7752 | 2024-09-27 01:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| c2c84850-be8e-3820-9689-9708f9ddaa2f | -11.2036 | -54.7548 | 2024-09-27 01:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 555d9f86-8520-307c-8484-2f80e34ca284 | -11.2223 | -54.7735 | 2024-09-27 01:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 94cabd9a-fba7-37d9-8d60-7e525a410299 | -12.1672 | -50.8004 | 2024-09-27 01:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 071c913e-fe77-3d0b-b03c-1c777cc10371 | -12.6636 | -54.6782 | 2024-09-27 01:46:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 4c2c2eea-2a23-3260-b668-0e01f64fe5d4 | -12.6824 | -54.6968 | 2024-09-27 01:46:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 2687db95-e67c-325d-908c-f6c52738ece2 | -12.6826 | -54.6763 | 2024-09-27 01:46:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| dc154501-223c-31e1-b989-903b7af1a61b | -12.8437 | -54.0422 | 2024-09-27 01:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 4ffaca93-425b-3e57-8845-80dd393c705b | -12.844 | -54.0215 | 2024-09-27 01:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 6a11b2f2-a807-3b83-9e4f-8c4943dabd7e | -12.8628 | -54.0402 | 2024-09-27 01:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 0ec941d5-b1e6-3688-9213-7c792aec5738 | -12.8631 | -54.0195 | 2024-09-27 01:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 0bed03e8-d279-3eee-85f2-2d99c8a2f5da | -12.8634 | -53.9988 | 2024-09-27 01:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f4b86c23-1a00-3bbc-86b4-7a3b499cb421 | -14.7109 | -45.5096 | 2024-09-27 01:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 415f51ac-95f3-32cc-8b4f-23eccd8904d1 | -14.7114 | -45.4863 | 2024-09-27 01:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 1a8c300b-ae3e-3505-86c5-04a6e3c3d115 | -14.7305 | -45.5061 | 2024-09-27 01:46:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 31622744-9e4c-339e-b25b-18a56ea8e67c | -14.731 | -45.4827 | 2024-09-27 01:46:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 786dd52f-bde5-32a1-a9ef-64f0434ff2ec | -16.8933 | -58.0213 | 2024-09-27 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 6fdc5721-e883-3026-a486-852388aefa10 | -19.6136 | -42.8159 | 2024-09-27 01:46:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.6 |
| 70b5d173-345b-3029-b20b-a76524ea9b10 | -21.0986 | -49.1347 | 2024-09-27 01:47:03 | GOES-16 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| 1d1ed1b9-5be3-38ec-8c28-5e5c17dbdbae | -21.4123 | -42.9778 | 2024-09-27 01:47:03 | GOES-16 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| 1bc81bc0-a621-32aa-a655-ac8af2468c92 | -22.7442 | -44.7785 | 2024-09-27 01:47:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 178.2 |
| 3734cc09-1fc1-3299-a096-a65ffd788f24 | -22.7433 | -44.8035 | 2024-09-27 01:47:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 267.7 |
| d60ddd7f-2717-3698-b1c5-9c44910909ee | -22.7645 | -44.7973 | 2024-09-27 01:47:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 50490b48-3aa6-3588-a37d-09b300b78ae5 | -2.3579 | -47.6206 | 2024-09-27 01:55:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| d62954ca-7f49-30bf-87ea-9048e587fa8e | -2.358 | -47.5989 | 2024-09-27 01:55:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a94a6cad-67ae-3fbb-9349-0832e2103cb4 | -2.6783 | -57.6087 | 2024-09-27 01:55:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 572e66eb-4a6c-3d65-9497-a90883745531 | -2.6783 | -57.5893 | 2024-09-27 01:55:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| c5441365-1300-3e3a-a1a4-48cd66973474 | -2.8611 | -51.6699 | 2024-09-27 01:55:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b1e04bcf-c1f4-3bcc-9664-d3072fad45bb | -2.8795 | -51.6695 | 2024-09-27 01:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 894e4b27-80a7-3c5c-b560-b2ccd2542ba8 | -3.2136 | -46.7843 | 2024-09-27 01:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| d51c9410-0fb0-3afd-939b-2e40750931b1 | -4.1423 | -46.7007 | 2024-09-27 01:55:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ee39703e-57af-3f29-86dc-713ed8e6e654 | -4.1425 | -46.6787 | 2024-09-27 01:55:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 98fec3e2-3a05-3a86-9ae8-f9c4399f7ecd | -5.397 | -43.4332 | 2024-09-27 01:55:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 99801374-2ce6-3882-89e9-9d5039a07f7b | -7.2006 | -60.6706 | 2024-09-27 01:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| e9a526f5-1c63-39aa-80be-b9a02e8e5637 | -7.272 | -61.1067 | 2024-09-27 01:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| e90100a1-1318-3e95-94a5-7b400a1c0ff8 | -7.2905 | -61.106 | 2024-09-27 01:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| a9c4c887-fcdd-302b-b00a-18c1ad52b089 | -7.2906 | -61.0869 | 2024-09-27 01:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| ac372506-19f9-3622-9440-15467ff7d7fb | -7.3089 | -61.1053 | 2024-09-27 01:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 51b5d08b-9f7f-3279-bbbb-0ac085b19b4f | -7.309 | -61.0862 | 2024-09-27 01:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 87f8d8c1-9190-37a0-a4cb-ae1a8f1dcc9e | -7.3091 | -61.0672 | 2024-09-27 01:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| f3e0bb61-0b0c-3c4d-9a96-cd6dd20afd5e | -7.5703 | -60.5984 | 2024-09-27 01:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 3893fd3b-85af-381b-a5a7-a2b8a1708784 | -7.5704 | -60.5793 | 2024-09-27 01:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| fe63b17c-36ba-3aab-9670-9827a27a073c | -7.5887 | -60.5976 | 2024-09-27 01:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 58b03bf5-c264-3c08-8a18-280903fed5f6 | -7.5888 | -60.5785 | 2024-09-27 01:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 5821c748-32ad-340d-a7e7-63e619ec82eb | -7.77 | -61.2015 | 2024-09-27 01:55:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 164.4 |
| b7f330e1-a43f-3354-b323-822a354547b4 | -7.7701 | -61.1825 | 2024-09-27 01:55:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 219.4 |
| 7698ffa3-0e27-3feb-8335-ed015965d92f | -7.8156 | -54.7252 | 2024-09-27 01:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 4af710cd-fca3-3449-b87f-4d08daf5fbfb | -7.7885 | -61.2008 | 2024-09-27 01:55:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 32a25c60-9686-31b8-bdc0-cbbee30ab01a | -7.7886 | -61.1817 | 2024-09-27 01:55:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 171.2 |
| 3b0d1b67-f44f-39d8-8a47-172e67936f7c | -7.9174 | -61.2909 | 2024-09-27 01:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3455132d-791a-3e48-88d2-cef83f14cf31 | -7.9175 | -61.2718 | 2024-09-27 01:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| a60ffaff-a752-3548-90c7-4728e40e5959 | -7.9359 | -61.2901 | 2024-09-27 01:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| f3b71e4a-92cd-3432-9500-c8b93a4bfe64 | -7.936 | -61.271 | 2024-09-27 01:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e070adc1-ed72-38ac-ad73-3e5201ce4e70 | -8.1394 | -61.2817 | 2024-09-27 01:55:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| ff8bc678-1943-31b2-9e23-af7f221042f6 | -8.1579 | -61.2809 | 2024-09-27 01:55:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8713fa8a-6771-3b7f-acf8-567b967917bf | -8.3215 | -56.4929 | 2024-09-27 01:55:54 | GOES-16 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1577c5af-d331-38f2-a595-a2036eb85481 | -8.556 | -49.6112 | 2024-09-27 01:55:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| b077042e-e4d9-3628-94ae-2d6a4bc3d095 | -8.6847 | -66.9911 | 2024-09-27 01:55:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 20fc0be3-f725-330b-8c62-55a3ee2ee15e | -8.7032 | -66.9907 | 2024-09-27 01:55:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 470cbba3-f7eb-3dbe-b689-a369b967c754 | -8.7033 | -66.9721 | 2024-09-27 01:55:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 13375fae-4bf6-37fc-b36d-d113da43c39a | -8.8116 | -67.6917 | 2024-09-27 01:55:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 11133b02-9183-34a0-b294-872f29ff9d88 | -8.8117 | -67.6732 | 2024-09-27 01:55:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 165.6 |
| f62d07a4-dfd6-3864-8e25-4a0362aae04d | -9.086 | -61.1245 | 2024-09-27 01:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 91bc08bd-a7c0-3546-82ea-c840a9ed0d45 | -9.4574 | -40.3641 | 2024-09-27 01:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 52.0 |
| 7042a7cd-8fa3-324e-9b36-00e354069052 | -9.4578 | -40.3392 | 2024-09-27 01:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 3860924c-cfa1-34ef-b4c4-b824be0a6d84 | -9.107 | -67.8881 | 2024-09-27 01:55:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 3f67c137-48d3-38d6-8b6d-a75456574339 | -9.1616 | -68.1643 | 2024-09-27 01:55:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 68bc0e7e-acef-3e7d-ab92-cb4f278d134c | -9.417 | -51.4426 | 2024-09-27 01:56:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5a2ded82-a4d9-3cef-8596-08bcf1b8510f | -9.3672 | -63.6972 | 2024-09-27 01:56:00 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| aae6f55d-ba25-34d9-87b8-04d82fadcaa8 | -9.6018 | -50.1352 | 2024-09-27 01:56:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| f43b8f8d-f77b-3449-8b44-c09dc9b6ae63 | -10.0322 | -53.4859 | 2024-09-27 01:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e3092424-4496-3f66-8f7c-c70704f7880b | -10.0324 | -53.4654 | 2024-09-27 01:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7a793f76-17fc-386c-96de-77dd63f22b44 | -10.051 | -53.4844 | 2024-09-27 01:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| c6107b2b-97ff-3731-ba87-0d87d945849b | -10.0513 | -53.4638 | 2024-09-27 01:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 42f6a374-4091-357f-96ca-c7f37afe0f04 | -10.3672 | -53.7858 | 2024-09-27 01:56:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 2290898b-d74d-365d-9426-008d42cdb4e8 | -10.6449 | -45.8862 | 2024-09-27 01:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 0b827ea2-5d6f-3657-bf55-97dc8d7d031b | -10.6452 | -45.8635 | 2024-09-27 01:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b16bc1bc-fe7d-3237-90c3-d8818fdc6489 | -10.6639 | -45.8838 | 2024-09-27 01:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 925ba0c9-75ae-3bd7-b175-6424af2a4e95 | -10.6643 | -45.861 | 2024-09-27 01:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| d8e3ff13-17d2-3176-ab7f-a01732ddc8e6 | -10.461 | -50.7529 | 2024-09-27 01:56:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8c25860f-f684-35db-8182-6c784571e684 | -10.4799 | -50.751 | 2024-09-27 01:56:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e907b9c1-7e24-3a10-afcf-532e9748501a | -10.7211 | -51.0869 | 2024-09-27 01:56:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 0c6cc77a-355f-3f57-b297-197a4dadc5c9 | -10.9264 | -54.2692 | 2024-09-27 01:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 207.2 |
| d545c7da-a9b0-3f5b-bdc2-6d9dee3079bc | -10.9267 | -54.2488 | 2024-09-27 01:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 232.9 |
| 6bc05548-053e-3dcc-b3bf-5e5259530acd | -10.9453 | -54.2676 | 2024-09-27 01:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 10df62f5-f8bb-3be9-a4d6-4c9a9bb679c1 | -10.9456 | -54.2471 | 2024-09-27 01:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 478d5701-e34c-3fa6-912d-0ff9eeacd7de | -11.2034 | -54.7752 | 2024-09-27 01:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 45810300-f7c4-3c08-b546-56ad4cc71a0b | -11.2036 | -54.7548 | 2024-09-27 01:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| c85b47dc-f966-3742-a664-c4e3799c95f2 | -11.2223 | -54.7735 | 2024-09-27 01:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 3042137e-2e66-3c3a-9976-dcf3c04b1b0d | -11.2409 | -54.7922 | 2024-09-27 01:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3bb01c9d-e16d-3ea3-b5b5-7039f7f55b5f | -11.2412 | -54.7719 | 2024-09-27 01:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 353bdc02-9775-381b-bac7-650ad6831964 | -12.1672 | -50.8004 | 2024-09-27 01:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 7bffa9c6-a1e9-3218-a217-4f4cab7e3a98 | -12.6636 | -54.6782 | 2024-09-27 01:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 4712cdf9-ae26-3118-a41c-a323da1c3789 | -12.6824 | -54.6968 | 2024-09-27 01:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| cb0414a4-160c-3411-bc9b-47b055c89e81 | -12.6826 | -54.6763 | 2024-09-27 01:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| dea08fcc-c1ad-358e-a825-ab156923c1af | -12.844 | -54.0215 | 2024-09-27 01:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 3ea07c33-9eef-3ee5-8721-bfa7de4f79ce | -12.8628 | -54.0402 | 2024-09-27 01:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| ce18614b-4476-3d19-abbe-47550585c11a | -12.8631 | -54.0195 | 2024-09-27 01:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 3077021f-67d0-3c2d-ba9c-34602ee755bd | -14.7109 | -45.5096 | 2024-09-27 01:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 71e88089-6798-35a4-a5e7-8e269c9c32b1 | -14.7305 | -45.5061 | 2024-09-27 01:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |


[Clique aqui para ver as próximas entradas](README40.md)
