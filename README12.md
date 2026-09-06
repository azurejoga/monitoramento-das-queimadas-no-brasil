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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 457d6615-a4e2-3416-bfe6-17b1d29d8f45 | -13.86862 | -44.30276 | 2026-09-06 03:45:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f413af1-da07-30db-9e99-8ce7efc7d2f3 | -13.43446 | -41.89251 | 2026-09-06 03:45:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b6bea6ce-698e-36a4-9d0d-58dfb82b0d0f | -11.33444 | -45.07837 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9dc23c61-cfdc-32f1-8002-bb234dd78f42 | -11.33169 | -45.07553 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea7928a5-cf94-35db-9ee5-331024254e55 | -11.29829 | -45.11244 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85ec4fbd-7efb-3f30-bbd6-4c61858b83d1 | -14.8633 | -40.90886 | 2026-09-06 03:45:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 99e1b466-f0b5-351b-8d56-7c0cb50b5f89 | -14.61096 | -41.04462 | 2026-09-06 03:45:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9b945291-2241-3ee0-bf61-e6bf33c6af76 | -14.9132 | -44.67084 | 2026-09-06 03:45:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 95fd8ecd-ec3f-3e4c-8512-193a39eb2c9a | -14.86868 | -40.90517 | 2026-09-06 03:45:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a5e2f0c7-10a1-3879-b989-774816f05f84 | -11.328 | -45.07801 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4225a15-86a0-35a3-b04f-6bf102ce36b3 | -13.42856 | -41.89664 | 2026-09-06 03:45:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6c0876d6-b992-3d6d-9831-004c1f479586 | -11.33278 | -45.07003 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 346d6b7d-100d-3402-9814-d886ac809346 | -15.81111 | -42.57482 | 2026-09-06 03:45:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2cd4ddaa-39bc-33c5-a80f-d8203e3e31b7 | -11.28581 | -45.70206 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f1f5b3df-0429-31d1-b184-453c3ef01ab3 | -14.61113 | -41.04778 | 2026-09-06 03:45:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3d2f2c43-e93a-3db0-b386-f767d3c86832 | -17.42743 | -40.0238 | 2026-09-06 03:45:00 | NPP-375D | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8c2bc68a-df7f-38f5-a213-7290df032aee | -14.91808 | -44.67613 | 2026-09-06 03:45:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| eaa5ac19-60c0-39d6-aabd-1088552c4dab | -17.42811 | -40.02014 | 2026-09-06 03:45:00 | NPP-375D | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f48c76cc-2aa7-372e-a8b9-72aa1dcf7d22 | -11.2912 | -45.70867 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce9a4727-4cd6-3c09-a038-611166c2c546 | -15.88361 | -39.9412 | 2026-09-06 03:45:00 | NPP-375D | ITAPEBI | BAHIA | Brasil | 2916302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f1e08395-4cee-3d10-bf93-adb676d23c4c | -11.28356 | -45.71281 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41c0c3d8-91b7-3513-8f0a-4b909fca6762 | -16.14403 | -40.68661 | 2026-09-06 03:45:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 52f8f250-e1ba-3709-956a-0c1350d16bdd | -11.33555 | -45.07293 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 824354e4-d5d7-3cb1-8841-9089c3a99705 | -16.75442 | -41.71598 | 2026-09-06 03:45:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 662a9f76-d002-330d-b0a4-12817420f9a7 | -13.43543 | -41.88743 | 2026-09-06 03:45:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 4b68f5db-8acf-3efa-a4b1-409dd36c311e | -11.2923 | -45.70343 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dcbc0984-113d-35da-a792-b54c1676ca8f | -17.42406 | -40.01927 | 2026-09-06 03:45:00 | NPP-375D | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 92ccb136-f388-3328-bbdc-fa0ab8b8dbe1 | -11.2927 | -45.70884 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 671b9d36-df8b-3d36-a244-98bbe4149d93 | -16.23 | -40.29755 | 2026-09-06 03:45:00 | NPP-375D | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 369e991f-e289-35f3-a48d-00ad65ad0042 | -11.29195 | -45.11153 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3683d115-12c6-3c23-ab75-b77e24118729 | -11.28687 | -45.69701 | 2026-09-06 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f47437c9-e630-3e50-b42b-f8484b22eb7e | -10.7492 | -60.7097 | 2026-09-06 03:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 42fad370-7024-3eb7-a92d-f083e581b305 | -5.3645 | -56.0447 | 2026-09-06 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 69ea0298-f5dd-3c8d-99d1-b8e5e44b2391 | -5.3462 | -56.0256 | 2026-09-06 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f7cf7d98-7f63-33d9-b69b-85806705bdcd | -6.6698 | -59.9443 | 2026-09-06 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| dd425a40-3c22-3962-a90b-3bce079a74ba | -6.6513 | -59.9642 | 2026-09-06 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 410d40a3-59ae-335e-9d34-4dd2214d5f36 | -5.1423 | -56.2703 | 2026-09-06 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c15b157f-1cf3-3228-b902-8e2f8049a838 | -6.6514 | -59.945 | 2026-09-06 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| f29012d3-0f20-3d1a-a68f-8a5267f35450 | -5.383 | -56.0242 | 2026-09-06 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 6fc83883-c33f-3a81-b3e6-481b8c777c60 | -5.3646 | -56.0249 | 2026-09-06 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 3bd290b8-af6b-3fb0-a56e-7d1aa0f9b278 | -5.1438 | -55.9741 | 2026-09-06 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| bf27e192-b5e1-38c2-9fcd-cd9b316a1250 | -5.1423 | -56.2703 | 2026-09-06 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| a7201980-9c42-3f91-82dc-5cde631a0c81 | -10.7492 | -60.7097 | 2026-09-06 04:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| b5e8fd20-9ef2-3fd2-849b-495a4afeae64 | -5.3645 | -56.0447 | 2026-09-06 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 7d57fcd4-f567-392b-9a20-e660adc53811 | -5.3646 | -56.0249 | 2026-09-06 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 40c1fe7c-afd9-3029-8722-d1184fb56b68 | -5.3462 | -56.0256 | 2026-09-06 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9a81fe97-1e26-357b-a4e4-96869f0653c3 | -3.60069 | -42.97377 | 2026-09-06 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27e0e8a9-e656-3488-87ce-f8837c443b40 | -3.54672 | -48.18818 | 2026-09-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 440cba1f-b441-39c1-8b0f-f0fed26e9d20 | -4.81632 | -49.39105 | 2026-09-06 04:00:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 770f9492-67b9-343b-b030-90e3626feaae | -3.15514 | -50.82716 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26e36857-85fd-3715-a3f7-37e63ed1b287 | -3.85492 | -51.04029 | 2026-09-06 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 621d9306-297b-3a91-a817-b070d8a6f457 | -2.7618 | -48.57648 | 2026-09-06 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f192c94-cff6-3bbd-885b-d892e2481a2b | -4.11277 | -49.08776 | 2026-09-06 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fe4323f3-10f0-38b7-89e2-e449bb451dae | -5.7416 | -43.2751 | 2026-09-06 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 52c2308d-bc34-39fb-9461-66ef8ec6efb5 | -4.90085 | -45.09764 | 2026-09-06 04:00:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61af4fe5-4eff-399c-bac2-c7b1cf25299b | -5.86295 | -46.22291 | 2026-09-06 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cb70850-5ab8-3a85-9bb9-28670d04be2f | -2.76551 | -48.57171 | 2026-09-06 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0aadbc93-9a05-3ed6-a12e-10f8855cc9ec | -4.98895 | -38.02908 | 2026-09-06 04:00:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bece554b-25df-3bdd-9ec2-9cb1d4c7341e | -5.86509 | -46.2218 | 2026-09-06 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78c369cb-501d-3680-9f82-6e54f54ab908 | -4.34728 | -48.97257 | 2026-09-06 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17bddebe-f76b-3bd4-8209-b7206f620cf2 | -3.54811 | -48.17995 | 2026-09-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 726658dc-1a77-358c-9e19-16cb8d1c7a4f | -2.87053 | -50.46887 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdf2a9e8-14d5-39ee-9209-1a1740f95a20 | -5.89194 | -44.73592 | 2026-09-06 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6a016c3-f818-36e4-a29d-f6884bec2dd6 | -2.24964 | -46.12664 | 2026-09-06 04:00:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9aa46884-be77-3b67-8fde-d9034dee4ae3 | -4.14173 | -45.63251 | 2026-09-06 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90309a18-a405-3cc1-929f-79d548e73022 | -4.45178 | -46.13875 | 2026-09-06 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 35f0d694-0a3f-37d0-a0f1-2b22e85d9c59 | -5.28896 | -45.14149 | 2026-09-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f80ddb57-ccb4-39d8-8889-deedfe82cf0b | -5.63484 | -44.36716 | 2026-09-06 04:00:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0aeb421c-b830-36d6-9c74-52d3b682f92c | -1.8652 | -47.9844 | 2026-09-06 04:00:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a3a235d-74a4-3f10-a7af-c434d6e1e630 | -3.85172 | -42.94294 | 2026-09-06 04:00:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 058df0f8-2f33-355c-a83e-4a740c27b08b | -3.97459 | -43.10867 | 2026-09-06 04:00:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b724aaf6-27b8-3ba6-a8fb-4395e9e3fed7 | -4.81026 | -49.38985 | 2026-09-06 04:00:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d6a742e-eae4-3a27-b5b1-fe6122a5dfec | -5.73704 | -43.27788 | 2026-09-06 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 46aa3bbe-e2f8-3259-9241-4ad1bc940d7c | -6.8759 | -41.04701 | 2026-09-06 04:00:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 635b1b88-8347-36b1-bd9f-b38f7b8937be | -3.85516 | -42.94713 | 2026-09-06 04:00:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b11f4a51-4bca-3122-bb75-f64eb0159848 | -2.76849 | -48.57307 | 2026-09-06 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af181c57-125f-3501-a5a3-c79e1a85570b | -4.36254 | -47.77755 | 2026-09-06 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 33ccf573-bba7-32de-9f0b-f2bbe1c2d34d | -2.86384 | -50.46773 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87725a12-eb5d-35c1-aa8c-d15eb2d4864a | -2.8672 | -50.46887 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c115d413-c4d4-3489-b62c-66a2b7a64c80 | -3.8819 | -38.49709 | 2026-09-06 04:00:00 | NOAA-20 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6512e062-1cb1-3fe6-a8b1-7431ba21a580 | -5.63913 | -44.36787 | 2026-09-06 04:00:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fa334fd-345c-3afc-809d-d60cedf30eb5 | -1.19875 | -47.76471 | 2026-09-06 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77ef65c9-5122-3c3d-8351-cca948b22847 | -4.36745 | -47.78207 | 2026-09-06 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 70637eb6-4bb4-3521-9975-55fef9a6dc75 | -4.36193 | -47.78111 | 2026-09-06 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 756c6db4-bb6a-34d2-ba6b-10dd18adeeac | -2.85949 | -50.47378 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a13c04e-e3ca-3437-a7f4-df6df15ced18 | -1.86006 | -47.97928 | 2026-09-06 04:00:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee459386-3e0c-3796-b9aa-647fba86cae8 | -4.35323 | -48.97368 | 2026-09-06 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a26d801-3db0-3c5e-8934-fbb6a1fbe867 | -5.73762 | -43.27439 | 2026-09-06 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 27a0eb56-35bb-3f4f-b3cb-f708dfc6b1cb | -2.87159 | -50.46281 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f96196f-5ab8-363f-80d1-0dc861172eeb | -2.86153 | -50.46167 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59135d34-0962-3cb8-a984-7e9072cd71da | -5.77113 | -45.07369 | 2026-09-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a46029b3-6269-380f-a179-a67500ce345c | -2.8649 | -50.4617 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f12fc67-4510-38d7-9ac6-f0d9b002f382 | -2.76253 | -48.57203 | 2026-09-06 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1113c8c9-272d-3d1a-99b1-b9db0e9cb46f | -5.28877 | -45.13852 | 2026-09-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19da18e1-72de-30ca-bc45-b25d12969d6f | -4.42625 | -38.36372 | 2026-09-06 04:00:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 448c21f3-09a9-32c2-99ad-4309ec81844a | -5.50246 | -44.02522 | 2026-09-06 04:00:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4df9fc14-3c39-3b19-8a46-d2bce847e0da | -4.81107 | -49.38523 | 2026-09-06 04:00:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22b990b8-c448-3682-bdec-71b17e1a6efc | -4.4508 | -46.13655 | 2026-09-06 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0a32ee16-953e-37c3-ac56-0dfcb98da459 | -3.55387 | -48.18085 | 2026-09-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1d7280d9-fbdc-3076-adab-8a5107c30183 | -5.69802 | -44.49119 | 2026-09-06 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README13.md)
