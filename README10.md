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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4241484f-d59e-3fc0-b9b2-2f15358a527a | -8.60019 | -48.01688 | 2026-07-08 04:06:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ac1e695-7a6e-35c0-bded-407c31fb4a1d | -5.47083 | -45.42299 | 2026-07-08 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4f036f2-5115-35e0-a677-6cfc02e58fb9 | -9.30815 | -51.92117 | 2026-07-08 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffe54938-3ebb-3140-b954-477ab700503f | -5.34362 | -45.3517 | 2026-07-08 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c65db3cd-29e4-3a77-9ce2-12de0154ea24 | -6.93189 | -43.7058 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7698fb2-add3-314a-95f2-7714e5ed62af | -6.91457 | -43.71006 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c08bfdd-91fd-3429-a2fc-7dc5cb69d437 | -6.91919 | -43.70723 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9e89c75-73e8-399f-a6ce-302b53a8a00c | -9.23563 | -50.14321 | 2026-07-08 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b60084a-8871-30ab-b180-f0fbcdbdf2fe | -9.33492 | -47.91886 | 2026-07-08 04:06:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 016065eb-d4e3-3491-8b75-fa0d1d64c702 | -7.66001 | -40.11121 | 2026-07-08 04:06:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b93454e5-ea1a-37cd-8802-f8d0d61107a5 | -5.66829 | -44.30735 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45c62ba8-d8a8-3b02-a216-fdadb077d42b | -8.59556 | -48.01258 | 2026-07-08 04:06:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4fe05b5-afb4-3d8e-ab5b-48308e5aec29 | -9.73558 | -49.03826 | 2026-07-08 04:06:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d224d7f-e288-3790-b6fc-0d6b3cb494c9 | -8.44627 | -45.82816 | 2026-07-08 04:06:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6eb19f5-6a13-391f-8b7b-b78ed6dc5699 | -6.93996 | -43.70721 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 426e37c0-9f0c-3272-bf94-d36fc96d7082 | -11.07395 | -45.67654 | 2026-07-08 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a504376e-dd09-3677-91c4-e576f249771b | -5.30699 | -47.24658 | 2026-07-08 04:06:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5849a8ea-3c3d-37ff-8b12-30d4184d13e8 | -9.33549 | -47.91582 | 2026-07-08 04:06:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef548933-4a51-3808-9a7c-0ecde2b6c4e4 | -10.89454 | -44.31619 | 2026-07-08 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 155ae4f8-5d21-370d-a8a4-cfec8ee027c9 | -6.94055 | -43.70369 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37f4b52d-14eb-3dc2-9e59-0f5c14a4f40e | -4.94067 | -48.24873 | 2026-07-08 04:06:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de43a02f-3ebc-3632-adf0-5ad59b5f3854 | -10.93195 | -43.05967 | 2026-07-08 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fb291b1-b467-3bc7-945e-1fe79eb80f04 | -8.12573 | -47.09974 | 2026-07-08 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23ee3a01-a305-3a19-a2c7-ff628a14c500 | -6.92785 | -43.70511 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b04f662-74a6-3157-8545-9f901efffd45 | -9.23103 | -50.14917 | 2026-07-08 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe3946bf-05d3-38fb-aa40-08c2be70f4c6 | -6.92323 | -43.70793 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f13fd669-09be-3674-b0b6-e336f7b63762 | -7.63945 | -50.02283 | 2026-07-08 04:06:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e4ddceaf-d69f-3da4-aab1-556000251a0f | -5.80122 | -43.80419 | 2026-07-08 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4dc4956-2077-36f4-ada8-4ac0e3cd3d2c | -6.91338 | -43.71716 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d82740b-898f-3255-aaf1-574da46cc375 | -9.22519 | -48.58083 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 926502c5-2ab7-3989-a767-b7707d3829b6 | -6.7122 | -40.00793 | 2026-07-08 04:06:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1cfe9994-0f3b-3bbf-9677-8c030b475ac6 | -6.92902 | -43.69812 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74611866-5bc2-3ec3-a0ad-8e7936fb7581 | -5.83102 | -43.47663 | 2026-07-08 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1e33eb6-83d0-38c0-a2cd-cb796df98032 | -5.47245 | -45.42654 | 2026-07-08 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e08d8754-f110-37d8-a003-3a40fb49d699 | -9.21986 | -48.57951 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b949a2aa-dadc-3c39-8f37-64fb82b69d46 | -8.12968 | -47.10633 | 2026-07-08 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f6bd4f8-5e8f-31ba-b76c-cac22e4f17e8 | -6.49299 | -43.62038 | 2026-07-08 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96451dfd-2dc9-3d19-911b-bbdbe4b3e591 | -9.30435 | -51.91938 | 2026-07-08 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e35e7d7-9d2d-3798-a936-ca0833e2abe9 | -9.2214 | -48.57927 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 80f80e88-2c51-30a7-bdaa-b3483f9479f2 | -9.22397 | -48.58757 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d35bb13d-6d85-3eb8-9b3c-7c9894fc228f | -9.22671 | -48.58065 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 42629102-8bd1-3caa-8135-19d3d593b031 | -9.37257 | -44.72806 | 2026-07-08 04:06:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6ba2899-34b3-3630-a1fc-37af85225a8b | -6.94574 | -43.6974 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d4627c9-e7f9-3b36-a003-1cacf9812e65 | -5.79619 | -43.6332 | 2026-07-08 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dcb7ef9-326c-325d-b01b-69d8dba12cf3 | -11.69553 | -44.14156 | 2026-07-08 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cae82b1e-af43-3945-8bc3-73c931d7423d | -6.90648 | -43.70869 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65fcce90-8083-3273-b91b-cded3d7e4f93 | -6.91742 | -43.71785 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb602fdb-cbb2-3aa7-8ee1-6225c2194ed2 | -6.94399 | -43.70794 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7587fc5-4ddf-3707-bce5-629e14c6b8a4 | -9.21943 | -48.58968 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 635624c1-d3ee-3112-8216-905f9003f8e0 | -9.21402 | -48.5888 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e59dbfc1-acc6-3538-81f7-57327c8f4e2d | -6.93247 | -43.7023 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0aa35029-bf74-3e50-9303-1babc4896d01 | -9.22608 | -48.58398 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ebd1563a-7829-3e89-80d1-82364c216219 | -6.64785 | -43.91041 | 2026-07-08 04:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 160b282f-1c51-365e-bf63-3d324101740b | -6.94516 | -43.70091 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ecda7623-fb63-3223-8757-f78ce6e250af | -5.83043 | -43.48016 | 2026-07-08 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbf65fb8-91ec-30fa-b2f7-589975ce9b9f | -11.70023 | -44.13739 | 2026-07-08 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 057613bd-b768-325b-9b44-82728a443e8e | -6.91801 | -43.71429 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9147368-8db6-3a89-9ba2-f8a80f887bf8 | -6.9186 | -43.71075 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e731538-6760-35ff-bf69-73a6d225a392 | -5.4678 | -45.4258 | 2026-07-08 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a6e3877-4ad9-3cf1-901c-0b679b351c2e | -9.33607 | -47.91279 | 2026-07-08 04:06:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46ee700d-2479-366c-8373-335563f12d05 | -11.12167 | -38.62753 | 2026-07-08 04:06:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 780b16c9-8f90-3f6a-9b57-e3fa7f6cdd93 | -7.25535 | -45.10579 | 2026-07-08 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d5a27da-e8a1-30e4-a8f1-cd5d8ec7d676 | -6.9449 | -43.70535 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8377e593-284c-3ad2-bb41-a2627fd208e8 | -11.69938 | -44.14226 | 2026-07-08 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cedab033-055d-37cf-a23e-a7b386dda9e6 | -6.02654 | -46.7307 | 2026-07-08 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e39b574c-38fc-39c0-a5f2-b589a389dd4b | -10.94514 | -43.04853 | 2026-07-08 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0bf9cd1b-eb5a-39a8-a88a-8df56a0441b3 | -5.66246 | -44.30379 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c9c1c52-3216-3e23-ba69-bc51ca4594e3 | -6.93534 | -43.71003 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8469ec0a-971e-34e3-a8c3-31810e4029c2 | -9.31108 | -51.92002 | 2026-07-08 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f1de049-1b59-38c4-8ff0-f7580693df40 | -7.8989 | -48.25799 | 2026-07-08 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1131a03c-c7b4-3cc1-997d-cd999ca1046a | -8.13071 | -47.10058 | 2026-07-08 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d3325ec6-a322-3700-a5c1-73ca8fec016e | -9.30145 | -51.92033 | 2026-07-08 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdcda4d9-b4a1-3a9f-877f-2e34b2dbc15c | -11.69637 | -44.13668 | 2026-07-08 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e898f2dc-afdb-37a9-a383-53c211a6d525 | -5.6604 | -44.30191 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9860cd38-ab09-355a-8b0c-90a85fce9720 | -6.94551 | -43.70185 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 332b9302-7d99-3076-a05f-d17c43f2bbf8 | -9.74108 | -49.03926 | 2026-07-08 04:06:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b14f6fff-72c6-3ea1-9b89-52612147852f | -11.4101 | -38.09514 | 2026-07-08 04:06:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 32fbe256-1a63-37a8-9276-28710fc2a2d2 | -5.66537 | -44.29869 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dad36c9-1991-3471-a4be-d386ebe6feab | -6.92844 | -43.70161 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 924a5472-8f77-36a6-a6cb-e86e6280f821 | -10.92534 | -43.05402 | 2026-07-08 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0f1756da-b42a-3191-a407-f9a95fae1e92 | -9.37294 | -44.71725 | 2026-07-08 04:06:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55016f4b-6612-3626-9306-e6e254a1e383 | -10.76493 | -45.03048 | 2026-07-08 04:06:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7645899-789a-3433-8099-f809ff143026 | -8.59616 | -48.00935 | 2026-07-08 04:06:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9f94da8-5332-3e99-9c99-9ecec0f35305 | -6.02603 | -46.7336 | 2026-07-08 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98415a2d-1165-3ccd-bc49-8a92a24c6122 | -10.94369 | -43.05724 | 2026-07-08 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 578a9e0d-9c6f-3967-8bc9-bbf41ed3b6db | -10.94735 | -43.05789 | 2026-07-08 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 62fb3be8-9c6b-3910-bae5-61958cf469c2 | -9.22458 | -48.58418 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 016ae953-cf53-3770-b9cc-d03df5a68e3a | -6.93709 | -43.6995 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2b6184c-2adb-33de-942e-2bba304d5108 | -10.92461 | -43.05838 | 2026-07-08 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad8a21b4-8620-33b0-9780-bd416c1b96b6 | -5.66048 | -44.31578 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5eceb31b-800a-3e7c-951d-d340f2d27450 | -9.37389 | -44.7206 | 2026-07-08 04:06:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb9133bd-2463-33ec-8002-1bcf95fc53f6 | -5.79708 | -43.80353 | 2026-07-08 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f4dbf88-57e8-373d-82db-7d6a79b1102e | -9.23783 | -50.14591 | 2026-07-08 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 505a6fc2-bf72-330b-a2a0-e11463e0322f | -5.46997 | -45.42791 | 2026-07-08 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3001d32e-1857-337e-9425-548438bcdeb3 | -10.94148 | -43.04788 | 2026-07-08 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6e9f482c-c0c4-380a-87d9-5b2573568408 | -8.73399 | -49.44781 | 2026-07-08 04:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 89661a8b-9a1a-381f-b15d-5576d583c8cc | -10.03117 | -49.62712 | 2026-07-08 04:06:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3dc48837-0723-3088-b13f-8f416fb0407c | -5.664 | -44.30663 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 46f9ff5a-9ff2-3cee-920e-746d15955c19 | -5.66332 | -44.31061 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ef0594ff-8b53-39c9-a4c1-c7889c63ed02 | -10.30043 | -40.72411 | 2026-07-08 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README11.md)
