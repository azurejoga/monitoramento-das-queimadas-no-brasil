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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eee2eb09-724b-3601-bd5b-2ab2736793ab | 2.66325 | -60.41178 | 2026-03-05 01:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 45550ce2-822e-3424-be55-6fbd69e2d74e | 1.15297 | -60.88584 | 2026-03-05 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8fc52d5c-fd4e-313d-8b34-9afa00750e0c | 2.78345 | -60.34356 | 2026-03-05 01:06:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 154.6 |
| 11411405-9b8c-30cb-b8ba-45fe0915bd31 | 4.5195 | -60.58017 | 2026-03-05 01:06:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 24641725-8c78-3ed5-b068-8643bcc15f56 | 0.03199 | -60.99788 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 00422818-0857-3ba3-b944-55d275689b6a | 0.47483 | -60.32464 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 07bfbf88-5a52-3f1b-a78a-162bb457169c | 2.31178 | -61.43177 | 2026-03-05 01:06:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 06a5ee72-28c8-37f9-80a6-527e63d4e668 | 2.68735 | -60.30416 | 2026-03-05 01:06:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1e65347d-e5f8-36d5-badb-b507d7e6de77 | 1.50965 | -59.91269 | 2026-03-05 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 0d7c67e8-37d5-3035-8b8e-3de0ca810ee4 | 0.47353 | -60.33412 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b978aeea-ee37-3764-97a6-e9eecb046222 | 0.66299 | -60.29531 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 04c6ef2f-1575-3e71-8011-1ec3590b0cc5 | 2.69884 | -60.68941 | 2026-03-05 01:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 74c31364-d284-314a-8df2-a62ae9483752 | 0.67607 | -60.53751 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0df661f3-d94e-3ff7-925c-018ff30540f2 | 0.04463 | -60.97219 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 39.3 |
| ff62737a-caad-32bb-9f0e-4a97a86b2ac3 | 2.9747 | -61.0352 | 2026-03-05 01:06:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 23.3 |
| e31bef1a-23de-3c30-8b50-b9375518ad0a | 0.81723 | -60.3776 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be3e8366-f59f-3b34-b35e-efd96ae66ecb | 1.94539 | -60.8154 | 2026-03-05 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cc201386-6943-3b6b-80e9-73d32e988a72 | 2.31303 | -61.42278 | 2026-03-05 01:06:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1509529d-8b13-34dc-ae1c-c3ea548182c1 | 0.04215 | -60.99016 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 32.5 |
| e50319b9-8307-3bd2-aa3f-ac9528892329 | 4.53963 | -60.57301 | 2026-03-05 01:06:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8a4f909e-f3d9-3029-91e3-ef99ebc473bd | 0.30883 | -60.46184 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6d60f956-e0c5-376c-8bd7-527e021fc213 | 0.03571 | -60.97094 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 41.1 |
| e835c10d-28a4-317c-aded-bc8752a983b6 | 0.66168 | -60.30487 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 9a5f3a7d-444c-3011-ae9c-72653cd358d9 | 0.07551 | -60.54955 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00ec08aa-f41b-3048-b82a-74402a5d84e1 | 4.51819 | -60.58986 | 2026-03-05 01:06:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 1c14fbb6-7544-3bcc-a56f-9757e83acfad | 0.05231 | -60.98246 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 31.9 |
| f81bf70b-26f6-3757-8334-1011841cb26e | 3.50954 | -61.90314 | 2026-03-05 01:06:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f81841c-552e-3459-98d8-1d316b9fcb79 | 3.39015 | -60.2279 | 2026-03-05 01:06:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c1fe3cc6-9d48-32cf-b5dd-d96ed6a4e252 | 2.78209 | -60.35348 | 2026-03-05 01:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| dde13ed4-bb2c-3269-a092-2b723d1c8ede | 2.95799 | -61.08982 | 2026-03-05 01:06:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2908c920-d9ab-33a6-add9-bed23d542672 | 0.04339 | -60.98119 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 09bbb299-6f49-3efd-8099-bfa3732c1cda | 2.2275 | -60.23039 | 2026-03-05 01:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b05db5ee-a142-34d2-97de-852927cf42ab | 2.97343 | -61.04453 | 2026-03-05 01:06:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1308adb7-22a0-3da4-97fc-26c07ccc8c03 | 3.27295 | -60.73716 | 2026-03-05 01:06:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| de0865b9-c3ca-3072-b1d0-b8b102f08567 | 2.09522 | -60.1999 | 2026-03-05 01:06:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2230a6bb-7ae1-353f-be35-cdf38f2b4cb4 | 0.49572 | -60.5096 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f7b740b0-27ff-3c6a-812f-801c07e16d7a | 2.7928 | -60.34483 | 2026-03-05 01:06:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e0256e50-6826-38c9-bbdf-f88929f7f28b | 3.27164 | -60.7468 | 2026-03-05 01:06:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8d014419-21f1-3ddc-a18f-634cf8d81b41 | 2.92384 | -60.45588 | 2026-03-05 01:06:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d3904747-6030-3818-884e-9bfbca55701d | 0.06123 | -60.9837 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be41d233-f27f-3d60-9e40-f481ad47ff88 | 1.51287 | -59.92923 | 2026-03-05 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bb2e3319-49d6-3e71-a406-f59ad3a09ede | 0.04091 | -60.99911 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 88fcc534-57b3-39d7-b72d-13f2f5560497 | 0.05999 | -60.99265 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d29eae4d-62c8-31b6-a2b4-1aa17ca7e1e0 | 3.18457 | -60.57047 | 2026-03-05 01:06:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.7 |
| cd8411c1-3314-3c6f-bfe0-33662d0717fc | 2.7848 | -60.33361 | 2026-03-05 01:06:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 258.3 |
| 3be01187-f94c-30db-8b6b-4d28afb6b9ff | 1.94158 | -60.37247 | 2026-03-05 01:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 34c75908-87ab-3c02-adbb-622eb969c2c3 | 1.0814 | -59.25586 | 2026-03-05 01:06:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e7898dc6-7114-33b4-aaa5-d7efd03a7e90 | 3.06761 | -60.63156 | 2026-03-05 01:06:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| faab42d4-80f0-3636-a115-b6f28e2382ff | 3.2848 | -60.71912 | 2026-03-05 01:06:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 8b04d785-f14a-39b3-a17e-0e219cb30556 | 1.51556 | -59.90933 | 2026-03-05 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0921ef2c-513e-33d3-a42b-bc40c1348fb7 | 4.52078 | -60.57074 | 2026-03-05 01:06:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e093aba4-7873-3f9a-8829-b83f2a4da9e9 | 0.30104 | -60.45121 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 861d0ed0-9c00-3611-a332-d244f61031fd | 3.02931 | -60.63614 | 2026-03-05 01:06:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fdd8390c-19a5-3081-8a3e-056aa5ec095c | 2.96563 | -61.03394 | 2026-03-05 01:06:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 4aa948ee-5745-3b4f-92a9-63328e358c71 | 0.03447 | -60.97994 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 2dd65580-c3df-310b-8679-2f1427780cef | 2.69075 | -60.69225 | 2026-03-05 01:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 11db632d-3292-3b97-b595-ecf454620a14 | 0.67736 | -60.52817 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6e56d09e-9024-3ec8-8f20-229a8c728550 | 2.79144 | -60.35475 | 2026-03-05 01:06:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a3f5a995-e009-392a-9ead-16ef8d424611 | 2.22884 | -60.2205 | 2026-03-05 01:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 9c7c90c7-63f8-3bd5-b88b-8ab179ef8819 | 3.28348 | -60.72878 | 2026-03-05 01:06:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 3cc8e680-62ff-3f78-a949-63899c86e22b | 3.28217 | -60.73844 | 2026-03-05 01:06:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 29da70cc-ff1b-3859-930a-b4dc8a3a3a95 | 1.51105 | -59.90264 | 2026-03-05 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 85dae652-933a-3c5e-8093-bb4d2e6f799c | 0.76592 | -59.89272 | 2026-03-05 01:06:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 578892c7-370d-3938-8e0e-fd8d11827c81 | 2.78074 | -60.36341 | 2026-03-05 01:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 605b4ec2-1850-3abf-8d84-dda41889a93a | 0.05356 | -60.97346 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a7d6f125-4457-32e3-a60c-ea713e351f3c | 2.96435 | -61.04326 | 2026-03-05 01:06:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 0456c24f-62e5-3a63-816e-da6c43b1fa79 | 2.69207 | -60.68269 | 2026-03-05 01:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a1499ec9-f521-3618-a190-3ca66cd3749b | 3.05837 | -60.63028 | 2026-03-05 01:06:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| be7631cd-b3c0-31d3-aec8-5f97b43e40c7 | 0.07013 | -60.45424 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5f5ab583-c66a-3e49-849b-8cd8ccc96948 | 0.29974 | -60.46055 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 5224aa21-bd4b-3721-8dd5-3fc430384066 | 1.00341 | -59.51142 | 2026-03-05 01:06:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c983905a-6a65-3381-b321-26ba34c2f68b | 3.27557 | -60.71783 | 2026-03-05 01:06:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 464c050d-0929-397e-954f-f673fee17d14 | 0.66037 | -60.3144 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58b21163-8263-3aac-b05b-ee1e93894c01 | 1.15171 | -60.89502 | 2026-03-05 01:06:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 987098ee-160b-3cd9-aeb4-3112360bbed9 | -0.49975 | -64.63567 | 2026-03-05 01:06:00 | TERRA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8dd149de-3505-3611-bf28-6880208ccf87 | 0.03322 | -60.98892 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 17.5 |
| e89e46fb-0278-3548-b199-98deae18c622 | 0.31013 | -60.4525 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c71b2f48-6f4b-3893-99a4-7ef3032f700d | 2.71982 | -60.67279 | 2026-03-05 01:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0d10e082-1a03-337a-bd83-891a912344f8 | 0.67085 | -60.30616 | 2026-03-05 01:06:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3a9e1467-dc6e-31c2-9ed2-9c34cf495f92 | 4.81066 | -60.67974 | 2026-03-05 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a491b98e-807f-3314-a45a-49e4d568915b | 4.96098 | -60.25617 | 2026-03-05 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0abe1df8-bb04-349c-ac27-7188045ea53e | 4.94721 | -60.28535 | 2026-03-05 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ae83d4ff-4efe-3238-b000-c5665bbae44e | 4.94855 | -60.2755 | 2026-03-05 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 109.0 |
| bc2c8a45-a799-369e-9a44-981e8904c38b | 4.95952 | -60.2668 | 2026-03-05 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a8825363-4820-356a-aa69-1207af63ec9a | 4.9581 | -60.27716 | 2026-03-05 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 79bf01dd-fef1-32eb-b880-4d1ef34eb9c4 | 4.96386 | -60.26253 | 2026-03-05 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 20.1 |
| cb47ad0d-3e83-3b8f-85c3-fab85dca4a36 | 0.6654 | -60.3159 | 2026-03-05 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 3d4daf14-7d70-3869-91e3-bd6d1149f33e | 0.6654 | -60.297 | 2026-03-05 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7c6de2b7-94cc-3a78-8506-bd458bbe2b54 | 2.7816 | -60.3338 | 2026-03-05 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 304.4 |
| c18aa1b7-fa62-33ac-91a3-469b04b7a1bd | 2.7999 | -60.3335 | 2026-03-05 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 590ea318-7756-3b7e-819c-9cc465aca993 | 4.959 | -60.268 | 2026-03-05 01:10:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1045ffc6-433b-313a-b8b4-8daa2c72768d | 1.5047 | -59.9116 | 2026-03-05 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f30b99cd-ed14-3a13-9ca7-afc90cbb3eda | 0.0455 | -60.9799 | 2026-03-05 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 26dcd371-7e2d-302b-93d4-4e89f5d79004 | 2.7817 | -60.3148 | 2026-03-05 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 923aafb2-12ac-3970-b75e-fba58e30b9a5 | 2.7816 | -60.3528 | 2026-03-05 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 192.9 |
| c380e29d-d517-37bd-8480-91ff071fd4e3 | 0.0273 | -60.9799 | 2026-03-05 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 90.5 |
| e849ae5d-6ee7-3888-ba91-bc5e2447c4bd | 3.2738 | -60.7432 | 2026-03-05 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 39acb93a-4eee-36f0-a072-b1bccf58c2a8 | 4.9407 | -60.2685 | 2026-03-05 01:10:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| f6491971-4d5a-303e-8c77-4c36fb8d117e | 4.9589 | -60.2871 | 2026-03-05 01:20:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 37.8 |
| c9664ffa-7f09-3638-bd09-0f1532110da3 | 3.2738 | -60.7622 | 2026-03-05 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 88.8 |


[Clique aqui para ver as próximas entradas](README3.md)
