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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2ab01d3-7d89-35e7-a279-dcde5363e7a7 | -3.3096 | -50.1781 | 2024-10-11 04:55:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 17c82499-9c30-3811-8a8b-21e7c3b0932b | -4.0962 | -48.2523 | 2024-10-11 04:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 8ac8ef4d-4808-37a7-be5f-80c0f2393212 | -4.0963 | -48.2307 | 2024-10-11 04:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e0d582e7-8081-3960-9ebd-f0f4bc88798d | -4.1146 | -48.2731 | 2024-10-11 04:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| da53d8b1-7669-3d5b-814b-402c936d8ac3 | -4.1148 | -48.2515 | 2024-10-11 04:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 396.4 |
| 643c0457-0710-3f2d-910c-89ec50d42a56 | -4.1149 | -48.2299 | 2024-10-11 04:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 226.3 |
| 46274cab-d678-38a2-aab9-74d76b4748a4 | -8.4417 | -55.4692 | 2024-10-11 04:55:53 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5ec6a6d4-df55-3766-834b-b7e1dbf1338e | -8.4419 | -55.4491 | 2024-10-11 04:55:53 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| cadf2b32-2161-3b39-a3fc-5ff43b778481 | -12.87 | -53.53 | 2024-10-11 05:04:11 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42f212e4-a3aa-3aa0-a496-41b648fa53b1 | -12.84 | -53.52 | 2024-10-11 05:04:11 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2bbdbccc-dde1-32e1-845a-9fa2941ce8af | -4.11 | -48.25 | 2024-10-11 05:05:04 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73d973a7-149f-3cf4-a6c5-97299bd0dfcb | -2.6716 | -53.3502 | 2024-10-11 05:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8e04082a-13c9-3655-9000-8ddc0883b3b8 | -2.6533 | -53.3506 | 2024-10-11 05:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 177fcbb5-ba5d-36f7-9d2d-d22a6d898aee | -2.8081 | -51.0084 | 2024-10-11 05:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9bf5a7d0-add5-305c-b352-be8f5c89658b | -2.9857 | -52.8961 | 2024-10-11 05:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 06b0ec58-2ac1-3ca8-9714-658816afc275 | -2.9857 | -52.9164 | 2024-10-11 05:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d57e4bf7-fcc0-367c-af8c-2d77a6a67351 | -2.9673 | -52.8966 | 2024-10-11 05:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4fe60c14-fd41-3b39-8ad7-97bc6fcb5b99 | 2.48566 | -50.8311 | 2024-10-11 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e3c75fc-d31e-330b-a917-309f870ee969 | 2.48499 | -50.82696 | 2024-10-11 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 55f3f064-baf0-3567-9ce8-0e996f734f07 | 2.47931 | -50.81933 | 2024-10-11 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbc45133-76d4-3bc1-9431-e2e307d491df | 2.47864 | -50.81518 | 2024-10-11 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3028d44f-125c-3f9b-a92a-fa8a76fc33b8 | 3.51564 | -51.46434 | 2024-10-11 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da8ef2e5-2ef1-3b21-b19d-83c932decfbc | 3.3872 | -51.33854 | 2024-10-11 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01466f83-184b-317d-b876-e07e4da25980 | 3.38661 | -51.33484 | 2024-10-11 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb2235b4-423f-3e88-8f59-7323a974ea0d | 3.38308 | -51.33922 | 2024-10-11 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b135b06a-c0dd-3c76-92f8-6fe82957fded | 3.34182 | -51.31927 | 2024-10-11 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11f3e608-be1b-339d-94f1-32cfc46edb75 | 3.3377 | -51.31996 | 2024-10-11 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d3ff4e1-99e9-3cbd-8170-a5d851b33eb7 | 3.33357 | -51.32065 | 2024-10-11 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 146cdc29-2052-3001-b260-4c6d07df5e38 | -3.0525 | -61.6727 | 2024-10-11 05:15:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 229a33c8-7439-3ea3-b9c9-d1fcfde80552 | -3.0343 | -61.673 | 2024-10-11 05:15:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 51f15269-61b8-3a70-a71b-bab20c822ff1 | 1.07891 | -60.42127 | 2024-10-11 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2956fa30-8c4c-31d0-9818-d71d2c846750 | 0.8363 | -60.47279 | 2024-10-11 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6772e0ff-c453-311e-b29e-52e878405302 | 0.81427 | -59.84595 | 2024-10-11 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcffd269-8a90-3350-a5de-64240cd78328 | 0.81078 | -59.84649 | 2024-10-11 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e38e075-34ec-33fd-b1ac-c32fa6f4317a | -3.08757 | -60.29401 | 2024-10-11 05:16:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 970a9162-6b1f-3594-b1b9-aca45cf5244a | -2.95578 | -60.01534 | 2024-10-11 05:16:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73b6110e-ac52-3826-b569-7c855fec4479 | -4.29851 | -60.14682 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c4c6233-f212-3966-8698-88057c3b8f06 | -4.13495 | -60.2705 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e3dbead-3e36-3136-a74e-e30183008075 | -4.13377 | -60.27784 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5364b212-d31a-3858-98d4-c3765598ea7a | -3.78102 | -60.12912 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a422f4b1-f3ee-3ddf-b92d-881f55ba3029 | -3.7782 | -60.12495 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63485bce-0962-3d7b-9f74-2bf93f64a51c | -3.77762 | -60.12859 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ba9d049-b626-3cdb-923b-e2c8e1be29da | 1.97021 | -60.91528 | 2024-10-11 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73b0cb41-44ce-391f-9d0a-88bbd6f00db7 | 1.96761 | -60.91306 | 2024-10-11 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8345027-f8d7-316c-826a-01cbe8993f77 | 1.60781 | -61.02525 | 2024-10-11 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39aac980-31c9-3a2b-ae55-37e86e349ad2 | -1.48992 | -61.59153 | 2024-10-11 05:16:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8db6802e-c599-36fd-8cc5-d1c8ce544a52 | -1.48923 | -61.59592 | 2024-10-11 05:16:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be71f1f4-ba2a-3160-8057-0877aa51ca83 | -3.04255 | -61.6834 | 2024-10-11 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 551e0fa5-4eda-3a9f-afeb-c405ea10f4b7 | -3.03958 | -61.67854 | 2024-10-11 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 277dd963-dc04-31b2-a0ad-c063e4d8aac9 | -3.03888 | -61.68282 | 2024-10-11 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20c3ed1f-5a9e-3a8a-b547-98952f1d612a | -3.03819 | -61.68711 | 2024-10-11 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9b33a30-70da-3611-a816-6471e4083e5c | -2.99923 | -61.41678 | 2024-10-11 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ec24eb2f-cd5b-3cb8-936e-378ab582f61b | -2.88339 | -61.86199 | 2024-10-11 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60043cd4-2a8f-3731-8bf6-09c8ce209ac0 | -3.0469 | -61.67969 | 2024-10-11 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0f234f4c-c7d5-3a17-ae8e-08dc5e53598c | -3.04621 | -61.68397 | 2024-10-11 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a56ab2d4-790c-376c-92d4-ccf136cd1264 | -3.04324 | -61.67912 | 2024-10-11 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5f53aa19-3c14-3264-b29a-7a7a46ee906c | -3.04185 | -61.68768 | 2024-10-11 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 661d9960-4d69-3c36-b5a9-bea8a71ed8b1 | -3.03522 | -61.68225 | 2024-10-11 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92eb5137-db21-3a91-b0ef-a5ad435afd7c | 1.09908 | -52.59069 | 2024-10-11 05:16:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2f2e47a-e1d1-36a0-a4a7-a95534ca9384 | -2.62223 | -66.35551 | 2024-10-11 05:16:00 | NOAA-21 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8cbaba9-263b-3328-b18f-5cd4ceab5aa1 | -3.61645 | -44.77633 | 2024-10-11 05:16:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 635eaa61-5be1-34d7-b2ec-a587fd147010 | -3.61551 | -44.78313 | 2024-10-11 05:16:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04f6f32a-d8a6-3144-8e94-b843c8fafeb6 | -3.61127 | -44.77781 | 2024-10-11 05:16:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cb8b060-d90a-327c-9373-c7e0c1fd5c70 | -3.61028 | -44.78461 | 2024-10-11 05:16:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85ec7027-72c2-3a10-a805-49870c5c5b8b | -3.60943 | -44.77518 | 2024-10-11 05:16:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f24643c6-7ef8-359d-9c9c-ff9929e221ee | -3.60849 | -44.78199 | 2024-10-11 05:16:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fae38931-8cc3-31b7-b49b-5e2195834ba1 | -3.60755 | -44.78881 | 2024-10-11 05:16:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cff2a4f-a52a-333e-84f7-7819a6b68666 | -5.60403 | -46.37063 | 2024-10-11 05:16:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bfa19420-b115-3e6e-88c3-9b1db9b2ed8a | -5.1969 | -45.94983 | 2024-10-11 05:16:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c87df69-d963-30ee-9aaf-2f163543b4f6 | -5.19018 | -45.94897 | 2024-10-11 05:16:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58c82dd1-4fba-39d2-a8f3-bb61aad0c4c7 | -3.30198 | -46.08004 | 2024-10-11 05:16:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a8c54cd-e5a2-3a12-9017-8207ee413154 | -2.54192 | -47.2257 | 2024-10-11 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 250b6d6e-1888-374e-86e7-a5622e625b41 | -2.54124 | -47.23015 | 2024-10-11 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aff8f1f8-01d0-30ad-9e8d-2966f4b3d1a0 | -2.53922 | -47.22363 | 2024-10-11 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a255c15b-798e-3783-b6d4-d7641f9eddf5 | -2.53857 | -47.22813 | 2024-10-11 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f6ea4ef-4bec-3e7d-80fd-ee601a57ef1c | -2.53593 | -47.22488 | 2024-10-11 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23e874e0-10a5-3b35-a24c-0bd6f00bc193 | -4.94695 | -47.40602 | 2024-10-11 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6777a1a2-c9bd-30dd-80f7-2d32999bfd80 | -4.92007 | -47.65253 | 2024-10-11 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2d506bb-b69c-31bf-91d5-a203a88d9a38 | -4.91811 | -47.65118 | 2024-10-11 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9175e9e0-f2e6-3a87-82b0-eca100725b80 | -4.91744 | -47.65588 | 2024-10-11 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b23570d-44db-33d1-8099-06b337ec471c | -4.91409 | -47.65136 | 2024-10-11 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 216ead77-d8b4-3408-94de-44ef4e706fa5 | -4.67979 | -46.43524 | 2024-10-11 05:16:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 442d365a-d93f-3e01-8a93-90a411ab8136 | -4.67937 | -46.4351 | 2024-10-11 05:16:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7c1f499-0c70-3ac2-8c77-96effac83093 | -4.67906 | -46.44056 | 2024-10-11 05:16:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88035445-d21e-35b7-a5dd-d9e80d0c7ce3 | -4.6786 | -46.44041 | 2024-10-11 05:16:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09e8d24d-e4f2-3eea-bf07-f4c98a4d9da8 | -4.67259 | -46.43967 | 2024-10-11 05:16:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c344260d-2d3f-313d-8c0d-6c307e46647e | -4.67213 | -46.43954 | 2024-10-11 05:16:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c015b9bc-861c-3357-bc6a-d8fbafdde9fc | -4.66692 | -46.43288 | 2024-10-11 05:16:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 007a1a3d-e78d-3186-a290-de72e33c16f2 | -4.6665 | -46.43274 | 2024-10-11 05:16:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad5cab2c-da1b-3ec3-98c5-04ff0c8b8dec | -4.66162 | -46.80304 | 2024-10-11 05:16:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcf8643f-6d5e-3134-a634-9ba6a833e99b | -3.93597 | -46.43888 | 2024-10-11 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c71094a0-fd94-3def-b304-af7d809aca34 | -3.9343 | -46.43683 | 2024-10-11 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 19e69489-93bb-3eb8-acce-be6ff7326ca1 | -3.93352 | -46.44217 | 2024-10-11 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9b519b19-c941-39ad-960a-7bb5dd0e0c32 | -3.93057 | -46.46223 | 2024-10-11 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e647ca8-0716-32bb-98f9-f3ffb22d704d | -3.92667 | -46.45873 | 2024-10-11 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9dd8bb7-094f-3e1d-bd2b-a40c275b2689 | -3.926 | -46.46353 | 2024-10-11 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86e207ff-42df-3b38-996c-b1ce697a7112 | -3.9241 | -46.46188 | 2024-10-11 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8891ab8a-d9c8-35ae-bd49-8df0a8ac7efd | -3.8124 | -47.4921 | 2024-10-11 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 023c55e7-33ba-3ac1-b883-c0fce1cf7c75 | -3.80704 | -47.4868 | 2024-10-11 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 654890ab-d2ba-36b2-9adc-599ad257fc73 | -3.70237 | -47.59832 | 2024-10-11 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README75.md)
