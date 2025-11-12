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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 650a6e4a-f8d8-37f4-8b84-d5aebb336e04 | -3.98142 | -47.30089 | 2025-11-12 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 710d7e7b-25e1-33c3-a28f-24950f9c1106 | 3.75985 | -51.78541 | 2025-11-12 00:56:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4c287fa3-5476-37cf-bfcb-d4248e9e7cf0 | -4.9643 | -43.7182 | 2025-11-12 01:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e543b66e-658a-36f7-8954-37133e3f4dcd | -4.1162 | -47.9919 | 2025-11-12 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 69b61b08-724d-3664-9016-3969b68444d9 | -2.6299 | -49.2045 | 2025-11-12 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0ba29bdf-c2c6-3156-addd-95fabe6d4c59 | -4.0974 | -48.0361 | 2025-11-12 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| a5879576-5026-3d80-8fa9-8a8d6bc3de2b | -2.9982 | -45.1658 | 2025-11-12 01:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2dffc3ee-f302-31e6-b00b-c3bd0f4a363b | -4.1161 | -48.0136 | 2025-11-12 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 228.5 |
| a4f8f3cd-4fe4-350c-a70c-b7f3770f02a8 | -4.0977 | -47.9927 | 2025-11-12 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 18e7b368-f1e2-30b1-8f89-fff2e20bb91f | -4.116 | -48.0352 | 2025-11-12 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| b85d12b7-6a10-3f35-bdf6-d24b99a8c255 | -2.9983 | -45.1433 | 2025-11-12 01:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 37f9af8b-4f62-3417-b002-7ad4660299b1 | -4.9456 | -43.7194 | 2025-11-12 01:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| e622bf90-535a-33e3-92d7-8d4f6f7ed89f | -4.0976 | -48.0144 | 2025-11-12 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 356.2 |
| 0d6b44b8-e352-38e3-b661-3c908d88fd26 | -4.1161 | -48.0136 | 2025-11-12 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 274.7 |
| edf38f7f-89ca-34fb-a29f-2bc0fc9448c5 | -4.9456 | -43.7194 | 2025-11-12 01:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6727ddc6-7cfb-36c3-b750-ad2e663f7d70 | -2.6299 | -49.2045 | 2025-11-12 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 8a852e7e-7a4f-3e6c-8059-e9d368854d81 | -4.9643 | -43.7182 | 2025-11-12 01:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 23d01b3f-9b7d-30c3-bae0-0734b458ae00 | -4.0977 | -47.9927 | 2025-11-12 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2142fc79-1314-3f9d-be35-d40aeddfd5b9 | -4.0974 | -48.0361 | 2025-11-12 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| cbef88a9-01a2-3475-9037-b4e3946f215a | -10.508 | -44.921 | 2025-11-12 01:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 0ce13e09-18ea-3c7b-8c8d-b1e729433b85 | -6.5631 | -51.1126 | 2025-11-12 01:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| f5316094-de98-3f49-a281-0fb1bba2b53d | -4.1162 | -47.9919 | 2025-11-12 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7ab7d3c4-9838-3493-9315-9acdf6f3c98c | -4.0976 | -48.0144 | 2025-11-12 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 366.3 |
| 6aaf3525-270e-322c-b233-dcc34c524b1b | -10.5076 | -44.944 | 2025-11-12 01:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| f4f51383-daa3-34a8-963f-4de95e6a0d23 | -4.116 | -48.0352 | 2025-11-12 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 6b20e5ae-6a41-3da6-b829-da29dc48697f | -2.6484 | -49.204 | 2025-11-12 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 8685445b-264c-30f1-93d5-3bc154873f76 | -2.8683 | -51.4604 | 2025-11-12 01:18:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7223ed38-0807-3d74-929b-0f5f3ba15d82 | 3.1377 | -60.7052 | 2025-11-12 01:18:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2746ea8c-fb9e-3577-a1b4-f438e66f92de | -19.8232 | -57.996899 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6bb4555d-2aa2-3b9c-abea-4df8c8497564 | -21.163099 | -48.684502 | 2025-11-12 01:18:00 | METOP-C | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 780a8abb-7028-378c-b018-1894c0fde9e4 | -19.821501 | -57.9884 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 87250eaa-3ceb-3cd9-9f41-97f78ae2f48e | -20.213499 | -56.618198 | 2025-11-12 01:18:00 | METOP-C | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9345e5ea-cace-3dfa-a8b2-53f16d748c99 | -4.1177 | -48.038898 | 2025-11-12 01:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bdd43ee-63d5-3584-b3c4-f82123d0e9f5 | -21.809 | -56.3027 | 2025-11-12 01:18:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c0e537e5-c265-326f-bccb-7ce3f41a62a5 | -22.785601 | -51.683998 | 2025-11-12 01:18:00 | METOP-C | LUPIONÓPOLIS | PARANÁ | Brasil | 4113809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 991b6334-c09a-32d5-9f90-5af56bf66796 | -4.0923 | -48.018501 | 2025-11-12 01:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61d01427-e706-3668-a1c4-f038147963f8 | -19.811701 | -57.990601 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 544257b6-5a8c-3ac5-bc64-83366f9e9d68 | -4.1019 | -48.016102 | 2025-11-12 01:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6473e7ad-3873-30d7-bbc5-9881209668d5 | -19.7708 | -57.990799 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| db47226c-bf84-3cb7-b679-ec716e193e7a | -19.7754 | -57.9632 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6a2126d4-2e4d-3bc5-81df-89020855e0ee | -19.7432 | -58.005901 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a7c8e14-b9a2-3f96-97e9-b22bfd666526 | -4.086 | -47.993301 | 2025-11-12 01:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bb12581-c429-3392-976e-3c144d47ca44 | -4.1115 | -48.013802 | 2025-11-12 01:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 368e7248-9bbb-3404-b0ee-a869d3028e6a | -4.0985 | -48.043598 | 2025-11-12 01:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43ba5a74-3d24-3263-8c5e-a58a6d953206 | -20.8964 | -50.093601 | 2025-11-12 01:18:00 | METOP-C | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae7c6feb-b703-360d-a531-6edf1027fc40 | -16.883499 | -51.654099 | 2025-11-12 01:18:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5b4f2057-9886-35b1-bd4d-19fa2e916bb3 | -21.8074 | -56.294899 | 2025-11-12 01:18:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c9cb59b1-bb5a-36ec-b5a5-693e054c32c8 | -23.5965 | -49.0051 | 2025-11-12 01:18:00 | METOP-C | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 16dc91d4-dec4-3774-9832-3c3406701b50 | -20.8892 | -50.1064 | 2025-11-12 01:18:00 | METOP-C | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1dee4ced-a7b1-39a4-9cff-e3fa42ebd422 | -19.709299 | -58.0401 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1c62097d-a8e9-3a76-a7a0-cc54173b64a4 | -4.1053 | -47.988602 | 2025-11-12 01:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c3e0687-6d31-3a36-b6d3-ea3784328f08 | -19.7512 | -57.995201 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ec8b3956-d219-32c3-b4f3-a17052af9b94 | -19.7208 | -58.046501 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2174562a-2077-3ce4-9c24-bc2cf24b20f4 | -19.798401 | -57.9758 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| db4a15c5-5d5f-3758-abf3-5b2f205fc481 | -16.881201 | -51.644798 | 2025-11-12 01:18:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c84d093a-1c83-3456-9508-ef0b51a3dae9 | -2.8622 | -51.477901 | 2025-11-12 01:18:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 475ff241-1555-342b-83ec-83fb4de366fa | -21.166201 | -48.696602 | 2025-11-12 01:18:00 | METOP-C | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c654e1f6-8e02-3058-bb54-fdfb276528a2 | -20.8867 | -50.096298 | 2025-11-12 01:18:00 | METOP-C | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f44a4ba0-5c0b-3d16-b563-89e1939fdd27 | -20.211901 | -56.6105 | 2025-11-12 01:18:00 | METOP-C | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6063ab0e-cf4b-3755-ba48-f8aff6dccaed | -19.8444 | -58.001099 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ac9f0dd3-5cef-32cb-a5c3-981b08a56b4f | -19.8001 | -57.984299 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| abe5e24d-0cd6-3ce6-b414-fe876471db36 | -19.846201 | -58.009602 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1c80a08a-ae73-3670-b741-7c598d026b8e | -21.414301 | -48.649899 | 2025-11-12 01:18:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| df533b26-9efc-3cb2-8799-6da3883b6483 | -4.1081 | -48.041199 | 2025-11-12 01:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e91ab6a-4b39-3ce9-9843-99fc8e8cd016 | -2.8719 | -51.475601 | 2025-11-12 01:18:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee137b1-06f8-337f-9284-714b071542bf | -19.7789 | -57.980099 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5257de40-f471-35eb-a116-3ca1507b216c | -19.719101 | -58.037899 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 129fa5c9-dd97-3539-ac37-e56168aa5297 | -19.753 | -58.0037 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 88b32e00-8d09-3475-a2df-cf8a745808ad | -19.7771 | -57.971699 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1e389a97-4a27-38bc-a258-7bdc6f183e8a | -19.711 | -58.048698 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 668609e2-65dd-37d1-9bd3-752e5c84ad2b | 3.1362 | -60.712101 | 2025-11-12 01:18:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a6fe5f7d-9fd3-3e98-b1d6-9c20044f21b9 | -20.898899 | -50.103699 | 2025-11-12 01:18:00 | METOP-C | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3afd4d08-7c24-367e-b82c-ae3ddbb04fee | -21.1728 | -48.681702 | 2025-11-12 01:18:00 | METOP-C | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 52209d54-3411-3902-8e11-28f243d295a6 | -19.8099 | -57.982101 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5a16658c-a4bc-38db-b39b-e2613626713f | -19.7449 | -58.0144 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| af9ee4a3-acc5-3876-82c2-e683d21f3eb7 | -21.4112 | -48.637901 | 2025-11-12 01:18:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6726cd27-f50d-3f88-a09e-97f890b56a73 | -9.4437 | -59.206501 | 2025-11-12 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 184fe15e-46ca-3d78-9101-a892a62322bd | -22.7836 | -51.6758 | 2025-11-12 01:18:00 | METOP-C | LUPIONÓPOLIS | PARANÁ | Brasil | 4113809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6c73cb25-17db-3442-988f-ab5ab14ba18d | -19.788601 | -57.977901 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 92ffd7b1-c331-3532-92d8-36c994065bf4 | -19.761 | -57.993 | 2025-11-12 01:18:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8ef90692-5742-3e14-b844-c953ccd8cbe4 | -9.4421 | -59.1991 | 2025-11-12 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 525867e6-cda0-3021-aa9e-9aa37eabdb8d | -16.878901 | -51.635502 | 2025-11-12 01:18:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d6822bdf-dd6e-39e0-9092-a0c956e8854b | -23.5991 | -49.015701 | 2025-11-12 01:18:00 | METOP-C | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| db97c2e4-99ff-31fc-95fd-e39ca58a9c0a | -4.0956 | -47.990898 | 2025-11-12 01:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd78bd84-0922-3b44-9d08-014aee393f1a | -2.7946 | -52.9701 | 2025-11-12 01:18:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04d41da3-2a37-3f2a-8357-d0ad4640ecd1 | -2.8586 | -51.4627 | 2025-11-12 01:18:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a48ed62c-8db3-3e6c-b3a6-93aee0b9dabc | -4.116 | -48.0352 | 2025-11-12 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ee81fd1c-e356-3b89-9608-80feede33fe3 | -4.9456 | -43.7194 | 2025-11-12 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 01806ad4-3704-3ae5-8e6d-8c7a7a9f9712 | -4.0974 | -48.0361 | 2025-11-12 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 81b68ce8-b11c-374e-8392-a16388770de0 | -4.0977 | -47.9927 | 2025-11-12 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 907d9227-ac6f-335b-a3b6-59bec6235ad8 | -4.1161 | -48.0136 | 2025-11-12 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 263.2 |
| 277ca3d9-87ab-35a4-9083-72ebd0f1841e | -4.9643 | -43.7182 | 2025-11-12 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| fbde6cbe-5dbe-3294-aab5-99efe78a2dd0 | -4.1162 | -47.9919 | 2025-11-12 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b615642e-5045-3a9f-8d9c-b8c93bc86bba | -4.0976 | -48.0144 | 2025-11-12 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 344.9 |
| f9ed096a-b71e-3aac-9cd0-011482b98344 | -4.9456 | -43.7194 | 2025-11-12 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 4bd47e25-4fef-3380-9b42-5fab9d05dac2 | -4.1161 | -48.0136 | 2025-11-12 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 252.2 |
| 0f914b56-38c6-3bec-9909-5d38fd421d80 | -19.7223 | -58.0491 | 2025-11-12 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| f371a23c-fcd8-394d-bcbc-8951822a64a3 | -4.9643 | -43.7182 | 2025-11-12 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 7dfed544-9cf8-3a40-b4ec-194da4c17416 | -2.6299 | -49.2045 | 2025-11-12 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| a4f9ec81-1731-3342-b909-e3c3d4c5e779 | -2.6484 | -49.204 | 2025-11-12 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |


[Clique aqui para ver as próximas entradas](README5.md)
