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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fa0e21d-f659-3836-ba8c-8ff40519b6e2 | -4.3985 | -44.4881 | 2024-10-13 02:45:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e113a436-0171-31bd-b86f-780ffffa0dc9 | -5.1381 | -45.3969 | 2024-10-13 02:45:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a834ff45-6d4f-368e-b531-df292dd57e9f | -7.6815 | -47.3213 | 2024-10-13 02:45:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| b3569b82-435c-3c7e-b1dd-488b56f26898 | -9.7359 | -64.2295 | 2024-10-13 02:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 4b1011d1-ae74-3260-aca9-5d037c8f4630 | -10.5097 | -42.5023 | 2024-10-13 02:46:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 055c1122-0e02-3a2a-9c59-c85427eb85a1 | -10.5094 | -49.9584 | 2024-10-13 02:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 87f5406b-ca79-365e-810f-49002b3aa183 | -10.5281 | -49.9778 | 2024-10-13 02:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 05684e8b-1e70-3de1-89a3-a981f8f959b0 | -10.5283 | -49.9564 | 2024-10-13 02:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 8238db37-e57c-3cbd-b31d-74be9264a71d | -10.9311 | -44.6789 | 2024-10-13 02:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| ab6896a0-9108-3739-9eb0-998868cce804 | -10.9315 | -44.6557 | 2024-10-13 02:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 7b81b8f8-ab90-3755-b34b-bdc4e75d2e61 | -10.9502 | -44.6762 | 2024-10-13 02:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 9e8b3f3e-b548-36f5-baf9-ef50467ca146 | -10.9506 | -44.653 | 2024-10-13 02:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 684f41d8-a737-3db4-979f-678bf4e126ce | -11.6334 | -48.3736 | 2024-10-13 02:46:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 449e5839-e2c5-3870-88bd-bce9b9737d92 | -11.7308 | -64.9769 | 2024-10-13 02:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 122a314f-b5c9-3e2b-b343-d7076d9f07f5 | -12.4792 | -63.0159 | 2024-10-13 02:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| f2eaa2e7-9d49-3624-a0a5-3acd6a94fd49 | -13.1475 | -62.3215 | 2024-10-13 02:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| fc115404-36f1-35a9-90e5-30f8e84cb3a1 | -15.6419 | -59.9767 | 2024-10-13 02:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| a778d90b-a14d-3fab-8245-8b4031258c21 | -17.2639 | -42.6527 | 2024-10-13 02:46:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 111.2 |
| f6579f97-e472-3f18-9c9a-7ecb17fa9902 | -17.284 | -42.6479 | 2024-10-13 02:46:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| db3b50f3-984a-386a-9a89-b4551e5461e1 | -17.6478 | -56.2668 | 2024-10-13 02:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| c5e7fd29-d5f3-338d-945f-6849723874f7 | -17.964 | -57.3843 | 2024-10-13 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.4 |
| 5a460753-2f67-386a-86ed-d71dfd3cda3e | -17.9643 | -57.3637 | 2024-10-13 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.0 |
| a8cc1ae4-ec3f-39a7-8a0a-d124cbb0d52d | -17.9837 | -57.3819 | 2024-10-13 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 7d22b709-2e18-3f28-85ad-f889f974d94e | -17.9841 | -57.3612 | 2024-10-13 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.5 |
| ac86138f-4763-375a-8109-e3ffcc004714 | -18.2147 | -56.5873 | 2024-10-13 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| dbed0557-e9ac-3a5a-9480-975d82f04013 | -18.2151 | -56.5665 | 2024-10-13 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 20a6f55c-b50c-3970-8034-172af6636aa7 | -18.2162 | -56.504 | 2024-10-13 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 12250b58-ef6e-395a-9b97-3d875579e562 | -18.2166 | -56.4832 | 2024-10-13 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.6 |
| 5d5d4737-9e73-3d24-9e98-99f61af1a1d9 | -18.236 | -56.5014 | 2024-10-13 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 644a654e-b0d3-32a2-85be-31ad529497a3 | -18.2364 | -56.4806 | 2024-10-13 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 162.6 |
| 29c8fad3-6830-35d6-b12a-94b3d35e5271 | -1.733 | -54.173 | 2024-10-13 02:55:16 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 2de3f390-05df-3b8e-97b3-2c376f108c20 | -2.1693 | -48.8108 | 2024-10-13 02:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| dd19e34c-05a2-3cb1-8143-862c554e4230 | -3.0956 | -53.0559 | 2024-10-13 02:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 8fd7ec1f-f456-3805-ae38-62f3adf131e8 | -3.0957 | -53.0355 | 2024-10-13 02:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 10983f7e-d851-3b50-8461-773182883f95 | -3.1141 | -53.0351 | 2024-10-13 02:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f7e774f2-1351-390c-9c60-e9a1c96a0e3f | -3.1607 | -50.4556 | 2024-10-13 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 4334fe59-56f1-37ad-8e9d-836505768452 | -3.1791 | -50.476 | 2024-10-13 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 0bc7a9f2-41dc-34c6-9d65-1530169f2b68 | -3.1792 | -50.4551 | 2024-10-13 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 54a89ab0-5241-306c-be14-a41dae034351 | -3.1976 | -50.4545 | 2024-10-13 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| cb60ff37-ca61-3be3-bacd-2a807697d52c | -4.1148 | -48.2515 | 2024-10-13 02:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 82fa77b2-8df4-3508-a7cb-aa1a31e57e32 | -4.3985 | -44.4881 | 2024-10-13 02:55:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 822aa5d7-f7ff-3288-b9fb-bd66162153ef | -4.3986 | -44.4652 | 2024-10-13 02:55:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 1b0c5772-90dc-3a09-97f1-63382700ec79 | -5.1381 | -45.3969 | 2024-10-13 02:55:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 2e3b9048-08f8-3852-8717-a1ed873dc25b | -7.6815 | -47.3213 | 2024-10-13 02:55:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b76da0d2-dca4-3d64-83c6-daf530c03f08 | -7.6817 | -47.2992 | 2024-10-13 02:55:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| f2919f89-fc1b-3cf4-9f5f-728992405b62 | -8.2352 | -64.0961 | 2024-10-13 02:55:54 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| a6474cbe-ad3b-33fd-97fe-29f5b8660159 | -9.7359 | -64.2295 | 2024-10-13 02:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 46a9c756-9d8e-30bc-b84a-c52f5484690e | -10.5097 | -42.5023 | 2024-10-13 02:56:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 2a4076a5-40a7-3b71-8da5-24fac52bbc29 | -10.5094 | -49.9584 | 2024-10-13 02:56:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 3e4dca4a-ce01-3842-ad21-8db45850a0fd | -10.5283 | -49.9564 | 2024-10-13 02:56:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3ee5ab42-01e5-3f98-84e3-89c01f61a21c | -10.9311 | -44.6789 | 2024-10-13 02:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 7bbadbfd-cd92-3b35-9e8a-e9618b5ff0d1 | -10.9315 | -44.6557 | 2024-10-13 02:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d6949f2b-2399-3763-a308-d81414fac9b6 | -10.9502 | -44.6762 | 2024-10-13 02:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 0c3133f5-8976-3704-924f-ec52cfa4ca72 | -10.9506 | -44.653 | 2024-10-13 02:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 852a27c0-8e2e-3fa5-8fe1-087271d4f998 | -11.7308 | -64.9769 | 2024-10-13 02:56:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4dc7226e-edb5-37b3-995f-7c3123e4cf6c | -12.4792 | -63.0159 | 2024-10-13 02:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c247f49c-7e66-3d66-b8a7-d70a57625d9a | -13.1475 | -62.3215 | 2024-10-13 02:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 45d261dc-66fe-3ca1-bf61-58752cea82de | -15.6105 | -59.4017 | 2024-10-13 02:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 05679a3c-43ae-3da1-a34c-944e181646b2 | -15.6299 | -59.3999 | 2024-10-13 02:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ce81f627-4f8d-3868-b292-8074b667ec00 | -15.6419 | -59.9767 | 2024-10-13 02:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a3cb1ff1-7f1e-3d21-b2c5-04e61b16875e | -17.2639 | -42.6527 | 2024-10-13 02:56:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 74844186-8574-3110-a8a8-dfca70ca7acd | -17.6474 | -56.2876 | 2024-10-13 02:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 216.9 |
| 149bebb9-c784-30de-922c-01b62052d4d9 | -17.6478 | -56.2668 | 2024-10-13 02:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.7 |
| 66d92bde-ea02-3e54-9023-6fc90cde1451 | -17.6672 | -56.2851 | 2024-10-13 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.5 |
| d5f0c67c-4644-303f-8d06-ed77c6942640 | -17.6675 | -56.2643 | 2024-10-13 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.9 |
| abbadcd1-9331-3ccc-8d9e-869e4e20a31c | -17.964 | -57.3843 | 2024-10-13 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.3 |
| f48e40fd-559b-32ba-b86a-499fa2a611d5 | -17.9643 | -57.3637 | 2024-10-13 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.6 |
| 39f49b4a-6c4c-31dd-b5fb-7a238619acc6 | -17.9837 | -57.3819 | 2024-10-13 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 5a2badfd-1178-305d-9951-a4736eb22133 | -17.9841 | -57.3612 | 2024-10-13 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.6 |
| 1f3525ee-feb3-3cfd-9259-8d20c17c8ffc | -18.2151 | -56.5665 | 2024-10-13 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| dd062339-451a-3856-8ec5-ad2f51717fb0 | -18.2155 | -56.5457 | 2024-10-13 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 57b42e1e-3d9f-368f-9207-8f9cfc8dcf4b | -18.2162 | -56.504 | 2024-10-13 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| e5db0257-c7b2-3c23-9cef-c89eda8924cc | -18.2166 | -56.4832 | 2024-10-13 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.1 |
| b7a581ea-ef41-346c-97a3-30fe6ff1a43c | -18.2169 | -56.4624 | 2024-10-13 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 5e686827-377f-3ba4-95ab-0b0d23391904 | -18.236 | -56.5014 | 2024-10-13 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.5 |
| 206ff600-c92a-3007-8d39-f4bef44bca93 | -18.2364 | -56.4806 | 2024-10-13 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 185.1 |
| 11003cf3-3d0e-399c-b3d0-97da7e841c89 | -6.65305 | -37.47073 | 2024-10-13 02:58:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 48e38360-3ddc-3d97-9c4e-1a8e103dbd35 | -6.6587 | -37.47845 | 2024-10-13 02:58:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 12dd8f77-ad6e-316c-9413-08bde215d006 | -9.30344 | -35.6067 | 2024-10-13 03:00:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6ce4ad31-3e34-35bc-9bac-e0adf687f1e6 | -9.29976 | -35.60354 | 2024-10-13 03:00:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f4b256ac-f2c1-38fc-9b75-0a9d311fd28f | -12.78125 | -38.50289 | 2024-10-13 03:00:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5fc14c62-27de-30ca-8576-0dfaaf9713ea | -9.29897 | -35.6077 | 2024-10-13 03:00:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2be5c740-d049-3789-afc8-b98ad19adecf | -1.733 | -54.173 | 2024-10-13 03:05:16 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| c7623c0a-406a-31a3-bafd-56a3e3b2b4ee | -2.1693 | -48.8108 | 2024-10-13 03:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| bf27634e-390e-3b01-aef4-ae2825edc00d | -3.0956 | -53.0559 | 2024-10-13 03:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 77b7126f-6f04-3656-9c9e-f3eab59c90b9 | -3.0957 | -53.0355 | 2024-10-13 03:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 181.3 |
| e0272050-0ba0-376a-a0c5-8336e85a93db | -3.1976 | -50.4545 | 2024-10-13 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 45808cc1-d172-3722-8b2c-a9f5cde3ad28 | -3.1792 | -50.4551 | 2024-10-13 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| b0e034ee-25c6-322e-8cb1-26e1fb545215 | -3.1791 | -50.476 | 2024-10-13 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 3661c22a-5d27-3f35-91e8-e07033a07a0c | -3.1607 | -50.4556 | 2024-10-13 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6c72b8e8-f14f-3888-b0e2-a8714afbe533 | -3.1141 | -53.0351 | 2024-10-13 03:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 46142491-60b8-3440-bc5d-d14d516b0e16 | -4.1148 | -48.2515 | 2024-10-13 03:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 1ee69c3d-86c7-351b-aab1-fd11795a77ec | -4.3985 | -44.4881 | 2024-10-13 03:05:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| fc147448-46bd-333e-bb09-8cf2355c3dbb | -5.1381 | -45.3969 | 2024-10-13 03:05:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 1e09e6e8-250a-33a6-a92d-9f0b0e4fb577 | -5.1239 | -60.3206 | 2024-10-13 03:05:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7f4fdac4-369e-361c-9d6e-683c380d60a2 | -5.1238 | -60.3397 | 2024-10-13 03:05:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| fcb47f4b-a7df-37f0-8bf7-4b64dd5fdfbc | -7.6817 | -47.2992 | 2024-10-13 03:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 61afbab2-2c2f-30de-8c50-45b93eb72053 | -7.6815 | -47.3213 | 2024-10-13 03:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8089600f-245f-3e7b-aabd-c23af0326e18 | -7.6627 | -47.3229 | 2024-10-13 03:05:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 73d015f7-a3ff-3cd6-b138-50bdd0a45eef | -8.2352 | -64.0961 | 2024-10-13 03:05:54 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |


[Clique aqui para ver as próximas entradas](README33.md)
