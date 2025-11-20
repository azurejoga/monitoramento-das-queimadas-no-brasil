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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96feb912-b7ff-3de7-81da-ebe850bf7d5f | -1.494 | -55.35008 | 2025-11-20 04:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad9068c7-8582-3624-8fbb-4e136e746651 | -2.51539 | -47.80781 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ea8f1cf-6491-3302-aed7-f2794b556ba3 | -2.50987 | -47.8212 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4642caba-fcf9-38a0-917c-db0aab628393 | -7.55293 | -47.58065 | 2025-11-20 04:31:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90356762-545b-3611-bcbe-66f429ed6cc3 | -2.95405 | -51.77342 | 2025-11-20 04:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9788d120-5e95-3de5-a3cc-7533ccf95c8c | -2.95797 | -51.77411 | 2025-11-20 04:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17acfc4f-5439-3350-bf72-ce79a3960ee5 | -3.6787 | -50.48767 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0ae2588-0583-3d34-bf54-728965337bef | -3.67802 | -50.49185 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 569eaa4c-852b-338a-ab1c-95bc1699cd7f | -3.02021 | -51.61099 | 2025-11-20 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be9e77d5-5a64-3795-8f88-7e77692def02 | -2.48167 | -49.32478 | 2025-11-20 04:31:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d66d742d-61b8-39d1-bdc5-16cd334d5be9 | -6.14611 | -53.02214 | 2025-11-20 04:31:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8edc6313-c446-3626-a3ee-31483dda3eaa | -2.9992 | -44.38646 | 2025-11-20 04:31:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29f41300-1bdb-3082-b240-fdcada83207d | -1.13763 | -54.10233 | 2025-11-20 04:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 242aa573-48e1-3c9b-89c0-312645866687 | -2.12464 | -46.19343 | 2025-11-20 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7db479e2-2490-3f16-bca1-8615111449b9 | -3.02099 | -51.60608 | 2025-11-20 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f681ff04-d4e0-3d1b-a323-785964d3c267 | -3.01354 | -44.4575 | 2025-11-20 04:31:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 995c2429-ab36-3bfb-97f0-e8719a9a16ed | -5.84387 | -47.88487 | 2025-11-20 04:31:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9fc4dca8-24cd-33e2-a889-eb490d15e741 | -7.26835 | -48.02931 | 2025-11-20 04:31:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b18e858-3927-32ff-becb-867fe14e0da3 | -1.4945 | -55.34703 | 2025-11-20 04:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 51787e45-65cf-3abc-b887-e1b550b87c9a | -1.35726 | -52.94307 | 2025-11-20 04:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b67f7b7-7c13-3c75-8b6f-90271c31ad6b | -7.95268 | -46.88704 | 2025-11-20 04:31:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87d5a59b-28cf-37c7-a63d-87afbe90bfe2 | -3.23253 | -44.8584 | 2025-11-20 04:31:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 619260de-a59e-3512-bf2b-4c4ee693d54e | -3.23373 | -44.85077 | 2025-11-20 04:31:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c403590c-2a1f-3f03-af03-ba6b16de12f2 | -4.39639 | -48.18277 | 2025-11-20 04:31:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afceac83-c3f4-35aa-92cf-9e3cf6d3ff8d | -4.85532 | -43.98662 | 2025-11-20 04:31:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b95fa22a-9e7e-3b04-b95c-b8572eb3dafd | -4.1024 | -50.06453 | 2025-11-20 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58c025fb-d478-378d-b521-1df838fa1c59 | -4.09888 | -50.06392 | 2025-11-20 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aa7779d8-01f7-35ab-a96e-7d783c5fcc8b | -3.57512 | -39.78259 | 2025-11-20 04:31:00 | NOAA-20 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c7d1ade7-3919-33ab-aadd-060741accbb0 | -6.04922 | -48.15418 | 2025-11-20 04:31:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e7540fe-8f7b-3181-a7b8-1b065c96f7a4 | -3.68231 | -50.48825 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f60c98f7-e6b6-3e76-9c87-e0be5ce1dede | -4.10593 | -50.06509 | 2025-11-20 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bd8f6c8-25da-3c48-be93-a6a32c640bf0 | -4.0288 | -48.88575 | 2025-11-20 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 006cf7da-de52-3801-b883-c32564658369 | -3.04965 | -40.11276 | 2025-11-20 04:31:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f4abe373-fdf1-3488-8ea4-197083cd677e | -3.95878 | -49.03458 | 2025-11-20 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddc55397-2c57-3c9f-a22a-8c21255b5405 | -6.84908 | -35.18393 | 2025-11-20 04:31:00 | NOAA-20 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e80b6983-48b2-3fc4-9134-41f447b2336c | -6.98106 | -47.08968 | 2025-11-20 04:31:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c095ab5-fb72-3f74-afad-ffacc08c9e37 | -0.94041 | -46.8707 | 2025-11-20 04:31:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be0bfd02-2f64-3c15-947b-22e468f3fc1f | -3.67441 | -50.49125 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87ccedee-a4ff-3f3f-bba6-950dc7897096 | -6.15077 | -53.01921 | 2025-11-20 04:31:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a98e490-603b-3e4c-950f-8b879a220077 | -6.48127 | -47.50437 | 2025-11-20 04:31:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 734eb08f-112a-39b0-a5cf-468dcdf71fa9 | -2.5093 | -47.80329 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3618f9aa-3721-3a8f-9633-9f394ba5eed3 | -6.92865 | -46.00531 | 2025-11-20 04:31:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af9ace44-2a95-3f10-b0e8-fe887db05abe | -3.23433 | -44.84695 | 2025-11-20 04:31:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cee229f-4ddc-3873-8f31-02fca3121423 | -2.92826 | -45.05261 | 2025-11-20 04:31:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7d8fac3d-b3af-3216-b863-1367efc2e3e0 | -1.86956 | -47.9606 | 2025-11-20 04:31:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6a05a47-3b44-31e4-969b-043de38127b6 | -2.51207 | -47.80729 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 54c626d7-e126-3804-a5ef-ed9f7e43cbaf | -6.20426 | -55.61402 | 2025-11-20 04:31:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3a095d6-c2f7-3438-ac2a-ee6be83b5311 | -0.71741 | -47.72656 | 2025-11-20 04:31:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c4e4338-7622-39c0-b937-3e22aabf1c81 | -2.25013 | -51.92413 | 2025-11-20 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d650ba4-e91c-378f-b7a9-03ba52705240 | -4.717 | -49.77756 | 2025-11-20 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df9df83b-da7e-34a4-9f02-c379272984b4 | -6.92923 | -46.00155 | 2025-11-20 04:31:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ac07f55b-8fee-35ea-a74c-3159add67dff | -3.01415 | -44.45356 | 2025-11-20 04:31:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b73f1a0a-6311-33b4-9619-5604f7c4af8b | -3.29976 | -53.84045 | 2025-11-20 04:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aba9064-8218-3e8d-90fc-54bba69ed406 | -3.79989 | -48.93484 | 2025-11-20 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0d53b2f8-2531-36ab-86df-aefca41dffc9 | -6.16045 | -46.10253 | 2025-11-20 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a398da0c-22de-3704-a985-f3cc0e34d23e | -3.67946 | -50.17287 | 2025-11-20 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1975f40-8f96-3ff1-90f3-6bb6ec3b6b2d | -1.0233 | -47.2081 | 2025-11-20 04:31:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 628c6c0f-513d-361f-b72c-251ef6f28b72 | -2.00805 | -54.48475 | 2025-11-20 04:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21b76755-29cb-30e2-abaf-4bdbf61ef544 | -4.232 | -48.44709 | 2025-11-20 04:31:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87435fa9-d224-3efa-97aa-a1fb09e7761f | -6.15017 | -53.02285 | 2025-11-20 04:31:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c14698b3-ab96-3506-a605-4a19cccf0629 | -2.50932 | -47.82467 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ceef7a7c-9008-3deb-ac28-48e62706477d | -1.02661 | -47.20862 | 2025-11-20 04:31:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23369904-6de9-30b2-b14c-b10294562a9c | -2.12796 | -46.19394 | 2025-11-20 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3ea68d1-6a47-3ccc-8f0e-e1b095b8455c | -6.48182 | -47.5009 | 2025-11-20 04:31:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ade67a8-6ff3-34b3-8217-ad2c3d32450c | -4.10937 | -38.8926 | 2025-11-20 04:31:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 14dbdfa2-5c2b-3ee1-8ab4-a4c86e10c344 | -2.51262 | -47.80381 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3555d3b1-d0e6-372d-9ef8-4c3398a399de | -4.46898 | -50.64766 | 2025-11-20 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2ed4a87-91d3-38f3-8ffa-ba7b89391edc | -3.29527 | -53.83971 | 2025-11-20 04:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9e1a254-d458-3d00-bee1-eea26176132f | -2.5082 | -47.81025 | 2025-11-20 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3fb811e1-7a30-3443-afa2-c24aedeacd5d | -2.99981 | -44.38249 | 2025-11-20 04:31:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d23a9f04-710b-31b5-b63f-d2de47ec7939 | -6.57116 | -47.36538 | 2025-11-20 04:31:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2cf4ba2-bd9a-327e-a948-fa7d6636861f | -9.05798 | -48.83103 | 2025-11-20 04:33:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11bf2ad2-c235-3eb4-80e6-38b08a8a964f | -11.41143 | -48.44611 | 2025-11-20 04:33:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e891d72-d0e0-3d13-979b-7be315664ad6 | -11.50253 | -48.55812 | 2025-11-20 04:33:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb25ff46-61a1-3e6d-ab28-b49784a9af6d | -9.67687 | -48.76312 | 2025-11-20 04:33:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59473d28-0967-3d59-8eb3-78dab587e3e1 | -10.36708 | -48.91029 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcb651df-ba16-3eb7-88af-1d810956edbb | -13.94145 | -47.46502 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7a060c1-beb6-36e8-8f36-1cd205e76d90 | -10.36102 | -48.90574 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f507e571-3c3a-334b-a6b5-ada7c20b004e | -10.38416 | -49.92791 | 2025-11-20 04:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e07603e3-b61c-31b6-8296-aced52916ff8 | -14.53956 | -48.62799 | 2025-11-20 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae62cdfe-c37a-3de4-97b9-bde184cb1c4a | -13.26875 | -47.33494 | 2025-11-20 04:33:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6375c824-51ce-358e-8af7-fe5a16db5e05 | -12.94272 | -47.7096 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cde50f0-973b-3652-b4e1-56eed9624216 | -13.07389 | -49.51656 | 2025-11-20 04:33:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3beefde0-63cd-3a9a-86bc-b9f13aef4af5 | -14.95247 | -47.34171 | 2025-11-20 04:33:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ace5db59-8b8f-37d4-b2e6-c2456afeb64d | -13.35639 | -47.65871 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e00251e4-65ab-3cbc-bede-591ac70778e3 | -12.47475 | -47.81932 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d53bb9dd-7d19-3fef-9d41-b602402a14f0 | -11.41862 | -48.44365 | 2025-11-20 04:33:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19b03617-1166-3f88-b896-4dff76bcfcd1 | -12.94611 | -47.71013 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1da25cf-3eb8-3bbb-a85d-63643c99a9b9 | -12.90034 | -50.2002 | 2025-11-20 04:33:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41c9456e-a948-3bbc-b2b0-525f8d6edbdd | -14.53024 | -49.34821 | 2025-11-20 04:33:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 305216d7-1e91-3bf8-b39b-cfbd06bf1773 | -10.36543 | -48.8993 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 14997acb-f541-3002-9ec0-0f03d33c8df8 | -13.36374 | -47.65618 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b84ea8e-0b20-387d-90af-0b7e4c8ead05 | -11.26623 | -48.50571 | 2025-11-20 04:33:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb0054d8-b645-3af1-befc-58275a5088cf | -10.36212 | -48.89877 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 906b7ea3-01bd-3df2-90e4-7cf30fa9df3e | -13.07059 | -49.51601 | 2025-11-20 04:33:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ceba1f6-64dc-3364-9634-f9407b7e50e0 | -13.85918 | -52.95275 | 2025-11-20 04:33:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cbc1562-033c-3f9d-ad45-f73c282f3fcc | -11.41198 | -48.44259 | 2025-11-20 04:33:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aadd4c96-db0d-34bf-a533-42b1c392687d | -10.02399 | -48.13221 | 2025-11-20 04:33:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd0c2e98-4fc3-3024-a581-d2f51218cb27 | -10.02508 | -48.12518 | 2025-11-20 04:33:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2383b8c1-2ac6-3c9f-9b00-56e0ccfa0f59 | -12.23813 | -47.71222 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README11.md)
