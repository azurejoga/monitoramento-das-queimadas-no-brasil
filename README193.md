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

## Dados Diários - Página 193

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9a19d97-123b-38ee-a192-43fd151c5e30 | -2.2444 | -48.4017 | 2024-10-25 18:45:18 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 448da085-8f75-3032-9c4e-15f5665643b6 | -2.6473 | -49.5225 | 2024-10-25 18:45:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3d602c93-e298-3172-b7ca-74e6a4826076 | -2.6658 | -49.5008 | 2024-10-25 18:45:20 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 28179473-03d5-38ef-940f-688720a65962 | -2.6473 | -49.5013 | 2024-10-25 18:45:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 82679840-7e69-3b17-933f-2245e4620c4c | -2.8556 | -53.3256 | 2024-10-25 18:45:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2ece29f4-df43-3681-841e-f112b3e886ea | -3.1281 | -54.286 | 2024-10-25 18:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 906eb53b-6201-37f8-bd55-4eec8c01b3aa | -3.2912 | -46.0731 | 2024-10-25 18:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 69e376ad-4404-3a4b-ae59-d01aa7270c20 | -3.3041 | -43.5078 | 2024-10-25 18:45:24 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e143998a-d3b2-335a-b84e-65ce6b57001d | -3.5977 | -44.369 | 2024-10-25 18:45:25 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 70792e84-3400-3912-9718-3d22a9e23aa2 | -3.4469 | -52.6386 | 2024-10-25 18:45:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| e9acc44a-d4d5-3c3b-aa31-3dcb589922ef | -3.4951 | -54.4366 | 2024-10-25 18:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 282.3 |
| b4f67f07-64aa-33e7-aea4-159e1621ce6e | -3.5978 | -44.3462 | 2024-10-25 18:45:25 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| d13c16bf-d65a-3978-98dc-a40c5a82d5f0 | -3.5056 | -44.1672 | 2024-10-25 18:45:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2a572474-7338-3d45-b280-b7c4ee0801b2 | -3.5495 | -46.4178 | 2024-10-25 18:45:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| bdcdb142-7b3b-3d76-a477-168b4813db5a | -3.4767 | -54.4371 | 2024-10-25 18:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| cd265686-2131-35e1-a742-0dfdb2f1c8c8 | -3.447 | -52.6182 | 2024-10-25 18:45:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 1cfa715f-0ee0-35cd-9487-c75b5d3520b9 | -3.4211 | -54.5787 | 2024-10-25 18:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| c24fb7d0-f87b-37ea-8cd2-bee13423127e | -3.7204 | -42.5063 | 2024-10-25 18:45:26 | GOES-16 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| c91b0aa2-bc77-3a49-b496-cded32b4cecc | -3.6381 | -55.5084 | 2024-10-25 18:45:26 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| f34413d2-8975-3a67-b762-3932aa5af15a | -3.6197 | -55.5089 | 2024-10-25 18:45:26 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b1b06f9c-7e3c-36b9-8f81-dab5c9a0388e | -3.7206 | -42.4827 | 2024-10-25 18:45:26 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 040677f5-d3be-3247-8849-d795b37fbf52 | -3.8144 | -48.9729 | 2024-10-25 18:45:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| d11d64d1-b58d-3cfd-8e1b-b82977f0dadf | -4.1287 | -42.9543 | 2024-10-25 18:45:28 | GOES-16 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 586.3 |
| 64442301-156f-3c84-8f47-9f2bb9018503 | -3.9462 | -52.2538 | 2024-10-25 18:45:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 08a4b728-4e2b-3741-b723-f2dff2fa29ce | -4.416 | -41.9929 | 2024-10-25 18:45:30 | GOES-16 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 190.8 |
| 8f094968-1110-3514-b6cc-f9d3628ba372 | -4.4214 | -43.8671 | 2024-10-25 18:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 347.2 |
| 5080b3f3-dddf-3a50-8b58-92b5e0107fa8 | -4.298 | -48.6309 | 2024-10-25 18:45:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 509b68ad-9f8d-3740-b8af-a8aaf2f5a2e4 | -4.7445 | -45.6679 | 2024-10-25 18:45:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 83213e09-d180-351b-b06e-7182cd4fbff9 | -4.7203 | -43.8492 | 2024-10-25 18:45:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| fcbf52ee-3850-379d-864f-735adbf04a5e | -5.189 | -43.68 | 2024-10-25 18:45:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 1d36c0f0-4758-3ba7-956f-3d761cb5ffdd | -5.2471 | -45.7721 | 2024-10-25 18:45:35 | GOES-16 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| f8c47d9d-35ad-3f2b-b9c7-d8b3cd8f7fd2 | -5.3987 | -41.107 | 2024-10-25 18:45:35 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| 348e86d5-a6ab-385b-bd8f-376c913d94eb | -5.3553 | -46.2344 | 2024-10-25 18:45:35 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 710bb15a-6e04-3a1e-a3b4-4415593fe14e | -5.7014 | -45.0199 | 2024-10-25 18:45:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ba355504-1a4a-3f3c-b266-1075b382d997 | -5.7016 | -44.9972 | 2024-10-25 18:45:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e04c3254-62ac-3ac2-8a37-04849dac04e5 | -5.5688 | -49.9941 | 2024-10-25 18:45:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 0c1a0c6d-8925-3fdf-b808-43292098f9b9 | -5.6406 | -43.4153 | 2024-10-25 18:45:37 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5007f708-b0ac-3ece-827d-ef77951223c4 | -6.299 | -49.3125 | 2024-10-25 18:45:41 | GOES-16 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 39a75b2f-97e6-3ed7-9243-4f2985e8db6f | -6.2742 | -47.8471 | 2024-10-25 18:45:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| eccb5ea0-6b03-39ef-903e-a9c626351f27 | -6.2744 | -47.8253 | 2024-10-25 18:45:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 149.7 |
| ff76e05e-1c32-37c7-8ec9-558e52202eb4 | -6.7045 | -43.9554 | 2024-10-25 18:45:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 89f401b3-4928-30c4-8d39-0316b57389a2 | -6.8927 | -38.987 | 2024-10-25 18:45:44 | GOES-16 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 79.7 |
| ba118383-62a9-3d7c-8995-3000aa0d061a | -7.1092 | -46.5065 | 2024-10-25 18:45:45 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 2999821c-7cce-3e1e-8fd2-6db561a28462 | -6.9527 | -47.1834 | 2024-10-25 18:45:45 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 1b84a2ca-c7cf-3e6e-8588-7ea5a44533cf | -6.9952 | -46.6714 | 2024-10-25 18:45:45 | GOES-16 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 199.9 |
| cd5e8ffe-b0c0-38dc-9b47-e900efab6dce | -7.1625 | -46.7908 | 2024-10-25 18:45:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 31bbe74e-d3df-37a2-9907-3ea9f7eb2449 | -7.3131 | -44.98 | 2024-10-25 18:45:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a4f4015b-9978-3c51-80cf-71a246205e45 | -7.1673 | -46.3233 | 2024-10-25 18:45:46 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 7e9385a9-eb67-310f-800d-c25152c1f9dc | -7.2943 | -44.9817 | 2024-10-25 18:45:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 9d1ae9ac-e127-31f9-861a-39d099b3f940 | -7.2073 | -47.9087 | 2024-10-25 18:45:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c0bfaf5b-a12b-3134-bb03-4327da611d9c | -7.1861 | -46.3217 | 2024-10-25 18:45:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 0db52af6-f017-3b83-8f55-0274d88bbb2f | -7.3263 | -47.2413 | 2024-10-25 18:45:47 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| d354f5e0-94a1-33a8-b7ba-bc2a0bdad928 | -7.5477 | -45.8417 | 2024-10-25 18:45:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4bc08127-3d8a-3ef4-bbf1-8ce001fcb35a | -7.5289 | -45.8434 | 2024-10-25 18:45:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c91ba23b-f72c-3a58-b961-ee20f4c6fb0c | -7.8727 | -45.3593 | 2024-10-25 18:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| b7668971-3606-3be5-a26d-8b6f38373dcc | -7.7321 | -61.3745 | 2024-10-25 18:45:50 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 08bd59d4-7571-3e1d-bec4-1ff5126e6f59 | -8.7667 | -44.7186 | 2024-10-25 18:45:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| d3a1ad8f-de2a-3985-851d-52283d9e52e7 | -9.0635 | -48.0051 | 2024-10-25 18:45:56 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| c3cc1b6a-2f1e-3c4c-ad3b-1bd1c075443a | -9.2024 | -43.3429 | 2024-10-25 18:45:57 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 9ba93e0c-887c-311d-9792-70b0d81da614 | -9.1503 | -47.1146 | 2024-10-25 18:45:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 0c9d2b45-df6f-314b-a902-05b2970d0e95 | -9.5073 | -47.2319 | 2024-10-25 18:45:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 680df9a6-42d0-36b9-a021-971f62d36a08 | -10.5091 | -44.8517 | 2024-10-25 18:46:04 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| a0dd7781-4088-39be-b262-b20b65433a9c | -10.5087 | -44.8748 | 2024-10-25 18:46:04 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 06a4fe1e-3254-31cf-b2c2-491e92384d9d | -10.6249 | -55.9757 | 2024-10-25 18:46:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 129.4 |
| d4936404-fcfc-3cf5-95fa-f46fb49ce3b3 | -11.5357 | -43.9853 | 2024-10-25 18:46:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 46ff40a5-4ae7-3fec-9ed1-8f8c8f0d3d7e | -11.9028 | -43.8348 | 2024-10-25 18:46:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 6a9a5767-19a0-3151-8e0e-b3a74079f5b0 | -12.6805 | -43.4235 | 2024-10-25 18:46:16 | GOES-16 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5b6eea81-be05-3530-a140-868ff48f3bee | -13.0364 | -43.0272 | 2024-10-25 18:46:18 | GOES-16 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 114.9 |
| bd5bd392-f1c4-37c4-b45f-8c074cbc3af6 | -13.4913 | -43.4955 | 2024-10-25 18:46:21 | GOES-16 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 6e77f94f-1007-3e32-a774-5dc949cf1622 | -14.4164 | -42.1577 | 2024-10-25 18:46:25 | GOES-16 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 04d728d4-263b-37af-b7c5-4e90843a32fd | -14.4169 | -42.1331 | 2024-10-25 18:46:25 | GOES-16 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 3e1e9556-c2e8-35ac-a0ab-0c6aac2e5854 | -17.7634 | -57.5937 | 2024-10-25 18:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.8 |
| 227bdd24-04fb-3466-ad9d-3dab4c1361de | -17.7443 | -57.555 | 2024-10-25 18:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 314.8 |
| 1dc30cd7-a26f-3e39-ad78-09f648e8eadd | -19.5272 | -56.6591 | 2024-10-25 18:46:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.3 |
| 492d1ad5-426f-317e-9e13-d8c2582c8c2f | -19.7266 | -56.7147 | 2024-10-25 18:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| f47682dc-8d93-384a-a8af-05282c4e4851 | -19.6453 | -56.7681 | 2024-10-25 18:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 119.9 |
| 2d100e00-6e0d-399b-b3cd-3ef0a2e5912d | -19.7061 | -56.7386 | 2024-10-25 18:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 9063ee54-a21a-3d37-a037-3fbe364fca91 | -1.0368 | -53.5171 | 2024-10-25 18:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 065f5abc-1b1b-3648-b31c-e919d26e9c0c | -1.1834 | -53.6569 | 2024-10-25 18:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c3a240ff-ef67-37fd-86db-4fc217034917 | -1.2762 | -52.9275 | 2024-10-25 18:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 7f61ccd4-46ad-3ee4-841f-18e5c4316e84 | -1.1834 | -53.6771 | 2024-10-25 18:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a298e3db-c7b5-3444-8c0f-a36ea98304c2 | -1.4004 | -55.8468 | 2024-10-25 18:55:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c884f801-a802-35f4-a25c-5cd20d684f78 | -1.382 | -55.847 | 2024-10-25 18:55:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 3304789f-3bb2-3174-bae2-ce1b8b76bc38 | -1.3637 | -55.8472 | 2024-10-25 18:55:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 6ac305e6-6ad3-37c4-bce1-4b27b7110687 | -1.4918 | -55.9443 | 2024-10-25 18:55:14 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5be5cd92-a829-388f-ac3b-b7f5e7161069 | -2.0232 | -55.7798 | 2024-10-25 18:55:17 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 544fd45f-e2ff-3c85-af3a-ee98688fa08d | -2.2444 | -48.4017 | 2024-10-25 18:55:18 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 53eb9888-0048-3635-90d7-b6627d31c070 | -2.6473 | -49.5225 | 2024-10-25 18:55:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 08dbca5a-8099-3871-92c4-eb49e47b1a05 | -2.6658 | -49.5008 | 2024-10-25 18:55:20 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b1114f39-106e-39bc-b80f-53fcf6c5e42a | -2.6657 | -49.522 | 2024-10-25 18:55:20 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 670ba383-2e5e-3cab-9027-8f99a387b4c4 | -2.6473 | -49.5013 | 2024-10-25 18:55:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 1882d92e-a032-369a-86f8-aec873bea208 | -2.8502 | -44.9905 | 2024-10-25 18:55:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 27639017-45ff-3954-9fb1-076c913e6143 | -2.8684 | -45.0803 | 2024-10-25 18:55:21 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 275f2ae1-da94-3e85-9adc-5effd83b375c | -3.2172 | -50.1811 | 2024-10-25 18:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 410738b8-c4ca-3ff8-9d25-31722beac8f0 | -3.2912 | -46.0731 | 2024-10-25 18:55:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| e3a064dd-aa87-3c98-a4ae-20a54817d502 | -3.3041 | -43.5078 | 2024-10-25 18:55:24 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 025823b3-22ec-3e98-87ce-3e903a82a123 | -3.4767 | -54.4371 | 2024-10-25 18:55:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 9dc3283f-4487-3f2e-9148-31e7c53680cf | -3.4951 | -54.4366 | 2024-10-25 18:55:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 215.7 |
| 1bed437e-eefe-3061-84f8-104b40c4165e | -3.4211 | -54.5787 | 2024-10-25 18:55:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 1db926dc-b3c4-3bbc-84b6-5cf74230eeda | -3.7099 | -44.2952 | 2024-10-25 18:55:26 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |


[Clique aqui para ver as próximas entradas](README194.md)
