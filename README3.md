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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40a83d87-a9c5-3040-aba5-f9ba7a50d105 | -22.467 | -51.7143 | 2025-04-08 04:51:00 | NPP-375D | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 9a506fca-428f-32cf-a6f9-1756008092af | -22.46999 | -51.71922 | 2025-04-08 04:51:00 | NPP-375D | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 2d2a631a-a16c-3925-a743-2736cc99cc2e | -20.57712 | -56.04411 | 2025-04-08 04:51:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b17da02-d780-304b-93f9-38f2a6b826ae | -20.58052 | -56.04477 | 2025-04-08 04:51:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73354415-3a1e-3f6f-acdc-24c6859c3f20 | -22.47059 | -51.71481 | 2025-04-08 04:51:00 | NPP-375D | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 9d90b505-8d0d-3449-b026-477cfa289939 | -21.99601 | -47.21657 | 2025-04-08 04:51:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3b4cb83e-b73b-3f32-8740-b1d51a2b2271 | -25.56849 | -49.36491 | 2025-04-08 04:51:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 78b515bb-a25f-3684-b2cb-cc2f42364226 | -20.83274 | -47.75802 | 2025-04-08 04:51:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f141743-51ea-3e33-b256-1817c573ec8f | -23.76308 | -53.13488 | 2025-04-08 04:51:00 | NPP-375D | CRUZEIRO DO OESTE | PARANÁ | Brasil | 4106605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e94c1ee4-276d-394d-a689-958041ee861a | -23.33832 | -46.77349 | 2025-04-08 04:51:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1a2d0319-683a-3b5a-9443-40d63e344968 | -21.43071 | -54.15547 | 2025-04-08 04:51:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| edcf639c-d656-3717-8542-14d613be2b44 | -20.68268 | -48.81942 | 2025-04-08 04:51:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8651e28c-2355-3df8-b94f-52f78d81b151 | -18.34033 | -55.59107 | 2025-04-08 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 23d74da0-f44e-362e-853c-5e437ef65a83 | -21.00447 | -47.65904 | 2025-04-08 04:51:00 | NPP-375D | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2028f7f-249d-34e1-9bb7-8f5525ba3a44 | -20.99389 | -47.35688 | 2025-04-08 04:51:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be35d24d-4f46-3012-be6d-7121fbfef479 | -20.68727 | -48.81619 | 2025-04-08 04:51:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 642ac195-24d8-31bf-8d70-94f37e8c8438 | -12.27279 | -63.80985 | 2025-04-08 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5183b31-b1b1-36d0-8ada-7899221eb957 | -12.11215 | -45.61544 | 2025-04-08 05:10:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee6c814f-d554-3a84-8f97-dacc61d1cc5a | -12.27684 | -63.8106 | 2025-04-08 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcd612cb-142a-3cb5-86a2-3f17eb3546f3 | -12.11081 | -45.62793 | 2025-04-08 05:10:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 787c078b-55c3-3032-b5ab-01844b2e9915 | -12.10795 | -45.62724 | 2025-04-08 05:10:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79f908cf-f1bc-33d9-aa31-95ca283ad0d3 | -15.2516 | -47.46991 | 2025-04-08 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1798b01-4442-368f-95a4-0ab9baf9c74f | -12.11148 | -45.62171 | 2025-04-08 05:10:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66e5a0ab-0c77-31e5-b7b7-10431ab4cdbb | -12.24035 | -63.80381 | 2025-04-08 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97822ab2-8b69-37ba-aec8-b0235fa0af09 | -12.11467 | -45.62797 | 2025-04-08 05:10:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b88078d1-8fc9-3c3f-a634-f6d98731cd67 | -15.25104 | -47.47518 | 2025-04-08 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33e284d8-8b6c-3a18-88b2-03e48ac1af90 | -12.28089 | -63.81137 | 2025-04-08 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e04ea540-611c-3a84-8bdd-010f6b7e460f | -12.11399 | -45.63393 | 2025-04-08 05:10:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f5c5f81e-72d2-34bc-a08b-5a870ee39647 | -12.11016 | -45.63395 | 2025-04-08 05:10:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf5a7c69-3e9e-35ea-8000-0aa6872dfc5c | -21.77047 | -55.32 | 2025-04-08 05:12:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5574ecc1-59c9-3e78-920b-84515177d108 | -22.46732 | -51.71451 | 2025-04-08 05:12:00 | NOAA-20 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 4a3d7707-bfc3-370d-930f-f694405f0d09 | -20.68766 | -48.8118 | 2025-04-08 05:12:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9607c9b5-135c-3c9d-a5c8-2b113041875a | -20.57967 | -56.04466 | 2025-04-08 05:12:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fdc1712-6c36-376e-9db2-52c2bb66070e | -22.46767 | -51.7111 | 2025-04-08 05:12:00 | NOAA-20 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1ed69e09-3638-3655-afe4-950c761013ab | -22.46697 | -51.71794 | 2025-04-08 05:12:00 | NOAA-20 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8afbbb25-b39f-3fd8-916c-e0cd1001193f | -20.83623 | -47.7615 | 2025-04-08 05:12:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af99cd25-3cf3-3b5f-8528-39401e23dbb0 | -20.68116 | -48.81578 | 2025-04-08 05:12:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 82b40b22-7cec-36e6-acde-52d21ce5f724 | -20.83019 | -47.75696 | 2025-04-08 05:12:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 018d4d50-b960-36c0-88da-539c7daf9e8c | -22.47253 | -51.71492 | 2025-04-08 05:12:00 | NOAA-20 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| d35cf3ed-14b1-3c3e-b662-436d8ac04024 | -20.68725 | -48.81643 | 2025-04-08 05:12:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ecbb2e2f-3d5a-34f4-aaf2-c37a329ce2e2 | -22.47218 | -51.71832 | 2025-04-08 05:12:00 | NOAA-20 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 39aab353-7102-359c-9e41-e2a818a2783c | -18.341 | -55.59222 | 2025-04-08 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 64480f16-8809-3af0-98a1-38d3c5f4106a | -21.85625 | -54.77718 | 2025-04-08 05:12:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 10914c20-3895-34ba-b295-35904d48b109 | -21.77093 | -55.31619 | 2025-04-08 05:12:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b72612d-1478-3ba3-a273-c87302dbc5c2 | -20.58352 | -56.04519 | 2025-04-08 05:12:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e793d3c2-048b-3f47-804c-d43cec21a99d | -20.82977 | -47.76041 | 2025-04-08 05:12:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3ff12f3a-f2d3-3133-a91c-3b7d880923ac | -20.82978 | -47.76213 | 2025-04-08 05:12:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 71333957-0867-324e-83f9-76b5ef57249c | -22.47398 | -51.70642 | 2025-04-08 06:01:00 | AQUA_M-M | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| d1f78563-a90d-309f-805e-e8195ac4271b | -22.46408 | -51.7051 | 2025-04-08 06:01:00 | AQUA_M-M | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 3f2bf4f0-858d-3d06-bb70-7588d960f531 | -22.46251 | -51.71727 | 2025-04-08 06:01:00 | AQUA_M-M | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 373d9af7-6381-345c-bdc9-54718e0e124c | -22.47241 | -51.71855 | 2025-04-08 06:01:00 | AQUA_M-M | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 6e3918d9-537d-3999-98e9-8ba84992b5d5 | -21.85174 | -54.77809 | 2025-04-08 06:01:00 | AQUA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 342b8b0f-ac87-314e-b1b2-a85d9fe83090 | -6.19806 | -48.03476 | 2025-04-08 12:32:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2165db63-a8a2-3956-9d4e-9d347f529376 | -8.76129 | -46.65155 | 2025-04-08 12:32:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d087e233-1065-38d6-9dab-0844bf6660fd | -12.11222 | -45.61435 | 2025-04-08 12:32:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 1c7208fb-e08a-3c8f-b351-ec7a2ad5d66e | -12.12438 | -45.63268 | 2025-04-08 12:32:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| deb023a1-6ecd-34b3-acc0-63cd3d589166 | -12.11884 | -45.63666 | 2025-04-08 12:32:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 8fbd1c75-278e-33a9-b55c-d777be60a0e3 | -8.73203 | -44.01625 | 2025-04-08 12:32:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bf7eb83d-591c-33f0-800d-8f2d3118e97e | -12.12173 | -45.61564 | 2025-04-08 12:32:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d821b395-7b31-3aff-8f21-d7a83e25d8db | -8.76635 | -46.67976 | 2025-04-08 12:32:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f23c0166-d353-3134-b715-0cdc55572026 | -7.61064 | -45.12199 | 2025-04-08 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e03f4a1f-3d89-378f-baac-bbc9152be825 | -12.12576 | -45.62217 | 2025-04-08 12:32:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| afbb60ba-bd4d-3163-a7b5-dfb3b13ab684 | -12.12028 | -45.62618 | 2025-04-08 12:32:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 353.0 |
| 7a0150b0-d0de-327e-b24c-b9fc8e732a3a | -8.11758 | -43.12614 | 2025-04-08 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| e2f10c60-63b9-33f5-8d12-b9c3279dc0e4 | -8.11938 | -43.11282 | 2025-04-08 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| d0cd3f0c-e5c5-3d93-ad96-fe216e236d85 | -8.10693 | -43.12471 | 2025-04-08 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 23eccc35-8ce0-3c86-b7e0-b07a35349844 | -10.67415 | -44.38679 | 2025-04-08 12:32:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8ef4f718-b17d-36be-85bf-05f41fc0d8b7 | -17.06074 | -45.00974 | 2025-04-08 12:34:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9a5bc799-3263-39ab-a98c-bfa9bd6a0f7c | -21.54591 | -45.09671 | 2025-04-08 12:34:00 | TERRA_M-T | SÃO BENTO ABADE | MINAS GERAIS | Brasil | 3160801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 56d29d7b-a66a-3b03-95a9-a18e5acc266e | -21.69546 | -50.35495 | 2025-04-08 12:34:00 | TERRA_M-T | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 5d13dbbf-9dae-37bc-93ec-1e5359c1bb1e | -23.74388 | -52.45186 | 2025-04-08 12:34:00 | TERRA_M-T | TERRA BOA | PARANÁ | Brasil | 4127205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| d3452f3c-81f0-3876-85e2-22404d539786 | -19.36227 | -49.18918 | 2025-04-08 12:34:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 39ded583-e553-3a2f-b022-3863d0357912 | -17.39189 | -49.23955 | 2025-04-08 12:34:00 | TERRA_M-T | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ab9d92ca-83f8-34c3-8768-addfd9d9d5e1 | -21.49853 | -50.68834 | 2025-04-08 12:34:00 | TERRA_M-T | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| a865003a-f497-3741-9a8b-ed1c21e42de6 | -16.64497 | -45.14577 | 2025-04-08 12:34:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 5dd4de67-f086-3864-b16f-4ffec716f8d1 | -23.73475 | -52.45024 | 2025-04-08 12:34:00 | TERRA_M-T | TERRA BOA | PARANÁ | Brasil | 4127205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a3ab34d3-9275-33da-9e13-6a752e8d8e5c | -20.68585 | -48.81607 | 2025-04-08 12:34:00 | TERRA_M-T | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| b2deacd4-9973-31f9-a78c-b7e9c1220448 | -15.51359 | -44.39725 | 2025-04-08 12:34:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 8.6 |
| ab79b7aa-5ddb-323e-b7f0-545aca7f383d | -22.47188 | -51.7099 | 2025-04-08 12:34:00 | TERRA_M-T | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 289c2652-be01-30d3-b624-dcf928ea5f2c | -18.80515 | -46.44023 | 2025-04-08 12:34:00 | TERRA_M-T | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0bcc4e52-2153-38ed-b5be-135b757c70e2 | -23.013 | -51.05603 | 2025-04-08 12:34:00 | TERRA_M-T | SERTANÓPOLIS | PARANÁ | Brasil | 4126504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| ba46b53d-2e30-3f5d-8088-715fd1e34ce5 | -17.39057 | -49.24873 | 2025-04-08 12:34:00 | TERRA_M-T | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cc54da03-caf5-3bf1-839a-cc266d382a7d | -22.76982 | -47.00732 | 2025-04-08 12:34:00 | TERRA_M-T | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| e6df7ea8-ae1f-3d71-9884-2223cd6649f2 | -16.6466 | -45.13275 | 2025-04-08 12:34:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 27.5 |
| fa9366e8-9e64-3c2b-8c28-675834340343 | -17.93512 | -44.4178 | 2025-04-08 12:34:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 26069049-2062-30a3-b5d7-9eebe14ea8b4 | -15.51186 | -44.41147 | 2025-04-08 12:34:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 11.4 |
| f73516e2-6b16-306c-85f8-088fa4f57bde | -17.61934 | -46.70625 | 2025-04-08 12:34:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 736240f6-35bb-304c-b918-9b90c5f77651 | -21.49993 | -50.67887 | 2025-04-08 12:34:00 | TERRA_M-T | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1365d280-ef49-3f87-b96b-344474e64686 | -17.94633 | -44.41932 | 2025-04-08 12:34:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 30855c1e-c4c0-3919-adc4-c6cebce8c8cd | -17.62076 | -46.69536 | 2025-04-08 12:34:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |


