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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83840868-4b42-3bf1-9251-51449c079a94 | -3.4185 | -61.3273 | 2026-08-31 18:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 555f1549-c1f5-3f71-9f40-e45e75611e5e | -3.6076 | -59.0769 | 2026-08-31 18:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 62f137eb-0523-3756-8036-590a7512de9d | -12.1113 | -45.0163 | 2026-08-31 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 18bc3deb-e09f-336c-ac5a-c53bbdc902b1 | -6.1295 | -57.6637 | 2026-08-31 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 4323d4ae-92fd-3415-b59a-75ccf78b8654 | -11.2298 | -51.2456 | 2026-08-31 18:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 121404ea-5a7a-3264-aa6c-047349a06322 | -10.5149 | -59.6184 | 2026-08-31 18:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 5fa36aa6-fd4a-37d2-8410-ed1df515a5e5 | -3.4167 | -43.3867 | 2026-08-31 18:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 61fbdf7a-a94d-3081-8d10-288b68ef7d4f | -11.0434 | -49.6851 | 2026-08-31 18:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 58fcfeb3-afa6-35f5-9041-fb6d20e514ad | -11.2485 | -45.0963 | 2026-08-31 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 7b889b8a-687c-35c2-8461-daf106d1dada | -8.6012 | -70.2192 | 2026-08-31 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 2b90a872-5524-3eff-bb35-47a164e84356 | -10.4793 | -64.5201 | 2026-08-31 18:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 0dfd37cd-63f4-3fa0-ab86-13e52d87ed37 | -3.1449 | -61.1808 | 2026-08-31 18:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 190.1 |
| e091acb4-e67a-3459-a724-b88eab2f2ebf | -8.803 | -70.84 | 2026-08-31 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c6ed1066-013a-3f10-a5eb-513888ebf58b | -8.9664 | -62.4076 | 2026-08-31 18:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ec6a8a26-e035-30f9-8d1a-ab4e40c0cb4a | -9.7126 | -65.0951 | 2026-08-31 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 60853371-ad0d-3571-b8c9-caf438660e01 | -13.471 | -57.0373 | 2026-08-31 18:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 73190317-33f2-3a75-9857-44163a023705 | -9.0245 | -65.3994 | 2026-08-31 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 1c019105-859e-3704-8f85-66723a7f8f19 | -9.2256 | -59.7894 | 2026-08-31 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 24a2be5a-a0ae-3859-9887-023a8bf763f3 | -6.8568 | -59.4757 | 2026-08-31 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| cc219b00-24c5-3d84-b6eb-32264897cbd8 | -9.4153 | -45.6726 | 2026-08-31 18:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 7d705701-ae69-35d4-a00b-d00cc450448e | -8.9428 | -63.2797 | 2026-08-31 18:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 87c46a28-5a0d-32f1-a758-c3f825ea76f0 | -7.2255 | -42.7616 | 2026-08-31 18:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 47.1 |
| e23218ad-d5b5-393f-b7a9-bb0e8cb88b0d | -10.844 | -45.3356 | 2026-08-31 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| fb25bb8a-5b17-3efe-b99f-0205aa2c1c2a | -9.1529 | -59.5609 | 2026-08-31 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7f0e0cec-dccf-3dbe-8c4e-d5357186923b | -7.4734 | -61.4037 | 2026-08-31 18:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 00bc8669-bae7-3d33-9067-6f323d26bb7d | -10.7271 | -50.6405 | 2026-08-31 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 9d32fde6-48de-3414-95d3-64f7b65a83dd | -15.6139 | -56.4103 | 2026-08-31 18:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 4cf089f5-c115-356d-b71e-4d2829aa983f | -7.3119 | -60.5706 | 2026-08-31 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 6cb4ad45-9016-3956-af7d-a6bad65bbf00 | -5.8692 | -52.0868 | 2026-08-31 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 44350fa4-b328-3ef0-8abf-ffcb82aaa1a1 | -10.8218 | -50.6306 | 2026-08-31 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 4c0745ff-9c98-33de-aa70-ab3ab0ab37cf | -14.4641 | -52.1964 | 2026-08-31 18:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 047e547b-9514-3005-8eee-8f9377d2b367 | -13.9667 | -54.4157 | 2026-08-31 18:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 4e7fddcd-ffa9-3c99-ae67-e9825a18b3bd | -14.5222 | -52.1887 | 2026-08-31 18:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 23226408-ad87-33df-9eae-868c770209c3 | -7.2934 | -60.5713 | 2026-08-31 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 168.3 |
| bf5cc1d8-0758-3bab-aaef-cb8c45b77ed8 | -8.9514 | -70.5627 | 2026-08-31 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c8090593-f921-396c-9554-ee46f7e63b6a | -6.8613 | -41.6532 | 2026-08-31 18:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 98cd92d5-b709-3d47-a689-9e916c6600ef | -11.2103 | -45.1017 | 2026-08-31 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 250.1 |
| 167e5579-6ec6-34d5-93b6-fdc573614f4f | -9.2099 | -59.4027 | 2026-08-31 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 055b2015-27aa-3786-8e4d-6c4f0bfe134a | -18.27 | -52.7068 | 2026-08-31 18:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 280.7 |
| 27ab1990-5873-3db7-a19b-8e8314186c0d | -8.1345 | -45.4923 | 2026-08-31 18:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| f8f05ac1-4f76-3538-9393-0b862b42ddae | -6.9368 | -55.6161 | 2026-08-31 18:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| e87733e0-1442-3fc3-b333-36a179565949 | -10.9355 | -50.6186 | 2026-08-31 18:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ee5fc95f-2a5a-3b55-bff5-d8ef03a855b2 | -8.7968 | -62.8695 | 2026-08-31 18:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 8e741d2d-e4d7-34f9-810e-e2c875ba9f69 | -9.6049 | -68.5979 | 2026-08-31 18:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 19c77705-1d12-3dd5-8eab-669d496f40f3 | -14.2369 | -51.9498 | 2026-08-31 18:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 9f9a5688-473a-3461-a63a-564af02237a9 | -11.9378 | -45.0656 | 2026-08-31 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 27590790-1a7f-3517-82aa-d4dc8ddf665d | -8.5555 | -66.9574 | 2026-08-31 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 6472e8d7-198a-3572-8f56-c8f13b05ac9a | -8.5739 | -66.9754 | 2026-08-31 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| c86d8bca-dd51-36b5-9535-f071e60ad635 | -9.6939 | -65.1145 | 2026-08-31 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 758.7 |
| 537160ee-63dd-3128-9831-12259168132d | -3.6399 | -60.5466 | 2026-08-31 18:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 139.6 |
| c3956b17-28b1-370e-a2ed-4f0ca18f0f13 | -3.7931 | -65.1119 | 2026-08-31 18:00:00 | GOES-19 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ffd898fb-45af-3268-924b-7d7a74cdad92 | -10.7081 | -50.6425 | 2026-08-31 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 283d9b9a-b864-3059-b682-df0e75e6bed5 | -9.12 | -61.6011 | 2026-08-31 18:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 24d83c2a-1e30-30ef-a5b1-417e87213841 | -8.2229 | -54.9412 | 2026-08-31 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| fca1a7f4-e57e-35f7-9471-89b4378b5f97 | -11.1995 | -55.1008 | 2026-08-31 18:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 5f985529-ae26-3a8b-880d-e0248d159215 | -6.9121 | -59.4734 | 2026-08-31 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| fd4a556c-b188-368a-a1cc-36abb266832b | -14.5028 | -52.1913 | 2026-08-31 18:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 41e0b944-e628-326b-be52-1e9c0498586f | -6.8419 | -41.7032 | 2026-08-31 18:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 4bfcd432-5c08-3dab-ba7b-1e04a42fa663 | -8.948 | -62.3894 | 2026-08-31 18:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b98bc942-8546-3fd3-b4fe-5347993c5fa7 | -6.6542 | -59.426 | 2026-08-31 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 6e45e6d7-dfa4-3351-a83f-f8a4831dcca3 | -5.9636 | -57.6704 | 2026-08-31 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| ecc39dcf-de61-3b36-9d53-d0a8d6936601 | -8.499 | -55.3051 | 2026-08-31 18:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 61e48bad-748b-3b02-913e-ed7daae46da6 | -3.1997 | -61.1799 | 2026-08-31 18:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| dbd2e8c0-62fb-39a8-bec8-42179a63a7e2 | -11.175 | -54.001 | 2026-08-31 18:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| df157483-8a83-3e02-a554-571602da8743 | -9.9708 | -53.9419 | 2026-08-31 18:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| ee871341-2b79-3530-9bc3-6d98532929fb | -12.1905 | -50.5194 | 2026-08-31 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 048486ba-e2ab-3df1-847c-40c51e069f08 | -8.8026 | -71.0783 | 2026-08-31 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 2969ae15-88b3-353a-b1b0-81388ca621a7 | -9.694 | -65.0958 | 2026-08-31 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 19981513-4a08-3efe-b5da-eba19977c90a | -10.5149 | -59.6184 | 2026-08-31 18:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| fe937ce8-3281-301a-97ae-a522d8249d4f | -7.4803 | -63.7267 | 2026-08-31 18:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 98819722-c26a-3e52-9b64-d84cdf223555 | -11.1915 | -45.0813 | 2026-08-31 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 0a81693d-e7fa-359b-a926-dbb70e532ff3 | -14.4641 | -52.1964 | 2026-08-31 18:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8996fdbc-9826-3252-9499-48efb123ec76 | -12.0925 | -44.996 | 2026-08-31 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 238.5 |
| 10132f78-2167-31f5-bb91-e3ffaf9e924a | -7.2934 | -60.5713 | 2026-08-31 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.1 |
| b1b42b61-f23a-353a-9f54-cd5574fc81dc | -9.6049 | -68.5979 | 2026-08-31 18:10:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 110.9 |
| a93f194a-c282-391a-a42a-2e91da2c0a1b | -3.4107 | -64.9137 | 2026-08-31 18:10:00 | GOES-19 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| f55e0238-66c6-3c03-93cc-9ffa50158f80 | -16.0153 | -54.4168 | 2026-08-31 18:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| bc07dd72-5e29-3b44-abea-6d7486473891 | -8.9428 | -63.2797 | 2026-08-31 18:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| d2785715-50a7-3154-b100-622894d9a8c1 | -6.2537 | -55.4308 | 2026-08-31 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 06c6e148-02ea-386d-bebd-8b86895289fb | -9.173 | -59.3659 | 2026-08-31 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3adea66c-8e25-30ce-9204-c5a77be679af | -8.4896 | -70.6243 | 2026-08-31 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 84.3 |
| b48ae7b9-da14-3ff4-9445-c1ebb9a64ae0 | -9.6683 | -50.8511 | 2026-08-31 18:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 4555202c-1db9-3832-844a-04fe404f4c19 | -13.967 | -54.395 | 2026-08-31 18:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 140.3 |
| f2fcf980-0652-311c-aec4-f5ace63088fa | -8.87 | -66.9121 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 50bd5249-da8d-300a-8565-350516136095 | -3.9708 | -60.0067 | 2026-08-31 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| d773b3ff-4bee-3cfb-9635-b79ebd707856 | -8.9514 | -70.5627 | 2026-08-31 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4f7743a1-a4cb-3d89-a5be-92a97a9c1896 | -3.6398 | -60.5656 | 2026-08-31 18:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 215.4 |
| ac0c0d20-286a-340d-a897-01983a623dc5 | -8.574 | -66.9569 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 28ab452e-f890-3e59-ad86-333323880197 | -9.1711 | -59.618 | 2026-08-31 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 30d0bdcd-e426-32ff-9699-78ec1dba5b2e | -10.9865 | -48.3869 | 2026-08-31 18:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9c4fae86-d8b6-31f1-92e4-c8b79ac51093 | -5.9636 | -57.6704 | 2026-08-31 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| c7097ad8-52f2-38c0-9440-aaff5d05ce99 | -8.9295 | -62.3712 | 2026-08-31 18:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8112329b-1494-3eea-9c21-e3b4d4126214 | -8.5555 | -66.9574 | 2026-08-31 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3b432a9d-ebd0-3bc2-ab16-9141d54eadea | -6.7514 | -55.6654 | 2026-08-31 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 7c7a36ac-62c4-31c6-bd7e-50576d89b919 | -14.4835 | -52.1938 | 2026-08-31 18:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 563fa6ea-b36c-32d9-a569-66dd37640003 | -7.5662 | -61.3049 | 2026-08-31 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7488116e-b8a7-30d9-b82e-d935f666a5d0 | -9.2256 | -59.7894 | 2026-08-31 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| de4132d2-2eda-35a8-9ba6-3013ab2c86e8 | -6.857 | -59.4371 | 2026-08-31 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| dc34a55d-98c7-3047-a667-c9e7abebe285 | -6.1293 | -57.7028 | 2026-08-31 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 7f6a19f9-2fa6-30ae-8d94-23e4efe1fe6b | -7.2745 | -60.6486 | 2026-08-31 18:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |


[Clique aqui para ver as próximas entradas](README182.md)
