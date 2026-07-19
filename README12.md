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
| 6d5fa21a-e2bd-34af-b6d7-6df41f79dbd4 | -12.00308 | -50.57129 | 2026-07-19 05:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66658841-272d-35fc-ad5a-b91ff1b90804 | -10.8997 | -50.3294 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97d30459-7a2f-3501-a903-2f10fecd6558 | -11.73208 | -62.32927 | 2026-07-19 05:42:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0817b60b-94fc-3d4c-b59e-e6f7db9b98e3 | -12.03712 | -55.46022 | 2026-07-19 05:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00e64cec-5f8c-32b0-9f0f-c552c60f7a4d | -10.90084 | -50.32286 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6656d9f-6cdf-3244-ac06-5bddc81e6a26 | -12.07882 | -53.34686 | 2026-07-19 05:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d76f5863-f416-39fc-be53-610ff60a9f51 | -10.89402 | -50.32197 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa0860d4-18e6-317c-90cd-7c7a84b6544c | -10.89436 | -50.31612 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ee7086b-b155-3b2f-a9de-e8371c315886 | -9.48391 | -57.32611 | 2026-07-19 05:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 104617b6-8bc9-344a-88a8-fafba6be8315 | -11.68034 | -54.58827 | 2026-07-19 05:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9baa0ea5-e392-3ccb-ac66-af32d3e41873 | -10.82008 | -50.23126 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 599abfa0-0fe5-374c-a3d2-45c418284e6d | -10.81933 | -50.23749 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b543423-3b38-3637-892f-6e65aec7c859 | -9.09554 | -59.40187 | 2026-07-19 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd0bab10-99ba-3a28-8c0a-99ed5de0d1a9 | -10.82618 | -50.23835 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b63a2992-7662-387d-b34c-63e26f43ec25 | -10.90045 | -50.32319 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e7dc40f-c0aa-3057-b0ce-5ca5f1f752b4 | -10.90578 | -50.33648 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa5afd55-eb5e-3c5f-beb3-8de28953ba70 | -9.48025 | -57.32261 | 2026-07-19 05:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d501fa0-da3b-38d0-b6d0-a2182b852bed | -10.82715 | -50.23794 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 683d7e79-3f81-3488-99bc-922df30ab542 | -9.47969 | -57.32548 | 2026-07-19 05:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 964b72b5-dc23-30c2-960d-a8b4241b25af | -21.99536 | -56.02491 | 2026-07-19 05:44:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f9b8d8f-4807-3c56-8bbb-2414197986b5 | -22.00187 | -56.0243 | 2026-07-19 05:44:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9b11f15e-7dfa-3b05-9b8e-9b48ed396b6e | -18.72823 | -54.20344 | 2026-07-19 05:44:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5efc0058-d4d7-3d5f-b65c-057d87d94f93 | -16.80673 | -54.59433 | 2026-07-19 05:44:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e51b27e7-77b1-32ce-a6e4-9c870daace17 | -22.25707 | -55.969 | 2026-07-19 05:44:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af47b6e7-3eb5-384c-aa54-c6507840a980 | -16.32069 | -54.768 | 2026-07-19 05:44:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d5f7dfad-7f7b-39b9-958d-6b5cd2de6b5c | -20.53176 | -57.39621 | 2026-07-19 05:44:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6676160-e813-3df8-8341-b6882b0cebec | -16.31986 | -54.7664 | 2026-07-19 05:44:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a71a3108-42c5-3459-936f-31afc6faadac | -18.73408 | -54.20466 | 2026-07-19 05:44:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16616e61-911f-3ea8-b247-654c351a2790 | -22.00083 | -56.02553 | 2026-07-19 05:44:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c91ca63c-f7eb-3dc0-8e57-e815dedaa06f | -20.53112 | -57.40197 | 2026-07-19 05:44:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78b22d5d-11c3-3638-bb0d-f68a9db2405b | -22.00735 | -56.02484 | 2026-07-19 05:44:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fb2da7d9-2484-304e-8968-fafb18efd2bd | -16.32027 | -54.7626 | 2026-07-19 05:44:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3b42e010-74c0-31e3-bf50-1ef8919a417d | -22.00119 | -56.02193 | 2026-07-19 05:44:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b10b9fa2-541a-35f2-8935-1323f39ad37e | -21.9964 | -56.02373 | 2026-07-19 05:44:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 126771eb-c3c5-3843-be4c-49f117de3f62 | -16.80717 | -54.59037 | 2026-07-19 05:44:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99102bc9-cc16-374b-bbdf-5800697f03cf | -20.56804 | -54.57707 | 2026-07-19 05:44:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d952e523-d62b-3c91-a8da-233edb9e8ee9 | -20.57394 | -54.57762 | 2026-07-19 05:44:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee894be9-5662-3f30-9281-f45accd08c99 | -20.5262 | -57.40135 | 2026-07-19 05:44:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21175ed8-7a45-3f14-9bc9-ee480a692ba9 | -22.25671 | -55.97277 | 2026-07-19 05:44:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 57aee299-b745-3360-b74f-4b276861c9b9 | -16.32113 | -54.76419 | 2026-07-19 05:44:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4362aebb-1941-3da2-8c63-2d77d5c39f31 | -23.76381 | -54.58564 | 2026-07-19 05:46:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e76b02fe-a0b0-3e03-bb3e-c78131b025a1 | -23.76987 | -54.58659 | 2026-07-19 05:46:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| be9a631f-3fc5-371c-8744-23c8eb4a93d8 | -31.25584 | -52.48778 | 2026-07-19 05:48:00 | NPP-375D | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| fce591d2-5273-397a-9832-49b5dff64021 | -13.6764 | -48.7786 | 2026-07-19 05:50:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 383a225d-7666-341b-9011-f2993fe12738 | 0.96717 | -60.41093 | 2026-07-19 05:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57399597-8b26-3a50-b294-aa5f018e7240 | 0.75766 | -60.45323 | 2026-07-19 05:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41fe94a4-9f2d-3330-a211-c39e58300134 | 1.77137 | -60.23008 | 2026-07-19 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74ca992f-6555-3410-98ca-f38d1a67f55e | 1.76691 | -60.23082 | 2026-07-19 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95843bb5-5df1-34aa-97af-58552285ee21 | -9.48023 | -57.32542 | 2026-07-19 05:59:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f67c8b0c-5f33-3280-839e-8c3d37fc135f | -9.48194 | -57.32424 | 2026-07-19 05:59:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9e88cd4-b772-36b3-9070-556c2524e7ec | -8.34794 | -72.77511 | 2026-07-19 05:59:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0f41bb5-e44d-311a-ad2b-176ffadd1817 | -7.76686 | -63.85717 | 2026-07-19 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 583327c7-ad58-3f15-b298-7dc5c91ecc0f | -9.0974 | -59.40441 | 2026-07-19 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61c96635-2e6f-3839-8363-017ada049393 | -9.91882 | -65.00799 | 2026-07-19 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab5b864d-2f8a-363d-9ff6-663697b19234 | -9.09791 | -59.40059 | 2026-07-19 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b826a116-616d-3077-be83-d5a8b4d43cf2 | -9.60935 | -66.47124 | 2026-07-19 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa3575df-6812-3e57-a187-f892451f59a1 | -9.48089 | -57.32019 | 2026-07-19 05:59:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce81b5e9-d7a0-340e-b6c5-a11fd615aaa1 | -10.7094 | -46.6232 | 2026-07-19 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| bb609bd4-6014-3684-ab78-d9162795e937 | -13.6764 | -48.7786 | 2026-07-19 06:10:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 88aa347b-9c86-3de8-ba47-0304cd7891a2 | -13.6764 | -48.7786 | 2026-07-19 07:10:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 2f74a182-b686-3eac-83f9-828b8a31cf0a | -10.7094 | -46.6232 | 2026-07-19 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| cfd55dc7-de70-30a8-8328-636220eb19f0 | -10.7094 | -46.6232 | 2026-07-19 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 6ac00136-e430-34fa-91bb-33b8ddad07f6 | -10.7094 | -46.6232 | 2026-07-19 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 64ab8869-4e4f-3391-8952-c796887eb445 | -10.7094 | -46.6232 | 2026-07-19 07:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| fa30893d-f2e1-3b7c-8f79-8239a1a13453 | -10.7094 | -46.6232 | 2026-07-19 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 27d78f12-5eb0-3920-b5d1-8330cee23e9a | -10.7094 | -46.6232 | 2026-07-19 08:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 2c2cf22d-5275-3db0-9216-0984945926d8 | -10.7094 | -46.6232 | 2026-07-19 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| d273ffc9-1232-303b-8c96-36cecf748f1e | -10.6904 | -46.6256 | 2026-07-19 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 86560d44-defa-3f23-bbd2-cecc2c9f5048 | -10.6904 | -46.6256 | 2026-07-19 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 9b0c4309-9226-3bf3-821b-69fe4685392a | -10.7094 | -46.6232 | 2026-07-19 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| d239edc8-0285-32ea-8c75-89be8857c7d5 | -10.6904 | -46.6256 | 2026-07-19 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 299f193c-4719-36c0-9432-448725cce107 | -10.7094 | -46.6232 | 2026-07-19 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| b3706a37-51bd-30d5-b34f-7a68f37dae0c | -10.6904 | -46.6256 | 2026-07-19 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 203.1 |
| 17eed05d-fbdd-3eb3-aff4-dbb192e9422e | -13.6764 | -48.7786 | 2026-07-19 11:50:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| a1d2565d-7e8a-32d6-a5f2-cbdf4241eab6 | -10.6904 | -46.6256 | 2026-07-19 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 1d65d06f-efd5-3bbe-85ef-122b47223c97 | -10.6904 | -46.6256 | 2026-07-19 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 55ff04c3-a85e-3272-97cd-93a9980c0164 | -10.7094 | -46.6232 | 2026-07-19 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| ddbbcede-41a1-361d-9fa7-7de122494bbd | -6.46552 | -46.07439 | 2026-07-19 12:02:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f2c71b26-bdeb-3f87-a7c7-a494ec603d88 | -8.93909 | -47.61074 | 2026-07-19 12:02:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 66fa9bf0-8d37-3d25-86f5-42bd3116d4d8 | -8.36603 | -45.39005 | 2026-07-19 12:02:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 82943fe0-af43-3884-9593-28d64ffb5030 | -6.16042 | -46.97519 | 2026-07-19 12:02:00 | TERRA_M-T | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 0656c06e-8337-3815-9469-50cea6f6248a | -6.16311 | -46.97015 | 2026-07-19 12:02:00 | TERRA_M-T | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f2a1b4f9-88d8-36ac-bff5-660c5f143ea6 | -7.11664 | -44.04211 | 2026-07-19 12:02:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 94e7812a-314d-32e7-85eb-0be491b99c4a | -2.78345 | -49.46044 | 2026-07-19 12:02:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 95d2c3f9-68a0-3c94-ae4b-f443319f5181 | -9.50521 | -46.66167 | 2026-07-19 12:02:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1f60b511-52b0-3a66-9b04-c888535da180 | -7.64756 | -50.02792 | 2026-07-19 12:02:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3237518c-62b9-3526-bdd6-828e08c024ab | -7.30088 | -46.25273 | 2026-07-19 12:02:00 | TERRA_M-T | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 37341ad9-1131-3c4c-a878-bfa96a740832 | -7.11908 | -44.02279 | 2026-07-19 12:02:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 0a9856f9-9438-3b2a-a3c0-288214593b04 | -8.94055 | -47.59965 | 2026-07-19 12:02:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| f442e2fd-d633-367c-b315-366d6eff3681 | -6.46719 | -46.06166 | 2026-07-19 12:02:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4733c6ac-1a8a-3ebd-acce-c9935a9a10b3 | -6.16162 | -46.9813 | 2026-07-19 12:02:00 | TERRA_M-T | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e90b72fc-fc88-3129-abc0-7b0790a41bd0 | -7.64882 | -50.01909 | 2026-07-19 12:02:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 40caf94f-0219-3d1d-b5aa-8ae9a6769476 | -7.11513 | -44.03638 | 2026-07-19 12:02:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ba08a852-7a48-3bb7-8b3e-bc22abe36436 | -7.3026 | -46.23977 | 2026-07-19 12:02:00 | TERRA_M-T | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9e61245b-9c72-3fb7-bcc8-194f40a22669 | -6.47065 | -46.06938 | 2026-07-19 12:02:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 6da9c9e6-5a6a-37f1-aea5-d0b2c60fd861 | -8.36407 | -45.40504 | 2026-07-19 12:02:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3ec5bf64-75f0-32ea-8089-6a1f12493746 | -8.12076 | -46.46762 | 2026-07-19 12:02:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b1b3e258-c9fb-35cf-a3bf-a3d56c6aacf6 | -9.21746 | -46.67228 | 2026-07-19 12:02:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8cf33866-7604-3d22-b0df-213627a36ac6 | -7.9158 | -48.2583 | 2026-07-19 12:02:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9be78373-8cbd-36db-9bb5-5d62f4aeb078 | -7.9215 | -48.26559 | 2026-07-19 12:02:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README13.md)
