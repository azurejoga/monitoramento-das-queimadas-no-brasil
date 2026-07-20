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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 746e4899-7298-3c64-bdee-4302771d94fd | -7.76717 | -63.84857 | 2026-07-20 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 603079ef-8f50-330f-9a27-010b04b8837c | -6.59028 | -51.70622 | 2026-07-20 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44ee363b-82c1-3a7f-9441-a8980ca2a21e | -8.93313 | -47.60619 | 2026-07-20 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b132ad2e-d0d2-38ce-bde7-4352dc1d1570 | -10.21164 | -48.87668 | 2026-07-20 05:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 190e5749-a193-37dd-901e-c2e4c637925d | -7.77145 | -63.84933 | 2026-07-20 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4aa6e08-0ef7-3232-92b7-9ac549b4356a | -11.26357 | -49.9504 | 2026-07-20 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bff5fc2b-964c-316f-8ec0-373608881ea2 | -10.90481 | -56.37123 | 2026-07-20 05:23:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 61a34fcf-686f-3875-b99f-5cff30937853 | -8.9443 | -47.61196 | 2026-07-20 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 729d3fd1-645f-3da8-9bdb-953629822dfb | -10.46849 | -49.09692 | 2026-07-20 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fdbd0502-68eb-39ea-92d1-dcb15e9ec1f1 | -21.13052 | -47.46221 | 2026-07-20 05:25:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57154a0e-3ea2-36c0-a209-ef11ea938ef0 | -23.17753 | -50.48793 | 2026-07-20 05:25:00 | NPP-375D | SANTA MARIANA | PARANÁ | Brasil | 4123907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 34b9f19c-1f47-3052-addb-56cd661ca4e1 | -13.34688 | -54.3133 | 2026-07-20 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91e8904a-f88a-303b-b76a-94db60443efb | -13.68338 | -48.79801 | 2026-07-20 05:25:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcb787c6-6c59-3e7b-a57c-870f6cfaa10f | -23.17715 | -50.49238 | 2026-07-20 05:25:00 | NPP-375D | SANTA MARIANA | PARANÁ | Brasil | 4123907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d1bc8517-d367-3b8d-a458-f86b1b2c1338 | -23.17866 | -50.48697 | 2026-07-20 05:25:00 | NPP-375D | SANTA MARIANA | PARANÁ | Brasil | 4123907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 23330101-7174-314a-9e54-2516214fcc9c | -22.37546 | -54.65187 | 2026-07-20 05:25:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c34a7a3c-0b69-384e-aae5-868ffa617ec6 | -13.68911 | -48.79919 | 2026-07-20 05:25:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8ec0b19-e200-3e16-bb0d-baa5f9627912 | -20.28477 | -46.42453 | 2026-07-20 05:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94240d26-d531-3a94-989b-be68cbd079c8 | -20.28037 | -46.43135 | 2026-07-20 05:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28fd3941-b4da-3be3-b099-7720dd0fb8c9 | -21.98957 | -56.01716 | 2026-07-20 05:25:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed51f837-00d3-36c8-bc93-8b52e0c2beed | -21.60606 | -46.61471 | 2026-07-20 05:25:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b501187f-7435-39d7-acd7-a8105d1bfbc0 | -13.68952 | -48.79569 | 2026-07-20 05:25:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 794259fa-5170-3904-b36d-74e8dd6252e4 | -20.28425 | -46.43113 | 2026-07-20 05:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89664263-6ea9-3e4a-a9d4-540904728bc3 | -12.9925 | -62.1578 | 2026-07-20 05:25:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79986b2a-e4e0-396d-8413-fdb401d1618a | -20.28825 | -46.42211 | 2026-07-20 05:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a792ac7-9d24-353d-a249-aec7b5d5e724 | -21.60557 | -46.62192 | 2026-07-20 05:25:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b9754dbe-a43e-310a-8266-f880794ac3cf | -23.17826 | -50.49145 | 2026-07-20 05:25:00 | NPP-375D | SANTA MARIANA | PARANÁ | Brasil | 4123907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 23d08ed2-bef0-3e80-acc3-ec3cfbb4fed3 | -12.99608 | -62.15846 | 2026-07-20 05:25:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b58f69bc-0f48-3b16-b545-1b31e8d68260 | -12.88725 | -58.28874 | 2026-07-20 05:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bde4e67f-da85-31d5-aee6-8b7b283b3f38 | -12.99679 | -62.15426 | 2026-07-20 05:25:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31e44f52-9536-32e3-b51e-a6f8fe6f008b | -20.28781 | -46.42803 | 2026-07-20 05:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb516d68-0d13-3328-9582-71792193c981 | -14.11611 | -46.35363 | 2026-07-20 05:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3739db15-ed66-3fe8-b0ba-a35b2fcb7391 | -21.13737 | -47.46239 | 2026-07-20 05:25:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| debc41f1-7806-3793-9a8d-05d0103bee1c | -10.90585 | -56.36528 | 2026-07-20 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3113fdbd-8ce2-3988-9536-4ad14619231f | -10.55371 | -56.34002 | 2026-07-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bef4886b-595b-3fd9-ad4b-4fc0e65d50d0 | -9.10293 | -59.3994 | 2026-07-20 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ebb1feb-b164-37f8-9742-138b646032aa | -12.99193 | -62.16131 | 2026-07-20 05:42:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e99273c6-dbaa-3ebb-8705-d1903e84d5b7 | -11.74618 | -57.81631 | 2026-07-20 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09e4e98b-c795-342a-baaf-cbd1ced62529 | -9.09838 | -59.40241 | 2026-07-20 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f03bf4b5-74f7-3262-b300-2b43f00780a4 | -11.74684 | -57.81132 | 2026-07-20 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 281c5919-8fbe-36a3-88ac-842043fd94ac | -10.90507 | -56.37148 | 2026-07-20 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f42e6097-7326-35a5-a679-e706f688da53 | -9.16686 | -61.4082 | 2026-07-20 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21c333ec-f1ed-3d86-be1f-175b7497aeec | -12.99679 | -62.15335 | 2026-07-20 05:42:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6c1b64f-ca2f-3d63-8133-f32c4c7a2a6d | -10.54984 | -56.33017 | 2026-07-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2784fa37-ae0d-3a38-b57c-26bab0f2a33e | -10.55491 | -56.33095 | 2026-07-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af49c88d-decc-3f96-bf7c-f72627cc9611 | -9.10242 | -59.40299 | 2026-07-20 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 89251161-0e26-3706-b6c5-8860be006e91 | -7.76441 | -63.84876 | 2026-07-20 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9469883f-efd0-3811-a66a-9fa26d911414 | -7.76827 | -63.84581 | 2026-07-20 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f97b734-8f4d-3a73-b018-0a6ed4ca5aac | -10.55411 | -56.337 | 2026-07-20 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b981575c-a963-3753-9fe6-06a0e5346d89 | -12.99255 | -62.15706 | 2026-07-20 05:42:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b40a76a-cfd1-3788-8746-cb34ae85a965 | -10.90797 | -56.36475 | 2026-07-20 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3df3942d-fd0a-3beb-abfa-50de36ffe53a | -7.77182 | -63.84668 | 2026-07-20 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 747fa996-552c-3368-9d45-cd529feff400 | -9.09889 | -59.3988 | 2026-07-20 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 927812da-8b9c-3d61-8dc3-985a5dff1aa7 | -11.74218 | -57.81065 | 2026-07-20 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60f092c1-a14a-3b9d-a5c2-a816804e3f18 | -10.90713 | -56.37097 | 2026-07-20 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9414420f-046e-3f75-a577-a16cb0fe46b4 | -12.99617 | -62.15759 | 2026-07-20 05:42:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f242a3b-3f5a-3437-8673-5d464eedcd95 | -9.25769 | -59.83168 | 2026-07-20 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc35160e-1eb7-39c1-9f89-f39f4673c502 | -10.90546 | -56.3684 | 2026-07-20 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1027e691-dfd7-34d7-a41d-ecb662140563 | -10.90755 | -56.36788 | 2026-07-20 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 529cc032-d5e4-36cb-b538-660e19fd4aee | -16.80807 | -54.59329 | 2026-07-20 05:44:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0964085-afca-3ce9-ac33-87aaf246a66d | -11.82828 | -44.75801 | 2026-07-20 06:27:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3e0f78c1-0680-3584-9899-8c92d1e02a29 | -22.69422 | -48.68573 | 2026-07-20 06:29:00 | AQUA_M-M | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 98503a01-fbd2-34e0-bbc9-2c42d21f3e72 | -8.02069 | -37.07286 | 2026-07-20 11:04:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 63373bab-2c30-37d9-a571-f53e5b2d0d08 | -7.76899 | -37.59499 | 2026-07-20 11:04:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 18.3 |
| b5146a00-de8e-344f-80cb-1a181783ead3 | -8.01932 | -37.08225 | 2026-07-20 11:04:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 7.7 |
| f38ff6f3-d86a-3c81-a780-36d056315cc3 | -7.77045 | -37.58506 | 2026-07-20 11:04:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d57a2a51-6c66-32b3-a8b7-a00331038140 | -19.87631 | -40.72899 | 2026-07-20 11:06:00 | TERRA_M-M | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 41b4f81e-9181-3a99-85c3-65b9db85f60e | -21.52715 | -41.30629 | 2026-07-20 11:06:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 43.1 |
| 6c0d35aa-ac69-30e8-a228-ebd3b6e098b2 | -21.52538 | -41.31752 | 2026-07-20 11:06:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| d11423cf-2640-376e-90a3-61a4fc13adf6 | -12.4947 | -48.2607 | 2026-07-20 11:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 02644b63-e786-3692-a09d-77564db44cc8 | -12.4947 | -48.2607 | 2026-07-20 12:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| bfb910cc-f523-3215-aa07-d9e1c349a157 | -21.1262 | -47.455 | 2026-07-20 12:10:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 08ab00a1-6de4-3ece-a5ff-e2755263fe15 | -12.4947 | -48.2607 | 2026-07-20 12:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 88c0bb20-a218-3aa5-b305-8e9d41be2bdb | -21.1469 | -47.45 | 2026-07-20 12:10:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 117.6 |
| e5d8171b-ac3e-3c6c-b237-3db599f94d2b | -11.99689 | -50.55381 | 2026-07-20 12:42:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| da1f9e09-d7e9-3b90-8b5d-7eac7d788dd3 | -11.99805 | -50.56098 | 2026-07-20 12:42:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 9d457192-4ce1-3c36-a4ca-e0a28ada2586 | -11.748 | -57.81227 | 2026-07-20 12:42:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 88dd3747-498a-3e78-97d8-95206449078e | -9.09992 | -59.40365 | 2026-07-20 12:42:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4f1b099a-6d77-3729-8177-9acacaef29ea | -9.1012 | -59.39451 | 2026-07-20 12:42:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d072aeb-dcbc-3447-adf3-9c717b41a616 | -12.99548 | -62.15611 | 2026-07-20 12:44:00 | TERRA_M-T | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5920e1e6-8cc8-3b92-a522-f1ea7aaf9e12 | -19.92225 | -56.86582 | 2026-07-20 12:44:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 99bf2a22-3b76-3b53-bace-04ac968a065e | -19.92024 | -56.88402 | 2026-07-20 12:44:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 86038904-6747-3f0d-88cb-7879b9af63f1 | -12.5138 | -48.2581 | 2026-07-20 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| c02c9f5b-5365-3cf9-9edd-b679b09efe33 | -10.7081 | -50.6425 | 2026-07-20 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| dbaa9250-93db-3acf-9c73-5e1acfecad05 | -9.1969 | -46.4408 | 2026-07-20 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 302db29c-7d67-3092-8100-0c693ff53ed1 | -10.7894 | -50.2285 | 2026-07-20 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d3e198a7-dbb4-3715-906f-9c499a549ac3 | -10.7894 | -50.2285 | 2026-07-20 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 1cf94e39-7435-327c-a1ed-5f44327f34c4 | -5.8967 | -46.1983 | 2026-07-20 14:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 9dc992cc-ad96-3b79-bf51-dfddb84cbc52 | -10.8084 | -50.2265 | 2026-07-20 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| cf4fe65c-fb71-33ae-8044-392fd7c1e9c2 | -10.7894 | -50.2285 | 2026-07-20 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6553a41a-be99-31e0-9265-dc660b07a193 | -10.7081 | -50.6425 | 2026-07-20 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| cec5db9f-301e-34fd-881f-9d30a708f3b2 | -5.8967 | -46.1983 | 2026-07-20 15:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 48eee156-c4ab-383d-8c21-078c3f305af4 | -10.7081 | -50.6425 | 2026-07-20 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ccded527-d323-32af-937a-4078e85d4315 | -10.8084 | -50.2265 | 2026-07-20 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| fcaf354c-122e-3ba7-a4d7-e0a35d764e18 | -10.7894 | -50.2285 | 2026-07-20 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| cef0b039-c9c1-34e4-9f43-8c57914648f4 | -10.7081 | -50.6425 | 2026-07-20 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5e230827-272a-3a2f-bad6-2efb9eef4aa1 | -10.7894 | -50.2285 | 2026-07-20 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 3d851ade-82c8-38bc-ad8c-7a99c2f465ac | -10.7894 | -50.2285 | 2026-07-20 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2131f319-a2d8-34d8-8ebf-ba92fc166fb8 | -10.8084 | -50.2265 | 2026-07-20 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 1195ce6b-e830-3a8f-8993-634b970c63fb | -10.8084 | -50.2265 | 2026-07-20 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |


[Clique aqui para ver as próximas entradas](README7.md)
