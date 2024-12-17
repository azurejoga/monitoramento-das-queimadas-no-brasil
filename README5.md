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
| 39dab746-9290-3e23-aace-3ca86c959525 | -3.2969 | -53.3547 | 2024-12-17 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6a628e8f-067e-386c-97ce-0ba6d30fc456 | 4.4435 | -60.9846 | 2024-12-17 01:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 4644a1c1-c8ca-359f-99d4-10c0e1d34cab | -19.1043 | -52.8493 | 2024-12-17 01:00:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 115.6 |
| fcabfcc8-d122-3bb5-8c13-de706a980b35 | 4.4435 | -60.9657 | 2024-12-17 01:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f0a03b0f-6dcb-35d4-9f3b-e61c5cecf8ca | -19.0641 | -52.8561 | 2024-12-17 01:00:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e68a7784-121a-3bc3-a1b2-c9dfa5d74914 | -3.1503 | -53.1762 | 2024-12-17 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 42425966-ceb1-3c0a-bdb4-11e70261bd75 | -6.214 | -46.2202 | 2024-12-17 01:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 35080a5a-3d99-3b34-852e-8537bf056c64 | -3.2968 | -53.3749 | 2024-12-17 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 56702bf9-6790-3d4c-8b7e-f2e6a625fbdb | -5.08 | -43.91 | 2024-12-17 01:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87c09ebf-234a-3184-9a9d-8087cbe4d6fd | -5.11 | -43.92 | 2024-12-17 01:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e636ceee-4ffc-316a-8d18-621f0e1ce0ce | -5.08 | -43.87 | 2024-12-17 01:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d16ec27-ab1a-343b-a434-fa75ac32d211 | -5.08 | -43.96 | 2024-12-17 01:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f8d1446-4a73-39e5-a757-131266866223 | -5.05 | -43.91 | 2024-12-17 01:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9846e9c7-0d36-320d-8c80-afdecc5701ae | -19.1043 | -52.8493 | 2024-12-17 01:10:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 90.2 |
| e81e7d95-a3f3-3f50-a707-585390069c77 | -3.2968 | -53.3749 | 2024-12-17 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9873d402-f171-3aed-8590-5d2ac66d7bf7 | -3.3152 | -53.3744 | 2024-12-17 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1d130821-9755-345d-a992-8ff12d7309a7 | -19.0842 | -52.8527 | 2024-12-17 01:10:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 115.5 |
| b64b577b-67c3-3ea0-b5c9-52ffef88553f | -3.2969 | -53.3547 | 2024-12-17 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4bd1c277-138b-3592-9c8a-d3eda1974f1b | -6.214 | -46.2202 | 2024-12-17 01:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 60aeee14-599f-3af3-ba71-e10b98f71427 | -6.1953 | -46.2215 | 2024-12-17 01:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 406a6f6e-58b1-389e-833a-17c0a8783925 | 4.4435 | -60.9657 | 2024-12-17 01:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 13acfc63-5699-3935-b2ac-4fb7c67500db | -4.7952 | -46.4012 | 2024-12-17 01:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a3185a45-e7c0-3db5-9b83-69d481495b0e | -4.886 | -44.1843 | 2024-12-17 01:10:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d93cd2c6-fc48-3f16-9671-1f344703ac24 | -18.89476 | -56.05344 | 2024-12-17 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 282e32b2-55c0-35d4-bfba-3c94e2ef2ff6 | -19.06489 | -52.86197 | 2024-12-17 01:17:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f86c52d5-6a1e-333b-bd3d-181cc6c63fa2 | -19.0636 | -52.85262 | 2024-12-17 01:17:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 6ae2f9b2-c855-3c3e-b6c7-83fa563a8468 | -19.09283 | -52.86713 | 2024-12-17 01:17:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 82.8 |
| f8b62460-e090-3424-be8f-b97a2e112ae9 | -19.09154 | -52.85778 | 2024-12-17 01:17:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 3d99b726-a10b-3191-adbc-135635ff17be | -18.90474 | -56.05207 | 2024-12-17 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.5 |
| d36ecca5-4d5c-351e-9efb-51d06163acf8 | -19.07248 | -52.85123 | 2024-12-17 01:17:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b9f8c564-e018-3ff3-b6a6-80395f0f950d | -21.33124 | -56.11657 | 2024-12-17 01:17:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fdf75980-5ba0-3d4f-aa4a-7b3356655bdd | -18.89328 | -56.04153 | 2024-12-17 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.0 |
| e38e9a05-a17c-3c6e-8127-751f0157315b | -19.07377 | -52.86057 | 2024-12-17 01:17:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 66c31e95-05e4-3d3e-8741-816c2d60ee07 | -10.1801 | -36.3232 | 2024-12-17 01:20:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| 557fee54-bb01-32fa-974b-61b545850027 | 4.4435 | -60.9846 | 2024-12-17 01:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ca4e55df-c1bd-3d0b-b638-370410734db9 | 4.4435 | -60.9657 | 2024-12-17 01:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 951f3307-5e14-334b-ada5-4d3bafcd1c7b | -9.5109 | -36.09 | 2024-12-17 01:20:00 | GOES-16 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| a0b4f8d9-143d-3359-970c-5449409ff7d3 | -19.1043 | -52.8493 | 2024-12-17 01:20:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 47943fe6-51d3-3a99-887a-bcd4fe3a5357 | -3.1503 | -53.1762 | 2024-12-17 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ea346afa-a402-34a0-b4b2-d6d5bda97dde | -10.1791 | -36.3773 | 2024-12-17 01:20:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| 19f30853-7ba6-31c1-ab20-f73d86640fa9 | -6.214 | -46.2202 | 2024-12-17 01:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 5a011ee8-321d-31ba-8fe4-d1df7f8a7f42 | -6.1953 | -46.2215 | 2024-12-17 01:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 42ac11f6-ca35-38e4-8cc1-ac7253286668 | -10.1796 | -36.3503 | 2024-12-17 01:20:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 235.9 |
| 68f5a8a0-24b8-3a4a-af63-12a1843598b3 | -19.0842 | -52.8527 | 2024-12-17 01:20:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 102.7 |
| c9439c62-8f26-3037-8c77-7c5627f10697 | -3.3152 | -53.3744 | 2024-12-17 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0dbf91b7-a127-39bf-a3de-b63a5f740777 | -9.5302 | -36.0867 | 2024-12-17 01:20:00 | GOES-16 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 65.5 |
| 74bff376-0e1c-3326-b0f3-bd89606950d8 | -3.2968 | -53.3749 | 2024-12-17 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| afd395c0-995e-3aed-9814-77895706815e | -3.2969 | -53.3547 | 2024-12-17 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 322009a1-e601-333c-81c5-d6b2dce580a8 | -4.886 | -44.1843 | 2024-12-17 01:20:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 26040dd5-2f71-3352-b1a6-b009224b93a5 | -3.15501 | -53.27893 | 2024-12-17 01:21:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 76afc417-da29-39a9-b8ed-d3389ab2ca3b | -1.40454 | -47.46338 | 2024-12-17 01:21:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| ad13caf8-6fd6-370f-b9cb-9c1a2a5c793b | -1.26904 | -53.02776 | 2024-12-17 01:21:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f56101df-a40b-317b-b5d9-9f1afaca22cc | -1.2807 | -53.18396 | 2024-12-17 01:21:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8a5f4eb3-0d5e-368d-a0d4-17c27b09c4bd | -1.4023 | -47.49148 | 2024-12-17 01:21:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| d7a8f42e-6665-3e0a-86ef-a2155ee95bb6 | -3.15079 | -53.17793 | 2024-12-17 01:21:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 06bcf7c1-1ca2-3bc1-9293-ae7a7be74e91 | -0.76175 | -47.76489 | 2024-12-17 01:21:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| c7d34484-ed32-3fb1-8243-ca288c250c46 | -2.92997 | -52.70925 | 2024-12-17 01:21:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7bcf5061-1466-3fbb-88b9-9b02f071e98e | -2.95194 | -52.5707 | 2024-12-17 01:21:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9885f682-6bf1-3ca8-81fa-bb86e7da4562 | -3.30352 | -53.37805 | 2024-12-17 01:21:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| d53bc34d-75bd-3df2-a9bd-78dda3f47089 | -1.28237 | -53.19575 | 2024-12-17 01:21:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 089df739-eaae-3e96-8f89-8587ce41596e | -2.94265 | -54.18129 | 2024-12-17 01:21:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eff7918a-6f5e-3fc0-bc13-e4c490611d11 | -2.08355 | -54.23717 | 2024-12-17 01:21:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 85ea4f94-b0d4-36bf-9155-d98611ba897a | -3.43851 | -53.98223 | 2024-12-17 01:21:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9f5dda7e-77a3-34ec-bed0-d9d40c6ff228 | -3.23471 | -46.78527 | 2024-12-17 01:21:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 4905973d-1a9c-3d8b-943b-5dd44fa7789b | -1.30125 | -52.83002 | 2024-12-17 01:21:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d8bd4476-9d61-3fa3-a51d-29249dccd93b | -2.57274 | -49.40919 | 2024-12-17 01:21:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 95f3dcc6-a6b6-3ebe-a567-d07e495c50f3 | -2.08215 | -54.22719 | 2024-12-17 01:21:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a04ce6c3-2414-30f3-a814-f2fa346e1953 | -3.15235 | -53.189 | 2024-12-17 01:21:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 97c06431-8e61-335c-bb28-7e7f603e8965 | -4.37707 | -46.55758 | 2024-12-17 01:21:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 4da505d4-53ae-3cdc-a9e3-2fdc75da1311 | -3.30043 | -53.35664 | 2024-12-17 01:21:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fa721828-c185-3ff6-90af-48ad904de338 | -3.24712 | -46.81132 | 2024-12-17 01:21:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 3e76733f-e318-3da3-a50c-f20bb6e6883c | -3.49686 | -53.94756 | 2024-12-17 01:21:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b79caffa-e8db-37da-94f8-4ab76a2855e5 | -3.2398 | -46.81952 | 2024-12-17 01:21:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| b710ee1d-05c3-3fb0-ab02-5679d2fd1303 | -1.27071 | -53.03964 | 2024-12-17 01:21:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e8114a62-72da-3132-a688-38c4b85a0270 | -1.93218 | -54.40281 | 2024-12-17 01:21:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 157921ac-799a-38e5-9c98-155d2bec0357 | -3.43896 | -54.05304 | 2024-12-17 01:21:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ac2cc0a5-4d3b-3f1f-8bd4-99993be01d60 | -3.48657 | -54.65396 | 2024-12-17 01:21:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1cda59d4-39c5-3cf4-b33f-a03bef51724d | -3.30198 | -53.36736 | 2024-12-17 01:21:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| c99e159f-e90b-3520-bc78-647aec082985 | -3.4399 | -53.99206 | 2024-12-17 01:21:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c2a3b928-550d-3964-86ff-296b2c9ccdf7 | -2.1422 | -48.04734 | 2024-12-17 01:21:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 78ca5275-cb82-3ecd-9f8b-e762a6796fc9 | -1.30303 | -52.84242 | 2024-12-17 01:21:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 10b5d4cc-1b68-3225-9063-e12bf4cd2945 | -1.40923 | -47.49588 | 2024-12-17 01:21:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| f77acf02-81bd-3600-a013-b7f1b8e1ff87 | -2.93175 | -52.72146 | 2024-12-17 01:21:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5b1bd00f-a886-358f-83c6-c2e7bf8bbda4 | -1.55134 | -53.43201 | 2024-12-17 01:21:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| abf31952-d973-3aa0-b160-015718759206 | 4.45166 | -60.97228 | 2024-12-17 01:24:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 8906886a-b51b-3b38-b80f-075dc05322ba | 3.32392 | -60.62934 | 2024-12-17 01:24:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 891a264e-113a-3f04-9d46-563a23f50e2a | 2.20303 | -60.24697 | 2024-12-17 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f3bba7bd-02b1-35df-b2f0-fcdab6760781 | 4.44166 | -60.97107 | 2024-12-17 01:24:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 77d09a23-5d50-3d44-a194-95d314fb44d4 | 4.44329 | -60.95973 | 2024-12-17 01:24:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 40f15015-9e9c-328e-8569-b1d524cbb9de | 4.44004 | -60.9823 | 2024-12-17 01:24:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 95.5 |
| ed269146-b469-3cc6-9fa8-5ab1da435458 | 4.4435 | -60.9657 | 2024-12-17 01:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b69a10ce-98e2-3e8f-ab43-667fb47b19f6 | -6.214 | -46.2202 | 2024-12-17 01:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 7c88e649-62aa-323b-a688-fc7f7d77b88d | -19.0842 | -52.8527 | 2024-12-17 01:30:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 6a81fabc-50d1-3996-a569-0e62a129d7ab | -3.2968 | -53.3749 | 2024-12-17 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 464bfa29-4533-31cc-acb5-e4f8509f1efa | -19.1043 | -52.8493 | 2024-12-17 01:30:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 525f99a6-a0d3-36ca-b7c1-6b9278a87cbc | -3.3152 | -53.3744 | 2024-12-17 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 69906461-bacc-3000-9a71-cafb44299c87 | 4.4435 | -60.9846 | 2024-12-17 01:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.6 |
| b5490cac-9488-3fe7-870b-c18baab6d755 | 4.4435 | -60.9657 | 2024-12-17 01:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1487e20e-840d-3880-95f9-df6101865ae5 | -3.3152 | -53.3744 | 2024-12-17 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ef9d5cb9-780d-3f9a-a371-2a5e47789ee9 | -19.1043 | -52.8493 | 2024-12-17 01:40:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 90.4 |


[Clique aqui para ver as próximas entradas](README6.md)
