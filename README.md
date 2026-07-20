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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c39ceae8-1fe3-346c-ba0e-77887d678c5d | -27.2395 | -51.58831 | 2026-07-20 00:11:00 | TERRA_M-M | LACERDÓPOLIS | SANTA CATARINA | Brasil | 4209201 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2add2cb7-095d-3259-91c5-5880f95a1f63 | -23.38851 | -47.52169 | 2026-07-20 00:13:00 | TERRA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| d7549f7d-22a5-37fe-a435-a090f34fb6b8 | -23.05529 | -46.88822 | 2026-07-20 00:13:00 | TERRA_M-M | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| aa06950a-522b-3fb3-b659-8d1a238a02ea | -22.90829 | -43.46928 | 2026-07-20 00:13:00 | TERRA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 74f35ad7-cdd3-3d5f-95dc-9a6a62ae7f6d | -21.62438 | -41.2424 | 2026-07-20 00:13:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 6e8c5063-4f54-3f6a-a470-11738993e3ed | -23.38708 | -47.51184 | 2026-07-20 00:13:00 | TERRA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 347.6 |
| 17ba0539-47f5-3ca2-9a03-378fe9c17c76 | -22.61918 | -47.81011 | 2026-07-20 00:13:00 | TERRA_M-M | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7cc14d55-05ed-374b-97e6-3d270be345fc | -18.68313 | -52.65282 | 2026-07-20 00:16:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5a8161d7-271c-35ea-8c8e-95aaf325e064 | -10.4729 | -49.10009 | 2026-07-20 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 183cf3a4-33f4-3e43-877d-bc776d1ddb6f | -10.90549 | -56.3744 | 2026-07-20 00:18:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 91950a58-c1ea-3092-807f-cf311ff57534 | -10.80116 | -50.22884 | 2026-07-20 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| a37cb938-729f-3457-9f22-a2d74d1a1b2a | -10.55731 | -56.33362 | 2026-07-20 00:18:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 8350cf62-33bb-3f62-a55a-e6bcfe482416 | -10.46194 | -49.09116 | 2026-07-20 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0b3c3094-08ca-3c3f-8f73-5c7c1573f32f | -10.90359 | -56.35902 | 2026-07-20 00:18:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 3ba9725b-6d39-37d0-97fa-f2003dfe27ba | -9.10126 | -59.39878 | 2026-07-20 00:18:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 018a1f46-817f-3419-a30e-3166f7563264 | -10.46344 | -49.10143 | 2026-07-20 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 71ce784d-422a-3df4-b44d-4af31040217b | -7.91476 | -48.26606 | 2026-07-20 00:18:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4832d9cc-75a2-3ee3-ac00-9418c0e7f74e | -10.80247 | -50.23809 | 2026-07-20 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0c5e2db2-1440-33bb-aeea-18d2d2003444 | -8.93959 | -47.60842 | 2026-07-20 00:18:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 968a4f54-9497-374f-9080-7355c2f30888 | -9.09731 | -59.40561 | 2026-07-20 00:18:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| c68793e2-0f17-366e-a1bb-b386a449b547 | -10.68776 | -49.62259 | 2026-07-20 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| f5ab2f67-6adc-3ee1-9010-d763b13f3d67 | -10.81014 | -50.2275 | 2026-07-20 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 21532e01-04b7-36e7-8de7-dfcd9ca1ede4 | -7.91101 | -48.26077 | 2026-07-20 00:18:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5e6b9580-12b8-3a4b-9d1f-e40044a5f86c | -9.17561 | -59.06923 | 2026-07-20 00:18:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| c5c49ad3-ec47-363f-bd78-370795ab0f69 | -13.68476 | -48.80394 | 2026-07-20 00:18:00 | TERRA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 88bafdb7-331a-3bb0-b3cc-8d0ba568188a | -11.97896 | -55.51864 | 2026-07-20 00:18:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3b6c7649-e184-371d-8f0e-7f94a826e45d | -10.68914 | -49.63231 | 2026-07-20 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 58128c5b-4f68-37b6-8abd-e49eec5a7bf6 | -6.72354 | -48.1154 | 2026-07-20 00:20:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 248863bd-5268-3bd3-957f-700aaeb563d6 | -6.73986 | -47.21985 | 2026-07-20 00:20:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| b34f3a0c-57c3-3703-83b3-4efe913ecd73 | -6.73768 | -47.2137 | 2026-07-20 00:20:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 9de29014-b048-30c6-8e03-94a035cc1e65 | -5.62766 | -47.10135 | 2026-07-20 00:20:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6a3ab2f5-58ae-3b40-a1bd-0c12919e1e53 | -6.59451 | -51.70673 | 2026-07-20 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ebf8d09b-d20d-3f02-aec0-143f57732a02 | -5.6326 | -47.10735 | 2026-07-20 00:20:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0f7e16db-2f15-3dd9-9db3-14bd6b755d0a | -5.70899 | -45.66384 | 2026-07-20 00:20:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| e09acacb-b20a-3df1-bb5e-8ea703888811 | -10.9027 | -56.3751 | 2026-07-20 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 60d7a211-5b3c-3b4e-a436-93bfadc458a8 | -9.0935 | -59.400501 | 2026-07-20 01:19:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95eea605-7753-34b3-ba5d-ac0b85514398 | -13.0127 | -62.159901 | 2026-07-20 01:19:00 | METOP-B | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d4f0ea68-1fe0-334b-86c8-6f1f77fb1519 | -10.9006 | -56.349899 | 2026-07-20 01:19:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6984826-3ea3-3daf-9ae2-b9fb107f2d69 | -10.891 | -56.352402 | 2026-07-20 01:19:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43f7dc84-cb10-3a05-a54a-618cb33f7181 | -11.9694 | -55.5194 | 2026-07-20 01:40:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 4f75542b-7aa2-338b-97bb-61a7522fdbbf | -12.9959 | -62.154301 | 2026-07-20 01:43:00 | METOP-C | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ea22078-2c93-3a68-8a83-d06c7b205ad7 | -11.9844 | -55.5271 | 2026-07-20 01:43:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b241873e-b0c1-3ce1-b2d8-e719e103aa49 | -13.0189 | -62.1642 | 2026-07-20 01:43:00 | METOP-C | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 29e7f6f7-6e01-3d8e-aa7b-82f37c863445 | -11.98 | -55.509998 | 2026-07-20 01:43:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b29e204-a288-3ba3-92b1-f74e3012c96d | -10.9043 | -56.350399 | 2026-07-20 01:43:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80e0842e-b817-3b80-9a52-e96f91f5be51 | -10.9083 | -56.366001 | 2026-07-20 01:43:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| babd8eb5-573c-3fb4-847d-7294b663567f | -9.1007 | -59.4044 | 2026-07-20 01:44:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2b148ce-1ec6-3152-b816-44ecd23ade78 | -17.80552 | -42.24719 | 2026-07-20 03:08:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0a143452-01df-38d5-9154-32feab4759f2 | -20.96333 | -40.97567 | 2026-07-20 03:08:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a32bfac9-3dbe-33d7-9b65-eef0c93f4afa | -20.96124 | -40.97714 | 2026-07-20 03:08:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2bd9036b-d5fd-3fcc-8fc2-610d1a1e8609 | -17.80431 | -42.25226 | 2026-07-20 03:08:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5eef1ced-4681-3c98-b320-7bca627bafd1 | -17.80382 | -42.25168 | 2026-07-20 03:08:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 209487b7-efe0-3990-96df-39aeb94ec1cc | -22.88877 | -42.95827 | 2026-07-20 03:10:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ab30e328-0668-3acd-8d62-e68aadad03cd | -5.67189 | -43.57372 | 2026-07-20 03:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8fed4bc-23d8-3642-904d-e043f62dd792 | -6.73918 | -43.13985 | 2026-07-20 03:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c000df82-5517-3029-9eb2-91760a9ac46c | -7.1158 | -44.03291 | 2026-07-20 03:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5657e05-6798-3578-aada-a95b6040bb53 | -6.73999 | -43.13544 | 2026-07-20 03:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adf33d78-db94-313b-b4ed-b77f762fc430 | -6.86248 | -38.35355 | 2026-07-20 03:40:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 123739f7-34d5-36a3-9e6b-ccefeea054dd | -5.79275 | -45.11729 | 2026-07-20 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cda76916-d57a-3c00-b71a-aecfba3d6a0e | -7.1167 | -44.02803 | 2026-07-20 03:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38718aea-537c-38d8-94f1-057c66a1452e | -6.74594 | -43.13655 | 2026-07-20 03:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4234544b-dbb4-3453-8bf0-2bc134325fd4 | -11.83797 | -44.78432 | 2026-07-20 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18fa62f6-11b2-3aba-9dec-f6edc3700aad | -13.29316 | -44.61704 | 2026-07-20 03:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f296aabb-96c7-3eff-91e6-b210e91dbd2b | -13.29124 | -44.61954 | 2026-07-20 03:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38df4b5a-d2c8-3cee-8a5a-8cf094543e8a | -11.83196 | -44.78295 | 2026-07-20 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64010dd7-37a9-3a02-a66f-39688abb0be8 | -11.83296 | -44.77788 | 2026-07-20 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bd76dad-a515-3b79-adb9-d9057309231b | -11.83187 | -44.78468 | 2026-07-20 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1695dbec-180b-346a-a0e0-1c43f9110be6 | -11.82874 | -44.76746 | 2026-07-20 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9bac727-5c1a-3aaa-adcc-c6a4d871122a | -11.82881 | -44.76894 | 2026-07-20 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4201a5c5-a558-347f-b384-cf9a7ec67d94 | -12.94813 | -44.73051 | 2026-07-20 03:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 594697c9-511e-3810-bd9d-aaf3a4eecd5b | -11.83296 | -44.77937 | 2026-07-20 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7d4b1e8-8a04-3a0f-8fef-e82da8d617f2 | -13.29233 | -44.62119 | 2026-07-20 03:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a34b607-90d0-33bd-95b4-a367d3f6869d | -13.29708 | -44.6207 | 2026-07-20 03:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ed474e2-eff8-308c-9c55-3513d3cc1cac | -11.82784 | -44.77199 | 2026-07-20 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f911a3f9-cf4b-3cef-b8d2-2db77d44ec65 | -11.83791 | -44.78588 | 2026-07-20 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 515153e8-94bc-3eaa-8f57-387dee92bae7 | -20.96492 | -40.97755 | 2026-07-20 03:45:00 | NPP-375D | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| ad6ad1b3-ee0b-32ed-8cc7-246f013340df | -20.96089 | -40.97673 | 2026-07-20 03:45:00 | NPP-375D | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 05173591-80a5-3948-88a0-cc9426e17f41 | -19.93107 | -44.07162 | 2026-07-20 03:45:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 10fd2d91-0f5a-3662-bc64-50f63e803800 | -20.5008 | -42.37209 | 2026-07-20 03:45:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 491d863c-7c4c-3c72-b750-7a75ccdc0acf | -19.77365 | -44.30246 | 2026-07-20 03:45:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f0263e1-4acf-39ff-a1e9-01b619d71be3 | -21.39489 | -45.51274 | 2026-07-20 03:45:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 987e684c-aa41-3cab-9d34-13180841b09d | -20.32204 | -42.33919 | 2026-07-20 03:45:00 | NPP-375D | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 46f43277-4982-3004-a2ee-da4ed7b80bf0 | -19.3892 | -40.3066 | 2026-07-20 03:45:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| abf17a64-0155-3246-a83d-0d8a6c27aa65 | -20.88423 | -42.91257 | 2026-07-20 03:45:00 | NPP-375D | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 55d50c6c-2b8c-3245-99e6-0b9398d94fff | -20.96017 | -40.98049 | 2026-07-20 03:45:00 | NPP-375D | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 09534d30-a472-3875-a31f-e051cc40afb3 | -21.13244 | -47.45908 | 2026-07-20 03:45:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4021732b-9a1a-354f-8e8e-e587b7513933 | -21.39408 | -45.51645 | 2026-07-20 03:45:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 252b78fa-a46b-36f1-8efd-988ba22e1eff | -21.40971 | -44.25637 | 2026-07-20 03:45:00 | NPP-375D | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 990db603-ff71-336b-8d63-de78323717c4 | -19.97299 | -41.64833 | 2026-07-20 03:45:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7eefa5d2-1bc4-3674-b430-cd26aa8a8d26 | -20.28985 | -46.42197 | 2026-07-20 03:45:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dedf7e9-45f7-3242-9ce7-359fda9a8e3d | -21.61155 | -46.61531 | 2026-07-20 03:45:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 17cd95f2-a68c-3aed-85a6-7bd05a0579a9 | -21.60909 | -46.6173 | 2026-07-20 03:45:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 8f9c0a2b-19b1-348c-b062-f54b0b0c7498 | -21.61012 | -46.61269 | 2026-07-20 03:45:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 03416fd6-2dfc-3754-924b-5bd44dc169a2 | -21.61048 | -46.61994 | 2026-07-20 03:45:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4830e2f7-ab20-35b4-9abb-837a79848638 | -20.28877 | -46.42676 | 2026-07-20 03:45:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a523cd31-b201-3b7b-8310-acca1b5d0870 | -20.28354 | -46.42337 | 2026-07-20 03:45:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb815394-cf36-3144-b414-0fbd0b948e70 | -19.77431 | -44.2993 | 2026-07-20 03:45:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79468ffb-3ada-3b8b-9cbd-d68ac724c1f6 | -21.45711 | -43.60373 | 2026-07-20 03:45:00 | NPP-375D | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ffdce21c-dae0-3f2a-8fde-a54336321812 | -22.57795 | -42.06125 | 2026-07-20 03:45:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 63026f4a-bf1e-376b-865e-cdb139aa2538 | -20.28452 | -46.41903 | 2026-07-20 03:45:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README2.md)
