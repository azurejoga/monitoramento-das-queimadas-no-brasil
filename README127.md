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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e0b384f-8d0a-36f3-a8a4-fb1dbbe1f442 | -3.69001 | -57.00669 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32ba0548-d368-3fc2-a30b-43faf20332ec | -11.86183 | -48.03685 | 2026-10-08 05:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b1f4db9-a965-3cca-8102-e88d2953f740 | -4.2754 | -55.7187 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49c98a5c-9f14-3472-b44b-4a9a804fa8d1 | -5.8757 | -50.09439 | 2026-10-08 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a852f4ca-d3cd-3ddc-b8e0-d6e1851f804c | -3.03339 | -53.92708 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d8e412b-d2a7-32fd-ad08-b27afa609cb2 | -3.06329 | -54.38417 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bb9115b-7352-3066-80e8-a5f78b0bb1e7 | -8.59674 | -67.30459 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f0c6ad3-b73c-315e-b2be-e13c25982709 | -10.64464 | -53.85219 | 2026-10-08 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 235e7a4a-ad51-3db9-aad0-05d9d2e46c81 | -4.53656 | -54.98503 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f4e6e054-4224-36f1-9be1-777426a679a3 | -3.53518 | -59.49633 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a0a6652-d07e-37d1-9645-c7b9e84473e7 | -8.72263 | -45.16489 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 28f82fa2-a53a-31c4-ba29-5b417e835358 | -2.97839 | -54.13786 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbd97984-469d-33aa-88b2-557881dd75a3 | -6.14665 | -47.9343 | 2026-10-08 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 05d3bf9a-3900-3e7e-853e-7e726af7dbd8 | -3.20751 | -50.56308 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a181936-8350-3b83-8fb2-d05bdda855c7 | -3.65264 | -55.50592 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad25d0be-d976-3352-9b66-a4ef567258f5 | -3.08268 | -53.95885 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| e12eef69-4e2c-3c31-8e12-8ad79e2ae2f3 | -3.79639 | -59.36669 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd77552c-56a3-3d14-8fff-0a9e74f95890 | -3.96848 | -56.12027 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea61c56e-275f-3436-8b79-07285e00d984 | -2.70673 | -56.54647 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81aac936-d7e4-326e-b9d1-77662aa1d228 | -3.73843 | -55.95245 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 973beb19-892b-355f-93aa-176276124b36 | -2.84225 | -57.48438 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9179767f-5ec2-3461-8e36-427a15a24526 | -4.198 | -55.63061 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6f9fb28-d220-36dc-9bce-4fa2d4c10c85 | -4.45048 | -54.97986 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45dc8c86-d5b7-3f7b-99b0-8b86fdf18dcd | -8.6158 | -67.0231 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c53b3cf0-5de0-318c-9b9f-532620d6b3f9 | -7.21353 | -55.17425 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c83fff3-b175-3161-bc85-e4c847fddc3b | -6.9491 | -45.28872 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 67011568-2e64-331e-9f8d-f4a5f7a778fd | -3.73067 | -55.97987 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3062772-4415-340e-9769-118a465d6569 | -1.08326 | -54.11129 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c338fac1-4536-38fb-8e76-ed273d7eab30 | -9.1112 | -65.35172 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcff6664-9e86-3812-8101-695b0df397ae | -9.22441 | -67.26902 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 27f8f5b5-61fc-3948-ab4e-27dd07ca5f35 | -3.10544 | -53.76767 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 913ef591-af61-32ae-b387-bc20c55ce734 | -2.9016 | -54.0786 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f7790e5-7ef3-39df-a119-9aa85c5cc0d0 | -3.2901 | -54.06105 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acc895c9-7b36-3679-89db-749b4f040027 | -3.53938 | -53.98921 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b0d818a-1204-3ab7-89ea-a37102991b27 | -3.81215 | -60.47376 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d7a95ae-3f36-3b0d-9771-9fa14fabe615 | -3.63033 | -58.94601 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b112171-cf9e-3d48-9907-10960457b285 | -3.50133 | -59.43295 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1ba5e4e-b192-3fe4-bdfc-8be1aaa76ea1 | -1.32785 | -55.43238 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01bac1f6-2620-3dd3-9a89-4440ae2b34f1 | -1.52728 | -54.54715 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e2ace34-8153-3f9e-8ffb-4ec42276c15f | -2.57131 | -56.16381 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4340dd24-bc63-3ee5-b647-7a11b018c188 | -3.04787 | -57.48814 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73ebb333-4d41-3cb0-8135-0218705e9722 | -4.30832 | -50.78154 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45916472-1858-33fe-8fbc-3805396f0cd1 | -3.00219 | -54.08215 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 509b7477-12e7-3e8d-8b6f-d7c357e4c7f2 | -3.08032 | -54.27433 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb8d6d55-8c8b-3c8d-92db-62a33ca5bcd4 | -3.01091 | -54.09539 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 19771a65-540b-3c98-9dad-5fd44fd507ae | -2.56967 | -56.17418 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 322827d3-9b7f-3900-8e35-b612bb9be69f | -2.94523 | -55.7889 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bde9b438-d8ea-337d-8cf0-8ae7c3a5f34f | -4.26678 | -54.87574 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c71e3d8-b648-3291-967c-ceb9237f422f | -4.77195 | -55.73046 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c788735a-5d78-35d8-a77e-5e0c807006b2 | -5.9771 | -55.38722 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2734ee18-310d-382e-b884-fc6f02722817 | -2.76915 | -54.09859 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27a0e74a-4236-3ea7-bc38-8900f42c7e79 | -3.47496 | -50.08162 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c2d8ea7-55bb-3d8d-b65d-c0729e1cebc5 | -2.50707 | -56.25304 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f589e144-3474-3d8b-bf7a-93ae77383bdb | -2.94084 | -54.17147 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54c0dfde-4bef-36c7-93f0-d2245897ac52 | -3.56575 | -59.47564 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b1f6515-3c57-3bbf-9a5c-f5734b1aa436 | -3.28568 | -54.02029 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5adc35e9-ccde-3b28-8ada-b9e9a9082eaf | -3.22108 | -54.29521 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39bb8178-49bd-3ab2-8ef7-e93f94e4cd3d | -2.48356 | -56.12189 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67e163fa-cb92-32da-a2fb-e3252c65f2e0 | -2.76855 | -54.10243 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c89c310-4d4a-3cb4-9361-d18a0a989a66 | -10.3616 | -56.43955 | 2026-10-08 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 637aa86d-efb6-3417-8d55-e6db94a2d7d4 | -3.55466 | -59.4987 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3dfb3692-28a5-323d-a0d8-0d6186771be7 | -3.87425 | -55.82277 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00cd16fd-d1ce-3716-b278-0c78859336a8 | -3.62643 | -55.50931 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f61963ff-a000-3fef-8c5d-39e7f91c8536 | -3.26038 | -54.0204 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| fcd1d80f-5022-3b7d-820d-d0d3b76abe41 | -3.10125 | -53.77108 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb4d4b45-1f76-30f2-8e82-792ef8173e9b | -3.27218 | -54.01421 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a0c6d7c-529c-329b-8487-5ea38a6fd507 | -3.2744 | -51.07359 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5e1afd84-74cd-372f-962c-1202b6143c3d | -5.85687 | -53.46117 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2e757e5d-a4db-31df-9cce-9f2781f5cd89 | -6.03425 | -51.72304 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36569488-5eb4-3e8f-89bd-4a1f6d61b149 | -6.63677 | -43.73275 | 2026-10-08 05:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c8ded4bb-59ee-323e-8caa-b523183c4b51 | -3.29811 | -54.01015 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09391b24-a968-345a-bf07-3926bf13a2e5 | -1.10433 | -54.15641 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 300a9d7d-767e-3fd5-adb4-a8b210e8a712 | -3.43251 | -58.60155 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51f4285c-c138-39a2-a52f-824a5512b692 | -3.9095 | -55.8928 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a8cde6f-3690-3cbd-8503-8e4b0ed43d03 | -3.69282 | -60.54244 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa8e1282-5b79-3ba4-a94a-ad4fcd9bb579 | -3.08321 | -54.2787 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76ea0ff5-3939-3955-978c-6cf3157c347b | -3.20382 | -50.55836 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b384c84-f595-3795-b6d6-df2dc6e0884e | -11.97034 | -57.61183 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d304d980-4742-3d45-8abb-ae5f3ed3c548 | -5.70663 | -53.4905 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b49d15a3-6a71-33df-9b5e-8caba3b442ea | -3.26083 | -59.60577 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7606384a-cb29-3c31-8955-5f57b78819ac | -1.4652 | -54.76303 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 819fc514-2dc9-333f-8dce-ff27ac38e89c | -3.63133 | -55.50987 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a340b27-369a-3f64-ab4e-27e10621bd26 | -3.29917 | -53.86467 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0a9772f-3308-34d7-8bcd-ec39de462158 | -5.23452 | -56.00874 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57a0f80c-688c-36d0-8dfe-26a191857ad5 | -2.84657 | -54.13033 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b258c478-bfbb-3ae7-b75e-11fd0d8ae9c8 | -3.30851 | -54.03585 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1b6f9a8f-0224-3416-bb4c-b1792f3119ae | -3.29166 | -54.00517 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 60168948-11d9-329a-acc9-69bd9db30f10 | -3.94759 | -56.0206 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0710beb-d74c-3c73-9392-c21f0ae0b116 | -11.33004 | -46.66367 | 2026-10-08 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5067604-3fc1-3348-95a6-e9c2e8400e15 | -2.04448 | -56.37472 | 2026-10-08 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7132e50-9c64-3f0e-9e36-ceca0d3d4abb | -3.0582 | -54.20535 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d83198ae-edda-3069-bed6-e2a674daa4bf | -3.96958 | -56.11329 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d84ceacc-ee15-3e3e-932b-cf25b74984fa | -3.68666 | -55.95508 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3578044c-5ac6-3c57-8fac-406a322c83bd | -4.15513 | -55.14877 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f694fdf6-31aa-3d0f-b1ed-3df609fcced1 | -6.9522 | -45.26497 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6387987-f440-336b-8f0b-12e9c11ef9da | -2.50359 | -56.16753 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ad5d2a6a-bb6c-32f0-951e-6540854d286d | -4.92554 | -55.86668 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37f21a42-36d2-30dd-8ad3-da3e1f9e9d24 | -3.29105 | -54.00908 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a0939a9-db1b-3975-bc9b-29e9093f7e92 | -2.98022 | -54.12631 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcf733e5-3fb2-3136-855e-c75c6aab8b4e | -6.53338 | -55.26394 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README128.md)
