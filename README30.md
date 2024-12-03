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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f18ba71-b371-36f7-b23c-e6c0b477dc0f | -3.07879 | -53.37773 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1b5e1843-0392-3e04-a4bd-e11dcc59c0b2 | -3.66704 | -50.19958 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7befeb5-d3b2-38a8-b32d-cb8a99210a1e | -3.95627 | -46.50422 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66098e6d-5737-3752-a184-07915faaf6dc | -3.66884 | -50.18899 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd524bf6-03af-343c-98f8-ffbda8688099 | -5.2291 | -44.2328 | 2024-12-03 04:06:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0018b75-7c9a-305c-9417-c6b109f90ccf | -3.26905 | -46.45612 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75f44f15-70ec-3b97-b54b-09b6064afaab | -3.81987 | -46.67388 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87ad0eae-80f2-3e90-a815-6a1250c5c635 | -3.34623 | -46.05424 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 89435df5-ead4-3475-9a31-df3b06c4ce5a | -4.82342 | -43.43519 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aa22805e-744a-3e55-83d0-fd680b679d3b | -3.46354 | -50.26793 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d272ef6-736a-3339-9385-6bc6aa418302 | -2.79891 | -53.05285 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d6a7cf5-aa59-3f41-a921-33baccc8db94 | -2.43126 | -46.67016 | 2024-12-03 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a0ded6f-88d7-3774-80c2-9f1720d03c78 | -3.26483 | -46.45538 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07513e13-1a6d-3b62-b265-442d8a371782 | -5.7929 | -46.47863 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ea306d1f-b5c1-384e-9f56-d4011f0679c4 | -2.58086 | -51.92476 | 2024-12-03 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4b3cc3f-baaa-389f-921f-10ed9af824c9 | -4.20618 | -44.37307 | 2024-12-03 04:06:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5e457fd-a846-3db4-b017-b21073b02bce | -4.07074 | -47.08656 | 2024-12-03 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb0ad3d3-5939-39cb-8a50-fe41a493b344 | -3.1819 | -51.16306 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1682ec21-e9ee-308c-8660-2f5327848df2 | -3.54625 | -50.17447 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| decfad32-a8f7-3a95-adc9-2ba91767f5c0 | -2.81759 | -53.05136 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a17a17a-0fdb-3ec9-9eb3-27cee5892947 | -3.10423 | -53.23333 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2863b505-d66b-38fa-8263-e253bdbc45fb | -3.19804 | -46.36103 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edd67e9d-b43d-327e-9e03-d834b41f619a | -3.3458 | -51.21408 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f07ccaa3-bfe6-330a-aa87-3dd9e7e73aff | -3.27921 | -50.32554 | 2024-12-03 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6fe2f11-ac13-3d64-963a-1c56631d1077 | -5.80167 | -46.47625 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| d9df80b5-a616-31dd-9f2d-3491f9e04de9 | -3.3375 | -46.05605 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5114ef51-3c41-30a5-831c-0f3431a1d60f | -1.08671 | -53.45631 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 525fb6a6-727e-3c0d-9ec1-1ff3d1cd2707 | -2.23176 | -46.38128 | 2024-12-03 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e15471bf-6745-3b16-9267-fbb012574523 | -3.13972 | -45.99559 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e35feb9e-2279-38a8-b34c-0190f72a5887 | -3.98708 | -46.63265 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2930b73-b7a9-3401-bb56-9124ff69355a | -2.12299 | -45.3431 | 2024-12-03 04:06:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bdff356a-e1a3-34c2-8c03-c6a611f0037b | -3.69706 | -51.82246 | 2024-12-03 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 889ed79e-133f-3925-9cd8-e71076fb68b6 | -5.16793 | -43.73838 | 2024-12-03 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4537b62f-445c-3fce-b014-c01b7ebcdfcf | -2.72875 | -45.21141 | 2024-12-03 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 24c366f1-85d1-3f02-90d6-939baacca5b2 | -3.70232 | -51.82793 | 2024-12-03 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8ce14b66-0abd-3a01-8e4f-422aca40ad9d | -5.2255 | -44.23223 | 2024-12-03 04:06:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b583438-5577-32a4-b50d-bc7c057949a4 | -3.33862 | -46.04904 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a47400e7-7d0a-3509-885a-7e67af04b2cb | -6.18215 | -42.62356 | 2024-12-03 04:06:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bda92191-f472-3d4c-bc2d-d7ec386d2a88 | -3.66279 | -50.19175 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f11e5e80-1377-3b67-abf8-63091cf560cd | -3.86926 | -43.35693 | 2024-12-03 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f4dd936-afb5-3524-9195-8c823caf3368 | -3.29663 | -53.66207 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 64fa6d4b-155f-3546-9893-6ecb2178cf3f | -1.75538 | -52.78497 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3475dcd6-79ba-3c49-91f2-23c295ec91f8 | -3.33919 | -46.04552 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2b6e0025-7a55-33e3-88c6-a7487e33a896 | -1.96596 | -45.83628 | 2024-12-03 04:06:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bff04d76-36ab-3f85-afd4-3361e921ae16 | -4.3477 | -43.74763 | 2024-12-03 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86531bcb-462c-39fe-845e-d4291d95f801 | -3.68122 | -44.70393 | 2024-12-03 04:06:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb3e6194-4d96-3daf-bd70-e18ce7858bf4 | -3.54343 | -50.19173 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eb65da1-c34f-3a14-9264-96a67c1181d1 | -1.8239 | -46.59253 | 2024-12-03 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b66e9726-a1bd-34a1-b515-34f6c184277a | -2.85042 | -45.8339 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a01947de-fed1-3aa2-89d1-882d0a31c87b | -4.56365 | -45.4709 | 2024-12-03 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eadd2475-0b13-31b2-8f53-4f1b668c08e8 | -5.22142 | -44.92272 | 2024-12-03 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eefd602d-2904-30f1-8cba-60b1932a40a2 | -4.74418 | -45.71125 | 2024-12-03 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e61a7b9e-d845-3f27-b28d-250c016c3208 | -5.00292 | -42.94679 | 2024-12-03 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0f8da29-882d-3623-bee2-d8357c5f7964 | -4.74208 | -45.11341 | 2024-12-03 04:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3355a98b-9119-3254-a7fa-ec0b30a858e7 | -4.70736 | -46.39296 | 2024-12-03 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6d0d13d-dfcd-3de4-b6c7-41c3c84e5f28 | -5.44194 | -45.58417 | 2024-12-03 04:06:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2498c80-24d5-34cf-ab46-c810d4fe7b4a | -5.81266 | -46.48558 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2b602d50-a211-368c-89aa-94a1e076d084 | -3.46164 | -42.00602 | 2024-12-03 04:06:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8c839440-25b5-3652-a7cc-1e5c4b42f4c1 | -0.83965 | -48.71972 | 2024-12-03 04:06:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f20d148c-b7c3-34a5-bee3-dc3e204d3ce5 | -4.16152 | -48.58025 | 2024-12-03 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b86855e0-fd7e-3ce3-85cb-fe6b9e360b6f | -5.99914 | -45.41074 | 2024-12-03 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f0802fa-ced1-3a5a-9d51-6ec7c91686c4 | -2.48745 | -46.56989 | 2024-12-03 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e310ea23-9d75-3923-83a4-90a63509a01c | -3.35106 | -44.35537 | 2024-12-03 04:06:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 638ea9b2-eba5-3214-9f70-b82ebb598927 | -3.55366 | -50.1721 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5baf006f-d627-3882-9f30-60467f0bfc05 | -2.19752 | -53.77735 | 2024-12-03 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38f818ad-fe4a-3b76-a991-79d785193778 | -3.08249 | -53.38181 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 0db2cbbb-6714-3a0f-8d1b-1a5d15e8db77 | -2.71831 | -47.55035 | 2024-12-03 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a0a8d57-528f-3e79-9862-53e15ad05d96 | -3.55676 | -50.18663 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a48787ef-8a11-34d0-a641-ee5bec7a19bc | -4.16548 | -48.58621 | 2024-12-03 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ebe1df8e-e57d-3b36-94b1-55c6dfe31ba6 | -5.41041 | -42.93171 | 2024-12-03 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 38f7ccaa-a65e-319b-aa65-2f6f03a49b53 | -4.94169 | -43.77583 | 2024-12-03 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 186af057-b151-30cd-827d-d6f7e7bfbc6a | -3.3178 | -42.78459 | 2024-12-03 04:06:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d727bb6-4f40-3851-9640-359ca18ec3f5 | -2.66454 | -44.98285 | 2024-12-03 04:06:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2bc063e-f648-3f7c-bda3-5cce6defced4 | -5.58693 | -45.14532 | 2024-12-03 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 833cfc17-f6f0-3849-847c-96c37c07c485 | -3.26466 | -46.93222 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fb221b1-ffba-33a1-818e-373f0cd4f824 | -2.58899 | -47.48554 | 2024-12-03 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2df8d70a-fdec-39ca-8d9e-c8c4341021c8 | -4.80753 | -44.99722 | 2024-12-03 04:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 050c1d0d-3609-3fb5-b88a-e2e4adf7936a | -3.55851 | -50.17638 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3c6f0883-e966-3f29-ae28-9af0dcd97580 | -4.55922 | -45.71896 | 2024-12-03 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 532e8510-0fae-3d13-a8da-1c078f70797c | -3.00994 | -45.61685 | 2024-12-03 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82f3f2c2-dcc1-3ef3-82e8-026956f9508f | -2.81304 | -53.04942 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81b2f545-d6c3-3ad8-8026-21e141287a6e | -3.75691 | -48.16161 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b6faf6e-3b85-3ee1-8caf-44c70fb37ce8 | -3.34068 | -51.20883 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8a85a314-2a39-308f-a6e8-faadffb5392b | -2.8074 | -53.04271 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1cb6c34-e9f6-3f8b-9f78-cd7a25086009 | -4.03819 | -46.92565 | 2024-12-03 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04b971ae-17d7-3c41-855c-319f0f34de39 | -3.97082 | -46.62581 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e01db0b-abc4-30ea-8384-cfc4ba7da329 | -2.80322 | -45.94549 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3fa965d6-c512-35e5-83c7-0b9d6a92ca3f | -3.85711 | -46.52768 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e610030c-cf34-3851-8b69-71b1dd80e5ab | -4.75791 | -45.65247 | 2024-12-03 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37f1af2e-440f-3914-bf5a-effc40ebd08c | -6.03505 | -42.52 | 2024-12-03 04:06:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 64089949-2af2-3d74-87d3-6bad9f068cd0 | -2.34077 | -45.89877 | 2024-12-03 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 916da259-a631-368c-8d1a-caa41ed84c87 | -3.33693 | -46.05961 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| da83736f-bc45-308c-b151-e552544c0a92 | -3.01918 | -54.03995 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc331d55-eec7-3eb2-a0a0-cb98a6facc1e | -3.83464 | -44.11056 | 2024-12-03 04:06:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a357032d-005d-3277-9fd1-8d27cc4c85e4 | -5.11103 | -43.21125 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1aff971f-2071-3bff-8848-ebee4707f2c4 | -3.55735 | -50.1832 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 476050a6-8fe1-3dee-83e0-b03b2693ac75 | -5.14203 | -43.23115 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4901d1b9-1340-37ec-a7a3-794cd575cd48 | -5.80227 | -46.47268 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d57fcf34-b23d-3b23-8db4-6c9ecbebf05f | -4.94104 | -43.7798 | 2024-12-03 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cd176e9-8a31-3a72-a84f-b491a79fc1e0 | -3.2683 | -53.62463 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README31.md)
