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
| aaf4d32e-6a71-3f07-acd7-d076ec80690c | -8.1182 | -54.773701 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7ce45e6-84a2-326f-9d1f-e0fb2b05549f | -8.184 | -62.774601 | 2026-09-04 00:25:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b1f6000-b0d2-3ad2-a0dc-57106d2df086 | -21.7269 | -47.128601 | 2026-09-04 00:25:00 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e1cc9623-3c7d-309c-b7ad-a0df249377ed | -18.7344 | -48.91 | 2026-09-04 00:25:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 129357de-f2a8-379d-9d06-e267c9f6c049 | -10.9089 | -45.349602 | 2026-09-04 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74cb0e2c-34b4-3208-9e55-a23b2ed6ab0d | -5.3858 | -54.438301 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9548648e-dba5-3a80-b0c8-40999b0e187b | -10.6369 | -50.412399 | 2026-09-04 00:25:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce3be3a1-f298-3d1e-adce-6b77b53e7b58 | -8.0768 | -55.327202 | 2026-09-04 00:25:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c22f6e4-601d-3634-a542-29300087b6d0 | -8.2944 | -54.917198 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c50fdcd8-1323-3cc8-a3dd-f1f645c7e0fa | -10.208 | -50.256001 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 253ce1d7-dc27-3351-bc93-71c25d62d972 | -13.5747 | -47.880299 | 2026-09-04 00:25:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e6d55a5b-9f64-3a6a-965b-dbc137dac790 | -10.5661 | -50.023701 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2186b738-83bc-34cb-a1b1-ee7cd90f535d | -8.4913 | -54.6465 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a856a7e-b67f-3663-ad25-0f36be7c9b07 | -4.474 | -55.4188 | 2026-09-04 00:25:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bcbbda0-eb44-353e-ba82-f7e8b7a94cd3 | -6.9963 | -62.959599 | 2026-09-04 00:25:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6efd4a5f-3550-3396-b61d-8078ace1e1c9 | -10.6272 | -50.4147 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b79fc4e1-c6f9-3cb0-b9cc-d878bf955e67 | -3.1196 | -51.735401 | 2026-09-04 00:25:00 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efe2d1d0-f722-3668-8a47-2845a29682d8 | -5.8269 | -52.081902 | 2026-09-04 00:25:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7bae844-64b9-3f1c-9491-8bedebecd249 | -20.0126 | -50.065399 | 2026-09-04 00:25:00 | METOP-B | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e65bbc8-a5c2-3a54-a259-855a6f2c7917 | -21.717199 | -47.131302 | 2026-09-04 00:25:00 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 57e327b9-bbd6-3545-ba3e-eb58db8e57d9 | -7.0098 | -62.976002 | 2026-09-04 00:25:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95dd2761-0029-3bd2-a5c8-29997f4d2967 | -8.1743 | -62.7766 | 2026-09-04 00:25:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2a042dc7-3f73-3706-919e-b6888130e365 | -15.9048 | -50.156799 | 2026-09-04 00:25:00 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 212120b1-9aac-315c-8872-78ca21d65704 | -11.9437 | -55.9133 | 2026-09-04 00:25:00 | METOP-B | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb43818d-f86f-30c3-9c9c-52a62a80a2fc | -18.139799 | -51.789501 | 2026-09-04 00:25:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 06b80417-99a5-3469-a094-2f6ad62bd089 | -14.2082 | -51.215302 | 2026-09-04 00:25:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fb85c800-2d29-3da7-8b84-0b4b7a5af6be | -10.3318 | -50.343399 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f34da7d-7ef4-32f3-8716-cae12eb51a72 | -10.2586 | -50.032902 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f150478-ec5d-3a3a-bd8e-50e6ca7c7d3a | -3.7667 | -47.548401 | 2026-09-04 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e31da0-a84c-3956-a79d-6bde80e27c5f | -17.1014 | -56.8424 | 2026-09-04 00:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 314f3bb9-9d4e-3bf7-bb7e-741e6c421a85 | -17.3176 | -49.6138 | 2026-09-04 00:25:00 | METOP-B | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3b939156-2cb1-3d8c-a02c-f8c690b3c7ee | -10.5759 | -50.0214 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a387e19-dac5-3817-a190-a08a70f10f50 | -5.0523 | -46.068901 | 2026-09-04 00:25:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c0227ac8-3736-375e-bb4e-c1b85224d239 | -10.9046 | -45.332699 | 2026-09-04 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 453f0891-ca2a-3421-bdf7-b623657878ac | -18.726601 | -48.9207 | 2026-09-04 00:25:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 72df06f3-6fa5-3716-b637-0fc3b23bbad7 | -6.1044 | -44.678501 | 2026-09-04 00:25:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aed94628-731c-3eb9-8c32-cbb707d39b84 | -8.2226 | -54.918499 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d67ace9-abdc-3a40-88f9-01cdc421e28e | -23.088499 | -48.6073 | 2026-09-04 00:25:00 | METOP-B | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ffd39720-96ba-3aab-b504-c11b20297909 | -4.1272 | -56.349499 | 2026-09-04 00:25:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a49fc95-7140-343c-946b-e62e97ad350b | -19.312099 | -47.086102 | 2026-09-04 00:25:00 | METOP-B | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6a8b188b-6438-30a8-ab74-a273f9efb76f | -23.277599 | -46.594501 | 2026-09-04 00:25:00 | METOP-B | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c421253b-e4b4-3299-b154-c8d7a13ed033 | -23.0788 | -48.610001 | 2026-09-04 00:25:00 | METOP-B | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 411ee332-a245-3e7e-8bcd-3e6050ae1a3c | -15.3244 | -47.044601 | 2026-09-04 00:25:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb125a5-8f94-3570-894d-8ece3cfdc9c7 | -5.0426 | -46.071201 | 2026-09-04 00:25:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef1aa61c-5913-3af3-a6da-0b5dc3b7ea52 | -14.7955 | -47.123798 | 2026-09-04 00:25:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 06541cda-e4bf-391b-9e17-6416ebf073c2 | -7.006 | -62.9576 | 2026-09-04 00:25:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f9ce7c6-928f-3459-b27b-3ea70a1c1116 | -11.5162 | -49.198399 | 2026-09-04 00:25:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d7b8b79-0914-39de-be27-0c766eeba2b8 | -8.4707 | -54.738701 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1579b5df-4c2b-3366-8995-c031a24248ad | -8.4928 | -54.6534 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51f7dde6-61e5-33ee-98ee-55a807e52a38 | -18.1511 | -51.794399 | 2026-09-04 00:25:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 771998a1-a04f-3a5f-9ed4-13a273582862 | -5.829 | -55.721901 | 2026-09-04 00:25:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34d9f98f-5ee3-3c8d-9828-3cda596882ab | -3.1294 | -51.7332 | 2026-09-04 00:25:00 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be9f65d9-6724-37ef-a457-d70c7d7a6771 | -4.3607 | -47.759499 | 2026-09-04 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f30eb98-1671-3b69-b960-abacd28b2d10 | -4.1455 | -60.691299 | 2026-09-04 00:25:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00156fab-cbb2-3e40-abbb-f9832e14fa8e | -14.7983 | -47.134998 | 2026-09-04 00:25:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e135c66e-4d13-35e7-b177-6e2d9f40b9c3 | -10.3298 | -50.3349 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77e74906-c7c2-3efb-9058-21acebc598e7 | -4.2897 | -59.948898 | 2026-09-04 00:25:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ac45656-11ff-3795-be6b-984a2bd7569a | -4.2192 | -56.255001 | 2026-09-04 00:25:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89ef8e2b-0621-3d48-8345-c03dd53829de | -20.978901 | -49.0956 | 2026-09-04 00:25:00 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6fa3c977-6079-359f-bd8f-0f0f7c0be32e | -10.8623 | -50.8904 | 2026-09-04 00:25:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d93be907-4da8-3de7-9149-e292fb1f02d0 | -6.2952 | -46.076 | 2026-09-04 00:25:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eed42aaf-e41b-3afb-9639-7d7994219862 | -7.5553 | -61.311298 | 2026-09-04 00:25:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3cdb0f12-47d5-3964-aa71-bf25110399f9 | -8.5042 | -54.658199 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e8a09d5-f183-3d9e-a2ad-1ab5bcdf6abd | -4.4642 | -55.421001 | 2026-09-04 00:25:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73d8b629-1f7a-3b77-9036-6f03ab2390f3 | -5.3874 | -54.445202 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57679d49-c123-3091-92cd-d07f253827d7 | -10.2607 | -50.041698 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02990e83-bac6-333c-af8f-6e917008cccf | -10.8992 | -45.3521 | 2026-09-04 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 396e495f-9e38-3fa3-ad7a-5fba8dc59ab6 | -18.801901 | -47.5439 | 2026-09-04 00:25:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 63215502-080a-3e9d-98b4-ecf07545e908 | -8.1084 | -54.775902 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21ef3100-b149-30e4-af3a-44807c2efa02 | -2.7604 | -49.471401 | 2026-09-04 00:25:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6f0ed44-a75b-34e8-839c-644430e8d850 | -13.4439 | -53.5952 | 2026-09-04 00:25:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8982f89e-f847-3f0f-a002-480ad3f1a12d | -10.4999 | -51.329498 | 2026-09-04 00:25:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d69e9bdb-5113-3c76-adeb-0642493091a4 | -6.2995 | -46.093899 | 2026-09-04 00:25:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6215816-79ee-31f5-ab2c-2bd55d04945d | -8.4469 | -54.678299 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a96a6e0-6e99-34b1-a6ab-c8b2efb00434 | -10.2003 | -50.266899 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83f93a29-0e4f-3028-84b1-6f187b779091 | -8.1069 | -54.769001 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c65f669b-51ab-3d88-8edd-2c35ec1f5e9d | -10.3122 | -50.348099 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc44a19a-772b-31ec-b33f-d33b55cda185 | -8.4252 | -54.7197 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1b9d79c-0ec0-3874-8971-a1c9c685f8f4 | -18.1429 | -51.803902 | 2026-09-04 00:25:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ec2f40c9-c725-3265-ab39-fd0d8470e51a | -17.087601 | -56.823799 | 2026-09-04 00:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a277162c-60df-38fa-bad0-a8a3ae484e9c | -7.265 | -61.093601 | 2026-09-04 00:25:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bcee2869-a656-307e-aa7a-e2d789527b90 | -6.9903 | -62.9799 | 2026-09-04 00:25:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9996ee3-2868-3978-aa91-dd8c610e3743 | -14.8232 | -48.081501 | 2026-09-04 00:25:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7c17f0d9-4b3c-3236-aaf3-d7a5e1a8cd3d | -13.4668 | -57.024399 | 2026-09-04 00:25:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e5922f9-d2bb-3a2f-8fc6-c1b9cdfbc07b | -4.3676 | -47.788898 | 2026-09-04 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 618f8142-9843-36e6-94b5-c57cf47c261e | -14.9013 | -44.681801 | 2026-09-04 00:25:00 | METOP-B | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5a66b117-ef22-3a9b-9a00-985e79d832b2 | -15.9066 | -50.1646 | 2026-09-04 00:25:00 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b2fc1c49-8c35-312b-a05e-2db524c61f98 | -8.11 | -54.782902 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50ee673b-fce0-3997-b972-b33b349fb7b5 | -17.0937 | -56.854801 | 2026-09-04 00:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c25be375-5a53-3689-80f2-869e67e18db6 | -7.5485 | -61.327599 | 2026-09-04 00:25:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36c42fea-7751-3e24-b013-61b25c946bdd | -7.5455 | -61.313301 | 2026-09-04 00:25:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d673cf0c-a4f2-3bc3-8ce2-b1e79f3177e7 | -7.7956 | -63.396999 | 2026-09-04 00:25:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77374ebf-1ecb-3d4c-909e-c750339bf102 | -11.526 | -49.195999 | 2026-09-04 00:25:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7beda514-bfba-3157-b19b-d354d999ec55 | -20.014299 | -50.072899 | 2026-09-04 00:25:00 | METOP-B | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe12704e-c053-32ff-b4e1-6fbc24f03ecc | -18.1315 | -51.799 | 2026-09-04 00:25:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 53824d3b-ceb7-3f12-84f8-b8de87be83aa | -10.4901 | -51.331799 | 2026-09-04 00:25:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b360c077-6a6f-31ef-8fa6-99fef79f91ae | -8.1167 | -54.7668 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22ac07b1-cc83-3455-8ae8-3bdb5e013447 | -20.0109 | -50.057899 | 2026-09-04 00:25:00 | METOP-B | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c33f8e87-fbf3-3b94-ac30-5e952079a71b | -21.458599 | -48.665901 | 2026-09-04 00:25:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3e083f19-f38d-300b-b174-f3342e687526 | -18.1527 | -51.801601 | 2026-09-04 00:25:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
