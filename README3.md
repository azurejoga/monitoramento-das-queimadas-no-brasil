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
| ebaecb68-e270-387c-be58-7596c739a4e0 | -3.7181 | -47.205299 | 2026-01-06 00:41:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b60bf7e-d6f6-33e9-801e-a37fcdd3077e | -2.5301 | -47.822498 | 2026-01-06 00:41:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d57313f-5ab5-31dc-b75d-3bc51f1082cf | -2.0979 | -53.511902 | 2026-01-06 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dfc63ab-a5c6-3ae7-9ff2-067473d73757 | -0.0923 | -51.266998 | 2026-01-06 00:41:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c3460682-b9ee-361e-b58b-b65491fb3023 | -2.6524 | -45.634201 | 2026-01-06 00:41:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 752f8884-0e3d-3a8c-b694-2723df750165 | -2.0067 | -53.201099 | 2026-01-06 00:41:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3e3ce49-7f99-3753-8ee2-d143eeafbbb5 | -2.164 | -47.889702 | 2026-01-06 00:41:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6267c2d8-c4e1-3b24-bc93-f3ca2d61fb83 | -1.8224 | -54.1549 | 2026-01-06 00:41:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56e42893-1f29-3a75-830a-7e88ad70b46b | -26.20794 | -51.3377 | 2026-01-06 00:45:00 | TERRA_M-M | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 6a93326a-f31e-37b2-99a3-ad8904a770b5 | -19.15465 | -50.7036 | 2026-01-06 00:47:00 | TERRA_M-M | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c38436b9-8c73-39f5-9926-d8601f5c01df | -20.30961 | -50.5967 | 2026-01-06 00:47:00 | TERRA_M-M | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| ee5d5a25-5bce-3993-957c-7c98f7ec48f2 | -22.49595 | -46.94614 | 2026-01-06 00:47:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 51be960e-b87a-3cb5-a037-a4070aae3533 | -21.31479 | -48.61231 | 2026-01-06 00:47:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 28998263-1d3e-345f-a53e-648ddeb3060e | -20.5138 | -58.00093 | 2026-01-06 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 6f09c43d-68ac-3058-8c97-878d3425743b | -21.02149 | -48.51074 | 2026-01-06 00:47:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.5 |
| 925a1bfe-8a7d-3db5-a142-0d11403de42d | -22.4932 | -46.9301 | 2026-01-06 00:47:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 0409043c-9fe2-3c5d-a3b3-e24661647b62 | -21.02738 | -48.5039 | 2026-01-06 00:47:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| dc270c93-ad61-3492-bcc9-d44e7ef33496 | -22.02827 | -56.30173 | 2026-01-06 00:47:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9ab31537-d965-306f-8aaf-806808c8a80f | -17.90895 | -54.13839 | 2026-01-06 00:47:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da15a9d2-080c-3dd0-b2db-59ddb43689b4 | -20.98655 | -54.48066 | 2026-01-06 00:47:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9838e2cf-6a47-3b0e-b371-c1fb4fbdc49c | -21.32395 | -48.6176 | 2026-01-06 00:47:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| e62f17a9-8c5d-39ea-8b12-3bf68b0f150a | -20.52529 | -57.99951 | 2026-01-06 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.3 |
| 792aead9-95cd-3c24-a3f9-61f98d7b6403 | -21.29829 | -48.57518 | 2026-01-06 00:47:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 63414bc6-d1bc-3b3b-823d-8f4bf182e5ac | -20.99648 | -48.48806 | 2026-01-06 00:47:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8f0a827b-e5e1-32b9-b468-53409168df44 | -21.53557 | -57.53901 | 2026-01-06 00:47:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 1830fd28-a332-39c5-98c7-021a4e4c578e | -17.65261 | -56.46223 | 2026-01-06 00:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 34ec7c53-f3fb-306d-be21-eb7ff7869a2f | -16.36081 | -57.3091 | 2026-01-06 00:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| f77d1537-1258-3586-87a4-b04536e3262d | -17.6512 | -56.45058 | 2026-01-06 00:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.0 |
| 066fcea2-40fe-37a1-8c2a-1157f52f42bc | -16.0765 | -56.5872 | 2026-01-06 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 02351103-c857-3a2a-965e-f2185ae55c54 | -2.5238 | -47.8115 | 2026-01-06 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4c3531ab-bc12-3519-b321-b5eeeed638f2 | -3.6962 | -43.4432 | 2026-01-06 00:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 22ab8177-6762-3d04-954c-1dbb70d53762 | -22.5059 | -46.9374 | 2026-01-06 00:50:00 | GOES-19 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 110.6 |
| d7b0f4cb-47c1-317d-b1a9-c935012607cf | 2.5442 | -60.3563 | 2026-01-06 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 26bbe2b0-f00f-3943-b057-ff79526c9ae8 | -20.5077 | -58.0066 | 2026-01-06 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.7 |
| ca9aa63f-b7d6-34ef-b678-69a6a9f37b24 | -2.5238 | -47.8332 | 2026-01-06 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 5dcd8280-93ef-3b0a-b04d-8b0c7585eeeb | -20.5279 | -58.0039 | 2026-01-06 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.4 |
| 19376489-e32f-3d47-bbae-d722b47ec806 | -2.6431 | -45.6499 | 2026-01-06 00:50:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 51e29f9f-b8dd-37e8-9c71-ab4937ae6765 | -2.5423 | -47.8327 | 2026-01-06 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| cff134c3-afaa-37c7-be85-b77a6fd94e1f | -1.36012 | -49.41845 | 2026-01-06 00:52:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| f1aaba98-2f36-3bec-b535-43ce6befc311 | -2.53817 | -47.84056 | 2026-01-06 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 3dfa1569-7801-30cd-beb9-04a6c043fb11 | -2.44617 | -53.82152 | 2026-01-06 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9a628976-70ce-3632-be49-fc0523fd0626 | -1.14396 | -48.10894 | 2026-01-06 00:52:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| ce097dc7-0a64-37c6-a13e-da3511a78c04 | -2.51428 | -47.80782 | 2026-01-06 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| cfea7bff-f8f2-33fb-8cec-3557370e175d | -1.60196 | -53.99723 | 2026-01-06 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| eb4598b4-dca8-326a-8f18-78ae53dc880b | -2.00367 | -53.21136 | 2026-01-06 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e7d55fa9-ab4f-324f-a93c-778c07bb2611 | -1.35208 | -49.413 | 2026-01-06 00:52:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 83c357e3-28db-3480-8f82-4370ecd89d87 | -2.51889 | -47.83822 | 2026-01-06 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 8f828337-b989-394f-bf26-896fc1f8ab22 | -2.80816 | -54.43981 | 2026-01-06 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3cff4c73-c02c-3dd9-bbe2-3d3ede320ed9 | -3.18123 | -51.09488 | 2026-01-06 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e2e18868-859a-3ed8-a272-f34b8a509a1a | -2.80951 | -54.4496 | 2026-01-06 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7fec3e2a-63a7-31c2-9603-018318e6ec09 | -1.81996 | -54.16817 | 2026-01-06 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 0b8b485a-47fc-34b7-8f35-5e8a27133b81 | -2.81455 | -54.82168 | 2026-01-06 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| af315559-48d0-3f57-8b32-bacac7ba4206 | -2.51842 | -47.81261 | 2026-01-06 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b3502cdf-cd7f-3267-9d35-45ab4b55cd22 | -2.53428 | -47.83582 | 2026-01-06 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| c71197e1-6050-383e-ae56-e576abe5876f | -2.00362 | -53.21755 | 2026-01-06 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dc401393-daba-36ad-9f9b-b0d8fb15205c | -2.0963 | -53.5098 | 2026-01-06 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e819d95b-87b6-3683-aff4-06ba7c782dcb | -1.60046 | -53.98656 | 2026-01-06 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c99321cc-13f0-336d-af51-30b50f1e9874 | -3.33243 | -52.70236 | 2026-01-06 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6537c4be-b02b-3e44-a4b6-e7f5fde36b02 | -3.17675 | -51.08992 | 2026-01-06 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9b915e9a-3f7b-33f1-8653-c923d62428a5 | -2.53384 | -47.81013 | 2026-01-06 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 97c02c05-cb07-3ae9-8906-bd25f1d22d3a | -2.5228 | -47.84309 | 2026-01-06 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| a877c7ba-22e3-3f5e-8ca8-3654872b8099 | 2.76137 | -60.62687 | 2026-01-06 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 81cdd03a-d66b-33e7-9713-b3496267889b | 2.54648 | -60.35173 | 2026-01-06 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.6 |
| ddb5d6d5-95c8-3411-bcec-f98e8d5d9bda | 3.10481 | -61.24448 | 2026-01-06 00:54:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6fda4bac-0d3e-33fa-b45e-da7a89bca14e | 3.5472 | -61.01705 | 2026-01-06 00:54:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9445fe12-455e-38cf-ba08-cd9dc239765e | 2.54476 | -60.57253 | 2026-01-06 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 987d0d73-6eae-3a99-88af-f008877cdf98 | 3.16456 | -60.96684 | 2026-01-06 00:54:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d35e6a9c-ae05-3099-85df-5aad4200acfd | 2.54496 | -60.36236 | 2026-01-06 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 534a778f-ea7d-3c7d-a430-a61984b16b5e | 3.54561 | -61.02266 | 2026-01-06 00:54:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 080297d3-ec36-3ba4-9757-ad2770def1ed | -2.6431 | -45.6499 | 2026-01-06 01:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 1e9b5d05-56c3-392d-b462-f219a524462f | -20.5077 | -58.0066 | 2026-01-06 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.5 |
| ad33e0a0-d15e-37c9-8d0b-ca4f48fcc5d2 | 2.5442 | -60.3563 | 2026-01-06 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7ef88ef6-83c0-32a2-aa73-19cd1c415c25 | -22.5059 | -46.9374 | 2026-01-06 01:00:00 | GOES-19 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 79bae7a1-de55-3368-b5f6-938adef5698c | -2.5238 | -47.8332 | 2026-01-06 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| b5bf2d69-27dc-31e4-85c6-ee1699b3642f | -3.6962 | -43.4432 | 2026-01-06 01:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| ed426e39-74f4-3dfb-9e79-74340e2fb0af | -2.5423 | -47.8327 | 2026-01-06 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| b3837684-f89b-38ba-9b77-b6f0bc97e34d | -2.6617 | -45.6493 | 2026-01-06 01:00:00 | GOES-19 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 43.3 |
| b5613349-5c5e-36f4-aee6-20f38cfca8e2 | -2.5238 | -47.8115 | 2026-01-06 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e7b9c452-5496-3cbb-9e52-cce700918f53 | -20.5279 | -58.0039 | 2026-01-06 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.9 |
| fbf814ab-fec0-382e-a438-64d4f3c5990a | -2.5238 | -47.8332 | 2026-01-06 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 1a72d1ec-9154-3f88-ad80-e2422c3c7fed | -20.5077 | -58.0066 | 2026-01-06 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 4eaa239c-c296-3883-bd5a-24476c8a9adc | -2.5238 | -47.8115 | 2026-01-06 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| fde4ba38-1ceb-37d5-acd5-789c834d4b1e | -20.5279 | -58.0039 | 2026-01-06 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.7 |
| 900864cf-e01a-3c41-82cf-de845f09eaef | -2.5423 | -47.8327 | 2026-01-06 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3314cc65-73e9-33a5-b9e9-2f2963122561 | -3.6962 | -43.4432 | 2026-01-06 01:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 07a24215-2293-3230-b096-d179093c553c | -3.6962 | -43.4432 | 2026-01-06 01:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| cf168c15-68c8-3132-af11-37fbd8b56c9f | -4.3491 | -46.3364 | 2026-01-06 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f64c7af3-91bc-3e4b-8f0e-885e225d5645 | -20.5279 | -58.0039 | 2026-01-06 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| f8f73eb5-17ae-35db-b96f-7dc9802fb9b7 | -2.5423 | -47.8327 | 2026-01-06 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 40d1c4da-f988-349c-8c6a-932658b946a9 | -2.5238 | -47.8332 | 2026-01-06 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8713bb77-2fff-3292-af9f-9ab646ec9def | -4.3492 | -46.3142 | 2026-01-06 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| fd0bb53b-0aca-3659-8825-0b440366e6a2 | -20.5077 | -58.0066 | 2026-01-06 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 35ce4d48-027f-3dd4-8375-03abce8c711e | -4.3492 | -46.3142 | 2026-01-06 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| faa2dd1f-664c-3e2f-bc36-7808fadfe0d1 | -4.3491 | -46.3364 | 2026-01-06 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 34fe4824-2b71-3b12-897d-b3c52f0b3cc2 | -20.5279 | -58.0039 | 2026-01-06 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.0 |
| b6e73d94-8beb-3bf2-945b-761f9a77271f | -9.5163 | -35.7909 | 2026-01-06 01:30:00 | GOES-19 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |
| 1ef45374-aa38-39e3-bc0c-aa618b7277b7 | -3.6962 | -43.4432 | 2026-01-06 01:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 4ceb28d7-d30b-3e5d-8f53-25ab4868dc7a | -20.5077 | -58.0066 | 2026-01-06 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| ce79eca4-2286-3e8d-974c-c08d9fb9bdbd | -9.5168 | -35.7636 | 2026-01-06 01:30:00 | GOES-19 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 137.3 |
| d644c70e-23f8-38a0-8315-2b82769ece0c | -9.9319 | -36.2059 | 2026-01-06 01:40:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 135.9 |


[Clique aqui para ver as próximas entradas](README4.md)
