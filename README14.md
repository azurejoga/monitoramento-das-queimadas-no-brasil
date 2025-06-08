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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f406cd07-9ea5-35e4-9675-925af8fcd6eb | -15.05864 | -60.05437 | 2025-06-08 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9d7fa65d-198b-3721-ac60-9ef0842acc6d | -14.03447 | -55.12775 | 2025-06-08 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e90c364c-e0d3-3669-99b6-ed691516d6a4 | -13.88542 | -56.2047 | 2025-06-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28d36da5-75d3-3a8d-b2fa-d816822822a5 | -13.88474 | -56.20967 | 2025-06-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dce598a7-15fc-389e-b7ce-7aebbd19251e | -14.88261 | -48.12914 | 2025-06-08 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0388bd5-0430-3a24-8efe-af965993409b | -14.42916 | -50.64794 | 2025-06-08 05:21:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6703ef1a-960b-368f-9b27-1c60d966c00a | -14.8869 | -48.12855 | 2025-06-08 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b22213b-1630-37dd-b4fa-bbddc8d7c33b | -18.72587 | -54.19258 | 2025-06-08 05:21:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef1a4e66-4990-34e1-9d90-d4558bca61ab | -18.72703 | -54.19341 | 2025-06-08 05:21:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb59c0ab-9dc0-3afa-a32e-cca34074858a | -14.88314 | -48.12395 | 2025-06-08 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71afc22e-7fe5-3c77-8a07-786ce0762b42 | -14.8904 | -48.11871 | 2025-06-08 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8012cff5-0acd-3ff6-9588-d849032b141d | -14.88791 | -48.11805 | 2025-06-08 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ef6f883b-a015-3142-aa74-11809d3b66ed | -14.02927 | -55.13503 | 2025-06-08 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 364fa2a9-9adb-387a-84fc-42b962684364 | -13.4704 | -56.85608 | 2025-06-08 05:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8c661f01-9f2b-3713-b7d7-773d9a08599b | -14.04177 | -55.13671 | 2025-06-08 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ab9b26a-50aa-3b4e-bbca-6c3a8314dd25 | -14.02978 | -55.1311 | 2025-06-08 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80b7c2b6-19da-3ee0-a699-cc2a0650bd9a | -13.88086 | -56.20909 | 2025-06-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ab1950d-755b-3b30-a7c2-d6f7b6cbad83 | -13.47411 | -56.85667 | 2025-06-08 05:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 21ece6f8-e438-32d2-a2dd-01bce19fc5fe | -14.43482 | -50.64869 | 2025-06-08 05:21:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2267ec07-3658-36cf-9524-d56f36147cbf | -18.72286 | -54.1877 | 2025-06-08 05:21:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98e72860-5934-3528-a472-e4dcf12ae6f9 | -14.4318 | -50.649 | 2025-06-08 05:21:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e5b6ad9-613f-30c0-b5c5-40b8577c7394 | -13.98801 | -56.00905 | 2025-06-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1516c07-d5fe-3281-a83b-5bbc094cfb55 | -14.26478 | -52.45447 | 2025-06-08 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0facd96-a5f4-34a0-8080-e827a9daaea8 | -13.88154 | -56.20411 | 2025-06-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a389218d-9079-3a9d-8cd3-bf3edf30f0aa | -17.68139 | -52.1114 | 2025-06-08 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 720e4fb8-7c07-3432-9f04-5a054d10d4da | -14.03759 | -55.1362 | 2025-06-08 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6f58389-222b-3e2b-9627-76965cd62968 | -18.72228 | -54.19294 | 2025-06-08 05:21:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 799b2549-5d9a-309a-8e25-bf854aed7ed6 | -18.02498 | -47.38177 | 2025-06-08 05:21:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac5797db-f7c2-3b77-ad69-429c3a773fa3 | -14.03708 | -55.14011 | 2025-06-08 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83992fe9-0627-3cc9-ba8e-435d8f3626fc | -14.88741 | -48.12329 | 2025-06-08 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5041afdb-2c40-3184-a104-20ba66670a20 | -9.92458 | -59.90044 | 2025-06-08 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8af6ddf-e127-3c2c-a482-8d881e678bc5 | -9.37001 | -64.45695 | 2025-06-08 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49f59d6a-bda4-39c1-ae34-5b3327dccde4 | -11.11998 | -54.65103 | 2025-06-08 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7408ecfc-328e-3e3d-8109-67c6688741dd | -11.11685 | -54.65272 | 2025-06-08 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1afbbed8-2187-3f3e-a2aa-fc7130b762e7 | -11.3815 | -56.55992 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85316068-c7ff-30d6-b1b9-b30e94a513e4 | -11.11806 | -54.64271 | 2025-06-08 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cb46a3db-60d4-3273-831f-f239673ec591 | -11.12055 | -54.64605 | 2025-06-08 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a7e25b4d-bb49-3bbe-9155-ae97beb718c0 | -11.54261 | -56.45708 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e275fdc3-d5d5-3cbb-b97a-88e3f0efd751 | -9.925 | -59.90145 | 2025-06-08 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9072d4f9-9199-3317-8fb6-4a38fdfcf560 | -9.18626 | -63.33307 | 2025-06-08 05:44:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57584886-47e3-3935-a2e7-7b383d72efd7 | -11.54921 | -56.45008 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b844db6-7ccb-35c2-a952-29f068b5a026 | -10.49436 | -53.66381 | 2025-06-08 05:44:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20b89776-37ac-3ccc-b930-e70e4477a58e | -11.54563 | -56.45887 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f550ef08-30cf-3b61-a59f-7ead6a1d8bde | -11.54611 | -56.45502 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72897671-7ebc-3fe6-b8a1-19c0ec9f87e8 | -10.49366 | -53.66959 | 2025-06-08 05:44:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8751afb6-a52f-3f1b-9040-b6afa18a389d | -11.53996 | -56.45812 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b01e95ec-09e9-3175-92fe-21b872155136 | -11.12749 | -54.64161 | 2025-06-08 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f548ae3c-a008-3bd7-88b7-7b3404837117 | -11.12691 | -54.64668 | 2025-06-08 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0ebeec28-43d4-3b53-994f-95b834f44743 | -6.99726 | -63.09819 | 2025-06-08 05:44:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cefdb4b6-08ac-375a-95d0-10269f2297e7 | -11.12441 | -54.64338 | 2025-06-08 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 943989f7-ba18-3eb5-861d-9cdca9f7f534 | -10.29837 | -57.13802 | 2025-06-08 05:44:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c075ed58-1547-3d46-9ceb-a2fe436cf5f4 | -10.29617 | -57.13306 | 2025-06-08 05:44:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf2ee80d-26a9-3092-a25c-89e0f5921e40 | -10.29572 | -57.13641 | 2025-06-08 05:44:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39117b01-6f85-3d13-8efa-5adc2fa90dc0 | -9.91942 | -59.90927 | 2025-06-08 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 056b17c8-57ca-3ba6-b527-955cf3f2f842 | -11.1232 | -54.65334 | 2025-06-08 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 64ea15f2-ced3-3645-a9f1-ecf68889dd7a | -7.89181 | -61.47371 | 2025-06-08 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a7bc06a-af11-3699-8988-8721b23c0ca5 | -9.16075 | -61.40929 | 2025-06-08 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97e1dc9b-fbe7-3cc4-b7be-db282b27f555 | -10.94713 | -55.33607 | 2025-06-08 05:44:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70e4866c-1c02-3473-aac8-e49f2a8f35fb | -10.30106 | -57.1371 | 2025-06-08 05:44:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5f23799-3858-3014-84ce-606ab7cbf2ec | -11.54044 | -56.45432 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2fd0074-883f-3ebc-a3b2-f82d3d80fed9 | -11.37072 | -56.55466 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e10954d2-1742-3953-acd7-cf72cb53d46e | -11.12113 | -54.64101 | 2025-06-08 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f6a4986a-ed41-33e1-98b6-d8a39a9bb4b4 | -10.29879 | -57.13464 | 2025-06-08 05:44:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5effcd5-439e-33e5-83c0-7d2b1b5081ea | -9.92877 | -59.93563 | 2025-06-08 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91336ed3-e958-357c-be55-7f0029504ce1 | -11.5466 | -56.45118 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba1c64a7-8686-3075-8f1a-8495ea5d25b8 | -11.11941 | -54.656 | 2025-06-08 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de8b70ad-c2ed-3bb8-9606-9e0e1f62ded4 | -9.64618 | -65.73987 | 2025-06-08 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5d0cb69-3422-3ff5-9927-d6af7a58db17 | -11.37682 | -56.55162 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f38e34a-03f0-3f92-ba34-5c35fd458500 | -10.30151 | -57.13374 | 2025-06-08 05:44:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70157268-6e74-32aa-a83a-40c4d6676f6b | -11.37635 | -56.55537 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 715b01f6-0e24-34b8-95dc-e36c4f5ad719 | -11.1238 | -54.64837 | 2025-06-08 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f3a5e03-c0dc-3f9d-8ecf-8987c05e5dce | -7.9062 | -61.50988 | 2025-06-08 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e6df03e-8b97-3b68-b348-cdd1f7be5cdf | -11.54875 | -56.45393 | 2025-06-08 05:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 884110ac-bb1e-3b86-adeb-c0bc589008d1 | -10.94768 | -55.33149 | 2025-06-08 05:44:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5934563c-cae2-3c11-9379-ac6fff2867be | -12.52618 | -58.36506 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27040638-e4bc-3056-a4c0-52aac07f2203 | -12.52804 | -58.35023 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 174bbe44-5676-32f5-bac6-8224892b6d5c | -12.52114 | -58.36423 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ee2d89a-b699-3ccd-bfd4-faa26d48a5b7 | -12.27303 | -55.07534 | 2025-06-08 05:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b1c4fbf-2566-3ed8-b9c5-13379e35260c | -12.66671 | -58.22004 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e98634ed-93c8-3ce8-8cae-eaba069c6a0b | -11.46659 | -61.94392 | 2025-06-08 05:46:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d8c837c-a473-357d-ad6f-840565170ce0 | -12.3693 | -57.41491 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f56bb8b1-bc2e-3847-877d-86cfa86da2c7 | -13.37352 | -54.24821 | 2025-06-08 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db7d00af-46fb-3d0e-a7f5-86f3cce89da4 | -13.46963 | -56.85467 | 2025-06-08 05:46:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ed241cb-a4b7-3c79-88cf-022098227251 | -13.46917 | -56.8586 | 2025-06-08 05:46:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ed87e82-d1e3-3927-8c06-d75846ad620e | -14.03831 | -55.13781 | 2025-06-08 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07f31e7c-24a8-3cbf-b526-e9a57cd7b819 | -13.47528 | -56.85556 | 2025-06-08 05:46:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4809366e-1017-34d2-8de5-76a77687b3b9 | -12.37639 | -57.40208 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6f9431e3-e103-3b94-b1bb-058f215b1ccc | -12.37057 | -57.40479 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b438c6b9-0b7f-31ab-8aa0-7af2b27bd14e | -12.66709 | -58.21697 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4509409-1582-383b-bc10-80dcabe69b6a | -12.37469 | -57.41559 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bfb3ecb7-6727-3308-8891-c7c392ce1cab | -14.03423 | -55.13847 | 2025-06-08 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c1b4c73-249c-35e3-8fff-7f8121108c56 | -12.36561 | -57.40069 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 36c366a0-a435-32e9-adc7-72ce0fe09144 | -12.36477 | -57.40742 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aaaa8470-f9fd-3a78-9b5e-d1d324624e57 | -12.52692 | -58.35916 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d19424b-6277-3520-9e11-d71a97190ab3 | -12.36519 | -57.40405 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9e2db3b-f014-32ae-a020-7e0e3cab56a4 | -12.37597 | -57.40548 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d83da28d-2a3f-3f5c-9763-7f78337176eb | -12.37143 | -57.398 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97b8cf60-4b0d-3279-8150-f44af1838648 | -12.52335 | -58.3465 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6aae5114-8ca3-37cf-84c3-d15b0e3778a8 | -12.36973 | -57.41151 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d98702c2-8018-34e2-914c-240cd1eba19b | -12.3805 | -57.41291 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README15.md)
