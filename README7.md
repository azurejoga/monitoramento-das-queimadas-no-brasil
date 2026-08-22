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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13027dd2-598a-3ad0-b1b8-1e3e2792d60d | -8.5221 | -54.8007 | 2026-08-22 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 3a1166d7-4a7f-39d5-b3ee-f088ebc39b5a | -3.15959 | -51.10533 | 2026-08-22 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 068c6feb-17fc-3619-8c20-5f7f5365198e | -1.98812 | -56.46878 | 2026-08-22 00:30:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c7aae1ad-b20a-38a3-b56c-2583d2c30675 | -1.93686 | -54.70876 | 2026-08-22 00:30:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c93e79ab-ff5c-3f37-9d01-c5e49a0722c5 | -6.37142 | -62.90815 | 2026-08-22 00:30:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 74e9b7a1-c9f9-3bf5-8966-d4a2445cc23c | -4.9363 | -55.78171 | 2026-08-22 00:30:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 10563b12-49cd-3bbf-b5d3-698bfbec58d7 | -2.89128 | -48.78615 | 2026-08-22 00:30:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| de86a2e1-ba29-38a7-af53-baf29a97acd5 | -2.5032 | -48.12703 | 2026-08-22 00:30:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c45d9758-8696-3a97-9c60-f1e01e130439 | -6.25781 | -62.53499 | 2026-08-22 00:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fa65c17d-9ccc-39a2-ae42-4f22218bb50b | -4.18202 | -49.40125 | 2026-08-22 00:30:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| bea63020-24b5-351a-ad2c-9fb307c9f9a4 | -2.50452 | -48.15061 | 2026-08-22 00:30:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 58b88c90-a30e-3637-a0c1-d8b5adbf9d92 | -2.49992 | -48.12058 | 2026-08-22 00:30:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 98426256-94ce-3136-b378-23977fa655da | -1.9869 | -56.46 | 2026-08-22 00:30:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 53ad52f8-d045-3ec7-8ba6-74087b24fd5d | -6.27079 | -62.53331 | 2026-08-22 00:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d270dd78-d66a-3263-b624-538fbed3b79d | -3.15712 | -51.0886 | 2026-08-22 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b8706f22-d0ce-3f1d-984d-1930de46c677 | -4.53104 | -56.12043 | 2026-08-22 00:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cef61e56-6d4f-3972-b34d-999144013447 | -6.27232 | -62.53852 | 2026-08-22 00:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| c1feffeb-a982-355b-8bd8-ea05b8ec2456 | -2.88908 | -48.79219 | 2026-08-22 00:30:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 23e8e11f-e49e-32c1-b18f-041c929df331 | -3.15136 | -51.09583 | 2026-08-22 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| cf905e50-e9d6-3069-a53d-99d4a9e7e24b | -6.26964 | -62.51812 | 2026-08-22 00:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| ab8cf624-b88d-3e2a-b2ad-d44a1d6ba411 | -1.74483 | -55.24732 | 2026-08-22 00:30:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 005c0d64-76f6-3fb3-98f3-8d469779b1b6 | -2.50758 | -48.1571 | 2026-08-22 00:30:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 57c4ce78-d7f6-3a58-9ff7-f77357417e27 | -6.26827 | -62.51289 | 2026-08-22 00:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 0199a659-6db8-3128-afd1-8bd7f357292a | -6.25668 | -62.51977 | 2026-08-22 00:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 3a06e69d-fd9c-32ee-a2b1-b6e39a9e1389 | -4.94511 | -55.78047 | 2026-08-22 00:30:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 05948c92-9613-341e-a5df-f7165edc12f7 | -3.1537 | -51.11256 | 2026-08-22 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5bbba179-c993-3144-a0a3-acdf41b35cd5 | -6.25934 | -62.54016 | 2026-08-22 00:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 9dcbd5e4-64ee-3440-94ab-ee46ca217ad4 | -4.70302 | -56.03037 | 2026-08-22 00:30:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 76b320e9-8751-37fe-a196-0d7e15422eed | -4.53147 | -54.86464 | 2026-08-22 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 380d3ac8-19a8-3627-8401-33f228277f29 | -6.25531 | -62.51457 | 2026-08-22 00:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 1c69065f-b9d5-3b42-b0d0-8b5d15a8b18f | -3.26466 | -49.52551 | 2026-08-22 00:30:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 1877a55b-0e66-357f-a5bb-c3dc31b0885f | -1.25587 | -55.84268 | 2026-08-22 00:33:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cb4e71c2-782a-3856-b053-77219e5e97ef | -1.42376 | -55.7235 | 2026-08-22 00:33:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7814a2e6-f922-3ad8-930f-07118491a991 | -1.25714 | -55.85177 | 2026-08-22 00:33:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 933a6741-54c0-3c7d-ab90-06637ac51ed3 | -6.2712 | -62.5231 | 2026-08-22 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1a0cbd1f-e1a1-37e9-98f7-895ca8190311 | -13.997 | -53.6853 | 2026-08-22 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 65dfd518-351c-395f-9602-d571f4a20cf9 | -10.2587 | -50.3478 | 2026-08-22 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 40483bc2-e3f6-3029-a0e0-906e5beb1f07 | -2.5042 | -48.1366 | 2026-08-22 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 4be9c266-6274-37a7-ade9-06d741021bac | -8.5406 | -54.8197 | 2026-08-22 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 237.7 |
| 3e35bb5d-7564-3f60-868a-3f4a2ea6a579 | -6.3678 | -54.946 | 2026-08-22 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 8c0858ae-2641-305c-95aa-a88b3bf59976 | -6.3863 | -54.9451 | 2026-08-22 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| b900453e-7f3c-395b-a4a5-1dafc7d8046c | -8.5218 | -54.8411 | 2026-08-22 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 183.6 |
| d9f94c73-ece0-302b-b3d5-827f19631c7a | -6.2528 | -62.5236 | 2026-08-22 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 960f6be8-f3df-3f0b-ac76-95eddd62883c | -6.8188 | -59.6696 | 2026-08-22 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 2c5b2338-ed88-3cb4-bdaa-79991e4b5a9d | -11.4298 | -44.5615 | 2026-08-22 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| a9906473-44c9-39c0-81b4-106367175147 | -10.2584 | -50.3692 | 2026-08-22 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 0ef09cc2-b9f8-3446-931d-35f04fa9dd29 | -8.9042 | -60.5385 | 2026-08-22 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 43c33b0b-b360-3031-92d7-b18e2ab1c214 | -10.2776 | -50.3459 | 2026-08-22 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a9bb60e1-d444-3ee4-922d-3e9600e2ae59 | -10.2395 | -50.3711 | 2026-08-22 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 6eac93c2-b053-30b6-95e2-2395f999edad | -8.5221 | -54.8007 | 2026-08-22 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c4f4f3a0-2e2f-30fe-b904-c638642d415a | -8.8856 | -60.5394 | 2026-08-22 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 2de5ddc6-988e-38b0-8b1b-ca250baaa846 | -8.5404 | -54.8398 | 2026-08-22 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 218.2 |
| e709faf8-3cf6-31f8-96f7-99536f023893 | -8.522 | -54.8209 | 2026-08-22 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 216.9 |
| 893dc35f-730b-3cc5-9e9a-6248b7fc3d26 | -11.449 | -44.5587 | 2026-08-22 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 0594921e-43ed-33e7-9128-fd7351ba9d88 | -16.4971 | -47.9344 | 2026-08-22 00:40:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0f5958e3-4160-3b3f-97f3-573bf3583ca9 | -6.3862 | -54.9651 | 2026-08-22 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 78cd3c3a-030d-3226-9c1e-43e11d5eb336 | -7.344 | -55.6741 | 2026-08-22 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| cf9a2077-67d0-3250-ab4b-fca2e85577ba | -10.2398 | -50.3497 | 2026-08-22 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 296c9635-304b-3126-97f3-69b8d871fc12 | -8.522 | -54.8209 | 2026-08-22 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 244.9 |
| 55364e3c-fa6c-32f5-b39f-0945633f4221 | -11.4298 | -44.5615 | 2026-08-22 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 5a57faa5-13fa-3952-8056-4cc760baf944 | -6.9699 | -59.0658 | 2026-08-22 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 1e9bc4cb-9c81-3e82-8f39-a81554b95c1f | -16.4965 | -47.9572 | 2026-08-22 00:50:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 30da25ab-3b66-3db3-b68a-b95462e94336 | -8.5406 | -54.8197 | 2026-08-22 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 198.0 |
| 9e583aea-5aef-3774-9656-104008900751 | -8.5221 | -54.8007 | 2026-08-22 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 934fe27f-e129-3333-acff-02ba4e5b961b | -17.9613 | -42.728 | 2026-08-22 00:50:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| 1d787af7-e4d1-363c-861e-fc1c1d24d822 | -10.2776 | -50.3459 | 2026-08-22 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| b7dc3d90-dc90-3ed9-a422-89f1cd5398d8 | -6.97 | -59.0465 | 2026-08-22 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| caf227e6-b04b-39dd-8676-9fd06d3ebc99 | -16.4971 | -47.9344 | 2026-08-22 00:50:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 5b37bc7c-1c85-34fa-bd9b-9b11ea5e3e21 | -8.9042 | -60.5385 | 2026-08-22 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 6dbca41e-27ba-3758-9f9d-b4aea013a13d | -6.2712 | -62.5231 | 2026-08-22 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 7597aacb-a533-3446-b9b9-ef9a5f10b89f | -10.2395 | -50.3711 | 2026-08-22 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d8e1e7bd-6530-3444-9f87-9e2a10d9d91f | -6.8188 | -59.6696 | 2026-08-22 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 06857139-acb6-3751-8a05-717d4fd2ed43 | -6.3862 | -54.9651 | 2026-08-22 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 72eec295-3bb3-3824-8063-e36ecce37f12 | -10.2398 | -50.3497 | 2026-08-22 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 234.3 |
| 047d6460-1328-3248-920a-3898374abd9b | -8.5218 | -54.8411 | 2026-08-22 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 150.7 |
| aafc2357-b547-355d-a6f7-296f1377aa9b | -8.5404 | -54.8398 | 2026-08-22 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| c8373c35-5767-3da3-9340-90c40da81e7d | -11.449 | -44.5587 | 2026-08-22 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 5a013031-8d3d-334a-9936-67487ad0c43e | -10.2584 | -50.3692 | 2026-08-22 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 40b9593f-ca74-30a7-8629-e37b4b9e7424 | -6.3678 | -54.946 | 2026-08-22 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f63c5793-b8c4-32b1-a629-7141a44b0d82 | -5.9997 | -57.8054 | 2026-08-22 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| a3cb8f5c-eb11-3e8e-9768-bfca49a0b92d | -6.3863 | -54.9451 | 2026-08-22 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 4160fc43-e6ee-3cc9-88a9-0ec1c0059885 | -10.2587 | -50.3478 | 2026-08-22 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 253.5 |
| 994806a0-da86-387c-af49-6ca3a3c667d1 | -2.5042 | -48.1366 | 2026-08-22 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 72212d12-577f-3106-aa39-2585ef6a1c66 | -9.1722 | -59.4629 | 2026-08-22 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 229.3 |
| eb8b3706-9dd0-30ff-a5f4-3d502242836c | -6.8593 | -59.0318 | 2026-08-22 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b79fff9c-66e5-390f-8462-06ce7bf912ac | -9.1538 | -59.4446 | 2026-08-22 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 9bb855e4-47f9-3926-8536-5bb660160cde | -9.1909 | -59.4619 | 2026-08-22 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 127d1732-8e05-33bc-b95a-3178ec12ca31 | -10.2587 | -50.3478 | 2026-08-22 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 182.0 |
| f406ef27-4c14-3bd5-9525-101c251aacb5 | -6.8188 | -59.6696 | 2026-08-22 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 041f1873-df12-317b-948d-88e72d0d7446 | -17.9613 | -42.728 | 2026-08-22 01:00:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.7 |
| f2c19241-ceae-3321-a02b-ff3ae2316a6c | -13.997 | -53.6853 | 2026-08-22 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 059b2619-fdb5-3291-943c-63a9bbd5a853 | -6.3678 | -54.946 | 2026-08-22 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| bddfdb1f-5530-3cee-896d-5fe5c0069257 | -6.3862 | -54.9651 | 2026-08-22 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 910541ad-bd66-3b8a-b6fe-d18020a65533 | -16.4971 | -47.9344 | 2026-08-22 01:00:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 12adab80-593d-3110-b3ef-a37633bc182d | -10.2584 | -50.3692 | 2026-08-22 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a1113015-86cf-36aa-bb0e-ae5c19431eca | -8.5406 | -54.8197 | 2026-08-22 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 171.6 |
| d8d63a1e-ce90-3292-81b9-e158cac5ee97 | -8.9042 | -60.5385 | 2026-08-22 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f196bc02-dd85-32d6-8be9-f8af0963cfa6 | -17.9754 | -44.3592 | 2026-08-22 01:00:00 | GOES-19 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 978ce21f-f4c9-3538-9b0c-c8445096ff42 | -10.2398 | -50.3497 | 2026-08-22 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| babdba0c-a031-3ac0-8066-0ddcc4db63ce | -9.1724 | -59.4436 | 2026-08-22 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |


[Clique aqui para ver as próximas entradas](README8.md)
