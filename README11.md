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
| 92ab8a4f-95f4-32aa-bf1b-6cbd0cdd1515 | -12.08843 | -49.48134 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68fbcc15-5c99-3d79-81ed-d2a1eda62ecf | -10.30112 | -57.14408 | 2025-05-31 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b43357dd-be04-36a4-959d-7fbb061606b6 | -12.10134 | -54.67126 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91876196-f8c2-3c5d-af67-7e06c06d1222 | -14.07064 | -44.09869 | 2025-05-31 04:27:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a14f7b93-4631-3375-91b6-968d9e54f84e | -12.60801 | -56.02077 | 2025-05-31 04:27:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c9270b3-cbe6-3fd5-8bf7-00e0d3e5a1d2 | -14.02849 | -55.13148 | 2025-05-31 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66d05d1a-17a2-3c54-b4e7-e08be3bed7ef | -14.66649 | -45.40537 | 2025-05-31 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb6f9d51-bedc-3808-9b52-3828a5f1a8fd | -10.73837 | -49.28674 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bece0bd7-1b89-339b-bf4e-2528bd7267e8 | -14.06766 | -44.10012 | 2025-05-31 04:27:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2341ca5a-ed03-3e3a-9393-cdb3d8f68dbe | -14.67002 | -45.40591 | 2025-05-31 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1bbdc16-595c-3855-b53c-bba859ff1eea | -10.73898 | -49.28297 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b6c9961-052b-362b-9a48-99b21be24d07 | -10.64689 | -49.43908 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b642c6fa-364b-3f5b-9e9e-c6770fd2d063 | -11.7059 | -54.5565 | 2025-05-31 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3894821b-9fd8-334d-ac5a-c4958bfaae81 | -15.88675 | -43.45425 | 2025-05-31 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| a1b4216c-f579-3704-b2ae-26fd81b62c20 | -10.46331 | -47.9467 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6c937a51-956f-3cb1-b2d3-808484ee41f9 | -13.10474 | -52.28838 | 2025-05-31 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 13a1d35d-c884-3b1f-93ed-da650680a103 | -11.90864 | -54.82294 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df947bf5-e1ec-30f8-a898-6eefffd663bc | -9.52519 | -54.76981 | 2025-05-31 04:27:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0b078ba-90bf-38a0-950a-e0ead48ad269 | -10.82749 | -56.95055 | 2025-05-31 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| de03b67b-ee9d-3ec2-a0fd-9806ec8d8152 | -12.60131 | -48.18099 | 2025-05-31 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a28e62f-2595-37c0-878e-0a8fcaf6dc92 | -9.24684 | -51.22545 | 2025-05-31 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 818a3b62-53bb-367b-8548-0a06d4da4847 | -12.01865 | -49.52 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 128cb1cb-b379-38c5-ae08-6afee4a3c4ac | -11.72725 | -56.43403 | 2025-05-31 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e49eb0bf-3b07-3e41-9c54-f3e321bec2c2 | -11.73419 | -56.42566 | 2025-05-31 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 388ffec9-c7b5-30fb-b07f-e2d59cb8e207 | -10.61355 | -44.7667 | 2025-05-31 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faa0ce7a-9b4d-346b-be2f-879b4196be12 | -14.44536 | -50.64943 | 2025-05-31 04:27:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0ea0216-6b7f-3eb1-ae88-ace702e77ce9 | -13.95024 | -54.48409 | 2025-05-31 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c07f9d8-5197-31cd-af98-f848f6d386e1 | -10.31169 | -44.95231 | 2025-05-31 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da26a054-4940-3993-a1b7-32d0c487fbf2 | -11.90726 | -54.8262 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d51901b-85b7-36c9-9f14-8e4bd70e6026 | -11.91279 | -54.8221 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7ae0cd1-9839-3d5c-9127-924b09f91611 | -11.8349 | -51.26472 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 50137738-337b-355b-9d99-97ed5fecda41 | -9.52564 | -54.76801 | 2025-05-31 04:27:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af5a9297-d5dd-3059-9e0f-0728d4cdedda | -9.71734 | -48.31254 | 2025-05-31 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1275bd3-727f-3fb6-b25d-ead528241a19 | -11.83415 | -51.26917 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 402a5f81-66ad-37fc-957a-ed4ac21677a3 | -14.84013 | -48.09363 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c4d7b840-ab39-3d10-9aee-5646ad8316dd | -12.01524 | -49.51942 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 587d138c-7797-3546-bb2c-1e59c2de541e | -10.46055 | -47.94266 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6ad28234-3eec-3f88-b215-1e959da7b5dc | -11.91187 | -54.82708 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 421a50b9-7d59-36fd-b363-dcd2313a579c | -11.91569 | -54.41826 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7544daf3-2f31-35ae-b1da-e6fd721a1ee2 | -12.10221 | -54.6665 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b9bca98-71f1-3825-9fe9-b7fbd9444016 | -10.65094 | -49.43584 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4d65f926-f80f-3df9-8197-6ecce5fee9f4 | -19.01934 | -53.48178 | 2025-05-31 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ac154b8-9b63-37c0-9161-934f42a02570 | -20.60903 | -48.87039 | 2025-05-31 04:29:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 06254626-64b3-3729-b7ff-926355c42f12 | -21.18434 | -53.18227 | 2025-05-31 04:29:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a06bfdc0-f518-35d9-985f-3820e869af03 | -21.25305 | -50.30553 | 2025-05-31 04:29:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 00317e5e-2275-36c9-8e62-fbd4130fcb93 | -17.97099 | -47.84969 | 2025-05-31 04:29:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61704ea3-0258-36d4-ae67-86c53721b03e | -20.76284 | -46.77083 | 2025-05-31 04:29:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 267319f8-0714-30c7-805c-f530daf62cda | -19.60331 | -44.81888 | 2025-05-31 04:29:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4f48905-1e2e-32a2-a20a-5ec5b762a859 | -21.1025 | -48.5032 | 2025-05-31 04:29:00 | NOAA-21 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1251aae5-f00e-3f77-a80d-a962fca029a6 | -22.63192 | -47.06491 | 2025-05-31 04:29:00 | NOAA-21 | HOLAMBRA | SÃO PAULO | Brasil | 3519055 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30e28a58-90ea-36bd-a1db-529748d521a8 | -22.53945 | -48.81345 | 2025-05-31 04:29:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbd92b8b-c160-3393-b242-526b9497de38 | -19.19805 | -52.09108 | 2025-05-31 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ef8d027-28d3-3cc7-9f12-84d1c16cbfac | -19.19597 | -52.08212 | 2025-05-31 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d64340f7-b7fb-357a-92d5-b0deecddf346 | -21.53148 | -49.5283 | 2025-05-31 04:29:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 68bb038c-1c08-3215-8302-5145e2f63ca0 | -20.3437 | -45.72752 | 2025-05-31 04:29:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 463cfb1b-c3fd-3166-a990-c34535b4585b | -19.19382 | -52.09457 | 2025-05-31 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35541846-c296-3a62-92c1-e9a157cbba52 | -19.19526 | -52.08627 | 2025-05-31 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33683602-6060-3229-b5fe-3f785069a0c9 | -20.5502 | -54.11979 | 2025-05-31 04:29:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd06949e-13a5-3cfb-8564-65a11fd7f392 | -17.26398 | -50.87514 | 2025-05-31 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e22ffc9-5935-3b25-92e6-c0ffdd39b8ff | -19.19103 | -52.08979 | 2025-05-31 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 110a3874-e8f8-3417-afdd-eb17a8f408b2 | -20.60959 | -48.86669 | 2025-05-31 04:29:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8935472b-ffa4-39e5-a04a-a92f2af4c22b | -17.11205 | -49.13929 | 2025-05-31 04:29:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a95cc525-3090-3fe0-bdba-c3283a7b0217 | -19.94951 | -46.49238 | 2025-05-31 04:29:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03af15b8-3a83-31a2-9e8a-d0b8f68fd988 | -18.49306 | -45.90297 | 2025-05-31 04:29:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6c24aba-2a31-302b-b3ae-f7c4d42d2cda | -19.19876 | -52.08694 | 2025-05-31 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8434e7c0-3b52-3921-abf3-ad88bb08a15c | -17.77556 | -49.05278 | 2025-05-31 04:29:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5feecea9-48a6-3d49-98e3-63ebef1d345a | -20.34542 | -45.7252 | 2025-05-31 04:29:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39b6c2fa-9a19-35b1-a438-8e956f61f762 | -19.19454 | -52.09042 | 2025-05-31 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e68c3c91-0282-3857-96c7-e5b4be5a18f2 | -17.02629 | -52.54267 | 2025-05-31 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42e78506-bc90-34c8-8360-359dfc4f1f21 | -19.96948 | -44.21818 | 2025-05-31 04:29:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9694408a-bc67-3cdd-82d0-e3876af6b95a | -18.83739 | -53.60465 | 2025-05-31 04:29:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20d7082d-ea09-312f-a34b-bc5b7441ab24 | -19.01915 | -53.48411 | 2025-05-31 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0354868-c22e-3302-81c8-ba9fff708639 | -18.83829 | -53.59966 | 2025-05-31 04:29:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94739e7e-edcb-306c-b61f-48f86a53b92e | -10.6492 | -49.4267 | 2025-05-31 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 4fe2aec4-f6b0-3a47-aa7e-a668cc4d14af | -11.8365 | -51.2854 | 2025-05-31 04:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 52fc2a72-e026-3c46-b97f-341846fb139d | -11.8368 | -51.2641 | 2025-05-31 04:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 8f2a7cf3-03dd-3d16-af2e-5189986329cf | -12.0154 | -49.5272 | 2025-05-31 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a255e300-36c3-35b2-a74e-ef9fe40ec1d1 | -26.87444 | -48.65697 | 2025-05-31 04:32:00 | NOAA-21 | NAVEGANTES | SANTA CATARINA | Brasil | 4211306 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f4326699-29cc-3504-8a98-5dec312f9b5f | -29.874 | -51.15884 | 2025-05-31 04:32:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 9ca904e9-378c-37f9-b97a-736cabd4c88d | -23.33847 | -53.06764 | 2025-05-31 04:32:00 | NOAA-21 | TAPIRA | PARANÁ | Brasil | 4126900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7364f9d3-f66d-31ec-96ae-d0979cf1734b | -24.07806 | -49.85669 | 2025-05-31 04:32:00 | NOAA-21 | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 74957dcc-f679-3ecc-a9e4-2bf3570db247 | -23.45254 | -46.73941 | 2025-05-31 04:32:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dadfd76e-2088-36da-bc3a-d3b7bc442354 | -24.29673 | -49.93751 | 2025-05-31 04:32:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa8623fc-c779-38b7-b05f-83d9c5cb3363 | -11.8365 | -51.2854 | 2025-05-31 04:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 3cbc7345-a244-3a6c-93a3-5d39e117b1e2 | -11.8368 | -51.2641 | 2025-05-31 04:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| f714e73c-aff7-3825-98eb-6cf568b10f58 | -10.462 | -47.9428 | 2025-05-31 04:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 5650a8e4-8797-3da2-9090-28db2a0c0fdc | -15.8757 | -43.4566 | 2025-05-31 04:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 6b2b5d28-6b72-3602-bc7f-17c42d044530 | -12.0154 | -49.5272 | 2025-05-31 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 9305d1f4-aa0e-3ee6-acd0-ee59b938bd92 | -11.8368 | -51.2641 | 2025-05-31 04:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b707840a-af14-3002-9c0d-aafb383889ee | -6.2123 | -43.34095 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cf61cf2-c19e-32c2-a1fb-ebb3c33dad6d | -6.15022 | -42.61572 | 2025-05-31 04:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ce74822b-70c1-3e56-832b-c02c14473ec2 | -7.24335 | -43.09032 | 2025-05-31 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 49663459-f6a9-3344-9beb-4a9cbb3b812b | -7.24887 | -43.2597 | 2025-05-31 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 337bc51b-82c6-3b6d-9772-8d209ed5264f | -7.00513 | -44.62477 | 2025-05-31 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7b5e775-7be9-3b79-a8b4-6cf7bcd2d89a | -5.86334 | -42.8396 | 2025-05-31 04:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ade5064a-540b-393b-a49a-07d8374c6c66 | -7.24437 | -43.09531 | 2025-05-31 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6f0298b9-7861-37e2-90a6-71c30edde16b | -6.20245 | -43.33239 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a64ed035-a8a9-32eb-845a-6565047f6b12 | -5.84943 | -43.63781 | 2025-05-31 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 844c1c16-f2de-3c56-a7ad-86c67933ca7b | -7.24489 | -43.0916 | 2025-05-31 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e350323c-5024-32cf-9fca-b78ea566fcf6 | -5.05232 | -43.24839 | 2025-05-31 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README12.md)
