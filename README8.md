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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd118e8f-c88c-3afd-95cd-cbb9cd503fca | -6.91566 | -42.4197 | 2026-08-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7353e623-60c3-3bb7-816b-62cbe965d93d | -9.39692 | -37.80918 | 2026-08-07 04:08:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e3bf5f7a-b124-3810-8acc-8732b4aacca0 | -6.91178 | -42.42268 | 2026-08-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e4af54ef-1d70-3a84-bb41-0d10a772f00d | -6.8592 | -46.00915 | 2026-08-07 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 402ee48b-484e-37da-b7e8-865c7449202e | -6.9127 | -41.9415 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e6d27702-20bd-38c9-bb3d-5b1f1f12ece3 | -2.47998 | -49.32407 | 2026-08-07 04:08:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc587503-6243-3eb4-b1f8-fcd649a48269 | -8.96746 | -48.15293 | 2026-08-07 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf30b952-114a-377c-854f-862c4b75f007 | -5.98396 | -52.15545 | 2026-08-07 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54f7ad27-9837-33c4-9de0-c712046c917b | -7.42105 | -38.9682 | 2026-08-07 04:08:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9696dc6f-0a2f-329b-b158-b64d9cc15289 | -6.98823 | -42.90771 | 2026-08-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3ffae0e9-6f80-33ee-a2a6-b6b2b8501ba1 | -8.47127 | -49.56392 | 2026-08-07 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d085d157-c208-3094-b8e7-5ce5bfe0f8d6 | -4.36665 | -47.76737 | 2026-08-07 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 618a8920-d016-32d4-b5fc-5e6fd6f8f8bd | -5.97795 | -52.15519 | 2026-08-07 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8ea2e56-a443-3be7-92e1-11b6e8918c41 | -6.13845 | -47.18278 | 2026-08-07 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 0b4f12c1-75e1-32f5-b3bb-e32116248163 | -6.06159 | -44.88806 | 2026-08-07 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a331371e-4dea-325d-8a21-020d6e79640b | -7.01382 | -43.73753 | 2026-08-07 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4a46cdb3-8aee-33a2-a68d-9fe2880c712e | -6.06754 | -49.48984 | 2026-08-07 04:08:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f751a990-1e7b-3f9e-859f-7e927e1ad448 | -6.92538 | -41.94703 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3c662870-d462-3d29-87b3-50a9e8c93cce | -2.48463 | -49.32798 | 2026-08-07 04:08:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c021770-83c9-31c5-b915-bfded96575ef | -7.37552 | -41.04139 | 2026-08-07 04:08:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ed5ceddf-fa27-34a7-8907-f76d5bfbdc5d | -5.82617 | -44.13692 | 2026-08-07 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39fbdb7d-7d00-37b4-8e2c-20d41fcf8bf2 | -4.91523 | -49.24023 | 2026-08-07 04:08:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6e3517d-247b-3a8a-ba64-d5c67afcdc07 | -6.69885 | -40.46838 | 2026-08-07 04:08:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ffa52884-b02f-3ede-a767-06eb9f04ce7f | -2.69112 | -47.35841 | 2026-08-07 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6102cf09-48bb-390c-9e9f-9fb72bdf639b | -8.65093 | -54.94945 | 2026-08-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96082db4-88e3-3282-b61a-f56c70b5a549 | -4.45907 | -47.92116 | 2026-08-07 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 5d20e196-a387-3eae-8e0e-87447f64666a | -8.20154 | -42.22463 | 2026-08-07 04:08:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9ba382a5-682d-3683-b7f7-d3b02cc89cfc | -3.12064 | -48.58528 | 2026-08-07 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fc7a568b-89b1-35fd-ad46-93497f01d9a7 | -4.3659 | -47.7719 | 2026-08-07 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 94426a77-02bd-3499-9796-012acad8bed7 | -6.91012 | -42.43318 | 2026-08-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7c4e2588-0f75-331b-9a00-6f0e3ca30fbc | -6.92864 | -41.92625 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ef8603b6-9187-396f-bbca-53efed9e522b | -4.99457 | -37.09785 | 2026-08-07 04:08:00 | NOAA-21 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 68f50d6b-ea64-3600-b5a2-9bcf437c3e19 | -8.54111 | -49.55535 | 2026-08-07 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e2383e2-9a68-3a19-9e05-c78338ae4b28 | -8.33798 | -46.39399 | 2026-08-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2637308d-1057-30db-96e3-970453df4646 | -7.75744 | -45.02731 | 2026-08-07 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 94625c63-6534-3f3d-b2fd-0e50cba03616 | -5.6308 | -44.1109 | 2026-08-07 04:08:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c5b8e85-cad8-36cc-a479-7800e97f6f62 | -6.91621 | -42.4162 | 2026-08-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 85adf71d-8a2e-3001-8b71-49aae1794b22 | -4.93642 | -41.98406 | 2026-08-07 04:08:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 64835984-ee91-358c-a320-2e40a911e0df | -6.91546 | -41.94548 | 2026-08-07 04:08:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3e9aa3c8-aede-319b-8c41-1459ec6ee4e3 | -4.84745 | -45.22234 | 2026-08-07 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42ebedf6-e1ab-35ee-b232-9f8d46315f03 | -9.93986 | -40.64284 | 2026-08-07 04:08:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e5d7110-d48f-3054-b5a1-9d4aa516bba4 | -7.75384 | -45.02673 | 2026-08-07 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 6f3cdffa-3586-36af-96fe-8e2e581059d3 | -11.1447 | -44.4632 | 2026-08-07 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6674f5aa-19e3-3b61-afcb-bfffce87ae2c | -11.1443 | -44.4865 | 2026-08-07 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a1f0f41f-1cb7-3e6b-bfe1-1c5dd66b6d25 | -11.13245 | -44.48582 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c7c3461-7188-3663-8683-90ced9cbf140 | -17.5709 | -47.50397 | 2026-08-07 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fe8854f-8d09-389e-b7fa-fc2b676f8109 | -11.33671 | -45.21864 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6d2c7b8-c5f7-3f85-aa26-f7480a2ae143 | -13.68923 | -51.97762 | 2026-08-07 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c91d5e7e-bdda-34cb-82a0-e05ddf3788d4 | -14.48275 | -47.98105 | 2026-08-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d410247-d7e5-3390-a8af-e80ea0069e72 | -11.14608 | -44.48805 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b47d90df-c1bc-3fbe-9ec8-5300b7ef2990 | -14.42157 | -45.668 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45b68726-e204-316f-9030-d2b1544e2aa3 | -11.08195 | -47.79932 | 2026-08-07 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| baabb42b-1641-3f4c-bdd4-5b5595451e25 | -13.8278 | -53.71469 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9308310e-8fc5-3697-a55e-ad85a56b2a19 | -16.68816 | -51.36739 | 2026-08-07 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a283b87-f500-3031-b1b1-69de0e70566d | -11.17819 | -54.86392 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d7a9691-d588-3f59-807b-42aeea9a6ab5 | -16.32961 | -43.14352 | 2026-08-07 04:10:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3ce41a3-c2cd-38b3-b494-fd2cefceebbe | -11.13766 | -44.47516 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e001589c-451d-3e0a-88c6-a85918fc0891 | -15.86588 | -56.05174 | 2026-08-07 04:10:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 3b1cf0ce-3bd3-343e-88e6-e8262993e0c3 | -12.00745 | -49.28497 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1e918aa7-d002-345e-a291-0377b5c26387 | -8.65403 | -54.95202 | 2026-08-07 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35729a53-33c4-3b9e-89ff-2cbbc6010662 | -11.13426 | -44.47459 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07f6bc18-ffd3-3624-82b4-383a398b0762 | -11.15069 | -44.48114 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4a061422-2eb0-377c-8b02-60874f28cec1 | -18.0714 | -42.93828 | 2026-08-07 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ec5702ee-67e9-3910-829f-5a72e4815959 | -17.53965 | -45.35528 | 2026-08-07 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6c0abb1-6383-3246-84a3-0d70811088da | -14.27168 | -45.29577 | 2026-08-07 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f6b9b50-eec1-3a1f-833e-2bcc05725407 | -11.13366 | -44.47833 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75baefd3-58f6-3174-9164-8eeece8df67d | -11.32054 | -45.20783 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bbeaf24-4fcd-3f4f-afb1-0a1277746081 | -15.86889 | -43.59778 | 2026-08-07 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b26f345b-19a3-3bc8-99e2-a7dfd44659ac | -11.14908 | -44.46939 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a38699d6-4cd7-3209-ba22-e064a4c0494e | -11.30247 | -44.84718 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 735198c1-55f7-3442-b512-c22395712274 | -11.13526 | -44.49012 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2bfa2ad-11bd-3ff4-a4c8-63dc52ca7edc | -12.90798 | -45.64278 | 2026-08-07 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2d9666a-7c2a-3d72-9183-dd2ef9d9a97f | -11.14327 | -44.48376 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 2d877dd4-b68c-331e-8f98-22283e4492ae | -12.86275 | -52.82091 | 2026-08-07 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00a8c10d-4449-3d84-bd0f-f583f020fc08 | -11.15265 | -54.85952 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 935a19d8-177a-3250-abd1-04f450ffdd78 | -11.13942 | -54.88235 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4354a67a-4140-3dc8-98bb-f75bacdac7da | -11.17716 | -54.86907 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f53b1a7f-f2e9-37e4-9145-96aea523aa88 | -14.26889 | -45.29139 | 2026-08-07 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d0f11ab-f040-38e9-9229-3fa4ca287498 | -14.48345 | -47.98357 | 2026-08-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97011603-1999-38a6-ba91-dd65fb47d354 | -13.82701 | -53.71863 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0c7e32f3-99d0-37c2-b9a5-e4342ca2049b | -11.15673 | -44.48955 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6ae64d2-856a-333f-8992-0d5cc99e0d9f | -13.93967 | -47.35871 | 2026-08-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba60e550-cacf-32df-8798-33bc879116ee | -11.14507 | -44.47256 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fc43cf1a-db5d-3e28-842e-9ea4035eac37 | -13.78694 | -49.72382 | 2026-08-07 04:10:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7fc08fb-f69c-34fe-a36d-c18cc10d1e79 | -15.69412 | -45.58004 | 2026-08-07 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a03a82eb-a28e-3857-a000-d788ac5c1258 | -12.51927 | -55.78421 | 2026-08-07 04:10:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2783502e-9292-3f1e-98a8-f3e106c726a3 | -12.86345 | -52.81736 | 2026-08-07 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 055258fe-a754-3c98-9903-a8794f62a200 | -12.60736 | -43.40637 | 2026-08-07 04:10:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b011c192-5e96-30f5-95af-1fada5f1f2f4 | -10.63657 | -47.48914 | 2026-08-07 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f8868db-7b9b-3d00-8c5b-827953882e8b | -10.63716 | -47.48569 | 2026-08-07 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42ca5f2b-9850-39b7-aeea-41a030fecc9d | -11.15188 | -44.47367 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 88102afe-6158-3df0-bebb-ff4e5b5d8e67 | -12.58461 | -46.90913 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8cd05820-bfc6-360d-92c5-5e9aecb5149f | -11.45782 | -44.55847 | 2026-08-07 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d1f8ee0-3209-3c1f-ab82-dc42c55f6111 | -14.34022 | -54.9304 | 2026-08-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0c274d4-c844-3d26-9895-12ea45abface | -13.93876 | -47.36624 | 2026-08-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9698f63-5471-33d0-9165-c57c072aa130 | -11.27775 | -44.84693 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca10a6f1-9f82-32d8-a40f-253f7cdff9a5 | -12.13972 | -48.26481 | 2026-08-07 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62a43af1-ec64-369e-8f92-786e08a7c8cf | -13.83344 | -53.7159 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 862f850d-adc4-3005-958e-ef5bfb173326 | -14.42566 | -45.6647 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cee49c8c-8f9c-3980-8f05-5e61c8c6737e | -17.53295 | -45.35411 | 2026-08-07 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README9.md)
