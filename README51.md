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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f89dcdab-0a66-361f-a0e4-5271a5a5853d | -8.34739 | -45.98037 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c731719-7169-3568-8071-ada0198ae3f1 | -8.7214 | -50.082 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 525a69d7-677c-3c69-8407-3aed44f39b53 | -4.29741 | -48.61189 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 822a59c0-4c26-305b-a66b-5a5f82997736 | -10.09041 | -50.3086 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| dc8da3a9-6c00-3706-8925-743603b48af4 | -2.90777 | -54.09319 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dddfd97e-c0b9-36b0-bb71-f1eee9709397 | -10.087 | -50.30807 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2ff47122-2dc2-3360-8ef7-01684701c53b | -6.14209 | -53.0613 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04d217fe-04f4-38c0-8750-75c04a248157 | -14.60839 | -48.94696 | 2026-09-30 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a857d358-fef0-30e8-8a9a-ea45639c17ab | -8.28158 | -54.70257 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e788077-5a7f-35c6-ad21-a3fb6908a019 | -3.41782 | -50.65113 | 2026-09-30 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce9994ed-f3f9-3e8b-b735-6c9ab0085588 | -8.37044 | -45.39583 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f415f546-2b10-37be-8141-cde42dde890b | -3.71391 | -54.22163 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b67326e-a15a-364b-8f3d-7e07a784c249 | -17.12055 | -52.13146 | 2026-09-30 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 893f9783-7449-3df3-8cb2-a2cb6e4e6100 | -10.9014 | -43.85946 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fda834dc-3479-3b87-87df-0ddd9f0473c2 | -5.74596 | -45.17553 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1d3950d-c47e-3118-9ed6-909527a477f5 | -11.40557 | -43.41956 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33d8aa4c-127e-3572-b784-2dd9197f2de1 | -10.70974 | -50.8345 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19287b30-57aa-3306-ab6e-7900186346cd | -5.09618 | -49.06302 | 2026-09-30 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3c84cc7-b35c-31ee-b619-c48b17cae473 | -15.20306 | -46.14831 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc60fbf6-1a2e-386d-b9a5-6f49c763b82a | -8.58921 | -50.41518 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ab2beed-c15a-3524-a6fd-7bb38c73905d | -6.13174 | -53.30124 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 655fff27-0bda-3170-9f41-ca4ccfbc765c | -4.31576 | -48.63015 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa79647d-3b78-33cb-8a69-8f536f62af58 | -11.37535 | -43.3624 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac50b320-f7ec-3c6c-b75c-0598dee46bbb | -3.37951 | -50.8497 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7eea83d4-30af-3100-8cec-c3e342164463 | -10.05956 | -50.89297 | 2026-09-30 04:53:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21e8afe2-c855-3e51-8187-63ff67f1a6cb | -11.7063 | -43.4458 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35ef1e65-2a6d-3f0b-863f-986e0c9768b0 | -3.83252 | -55.7974 | 2026-09-30 04:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eefbeb25-51dc-3611-8788-186f1797ce66 | -11.38848 | -47.43018 | 2026-09-30 04:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df8b2bf0-1d86-3524-8a02-8ef1d28a32e6 | -11.19256 | -44.83864 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 242325cc-4505-3ce3-9ede-62af26d7e868 | -8.86694 | -50.68187 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9fb3561-0d26-3b33-9529-f5b5ed94f60b | -7.82194 | -45.82452 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c616c4f1-fa24-35c6-af90-451cee1bf5d0 | -6.71502 | -45.62903 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5324bf0-5638-305f-93f8-cdb2c4a4483b | -11.16156 | -44.78198 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0331d61a-49c9-34d7-9657-d4b72ca25e10 | -4.80616 | -49.46565 | 2026-09-30 04:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65d9b0fe-f8a7-3294-a2ed-5bd99bd47192 | -4.81461 | -45.64238 | 2026-09-30 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5487261f-dc36-3873-be3e-be65fac0de82 | -7.02743 | -44.63149 | 2026-09-30 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ccaa9b5-d41c-33a6-923f-2827c09d99f8 | -11.18311 | -44.83717 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 559f54c2-c095-3396-81ed-1e763c07aee3 | -2.98878 | -54.91015 | 2026-09-30 04:53:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 387019d3-73d1-3ae9-896a-28a7ab59529e | -4.02442 | -54.2066 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4b0a1d7-9041-3b7f-85b6-5865c160654f | -9.15852 | -45.60099 | 2026-09-30 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c78c291-3e59-3fa2-8872-1203b851ba04 | -11.17987 | -44.83387 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 84109b7a-be86-39ab-8a30-a82a6f5c1586 | -4.11722 | -48.82508 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3b62916b-8634-3df3-9302-27214615bc96 | -3.01729 | -53.87738 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48793274-191c-30bb-85a9-937b86ab0472 | -10.83966 | -48.7039 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53c406fa-cbeb-3e9e-aea8-c6d8de4cdd20 | -9.17097 | -60.79091 | 2026-09-30 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a29e558a-ee3e-34d2-8fc5-ad05cea5d17e | -6.79018 | -55.82269 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d42ce4a-39b0-3346-9c75-b9b33457a57e | -3.42759 | -50.43733 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d574b4b-3dee-3491-bcdf-32d34977c233 | -4.36239 | -47.7707 | 2026-09-30 04:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61d9d30d-31f3-394f-8c0c-1eb826c1c1d7 | -7.83986 | -45.81956 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef7bd706-4f28-3615-9a54-b36dc64110ba | -4.81401 | -49.45951 | 2026-09-30 04:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 445fab98-be51-3703-8845-5df993056b2b | -5.85625 | -51.78968 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5a800f9a-fe01-3344-95d3-5e963537a4b1 | -11.3782 | -43.38165 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66a239ed-72c8-3c0a-8e37-f089ee01db3b | -11.4586 | -43.46265 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 484a6f50-4319-3c7b-8820-7d0a517d42fd | -2.89808 | -54.08257 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d6656fc-e98d-368b-a974-995ebe1dc7d8 | -10.5544 | -50.87042 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f365fa4b-dcf6-3402-a6a3-3cd3da197a18 | -10.51161 | -50.84528 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f1e5e89-7eac-3552-9415-14ef149f5724 | -5.33903 | -46.19226 | 2026-09-30 04:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7451aa12-8049-37ec-bc21-68c065f1cc8a | -5.7588 | -45.17728 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5eff7b40-35d0-3f63-a2ea-6be3bb04a696 | -9.09906 | -47.1675 | 2026-09-30 04:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 574deb0f-b5ce-3599-91bf-d6afceaf204b | -5.71619 | -46.19526 | 2026-09-30 04:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca2e083d-a889-3bd6-b675-25faa33cb430 | -9.70443 | -46.7168 | 2026-09-30 04:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 815726c3-ab3b-3e9f-ab4b-b187ea99f281 | -11.43494 | -43.43987 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15e83ceb-1653-34d6-9956-a38480c9d405 | -8.97578 | -44.17759 | 2026-09-30 04:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4efb81a0-ca74-301b-8f42-f8079388157d | -6.37979 | -55.13622 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56ed5727-edb6-305e-95a8-46fb3da0753f | -7.81791 | -45.82035 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7411be3e-b2d0-3b4b-a94a-acf197379d06 | -10.41511 | -53.77472 | 2026-09-30 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53bc62df-1729-344b-8067-a60d5417a88c | -5.73768 | -45.05494 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 267320f2-10ef-369b-8583-54d637c09cf9 | -8.56176 | -50.41459 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c8a472e3-f95b-32c7-a37a-af280c9e2b27 | -4.29454 | -48.60759 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ab7407f-5236-37d7-b4e8-c15ab33fb00c | -10.81813 | -48.72254 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb6996b8-a92e-30b6-9366-d1db2690bf40 | -6.06788 | -47.28107 | 2026-09-30 04:53:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d2b9a261-c504-3540-a98a-b61437596651 | -11.18535 | -45.1216 | 2026-09-30 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e83b51d5-9573-3418-a52e-179d9a4d174e | -11.39421 | -43.46746 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7ed4113d-00f6-3971-a24d-54a6ca1a45ae | -11.41606 | -43.4209 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6ef93f0-c69f-3bd6-8fd0-39a3542ba4b7 | -11.44499 | -43.44452 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 797f0f80-8768-3cae-944b-deab6a9fddc0 | -2.75473 | -54.67456 | 2026-09-30 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7c8784d-5786-39d0-a7f3-56ded3e372c7 | -7.72057 | -54.78677 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8441b68d-6ec9-3343-a2d8-42a0b552825f | -16.6766 | -41.85078 | 2026-09-30 04:53:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 3a09a5e0-ef78-3727-aafb-4fe33c3dcedf | -11.43619 | -43.43017 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c5c2bf5-295e-32a3-ac7b-de4ab6ac6daa | -3.25011 | -50.80775 | 2026-09-30 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 47f364f6-5653-3103-b6ee-c6ccf0ebf3e5 | -7.17296 | -55.40476 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf3f423e-f613-3ec3-b566-10299a2a278f | -6.74831 | -55.08912 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec351018-06f5-3abe-8a2a-f605d6dc2ed7 | -14.52867 | -48.29787 | 2026-09-30 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 852ab17b-fc73-3a2d-9449-aff15273ac43 | -7.0697 | -46.57055 | 2026-09-30 04:53:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaf83523-c05b-38c7-8213-12bb9df1593a | -5.738 | -45.17038 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09302dc7-4d3d-36f1-a3c4-900cb67832eb | -11.16553 | -44.82434 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9d500a2-6ced-37cb-bc96-64e0d934c4a6 | -8.95093 | -49.79374 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ee6ee94-c619-3e58-a75f-5fca3c152d56 | -10.55777 | -50.87095 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 570ff391-0a79-3e9b-ac9b-13ac4515d3a4 | -7.50213 | -45.82439 | 2026-09-30 04:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1ecfa6f-d3ea-3871-9421-0c1fb29e6564 | -2.89965 | -54.09639 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| f18f8286-6566-34fc-9f45-ec2ef4822eac | -9.7893 | -48.23042 | 2026-09-30 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a4144f88-fc7c-3dd6-825a-61e1a59e91cf | -4.25173 | -51.04765 | 2026-09-30 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4748af02-db92-36a6-a741-ee07e7da0885 | -7.46123 | -54.9971 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6086376b-222c-36f8-b773-2f084d2b4c85 | -11.17094 | -44.82003 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 39e088ea-f846-365c-a46d-743af5740bc6 | -11.67727 | -43.50611 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c112bcd-3e55-34b3-9571-9ec2f2d89059 | -6.19665 | -55.54401 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf240f5b-6a95-34c8-bbff-39b1dcd9d5e5 | -13.56427 | -53.20062 | 2026-09-30 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f203c176-1b8c-3af5-98a6-72a25b2bc9c4 | -7.82668 | -45.82139 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fca7ac5b-5662-3999-a3e9-8990beddac46 | -5.16614 | -56.00943 | 2026-09-30 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dbfd040-df1c-3fa8-bb46-f813a4928fca | -6.74612 | -55.0793 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README52.md)
