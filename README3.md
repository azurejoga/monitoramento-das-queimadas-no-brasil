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
| bbe8aaf9-9b86-3581-a8d3-a6662f810453 | -6.96592 | -43.56119 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5c69dcfa-2c8b-3cff-a67c-62a8b9924788 | -6.91435 | -43.55485 | 2025-02-04 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e71fc144-e13a-3b6d-964b-5e16ff086710 | -6.94565 | -43.54272 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a0713bb-a2a5-3b4f-a080-9c6b1cfde1bc | -6.96831 | -43.56305 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47e31cfe-2426-3538-89e0-ad8a31156355 | -6.94925 | -43.54328 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7b9e217-d85d-39ce-9e25-5eb07d1407c6 | -6.9725 | -43.5664 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd3290cc-7325-318c-b24a-a0bc1af6381e | -5.1347 | -37.59924 | 2025-02-04 04:25:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3c67200d-b3d5-3661-9221-7aa65fc313cc | -6.96004 | -43.54497 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4975fd2-fc83-38ec-ae48-a93948a6fbca | -6.95519 | -43.55262 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f0da40c-0766-31b1-8b6c-5de44834153d | -6.9577 | -43.53619 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb1b28bc-1727-3d6d-8e9e-4df39941356d | -6.9649 | -43.53729 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| baa91bce-0dc2-35db-b5b8-f98d2f722bac | -8.94097 | -44.24151 | 2025-02-04 04:27:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec4ad421-b108-307d-a0e6-99fa2b01c177 | -10.95257 | -40.73631 | 2025-02-04 04:27:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 279b04e5-9b7e-3c22-a6a6-858e28f6b747 | -9.08239 | -40.25108 | 2025-02-04 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f2bed350-699d-32e5-b294-66be7bbbcf56 | -9.07721 | -40.25499 | 2025-02-04 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 45fe5659-2efb-3fbc-9ac8-b7c9baf97a58 | -13.40913 | -41.33125 | 2025-02-04 04:27:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 433ae921-d0f9-3044-986f-927b08ab8051 | -10.52348 | -42.42538 | 2025-02-04 04:27:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4ed87a9c-e0a0-3e27-9f4b-4695b0c7b3bf | -9.08176 | -40.25566 | 2025-02-04 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5d8dc68b-c87d-33eb-b00d-693a0e12df6a | -13.40755 | -41.32901 | 2025-02-04 04:27:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 81971d5b-6255-3217-bf37-20811d50db69 | -10.5275 | -42.42599 | 2025-02-04 04:27:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2bb7e2f5-80a0-32b0-a418-d5f591676e54 | -15.51877 | -42.6758 | 2025-02-04 04:29:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 75dc3bd6-598c-3b95-aae9-10500b680fe5 | -20.41832 | -43.55194 | 2025-02-04 04:29:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f44f4141-8490-33e1-a890-7705994d3279 | -15.51925 | -42.67205 | 2025-02-04 04:29:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e595abd7-678c-3e09-972a-b60902c9643a | -15.51454 | -42.67507 | 2025-02-04 04:29:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b7b64d3f-b82d-3ccc-9496-1b487fdfb3a3 | -18.04037 | -39.92511 | 2025-02-04 04:29:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d565da60-e1ab-30dc-af04-d2a28e97ca97 | -6.9529 | -43.5617 | 2025-02-04 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 85d46b4a-4a6f-337f-9c08-684ed7da945f | -6.9532 | -43.5384 | 2025-02-04 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 8c63d40b-1c7a-3a69-8daa-bae604d9d6ad | -6.9718 | -43.56 | 2025-02-04 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 3c89d168-6915-3422-b3db-3d8c526fe854 | -6.972 | -43.5366 | 2025-02-04 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 10e93972-5588-3830-9629-19d78ad890d4 | -22.15068 | -56.67538 | 2025-02-04 04:31:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8b15c3b-fd02-37fd-81a5-c7fbe9416874 | -27.15686 | -52.84456 | 2025-02-04 04:31:00 | NPP-375D | GUATAMBÚ | SANTA CATARINA | Brasil | 4206652 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9b2d63c4-03b9-3dca-87cc-1b0cb8e1f2ae | -21.07377 | -56.39272 | 2025-02-04 04:31:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41307a20-e1be-3335-956a-6f73e187f27d | -24.94205 | -52.36179 | 2025-02-04 04:31:00 | NPP-375D | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 59551940-92e3-3ec6-be2e-b80f39edb558 | -22.19985 | -56.31527 | 2025-02-04 04:31:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2e20769-5641-3cb7-a82f-1b1deebdc1b7 | -27.15753 | -52.84056 | 2025-02-04 04:31:00 | NPP-375D | GUATAMBÚ | SANTA CATARINA | Brasil | 4206652 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fbfb61f4-0076-363e-b478-14acbc1c3408 | -21.07295 | -56.3949 | 2025-02-04 04:31:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbf1c1b2-04c1-3028-94ba-c7fc60cabc24 | -19.88897 | -55.07463 | 2025-02-04 04:31:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3a2454f-d12f-3bc6-8ea0-93646bb041af | -22.67554 | -42.85447 | 2025-02-04 04:31:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 824cf2cd-26f6-36ca-9f80-415c65ab89d3 | -32.53241 | -53.34575 | 2025-02-04 04:33:00 | NPP-375D | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 317d67d8-b980-3619-ab26-50e0c29d7849 | -29.95129 | -51.61518 | 2025-02-04 04:33:00 | NPP-375D | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| b081cf34-072d-33cd-8e26-b7845c3917d0 | -28.6666 | -49.31119 | 2025-02-04 04:33:00 | NPP-375D | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4ccdd89b-604c-31c2-9f93-6e73341f2e4f | -28.66648 | -49.30877 | 2025-02-04 04:33:00 | NPP-375D | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5c172ec3-279f-33f5-9158-5b07e5760b28 | -6.9718 | -43.56 | 2025-02-04 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c5d67fec-db26-3863-990e-b0a20e41b9a2 | -6.972 | -43.5366 | 2025-02-04 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8c2070cb-3b69-31a9-91ea-cbbc22412a16 | -6.9532 | -43.5384 | 2025-02-04 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 173.8 |
| f6f1aeaa-5698-3950-9286-4f8c866ba659 | -6.9529 | -43.5617 | 2025-02-04 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| d8b75c14-5a91-3711-bb40-0ed206bf5663 | -6.9535 | -43.515 | 2025-02-04 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 986f2b8a-9ab8-39e2-ba87-abb939aa2802 | 2.24112 | -60.22348 | 2025-02-04 04:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97738494-21b5-37fa-b380-1aa2cc9a12ba | 3.0661 | -60.30864 | 2025-02-04 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c37b740d-54b7-3e84-b4b0-0cf5297964c2 | 3.07038 | -60.30767 | 2025-02-04 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6943b52-3607-362a-8d95-74a0076e7b3a | 3.07168 | -60.30781 | 2025-02-04 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e62b21e9-07c8-3fe8-8e82-13028a930668 | 3.06534 | -60.31223 | 2025-02-04 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99f4857f-8775-32ee-9bbb-6475e562e5d5 | 2.23564 | -60.2243 | 2025-02-04 04:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d051fbd1-51f0-3cc6-b360-b8bfbe375ac0 | 2.24059 | -60.21996 | 2025-02-04 04:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3067cf4-230b-3151-9ce0-44fa351cb7ae | -6.9532 | -43.5384 | 2025-02-04 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| fc306e06-0e7a-33c1-afae-401f75fa2212 | -6.96533 | -43.56647 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 32a6a365-a9c8-3921-bccc-32b1566c1d12 | -6.95115 | -43.52983 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74ab0217-67a7-3c04-9a17-d934b3617168 | -6.96469 | -43.51071 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f961541b-cf7e-3bfe-a036-0f36fa91c12f | -6.95607 | -43.53402 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62a4b865-2e1d-3271-b1e5-ea844e7678d4 | -6.9526 | -43.54038 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| f91c6c5a-cf37-32ea-b0de-8d9620122c21 | -2.86719 | -54.10402 | 2025-02-04 04:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13b74807-76f5-3e98-b762-bb1618680084 | -6.96485 | -43.56988 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 02fb809d-9dad-3db4-9f3f-18fad5d2dbc8 | -6.95404 | -43.53025 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ece9ae4e-7c97-3946-85da-6a0ee38e425b | -6.95653 | -43.53059 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35d61e7e-cc43-3bd5-b651-2c5cdbb27843 | -6.96716 | -43.57368 | 2025-02-04 04:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc7a6738-2b3b-3ca8-99ec-a6cc5798576c | -6.96675 | -43.51802 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 140e35b0-0b40-317f-81b0-302215f8b627 | -6.95117 | -43.55049 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e438e3c3-aa4a-3447-b788-ff3faf5b397b | -6.94935 | -43.54331 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 05fe9230-c0f8-340a-96ed-04bf358098cf | -6.95893 | -43.53442 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e66c63a1-df34-3a29-a411-2e348da5bd43 | -6.95356 | -43.53366 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0e8e2ec-7ec0-308f-a763-beb4bc375d20 | -6.95427 | -43.5475 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 960b44a2-d900-380f-b109-d22c99b929b5 | -6.95308 | -43.53704 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 799823c3-566b-3821-ba12-a7f472bd0637 | -6.9575 | -43.54455 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ba9c7909-5b6f-375f-84a3-af075134e515 | -6.96422 | -43.51417 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be170ebc-8880-3954-aaf5-fca54e5948e3 | -6.96045 | -43.56234 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ec0389e-a953-34ef-a1a8-4719b3bf3fba | -6.96008 | -43.54499 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db476d83-3ffd-3fdb-b8cd-4c2d318351dc | -6.96725 | -43.51457 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a026b5b4-fbba-3d9c-b0f2-29d6696790bb | -6.96317 | -43.56277 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 408677fd-585e-3003-8f1b-87e50f16abf2 | -6.96762 | -43.57033 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4bc4cb89-32e7-3b6c-a506-30b3a57aa924 | -6.94844 | -43.55008 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3942117-bea7-3972-b31a-4e27fe46cdd2 | -6.95702 | -43.54792 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 227e3797-4028-3e7c-b942-8393dbc5c0b4 | -6.95165 | -43.54709 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f9749173-cc98-37e8-ab3d-870f4298bc56 | -6.95997 | -43.56572 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0e680941-c6bc-396c-afa8-a71779e38242 | -6.95797 | -43.5412 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a2a58629-a30f-3f86-b606-08199d9fa068 | -10.52579 | -42.42483 | 2025-02-04 04:50:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4f2f7467-0125-3dce-be92-ee384102a339 | -6.95734 | -43.56538 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 42852dc7-d5af-3639-9bf3-903a367a86de | -6.95213 | -43.54372 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c808f6ea-7c93-3624-b9f9-b86c063492eb | -6.96225 | -43.56958 | 2025-02-04 04:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3bb82520-827d-31fa-8d50-f21efbc62ba4 | -9.08228 | -40.25589 | 2025-02-04 04:50:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 698d49b4-0eff-3371-a774-5df6ef499756 | -6.95472 | -43.54412 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 71d91a84-75ab-3a9e-85d4-a9448b1b73b4 | -6.94771 | -43.53618 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ff5facd-80af-31c9-bb74-75f208963d82 | -6.95562 | -43.53743 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 613137b4-ed36-318e-9695-6b56510159d5 | -9.07547 | -40.25494 | 2025-02-04 04:50:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dcd9728f-2f7b-3940-ad00-a1551a6708af | -6.96437 | -43.57321 | 2025-02-04 04:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 80d8efa5-7870-3923-bfe2-2fdce375b01c | -6.94819 | -43.53284 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 713fc043-46b9-3fa6-816e-b2d810026603 | -6.9618 | -43.57291 | 2025-02-04 04:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 488f6771-fe98-307d-80fe-1926022d6b60 | -6.94676 | -43.54292 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 619795ab-a266-3003-9a34-5a085bf372c8 | -6.95949 | -43.56909 | 2025-02-04 04:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82d53a30-5a96-3181-bb54-30dce204f2c6 | -6.96808 | -43.56691 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 98f9af60-2cfa-355a-b590-e2f33dfa5321 | -6.94724 | -43.53954 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README4.md)
