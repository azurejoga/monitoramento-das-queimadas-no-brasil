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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 189a7c14-3fbe-3e68-b118-540aa537bf9f | -7.2701 | -47.463001 | 2026-08-21 00:42:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1151452-5fe7-369d-b0bf-701439e3ef78 | -6.693 | -58.913898 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9be408a-086f-3b30-af56-f1d33918a9df | -12.2531 | -43.167801 | 2026-08-21 00:42:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2a3e3235-8b29-3a3c-b3c8-020c8fc43edd | -3.849 | -49.048 | 2026-08-21 00:42:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5c6e5f-8184-3bf0-a590-4cac016dffbf | -6.4381 | -52.715302 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9dd8533-f82b-3fb0-9430-e653f5bd101b | -9.0542 | -57.068699 | 2026-08-21 00:42:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45bbf9e4-2743-3870-b5f2-acf8214ebd1a | -10.5283 | -50.808498 | 2026-08-21 00:42:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5c91422b-1f68-3fd4-87cb-c36980454d35 | -10.5267 | -50.8008 | 2026-08-21 00:42:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45fcbff6-b849-3327-95d5-9e6257f92e52 | -6.0651 | -47.829399 | 2026-08-21 00:42:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5810279-ae73-3de6-bbd7-e78c554a772f | -10.3048 | -48.2346 | 2026-08-21 00:42:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47cd48c2-0155-3c77-816b-52eaeccefbfc | -14.719 | -47.148102 | 2026-08-21 00:42:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 789d26f2-1637-3f82-bc1b-02427477cfff | -18.1984 | -50.761002 | 2026-08-21 00:42:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9dfece31-7969-361c-8a61-c7e81831ca33 | -11.1776 | -54.001999 | 2026-08-21 00:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e32191b1-01c7-38cc-ac22-0e7add998638 | -12.434 | -43.400398 | 2026-08-21 00:42:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3e68696-6afe-3aec-9ad1-19b2354282de | -7.3507 | -45.8186 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d91a7f66-678a-350c-a2e9-a640910f366a | -13.3973 | -54.358398 | 2026-08-21 00:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef36ee89-5609-36c2-b0dd-1c39442edffc | -6.9638 | -50.414101 | 2026-08-21 00:42:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1124e606-0e23-3b79-b9b0-276224ee7811 | -9.4014 | -60.4002 | 2026-08-21 00:42:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f68f8eeb-9bff-3103-9d74-adec760dd997 | -6.2302 | -55.415001 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7298fe20-5c3d-3bff-aebd-04ce9f3b21f7 | -7.3722 | -45.822399 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27ef26f2-bb05-3705-a118-795c00b83327 | -12.7315 | -48.486198 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48a81b6a-98d7-3afa-b5da-45c455a5f5d8 | -12.4364 | -43.410301 | 2026-08-21 00:42:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4cb617d6-e3d7-3e5a-ac3c-ed94eedbee5d | -6.3917 | -54.934502 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87ce9f0b-3fa8-31cf-8c59-cb196ac3e8d0 | -3.2658 | -49.518398 | 2026-08-21 00:42:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f44fef4-5f62-39db-b208-b02a6f1e36b3 | -5.1743 | -47.948299 | 2026-08-21 00:42:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d4d05d84-033a-3fb4-be8b-9c939c5d7598 | -12.2286 | -43.152 | 2026-08-21 00:42:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 24ce0919-2e08-3b7a-8432-e6e22161f78a | -18.027901 | -44.601101 | 2026-08-21 00:42:00 | METOP-C | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 23c3a0f8-3f1d-3c2c-bf6f-d9b11ecce4f7 | -2.7721 | -48.580601 | 2026-08-21 00:42:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1c83be1-a248-3160-ae55-0eb7eec37ce4 | -20.186399 | -49.117901 | 2026-08-21 00:42:00 | METOP-C | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf9502c9-c2a4-3749-be83-2913054e8e15 | -10.5216 | -50.777599 | 2026-08-21 00:42:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f7d5c81-f338-39a8-99de-1251279851b6 | -10.7553 | -50.3438 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf00b0d7-392f-38cc-be66-d5501f3631cf | -12.7973 | -48.412102 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e48ce4c-183c-34c7-8dc4-cc19022f7515 | -10.801 | -50.271 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3fe027fe-3819-3db8-adbb-d66b08da34f9 | -14.3014 | -51.831001 | 2026-08-21 00:42:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 833450c6-4f66-3751-b223-d1ed0b534242 | -9.4171 | -60.428799 | 2026-08-21 00:42:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40231637-9f66-3d2e-924a-98a43982d257 | -11.2113 | -55.0578 | 2026-08-21 00:42:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e701c04-e1db-3965-b12c-f7b1168fdf28 | -20.3146 | -44.612598 | 2026-08-21 00:42:00 | METOP-C | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 001fd87c-0edf-330b-bf67-d0d681c377d2 | -7.2503 | -49.902599 | 2026-08-21 00:42:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 576bc584-e220-396f-94e9-2a658bad0e16 | -18.048401 | -44.423 | 2026-08-21 00:42:00 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4e48dcbc-c38a-3ab0-8c1d-0a9a0bef1bc9 | -7.7765 | -61.139801 | 2026-08-21 00:42:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c2ef93b-04b2-39a5-b655-c1bf0a120d86 | -6.3721 | -54.938599 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac1a70e2-4106-3af2-8a48-e78080ca0f92 | -14.7158 | -47.133999 | 2026-08-21 00:42:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 11e69077-0c50-30a3-8518-75d35cd7b60a | -8.0955 | -51.660099 | 2026-08-21 00:42:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c751245-fa09-38d0-8ee7-52d892637e8d | -20.6458 | -47.1852 | 2026-08-21 00:42:00 | METOP-C | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c0e9613f-dc3e-33c6-a1a4-c2f187626a2d | -11.4899 | -45.108898 | 2026-08-21 00:42:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5fe65111-b003-3d10-979b-b11c266624e6 | -7.3645 | -45.833099 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4a0c981-5756-3630-b83f-0c9d51552a6e | -10.7455 | -50.345901 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d67946f9-2d1a-3c34-a826-bab3577721e8 | -22.757999 | -41.881699 | 2026-08-21 00:42:00 | METOP-C | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2262fde1-ed5f-3b5f-a8ad-37af99c94fb1 | -12.8087 | -48.416901 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94c90fb2-0f8b-3b24-8fca-b322b0458f0f | -12.2628 | -43.165298 | 2026-08-21 00:42:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 36dc76e9-b753-3c21-9600-12a162051283 | -9.0547 | -50.883598 | 2026-08-21 00:42:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9e3899f-495d-3c9d-857b-7cab6dea97f7 | -6.6975 | -58.935699 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9bc782fd-ac3f-3b72-89f5-d9df73121f9e | -9.4306 | -48.244701 | 2026-08-21 00:42:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b141c2b-2d7b-32df-9c77-f83330d4ea96 | -6.6833 | -58.915901 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1de558f2-4878-3b33-b5d2-882e1659d555 | -3.8474 | -49.0411 | 2026-08-21 00:42:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5ed0c30-71c6-31a8-811c-2af8098e16b8 | -8.114 | -50.032902 | 2026-08-21 00:42:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94ca0ad6-9271-376f-be16-893d0d8e8f0d | -6.5761 | -58.983398 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c84da6a0-c405-38e1-9a72-f92ff3ff972a | -6.24 | -55.412899 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 441ced6c-3ed1-3cd6-bcf4-62a9069da4f1 | -23.536501 | -47.320301 | 2026-08-21 00:42:00 | METOP-C | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6eb9369a-b44f-35e7-9d1b-a5d84992a5fd | -11.3556 | -45.9865 | 2026-08-21 00:42:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f91adc3-9bb5-3ebb-a7b7-580b1fd71947 | -11.1604 | -54.017899 | 2026-08-21 00:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 601a7156-fd46-35ca-b7d0-bb25592e0775 | -18.2003 | -50.7705 | 2026-08-21 00:42:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4d0c476e-c35e-37c3-a788-662e723fb71b | -6.8652 | -43.7365 | 2026-08-21 00:42:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 11408669-e29d-35e9-b26b-09b3580610e4 | -13.4396 | -51.815701 | 2026-08-21 00:42:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5295de8b-624d-3863-a08b-b519ec88e527 | -4.1904 | -49.4123 | 2026-08-21 00:42:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59797af9-e6bc-3330-ae25-cf8872755651 | -5.5989 | -44.0014 | 2026-08-21 00:42:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8965ffec-26a9-3ede-86d2-973b2f5a2dbb | -13.9801 | -49.4398 | 2026-08-21 00:42:00 | METOP-C | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2d3fc151-921f-3549-b09a-79e3d11aff35 | -10.3033 | -48.2276 | 2026-08-21 00:42:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d8a7082-5eeb-334e-82f5-35596419b467 | -9.0562 | -50.843899 | 2026-08-21 00:42:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98f50938-3515-31fc-9ee1-15c7b901504f | -9.4521 | -51.6171 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d551ca-af65-3d33-ac63-220e97476b3d | -6.3844 | -54.948002 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76b036f5-c2f8-3c07-a137-b72aa1896a09 | -10.3124 | -50.293301 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a40911b2-4e38-39f3-bba1-c48306bdcfce | -6.3499 | -44.0812 | 2026-08-21 00:42:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3cc10863-197f-34a6-9a27-5c872e27354d | -12.7578 | -48.4655 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2d1ac5b-3a6b-39a5-a553-1310f0b3239a | -14.5741 | -53.021198 | 2026-08-21 00:42:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63b4b9ae-6198-3942-a71a-ef2c76c7c287 | -13.2464 | -51.6255 | 2026-08-21 00:42:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aba18b54-e5e3-3a78-a184-b2ab0a13f765 | -22.073299 | -46.554001 | 2026-08-21 00:42:00 | METOP-C | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39795c83-bdd6-3f80-8a1f-eeaf39b5de27 | -6.8413 | -59.4291 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a65420bb-b63b-36fe-b3bb-ce23be1634c2 | -10.6232 | -51.623299 | 2026-08-21 00:42:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7ea22bb-74c5-3e9a-885f-5d7d9f5cabee | -12.5072 | -47.853901 | 2026-08-21 00:42:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e71d1e72-294b-3670-81ca-eca592deaea2 | -6.4359 | -52.751499 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad25f7b6-dcb0-347a-970b-527b228b2dd5 | -12.5136 | -54.7644 | 2026-08-21 00:42:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08ec37a3-0e22-3d4b-acd0-40dc5e84b9d9 | -9.9986 | -48.566002 | 2026-08-21 00:42:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aeb4418c-98ae-37d8-ae81-ac11b28fab22 | -12.2556 | -43.178001 | 2026-08-21 00:42:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2f294178-a4a1-39a0-b590-b3d5bea896f8 | -5.1645 | -47.9505 | 2026-08-21 00:42:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cdf19749-b7e6-3b4f-a077-cfba687bd529 | -12.846 | -48.4454 | 2026-08-21 00:42:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c649a14e-5ed7-3eca-9587-887570a61f69 | -6.2246 | -55.624699 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa048ec-45cf-34cc-bcab-a967c7a75952 | -8.4537 | -46.959202 | 2026-08-21 00:42:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1475f9df-402d-378a-8528-6fa72117d786 | -6.0667 | -47.836601 | 2026-08-21 00:42:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e72df5e4-b4cb-344d-aa01-59d2fae71448 | -21.0755 | -43.257198 | 2026-08-21 00:42:00 | METOP-C | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 091a32ce-fa58-3f71-912b-6d11f24b316f | -6.2427 | -55.425201 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 856498bf-349e-35de-9c2f-c68c0d04ccdd | -8.4422 | -46.954102 | 2026-08-21 00:42:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8aa85be6-82d2-309e-9170-6af9bc385995 | -4.0864 | -42.499001 | 2026-08-21 00:42:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5f08489a-9e17-3403-bcb4-e22abcbd4958 | -10.7765 | -50.2999 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 091eae1e-390d-3938-bd97-de608135fe1d | -11.6379 | -46.5336 | 2026-08-21 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd1909a6-cdd4-3bf0-9c60-9dd7de6f69c6 | -12.7413 | -48.484001 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94bbe132-03a5-3a4a-a42c-facaa36ed5de | -10.3092 | -50.2785 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbbfb742-44b7-35a7-8de3-28b1efadaf43 | -16.959999 | -44.721199 | 2026-08-21 00:42:00 | METOP-C | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| babbbf66-74d2-3285-8383-ba2b0858bee3 | -20.9659 | -44.614399 | 2026-08-21 00:42:00 | METOP-C | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3735afb1-d310-32da-8aa8-d1eb56b62545 | -14.012 | -53.669899 | 2026-08-21 00:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
