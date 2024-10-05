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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2bf7a79-9f7d-3d55-8d4c-be29249b2a00 | -5.84336 | -44.123 | 2024-10-05 05:08:00 | AQUA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 6b65b7ea-2dc0-3924-a9a7-7a2079568a7f | -5.84201 | -44.13193 | 2024-10-05 05:08:00 | AQUA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 5755a6cb-1cc0-38d3-b708-de74a707080f | -5.83447 | -44.12168 | 2024-10-05 05:08:00 | AQUA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b7a48c1d-ff55-3fb2-aea5-b7e71c1a99db | -5.83312 | -44.13062 | 2024-10-05 05:08:00 | AQUA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 1096c800-1e9c-39d2-a123-50e9689055f8 | -4.86807 | -46.5211 | 2024-10-05 05:08:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 89dbe202-95f4-306d-908a-7d42148944be | -4.70879 | -45.87933 | 2024-10-05 05:08:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b37822e0-0034-36c8-a632-dab25b633f7d | -4.09495 | -47.94229 | 2024-10-05 05:08:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 1a35bad4-35cf-3296-9bfe-bd057136222c | -4.0926 | -47.95748 | 2024-10-05 05:08:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| decf7297-5f88-360a-81c1-0d8d140c5a45 | -3.62982 | -47.5214 | 2024-10-05 05:08:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 91f325bb-bd8e-3d4c-aef6-cad5931e5401 | -3.33306 | -50.46612 | 2024-10-05 05:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 07d2db42-1da7-3ee6-be87-1f7ea3bb023e | -3.32284 | -50.43956 | 2024-10-05 05:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 1825ebc3-ce58-32a5-8e59-39970c5c043e | -3.31898 | -50.46401 | 2024-10-05 05:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f037d1fe-ca23-3f64-84b4-1720e2dafd5d | -3.25455 | -50.37468 | 2024-10-05 05:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1dffb370-f0b9-3d00-83d0-2f7cf6295243 | -3.24435 | -50.84125 | 2024-10-05 05:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| fcd071a0-5b03-389f-a3cd-dcb4f4369714 | -3.24163 | -50.83593 | 2024-10-05 05:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| d0bf4b9c-2175-3c9f-b170-3d93b095c7ef | -2.58062 | -49.06581 | 2024-10-05 05:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0ad47ad9-4dc4-3e13-9ea3-0a68b74eb74a | -11.72323 | -47.80641 | 2024-10-05 05:10:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7706827f-943e-30cd-ac4c-8aca4c65b9ee | -11.72275 | -47.81306 | 2024-10-05 05:10:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 6e9fbc96-1e89-38db-898a-01c966eddf09 | -11.72145 | -47.81772 | 2024-10-05 05:10:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 8a7d9b60-f4e1-3904-9fb8-f631afde6347 | -11.38049 | -47.19914 | 2024-10-05 05:10:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 208c2728-7363-3960-9ad8-85435b083280 | -11.37881 | -47.2097 | 2024-10-05 05:10:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9e0a2154-125a-3473-aa99-d8717033558e | -11.25891 | -46.98463 | 2024-10-05 05:10:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 03520843-2a77-36e2-a141-ef7937fbbbdc | -11.25729 | -46.99495 | 2024-10-05 05:10:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 93d4eb31-809e-37ef-a22d-1981138ca31e | -11.24946 | -46.98316 | 2024-10-05 05:10:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 33a92941-6fec-3522-ba49-a302c21bea87 | -11.24783 | -46.99346 | 2024-10-05 05:10:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| ea35a414-fc52-38ce-a748-cef89c769468 | -11.24315 | -46.61283 | 2024-10-05 05:10:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f3821d15-8f73-3e01-8bae-28468981c87d | -11.24159 | -46.62288 | 2024-10-05 05:10:00 | AQUA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bf85d2c2-998d-3c81-a74b-1cd2375ef268 | -11.15769 | -46.51172 | 2024-10-05 05:10:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c08b662f-4e76-3cfa-993d-049ba1313dc7 | -11.13763 | -46.51889 | 2024-10-05 05:10:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2e320a00-1a04-3774-89db-6b26ec6f44d5 | -10.9374 | -46.67888 | 2024-10-05 05:10:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ec2e8590-73b8-3b30-81a3-096ee76855c7 | -10.92964 | -46.66737 | 2024-10-05 05:10:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c9c4f7b7-f31d-3df0-8686-1cb4c1e5dd3f | -10.92807 | -46.67736 | 2024-10-05 05:10:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| ddfb2b80-66e1-3589-8b9e-3adc4827c6e6 | -10.74163 | -47.72416 | 2024-10-05 05:10:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 79cf682d-f82a-313d-952d-94420f933abe | -10.71491 | -48.71564 | 2024-10-05 05:10:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cc60a78c-acc0-3638-a51b-b43b678a0cf9 | -10.47827 | -48.33789 | 2024-10-05 05:10:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 51083328-9990-3ab6-b578-b5f13c52d690 | -10.4762 | -48.35065 | 2024-10-05 05:10:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 90b012a6-e2b2-36ab-bb06-5dc8724f55fd | -10.4651 | -50.71748 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 1f3c99e7-3ce6-3216-82d2-125cec938df9 | -10.46192 | -50.73627 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9997596c-1717-3e3a-831f-38a4b28b2a96 | -10.45257 | -50.71524 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a5ab956c-7882-379d-a13e-9c813d6af033 | -10.44937 | -50.73406 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 4873041a-3b17-336e-b210-7cfc73bd3ce2 | -10.34517 | -50.49926 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5bbc2b56-d479-3267-9d9a-62dc4df48765 | -10.34198 | -50.51767 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a2857ca0-fd9f-3943-ab54-b98dc2e36f44 | -10.34111 | -50.51019 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| fdef48cf-8365-329c-9da6-5932a8b7df4e | -10.33877 | -50.53615 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 7dcba966-f367-3e93-b651-163eea9bfb4d | -10.33804 | -50.52868 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| e942a553-fa8b-392c-84d0-df2db2ce0e3d | -10.32874 | -50.50806 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2b64da36-da54-3622-a389-0cfa6d7a1772 | -9.96608 | -44.08104 | 2024-10-05 05:10:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d1ebcae9-f2a9-36ef-b5de-857ee74ef0b3 | -9.96475 | -44.08997 | 2024-10-05 05:10:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 52444cae-e3f6-3a5a-9104-fa337f1ef098 | -8.79566 | -44.8141 | 2024-10-05 05:10:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c254871d-e78e-3264-b9d1-29909edadbd3 | -8.79429 | -44.82312 | 2024-10-05 05:10:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e5834f66-44e6-3b72-ad2e-92b1ca6f2d98 | -8.79292 | -44.83217 | 2024-10-05 05:10:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bcf8e730-366b-30e4-97da-4074b8e83a71 | -8.78677 | -44.81275 | 2024-10-05 05:10:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f3f463d5-9609-3990-930d-974eeacf93d0 | -8.78539 | -44.82177 | 2024-10-05 05:10:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| bd2a5c64-8fe0-3690-afec-d954361286bf | -8.78401 | -44.83082 | 2024-10-05 05:10:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 344a67bc-f166-368d-ac4f-7f6442420bd9 | -8.77649 | -44.82043 | 2024-10-05 05:10:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7282af94-bbd1-3794-9d52-3b788f4da1c6 | -8.77511 | -44.82946 | 2024-10-05 05:10:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 62ac58a2-01a4-30ef-8d00-767cad535036 | -11.69184 | -45.2598 | 2024-10-05 05:10:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 453bb832-55fd-3160-9da2-6f2aaccfcbe5 | -10.85663 | -42.85039 | 2024-10-05 05:10:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 0579f8f4-19f3-3fa7-b389-1bbff3c735f1 | -10.85525 | -42.86005 | 2024-10-05 05:10:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| fbba4b15-9642-372d-bfdd-ce92b15a83d7 | -10.30075 | -45.47466 | 2024-10-05 05:10:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4a2a29e6-d875-372c-b429-328e061ee2c7 | -10.29319 | -45.46409 | 2024-10-05 05:10:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 54fd4da6-92f2-3045-93bb-85f54aa351bc | -10.29178 | -45.47328 | 2024-10-05 05:10:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| eb212ba1-d724-37ef-b5ef-97dfa36fb639 | -8.79981 | -49.94964 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b39048b7-6eb3-3a06-814d-dc5d1055b9c3 | -8.79291 | -49.93751 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7b4d0c1e-91ca-37e8-977e-1db16462d01a | -8.78991 | -49.95523 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 451f058f-dde3-30f5-83ce-0c73291cfa1a | -8.78763 | -49.94759 | 2024-10-05 05:10:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 5018d6e9-3430-3606-b9a3-4b92380931d7 | -8.60199 | -46.50592 | 2024-10-05 05:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 375bf892-8efd-3710-85ff-318adf372a75 | -16.69282 | -55.54244 | 2024-10-05 05:12:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 38.6 |
| fbb411cf-985a-3518-82d8-59daa9f5ef41 | -16.68373 | -55.53502 | 2024-10-05 05:12:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 5ffcd25b-2f6e-32da-891d-65702655cedd | -13.64316 | -51.2575 | 2024-10-05 05:12:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| c5adee10-530d-3d87-a62b-ecea2507f588 | -13.63958 | -51.25174 | 2024-10-05 05:12:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 53a94fc4-dea8-3e74-b216-bc3d0fdd5d9b | -13.63642 | -51.27024 | 2024-10-05 05:12:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e5eb286c-cae3-303e-a9aa-d4d4ad749d2f | -12.82331 | -50.55111 | 2024-10-05 05:12:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 5bb3732b-58d4-3dc7-8e01-46b0df6bd336 | -12.80255 | -50.53006 | 2024-10-05 05:12:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 5dc36e96-e32c-36c3-b490-798dd2c2081f | -12.79968 | -50.5469 | 2024-10-05 05:12:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 24c67f3c-fd7c-3b11-b644-c7a2a09ed050 | -12.79679 | -50.56379 | 2024-10-05 05:12:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7c6251e3-6436-3e70-acd9-40ae72191417 | -12.78786 | -50.54481 | 2024-10-05 05:12:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 222.6 |
| 4085e794-aad1-3dd2-a6f6-9d8cfa988172 | -12.78496 | -50.56169 | 2024-10-05 05:12:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| bc4f11f2-a6b4-3834-9ed5-66f3c8ed4775 | -12.64563 | -53.09285 | 2024-10-05 05:12:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 150.7 |
| d1964cc1-10b4-360d-8c8b-c4c7983ada77 | -12.6455 | -53.10052 | 2024-10-05 05:12:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 197.3 |
| 662e9e70-3579-366e-bd23-abad2462f988 | -12.64084 | -53.11959 | 2024-10-05 05:12:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 311.0 |
| 0932a8a8-56a1-36c0-b6fd-9236af974b7f | -12.64054 | -53.12708 | 2024-10-05 05:12:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 150.0 |
| f385e579-72cb-3fe5-95bc-1f876fd9df23 | -12.62634 | -53.11692 | 2024-10-05 05:12:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 161.5 |
| e0db24a8-1bfc-35b4-83e2-1ca08e0fa85a | -12.61185 | -53.11419 | 2024-10-05 05:12:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 5df5a59d-de4d-34e9-92b3-ac9563d37d7f | -19.81918 | -46.44765 | 2024-10-05 05:12:00 | AQUA_M-M | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 242cf4c7-fe20-3b61-90eb-c6ef0e4d0ba9 | -19.82817 | -43.83836 | 2024-10-05 05:12:00 | AQUA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3d393e6f-3c38-38c9-bdcb-f188760e494a | -19.82668 | -43.84951 | 2024-10-05 05:12:00 | AQUA_M-M | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 384b4055-f614-309e-95f0-9cd651f7e7f9 | -19.15588 | -46.62111 | 2024-10-05 05:12:00 | AQUA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9dd3ac3c-a8fd-320d-b704-78e395a77fb7 | -19.03879 | -43.17199 | 2024-10-05 05:12:00 | AQUA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 205bd5e3-3e15-308e-b897-c76988a369a6 | -19.03726 | -43.18349 | 2024-10-05 05:12:00 | AQUA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 46c451b5-aa24-3170-915c-fd29e71f1098 | -19.03038 | -43.15917 | 2024-10-05 05:12:00 | AQUA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 0dbb1502-590f-3e62-87fe-2b5e74b6b521 | -19.02884 | -43.17075 | 2024-10-05 05:12:00 | AQUA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 1dbc3be9-439b-3bed-9360-1d6f61a97eda | -18.89977 | -43.59053 | 2024-10-05 05:12:00 | AQUA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 3a5737a1-6988-3e57-97b5-29c067e0e716 | -18.89825 | -43.60166 | 2024-10-05 05:12:00 | AQUA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| f828b9a2-d9e7-3cda-b007-5ac060ac2496 | -18.89009 | -43.58926 | 2024-10-05 05:12:00 | AQUA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 3037ee48-99db-387f-8a9e-7a18874ef7aa | -18.88859 | -43.60034 | 2024-10-05 05:12:00 | AQUA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 6e1761d1-c304-3053-8dbc-bcc77c337897 | -18.88705 | -43.61162 | 2024-10-05 05:12:00 | AQUA_M-M | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 34c254f3-6bac-3597-bc9d-9137bafa9f50 | -18.80858 | -48.44288 | 2024-10-05 05:12:00 | AQUA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 11f88778-ae4f-3af7-8964-ebe87da4dc2a | -18.65551 | -43.14036 | 2024-10-05 05:12:00 | AQUA_M-M | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 25d96689-729e-3977-8f75-2e37fe94c630 | -18.65397 | -43.15193 | 2024-10-05 05:12:00 | AQUA_M-M | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |


[Clique aqui para ver as próximas entradas](README130.md)
