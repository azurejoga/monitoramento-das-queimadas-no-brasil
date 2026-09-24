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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee9a8ac5-151f-3bd8-a452-375f2c5d9245 | 1.56991 | -55.93456 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2600cd0-bfad-339f-94b4-c1b4a2d62827 | 1.60549 | -55.91469 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3da469f-d0bd-3f6b-ac32-7412aaca2809 | 1.57406 | -55.83447 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f77565e7-1f70-35c3-9b70-31b0cc27b794 | 2.76952 | -60.25582 | 2026-09-24 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d57920c-0651-3f74-b06c-73f7b6928fa4 | 1.57353 | -55.83104 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 523fcafd-1841-336d-a90e-b33e707eec07 | 1.6004 | -55.88333 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f32d29c6-ca8c-31c5-9d64-c84c5d3b9f21 | 1.55763 | -55.82642 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69d58ab7-a7a5-3e9e-93e6-c9706b5977a3 | 1.61202 | -55.92068 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f94db64-3720-387a-8eea-08c526f9363d | 1.56161 | -55.82623 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd8fab44-2154-3eba-9593-4b134ff97832 | 2.9028 | -61.2394 | 2026-09-24 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 265bbd66-0ef4-37e3-8cc0-9af3e402bd33 | 1.57196 | -55.92758 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bf15ac8-e842-3590-b799-5b8ddcdc9b44 | 2.76557 | -60.25645 | 2026-09-24 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6108db29-a8ee-3850-9899-bc263fe106d1 | 1.61425 | -55.93448 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a42543da-9127-3b4c-9338-fb680bf9d911 | 1.57562 | -55.8339 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8318df5-bb68-3b73-909c-0e299db67b23 | 1.56962 | -55.83141 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8fb6498-2fd9-3427-b508-06d26bd4c85b | 1.5631 | -55.8257 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80d3e458-8cda-3d43-8104-a86b429e708c | 1.57251 | -55.93103 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1042a9f8-373a-32de-b979-d5c5709e2dad | 1.56757 | -55.82864 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c003b0d7-a075-3e58-aac4-dcbb465be1a3 | 1.7727 | -60.23616 | 2026-09-24 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49581219-d626-3cfc-8b38-53ad505c8bcb | 1.56934 | -55.9311 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a0906b9d-acc2-3908-883c-27e379a920b3 | 1.6038 | -55.90427 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c6af1a7-4be2-364c-8b98-a6ad1a1e7580 | 1.60097 | -55.88684 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f85a873-0ddb-33f7-b0ef-47cdfe7ac4b6 | 1.57618 | -55.83736 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44b6a829-d328-3732-87b4-97007029b435 | 1.60153 | -55.89033 | 2026-09-24 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dede9198-e2e5-392f-b884-2e65df9249a3 | -3.71376 | -54.20497 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c8910477-c130-3e8a-abe8-28ffa7642e47 | -5.80203 | -57.53372 | 2026-09-24 05:48:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5aa82c11-dc1c-321a-8956-91d732e401d4 | -1.62676 | -54.91242 | 2026-09-24 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0160b09a-7b23-374a-a559-5e5d92cb03f1 | -1.27436 | -57.03323 | 2026-09-24 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c22a95f1-7e02-3ebf-8256-7700955276c2 | -3.73645 | -59.42556 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34dfbbe3-ab00-3cb1-95b6-46de9c5626ff | -3.68585 | -60.56607 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ae77cfe-3ed6-34f5-9baf-f937150c0319 | -3.14236 | -61.38985 | 2026-09-24 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 727d5261-fda8-36d9-9084-ac0269eed9eb | -3.85841 | -58.8909 | 2026-09-24 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f7ca938d-f461-3698-a65f-8386ac4ac2fe | -3.7469 | -59.28841 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01ef76ba-adfc-3300-8083-c63a9fd865ea | -3.68526 | -60.57008 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fd06a16-a076-32c0-b134-fa884f90dcc6 | -3.71505 | -54.19983 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0488eba1-477e-3b02-82c0-47ab8bfc4e33 | -1.22158 | -54.55753 | 2026-09-24 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11b45b1e-97ce-3584-a7cc-16d9d431ea10 | -3.70858 | -54.19849 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c8932d3-42e3-3a57-a975-9ffce88532fa | -1.84437 | -54.71863 | 2026-09-24 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c4be0a84-6f51-31ab-ba08-dd6b1a0bdd3a | -5.77301 | -56.52543 | 2026-09-24 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 492ac426-9553-35a1-8730-ed791604935b | -3.56803 | -59.45555 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5112a49-3d6f-3be2-b38d-29c21fe98c28 | -2.8596 | -60.91484 | 2026-09-24 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04a1f43a-8c44-3b6e-abc6-55f19cdd39d4 | -4.47704 | -54.97019 | 2026-09-24 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3f13c2e-fa15-3b0a-8408-3f14245dce28 | -4.07177 | -59.86484 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49b50149-a3bb-38fd-91ac-b88d1260febc | -3.16549 | -60.09842 | 2026-09-24 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0785c18e-97a1-3267-8136-691538221dd1 | -4.47326 | -54.97169 | 2026-09-24 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fc4dee3-1ff3-3744-b6b2-f3840e2ea079 | -1.82527 | -55.33703 | 2026-09-24 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cded93f-9502-3d0c-8a36-f179212fd7e1 | -5.42109 | -60.2497 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f74cb0a-a781-318c-8f8b-7f292932453b | -3.08471 | -61.16447 | 2026-09-24 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 348b2b53-3412-3bad-80de-47e12b276086 | -3.21522 | -53.37209 | 2026-09-24 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce32c056-648d-3755-a270-af35ffb453d7 | -1.9219 | -58.26679 | 2026-09-24 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e515bc3-4e82-3a15-bbc1-d07d8b98f2c9 | -2.89399 | -54.08805 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dbc44f3-97df-3cec-abff-5ee41c856898 | -1.91872 | -58.26614 | 2026-09-24 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2d64d0a-899f-395a-acaa-6ebe1c0d0a87 | -3.44625 | -60.57667 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6df2719e-9148-3c1b-a7a6-2c01a2ee824c | -3.65266 | -60.61407 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aaf9cd80-5287-307f-bbfa-570d8271e3db | -5.41482 | -60.21521 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07254b3b-914b-30dd-a901-44991ca971a9 | -3.67804 | -60.58941 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cedf907-eb83-3dc6-83a0-5dbdb915e5e0 | -3.68704 | -60.55802 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a4fb822-3128-3947-b38c-c04b8fbd6ac2 | -5.3748 | -56.05301 | 2026-09-24 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8977e120-14ac-3f6e-b832-0c46acf42964 | -3.91666 | -59.66936 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb39b154-7618-335f-bc7e-f19cfaf6e7f9 | -2.83321 | -60.22953 | 2026-09-24 05:48:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7219e28e-fb5e-3972-967f-fc5e30e092ee | -3.68883 | -60.54594 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 201e7933-f544-3012-95db-3c389e74ced3 | -3.9033 | -60.5876 | 2026-09-24 05:48:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c253d131-bbff-3817-bec0-9f1124e6fbff | -5.14681 | -60.36717 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b43e2a5a-529e-3ac6-8eda-29db2672d7cd | -1.27339 | -57.0397 | 2026-09-24 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3f9e0fc-2367-34b9-8331-45a4d37a57a4 | -5.59802 | -60.2028 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a04857e-ac02-3f13-9712-1274c26c9832 | -4.26018 | -55.76316 | 2026-09-24 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 390acce2-8c52-3668-84a9-24f753dc9a0d | -1.6254 | -54.92149 | 2026-09-24 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bcf526a5-b5e7-3fa2-9a4e-a677813aa85b | -3.68467 | -60.57408 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 889789b4-a742-37fd-8a79-30b022011062 | -3.9631 | -59.35014 | 2026-09-24 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 767c68c2-e2e1-37cb-8514-4437e7e88be3 | -3.76966 | -60.73115 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 620c2564-5e39-3741-a400-832b4423d3bd | -4.06323 | -56.23073 | 2026-09-24 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 129e77f7-660a-3eed-b288-85617da1f3fc | -5.22089 | -60.05021 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b504e29-346e-3ad5-9d30-ed1e1d5bb525 | -3.14288 | -61.38634 | 2026-09-24 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69ce7f93-8e28-30d9-9032-47f0f3c9dd0f | -5.83534 | -53.85813 | 2026-09-24 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0a5699c-1ba8-35e2-b853-8533be345693 | -3.71455 | -54.1993 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49060251-25c7-3fd8-94f8-024c6bd1e2d1 | -1.21592 | -54.55616 | 2026-09-24 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 062924e8-a04e-39bf-9129-94fafc892081 | -1.84411 | -54.71863 | 2026-09-24 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1ae1f2dd-c478-357a-9d1a-68f497488433 | -3.72025 | -54.20615 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4e3d55e-5203-3324-b113-1105e11ccf28 | -2.83135 | -60.22742 | 2026-09-24 05:48:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80cfda49-479e-3a73-bfef-0dfbc7df4969 | -4.06426 | -56.22839 | 2026-09-24 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40e33858-ec47-34b9-8533-4035b1759bd5 | -1.28009 | -57.03085 | 2026-09-24 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50de2610-0ee2-3f28-b0ec-fdef97a8f1fb | -3.96381 | -59.34524 | 2026-09-24 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 85d7abbe-29fc-3945-ba4b-78026b4da8a8 | -1.82736 | -55.71331 | 2026-09-24 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e02c2f70-fb7e-3e54-b5fc-b5c2a8b5e709 | -3.70889 | -54.19207 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80ff65b6-c984-3a5e-a73c-5afc1d96b1b2 | -5.42386 | -60.24869 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c238f1b8-130c-3ce1-83e9-c5768febc9e0 | -3.18116 | -61.10464 | 2026-09-24 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fea5ee89-7cbc-3509-8c87-1145f8b1f216 | -5.42557 | -60.25036 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46be3ca4-7c38-3b2b-bbd4-c0901f9b1140 | -4.22237 | -63.08168 | 2026-09-24 05:48:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0f55b2d-0cc2-3ee6-a6b3-80fbe43bef62 | -3.68764 | -60.55399 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27f77900-cf02-3f58-ab92-223b4f17177d | -3.17047 | -60.09489 | 2026-09-24 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0af7f7f-1973-32af-94ec-f5e68c94c7f4 | -5.77358 | -56.52125 | 2026-09-24 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a9e8c42-aefd-3f85-9969-6fe7c5545925 | -3.54739 | -59.94813 | 2026-09-24 05:48:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d565af42-9df0-36f7-9480-d013087cfdf2 | -1.21672 | -54.55106 | 2026-09-24 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c55c4e5-d9f2-3fda-847f-0e439460263a | -5.10809 | -60.25842 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 80ff0a3e-e0d5-34f9-ac88-0a553f00f0a5 | -3.70778 | -54.20398 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6c810b0f-4675-3375-869a-312d552b29ca | -4.52728 | -54.97815 | 2026-09-24 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1560b19-4069-3c36-befb-25abcd8abf90 | -2.89893 | -54.09996 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| bb4dc5c1-9a13-36d9-8a71-7764fa77b068 | -3.08877 | -61.16511 | 2026-09-24 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd8a4734-9510-3087-9175-3c99c3f75100 | -3.44684 | -60.57269 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3dabfe2d-26f8-3be6-b69b-ec341d69f33c | -1.63145 | -54.92251 | 2026-09-24 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README81.md)
