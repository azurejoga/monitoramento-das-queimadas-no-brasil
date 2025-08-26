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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d9bf133-c422-3465-a582-869f6a31a381 | -8.8548 | -62.4503 | 2025-08-26 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 254.6 |
| f4c580ea-294a-3667-a4b5-0a05318106f5 | -7.3669 | -64.3667 | 2025-08-26 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 64dcb88c-f387-36c3-ad2d-7fc207999b90 | -6.7144 | -58.5732 | 2025-08-26 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 9207b08e-2fe7-3925-b9a2-d8b511c0bae7 | -11.14 | -44.7422 | 2025-08-26 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 327f3979-5f38-35e2-a4fc-72411d3121ea | -6.7636 | -59.6526 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| fb481989-e024-3838-9112-400fc3494a05 | -8.3396 | -50.5652 | 2025-08-26 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| baf13748-8cd7-370f-a51f-e40039797f5f | -9.1724 | -59.4436 | 2025-08-26 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| ac87a6aa-8b0c-3ce8-bbf6-0eda30e375b3 | -11.1591 | -44.7395 | 2025-08-26 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 219.3 |
| 7c9118b9-2b1d-311c-ae96-453ba93f1316 | -6.8413 | -58.9552 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 1008ce3f-fa7f-3ab0-9382-d27d926140fa | -8.855 | -62.4313 | 2025-08-26 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 97.4 |
| d1803715-7fe2-3a33-b963-32dbd17a5b91 | -6.246 | -59.9982 | 2025-08-26 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 3ca7dcd2-8275-3ec3-8a1d-9d62852aca22 | -6.8228 | -58.9753 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 538.4 |
| 8a52d0bd-0cfe-3326-9420-262f238ea982 | -4.9605 | -55.8226 | 2025-08-26 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| e96195d8-60f7-3bc0-bf5a-db68a3922680 | -11.6277 | -46.3899 | 2025-08-26 00:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 09167fa1-10b2-33d7-9e03-7004469b62ad | -10.4241 | -64.3903 | 2025-08-26 00:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 63f3c822-107b-3a12-8b79-c8853e8fc51c | -6.7635 | -59.6718 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| aaa03fac-47df-3326-b71d-b3b385cb17f0 | -13.1644 | -45.2897 | 2025-08-26 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 173.1 |
| c6d9e543-b5ea-32f4-a27c-f3c8060b90c5 | -7.367 | -64.348 | 2025-08-26 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 0d5662ad-9015-3d79-827d-694fc66e7bd3 | -6.7819 | -59.6711 | 2025-08-26 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7da7dc20-0d6a-3397-b2b1-dba8879d024a | -6.2275 | -60.018 | 2025-08-26 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 715ca510-f229-313f-9ab8-54359670e6fe | -11.3126 | -55.1112 | 2025-08-26 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 130f21f0-f998-3805-b219-82c69250a11c | -6.6961 | -58.5546 | 2025-08-26 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 82061a1c-47c6-3e1f-82fc-78876adfa7dd | -9.1909 | -59.4619 | 2025-08-26 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| aca47b9d-1d5d-3afd-83c2-c16c6490f15d | -9.0231 | -65.7169 | 2025-08-26 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 2bc90d9c-94ba-39b0-958c-ce690e42da5b | -11.6273 | -46.4126 | 2025-08-26 00:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 79bd44f0-9d33-38c0-94eb-08e94a32aaed | -13.4425 | -51.1566 | 2025-08-26 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 2217c09e-96f4-3328-a234-ed8a3705ba15 | -9.0415 | -65.7349 | 2025-08-26 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| c6d9b452-2435-3f43-852e-09e98c7a7f04 | -7.3875 | -64.326202 | 2025-08-26 00:42:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 811dcb60-4bd3-34b0-bafa-d1b45d23b856 | -6.2415 | -59.988499 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6cdf5abf-0233-32e0-ac09-29b394050be1 | -6.8364 | -58.950401 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3726e7bf-1952-3d01-89d8-d9c6d92afc6f | -6.2336 | -59.999401 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 465315e1-9a2f-37f9-bad3-0bd5c93f3cc5 | -9.2843 | -56.895699 | 2025-08-26 00:42:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79a033d0-0d64-3150-9119-847dc7ab5778 | -9.1705 | -59.452999 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8903d564-9ff6-3b02-9715-3b0da7c02984 | -8.3251 | -50.553001 | 2025-08-26 00:42:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edc224c1-cec6-3c59-9ebf-fe000ad7cc9b | -5.4519 | -60.131302 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d3f9476-6bd8-3b8e-a53a-f621e51b1d34 | -9.5816 | -55.359699 | 2025-08-26 00:42:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e5dfa44-723c-3191-a907-6f151ecd761d | -6.781 | -59.6385 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc81b04-8705-34e2-87d2-8fb7f8993189 | -8.9124 | -60.6987 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| caa88ed1-050b-3403-a321-cf0539143700 | -6.7057 | -58.5415 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 077e82b6-29f0-3b45-ae91-affab6e9f68f | -7.3778 | -64.328201 | 2025-08-26 00:42:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f158da2e-6264-3c78-8764-9563208b857c | -6.315 | -59.855 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9cb63e-3afd-3a00-ae0f-20307426ad2b | -6.9127 | -59.347599 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02e99dd2-2917-3f00-b0c3-6cd6fa921aed | -9.1901 | -59.448799 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f031e4c5-cc31-38a1-9187-a885064844ce | -20.8585 | -48.461899 | 2025-08-26 00:42:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 28ab69d8-2d4d-3234-916e-5e930d65697a | -9.1858 | -60.783901 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48f8d363-726c-3d69-94ad-fbadc526601a | -9.2673 | -59.764099 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f29951a-b61d-38c3-90bc-820832d0f8ed | -8.9066 | -62.432098 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b31b0c67-0805-342c-aa79-2749291197e1 | -8.9892 | -65.387901 | 2025-08-26 00:42:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b379badc-51f2-3260-9f79-dc9223f082a6 | -8.2166 | -49.543098 | 2025-08-26 00:42:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23dfbddc-a6b1-3032-b8aa-2a0e5c78b619 | -9.8085 | -64.2285 | 2025-08-26 00:42:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 85cbd4e4-f95d-3d28-887d-d7de9bbe349b | -9.2033 | -59.5112 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98198637-8a5c-304d-a2da-e9812707c033 | -7.4412 | -60.609402 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78ffef09-46ee-3df6-93fc-01ae357f19c3 | -9.2376 | -60.884701 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9c4e617-4115-3234-87d2-b99540855b80 | -6.7712 | -59.640598 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6bad2838-b74b-3ffc-94ce-664f933c843b | -7.1069 | -59.202702 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0aa2f14-b671-3ec3-b081-c4a19f2ddb95 | -5.8022 | -59.1996 | 2025-08-26 00:42:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18752565-2daa-3a09-b8d1-80aaab15a01c | -9.8122 | -64.247101 | 2025-08-26 00:42:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 60c32227-894b-3dc0-bba1-7d5c434b9062 | -9.1699 | -59.546501 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7b91ea8-1071-3495-b1cb-18dd8b6dab21 | -7.3576 | -59.648899 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e03542e5-5d59-333f-b2a7-5e7383d6a7e1 | -6.8202 | -58.970501 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d81d1e4-a288-32df-bf20-4fcef2f1d9d4 | -9.0815 | -62.6395 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cd0d2969-3bb3-3a7d-b7dd-a28aa3bfbb36 | -7.3674 | -59.646801 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8fcc803-2854-3917-a183-36e99ad01db0 | -9.1882 | -59.439899 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a60044e-f9c8-38cc-84a2-1a075de4e9b3 | -6.6909 | -58.520901 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9cc6745d-242d-333d-b833-8e792ce6dd2c | -8.855 | -62.4286 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad639f41-6406-3e19-ad20-46e67ca2f0ce | -9.198 | -59.437901 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f28f1e5-3db0-30ec-af1b-73cdfeb7ddfd | -6.6814 | -58.8526 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0dde845f-f2fc-3d0f-86b9-e6316be18cbe | -8.3437 | -62.908401 | 2025-08-26 00:42:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca889be-fd38-36d8-a8e7-bf1d5d9d9e0e | -9.1682 | -59.4907 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 991a7ff1-25f5-3cc2-b82d-01873ec6cad7 | -6.7945 | -59.6534 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89c2663a-789d-39fd-9578-8336f79ce3a8 | -8.8675 | -62.440102 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d94a9bc0-5891-38db-98fd-1f26a951d95d | -7.748 | -50.294399 | 2025-08-26 00:42:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8b3390c-ebd0-3753-a615-e367bb3e6199 | -6.2532 | -59.995201 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e972505c-c260-3f26-be05-922b9fd15c20 | -4.9627 | -55.801201 | 2025-08-26 00:42:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b929f82b-9c15-3c14-bf8c-042d4e8951ce | -9.1686 | -59.444099 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97261684-353f-3df0-b4ad-bdda6cc87362 | -8.8592 | -62.399799 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ec9098cc-bfef-3111-98d1-335ebcb36a0c | -7.541 | -61.365501 | 2025-08-26 00:42:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87fdfc12-3614-38df-836a-780398a9d032 | -8.8494 | -62.401798 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c16f3ed-6ba3-3675-b50a-c642188c40f6 | -9.1818 | -59.506401 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01eecd4a-b9a6-3222-92ce-a66b5f6f8ba6 | -6.7074 | -58.549099 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6cfcbb08-157d-37ca-9893-213703b90abe | -6.8231 | -58.936798 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 764b799a-0514-3b2a-9d46-7fc3a350a3fb | -6.6644 | -58.775002 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed1978db-ca0f-33d8-9b44-a33599316c03 | -8.9752 | -65.368202 | 2025-08-26 00:42:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93131959-0639-3ae4-b814-61504b015280 | -6.709 | -58.556702 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 546a9229-f17e-34c3-b836-5538324a21b0 | -9.0368 | -65.677902 | 2025-08-26 00:42:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a44227d-d9e2-3ffd-8bd4-74a3dfb31314 | -8.8842 | -62.4226 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d9ba0ad-b3c2-37bd-9f6a-6b6306ec1a9b | -9.178 | -59.488602 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7b11948-2dee-3927-aa92-90a69d258623 | -6.7865 | -59.664001 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10d368b6-6839-32c2-90c2-4c5356639820 | -9.1857 | -59.524399 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 050e94e4-472a-3bc7-afd6-7d822743d677 | -7.6197 | -61.014599 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3e31274-4091-38b6-87c4-802b9bdd374c | -7.3594 | -59.657501 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f198117c-0a7a-3ddd-8c9e-3e4fa588e99d | -9.1916 | -59.504299 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12e29b0d-6eee-34f5-b676-e5a86e6940f8 | -6.653 | -53.182201 | 2025-08-26 00:42:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4804ba34-fb61-36fe-8e20-d7fa210a2d01 | -9.1759 | -59.526501 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 653f73f9-ffec-35e2-b582-91b710d661f9 | -8.8718 | -62.411201 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2067287c-1de1-33d7-8bc4-dd9607504586 | -9.168 | -59.537498 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15c29e4f-fc17-3f2f-a9c7-8d4cc563258f | -6.6942 | -58.536098 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4c288bd-32ab-3a4e-8901-c49e1e8f76cb | -21.040501 | -48.613201 | 2025-08-26 00:42:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 225c8991-3492-35c1-92aa-76214b2e1ff0 | -9.1563 | -59.530701 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0bad7d8f-808a-3f3e-8743-25d6fa8a70be | -9.5734 | -55.3689 | 2025-08-26 00:42:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
