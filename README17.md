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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0377ee8-ebf9-3005-af80-d629801a9d16 | -19.02371 | -57.62202 | 2025-06-14 04:17:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 55165bbf-e065-3780-b650-86a3266fb040 | -17.37907 | -53.82127 | 2025-06-14 04:17:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3957af6-972e-331a-a5f0-3d20b94a4c8c | -16.78543 | -49.1134 | 2025-06-14 04:17:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 608db0ee-e316-3641-935f-7c22436fc304 | -17.97957 | -44.26434 | 2025-06-14 04:17:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5409d0a5-a3e8-360a-8251-dfbebe859b12 | -20.41565 | -43.55066 | 2025-06-14 04:17:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 470aa136-4ce1-36ff-bda5-6b38083c6263 | -21.62609 | -45.84283 | 2025-06-14 04:17:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0b219b36-aa75-36be-9dde-9fa523fdf0c0 | -21.19542 | -44.93522 | 2025-06-14 04:17:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e773c9c0-ecb1-381d-913f-bfdc6a2d5b29 | -21.62885 | -45.84716 | 2025-06-14 04:17:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 42ca9fb0-d2a7-3208-af64-b14b531b887f | -19.579 | -49.10343 | 2025-06-14 04:17:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43883158-705d-3e0b-869f-87bb9f2d9bc0 | -17.58004 | -47.49465 | 2025-06-14 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 982cc48a-3784-38a2-8cc8-65cbb0693684 | -17.57772 | -45.38339 | 2025-06-14 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac86c601-901d-3abe-9811-573dda29c6ed | -26.72843 | -50.12471 | 2025-06-14 04:17:00 | NOAA-20 | PAPANDUVA | SANTA CATARINA | Brasil | 4212205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a623b773-b09b-375c-81d9-36f293d17fe4 | -19.9692 | -44.21616 | 2025-06-14 04:17:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a7e2677b-8dc3-3f9f-872f-f2e5c9b5f6d6 | -20.83773 | -45.45299 | 2025-06-14 04:17:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9460d84c-740b-309e-b7ae-087bf8fdd0aa | -21.62116 | -46.92067 | 2025-06-14 04:17:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c40b8b0b-5f40-3b72-a97c-5793d78c0939 | -17.93469 | -52.68928 | 2025-06-14 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13afe302-75b7-322e-a38b-e9be8eebe51a | -18.98168 | -48.37194 | 2025-06-14 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| df34b8b4-035f-33f2-b61d-036ba65eed1e | -20.31216 | -45.58662 | 2025-06-14 04:17:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5741356f-1b0d-3bb2-86c7-6d31574276e9 | -22.50365 | -44.56447 | 2025-06-14 04:17:00 | NOAA-20 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0e6a8762-6643-30c0-8e04-e2119410a5b9 | -23.98085 | -48.9173 | 2025-06-14 04:17:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1c8398a-2d70-3145-8845-39c294b953c9 | -23.62998 | -46.4257 | 2025-06-14 04:17:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0d099ee5-d6c7-3dec-8b88-4a75ce0c589f | -19.88798 | -44.05474 | 2025-06-14 04:17:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 170ef22d-ac3e-3b03-9248-7d1e3e24fd4f | -21.62943 | -45.84341 | 2025-06-14 04:17:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1beace15-fd27-3453-966d-81b4e47bd48a | -20.60864 | -48.86327 | 2025-06-14 04:17:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 468bc6a7-23e8-3b26-99f6-56c78db6d71e | -23.98423 | -48.91796 | 2025-06-14 04:17:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc5b76cc-d0b6-3baf-90df-9b3e95d0ef9d | -29.73863 | -51.26677 | 2025-06-14 04:17:00 | NOAA-20 | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| bb959231-c576-3fbd-839a-ceffc73be3a9 | -16.78464 | -49.11795 | 2025-06-14 04:17:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f80389e4-1136-3f5f-8037-4ce1ba0f0633 | -17.61157 | -46.68472 | 2025-06-14 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c6bdaf27-f1f0-3588-ba62-ace8e3680f1a | -19.89142 | -44.05531 | 2025-06-14 04:17:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c457a0b-5656-378e-9212-ca9552ad9ed9 | -23.59445 | -47.437 | 2025-06-14 04:17:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e72f1acd-5e3e-355a-ae19-e211e7675d4c | -18.21273 | -47.63847 | 2025-06-14 04:17:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a08cd353-2ead-38db-995e-706cca6f78a1 | -22.54018 | -48.81129 | 2025-06-14 04:17:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 569455c7-03d6-39d0-8b04-e949f4bcdb55 | -17.58067 | -47.49084 | 2025-06-14 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 560e07c5-7324-3152-a372-aa2cdc76583b | -21.40286 | -44.27286 | 2025-06-14 04:17:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d2574665-7456-3301-ba6a-504e0df6d3d3 | -22.67539 | -47.29647 | 2025-06-14 04:17:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9385c618-e544-39ca-b2a9-880a90d22523 | -19.7721 | -44.15452 | 2025-06-14 04:17:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2789c7c9-1eb4-34b2-98dc-5015086e86d8 | -17.75796 | -52.4295 | 2025-06-14 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f14bddfe-89bc-3881-85c4-36d1b45df49a | -22.85739 | -42.98217 | 2025-06-14 04:17:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b0f6c770-0414-3fad-a3c0-b24aae5d7950 | -19.43723 | -44.34026 | 2025-06-14 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 538cee4f-36b5-3b66-8274-e07208751b59 | -22.83567 | -47.22945 | 2025-06-14 04:17:00 | NOAA-20 | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e5a6413a-6677-3b9a-a21f-a99b88cb9f09 | -23.3388 | -46.77301 | 2025-06-14 04:17:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| adf9fb47-206d-35fc-97cd-5a25922f2175 | -22.35307 | -41.99786 | 2025-06-14 04:17:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9de17a84-b1a0-307d-8861-81d9b42ab445 | -17.38391 | -53.8223 | 2025-06-14 04:17:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 815e9cf0-a061-3bb2-b979-71eca8d4bec0 | -19.45251 | -45.30678 | 2025-06-14 04:17:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36980f9c-8204-35c3-b1be-1d1c91410056 | -19.5127 | -44.27754 | 2025-06-14 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc183959-1afb-3f87-9953-55d2320cc72c | -22.78609 | -43.75665 | 2025-06-14 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a9647098-eb30-3a4a-a72c-69386b4a32f4 | -17.75044 | -42.89453 | 2025-06-14 04:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 283c5451-313a-3eec-808d-8d9040341b08 | -30.14916 | -52.0229 | 2025-06-14 04:19:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| dcb06cc0-72bc-37d0-b776-886201061c9c | -25.19117 | -49.32664 | 2025-06-14 04:19:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e2b48038-46f3-39c6-9f09-456c5584d2af | -30.15141 | -52.02627 | 2025-06-14 04:19:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 788c351e-aea4-3398-a7b1-67ce2c523c34 | -14.2121 | -57.4098 | 2025-06-14 04:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ec079c37-2dcf-3ebf-82be-d40992be76c4 | -6.9605 | -42.8816 | 2025-06-14 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 1230b5df-bff1-3fd1-b188-9ed1dcd50735 | -13.9062 | -54.6084 | 2025-06-14 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 288bf3be-f8af-3eb7-a2ec-527ebb65de71 | -10.9353 | -56.8522 | 2025-06-14 04:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| e380a478-4f8d-3418-a499-5b987e992683 | -10.9355 | -56.8322 | 2025-06-14 04:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 86d30621-f9f9-361f-a3c6-791f0b5fc7e0 | -6.9602 | -42.9052 | 2025-06-14 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| fef919fa-b894-3f47-8fe9-f7c8d0412130 | -10.9355 | -56.8322 | 2025-06-14 04:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 125bf8f9-4dff-32c8-8ff5-9f8ff532026c | -6.9605 | -42.8816 | 2025-06-14 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| aefeaeae-33a2-3400-ae8d-b6f59c23989a | -14.2121 | -57.4098 | 2025-06-14 04:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b1c59fef-23da-3008-8c9d-fcc500a80ede | -6.9602 | -42.9052 | 2025-06-14 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 5d3a9b67-010c-3f5b-835d-94c5643927e2 | -13.9062 | -54.6084 | 2025-06-14 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| bae13dba-b4ef-3872-89a7-25a15c295491 | -10.9353 | -56.8522 | 2025-06-14 04:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 7c0c234f-5800-3c8a-af27-e2f0934a35b3 | -6.9605 | -42.8816 | 2025-06-14 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 269f9e8e-ecdb-36ca-b365-a4d4c5b0ea0c | -10.9355 | -56.8322 | 2025-06-14 04:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 977bd8d0-eb47-3fab-b630-e34d90797cb5 | -13.9062 | -54.6084 | 2025-06-14 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| f239d275-f078-36b4-821a-7c65cc645d89 | -6.9602 | -42.9052 | 2025-06-14 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 1dae40df-3d76-3f94-b94f-f78f918a5499 | -13.887 | -54.6106 | 2025-06-14 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| e51f5f51-67f8-3089-83c3-cbf68b3fbe8d | -14.2121 | -57.4098 | 2025-06-14 04:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 30e74a40-e476-395e-8ba4-35f53d18bcd0 | -6.9416 | -42.8834 | 2025-06-14 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 923f7776-202d-373c-b8dc-b4a673f6c82c | -10.9355 | -56.8322 | 2025-06-14 04:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| beed8bbb-3aa9-3f85-b772-56b01e44f00d | -6.9602 | -42.9052 | 2025-06-14 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| a5caece7-dab5-3ed0-9629-e376fac3cccc | -6.9605 | -42.8816 | 2025-06-14 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| b9a2532f-47ed-3300-81e2-a2ee4a55eb05 | -13.9062 | -54.6084 | 2025-06-14 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 2539c9f4-5fc4-3b75-9313-0af41a3e5a8d | -14.2121 | -57.4098 | 2025-06-14 04:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| e43107ee-d58d-3c50-b9b9-012f2cddf74b | -13.887 | -54.6106 | 2025-06-14 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 0ab835e9-6d08-3c54-9e01-05537a1b7893 | -6.9605 | -42.8816 | 2025-06-14 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| d0e71292-d2a9-394f-89cd-d39c3c3e15db | -14.2121 | -57.4098 | 2025-06-14 05:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 2bbad536-1225-334f-a21b-6b1f6ac1e467 | -10.9355 | -56.8322 | 2025-06-14 05:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 39bec64b-bb82-323b-a59c-d6b1d414bee0 | -6.9416 | -42.8834 | 2025-06-14 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 19b9fa9e-b3f6-39d1-9152-3bb87ca61828 | -6.9602 | -42.9052 | 2025-06-14 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 6c1f6a63-f707-3d78-8277-3502ef6d2c08 | -9.55866 | -46.76542 | 2025-06-14 05:04:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff8590b8-0aaf-3439-9ee2-772984f18c90 | -9.53563 | -46.30208 | 2025-06-14 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 169fb954-9fb7-3ade-82ab-fecb2a6449a6 | -8.20814 | -42.84209 | 2025-06-14 05:04:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 642ca663-edaa-38b8-945b-d4437a9891b8 | -8.42755 | -49.56046 | 2025-06-14 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c5d0972-2b22-3cbc-afaf-1aa897696e8e | -6.60574 | -43.89245 | 2025-06-14 05:04:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 665b76bb-2a90-3688-a3ee-0c25d74133ea | -6.60433 | -43.90303 | 2025-06-14 05:04:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2a6665ce-47d2-38dd-bdec-c7459f302d67 | -9.41169 | -50.42137 | 2025-06-14 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52abc30f-9b15-3cd3-a087-e02b937d7c42 | -8.07603 | -43.11108 | 2025-06-14 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 663d173b-21f9-304c-95f4-c6db3417e2da | -9.40117 | -48.41412 | 2025-06-14 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93b12afd-b121-3e00-9706-31b241aaacd6 | -9.53617 | -46.29792 | 2025-06-14 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72fbe772-65b8-322f-9772-317bda12d802 | -8.07523 | -43.11749 | 2025-06-14 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 76290fad-a9a4-3294-8e50-d825731b00ee | -9.40957 | -48.42709 | 2025-06-14 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88b1bd20-20a0-3d38-9197-5fd757c6ceee | -8.43207 | -49.56114 | 2025-06-14 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f6ae8f76-25db-31d9-9218-ea954ca662a4 | -7.45522 | -45.50085 | 2025-06-14 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4c67b775-940a-33d8-8e08-c30932b5f7d4 | -2.66425 | -47.39997 | 2025-06-14 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16b39119-bf28-3924-b3ff-2e115ae89971 | -6.21113 | -43.33154 | 2025-06-14 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e2c4ad19-7276-35b7-bb76-d5ed47f9d5c8 | -9.84873 | -44.692 | 2025-06-14 05:04:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db44009f-70a4-3fa6-9aa3-9b0350990610 | -9.86353 | -48.19955 | 2025-06-14 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| feeeef58-0f62-3778-90d8-12c0578658ab | -8.73131 | -47.99556 | 2025-06-14 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dfd6fb9-65fd-34fb-bb99-f60707e8aa80 | -9.84809 | -44.69711 | 2025-06-14 05:04:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README18.md)
